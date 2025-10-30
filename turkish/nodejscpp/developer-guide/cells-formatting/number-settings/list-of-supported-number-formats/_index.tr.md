---
title: Desteklenen Sayı Biçimleri Listesi
linktitle: Desteklenen Sayı Biçimleri Listesi
description: Aspose.Cells, çeşitli sayı biçimlerini destekleyen Node.js tabanlı bir kütüphanedir. Bu makale, kullanıcıların ihtiyaçlarına göre uygun biçimi seçebilmeleri için desteklenen sayı biçimlerinin bir listesini sunmaktadır.
keywords: Aspose.Cells, Node.js kütüphanesi, elektronik tablo, sayı biçimi, liste, destek
type: docs
weight: 30
url: /tr/nodejs-cpp/list-of-supported-number-formats/
---

## **Aspose.Cells**
Aspose.Cells bileşeni, sayıların ve tarihlerinin görüntüleme biçimlerini yapılandırmak için yerleşik bazı sayı biçimleri sunar. Bu yerleşik sayı biçimleri, **Style** nesnesinin **Number** özelliği kullanılarak uygulanabilir. Tüm yerleşik sayı biçimlerinin benzersiz sayısal değerleri vardır. Geliştiriciler, isteğe bağlı olarak herhangi bir sayısal değeri **Style** nesnesinin **Number** özelliğine atayabilir ve böylece görüntüleme biçimi uygulanır. Bu yöntem daha hızlıdır. Aspose.Cells tarafından desteklenen yerleşik sayı biçimleri aşağıda verilmiştir:

|**Değer**|**Tür**|**Biçim Dizesi**|
| :- | :- | :- |
|0 |General |General |
|1 |Decimal |0 |
|2 |Decimal |0.00 |
|3 |Decimal |#,##0 |
|4 |Decimal |#,##0.00 |
|5 |Currency |$#,##0;$-#,##0 |
|6 |Currency |$#,##0;$-#,##0 |
|7 |Currency |$#,##0.00;$-#,##0.00 |
|8 |Currency |$#,##0.00;$-#,##0.00 |
|9 |Percentage |0% |
|10 |Percentage |0.00% |
|11 |Scientific |0.00E+00 |
|12 |Fraction |# ?/? |
|13 |Fraction |# */*|
|14 |Date |m/d/yy |
|15 |Date |d-mmm-yy |
|16 |Date |d-mmm |
|17 |Date |mmm-yy |
|18 |Time |h:mm AM/PM |
|19 |Time |h:mm:ss AM/PM |
|20 |Time |h:mm |
|21 |Time |h:mm:ss |
|22 |Time |m/d/yy h:mm |
|37 |Currency |#,##0;-#,##0 |
|38 |Currency |#,##0;-#,##0 |
|39 |Currency |#,##0.00;-#,##0.00 |
|40 |Currency |#,##0.00;-#,##0.00 |
|41 |Accounting |_ * #,##0_ ;_ * "_ ;_ @_ |
|42 |Accounting |_ $* #,##0_ ;_ $* "_ ;_ @_ |
|43 |Accounting |_ * #,##0.00_ ;_ * "??_ ;_ @_ |
|44 |Accounting |_ $* #,##0.00_ ;_ $* "??_ ;_ @_ |
|45 |Time |mm:ss |
|46 |Time |h :mm:ss |
|47 |Time |mm:ss.0 |
|48 |Scientific |##0.0E+00 |
|49 |Text |@ |

## **Aspose.Cells Izgarasının Kapsamlı**
Bilindiği gibi iki Aspose.Cells Izgara kontrolleri var: Aspose.Cells.GridDesktop ve Aspose.Cells.GridWeb. Her iki kontrol de birçok sayı biçimini destekler ve her bir kontrol için aşağıdaki gibi iki bölüme ayrılır:

- Aspose.Cells.GridDesktop'da Desteklenen Sayı Biçimleri
- Aspose.Cells.GridWeb'de Desteklenen Sayı Biçimleri

### **Aspose.Cells.GridDesktop'da Desteklenen Sayı Biçimleri**
Aspose.Cells.GridWeb ayrıca aşağıda listelenen 59 türde sayı biçimini desteklemektedir:

|**Endeks**|**Sayı Biçimleri**|
| :- | :- |
|0 |General |
|1 |0 |
|2 |0.00 |
|3 |#,##0 |
|4 |#,##0.00 |
|5 |\"$\"#,##0_);(\"$\"#,##0) |
|6 |\"$\"#,##0_);(\"$\"#,##0) |
|7 |\"$\"#,##0.00_);(\"$\"#,##0.00) |
|8 |\"$\"#,##0.00;\"$\"-#,##0.00 |
|9 |0% |
|10 |0.00% |
|11 |0.00E+00 |
|12 |#?/? |
|13 |# */*|
|14 |m/d/yy |
|15 |d-mmm-yy |
|16 |d-mmm |
|17 |mmm-yy |
|18 |h:mm AM/PM |
|19 |h:mm:ss AM/PM |
|20 |h:mm |
|21 |h:mm:ss |
|22 |m/d/yy h:mm |
|23 |\"$\"#,##0;(\"$\"#,##0) |
|24 |\"$\"#,##0.00;(\"$\"#,##0.00) |
|25 |\"$\"#,##0.00;(\"$\"#,##0.00) |
|26 |\"$\"#,##0.00_);(\"$\"#,##0.00) |
|27 |M月D日|
|28 |M月D日|
|29 |M/G/YY |
|30 |YılYıl AyAy GünGün|
|31 |h saat mm dakika|
|32 |h\ saat \"mm\" dakika \"ss\" saniye|
|33 |tt saat mm dakika|
|34 |tt saat mm dakika ss saniye|
|35 |YılYıl AyAy|
|36 |_(#,##0 );(#,##0) |
|37 |_(#,##0 );(#,##0) |
|38 |_(#,##0.00 );(#,##0.00) |
|39 |_(#,##0.00 );(#,##0.00) |
|40 |*(\"$\"* ***#,##0** **);*** **(\"$\"** *_(#,##0);* (\"$\"*\"-\" *);* (@_) |
|41 |*(* ***#,##0** **);*** **(** *_(#,##0);* (*-\" *);* (@_) |
|42 |*(* ***#,##0.00** **);*** **(** *_(#,##0.00);* (*-\"?? *);* (@_) |
|43 |*(\"$\"* ***#,##0.00** **);*** **(\"$\"** *_(#,##0.00);* (\"$\"*\"-\"?? *);* (@_) |
|44 |mm:ss|
|45 |h:mm:ss|
|46 |mm:ss.0|
|47 |##0.0E+0|
|48 |@ |
|49 |YılYıl AyAy|
|50 |AyAyGünGün|
|51 |YılYıl AyAy|
|52 |AyAyGünGün|
|53 |YılYıl AyAy|
|54 |M月D日|
|55 |tth 时 mm 分 |
|56 |tth 时 mm 分 ss 秒 |
|57 |YYYY年M月|
|58 |M月D日|

{{% alert color="primary" %}} 

Bazı sayı biçimlerinde 月 gibi karakterler fark edebilirsiniz. Bunlar aslında Çin karakterleri olup Çin ve Japonya versiyonlarında kullanılabilir.

{{% /alert %}} 

### **Aspose.Cells.GridWeb'de Desteklenen Sayı Biçimleri**
Aspose.Cells.GridWeb ayrıca aşağıda listelenen 59 türde sayı biçimini desteklemektedir:

|**Sayı Biçimi Türleri**|**Sayı Biçimleri**|
| :- | :- |
|General |General |
|Decimal1 |0 |
|Decimal2 |0.00 |
|Decimal3 |#,##0 |
|Decimal4 |#,##0.00 |
|Currency1 |$#,##0;$-#,##0 |
|Currency2 |$#,##0;$-#,##0 |
|Currency3 |$#,##0.00;$-#,##0.00 |
|Currency4 |$#,##0.00;$-#,##0.00 |
|Currency5 |#,##0;-#,##0 |
|Currency6 |#,##0;-#,##0 |
|Currency7 |#,##0.00;-#,##0.00 |
|Currency8 |#,##0.00;-#,##0.00 |
|Currency9 |$#,##0;($#,##0) |
|Currency10 |$#,##0;($#,##0) |
|Currency11 |$#,##0.00;($#,##0.00) |
|Currency12 |$#,##0.00;($#,##0.00) |
|Percentage1 |0% |
|Percentage2 |0.00% |
|Scientific1 |0.00E+00 |
|Scientific2 |##0.0E+00 |
|Fraction1 |#?/? |
|Fraction2 |# */*|
|Date1 |m/d/yy |
|Date2 |d-mmm-yy |
|Date3 |d-mmm |
|Date4 |mmm-yy |
|Time1 |h:mm AM/PM |
|Time2 |h:mm:ss AM/PM |
|Time3 |h:mm |
|Time4 |h:mm:ss |
|Time5 |m/d/yy h:mm |
|Time6 |mm:ss |
|Time7 |h: mm:ss |
|Time8 |mm:ss.0 |
|Accounting1 |_ * #,##0_ ;_ * "_ ;_ @_ |
|Accounting2 |_ $* #,##0_ ;_ $* "_ ;_ @_ |
|Accounting3 |_ * #,##0.00_ ;_ * "??_ ;_ @_ |
|Accounting4 |_ $* #,##0.00_ ;_ $* "??_ ;_ @_ |
|Text |@ |
|EasternDate1 |YYYY?M? |
|EasternDate2 |M?D? |
|EasternDate3 |M?D? |
|EasternDate4 |M/D/YY |
|EasternDate5 |YYYY?M?D? |
|EasternDate6 |YYYY?M? |
|EasternDate7 |YYYY?M? |
|EasternDate8 |M?D? |
|EasternDate9 |YYYY?M? |
|EasternDate10 |M?D? |
|EasternDate11 |M?D? |
|EasternDate12 |YYYY?M? |
|EasternDate13 |M?D? |
|EasternTime1 |h?mm? |
|EasternTime2 |h?mm?ss? |
|EasternTime3 |tth?mm? |
|DoğuZamanı4 |tth?mm?ss |
|EasternTime5 |tth?mm? |
|DoğuZamanı6 |tth?mm?ss | 

{{< app/cells/assistant language="nodejs-cpp" >}}
