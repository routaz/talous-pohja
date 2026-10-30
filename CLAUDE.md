# Osakeyhtiön talouden agenttityönkulku

Tämä repo hoitaa yhtiön laskutuksen, kirjanpidon tuen, varmuuskopiot ja
lakisääteiset määräajat. Yhtiön tiedot ovat tiedostossa `config/yritys.yaml`.
Repon kieli on **suomi**: dokumentit, commit-viestit ja agentin vastaukset
kirjoitetaan suomeksi.

> **Käyttöönotto kesken?** Jos `config/yritys.yaml` sisältää vielä
> `TÄYTÄ`-merkintöjä, lue ensin `README.md` ja `docs/tehtavat.md` ja auta
> käyttäjää täyttämään puuttuvat tiedot ennen muita töitä. Älä arvaa yhtiön
> tietoja.

## Yhtiön toimintamalli

- Yhtiön nimi, Y-tunnus, tilikausi, osakkaat ja hallitus ovat tiedostossa
  `config/yritys.yaml`. Lue se istunnon alussa.
- Rahat pidetään yhtiön tilillä. Osakas ei nosta palkkaa, vaan osinkoa kerran
  vuodessa vahvistetun tilinpäätöksen perusteella (`palkanmaksu`,
  `osinkostrategia` tiedostossa `config/yritys.yaml`).
- ALV-asema ja laskurivien ALV-luokat ovat kohdassa `arvonlisavero`.
  Hinnat ovat aina muotoa veroton summa + alv. Esiintymispalkkiot
  kulttuuritapahtumista suomalaiselle ostajalle laskutetaan 13,5 %:n ALV:lla
  ja muut palvelut 25,5 %:lla, kun yhtiö on ALV-rekisterissä
  (`fi-rules` → `arvonlisavero.md`).

## Kirjanpito: NoCFO

- **NoCFO on virallinen kirjanpito, laskutus ja sähköinen arkisto.** Yrityksen
  tunniste on `config/yritys.yaml` → `kirjanpito.nocfo_business`.
- Agentti käyttää NoCFO:ta MCP-liittimellä. Claude.ai:ssa ja pilvisessioissa
  se on liitin "NoCFO". Claude Codessa se on `nocfo` tiedostosta `.mcp.json`,
  ja kirjautuminen tehdään komennolla `/mcp` kerran jokaisella koneella.
  Ohjeet: `docs/nocfo-liitin.md`.
- Myyntilaskut tehdään `invoice-issuer`-skillillä. Hyväksytty lasku kirjautuu
  kirjanpitoon automaattisesti.
- Kirjanpito varmuuskopioidaan repoon (`arkisto/nocfo/`) `nocfo-backup`-skillillä
  kuukausittaisella ajastetulla tehtävällä.

## Ehdottomat säännöt

1. **Ensin selvitys, sitten muutos.** Ennen kuin agentti kirjoittaa NoCFO:hon,
   se hakee kohteen list- tai retrieve-työkalulla. Agentti kertoo, mitä on
   tekemässä, ja odottaa käyttäjän luvan kaikkeen, mitä ei voi perua: laskun
   hyväksyntä, poisto, tilikauden lukitus tai muutos ja tositteen kirjaus.
2. **Agentti ei asioi viranomaisten kanssa eikä siirrä rahaa.** OmaVero- ja
   PRH-ilmoitukset sekä maksut tekee ihminen. Laskun lähettää ihminen
   NoCFO:ssa. Agentti voi lähettää laskun vain, jos käyttäjä pyytää
   nimenomaisesti lähettämään juuri sen laskun.
3. **Jokainen kirjaus perustuu tositteeseen** (KPL 2:5). Kuitit ja muut
   tositteet tallennetaan NoCFO:hon ja liitetään kirjaukseen.
4. **Yhtiön rahat ovat yhtiön.** Jos agentti huomaa yksityismenon,
   osakkaalle maksetun summan tai muun varojen siirron, jolla ei ole
   osinkopäätöstä, palkkaa tai muuta perustetta, se merkitään
   **varoitukseksi** eikä sitä luokitella hiljaa. Vaarana on peitelty osinko
   tai osakaslaina (ks. `fi-rules`).
5. **Säännöistä ei arvata.** Lakiviittaukset ja määräajat tarkistetaan
   `fi-rules`-skillistä. Kohdat, joissa on merkintä `⚠ TARKISTA`, on
   varmistettava lähteestä ennen kuin niihin perustuva toimenpide tehdään.
6. **Henkilötiedot ja tunnukset** (henkilötunnus, pankkitunnukset, Suomi.fi-
   valtuudet, NoCFO:n API-avaimet) eivät kuulu repoon. Repon on oltava
   **yksityinen**, koska arkistoon tallennetaan yhtiön asiakirjoja.

## Rakenne

```
.claude/skills/fi-rules/        Säännöt ja määräajat (lakiviittaukset)
.claude/skills/invoice-issuer/  Myyntilaskut NoCFO:ssa
.claude/skills/nocfo-backup/    Kirjanpidon varmuuskopio repoon
.claude/skills/alv-muistutus/   Kuukausittainen ALV-muistutus (ajastettu, kuun 3. päivä)
config/yritys.yaml              Yhtiön perustiedot, rekisteröinnit, ALV-luokat
.mcp.json                       NoCFO-liitin Claude Codelle
README.md                       Käyttöönotto-ohje
docs/nocfo-liitin.md            NoCFO-liittimen käyttöönotto
docs/arkkitehtuuri.md           Putken kuvaus ja tulevat skillit
docs/tehtavat.md                Avoimet tehtävät – lue istunnon alussa, päivitä kun tehtävä etenee
arkisto/nocfo/VVVV-VVVV/        Kirjanpidon varmuuskopio (CSV + raportit + MANIFEST)
arkisto/yhtio/                  Osake- ja osakasluettelo, perustamisasiakirjat, yhtiöjärjestys
arkisto/tilinpaatokset/         Allekirjoitetut tilinpäätökset ja tase-erittelyt
arkisto/paatokset/              Osakkaan päätökset, hallituksen pöytäkirjat
arkisto/sopimukset/             Sopimukset: pankki/, asiakkaat/, palvelut/ (VVVV-KK-PP_osapuoli_aihe.pdf)
arkisto/viranomaiset/           Verohallinnon ja PRH:n päätökset ja kuitit
```

## Useampi kone (Mac ja Windows)

- Repoa käytetään Macilla ja Windowsilla. `.gitattributes` pakottaa
  rivinvaihdoksi LF:n, ja polut kirjoitetaan kauttaviivoilla (`/`).
- Aloita työ aina komennolla `git pull` ja lopeta komennolla `git push`.
- Python-komento on Windowsissa `py` ja Macilla `python3`.
- Kirjanpito on NoCFO:ssa eikä kulje gitin mukana, joten koneiden välillä ei
  synny ristiriitoja.

## Koodi

Apuskriptit (esim. `nocfo-backup`) kirjoitetaan Pythonilla ja pelkällä
vakiokirjastolla, jotta ne toimivat kaikkialla ilman asennuksia. Laajempi
koodi, kuten oma palvelin, tehdään C#:lla SOLID-periaatteita noudattaen.
Riippuvuudet kulkevat pienten rajapintojen kautta, jotta kirjanpito-ohjelman
voi vaihtaa myöhemmin.
