# Plan de execuție SEO — audit Ubersuggest (v2, actualizat 9 iulie 2026)

> **Pentru modelul care execută:** acest plan e autonom — conține tot contextul necesar.
> Citește secțiunea „Context obligatoriu" înainte de orice task. Execută task-urile în ordine.
> Fiecare task are criterii de acceptare. **NU face git add/commit/push** — utilizatorul (Daniil) le face manual.
>
> **v2:** planul integrează (a) cerința lui Daniil ca paginile de conținut să țintească **2.000–2.200 de cuvinte** (pragul Ubersuggest pentru paginile care rankează) și (b) soluțiile documentate pe **neilpatel.com/blog** pentru fiecare tip de problemă. Sursele sunt citate la fiecare task și în anexă.

## Context obligatoriu

- **Site:** https://www.xpertpoint.ro — atelier service biciclete + espressoare, București, Sector 6.
- **Repo:** acest folder = site-ul static (HTML/CSS/JS + PHP form). Deploy prin cPanel Git manager (`.cpanel.yml` copiază fișierele).
- **Blogul** rulează separat, WordPress pe `xpertpoint.ro/blog/` (fără www). Tema custom e în repo la `wordpress-blog-theme/xpertpoint-blog/`, dar se instalează manual: după orice modificare a temei trebuie re-arhivat zip-ul și urcat în WP admin, SAU editat direct prin cPanel File Manager. **La orice editare a temei: bump la `Version:` din `style.css` al temei** (altfel browserele țin CSS-ul vechi în cache).
- **Hosting:** cPanel shared — doar PHP + MySQL + File Manager. Fără Node, SSH, Docker.
- **Nav + footer** trebuie să rămână identice pe toate paginile principale (index, cele 2 service, programare). Paginile legale (privacy, terms) rămân minimale — excepție confirmată.
- Auditul original e în `/Users/maretchid/Desktop/ubersuggest site audit xpertpoint.ro/` (7 CSV-uri + readme).
- **NU inventa date despre atelier** (prețuri, garanții, dotări). Folosește doar datele publice din schema JSON-LD de pe index.html (NAP, program, geo).

## Principii de conținut (din cercetarea Neil Patel — aplică-le la orice text scris)

1. **Lungime:** ținta lui Daniil e 2.000–2.200 cuvinte pe paginile de conținut. Cercetarea Neil Patel confirmă intervalul (sweet spot 1.760–2.400 cuvinte, HubSpot: 2.100–2.400), dar subliniază: **lungimea e corelată cu rankingul, nu cauza lui**. Ce contează: adâncimea tratării subiectului, acoperirea subiectelor conexe și variații naturale ale cuvintelor-cheie. Nu umple cu repetiții ca să atingi cifra — extinde cu secțiuni utile (FAQ, pași detaliați, greșeli frecvente).
2. **Title tags:** 50–60 caractere (ideal ~55), cuvântul-cheie cât mai aproape de început, unic pe fiecare pagină. (Pragul Ubersuggest de 65 e limita superioară absolută.)
3. **Meta descriptions:** sub 160 caractere (primele ~113 contează pe mobil — pune beneficiul acolo), unice, limbaj activ („programează", „află"), comunică beneficiul, fără keyword stuffing.
4. **Headings:** ierarhie strictă H1→H2→H3 fără salturi; cuvinte-cheie integrate natural.
5. **Imagini:** alt text sub 125 caractere cu cuvânt-cheie relevant, dimensiune optimizată (~300KB), lazy loading.
6. **Linkuri interne:** anchor text descriptiv (nu „click aici"), fiecare articol de blog leagă spre pagina de serviciu relevantă și spre programare.
7. **Local SEO** (business local ca XpertPoint): Google Business Profile complet + recenzii, NAP identic peste tot (atenție la „Str." vs „Strada"), pagini de serviciu localizate (avem: service-biciclete-**bucuresti**, service-espressoare-**bucuresti** ✅), mobil-friendly, articole de blog lungi (1.500–3.000 cuvinte) pe subiecte locale.

## Starea execuției (9 iulie 2026)

| Task | Stare | Detalii |
|---|---|---|
| Task 1 — blog: curățare + articole | ❌ De executat | Agentul a fost oprit înainte să producă ceva; cerință nouă: articole 2.000+ cuvinte |
| Task 2 — extindere pagini de serviciu | ❌ De executat | **NOU în v2** — paginile de serviciu au 845 / 1.084 cuvinte, sub țintă |
| Task 3 — linkuri temă blog | ✅ **FĂCUT** | Linkuri înlocuite, `Version: 1.4`, zip regenerat. Rămâne doar re-upload-ul temei de către Daniil (pas 1 din Task 6) |
| Task 4 — URL programare.html | ⏸️ Decizie Daniil | Recomandare: nu se schimbă (pagină de conversie) |
| Task 5 — redirect www | ❌ De executat | Agentul a fost oprit înainte de orice modificare |
| Task 6 — pași manuali Daniil + verificare | ❌ La final | |

Găsiri deja rezolvate anterior (nu necesită nimic): title-uri prea lungi/scurte pe site-ul static (acum 54/55 car.), pagini „blocate" (privacy/terms/wp-login — `noindex` intenționat).

---

## Task 1 — Blog WordPress: curățare conținut demo + articole 2.000+ cuvinte + meta

**Prioritate: MARE.** Blogul e live cu conținut demo („Hello World", „Sample Page"), fără meta descriptions, cu title prea lung pe `/blog/` (69 car.).

**Soluții Neil Patel aplicate:** meta description unică <160 car. pe fiecare URL; title <60 car.; articole long-form 1.500–3.000 cuvinte pe subiecte pe care le caută clienții locali; link intern din fiecare articol spre pagina de serviciu + programare.

### 1a. Livrabile în repo (executabil de model)

Creează `seo-execution/task1-blog/` cu:

1. **`ghid-wordpress.md`** — ghid pas cu pas pentru Daniil (non-tehnic) în WP admin (`xpertpoint.ro/blog/wp-admin/`):
   - Ștergerea definitivă a „Hello World" (Posts) și „Sample Page" (Pages), inclusiv din Trash.
   - Instalarea pluginului **Rank Math** (gratuit) + configurare de bază: meta description pentru homepage-ul blogului (propune text <155 car.) și title pentru `/blog/` <60 car. — propunere: „Blog XpertPoint — Sfaturi biciclete și espressoare" (50 car.).
   - Cum se publică articolele: unde se lipește conținutul, unde se setează title-ul SEO și meta description în Rank Math.
2. **`articol-decalcifiere-espressor.md`** — „Cât de des trebuie decalcifiat un espressor și de ce contează". **Minim 2.000 de cuvinte**, structurat H2/H3. Secțiuni recomandate: semne de calcar, duritatea apei (Bucureștiul are apă dură — verificabil public), frecvențe pe tip de aparat, pași de decalcifiere pe categorii (manual / automat / capsule), greșeli frecvente, când NU e de făcut acasă, FAQ. Metadate în capul fișierului: Title SEO (<60 car., cuvânt-cheie la început) + Meta description (120–155 car., beneficiu în primele 113). Link intern natural spre `https://www.xpertpoint.ro/service-espressoare-bucuresti.html` + CTA final spre `https://www.xpertpoint.ro/programare.html`.
3. **`articol-revizie-bicicleta.md`** — „Semne că bicicleta ta are nevoie de revizie". **Minim 2.000 de cuvinte**, aceeași structură. Secțiuni: verificări pe componente (frâne, schimbătoare, lanț/pinioane, anvelope, direcție/rulmenți), verificarea de sezon (primăvară/toamnă), ce poți face singur vs ce cere atelier, greșeli frecvente, FAQ. Link intern spre `https://www.xpertpoint.ro/service-biciclete-bucuresti.html` + CTA spre programare.

Ton: expert local, prietenos, practic. Fără umplutură repetitivă — atinge ținta de cuvinte prin acoperirea subiectelor conexe (principiul „comprehensive coverage" al lui Neil Patel), nu prin parafrazări.

### 1b. Pași manuali (Daniil, după ghid)

Ștergere demo → instalare Rank Math → setare title/description blog → publicare articole.

**Acceptare:** fișierele există, fiecare articol ≥2.000 cuvinte (numără cu script, nu estima), title-uri <60 car., meta descriptions 120–155 car.; după pașii manuali: hello-world și sample-page dau 404, `curl -s https://xpertpoint.ro/blog/ | grep -i 'description\|<title>'` arată meta description prezentă și title <65 car.

## Task 2 — Extinderea paginilor de serviciu la 1.500–2.200 cuvinte (NOU în v2)

**Prioritate: MARE.** Paginile care trebuie să rankeze pe „service biciclete București" / „service espressoare București" au acum **845**, respectiv **1.084** cuvinte vizibile — sub ținta de 2.000–2.200 și sub sweet spot-ul Neil Patel (1.760–2.400).

Extinde fiecare pagină cu secțiuni **vizibile**, utile, în stilul vizual existent (folosește componentele/clasele CSS deja prezente pe pagină — nu introduce stiluri noi majore):

- `service-biciclete-bucuresti.html` (~845 → țintă ≥1.800): secțiune „Cum decurge o revizie la noi" (pași, fără prețuri inventate — prețurile existente pe pagină rămân neatinse), secțiune educativă „Când e cazul de revizie" (scurtă, cu link spre articolul de blog din Task 1 după publicare), **FAQ cu 6–8 întrebări reale** (durata unei revizii, ce biciclete acceptă, dacă e nevoie de programare, garanția lucrării — DOAR ce e deja afirmat pe site sau formulat generic fără promisiuni noi), marcat cu **schema JSON-LD `FAQPage`** (recomandare Neil Patel: schema pentru FAQ).
- `service-espressoare-bucuresti.html` (~1.084 → țintă ≥1.800): idem — „Cum decurge diagnosticarea", „Mărci și tipuri de aparate deservite" (doar dace e deja menționat pe site; altfel generic: manuale/automate/capsule), FAQ 6–8 întrebări cu schema `FAQPage`.
- Respectă: H2/H3 în ierarhie corectă, cuvinte-cheie natural („service biciclete București" și variații — reparații, revizie, atelier), NAP neatins, nav/footer identice, alt text <125 car. la orice imagine nouă (preferabil fără imagini noi — cele Unsplash oricum sunt de înlocuit cu poze reale).
- **Homepage (`index.html`) și `programare.html` NU se umflă la 2.000 de cuvinte** — sunt pagini de conversie/splash; chiar cercetarea Neil Patel spune că lungimea nu e o lege, intenția de căutare primează. Dacă Daniil vrea totuși text vizibil pe homepage (decizia de la Task 2 v1, încă deschisă), adaugă o secțiune scurtă (2–3 fraze + NAP) sub butoane — nu mai mult, și fără conținut `sr-only` suplimentar (risc de cloaking).

**Verificare vizuală obligatorie:** preview-ul nu poate servi de pe Desktop (restricție TCC) — copiază fișierele în scratchpad și servește de acolo. Compară vizual înainte/după: designul existent trebuie să rămână intact, secțiunile noi în același stil.

**Acceptare:** ≥1.800 cuvinte vizibile pe fiecare pagină de serviciu (numărate cu script: strip `<script>`/`<style>`/`<head>`/tags), schema FAQPage validă (validator JSON + structura Google), zero regresii vizuale, nav/footer neschimbate, H1 unic pe pagină.

## Task 3 — Linkuri vechi în tema WordPress ✅ FĂCUT

Executat pe 9 iulie: `bike_page.html`/`coffee_page.html` → noile URL-uri cu www în `parts/header.html` și `parts/footer.html`, `Version: 1.4` în style.css, `xpertpoint-blog.zip` regenerat.

**Rămas:** doar re-upload-ul temei de către Daniil (inclus în Task 6). **Opțional, la următoarea editare a temei:** restul linkurilor din temă (logo, programare, privacy, terms) folosesc încă varianta fără www — de trecut pe `https://www.xpertpoint.ro/...` după ce redirectul din Task 5 e live (până atunci nu e nicio problemă reală).

## Task 4 — URL `programare.html` (DOAR cu confirmarea explicită a lui Daniil)

Neschimbat față de v1. Recomandare fermă: **a nu se schimba** — e pagină de conversie, nu de ranking; nimeni nu caută „programare service" ca să o găsească organic, iar costul redenumirii (redirect, Google Ads final URLs, linkuri GBP) depășește beneficiul aproape nul. Cercetarea Neil Patel despre URL-uri cere doar: simplu, clar, cuvinte-cheie unde e relevant — `/programare.html` respectă toate trei.

Dacă Daniil confirmă totuși redenumirea: `programare-service-bucuresti.html`, actualizare linkuri interne (index, ambele pagini de serviciu, temă blog + bump Version + zip), canonical, og:url, `sitemap.xml`, `.cpanel.yml`, `Redirect 301` în `.htaccess`, reminder Google Ads.

## Task 5 — Redirect www ↔ non-www în `.htaccess`

Neschimbat față de v1 (agentul a fost oprit înainte de execuție). Site-ul răspunde și pe www și pe non-www fără 301 canonic — auditul a crawlat ambele. Canonical-urile atenuează, dar 301 e soluția corectă.

**Pași:**
1. Investighează live (doar citire): `curl -sI` pe `https://xpertpoint.ro/`, `https://www.xpertpoint.ro/`, ambele + `/blog/`, și variantele `http://`. Plus `curl -s https://xpertpoint.ro/blog/ | grep -io 'https\?://[^/]*xpertpoint[^"]*' | head -20` ca să vezi ce URL-uri emite WordPress.
2. Citește `.htaccess` existent (păstrează cele 2 linii `Redirect 301` pentru bike_page/coffee_page).
3. Adaugă forțarea `https://www.xpertpoint.ro`:
   ```apache
   RewriteEngine On
   RewriteCond %{HTTP_HOST} ^xpertpoint\.ro$ [NC]
   RewriteRule ^(.*)$ https://www.xpertpoint.ro/$1 [R=301,L]
   ```
   **ATENȚIE:** dacă WordPress are `siteurl` pe non-www și redirectează înapoi (buclă), exclude blogul (`RewriteCond %{REQUEST_URI} !^/blog/`) și documentează; varianta completă cere schimbarea WP Settings → General la www **simultan cu deploy-ul** (pe shared hosting, search-replace în DB cu pluginul Better Search Replace dace apar URL-uri mixte).
4. Verifică că `.cpanel.yml` copiază `.htaccess`.

**Acceptare:** după deploy — `curl -sI https://xpertpoint.ro/` → 301 spre www; blogul se încarcă fără buclă și cu CSS intact; instrucțiuni de deploy scrise pentru Daniil.

## Task 6 — Pași manuali Daniil + verificare finală + raport

1. **Re-upload temă blog** (Task 3 e gata în repo): WP admin → Appearance → Themes → Upload `wordpress-blog-theme/xpertpoint-blog.zip` (sau înlocuire prin cPanel File Manager în `wp-content/themes/`), apoi hard-refresh.
2. Pașii din `ghid-wordpress.md` (Task 1b): ștergere demo, Rank Math, publicare articole.
3. Deploy site static (git push → cPanel) după Task 2 și Task 5, cu schimbarea WP siteurl coordonată (vezi Task 5).
4. Modelul re-verifică toate criteriile de acceptare + adaugă în `raport-seo.md` secțiune „Actualizare <data>" cu ce s-a executat.
5. Recomandări finale pentru Daniil (din cercetarea local SEO Neil Patel): Search Console + trimitere sitemap (era deja pe lista lui), recenzii constante pe Google Business Profile (factor principal pentru local pack), poze reale din atelier în locul celor Unsplash, re-rulare audit Ubersuggest peste 1–2 săptămâni.

## Ce NU trebuie făcut

- Nu umfla homepage-ul sau programare.html la 2.000 de cuvinte — pragul se aplică paginilor de conținut (servicii, articole), nu paginilor de conversie.
- Nu adăuga conținut `sr-only` suplimentar (risc de cloaking).
- Nu inventa prețuri, garanții, dotări, mărci deservite — doar informații deja publice pe site sau sfaturi generice.
- Nu atinge `noindex` de pe privacy-policy.html și terms.html — e intenționat.
- Nu schimba title-urile/meta descriptions deja fixate pe site-ul static (corecte, verificate).
- Nu face commit/push — Daniil face git manual.

## Anexă — surse Neil Patel folosite

- Lungimea conținutului: [The Best Content Length for SEO](https://neilpatel.com/blog/best-content-length-seo/) — sweet spot 1.760–2.400 cuvinte; adâncime + acoperire > cifră brută
- Word count vs performanță: [Does Word Count Impact Performance?](https://neilpatel.com/blog/word-count-impact-performance/) — corelație, nu cauzalitate; media pe industrii ~900 cuvinte
- Title tags: [Best Practices for Writing SEO Title Tags](https://neilpatel.com/blog/title-tags-seo/) — 50–60 car., keyword la început, unice
- Meta descriptions: [Meta Description 101](https://neilpatel.com/blog/meta-description-magic/) — <160 car. (113 pe mobil), limbaj activ, beneficiu
- Checklist on-page: [On-Page SEO: Guide & Optimization Checklist](https://neilpatel.com/blog/the-on-page-seo-cheat-sheet/) — headings, alt text <125 car., linkuri interne, schema
- Local SEO: [Local SEO: All-in-One Guide](https://neilpatel.com/blog/definitive-guide-local-seo/) și [5 Ways to Rank a Local Business Fast](https://neilpatel.com/blog/rank-local-business-fast/) — GBP + recenzii, NAP consistent, pagini localizate, blog long-form 1.500–3.000
