# Yhtiön varojen sijoittaminen (osakkeet, rahastot)

Koskee tilannetta, jossa yhtiö sijoittaa ylimääräisiä kassavarojaan
arvopapereihin, esimerkiksi Nordnetin yritystilillä. Lähteet ja tarkistukset
ovat tiedostossa `lahteet.md`.

## Yhtiöoikeus (OYL)

| Sääntö | Viite |
|---|---|
| Sijoitus yhtiön omaan arvo-osuustiliin ei ole varojenjakoa: varat pysyvät yhtiön omaisuutena | OYL 13:1 |
| Tilin ja sijoitusten on oltava **yhtiön nimissä** (yritysasiakkuus). Osakkaan omalla tilillä tehty sijoitus yhtiön rahoilla on peiteltyä osinkoa tai osakaslainaa | OYL 13:1, 13:10, VML 29 § |
| Varojen sijoittaminen kuuluu hallituksen yleistoimivaltaan | OYL 6:2 |
| Johdon on toimittava huolellisesti yhtiön edun mukaisesti | OYL 1:8 |
| Maksukyky säilytetään: tilille jätetään tilitettävä ALV, ennakkoverot ja tulevat laskut | OYL 13:2 |

Tarkista yhtiön toimiala (`config/yritys.yaml` → `toimiala`) ja
yhtiöjärjestys. Jos toimialana on "kaikki laillinen liiketoiminta",
sijoittaminen mahtuu siihen.

**Hallituksen päätös sijoitustoiminnasta** kirjataan pöytäkirjaan
(`arkisto/paatokset/`). Siinä päätetään vähintään:
- sijoitettava enimmäismäärä ja tilille jätettävä käteispuskuri
- sallitut kohteet (esim. laajasti hajautetut rahastot, pörssiosakkeet)
- välittäjä ja tili yhtiön nimissä
- kuka tekee kaupat (hallituksen jäsen yhtiön puolesta)

## Kirjanpito (KPL)

| Sääntö | Viite |
|---|---|
| Lyhytaikaiset sijoitukset (rahoitusarvopaperit) arvostetaan hankintamenoon tai sitä alempaan todennäköiseen luovutushintaan tilinpäätöspäivänä. Arvonalentuminen kirjataan, vaikka se ei olisi pysyvä | KPL 5:2, 2 kohta |
| Pitkäaikaiset sijoitukset (pysyvät vastaavat) arvostetaan hankintamenoon. Arvonalentuminen kirjataan, jos se on olennainen ja pysyvä | KPL 5:13 |
| Jokainen osto, myynti, osinko ja kulu kirjataan tositteen perusteella. Tositteina ovat välittäjän kauppavahvistukset ja vuosiraportti | KPL 2:5 |

- Luokittelu (pysyvä vai vaihtuva) päätetään sijoitusaikeen mukaan ja
  kirjataan hallituksen päätökseen.
- `⚠ TARKISTA`: saako mikroyritys arvostaa rahoitusvälineet käypään arvoon
  (KPL 5:2a, PMA). Oletus: ei käytetä, vaan noudatetaan hankintamenoa.
- `⚠ TARKISTA`: KPL 5:2:n ajantasainen sanamuoto ("todennäköinen
  luovutushinta" vai "todennäköinen käypä markkinahinta") Finlexistä.

## Tuloverotus (EVL, TVL)

| Sääntö | Viite |
|---|---|
| Osakeyhtiöllä ei ole verovuodesta 2020 alkaen henkilökohtaista tulolähdettä. Sijoitukset kuuluvat elinkeinotoiminnan tulolähteeseen | Laki tulolähdejaon poistamisesta, EVL |
| Myyntivoitot ja korot ovat veronalaista tuloa, yhteisöverokanta 20 % | TVL 124 § |
| Osinko pörssiyhtiöltä, kun yhtiö omistaa siitä **alle 10 %**: osinko on **kokonaan veronalaista** tuloa (20 %) | EVL 6 a § 3 mom. 2 kohta |
| Osinko pörssiyhtiöltä, kun omistus on vähintään 10 %: verovapaa | EVL 6 a § |
| Osakkeiden myyntivoiton verovapaus edellyttää mm. vähintään 10 %:n omistusta ja vähintään vuoden omistusaikaa, joten pienet sijoitukset eivät ole verovapaita | EVL 6 b § |

- Tappioiden vähentäminen: `⚠ TARKISTA`, voiko arvopaperien luovutustappiot
  vähentää kaikesta elinkeinotulosta vai rajoittaako jokin säännös
  vähentämistä (EVL 6 b §, EVL 8 a §).
- Sijoitusrahaston kasvuosuuden arvonnousua ei veroteta ennen myyntiä.
  `⚠ TARKISTA` rahaston tuotto-osuuden voitonjaon verokohtelu osakeyhtiölle.
- Ulkomaiset osingot ja lähdeverot: `⚠ TARKISTA` ennen ulkomaisten osakkeiden
  ostoa.

### Vaikutus omaan osinkoon (TVL 33 b §)

Kevyesti verotetun osingon raja lasketaan nettovarallisuudesta
(`osinko-ja-nostot.md`). Pörssiosakkeet ja rahasto-osuudet arvostetaan
nettovarallisuudessa **poistamattomaan hankintamenoon tai vertailuarvoon
(70 % tilinpäätöspäivän kurssista), kumpi on suurempi** (ArvL 4 §).
Sijoittaminen ei siis pienennä 8 %:n kiintiötä hankintamenon alle. Jos arvo
nousee yli 1/0,7 = noin 143 % hankintamenosta, arvonnousu alkaa näkyä
kiintiössä. Kiintiö riippuu yhtiön nettovarallisuudesta, joten ensimmäisinä
vuosina vaikutus on pieni.

## Arvonlisävero (AVL)

| Sääntö | Viite |
|---|---|
| Arvopaperikauppa ja arvopaperien välitys ovat verottomia rahoituspalveluja | AVL 41 §, 42 § |
| Passiivinen arvopaperien omistaminen on arvonlisäverolain ulkopuolista sijoitustoimintaa. Hankintaan suoraan liittyvien kulujen ALV:tä ei vähennetä | Verohallinnon ohje "Arvonlisäveron vähennysoikeudesta" |

- Välityspalkkiot ovat yleensä ALV:ttomia, joten niissä ei ole vähennettävää.
- `⚠ TARKISTA`: rajoittaako satunnainen oman kassan sijoittaminen yhtiön
  yleiskulujen ALV-vähennystä. Oletus: ei, kun sijoittaminen on passiivista
  ja vähäistä. Kirjaa johtopäätös tähän.

## Riskit tälle yhtiölle

- **Rahojen sekoittuminen:** sijoitukset tehdään vain yhtiön tililtä
  yhtiön tilille (CLAUDE.md, sääntö 4).
- **Henkilökohtainen työ yhtiön kautta (VML 28 §):** sijoittaminen ei poista
  riskiä, mutta yhtiön oma varallisuus ja taloudellinen riski voivat tukea
  sitä, että yhtiöllä on todellista toimintaa (ks. `SKILL.md`).
- **Kurssilasku ennen osingonjakoa:** tasetesti (OYL 13:5) huomioi
  tilinpäätöksen jälkeiset olennaiset muutokset. Iso kurssilasku voi
  pienentää jakokelpoisia varoja.

## Tarkistuslista ennen ensimmäistä sijoitusta

- [ ] Yhtiöllä on käteispuskuri ALV:lle, ennakkoveroille ja laskuille.
- [ ] Hallituksen päätös sijoitustoiminnasta on allekirjoitettu ja arkistoitu.
- [ ] Välittäjän tili on yhtiön nimissä ja rahat siirretään yhtiön tililtä.
- [ ] Sijoitusten tilit ja kirjaustapa on sovittu NoCFO:ssa.
- [ ] Tämän tiedoston `⚠ TARKISTA`-kohdat on käyty läpi.
