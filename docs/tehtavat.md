# Avoimet tehtävät

Agentti päivittää tämän listan aina, kun tehtävä valmistuu tai uusi tehtävä
syntyy: valmis tehtävä merkitään [x] ja lisätään päivämäärä.

Tehtävät, joissa on merkintä **Odottaa**, tehdään vasta, kun ehto täyttyy.
Kysy käyttäjältä, onko ehto täyttynyt, äläkä oleta sitä.

## 1. Käyttöönotto
- [ ] Varmista, että repo on GitHubissa **yksityinen**.
- [ ] Yhdistä NoCFO-liitin (`docs/nocfo-liitin.md`) ja tarkista yritys
      työkalulla `common_current_business_retrieve`. Kirjaa slug kenttään
      `kirjanpito.nocfo_business`.
- [ ] Täytä `config/yritys.yaml`: hae nimi, Y-tunnus ja osoite NoCFO:sta tai
      YTJ:stä (`invoicing_ytj_company_retrieve`). Kysy loput käyttäjältä
      (tilikausi, osakkaat, hallitus, ALV-asema, pankki). Älä arvaa.
- [ ] Kirjaa `kirjanpito.github_repo` (omistaja/repo).
- [ ] Tarkista NoCFO:n tilikaudet (`reporting_accounting_periods_list`) ja
      vertaa niitä kenttään `tilikausi`.
- [ ] Päivitä `fi-rules/viitteet/maaraajat.md` vastaamaan yhtiön tilikautta.
- [ ] Valitse ALV-malli (`fi-rules/viitteet/arvonlisavero.md`) ja poista
      käyttämättömät luokat kohdasta `arvonlisavero.luokat`. Tarkista, että
      NoCFO:n ALV-asetukset vastaavat valintaa.
- [ ] Lisää vakioasiakkaat NoCFO:hon ja `invoice-issuer`-skillin
      asiakastaulukkoon.
- [ ] Arkistoi yhtiön asiakirjat kansioon `arkisto/`: kaupparekisteriote,
      yhtiöjärjestys, viimeisin tilinpäätös, osake- ja osakasluettelo.
- [ ] Ensimmäinen varmuuskopio `nocfo-backup`-skillillä.
- [ ] Luo ajastetut tehtävät: varmuuskopio kuun 5. ja ALV-muistutus kuun 3.
      päivänä (README, kohta 5).

## 2. Rekisteröinnit
- [ ] Tarkista YTJ:stä ALV- ja ennakkoperintärekisteröinti ja päivitä
      `arvonlisavero.rekisterissa` ja `ennakkoperintarekisteri`.
      Jos rekisteröinnit puuttuvat, käyttäjä tekee ilmoituksen (Y4/Y3).

## Valmiit
