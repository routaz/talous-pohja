---
name: invoice-issuer
description: Yhtiön myyntilaskut NoCFO:ssa. Tekee laskun luonnoksena NoCFO-liittimellä, valitsee ALV-luokan (esiintymispalkkio 13,5 %, muu palvelu 25,5 %, käännetty verovelvollisuus EU-yritykselle, veroton ennen rekisteröintiä), hyväksyy sen käyttäjän luvalla, jolloin se kirjautuu kirjanpitoon, ja lähettää vain käyttäjän nimenomaisesta pyynnöstä. Käytä aina, kun käyttäjä haluaa laskuttaa, tehdä laskun, laskuttaa keikan tai esiintymisen, lisätä asiakkaan tai kysyy laskun ALV:sta.
---

# invoice-issuer – myyntilaskut NoCFO:ssa

Laskut tehdään NoCFO:ssa NoCFO-liittimellä. Kun lasku hyväksytään, NoCFO
kirjaa sen kirjanpitoon automaattisesti, joten erillistä kirjausta ei tarvita.
Lue ensin `fi-rules`-skillistä tiedosto `viitteet/arvonlisavero.md` ja
`config/yritys.yaml`.

## Laskun elinkaari ja luvat

| Vaihe | Työkalu | Kuka päättää |
|---|---|---|
| 1. Luonnos | `invoicing_sales_invoice_create` | Agentti voi tehdä. Luonnos ei ole vielä kirjanpidossa. |
| 2. Hyväksyntä (numero, kirjaus) | `invoicing_sales_invoice_action` → `accept` | **Vain käyttäjän luvalla.** Ei peruttavissa. Korjaus tehdään hyvityslaskulla. |
| 3. Lähetys | `invoicing_sales_invoice_send` | **Vain käyttäjän nimenomaisesta pyynnöstä juuri tälle laskulle.** Muuten käyttäjä lähettää laskun NoCFO:ssa. |

Repon asetukset (`.claude/settings.json`) vaativat vahvistuksen hyväksyntään,
lähetykseen ja poistoon myös teknisesti.

## Työnkulku

1. **Tarkista edellytykset** tiedostosta `config/yritys.yaml`:
   - `arvonlisavero.rekisterissa`: jos `false`, käytettävissä ovat vain
     luokat `veroton_avl45` ja `veroton_avl3`. Älä tee verollista laskua.
   - `ennakkoperintarekisteri`: jos `false`, **älä tee laskua**. Kerro, että
     yhtiön on oltava ennakkoperintärekisterissä ennen laskutusta. Muuten
     maksajan on toimitettava palkkiosta ennakonpidätys, eikä asiakas välttämättä
     maksa rekisteröimättömälle. Poikkeus vain käyttäjän nimenomaisella
     päätöksellä, joka mainitaan laskun lisätiedoissa.
2. **Asiakas:** etsi asiakas työkalulla `invoicing_contacts_list` ja lue
   asiakkaan muistiinpanoista (`notes`) laskutusohje.
   - **Uusi suomalainen asiakas:** hae tiedot työkalulla
     `invoicing_ytj_company_retrieve` (Y-tunnuksella) ja luo asiakas
     työkalulla `invoicing_contact_create`. Kirjaa asiakkaan laskutusohje
     muistiinpanoihin.
   - **Ulkomainen asiakas:** kysy tiedot käyttäjältä. ALV-tunnus tallennetaan
     kenttään `invoicing_tax_code`.
3. **Kerää tiedot käyttäjältä.** Älä arvaa mitään:
   - suorituspäivä, eli esityksen tai palvelun päivä
   - rivit: kuvaus, määrä, yksikkö ja **veroton** hinta
   - ALV-luokka jokaiselle riville. Käytä asiakkaan oletusta, mutta kysy, jos
     myydään jotain muuta.
4. **Tee luonnos.** Rivin `vat_rate` ja `vat_code` tulevat ALV-luokasta
   (`config/yritys.yaml` → `arvonlisavero.luokat`). Tarkista arvot ensin
   työkalulla `constants_retrieve`, koska kannat voivat muuttua. Suorituspäivä
   ja luokan `laskuteksti` (esim. reverse charge -teksti) laitetaan laskun
   lisätietoihin.
5. **Näytä luonnos** käyttäjälle: rivit, ALV-erittely, summat ja eräpäivä.
   Hae tiedot työkalulla `invoicing_sales_invoice_retrieve`. Pyydä lupa
   hyväksyntään.
6. **Hyväksy** luvan saatuasi (`accept`). Kerro laskun numero ja viite.
7. **Lähetys:** kerro, että laskun voi lähettää NoCFO:ssa asiakkaan
   ohjeen mukaisella tavalla (esim. PDF sähköpostilla). Jos käyttäjä pyytää
   agenttia lähettämään juuri tämän laskun, tarkista tapa työkalulla
   `invoicing_sales_invoice_delivery_methods` ja lähetä työkalulla
   `invoicing_sales_invoice_send`.

## ALV-luokat

| Luokka | Milloin | NoCFO |
|---|---|---|
| `esiintymispalkkio` | Esitys kulttuuritapahtumassa, suomalainen ostaja | 13,5 %, koodi 1 |
| `yleinen` | Muu palvelu: studiotyö, tuotanto, koulutus, muu kuin julkinen esitys | 25,5 %, koodi 1 |
| `kaannetty` | Palvelu yritykselle toisessa EU-maassa (ostajan ALV-tunnus pakollinen) | 0 %, koodi 6 + reverse charge -teksti |
| `veroton_avl45` | Esiintymispalkkio **ennen** ALV-rekisteröintiä | 0 %, koodi 3 + verottomuusperuste |
| `veroton_avl3` | Muu myynti **ennen** ALV-rekisteröintiä | 0 %, koodi 3 + verottomuusperuste |

Estä nämä yhdistelmät:
- käännetty verovelvollisuus suomalaiselle ostajalle
- käännetty verovelvollisuus ilman ostajan ALV-tunnusta
- verollinen luokka ennen kuin `rekisterissa: true`

Jos ostaja on ulkomainen eikä rivillä ole käännettyä verovelvollisuutta,
pysähdy ja tarkista myyntimaa (`fi-rules`, `⚠ TARKISTA`).

## Asiakkaat

| Asiakas | Ohje (myös NoCFO:n muistiinpanoissa) |
|---|---|
| _Esimerkki Oy (1234567-8)_ | _Rivi "Esiintymispalkkio", ALV 13,5 %, PDF sähköpostilla laskut@esimerkki.fi. Korvaa omilla asiakkailla._ |
