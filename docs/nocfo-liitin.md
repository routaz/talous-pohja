# NoCFO-liitin

NoCFO tarjoaa MCP-palvelimen osoitteessa `https://mcp.nocfo.io`. Claude
lukee ja kirjoittaa kirjanpitoa ja laskuja sen kautta. Kirjautuminen tehdään
OAuthilla selaimessa NoCFO-tunnuksilla. API-avaimia ei tallenneta repoon.

## Ennen kuin aloitat

1. Luo NoCFO-tili ja perusta yhtiö NoCFO:ssa (nocfo.io).
2. Täytä NoCFO:n yritysasetukset: osoite, IBAN, laskun maksuehto ja ulkoasu,
   ALV-rekisteröinti ja ALV-kausi. Laskut käyttävät näitä tietoja.
3. Tarkista, että NoCFO:ssa on oikea tilikausi.

## claude.ai, Claude-sovellus ja pilvisessiot

1. Avaa https://claude.ai/customize/connectors.
2. Lisää mukautettu liitin (custom connector):
   - nimi: `NoCFO`
   - URL: `https://mcp.nocfo.io`
3. Paina **Connect** ja kirjaudu NoCFO-tunnuksillasi.
4. Aloita uusi keskustelu tai sessio. Liittimet luetaan session alussa.

Pilvisessiossa liittimen työkalut näkyvät nimellä `mcp__NoCFO__…`.

## Claude Code omalla koneella

Liitin on valmiiksi tiedostossa `.mcp.json`:

```json
{ "mcpServers": { "nocfo": { "type": "http", "url": "https://mcp.nocfo.io" } } }
```

1. Käynnistä `claude` repon kansiossa ja hyväksy `.mcp.json`-palvelin.
2. Aja `/mcp`, valitse `nocfo` ja kirjaudu selaimessa.
3. Tee tämä kerran jokaisella koneella.

Työkalut näkyvät nimellä `mcp__nocfo__…`. `.claude/settings.json` pyytää
vahvistuksen molemmille nimille.

## Tarkistus

Pyydä Claudea: "Hae NoCFO:sta nykyinen yritys." Claude kutsuu
`common_current_business_retrieve`-työkalua. Kirjaa vastauksen slug
(yleensä Y-tunnus) tiedostoon `config/yritys.yaml` →
`kirjanpito.nocfo_business`. `nocfo-backup` tarkistaa sen joka ajolla.

## Luvat

Tiedosto `.claude/settings.json` vaatii vahvistuksen näihin:

- laskun hyväksyntä, lähetys ja poisto
- tositteen ja tilin poisto
- tilikauden muutos ja poisto

Älä poista näitä. Hyväksyttyä laskua ei voi perua, vaan se korjataan
hyvityslaskulla.

## Vianetsintä

- **Liitin ei yhdisty pilvisessiossa** (esim. 403): tarkista, että liitin on
  yhdistetty claude.ai:ssa, ja aloita uusi sessio. Tarkista myös ympäristön
  verkkoasetukset (sallittu `mcp.nocfo.io`).
- **Väärä yritys:** jos NoCFO-tunnuksella on useita yrityksiä, Claude käyttää
  oletusyritystä (`business: "current"`). Vaihda oletus NoCFO:ssa tai pyydä
  Claudea käyttämään oikeaa slugia.
