# Kirjanpito – Kirjanpitolaki (KPL 1336/1997) ja pienyritysasetus (PMA 1753/2015)

## Kokoluokka

Yhtiö on **mikroyritys** (KPL 1:4 b), kun se ylittää
päättyneellä ja sitä edeltäneellä tilikaudella enintään yhden rajoista:

- taseen loppusumma 350 000 €
- liikevaihto 700 000 €
- keskimäärin 10 työntekijää

Mikroyritys laatii tilinpäätöksen PMA:n kevennetyillä säännöillä. Se ei tarvitse
rahoituslaskelmaa eikä toimintakertomusta (KPL 3:1). Liitetiedot laaditaan PMA:n
mikroyrityssäännösten mukaan. `⚠ TARKISTA` mikroyrityksen liitetietoluettelo
PMA:sta tilinpäätöstä laadittaessa.

## Kirjaaminen

| Sääntö | Viite |
|---|---|
| Kahdenkertainen kirjanpito | KPL 2:1 |
| Suoriteperuste: tulot ja menot kirjataan suoritusperusteella | KPL 2:3 |
| Käteismaksut kirjataan viipymättä kunkin päivän osalta | KPL 2:4 |
| Muut kirjaukset kuukausittain, viimeistään 4 kk jakson päättymisestä | KPL 2:4 |
| Kirjaukset aikajärjestyksessä (päiväkirja) ja asiajärjestyksessä (pääkirja) | KPL 2:4 |
| Jokainen kirjaus perustuu päivättyyn ja numeroituun tositteeseen | KPL 2:5 |
| Rahaliikenne kirjataan rahoituslaitoksen tositteen perusteella (tiliote) | KPL 2:5 |
| Tililuettelo ja luettelo kirjanpidoista ja aineistoista (menetelmäkuvaus) | KPL 2:7 |

Käytännön sovellus:

- **Myyntilasku** kirjataan myyntisaamiseksi laskun päivämäärälle tai
  suoritusajankohdalle (suoriteperuste). Maksu kirjataan tiliotteelta.
- **Ostotosite** (kuitti, lasku) tallennetaan NoCFO:hon ja liitetään kirjaukseen.
- **Tiliote** kuukausittain arkistoon. Pankkitilin saldon on täsmättävä
  kirjanpitoon kuun lopussa (täsmäytys).
- **Osakkaan maksamat yhtiön kulut** kirjataan velaksi osakkaalle. Ne
  palautetaan kulukorvauksena tositteita vastaan.

## Säilytysajat (KPL 2:10)

| Aineisto | Aika |
|---|---|
| Tilinpäätös, tase-erittelyt, päivä- ja pääkirja, tililuettelo, luettelo kirjanpidoista | 10 vuotta tilikauden päättymisestä |
| Tositteet, kirjeenvaihto, muu aineisto | 6 vuotta sen vuoden lopusta, jona tilikausi päättyi |

Säilytys sähköisesti on sallittu, kun aineisto on tulostettavissa ja tarkasteltavissa
Suomessa koko säilytysajan.

**Säilytyspaikka tässä yhtiössä:**

| Kopio | Sijainti | Rooli |
|---|---|---|
| NoCFO (kirjanpito ja sähköinen arkisto) | Suomalainen palvelu | Virallinen kirjanpito, tositteet liitteineen |
| GitHub (`arkisto/nocfo/`, yksityinen repo) | Palvelimet Yhdysvalloissa | Lisäkopio, kuukausittaiset tilannekuvat |

`⚠ TARKISTA`: NoCFO:n palvelimien sijainti ja arkistointi KPL 2:10:n
säilytysaikojen (6 ja 10 vuotta) osalta. Tarkista myös, miten aineisto
saadaan ulos, jos NoCFO:n käyttö päättyy. GitHub ei ole ainoa kopio, koska
virallinen arkisto on NoCFO:ssa.

## Tilinpäätös

| Sääntö | Viite |
|---|---|
| Sisältö: tase, tuloslaskelma, liitetiedot | KPL 3:1 |
| Laadittava 4 kk:n kuluessa tilikauden päättymisestä | KPL 3:7 |
| Hallitus (ja toimitusjohtaja) allekirjoittaa ja päivää | KPL 3:7 |
| Tase-erittelyt: laaditaan, ei julkisteta | KPL 3 luku, PMA |
| Rekisteröitävä PRH:een 8 kk:n kuluessa tilikauden päättymisestä | KPL 3:9 |

Tilinpäätöksen voi toimittaa PRH:lle Verohallinnon kautta veroilmoituksen
yhteydessä. `⚠ TARKISTA` OmaVeron nykyinen menettely vuosittain.

## Tarkistuslista kirjausehdotukselle

- [ ] Tosite on olemassa, päivätty ja numeroitu.
- [ ] Kirjauspäivä on suoritusajankohta (suoriteperuste).
- [ ] Tili on NoCFO:n tililuettelosta (`bookkeeping_accounts_list`, älä arvaa numeroa).
- [ ] ALV-käsittely vastaa `config/yritys.yaml`:n ALV-asemaa.
- [ ] Jos vastapuoli on osakas: onko peruste (osinkopäätös, kulukorvaus,
      lainasopimus)? Jos ei, kirjoita varoitus.
