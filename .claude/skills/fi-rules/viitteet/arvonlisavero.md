# Arvonlisävero – AVL (1501/1993)

## Onko yhtiö arvonlisäverovelvollinen?

Kaksi erillistä kysymystä:

1. **Esiintymispalkkioiden verottomuus (AVL 45 §).** Esiintyvän taiteilijan ja
   muun julkisen esiintyjän palkkio on lähtökohtaisesti arvonlisäveroton.
   Verohallinnon syventävä ohje "Esiintymispalkkiot arvonlisäverotuksessa"
   (voimassa 1.1.2026 alkaen) kertoo, milloin vapautus koskee myös esiintyjän
   omaa yhtiötä. Vanhassa ennakkoratkaisussa yhtiö katsottiin esiintyjän
   välittäjäksi, jolloin palkkio oli veroton.
   `⚠ TARKISTA`: lue ohje ja kirjaa johtopäätös tähän tiedostoon. Se ratkaisee,
   näkyykö laskuissa ALV vai verottomuusperuste.
2. **Vähäinen toiminta (AVL 3 §).** Jos myynti on verollista, yhtiön ei tarvitse
   rekisteröityä, kun liikevaihto on **enintään 20 000 €** sekä kuluvana että
   edellisenä kalenterivuonna (raja voimassa 1.1.2025 alkaen). Raja on
   ylittymisen hetkellä, ei vasta vuoden lopussa. Rajan ylittyessä yhtiö
   rekisteröityy ylittymispäivästä alkaen.

**Vapaaehtoinen rekisteröityminen:** esiintymispalkkioista voi hakeutua
verovelvolliseksi. Silloin palkkiosta maksetaan alennetun verokannan veroa ja
hankintojen ALV:n saa vähentää. `⚠ TARKISTA` voimassa oleva verokanta ohjeesta.

Nykyinen asema: `config/yritys.yaml` → `arvonlisavero.rekisterissa`.

## Malli: vapaaehtoinen rekisteröityminen

Pohjan oletusmalli. Yhtiö hakeutuu ALV-rekisteriin, vaikka liikevaihto jää
alle 20 000 €. Jos yhtiö ei hakeudu rekisteriin, laskutetaan luokilla
`veroton_avl45` ja `veroton_avl3`, ja tämä kohta korvataan valitulla mallilla.
Kaikki hinnat ilmoitetaan muodossa **veroton summa + alv**.

Seuraukset:

- **Verokanta riippuu siitä, mitä myydään:**

  | Laskutettava | Kanta | Laskun merkintä |
  |---|---|---|
  | Esiintymispalkkio kulttuuritapahtumasta, ostaja suomalainen | **13,5 %** | Veroton summa, ALV 13,5 %, verollinen summa |
  | Muu palvelu (studiotyö, tuotanto, koulutus ilman julkista esitystä) | 25,5 % | Veroton summa, ALV 25,5 %, verollinen summa |
  | Palvelu toisen EU-maan yritykselle | 0 % (käännetty verovelvollisuus) | "VAT reverse charge – VAT to be accounted for by the recipient" + ostajan ALV-tunnus |
  | Esitys ulkomailla tai EU:n ulkopuolinen ostaja | Erikseen selvitettävä | `⚠ TARKISTA` myyntimaa |

  Käännetty verovelvollisuus perustuu yritysten välisten palvelujen
  pääsääntöön, jonka mukaan myyntimaa on ostajan maa. Tapahtumaan pääsyyn
  liittyvillä palveluilla on poikkeussääntöjä. `⚠ TARKISTA` ennen ensimmäistä
  ulkomaista laskua, koskeeko pääsääntö esiintymispalkkiota, kun esitys
  pidetään Suomessa ja kun se pidetään ulkomailla. Lisäksi tällainen myynti
  ilmoitetaan ALV-ilmoituksella ja yhteenvetoilmoituksella (EU-myynti).

  13,5 %:n kanta perustuu Verohallinnon ohjeeseen "Esiintymispalkkiot
  arvonlisäverotuksessa" (1.1.2026–). `⚠ TARKISTA` ohjeesta tai
  Verohallinnon ALV-neuvonnasta, että kanta koskee yhtiön esiintymisiä. Kanta edellyttää, että yhtiö on hakeutunut verovelvolliseksi
  esiintymispalkkioista. Ennen sitä palkkio on veroton (AVL 45 §).
  Jos laskulla on sekä esitys että muuta palvelua, rivit erotellaan
  verokannoittain. `invoice-issuer` kysyy epäselvissä tapauksissa, kumpi rivi on kyseessä.
- **Ostajalle ALV on yleensä neutraali**, jos ostaja on itse ALV-velvollinen
  ja vähentää veron.
- **Yhtiö saa vähentää hankintojen ALV:n** (kalusto, soittimet, palvelut).
  Tämä on rekisteröitymisen todellinen taloudellinen hyöty.
- **ALV ei ole yhtiön tuloa.** Myynnin ALV kirjataan velaksi (tilitettävä ALV),
  eikä sitä saa jakaa osinkona. Maksukykytestissä tilitettävä ALV on velka.
- **Ilmoitusvelvollisuus** syntyy rekisteröinnistä alkaen, myös nollakausilta.
- **Vähennysoikeus koskee vain rekisteröinnin jälkeen tehtyjä hankintoja**,
  pieniä poikkeuksia lukuun ottamatta. Isot kalustohankinnat kannattaa ajoittaa
  rekisteröinnin jälkeen.

## Verokannat

| Kanta | Käyttö |
|---|---|
| 25,5 % | Yleinen verokanta (1.9.2024 alkaen) |
| 13,5 % | Esiintymispalkkiot hakeutuneella esiintyjällä (2026) |
| 0 % / veroton | Esiintymispalkkio ilman hakeutumista (AVL 45 §) |

## Laskun pakolliset merkinnät (AVL 209 e §)

- laskun päiväys ja yksilöivä juokseva numero
- myyjän Y-tunnus (ALV-rekisterissä: ALV-tunniste)
- myyjän ja ostajan nimet ja osoitteet
- palvelun laatu ja laajuus sekä suorituspäivä
- veron peruste, verokanta ja veron määrä verokannoittain, **tai**
  verottomuuden peruste (esim. "AVL 45 §, esiintymispalkkio" tai
  "Myyjä ei ole arvonlisäverovelvollinen, AVL 3 §")

Lisäksi suositellaan viitenumeroa ja eräpäivää.

## Verkkolasku

Laki sähköisestä laskutuksesta (241/2019): elinkeinonharjoittajana toimiva
ostaja voi vaatia verkkolaskua, jos myyjän liikevaihto on yli 10 000 €.
NoCFO lähettää verkkolaskuja (maksullinen lisäpalvelu).

## ALV-ilmoitukset (vain rekisterissä ollessa)

| Verokausi | Liikevaihto enintään | Määräpäivä |
|---|---|---|
| Kuukausi | ei rajaa (oletus) | kauden päättymistä seuraavan toisen kuukauden 12. päivä |
| Neljännesvuosi | 100 000 € | sama kuin kuukausikaudella |
| Kalenterivuosi | 30 000 € | seuraavan vuoden helmikuun loppu (seuraava arkipäivä, jos se on pyhä tai viikonloppu) |

- Ilmoitus ja maksu tehdään OmaVerossa. Ilmoitus annetaan myös silloin, kun
  myyntiä ei ole ollut (nollailmoitus).
- **Kausi:** `config/yritys.yaml` → `arvonlisavero.kausi`. Kuukausikausi
  pitää ALV-summat pieninä, kun keikkoja on harvoin. Muistutuksen
  hoitaa `alv-muistutus`-skill ajastettuna kuun 3. päivänä. Myynnin ALV ei
  ole yhtiön rahaa, eikä sitä saa jakaa osinkona.
- Jos yhtiö tekee isoja hankintoja ja ALV:tä on palautettavana, lyhyempi kausi
  nopeuttaa palautusta. Kautta voi vaihtaa. `⚠ TARKISTA` vaihtamisen ehdot ja
  pidemmän kauden vähimmäiskesto (Verohallinnon ohje "Verokauden muutos").
