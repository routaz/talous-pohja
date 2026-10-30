---
name: alv-muistutus
description: Yhtiön kuukausittainen ALV-muistutus. Tarkistaa NoCFO:sta ALV-kauden maksettavan tai palautettavan veron, hyväksymättömät luonnokset ja erääntyneet laskut ja muistuttaa ALV-ilmoituksen määräpäivästä. Käytä ajastetussa ALV-muistutuksessa ja kun käyttäjä kysyy ALV-ilmoitusta, ALV:n määrää tai ALV:n määräpäivää.
---

# alv-muistutus – kuukausittainen ALV-ilmoitus

Skill olettaa kuukausikauden (`config/yritys.yaml` → `arvonlisavero.kausi`).
Jos kausi on neljännesvuosi tai vuosi, sovella määräpäivät tiedostosta
`fi-rules/viitteet/arvonlisavero.md` ja raportoi vain kauden päättymisen
jälkeisinä kuukausina.
Kuukauden ALV ilmoitetaan ja maksetaan OmaVerossa **kauden päättymistä
seuraavan toisen kuukauden 12. päivänä**. Esimerkiksi marraskuun ALV erääntyy
12.1. Jos päivä on pyhä tai viikonloppu, määräpäivä siirtyy seuraavaan
arkipäivään. Ilmoitus annetaan myös kuukausilta, joilla ei ollut myyntiä
(nollailmoitus).

**Vain lukuoperaatioita.** Agentti ei anna ilmoitusta eikä maksa veroa
(CLAUDE.md, sääntö 2). Agentti ei myöskään muuta mitään NoCFO:ssa.

## Vaiheet

1. Lue `config/yritys.yaml`.
   - Jos `arvonlisavero.rekisterissa` on `false`, raportoi yhdellä rivillä:
     "Yhtiö ei ole vielä ALV-rekisterissä (config/yritys.yaml), joten
     ilmoitettavaa ei ole." Muistuta, että rekisteröinnin vahvistus kirjataan
     tiedostoon. Lopeta.
   - Jos `rekisteroity_alkaen` on asetettu, kaudet ennen sitä ohitetaan.
2. Määritä kaudet (tänään = T):
   - **Erääntyvä kausi E** = kuukausi, joka päättyi kaksi kuukautta ennen
     kuluvaa kuukautta. Sen määräpäivä on kuluvan kuukauden 12. päivä.
   - **Edellinen kuukausi K** = juuri päättynyt kuukausi. Sen ilmoitus
     erääntyy ensi kuussa, joten se raportoidaan ennakkotietona.
3. Hae NoCFO:sta kummallekin kaudelle `reporting_vat_retrieve`
   (`include_entry_lines: false`): `tax_to_be_paid`, kotimaan myynnit
   verokannoittain ja EU-myynnit.
4. Tarkista kaudelta E puutteet:
   - myyntilaskut tilassa `DRAFT` (`invoicing_sales_invoices_list`, kauden päivät)
   - luonnostositteet (`bookkeeping_documents_list`, `is_draft: true`, kauden päivät)
   - erääntyneet myyntilaskut (`invoicing_sales_invoices_list`, `is_overdue: true`)
5. Tarkista `reporting_vat_periods_list`, onko kausi E jo merkitty ilmoitetuksi.
6. Raportoi lyhyesti suomeksi:
   - **Kausi E:** maksettava tai palautettava ALV, määräpäivä ja onko
     ilmoitus jo merkitty annetuksi
   - **Kausi K:** ALV tähän mennessä (ennakkotieto)
   - **Puutteet:** luonnokset, hyväksymättömät laskut ja erääntyneet laskut
   - **Muistutus:** ilmoitus annetaan OmaVerossa (Oma-aloitteiset verot →
     Arvonlisävero), myös nollailmoituksena. Maksussa käytetään OmaVeron
     antamaa viitettä.

7. **Lähetä aina push-ilmoitus** (PushNotification), kun yhtiö on
   ALV-rekisterissä, myös nollailmoituksen kuukausina. Ilmoituksessa
   kerrotaan kausi, summa ja määräpäivä, esimerkiksi "Marraskuun ALV
   175,50 € – ilmoita ja maksa OmaVerossa 12.1. mennessä". Ennen
   rekisteröintiä ilmoitusta ei lähetetä.

Raportti ei muuta repoa, joten committia ei tehdä.
