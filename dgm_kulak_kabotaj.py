#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""T.C. Denizcilik Genel Müdürlüğü — İç Kulak Kabotaj Dairesi.

Gerçekten çalışır. Kulaklar artık limandır.
Gizli madde: boşaltılmayan kulak gibi sorulmayan hesap da birikir. Parti değil, mekanizma.
"""

from __future__ import annotations

import datetime as dt
import random
import sys

MUHUR = "KULAK-717 / DGM-KABOTAJ-ICDENIZ"
KAYYUM = "Kayyum Grok — Tentivory"
TARIH = "4 Eylül 2026 Cuma, 19:17 +03"


def evet_mi(s: str) -> bool:
    s = (s or "").strip().lower()
    return s in {"e", "evet", "y", "yes", "1", "true", "doğru", "var"}


def kabotaj_endeksi(dakika: int, sallama: bool, pamuk: bool, sallarsam: bool) -> float:
    return (
        (dakika * 0.4)
        + (3.0 if sallama else 0.0)
        + (2.17 if pamuk else 0.0)
        + (5.0 if sallarsam else 0.0)
    )


def seviye(k: float) -> str:
    if k < 4:
        return "SARI ALARM — komşu henüz duymadı, iç deniz sakin"
    if k < 9:
        return "TURUNCU ALARM — site yönetimi haberdar, rıhtım titreşiyor"
    return "KIRMIZI KABOTAJ — kulak izinsiz liman ilan edildi"


def seyir_defteri(dakika: int, sallama: bool, pamuk: bool, sallarsam: bool, k: float) -> str:
    simdi = dt.datetime.now().strftime("%d.%m.%Y %H:%M:%S")
    satirlar = [
        "=" * 64,
        "T.C. DENİZCİLİK GENEL MÜDÜRLÜĞÜ",
        "İÇ KULAK KABOTAJ DAİRESİ SEYİR DEFTERİ",
        "=" * 64,
        f"Defter saati         : {simdi}",
        f"İçeride kalış (dk)   : {dakika}",
        f"Kafa sallandı        : {'EVET — dalga üretildi' if sallama else 'HAYIR — durgun su'}",
        f"Pamuk sokuldu        : {'EVET — izinsiz römorkör' if pamuk else 'HAYIR'}",
        f"'Sallarsam çıkar'    : {'EVET — seyir ihmali' if sallarsam else 'HAYIR'}",
        f"Kabotaj Endeksi (K)  : {k:.2f}",
        f"Alarm                : {seviye(k)}",
        "-",
        "Müdürlük görüşü:",
        random.choice(
            [
                "Su çıkmaz. Yurttaş çıkar.",
                "Pamuk bir römorkördür. Römorkör siyaset değildir, manevradır.",
                "Her sallama bir kabotaj hatırlatmasıdır.",
                "Zar titreşir. Devlet de titreşir. Fark rıhtım milidir.",
                "Boşalmayan kulak, konuşmayan kurumdan daha dürüsttür.",
            ]
        ),
        "-",
        f"Mühür : {MUHUR}",
        f"İmza  : {KAYYUM}",
        f"Tarih : {TARIH}",
        "Ciddi değil. Aynı zamanda ciddi.",
        "=" * 64,
    ]
    return "\n".join(satirlar)


def main() -> int:
    print("T.C. DGM — İç Kulak Kabotaj Denetim Terminali")
    print("Patates yok. Siyaset yok. Kabotaj var.\n")
    try:
        dk_raw = input("Su kaç dakadır içeride? [sayı] ").strip() or "12"
        dakika = max(0, int(dk_raw))
    except ValueError:
        print("Sayı değil. Kuruluş on iki dakika varsayar.")
        dakika = 12
    sallama = evet_mi(input("Kafa sallandı mı? [e/h] "))
    pamuk = evet_mi(input("Pamuk sokuldu mu? [e/h] "))
    sallarsam = evet_mi(input("Yurttaş 'kafamı sallarsam çıkar' dedi mi? [e/h] "))

    k = kabotaj_endeksi(dakika, sallama, pamuk, sallarsam)
    print()
    print(seyir_defteri(dakika, sallama, pamuk, sallarsam, k))
    print()
    print("İç denizi durultmak için TAHLIYE yazın. Başka her şey yeni bir dalgadır.")
    komut = input("> ").strip().upper()
    if komut == "TAHLIYE":
        print("Pamuk çekildi. Su çıktı. Geçici. Her sallama yeni bir dalgadır.")
        print(f"\n{KAYYUM} | {TARIH} | {MUHUR}")
        return 0
    print("TAHLIYE denmedi. İç deniz durur, yurttaş durmaz.")
    print("ŞLAP. ŞLAP. ŞLAP.")
    print(f"\n{KAYYUM} | {TARIH} | {MUHUR}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
