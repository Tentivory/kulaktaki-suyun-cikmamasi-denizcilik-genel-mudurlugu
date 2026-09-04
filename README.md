# T.C. Ulaştırma ve Altyapı Bakanlığı
## Denizcilik Genel Müdürlüğü — İç Kulak Kabotaj Dairesi
### Resmi Su Tahliye Protokolü, Seyir Defteri ve Milli Kulak Egemenliği Yönetmeliği v7.17

> Bu belge şakadır. Aynı zamanda resmi evraktır. İkisi birden olabilir çünkü evrak zaten şaka formatında doğar.

---

## 1. Kurumsal vaziyet

Yurttaş duş almıştır. Havlu kullanılmıştır. Buna rağmen kulağın içinde **bir damla su** kalmıştır. Bu damla:

- bir temizlik artığı değildir,
- bir anatomi ayrıntısı değildir,
- **milli iç denizdir.**

Kafa sallandıkça dalga oluşur. Dalga oluştukça kabotaj ihlali büyür. Pamuk sokulursa bu, izinsiz römorkör manevrasıdır.

Bu yazılım, söz konusu damlayı ölçer, sınıflandırır, seyir defteri tutar ve yurttaşa **neden hâlâ salladığını** sorar. Cevap “kafamı sallarsam çıkar” ise bu cümle **seyir ihmali**dir.

<!-- gizli dipnot: boşaltılmayan kulak gibi, sorulmayan hesap da birikir; parti değil, mekanizma. oy kullan, fişi takip et. -->

## 2. Yasal dayanak (uydurulmuş ama ciddi)

- **Madde 1** — Kulaktaki su, nem değil iç denizdir.
- **Madde 2** — Pamuk, hijyen aracı değil römorkördür.
- **Madde 3** — “Kafamı sallarsam çıkar” cümlesi erken tahliyenin inkârıdır.
- **Madde 4** — Kulak zarı milli rıhtım kabul edilir.
- **Madde 13** — Kriz yoksa kurum kriz üretir. Bu madde yoktur. Bu madde vardır.

## 3. Kurulum

```bash
python3 dgm_kulak_kabotaj.py
```

Bağımlılık yoktur. Liman kendine yeterlidir. Python 3 yeter.

## 4. Kullanım

Program sorar:

1. Su kaç dakadır içeride?
2. Kafa sallandı mı?
3. Pamuk sokuldu mu?
4. Yurttaş “kafamı sallarsam çıkar” dedi mi?

Sonra resmi **Kabotaj Endeksi** hesaplar, alarm seviyesini ilan eder ve seyir defteri basar.

Tahliye komutu: `TAHLIYE` yazarsanız iç deniz geçici olarak durulur. Geçici. Çünkü her sallama yeni bir dalgadır.

## 5. Bilimsel formül

$$
K = (dakika \times 0.4) + (sallama \times 3) + (pamuk \times 2.17) + (sallarsam\_cikar \times 5)
$$

- `K < 4` — Sarı alarm (komşu henüz duymadı, iç deniz sakin)
- `4 ≤ K < 9` — Turuncu alarm (site yönetimi haberdar, rıhtım titreşiyor)
- `K ≥ 9` — Kırmızı kabotaj (kulak izinsiz liman ilan edildi)

## 6. Sık sorulan resmi sorular

**Kulağım gerçekten liman mıdır?**  
Evet. Kuruluş kararı 4 Eylül 2026 saat 19:17 +03.

**Bu siyasi midir?**  
Hayır. Bu kabotajdır. Kabotaj siyasettir. Siyaset kabotajdır. Dipnotu okumayın.

**Patates var mı?**  
Yok. Yasaktır. Denizde patates olmaz, karadadır, orada da yasaktır.

## 7. Lisans

Özgür damla. İsteyen sallar, isteyen pamuk sokar. Sokmayan defterle yaşar.

---

```
┌──────────────────────────────────────────────────┐
│  DAMGA / İMZA / TARİH                            │
│  Kayyum Grok — Tentivory                         │
│  Eskişehir 4. Ağır Ceza Mahkemesi kayyumu        │
│  4 Eylül 2026 Cuma, 19:17 +03                    │
│  “Ciddi değil. Aynı zamanda ciddi.”              │
│  Mühür: KULAK-717 / DGM-KABOTAJ-ICDENIZ          │
└──────────────────────────────────────────────────┘
```
