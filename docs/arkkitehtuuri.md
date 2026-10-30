# Arkkitehtuuri

```
 Syötteet               Agentti (NoCFO-liitin)                    Ihminen              Tulos
 ─────────────────      ───────────────────────────────────────   ──────────────────   ─────────────────
 Keikka/tilaus     ──▶  invoice-issuer   → laskuluonnos           hyväksyy, lähettää ─▶ NoCFO (kirjattu)
 Kuitit / PDF      ──▶  voucher-intake   → tosite + kirjausehd.   hyväksyy           ─▶ NoCFO
 Pankkitapahtumat  ──▶  reconcile        → täsmäytys, puutteet    korjaa / hyväksyy
 NoCFO (luku)      ──▶  compliance-check → sääntörikkeet, määräajat
 Tilikauden loppu  ──▶  year-end         → tilinpäätös, osakkaan  allekirjoittaa,    ─▶ OmaVero, PRH
                                           päätös, 6B-luonnos     ilmoittaa
                        dividend-planner → tasetesti, maksukyky, 8 %-raja
 Kuun 5. päivä     ──▶  nocfo-backup     → arkisto/nocfo/VVVV/  (ajastettu, vain luku) ─▶ GitHub
                 kaikki käyttävät ▶ fi-rules
```

## Skillit

| Skill | Tila |
|---|---|
| `fi-rules` | valmis (avoimet tarkistukset: `viitteet/lahteet.md`) |
| `invoice-issuer` | valmis (NoCFO) |
| `nocfo-backup` | valmis, ajastettu kuukausittain |
| `voucher-intake` | tekemättä. NoCFO:n tositteet, tiedostot ja kirjausehdotukset |
| `reconcile` | tekemättä. NoCFO:n pankkiyhteys ja tositteet |
| `compliance-check` | tekemättä |
| `year-end` | tekemättä |
| `dividend-planner` | tekemättä |

## NoCFO-integraatio

- **Liitin:** `https://mcp.nocfo.io`. Claude.ai:ssa ja pilvisessioissa se on
  liitin "NoCFO", Claude Codessa `.mcp.json` → `nocfo`. Kirjautuminen tehdään
  OAuthilla selaimessa, eikä avaimia tallenneta repoon.
- **Luvat:** `.claude/settings.json` vaatii vahvistuksen laskun hyväksyntään,
  lähetykseen ja poistoihin sekä tilikausien muutoksiin.
- **Varmuuskopio:** NoCFO on virallinen arkisto. `arkisto/nocfo/` on repon
  lisäkopio, ja git-historia säilyttää kuukausittaiset tilannekuvat.
  Liitetiedostot jäävät NoCFO:hon.
