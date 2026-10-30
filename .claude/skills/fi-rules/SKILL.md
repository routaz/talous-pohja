---
name: fi-rules
description: Suomalaisen osakeyhtiön kirjanpidon, verotuksen ja yhtiöoikeuden säännöt. Lakiviittaukset, määräajat, säilytysajat, ALV, yhteisövero, osingonjako, peitelty osinko ja osakaslaina. Käytä aina, kun kirjaat, laskutat, laadit tilinpäätöstä, suunnittelet osinkoa, nostat rahaa yhtiöstä, tarkistat määräaikoja tai kun kysymys koskee Kirjanpitolakia, Osakeyhtiölakia, EVL:ää, TVL:ää, AVL:ää, OmaVeroa tai PRH:ta.
---

# fi-rules – säännöt ja määräajat

Tämä skill on muiden skillien yhteinen sääntöpohja. Se ei tee kirjauksia, vaan
kertoo, mitä sääntöjä kirjausten, laskujen ja päätösten on noudatettava.

## Käyttö

1. Lue `config/yritys.yaml`: tilikausi, ALV-asema, osakkaat ja hallitus.
2. Avaa aiheen viitetiedosto:

| Aihe | Tiedosto |
|---|---|
| Kirjanpito, tositteet, säilytys, tilinpäätös | `viitteet/kirjanpito.md` |
| Yhtiökokous, päätökset, osinko, osakaslaina | `viitteet/osakeyhtio.md` |
| Yhteisövero, kulujen vähennyskelpoisuus, 6B | `viitteet/tuloverotus.md` |
| Rahan nostaminen yhtiöstä, osingon verotus | `viitteet/osinko-ja-nostot.md` |
| Yhtiön varojen sijoittaminen (osakkeet, rahastot) | `viitteet/sijoittaminen.md` |
| ALV, esiintymispalkkiot, laskumerkinnät | `viitteet/arvonlisavero.md` |
| Vuosikalenteri ja määräajat | `viitteet/maaraajat.md` |
| Lähteet ja niiden tarkistaminen | `viitteet/lahteet.md` |

3. Mainitse vastauksessa lakiviittaus (esim. "KPL 2:4", "OYL 13:2").
4. Jos kohdassa on merkintä `⚠ TARKISTA`, sano se käyttäjälle ja tarkista
   ajantasainen arvo lähteestä (`viitteet/lahteet.md`) ennen kuin sitä käytetään
   laskelmassa tai päätöksessä.

## Ydinsäännöt

- **Kahdenkertainen kirjanpito, suoriteperuste**, NoCFO:n osakeyhtiön tililuettelo.
- **Ei kirjausta ilman tositetta.** Tosite on päivätty ja numeroitu (KPL 2:5).
- **Kirjaukset viimeistään 4 kk kuukauden päättymisestä**, käteismaksut viipymättä (KPL 2:4).
- **Yhtiön ja osakkaan rahat pidetään erillään.** Jokainen yhtiöstä osakkaalle
  lähtevä euro tarvitsee perusteen: osinkopäätöksen, palkan, kulukorvauksen
  tositteineen tai kirjallisen lainasopimuksen. Muuten kyse voi olla
  laittomasta varojenjaosta (OYL 13:1) tai peitellystä osingosta (VML 29 §).
- **Osinko vain vahvistetun tilinpäätöksen perusteella** ja vain, jos
  maksukyky säilyy (OYL 13:2, 13:6).
- **Agentti ei ilmoita mitään viranomaisille.** Se valmistelee luonnokset, ja ihminen ilmoittaa.

## Tärkein epävarmuus: henkilökohtainen työ yhtiön kautta

Yhtiön tulot syntyvät osakkaan henkilökohtaisesta esiintymisestä. Jos yhtiöllä
ei ole todellista omaa toimintaa, Verohallinto voi verottaa tulon suoraan
osakkaan ansiotulona (VML 28 §, veron kiertäminen). Silloin osinkomallin
veroetu katoaa. Riskiä pienentävät esimerkiksi useat asiakkaat, yhtiön omat
investoinnit (kalusto, studio), yhtiön kantama taloudellinen riski ja
sopimukset yhtiön nimissä.
`⚠ TARKISTA`: Pyydä ennakkoratkaisu tai asiantuntijan arvio ennen ensimmäistä
osingonjakoa. Kirjaa johtopäätös tiedostoon `arkisto/viranomaiset/`.
