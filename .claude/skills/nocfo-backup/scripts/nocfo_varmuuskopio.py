"""NoCFO-varmuuskopion viimeistely: CSV-muunnos, tarkistukset ja MANIFEST.md.

Käyttö: python3 nocfo_varmuuskopio.py arkisto/nocfo/VVVV

Kansiossa on oltava agentin NoCFO:sta tallentamat tiedostot (ks. SKILL.md):
  raw/paivakirja.json           päiväkirjaraportin vastaus (yhteenveto + dataset-tiedot)
  raw/paivakirja_viennit.json   kaikki viennit listana (reporting_dataset_query, entries, kaikki sivut)
  raw/tase.json, raw/tuloslaskelma.json, raw/alv.json
  raw/tositteet.json, raw/myyntilaskut.json, raw/tilit.json   listoja

Vain Pythonin vakiokirjasto, jotta skripti toimii kaikkialla ilman asennuksia.
Paluuarvo 0 = kopio on eheä, 1 = tarkistus epäonnistui (älä commitoi).
"""
from __future__ import annotations

import csv
import json
import sys
from datetime import datetime, timezone
from decimal import Decimal, InvalidOperation
from pathlib import Path

LISTAT = ("paivakirja_viennit", "tositteet", "myyntilaskut", "tilit")
RAPORTIT = ("paivakirja", "tase", "tuloslaskelma", "alv")


def lue(polku: Path):
    with polku.open(encoding="utf-8") as f:
        return json.load(f)


def litista(rivi: dict, etuliite: str = "") -> dict:
    """Sisäkkäiset kentät muotoon a.b, listat JSON-tekstinä."""
    tulos = {}
    for avain, arvo in rivi.items():
        nimi = f"{etuliite}{avain}"
        if isinstance(arvo, dict):
            tulos.update(litista(arvo, f"{nimi}."))
        elif isinstance(arvo, list):
            tulos[nimi] = json.dumps(arvo, ensure_ascii=False)
        else:
            tulos[nimi] = arvo
    return tulos


def kirjoita_csv(rivit: list[dict], polku: Path) -> None:
    litteat = [litista(r) for r in rivit]
    kentat: list[str] = []
    for r in litteat:
        kentat += [k for k in r if k not in kentat]
    with polku.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=kentat or ["(tyhjä)"], delimiter=";", lineterminator="\n")
        w.writeheader()
        w.writerows(litteat)


def summa(rivit: list[dict], kentta: str) -> Decimal | None:
    arvot = [r.get(kentta) for r in rivit if r.get(kentta) not in (None, "")]
    if not arvot:
        return None
    try:
        return sum((Decimal(str(a)) for a in arvot), Decimal(0))
    except InvalidOperation:
        return None


def main(kansio: Path) -> int:
    raw = kansio / "raw"
    virheet: list[str] = []
    tiedot: dict[str, object] = {}
    for nimi in LISTAT + RAPORTIT:
        polku = raw / f"{nimi}.json"
        if not polku.exists():
            virheet.append(f"Puuttuu: raw/{nimi}.json")
            continue
        tiedot[nimi] = lue(polku)
        # Yhtenäinen muotoilu, jotta kuukausien väliset erot näkyvät gitissä riveittäin.
        polku.write_text(json.dumps(tiedot[nimi], ensure_ascii=False, indent=1, sort_keys=True) + "\n", encoding="utf-8")
    for nimi in LISTAT:
        if nimi in tiedot and not isinstance(tiedot[nimi], list):
            virheet.append(f"raw/{nimi}.json: odotettiin listaa (kaikki sivut yhdistettynä).")

    for nimi in RAPORTIT:
        r = tiedot.get(nimi)
        if nimi in tiedot and not (isinstance(r, dict) and isinstance(r.get("data"), dict) and (r.get("as_of") or {}).get("observed_at")):
            virheet.append(f"raw/{nimi}.json: tallenna NoCFO:n vastaus kokonaisena (kentät as_of.observed_at ja data puuttuvat).")

    viennit = tiedot.get("paivakirja_viennit") if isinstance(tiedot.get("paivakirja_viennit"), list) else []
    raportti = tiedot.get("paivakirja") or {}
    data = raportti.get("data", {}) if isinstance(raportti, dict) else {}
    if isinstance(raportti, dict) and not (raportti.get("dataset") or {}).get("sha256"):
        virheet.append("raw/paivakirja.json: dataset.sha256 puuttuu (tallenna vastaus kokonaisena).")

    odotettu = data.get("entry_count")
    if odotettu is None:
        virheet.append("raw/paivakirja.json: data.entry_count puuttuu.")
    elif odotettu != len(viennit):
        virheet.append(f"Vientejä {len(viennit)}, päiväkirjaraportin mukaan {odotettu}. Hae kaikki sivut.")

    debet, kredit = summa(viennit, "debet"), summa(viennit, "credit")
    tasapaino = "ei tarkistettavissa (debet/credit-kenttiä ei löytynyt)"
    if debet is not None and kredit is not None:
        if debet != kredit:
            virheet.append(f"Debet {debet} ≠ kredit {kredit}.")
        tasapaino = f"debet {debet} = kredit {kredit}" if debet == kredit else f"EI TÄSMÄÄ: debet {debet}, kredit {kredit}"

    for nimi in LISTAT:
        if isinstance(tiedot.get(nimi), list):
            kirjoita_csv(tiedot[nimi], kansio / f"{nimi}.csv")

    as_of = raportti.get("as_of", {}) if isinstance(raportti, dict) else {}
    sormenjalki = as_of.get("books_fingerprint", {}) if isinstance(as_of, dict) else {}
    dataset = raportti.get("dataset", {}) if isinstance(raportti, dict) else {}
    manifest = [
        f"# NoCFO-varmuuskopio {kansio.name}",
        "",
        f"- Luotu: {datetime.now(timezone.utc).isoformat(timespec='seconds')}",
        f"- NoCFO:n tila hetkellä: {as_of.get('observed_at', '?')}",
        f"- Jakso: {data.get('date_from', '?')} – {data.get('date_to', '?')}",
        f"- Tositteita (päiväkirja): {data.get('document_count', '?')}, uusin: {sormenjalki.get('newest_document_number')} ({sormenjalki.get('newest_document_date')})",
        f"- Vientejä: {len(viennit)} (raportti: {odotettu})",
        f"- Tasapaino: {tasapaino}",
        f"- Päiväkirjan dataset sha256 (NoCFO): {dataset.get('sha256', '?')}",
        "",
        "| Tiedosto | Rivejä |",
        "|---|---|",
    ]
    for nimi in LISTAT:
        if isinstance(tiedot.get(nimi), list):
            manifest.append(f"| {nimi}.csv | {len(tiedot[nimi])} |")
    manifest += [
        "",
        "Raportit alkuperäisessä muodossa kansiossa `raw/`. CSV-erotin on puolipiste.",
        "Liitetiedostot (kuitit, PDF:t) ovat NoCFO:n sähköisessä arkistossa; `tositteet.csv` listaa niiden tunnisteet.",
    ]
    if virheet:
        manifest += ["", "## VIRHEET", *[f"- {v}" for v in virheet]]
    (kansio / "MANIFEST.md").write_text("\n".join(manifest) + "\n", encoding="utf-8")

    print("\n".join(manifest))
    return 1 if virheet else 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(__doc__, file=sys.stderr)
        sys.exit(2)
    sys.exit(main(Path(sys.argv[1])))
