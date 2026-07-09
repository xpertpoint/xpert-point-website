# Ghid WordPress pentru blogul XpertPoint (pas cu pas)

> Acest ghid e făcut pentru tine, Daniil. Nu ai nevoie de cunoștințe tehnice — urmează pașii exact în ordine. Blogul e la **https://xpertpoint.ro/blog/wp-admin/** (fără www). Login-ul e cu userul și parola de WordPress.
>
> Timp estimat total: ~30-40 de minute. Fă pașii într-o singură sesiune dacă poți.

---

## Partea 1 — Ștergerea conținutului demo („Hello World" și „Sample Page")

WordPress vine din instalare cu un articol de test („Hello World!") și o pagină de test („Sample Page"). Ambele arată neprofesionist și trebuie șterse **definitiv** (nu doar mutate la coș).

### 1.1 Șterge articolul „Hello World!"

1. În meniul din stânga al WP admin, dă click pe **Posts** (Articole).
2. În listă găsești **„Hello world!"**. Treci cu mouse-ul peste titlu — apar niște linkuri sub el.
3. Dă click pe **Trash** (Coș).
4. Articolul dispare din listă, dar încă e în coș. Trebuie golit coșul:
   - Sus, în lista de Posts, dă click pe **Trash (1)** / **Coș (1)** (linkul apare doar când e ceva în coș).
   - Treci cu mouse-ul peste articol și dă click pe **Delete Permanently** (Șterge definitiv).
   - SAU, mai rapid: bifează căsuța din stânga articolului, alege din dropdown-ul **Bulk actions** opțiunea **Delete Permanently** și apasă **Apply**.

### 1.2 Șterge pagina „Sample Page"

1. În meniul din stânga, dă click pe **Pages** (Pagini).
2. Găsești **„Sample Page"**. Treci cu mouse-ul peste titlu și dă click pe **Trash** (Coș).
3. Golește coșul la fel ca la articol:
   - Dă click pe **Trash (1)** / **Coș (1)** sus.
   - **Delete Permanently** pe pagina respectivă.

### 1.3 Verificare

Deschide într-un tab nou:
- **https://xpertpoint.ro/blog/hello-world/** → trebuie să dea pagină de eroare (404 / „nu s-a găsit").
- **https://xpertpoint.ro/blog/sample-page/** → la fel, 404.

Dacă mai apar, mai verifică o dată coșul de la Posts și de la Pages — probabil au rămas acolo.

> **Bonus recomandat (opțional):** dacă în lista de comentarii (meniul **Comments**) apare un comentariu demo de la „A WordPress Commenter", șterge-l tot definitiv la fel — Trash apoi Delete Permanently.

---

## Partea 2 — Instalarea și configurarea de bază a pluginului Rank Math (SEO)

**Rank Math** este un plugin gratuit care ne lasă să setăm, pentru fiecare pagină și articol, un **title SEO** (titlul care apare în Google) și o **meta description** (textul de sub titlu în Google). Fără el, blogul nu are meta descriptions — exact problema semnalată în audit.

### 2.1 Instalare

1. În meniul din stânga, dă click pe **Plugins** → **Add New Plugin** (Adaugă plugin nou).
2. În căsuța de căutare din dreapta sus scrie: **Rank Math**.
3. Găsești **„Rank Math SEO"** (autor: Rank Math). Dă click pe **Install Now** (Instalează acum).
4. După ce se instalează, butonul devine **Activate** (Activează) — dă click pe el.

### 2.2 Configurarea inițială (wizard-ul Rank Math)

După activare, Rank Math pornește un mic ghid de configurare („Setup Wizard").

1. Dacă îți cere să creezi cont / să te conectezi, poți alege varianta gratuită — caută linkul mic **„Skip"** / **„Connect Later"** dacă nu vrei cont acum (nu e obligatoriu pentru funcțiile de bază).
2. La pasul **„Your Site"** alege tipul de site: **Small Business Site** (Site de firmă mică) — se potrivește cel mai bine cu un atelier local.
3. La numele afacerii pune: **XpertPoint** (sau **XpertPoint SRL**).
4. Restul pașilor (sitemap, viteza etc.) — lasă setările implicite (default), doar apasă **Save and Continue** până la final. La sitemap lasă opțiunea de sitemap **activată**.
5. La final apasă **Finish Setup / Return to dashboard**.

> Dacă wizard-ul nu pornește singur, îl găsești oricând în meniul din stânga: **Rank Math SEO** → **Dashboard**.

### 2.3 Title și meta description pentru pagina principală a blogului (`/blog/`)

Acum setăm ce apare în Google pentru pagina principală a blogului.

1. În meniul din stânga: **Rank Math SEO** → **Titles & Meta** (Titluri și meta).
2. Caută secțiunea **Homepage** (Pagina principală). *(Notă: la un WordPress instalat în subfolderul `/blog/`, „homepage" înseamnă chiar pagina principală a blogului.)*
3. Completează:

   **SEO Title (Titlu SEO)** — copiază exact:
   ```
   Blog XpertPoint — Sfaturi biciclete și espressoare
   ```
   *(50 de caractere — sub limita de 60.)*

   **Meta Description (Descriere meta)** — copiază exact:
   ```
   Sfaturi practice de la atelierul XpertPoint din București: întreținere biciclete și espressoare, revizii, decalcifiere și reparații.
   ```
   *(132 de caractere — între 120 și 155, beneficiul e în primele cuvinte.)*

4. Apasă **Save Changes** (Salvează).

> Dacă din vreun motiv secțiunea „Homepage" nu apare (ex.: blogul folosește o pagină statică setată ca „Posts page"), atunci mergi la **Pages**, deschide pagina respectivă și setează title-ul + descrierea din caseta Rank Math de sub editor (vezi Partea 3, pasul 3.4) — textele rămân aceleași de mai sus.

### 2.4 Verificare

După ce salvezi, deschide într-un tab nou **https://xpertpoint.ro/blog/**, dă click dreapta → **View Page Source** (Vezi sursa paginii) și caută (Ctrl+F / Cmd+F) cuvântul `description`. Ar trebui să vezi meta description-ul de mai sus. Titlul din tab-ul browserului ar trebui să fie cel setat.

---

## Partea 3 — Cum publici cele 2 articole

Ai primit două fișiere cu articole gata scrise:
- `articol-decalcifiere-espressor.md`
- `articol-revizie-bicicleta.md`

Fiecare fișier are, **în cap (sus de tot)**, un bloc cu metadate — acolo găsești **Title SEO propus**, **Meta description propusă** și **URL (slug) propus**. Sub bloc începe conținutul propriu-zis al articolului (titlul mare, apoi paragrafele).

Repetă pașii de mai jos pentru fiecare articol în parte.

### 3.1 Creează articolul nou

1. În meniul din stânga: **Posts** → **Add New Post** (Adaugă articol nou).
2. Sus, în locul unde scrie „Add title" / „Adaugă titlu", scrie **titlul mare al articolului** (îl găsești în fișier imediat sub blocul de metadate — este primul rând care începe cu `#`, dar tu scrii doar textul, fără semnul `#`).
   - Pentru primul articol: **Cât de des trebuie decalcifiat un espressor și de ce contează**
   - Pentru al doilea: **Semne că bicicleta ta are nevoie de revizie**

### 3.2 Lipește conținutul

Ai două variante — a doua e mai simplă și recomandată:

**Varianta recomandată (editorul de blocuri):**
1. Deschide fișierul `.md` și copiază tot textul articolului (fără blocul de metadate din cap și fără primul rând cu titlul mare — pe acela l-ai pus deja la titlu).
2. În zona de conținut a articolului (sub titlu), lipește textul (Ctrl+V / Cmd+V). WordPress transformă automat rândurile în paragrafe.
3. **Titlurile de secțiune** (rândurile care în fișier încep cu `##` sau `###`) trebuie transformate în Heading-uri:
   - Selectează rândul de titlu, șterge semnele `##` / `###` din față.
   - Dă click pe cele trei puncte / iconița blocului și alege **Heading**, apoi din bara de sus alege nivelul: **H2** pentru `##` și **H3** pentru `###`.
   - Titlul mare al articolului (cel de la pasul 3.1) rămâne H1 automat — nu-l pune și în conținut.

**Varianta rapidă (dacă te descurci cu editorul de cod):**
1. Îți pot livra, la cerere, articolul deja convertit în HTML.
2. În editorul de articol, sus dreapta, dă click pe cele trei puncte → **Code editor** (Editor de cod), lipești HTML-ul, apoi te întorci la **Visual editor**.

> Important: **nu pune semnele `#`, `##`, `###` în textul publicat** — acelea sunt doar marcaje din fișier ca să știi ce e titlu și ce nivel are. În WordPress, nivelul de titlu se alege din butonul H2/H3.

### 3.3 Adaugă o imagine reprezentativă (opțional dar recomandat)

- Sus dreapta, la **Featured image** (Imagine reprezentativă), poți urca o poză reală din atelier. Dacă nu ai acum, poți publica și fără — dar o poză reală ajută.
- Dacă pui imagine, la **Alt Text** scrie o descriere scurtă și clară (sub 125 de caractere), ex.: `Decalcifierea unui espressor la atelierul XpertPoint din București`.

### 3.4 Setează Title SEO și Meta description în Rank Math

Aici e partea cheie — asta lipsea complet până acum.

1. Derulează sub editorul articolului (sau caută caseta **Rank Math SEO**, de obicei sub conținut sau într-un panou lateral). Dă click pe butonul **Edit Snippet** (Editează previzualizarea).
2. Se deschid trei câmpuri:
   - **Title** — șterge ce e acolo și pune **Title SEO propus** din capul fișierului `.md`.
   - **Description** — pune **Meta description propusă** din capul fișierului `.md`.
   - **Permalink / URL** — asigură-te că se termină cu **slug-ul propus** din fișier (ex.: `decalcifiere-espressor`). Îl poți edita și direct sus, sub titlul articolului, la **Permalink** → **Edit**.
3. Rank Math îți arată o bară de scor (verde = bine). Nu e obligatoriu să fie 100 — important e ca title-ul și descrierea să fie completate cu textele din fișier.

### 3.5 Publică

1. Sus dreapta apasă **Publish** (Publică), apoi confirmă încă o dată **Publish**.
2. După publicare, dă click pe **View Post** (Vezi articolul) ca să verifici cum arată live.

### 3.6 Verificare finală per articol

- Deschide articolul live și verifică vizual: titlurile de secțiune sunt îngroșate/mari (H2/H3), paragrafele sunt separate corect, linkurile către paginile de service și către programare funcționează.
- Click dreapta → **View Page Source** și caută `description` — trebuie să apară meta description-ul setat.

---

## Rezumat — ce trebuie să rămână făcut la final

- [ ] „Hello world!" șters definitiv (404 la `/blog/hello-world/`)
- [ ] „Sample Page" ștearsă definitiv (404 la `/blog/sample-page/`)
- [ ] Rank Math instalat și activat
- [ ] Title + meta description setate pentru pagina principală a blogului `/blog/`
- [ ] Articol 1 (decalcifiere espressor) publicat, cu Title SEO + meta description din fișier
- [ ] Articol 2 (revizie bicicletă) publicat, cu Title SEO + meta description din fișier

Când toate sunt bifate, Task 1 e complet din partea ta.
