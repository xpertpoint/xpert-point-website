# Raport SEO — xpertpoint.ro

Data: 2026-07-08

## Constatare importantă înainte de a începe

Planul primit menționa că `index.html` e generat de `build-unificat.py` din sursa `index-option-b`. Am verificat: acest script și acest fișier sursă nu mai există (nici în istoricul git, nici pe disc) — `index-option-b.html` a fost redenumit direct în `index.html` printr-un commit anterior, iar `.cpanel.yml` copiază `index.html` ca fișier final la deploy. Fluxul de build a fost deja abandonat.

Am editat, cum am confirmat împreună, **`index.html` direct**, la fel ca celelalte pagini. Dacă mai există undeva o versiune veche a scriptului, nu se mai aplică — tratați `index.html` ca sursă unică de-acum înainte.

Am inclus și **`programare.html`** în lucrare (nu era în planul inițial, dar e o pagină live, listată în `.cpanel.yml`) — i-am adăugat meta description, canonical și Open Graph.

## Ce s-a schimbat pe fiecare fișier

### `index.html` (14 074 octeți)
- `<title>`: „Service Biciclete și Espressoare București | XpertPoint" (înlocuiește „Alege Serviciul (Minimal)")
- Meta description (147 caractere), canonical, Open Graph (title/description/url/image/locale)
- Schema JSON-LD `LocalBusiness` completă: nume, adresă, telefon, email, program, priceRange, geo (44.4511992, 26.0472499), sameAs cu Facebook/Instagram/TikTok/Google Business Profile
- `<h1>` „Service biciclete și espressoare în București" + un paragraf scurt (60 de cuvinte, menționează adresa, revizie bicicletă, reparații frâne/schimbătoare, decalcifiere espressoare) + un footer cu NAP complet — toate adăugate ca **conținut accesibil dar vizual ascuns** (tehnică standard `sr-only`, indexabilă de motoarele de căutare, nu afectează deloc aspectul paginii pe ecran), conform preferinței exprimate
- `lang="ro"` — era deja prezent

### `bike_page.html` (64 533 octeți)
- `<title>`: „Service Biciclete București — Revizii și Reparații | XpertPoint" (înlocuiește titlul vechi)
- Meta description (145 caractere), canonical, Open Graph
- Schema JSON-LD `["LocalBusiness", "BikeStore"]` completă, cu geo și Google Business Profile în sameAs
- Imaginea din secțiunea „about": alt îmbunătățit („Mecanic XpertPoint reparând o bicicletă în atelierul din București"), `loading="lazy"`, `width="900" height="600"`
- Footer-ul avea deja NAP corect — nu l-am modificat

### `coffee_page.html` (68 435 octeți)
- `<title>`: „Service Aparate de Cafea București — Reparații Espressoare | XpertPoint" (înlocuiește „· B (Povestea & Abonament)" — acesta era exact numele de draft care apărea în Google)
- Meta description (146 caractere), canonical, Open Graph
- Schema JSON-LD `LocalBusiness` completă, cu geo și Google Business Profile în sameAs
- Imaginea din secțiunea „about": alt îmbunătățit („Tehnician XpertPoint reparând un espressor în atelierul din București"), `loading="lazy"`, `width="900" height="600"`
- Footer-ul avea deja NAP corect — nu l-am modificat

### `programare.html` (18 209 octeți)
- Titlul era deja corect, l-am păstrat
- Am adăugat: meta description, canonical, Open Graph
- Nu am adăugat schema JSON-LD aici (e o pagină de programare, nu o pagină de „locație" — schema business e deja pe celelalte 3 pagini)

### `sitemap.xml` (nou, 391 octeți)
Include cele 4 pagini: `/`, `/bike_page.html`, `/coffee_page.html`, `/programare.html`.

### `robots.txt` (nou, 126 octeți)
`Allow: /` + link către `sitemap.xml` și `blog/wp-sitemap.xml`.

### `.cpanel.yml`
Am adăugat linii de `cp -f` pentru `sitemap.xml` și `robots.txt`, ca să ajungă și ele pe server la deploy.

## Fișiere de urcat în cPanel

- `index.html`
- `bike_page.html`
- `coffee_page.html`
- `programare.html`
- `sitemap.xml` (nou)
- `robots.txt` (nou)
- `.cpanel.yml` (dacă folosiți integrarea git → cPanel; dacă upload-ul e manual prin File Manager, acest fișier nu trebuie urcat)

## Actualizare: coordonate GPS și Google Business Profile — completate

Ai trimis linkul `https://maps.app.goo.gl/LRug4v5BZkffBh4p6` — l-am rezolvat și am extras coordonatele exacte ale profilului „XpertPoint" din Google Maps: **latitudine 44.4511992, longitudine 26.0472499**. Am completat câmpul `geo` în schema JSON-LD pe toate cele 3 pagini (index, bike, coffee) și am adăugat linkul Google Business Profile în lista `sameAs`, alături de Facebook/Instagram/TikTok. Am validat JSON-ul după modificare — e corect pe toate cele 3 fișiere.

## Ce rămâne pentru tine, Cristian

1. **Search Console** — trebuie să adaugi site-ul în Google Search Console și să trimiți manual `sitemap.xml`. Nu pot face asta eu (necesită verificare de proprietate a domeniului).
2. **Task 6 (URL-uri prietenoase)** — nu a fost executat, cum am convenit. Rămâne pentru o confirmare separată, pentru că schimbă URL-uri live și trebuie sincronizat cu Google Ads.

## Imagini Unsplash rămase (de înlocuit treptat cu poze reale din atelier)

- `bike_page.html`: `https://images.unsplash.com/photo-1507035895480-2b3156c31fc8` (secțiunea „about")
- `coffee_page.html`: `https://images.unsplash.com/photo-1447933601403-0c6688de566e` (secțiunea „about")
- `index.html`: aceleași două imagini, folosite ca fundal la hover pe cele două butoane (`bg-biciclete` / `bg-cafea`) — una dintre ele e și folosită acum ca `og:image` pe fiecare pagină

Nu există alte imagini pe site (restul e CSS/decor sau text) — doar aceste 2 fotografii Unsplash, repetate.

## Ce nu am atins

- Blogul WordPress (`/blog`)
- Conținutul existent (testimoniale, prețuri, statistici) — neschimbat
- Design-ul vizual al niciunei pagini
