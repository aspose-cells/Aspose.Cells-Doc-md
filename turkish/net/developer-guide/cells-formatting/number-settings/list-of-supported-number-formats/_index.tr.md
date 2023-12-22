---
title: Desteklenen Sayı Formatlarının Listesi
description: Aspose.Cells, elektronik tablo dosyalarını işlemek için çeşitli sayı formatlarını destekleyen bir .NET kitaplığıdır. Bu makalede, kullanıcıların ihtiyaçlarına göre uygun biçimi seçebilmeleri için desteklenen sayı biçimlerinin bir listesi sağlanmaktadır.
keywords: Aspose.Cells, .NET library, spreadsheet, number format, list, supported
type: docs
weight: 30
url: /tr/net/list-of-supported-number-formats/
---
##  **Aspose.Cells**
 Aspose.Cells bileşeni, sayıların ve tarihlerin görüntülenme biçimlerini yapılandırmak için bazı yerleşik sayı biçimleri sunar. Bu yerleşik sayı biçimleri aşağıdakiler kullanılarak uygulanabilir:**Sayı** mülkiyeti**Stil** nesne. Tüm yerleşik sayı biçimlerine benzersiz sayısal değerler verilir. Geliştiriciler istenilen herhangi bir sayısal değeri atayabilir.*Sayı* mülkiyet**Stil** nesne ve dolayısıyla görüntüleme formatı uygulanır. Bu yaklaşım daha hızlıdır. Aspose.Cells bileşeninin desteklediği yerleşik sayı formatları aşağıda verilmiştir:

|**Değer**|**Tip**|**Dizeyi Biçimlendir**|
| :- | :- | :- |
|0 |General | Genel|
|1 |Decimal |0 |
|2 |Decimal |0.00 |
|3 |Decimal |# ,##0
|
|4 |Decimal |# ,##0.00
|
|5 |Currency |$#,##0;$-#,##0 |
|6 |Currency |$#,##0;$-#,##0 |
|7 |Currency |$#,##0.00;$-#,##0.00 |
|8 |Currency |$#,##0.00;$-#,##0.00 |
|9 |Percentage |0% |
|10 |Percentage |0.00% |
|11 |Scientific | 0.00E+00|
|12 |Fraction |#  ?/?
|
|13 |Fraction |#  */*
|
|14 |Date | a/g/yy|
|15 |Date | d-aaa-yy|
|16 |Date | d-aa|
|17 |Date | mmm-yy|
|18 |Time | s:dd AM/PM|
|19 |Time | s:dd:ss AM/PM|
|20 |Time | Hmm|
|21 |Time | s:dd:ss|
|22 |Time | a/g/yy sa:dd|
|37 |Currency |# ,##0;-#,##0
|
|38 |Currency |# ,##0;-#,##0
|
|39 |Currency |# ,##0.00;-#,##0.00
|
|40 |Currency |# ,##0.00;-#,##0.00
|
|41 |Accounting |_ * #,##0_ ;_ * "_ ;_ @_ |
|42 |Accounting |_ $* #,##0_ ;_ $* "_ ;_ @_ |
|43 |Accounting |_ * #,##0.00_ ;_ * "??_ ;_ @_ |
|44 |Accounting |_ $* #,##0.00_ ;_ $* "??_ ;_ @_ |
|45 |Time | aa:ss|
|46 |Time | h :dd:ss|
|47 |Time | mm:ss.0|
|48 |Scientific |## 0.0E+00
|
|49 |Text |@ |
##  **Aspose.Cells Izgara Süiti**
Bildiğimiz gibi iki adet Aspose.Cells Grid kontrolü vardır: Aspose.Cells.GridDesktop & Aspose.Cells.GridWeb. Her iki kontrol de çok sayıda sayı formatını destekler ve bunlar her bir kontrole göre aşağıdaki şekilde iki bölüme ayrılır:

- Aspose.Cells.GridDesktop'ta Desteklenen Sayı Formatları
- Aspose.Cells.GridWeb'de Desteklenen Sayı Formatları
###  **Aspose.Cells.GridDesktop'ta Desteklenen Sayı Formatları**
Aspose.Cells.GridWeb ayrıca aşağıda listelenen 59 tür sayı biçimini de destekler:

|**Dizin**|**Sayı Formatları**|
| :- | :- |
|0 | Genel|
|1 |0 |
|2 |0.00 |
|3 |# ,##0
|
|4 |# ,##0.00
|
|5 |\"$\"#,##0_);(\"$\"#,##0) |
|6 |\"$\"#,##0_);(\"$\"#,##0) |
|7 |\"$\"#,##0.00_);(\"$\"#,##0.00) |
|8 |\"$\"#,##0.00;\"$\"-#,##0.00 |
|9 |0% |
|10 |0.00% |
|11 | 0.00E+00|
|12 |# ?/?
|
|13 |#  */*
|
|14 | a/g/yy|
|15 | d-aaa-yy|
|16 | d-aa|
|17 | mmm-yy|
|18 | s:dd AM/PM|
|19 | s:dd:ss AM/PM|
|20 | Hmm|
|21 | s:dd:ss|
|22 | a/g/yy sa:dd|
|23 |\"$\"#,##0;(\"$\"#,##0) |
|24 |\"$\"#,##0.00;(\"$\"#,##0.00) |
|25 |\"$\"#,##0.00;(\"$\"#,##0.00) |
|26 |\"$\"#,##0.00_);(\"$\"#,##0.00) |
|27 |M月D日|
|28 |M月D日|
|29 |M月D日|
|30 |A/G/YY|
|31 |YYYY Ay Ay Gün|
|32 | h mm mm|
|33 | h\ 时 \"mm\" ve \"ss\" 秒 \"|
|34 | tth 时 mm 分|
|35 |tth 时 mm 分 ss 秒|
|36 |YYYY mayıs ayı|
|37 |_(#,##0 );(#,##0) |
|38 |_(#,##0 );(#,##0) |
|39 |_(#,##0.00 );(#,##0.00) |
|40 |_(#,##0.00 );(#,##0.00) |
|41 |*(\"$\"* ***#,##0** **);*** **(\"$\"** _(#,##0);* (\"$\"*\"-\" *);* (@_) |
|42 |*(* ***#,##0** **);*** *(** _(#,##0);* (*-\" *);* (@_) |
|43 |*(* ***#,##0.00** **);*** *(** _(#,##0.00);* (*-\"?? *);* (@_) |
|44 |*(\"$\"* ***#,##0.00** **);*** **(\"$\"** _(#,##0.00);* (\"$\"*\"-\"?? *);* (@_) |
|45 | aa:ss|
|46 | s:dd:ss|
|47 | mm:ss.0|
|48 |## 0.0E+0
|
|49 |@ |
|50 |YYYY mayıs ayı|
|51 |M月D日|
|52 |YYYY mayıs ayı|
|53 |M月D日|
|54 |M月D日|
|55 | tth 时 mm 分|
|56 |tth 时 mm 分 ss 秒|
|57 |YYYY mayıs ayı|
|58 |M月D日|

{{% alert color="primary" %}} 

Bazı sayı biçimlerinde 月 gibi bazı karakterleri fark edebilirsiniz. Bunlar aslında Çin karakterleridir ve MS Excel'in Çince ve Japonca sürümlerinde kullanılabilir.

{{% /alert %}} 
###  **Aspose.Cells.GridWeb'de Desteklenen Sayı Formatları**
Aspose.Cells.GridWeb ayrıca aşağıda listelenen 59 tür sayı biçimini de destekler:

|**Sayı Biçimi Türleri**|**Sayı Formatları**|
| :- | :- |
| Genel| Genel|
| Ondalık1|0 |
| Ondalık2|0.00 |
| Ondalık3|# ,##0
|
| Ondalık4|# ,##0.00
|
| Para birimi1|$#,##0;$-#,##0 |
| Para birimi2|$#,##0;$-#,##0 |
| Para birimi3|$#,##0.00;$-#,##0.00 |
|Para birimi4|$#,##0.00;$-#,##0.00 |
| Para birimi5|# ,##0;-#,##0
|
| Para birimi6|# ,##0;-#,##0
|
| Para birimi7|# ,##0.00;-#,##0.00
|
| Para birimi8|# ,##0.00;-#,##0.00
|
| Para birimi9|$#,##0;($#,##0) |
| Para birimi10|$#,##0;($#,##0) |
| Para birimi11|$#,##0.00;($#,##0.00) |
| Para birimi12|$#,##0.00;($#,##0.00) |
| Yüzde1|0% |
| Yüzde2|0.00% |
| Bilimsel1| 0.00E+00|
| Bilimsel2|## 0.0E+00
|
| Kesir1|# ?/?
|
| Kesir2|#  */*
|
| Tarih1| a/g/yy|
| Tarih2| d-aaa-yy|
| Tarih3| d-aa|
| Tarih4| mmm-yy|
| Süre1| s:dd AM/PM|
| Zaman2| s:dd:ss AM/PM|
| Zaman3| Hmm|
| Zaman4| s:dd:ss|
| Zaman5| a/g/yy sa:dd|
| Zaman6| aa:ss|
| Zaman7| s:dd:ss|
| Zaman8| mm:ss.0|
| Muhasebe1|_ * #,##0_ ;_ * "_ ;_ @_ |
| Muhasebe2|_ $* #,##0_ ;_ $* "_ ;_ @_ |
| Muhasebe3|_ * #,##0.00_ ;_ * "??_ ;_ @_ |
| Muhasebe4|_ $* #,##0.00_ ;_ $* "??_ ;_ @_ |
| Metin|@ |
| DoğuTarihi1| YYYY?A?|
| DoğuTarihi2| MD?D?|
| DoğuTarihi3| MD?D?|
| DoğuTarihi4|A/G/YY|
| Doğu Tarihi5| YYYY?A?G?|
| DoğuTarihi6| YYYY?A?|
| Doğu Tarihi7| YYYY?A?|
| DoğuTarihi8| MD?D?|
| DoğuTarihi9| YYYY?A?|
| DoğuTarihi10| MD?D?|
| DoğuTarihi11| MD?D?|
| DoğuTarihi12| YYYY?A?|
| DoğuTarihi13| MD?D?|
| Doğu Saati1| Hmm?|
| Doğu Zamanı2| h?mm?ss?|
| Doğu Saati3| öyle mi? mm?|
| Doğu Zamanı4| öyle mi? mm? ss?|
| Doğu Saati5| öyle mi? mm?|
| Doğu Saati6| öyle mi? mm? ss?|

