# Osakeyhtiön talous Clauden ja NoCFO:n avulla

Pohja pienen suomalaisen osakeyhtiön taloushallintoon. Claude hoitaa
laskutuksen, kirjanpidon varmuuskopiot, ALV-muistutukset ja lakisääteiset
määräajat NoCFO-kirjanpito-ohjelman kautta. Ihminen hyväksyy laskut, tekee
viranomaisilmoitukset ja maksaa.

Pohja on tehty yhtiölle, joka laskuttaa satunnaisesti toisia yrityksiä
(esim. esiintymis- ja suorituspalkkioita), pitää rahat yhtiössä ja nostaa
osinkoa kerran vuodessa. Säännöt ovat skillissä `fi-rules`.

> ## ⚠ Vastuuvapaus
>
> Repo on maksutta jaettu esimerkki, **ei oikeudellista, verotuksellista,
> kirjanpidollista eikä sijoitusneuvontaa**. Sisältö toimitetaan sellaisenaan
> ilman takuuta, ja tekoäly voi erehtyä. **Käyttö on täysin omalla
> vastuullasi.** Tekijä ei vastaa repon käytöstä aiheutuvista vahingoista tai
> menetyksistä. Lue koko lauseke: [`VASTUUVAPAUS.md`](VASTUUVAPAUS.md).
>
> Pohja ei korvaa tilitoimistoa tai veroneuvontaa. `⚠ TARKISTA`-merkityt
> kohdat on tarkistettava lähteestä. Lakiviittaukset on koottu syksyllä 2026.

## Mitä mukana on

| Osa | Tehtävä |
|---|---|
| `CLAUDE.md` | Agentin säännöt: mitä saa tehdä itse ja mihin tarvitaan lupa |
| `config/yritys.yaml` | **Yhtiön tiedot – täytä tämä ensin** |
| `.claude/skills/fi-rules` | Kirjanpito-, vero- ja yhtiöoikeuden säännöt ja määräajat |
| `.claude/skills/invoice-issuer` | Myyntilaskut NoCFO:ssa luonnoksesta hyväksyntään |
| `.claude/skills/nocfo-backup` | Kirjanpidon kuukausittainen varmuuskopio repoon |
| `.claude/skills/alv-muistutus` | Kuukausittainen ALV-ilmoituksen muistutus |
| `.mcp.json`, `.claude/settings.json` | NoCFO-liitin ja vahvistuspyynnöt peruuttamattomille toimille |
| `arkisto/` | Yhtiön asiakirjat (tyhjät kansiot) |
| `docs/` | Arkkitehtuuri, NoCFO-ohje ja käyttöönoton tehtävälista |
| `VASTUUVAPAUS.md`, `LICENSE` | Vastuuvapauslauseke ja MIT-lisenssi |

## Käyttöönotto

### 1. Tarvitset

- GitHub-tilin
- Claude-tilauksen (Pro tai Max), jossa on Claude Code
- NoCFO-tilin, jossa yhtiö on perustettu (nocfo.io)
- Gitin ja Pythonin (3.9+), jos käytät Claude Codea omalla koneella

### 2. Tee oma repo pohjasta

Lue ensin [`VASTUUVAPAUS.md`](VASTUUVAPAUS.md). Käyttämällä pohjaa hyväksyt sen ehdot.

1. Paina tämän repon GitHub-sivulla **Use this template → Create a new repository**.
2. Valitse nimi (esim. `yhtio-talous`) ja **Private**. Repoon tallennetaan
   yhtiön asiakirjoja, joten sen on oltava yksityinen.
3. Kloonaa repo koneellesi:

```bash
git clone https://github.com/KAYTTAJA/yhtio-talous.git
```

### 3. Yhdistä NoCFO

Katso `docs/nocfo-liitin.md`. Lyhyesti:

- **claude.ai ja pilvisessiot:** lisää mukautettu liitin osoitteella
  `https://mcp.nocfo.io` sivulla https://claude.ai/customize/connectors ja
  kirjaudu NoCFO-tunnuksillasi.
- **Claude Code omalla koneella:** liitin on valmiina tiedostossa `.mcp.json`.
  Käynnistä `claude` repon kansiossa, aja `/mcp` ja kirjaudu `nocfo`-palvelimeen.

### 4. Täytä yhtiön tiedot Clauden kanssa

Käynnistä Claude Code repon kansiossa ja pyydä:

> Ota tämä repo käyttöön yhtiölleni. Käy läpi docs/tehtavat.md.

Claude hakee NoCFO:sta yrityksen tiedot, kysyy loput ja täyttää
`config/yritys.yaml`:n. Kaikki `TÄYTÄ`-kohdat on täytettävä. Käy samalla
läpi:

- `config/yritys.yaml` → `arvonlisavero.luokat`: poista luokat, joita et käytä.
- `.claude/skills/fi-rules/viitteet/maaraajat.md`: tarkista, että tilikausi
  vastaa omaasi.
- `.claude/skills/fi-rules/viitteet/arvonlisavero.md`: valitse ALV-malli.
- `.claude/skills/invoice-issuer/SKILL.md` → Asiakkaat: lisää vakioasiakkaat.

Tallenna yhtiön asiakirjat (kaupparekisteriote, yhtiöjärjestys,
tilinpäätökset, osakeluettelo) kansioihin `arkisto/…`.

### 5. Ajastetut tehtävät

Ajastetut tehtävät tehdään Claudessa (claude.ai/code → Scheduled tasks
tai pyytämällä Claudea luomaan ajastettu tehtävä pilvisessiossa).
Ajastetun tehtävän ympäristössä on oltava NoCFO-liitin ja pääsy repoon.

| Tehtävä | Ajankohta | Kehote |
|---|---|---|
| Kirjanpidon varmuuskopio | kuun 5. päivä | `Tee NoCFO-varmuuskopio nocfo-backup-skillillä.` |
| ALV-muistutus | kuun 3. päivä | `Aja alv-muistutus-skill.` |

### 6. Käyttö

Esimerkkejä:

- "Laskuta Esimerkki Oy:tä 15.11. keikasta, 1 200 € + alv."
- "Tee varmuuskopio kirjanpidosta."
- "Mitä määräaikoja on tulossa?"
- "Paljonko ALV:ta pitää maksaa tässä kuussa?"

Laskun hyväksyntä, lähetys, poistot ja tilikausien muutokset vaativat aina
vahvistuksesi.

## Useampi kone

Repo toimii Macilla, Windowsilla ja Linuxilla. Aloita työ komennolla
`git pull` ja lopeta komennolla `git push`. Python-komento on Windowsissa
`py` ja muualla `python3`.
