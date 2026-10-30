# Rahan nostaminen yhtiöstä – osinkomalli

Yhtiön toimintamalli: rahat pidetään yhtiön tilillä ja osinko nostetaan kerran
vuodessa. Tämä tiedosto kuvaa, miten se tehdään laillisesti ja veroedullisesti.

## Nostotavat ja niiden seuraukset

| Tapa | Edellytys | Verotus osakkaalla | Huom. |
|---|---|---|---|
| **Osinko** | Vahvistettu tilinpäätös, osakkaan päätös, maksu- ja tasetesti (OYL 13:2, 13:5, 13:6) | TVL 33 b § (alla) | Valittu malli |
| Palkka | Palkkalaskelma, ennakonpidätys, tulorekisteri-ilmoitus | Ansiotulo | Ei käytössä. Palkka vaikuttaisi YEL-vakuutukseen |
| Kulukorvaus | Tosite yhtiön kulusta, jonka osakas maksoi | Verovapaa | Vain todellisista yhtiön kuluista |
| Osakaslaina | Kirjallinen sopimus, jakokelpoiset varat (OYL 13:10) | Pääomatulo (TVL 53 c §) | **Vältä** – ei veroetua |
| Ilman perustetta | – | Peitelty osinko (VML 29 §), mahdollisesti ansiotulo | **Kielletty** (OYL 13:1) |

## Listaamattoman yhtiön osingon verotus (TVL 33 b §)

Raja lasketaan osakkeiden **matemaattisesta arvosta**. Se on yhtiön
nettovarallisuus **osingonjakovuotta edeltävän tilikauden päättyessä**.

| Osinko | Verotus osakkaalla |
|---|---|
| Enintään 8 % matemaattisesta arvosta, enintään 150 000 €:n osalta | 25 % veronalaista pääomatuloa, 75 % verovapaata |
| Enintään 8 % matemaattisesta arvosta, 150 000 €:n ylittävältä osalta | 85 % veronalaista pääomatuloa |
| 8 %:n ylittävä osa | 75 % veronalaista ansiotuloa, 25 % verovapaata |

`⚠ TARKISTA` prosentit ja euroraja vero.fi:stä ennen jokaista osingonjakoa.

### Mitä tämä tarkoittaa tälle yhtiölle

1. **Rahan pitäminen yhtiössä kasvattaa nettovarallisuutta.** Se puolestaan
   kasvattaa seuraavien vuosien kevyesti verotettua 8 %:n osinkokiintiötä.
   Malli toimii vuosi vuodelta paremmin.
2. **Ensimmäisinä vuosina 8 %:n kiintiö on pieni.** Jos nettovarallisuus on
   esimerkiksi 10 000 €, kiintiö on 800 €. Sen ylittävä osinko verotetaan
   pääosin ansiotulona, ja lisäksi yhtiö on jo maksanut voitosta 20 %:n veron.
   `dividend-planner` laskee joka vuosi, kannattaako jakaa vain kiintiön verran
   ja jättää loput yhtiöön.
3. **Ajoitus**: tilikauden 2026 voitto voidaan jakaa vasta, kun tilinpäätös 2026
   on vahvistettu, eli käytännössä vuoden 2027 puolella. Osingon 8 %:n raja
   lasketaan silloin 31.12.2026 nettovarallisuudesta.
4. **Henkilökohtaisen työn riski** (VML 28 §): jos Verohallinto katsoo, että
   tulo on osakkaan omaa työtuloa, osinkomalli voidaan sivuuttaa. Katso `SKILL.md`.

## Osingonjaon tarkistuslista

- [ ] Tilinpäätös on laadittu, allekirjoitettu ja vahvistettu osakkaan päätöksellä.
- [ ] Vapaa oma pääoma ≥ osinko (tasetesti, OYL 13:5). Tilinpäätöksen jälkeiset
      olennaiset muutokset on huomioitu.
- [ ] Maksukykytesti dokumentoitu: tilillä on rahaa tuleviin veroihin ja
      laskuihin osingon jälkeenkin (OYL 13:2).
- [ ] Osakkaan päätös allekirjoitettu ja arkistoitu (`arkisto/paatokset/`).
- [ ] Ennakonpidätys: listaamattoman yhtiön osingosta toimitetaan
      ennakonpidätys. `⚠ TARKISTA` prosentti ja ilmoitustapa (tulorekisteri) vero.fi:stä.
- [ ] Osingonmaksu ja pidätys kirjattu NoCFO:hon.
