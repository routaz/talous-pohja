---
name: nocfo-backup
description: Yhtiön kirjanpidon varmuuskopio NoCFO:sta repoon (arkisto/nocfo/). Hakee NoCFO-liittimellä päiväkirjan kaikki viennit, tase-, tulos- ja ALV-raportit, tositeluettelon, myyntilaskut ja käytetyt tilit, muuntaa ne CSV:ksi, tarkistaa eheyden ja commitoi. Käytä, kun käyttäjä pyytää varmuuskopiota tai kirjanpidon tallentamista repoon, ja kuukausittaisessa ajastetussa tehtävässä.
---

# nocfo-backup – kirjanpidon varmuuskopio

Virallinen kirjanpito ja sähköinen arkisto ovat NoCFO:ssa. Tämä skill tekee
repoon **lisäkopion**, jonka voi lukea ilman NoCFO:ta. Git-historia säilyttää
jokaisen kuukausittaisen tilannekuvan.

**Vain lukuoperaatioita.** Älä koskaan muuta NoCFO:n tietoja tämän skillin
aikana. Varmuuskopioon tarvittavat työkalut ovat kaikki `*_list`-,
`*_retrieve`- ja `reporting_*`-työkaluja.

## Mitä varmuuskopioidaan

Varmuuskopioon tulee **koko tilikausi** alusta tähän päivään. Kansio on
`arkisto/nocfo/VVVV-VVVV/` (tilikauden alku- ja loppuvuosi, esim. `2026-2027`), ja se ylikirjoitetaan joka kerta.
- **Kuuden kuukauden ajan tilikauden päättymisestä** varmuuskopioi lisäksi
  **edellinen tilikausi**, koska tilinpäätöskirjauksia tehdään vielä silloin.
  Tilikausi on `config/yritys.yaml` → `tilikausi`. Kalenterivuosi-tilikaudella
  edellinen tilikausi kopioidaan tammi–kesäkuussa.
- **Sen jälkeen** edellistä tilikautta ei enää muuteta, joten sen viimeinen
  kopio jää voimaan.

Tilikausien rajat haetaan työkalulla `reporting_accounting_periods_list`.

## Vaiheet (yksi tilikausi, alku A, loppu L = min(tilikauden loppu, tänään))

Kaikissa kutsuissa käytetään parametria `business: "current"`. Tarkista
`common_current_business_retrieve`-työkalulla, että slug on sama kuin
`config/yritys.yaml` → `kirjanpito.nocfo_business`. Muuten lopeta ja kerro
käyttäjälle.

1. **Päiväkirja:** `reporting_journal_retrieve`, yksi sarake A–L,
   `extend_accounts: true`. Tallenna vastaus sellaisenaan tiedostoon
   `raw/paivakirja.json`.
2. **Viennit:** hae `reporting_dataset_query`-työkalulla edellisen vastauksen
   `dataset_ref`:llä parametrein `operation: "entries"`, `group_by: "none"` ja
   `limit: 200`. Jatka hakua `offset`-parametrilla, kunnes kaikki viennit on
   haettu. Yhdistä kaikki rivit **yhdeksi JSON-listaksi** tiedostoon
   `raw/paivakirja_viennit.json`. Rivien määrän on vastattava päiväkirjan
   `entry_count`-arvoa.
   - Jos `entry_count` on 0, älä kysele aineistoa, koska tyhjä aineisto
     palauttaa virheen. Tallenna silloin tyhjä lista `[]`.
3. **Raportit**, jokainen omaan tiedostoonsa sellaisenaan:
   - `reporting_balance_sheet_retrieve`: `date_at` = L ja
     `extend_accounts: true` → `raw/tase.json`
   - `reporting_income_statement_retrieve`: A–L ja `extend_accounts: true`
     → `raw/tuloslaskelma.json`
   - `reporting_vat_retrieve`: A–L ja `include_entry_lines: false`
     → `raw/alv.json`
4. **Listat**, jokainen omaan tiedostoonsa. Jos vastaus on `compacted`, käy
   läpi `reference_inspect` view=items -näkymällä kaikki sivut:
   - `bookkeeping_documents_list` (date_from A, date_to L) → `raw/tositteet.json`
   - `invoicing_sales_invoices_list` (invoicing_date_from A, invoicing_date_to L)
     → `raw/myyntilaskut.json`
   - `bookkeeping_accounts_list` (`is_used: true`) → `raw/tilit.json`
5. **Viimeistely:** aja
   `python3 .claude/skills/nocfo-backup/scripts/nocfo_varmuuskopio.py arkisto/nocfo/VVVV-VVVV`.
   Windowsissa komento on `py`. Skripti kirjoittaa CSV-tiedostot ja
   `MANIFEST.md`:n ja tarkistaa vientien määrän sekä debetin ja kreditin
   täsmäämisen.
   - **Paluuarvo ≠ 0:** älä commitoi. Korjaa puuttuvat sivut ja aja
     uudelleen, tai raportoi virhe käyttäjälle.
   - Tallenna raporttien vastaukset **kokonaisina**. Älä tiivistä niitä äläkä
     jätä kenttiä pois. Skripti hylkää kopion, jos `as_of.observed_at`,
     `data` tai päiväkirjan `dataset.sha256` puuttuu.
6. **Commit ja push aina,** vaikka luvut eivät olisi muuttuneet. Uusi
   `MANIFEST.md` ja NoCFO:n aikaleima ovat todiste siitä, että kuukauden
   tarkistus on tehty. Viesti on muotoa
   `NoCFO-varmuuskopio VVVV-VVVV (tila PP.KK.VVVV)`. Commitoi vain kansio
   `arkisto/nocfo/`.
7. **Raportoi lyhyesti:** tositteiden ja vientien määrä, tasapaino ja mahdolliset huomiot.

Jos tilikaudella ei ole tositteita, varmuuskopio tehdään silti. Tyhjät
tiedostot osoittavat, että tila on tarkistettu.

## Liitetiedostot

Kuitit ja PDF:t pysyvät NoCFO:n arkistossa. Liitetiedostojen sisältö palautuu
työkaluista vain näytettävänä sisältönä, ei tallennettavina tiedostoina.
Siksi `tositteet.csv` sisältää liitteiden tunnisteet (`attachment_ids`) mutta
ei itse tiedostoja. Jos jokin myöhempi NoCFO-työkalu antaa ladata
tiedostoja, täydennä tämä kohta.

## Kuukausittainen ajo

Ajastettu tehtävä käynnistää varmuuskopion kuun 5. päivänä uudessa
pilvisessiossa, jossa on NoCFO-liitin. Ajastetussa ajossa:
- Jos repoa ei ole sessiossa, liitä se (`config/yritys.yaml` →
  `kirjanpito.github_repo`; add_repo, push) ja kloonaa.
- Pushaa suoraan `main`-haaraan.
