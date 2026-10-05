#!/usr/bin/env python3
"""Build pentru site-ul static XpertPoint.

Rulează înainte de fiecare commit (din folderul Website-Site):

    python3 tools/build.py

Ce face, pe toate paginile din PAGES:
  * pune header-ul comun (partials/header.html) între <!-- SITE-HEADER:START/END -->
    și marchează linkul paginii curente cu aria-current="page";
  * pune footer-ul comun + bara de acțiune mobil între <!-- SITE-FOOTER:START/END -->;
  * pune bannerul de cookie-uri + tracking între <!-- CONSENT:START/END --> (doar paginile noi,
    cele vechi îl au deja inline);
  * pune breadcrumbs vizibile între <!-- BREADCRUMB:START/END -->;
  * generează schema JSON-LD (@graph: LocalBusiness + WebSite + WebPage + BreadcrumbList
    + Service/Offer) între <!-- SCHEMA:START/END -->;
  * generează tabelele de prețuri din tools/preturi.json în preturi.html și în paginile
    care au <!-- PRICE-GROUP:<id>:START/END --> (id = o categorie din preturi.json);
  * generează FAQPage din întrebările vizibile între <!-- FAQ-SCHEMA:START/END -->;
  * rescrie sitemap.xml.

Fișierele se rescriu doar dacă s-a schimbat ceva. Nu are dependențe externe.
"""
import hashlib
import html
import json
import re
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BASE = 'https://www.xpertpoint.ro'
BLOG = 'https://xpertpoint.ro/blog/'
OG_IMAGE = 'https://images.unsplash.com/photo-1485965120184-e220f721d03e?w=1200&q=80&auto=format&fit=crop'

BIKE_HUB = ('Service biciclete', '/service-biciclete-bucuresti.html')

# crumbs: lista (nume, url) fără „Acasă" (se adaugă automat); ultimul element e pagina curentă.
PAGES = {
    'index.html': dict(url='/', name='Service biciclete și espressoare București', type='WebPage', priority='1.0'),
    'service-biciclete-bucuresti.html': dict(name='Service biciclete', crumbs=[BIKE_HUB], service='bike', priority='0.9'),
    'service-espressoare-bucuresti.html': dict(name='Service espressoare', crumbs=[('Service espressoare', '/service-espressoare-bucuresti.html')], service='coffee', priority='0.9'),
    'revizie-bicicleta-electrica-bucuresti.html': dict(name='Revizie bicicletă electrică', crumbs=[BIKE_HUB, ('Revizie bicicletă electrică', None)], service='ebike', priority='0.8'),
    'reparatii-frane-bicicleta-bucuresti.html': dict(name='Reparații frâne bicicletă', crumbs=[BIKE_HUB, ('Reparații frâne', None)], service='frane', priority='0.8'),
    'preturi.html': dict(name='Prețuri', crumbs=[('Prețuri', None)], service='catalog', priority='0.9', consent=True),
    'despre-noi.html': dict(name='Despre noi', crumbs=[('Despre noi', None)], type='AboutPage', priority='0.6', consent=True),
    'contact.html': dict(name='Contact', crumbs=[('Contact', None)], type='ContactPage', priority='0.7', consent=True),
    'programeaza-te.html': dict(name='Programează-te', crumbs=[('Programează-te', None)], priority='0.7'),
    'privacy-policy.html': dict(name='Politică de confidențialitate', sitemap=False, schema=False, consent=True),
    'terms.html': dict(name='Termeni și condiții', sitemap=False, schema=False, consent=True),
    '404.html': dict(name='Pagina nu există', sitemap=False, schema=False, consent=True),
}
for _f in ('revizie-bicicleta-electrica-bucuresti.html', 'reparatii-frane-bicicleta-bucuresti.html'):
    PAGES[_f]['consent'] = True

SERVICES = {
    'bike': dict(name='Service și reparații biciclete', type='Service biciclete', groups=['bici-revizii']),
    'ebike': dict(name='Revizie bicicletă electrică', type='Revizie bicicletă electrică', groups=['bici-revizii', 'bici-ebike']),
    'frane': dict(name='Reparații și service frâne bicicletă', type='Reparații frâne bicicletă', groups=['bici-frane']),
    'coffee': dict(name='Service și reparații espressoare', type='Service espressoare', groups=['cafea-pachete', 'cafea-servicii']),
}

AREA_SERVED = ['București', 'Sector 6', 'Regie', 'Crângași', 'Belvedere', 'Drumul Taberei', 'Militari', 'Giulești', 'Ilfov']


def page_url(fname):
    return BASE + PAGES[fname].get('url', '/' + fname)


def load_prices():
    return json.loads((ROOT / 'tools' / 'preturi.json').read_text(encoding='utf-8'))


def all_groups(prices):
    return {g['id']: g for key in ('biciclete', 'espressoare') for g in prices[key]}


def fmt_price(item):
    if item['price'] is None:
        return 'În pregătire'
    if item['price'] == 0:
        return 'Gratuit'
    txt = ('de la ' if item.get('from') else '') + f"{item['price']} lei"
    if item.get('unit'):
        txt += ' ' + item['unit']
    return txt


# ---------------------------------------------------------------- schema

def business():
    return {
        '@type': 'LocalBusiness',
        '@id': BASE + '/#business',
        'name': 'XpertPoint',
        'legalName': 'XpertPoint SRL',
        'url': BASE + '/',
        'logo': BASE + '/apple-touch-icon.png',
        'image': OG_IMAGE,
        'description': 'Atelier de service pentru biciclete și espressoare în București, Sector 6: revizii și reparații biciclete, '
                       'revizie biciclete electrice și reparații frâne, plus service pentru espressoare De\'Longhi și Philips. '
                       'Diagnostic gratuit, deviz înainte de lucru și garanție.',
        'foundingDate': '2013',
        'telephone': '+40773565576',
        'email': 'hello@xpertpoint.ro',
        'priceRange': '$$',
        'currenciesAccepted': 'RON',
        'paymentAccepted': 'Numerar, card',
        'address': {
            '@type': 'PostalAddress',
            'streetAddress': 'Strada General Petre Popovăț 9',
            'addressLocality': 'București',
            'addressRegion': 'Sector 6',
            'postalCode': '060314',
            'addressCountry': 'RO',
        },
        'geo': {'@type': 'GeoCoordinates', 'latitude': 44.4511992, 'longitude': 26.0472499},
        'hasMap': 'https://maps.app.goo.gl/LRug4v5BZkffBh4p6',
        'openingHoursSpecification': [
            {'@type': 'OpeningHoursSpecification', 'dayOfWeek': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'], 'opens': '10:00', 'closes': '19:00'},
            {'@type': 'OpeningHoursSpecification', 'dayOfWeek': ['Saturday'], 'opens': '10:00', 'closes': '14:00'},
        ],
        'areaServed': [{'@type': 'Place', 'name': a} for a in AREA_SERVED],
        'knowsAbout': ['Service biciclete', 'Revizie bicicletă', 'Revizie bicicletă electrică', 'Frâne hidraulice',
                       'Service espressoare DeLonghi', 'Service espressoare Philips', 'Decalcifiere espressor', 'Reparații aparate de cafea'],
        'sameAs': [
            'https://www.facebook.com/profile.php?id=61591523255375',
            'https://www.instagram.com/xpertpoint.ro/',
            'https://www.tiktok.com/@xpertpoint.ro',
            'https://maps.app.goo.gl/LRug4v5BZkffBh4p6',
        ],
    }


def offer(item, url):
    o = {
        '@type': 'Offer',
        'name': item['name'],
        'price': str(item['price']),
        'priceCurrency': 'RON',
        'itemOffered': {'@type': 'Service', 'name': item['name']},
        'url': url,
    }
    desc = ' · '.join(x for x in (('de la ' if item.get('from') else '') + (item.get('unit') or '').strip(), item.get('note', '')) if x.strip())
    if desc:
        o['description'] = desc
    return o


def service_node(key, fname, groups):
    cfg = SERVICES[key]
    url = page_url(fname)
    catalog = []
    for gid in cfg['groups']:
        g = groups[gid]
        offers = [offer(i, BASE + '/preturi.html#' + gid) for i in g['items'] if i['price'] is not None]
        if offers:
            catalog.append({'@type': 'OfferCatalog', 'name': g['title'], 'itemListElement': offers})
    node = {
        '@type': 'Service',
        '@id': url + '#service',
        'name': cfg['name'],
        'serviceType': cfg['type'],
        'url': url,
        'provider': {'@id': BASE + '/#business'},
        'areaServed': {'@type': 'City', 'name': 'București'},
    }
    if catalog:
        node['hasOfferCatalog'] = catalog[0] if len(catalog) == 1 else {'@type': 'OfferCatalog', 'name': cfg['name'], 'itemListElement': catalog}
    return node


def catalog_node(fname, prices):
    url = page_url(fname)

    def section(key, title):
        groups = []
        for g in prices[key]:
            offers = [offer(i, url + '#' + g['id']) for i in g['items'] if i['price'] is not None]
            if offers:
                groups.append({'@type': 'OfferCatalog', 'name': g['title'], 'itemListElement': offers})
        return {'@type': 'OfferCatalog', 'name': title, 'itemListElement': groups}
    return {
        '@type': 'OfferCatalog',
        '@id': url + '#catalog',
        'name': 'Listă de prețuri XpertPoint — service biciclete și espressoare',
        'itemListElement': [section('biciclete', 'Service biciclete'), section('espressoare', 'Service espressoare')],
    }


def crumbs_full(fname):
    cfg = PAGES[fname]
    items = [('Acasă', '/')]
    for name, url in cfg.get('crumbs', []):
        items.append((name, url))
    # ultimul element = pagina curentă
    items[-1] = (items[-1][0], cfg.get('url', '/' + fname))
    return items


def schema(fname, prices, title, description):
    cfg = PAGES[fname]
    url = page_url(fname)
    webpage = {
        '@type': cfg.get('type', 'WebPage'),
        '@id': url + '#webpage',
        'url': url,
        'name': title,
        'inLanguage': 'ro-RO',
        'isPartOf': {'@id': BASE + '/#website'},
        'about': {'@id': BASE + '/#business'},
    }
    if description:
        webpage['description'] = description
    graph = [business(),
             {'@type': 'WebSite', '@id': BASE + '/#website', 'url': BASE + '/', 'name': 'XpertPoint', 'inLanguage': 'ro-RO',
              'publisher': {'@id': BASE + '/#business'}},
             webpage]
    if cfg.get('crumbs'):
        webpage['breadcrumb'] = {'@id': url + '#breadcrumb'}
        graph.append({'@type': 'BreadcrumbList', '@id': url + '#breadcrumb', 'itemListElement': [
            {'@type': 'ListItem', 'position': i + 1, 'name': n, 'item': BASE + u}
            for i, (n, u) in enumerate(crumbs_full(fname))]})
    svc = cfg.get('service')
    if svc == 'catalog':
        graph.append(catalog_node(fname, prices))
        webpage['mainEntity'] = {'@id': url + '#catalog'}
    elif svc:
        graph.append(service_node(svc, fname, all_groups(prices)))
        webpage['mainEntity'] = {'@id': url + '#service'}
    data = {'@context': 'https://schema.org', '@graph': graph}
    return '<script type="application/ld+json">\n' + json.dumps(data, ensure_ascii=False, indent=2) + '\n</script>'


# ---------------------------------------------------------------- HTML blocks

def breadcrumb_html(fname):
    items = crumbs_full(fname)
    lis = []
    for i, (name, url) in enumerate(items):
        if i == len(items) - 1:
            lis.append(f'<li><span aria-current="page">{html.escape(name)}</span></li>')
        else:
            lis.append(f'<li><a href="{url}">{html.escape(name)}</a></li>')
    return '<div class="xp-breadcrumb" role="navigation" aria-label="Breadcrumb"><ol>' + ''.join(lis) + '</ol></div>'


def header_html(fname):
    tpl = (ROOT / 'partials' / 'header.html').read_text(encoding='utf-8')
    here = PAGES[fname].get('url', '/' + fname)
    return tpl.replace(f'href="{here}"', f'href="{here}" aria-current="page"')


def price_tables(prices, key):
    return render_groups(prices[key])


def render_groups(groups):
    out = []
    for g in groups:
        rows = []
        for it in g['items']:
            note = f'<span class="xp-note">{html.escape(it["note"])}</span>' if it.get('note') else ''
            rows.append(f'      <tr><th scope="row">{html.escape(it["name"])}{note}</th><td class="xp-p">{html.escape(fmt_price(it))}</td></tr>')
        intro = f'\n  <p>{html.escape(g["intro"])}</p>' if g.get('intro') else ''
        out.append(
            f'<section class="xp-price-group" id="{g["id"]}" aria-labelledby="{g["id"]}-t">\n'
            f'  <h3 id="{g["id"]}-t">{html.escape(g["title"])}</h3>{intro}\n'
            f'  <table class="xp-table">\n'
            f'    <caption>Prețuri {html.escape(g["title"].lower())} — XpertPoint București</caption>\n'
            f'    <thead><tr><th scope="col">Serviciu</th><th scope="col" class="xp-p">Preț</th></tr></thead>\n'
            f'    <tbody>\n' + '\n'.join(rows) + '\n    </tbody>\n  </table>\n</section>')
    return '\n'.join(out)


def text_only(fragment):
    t = re.sub(r'<[^>]+>', ' ', fragment)
    return re.sub(r'\s+', ' ', html.unescape(t)).strip().replace(' ,', ',').replace(' .', '.')


def faq_schema(s):
    """FAQPage generat din întrebările vizibile, ca schema să fie mereu identică cu pagina."""
    pairs = re.findall(r'<button class="faq-q" type="button">(.*?)</button>\s*<div class="faq-a">(.*?)</div>', s, re.S)
    pairs += re.findall(r'<summary>(.*?)</summary>\s*<div class="xp-faq-a">(.*?)</div>', s, re.S)
    if not pairs:
        return ''
    data = {'@context': 'https://schema.org', '@type': 'FAQPage', 'mainEntity': [
        {'@type': 'Question', 'name': text_only(q), 'acceptedAnswer': {'@type': 'Answer', 'text': text_only(a)}}
        for q, a in pairs]}
    return '<script type="application/ld+json">\n' + json.dumps(data, ensure_ascii=False, indent=2) + '\n</script>'


def put(s, name, content):
    pat = re.compile(r'(<!-- %s:START -->)(.*?)(<!-- %s:END -->)' % (re.escape(name), re.escape(name)), re.S)
    if not pat.search(s):
        return s
    return pat.sub(lambda m: m.group(1) + '\n' + content.strip('\n') + '\n' + m.group(3), s)


def meta(s, pattern):
    m = re.search(pattern, s, re.S)
    return html.unescape(m.group(1).strip()) if m else ''


# ---------------------------------------------------------------- minificare

def minify_css(css):
    """Minificare conservatoare: șirurile dintre ghilimele sunt protejate, restul pierde comentarii și spații."""
    css = re.sub(r'/\*.*?\*/', '', css, flags=re.S)   # comentariile întâi: pot conține ghilimele
    strings = []

    def keep(m):
        strings.append(m.group(0))
        return f'\x00{len(strings) - 1}\x00'
    css = re.sub(r'"(?:\\.|[^"\\])*"|\'(?:\\.|[^\'\\])*\'', keep, css)
    css = re.sub(r'\s+', ' ', css)
    css = re.sub(r'\s*([{};,>])\s*', r'\1', css)
    css = re.sub(r'([{;])\s*([\w-]+)\s*:\s*', r'\1\2:', css)
    css = css.replace(';}', '}').strip()
    return re.sub(r'\x00(\d+)\x00', lambda m: strings[int(m.group(1))], css)


def minify_js(js):
    """Minificare conservatoare: scoate doar liniile de comentariu, indentarea și rândurile goale."""
    lines = []
    for line in js.splitlines():
        t = line.strip()
        if not t or t.startswith('//'):
            continue
        lines.append(t)
    return '\n'.join(lines) + '\n'


def write_if_changed(path, content, changed):
    if not path.exists() or path.read_text(encoding='utf-8') != content:
        path.write_text(content, encoding='utf-8')
        changed.append(str(path.relative_to(ROOT)))


def build_assets(changed):
    """assets/fonts.css + site.css -> site.min.css, site.js -> site.min.js, pages/*.css -> pages/*.min.css,
    plus style.min.css pentru tema de blog (fonturi încărcate de pe www)."""
    a = ROOT / 'assets'
    fonts = (a / 'fonts.css').read_text(encoding='utf-8')
    write_if_changed(a / 'site.min.css', minify_css(fonts + '\n' + (a / 'site.css').read_text(encoding='utf-8')) + '\n', changed)
    write_if_changed(a / 'site.min.js', minify_js((a / 'site.js').read_text(encoding='utf-8')), changed)
    for src in sorted((a / 'pages').glob('*.css')):
        if src.name.endswith('.min.css'):
            continue
        write_if_changed(src.with_name(src.stem + '.min.css'), minify_css(src.read_text(encoding='utf-8')) + '\n', changed)
    theme = ROOT / 'wordpress-blog-theme' / 'xpertpoint-blog'
    if theme.exists():
        body = (theme / 'style.css').read_text(encoding='utf-8')
        body = re.sub(r'^/\*.*?\*/', '', body, count=1, flags=re.S)          # antetul temei
        body = re.sub(r'@import url\([^)]*fonts\.googleapis[^)]*\);?', '', body)  # fonturile vin de pe www
        theme_fonts = fonts.replace('url(/assets/fonts/', f'url({BASE}/assets/fonts/')
        write_if_changed(theme / 'style.min.css', minify_css(theme_fonts + '\n' + body) + '\n', changed)


def asset_version(*parts):
    h = hashlib.md5()
    for p in parts:
        h.update((ROOT / p).read_bytes())
    return h.hexdigest()[:8]


def main():
    prices = load_prices()
    changed = []
    build_assets(changed)
    footer = (ROOT / 'partials' / 'footer.html').read_text(encoding='utf-8').replace(
        '{{ASSET_VERSION}}', asset_version('assets/site.min.js'))
    consent = (ROOT / 'partials' / 'consent.html').read_text(encoding='utf-8')
    css_link = (f'<link rel="preload" href="/assets/fonts/dm-sans-normal-latin.woff2" as="font" type="font/woff2" crossorigin>\n'
                f'<link rel="preload" href="/assets/fonts/bebas-neue-normal-latin.woff2" as="font" type="font/woff2" crossorigin>\n'
                f'<link rel="stylesheet" href="/assets/site.min.css?v={asset_version("assets/site.min.css")}">')
    for fname, cfg in PAGES.items():
        path = ROOT / fname
        if not path.exists():
            print(f'  ! lipsește {fname}')
            continue
        s = orig = path.read_text(encoding='utf-8')
        title = meta(s, r'<title>(.*?)</title>')
        desc = meta(s, r'<meta name="description" content="([^"]*)"')
        s = put(s, 'SITE-CSS', css_link)
        page_css = ROOT / 'assets' / 'pages' / (path.stem + '.min.css')
        if page_css.exists():
            s = put(s, 'PAGE-CSS', f'<link rel="stylesheet" href="/assets/pages/{page_css.name}?v='
                                   f'{asset_version(str(page_css.relative_to(ROOT)))}">')
        s = put(s, 'SITE-HEADER', header_html(fname))
        s = put(s, 'SITE-FOOTER', footer)
        if cfg.get('consent'):
            s = put(s, 'CONSENT', consent)
        if cfg.get('crumbs'):
            s = put(s, 'BREADCRUMB', breadcrumb_html(fname))
        if cfg.get('schema', True):
            s = put(s, 'SCHEMA', schema(fname, prices, title, desc))
        s = put(s, 'FAQ-SCHEMA', faq_schema(s))
        if fname == 'preturi.html':
            s = put(s, 'PRICE-TABLES:BICICLETE', price_tables(prices, 'biciclete'))
            s = put(s, 'PRICE-TABLES:ESPRESSOARE', price_tables(prices, 'espressoare'))
        groups = all_groups(prices)
        for gid in re.findall(r'<!-- PRICE-GROUP:([\w-]+):START -->', s):
            s = put(s, 'PRICE-GROUP:' + gid, render_groups([groups[gid]]))
        if s != orig:
            path.write_text(s, encoding='utf-8')
            changed.append(fname)

    urls = []
    for fname, cfg in PAGES.items():
        if not cfg.get('sitemap', True) or not (ROOT / fname).exists():
            continue
        lastmod = date.fromtimestamp((ROOT / fname).stat().st_mtime).isoformat()
        urls.append(f'  <url>\n    <loc>{page_url(fname)}</loc>\n    <lastmod>{lastmod}</lastmod>\n'
                    f'    <priority>{cfg.get("priority", "0.5")}</priority>\n  </url>')
    sitemap = ('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
               + '\n'.join(urls) + '\n</urlset>\n')
    sm = ROOT / 'sitemap.xml'
    if not sm.exists() or sm.read_text(encoding='utf-8') != sitemap:
        sm.write_text(sitemap, encoding='utf-8')
        changed.append('sitemap.xml')

    print('Actualizate:', ', '.join(changed) if changed else 'nimic (totul era la zi)')


if __name__ == '__main__':
    main()
