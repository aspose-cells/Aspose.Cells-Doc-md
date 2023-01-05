---
title: Desteklenen Sayı Biçimlerinin Listesi
type: docs
weight: 30
url: /tr/net/list-of-supported-number-formats/
---
## **Aspose.Cells**
 Aspose.Cells bileşeni, sayıların ve tarihlerin görüntülenme biçimlerini yapılandırmak için bazı yerleşik sayı biçimleri sunar. Bu yerleşik sayı biçimleri kullanılarak uygulanabilir.**Sayı** mülkiyeti**stil** nesne. Tüm yerleşik sayı biçimlerine benzersiz sayısal değerler verilir. Geliştiriciler, istenen herhangi bir sayısal değeri atayabilir.*Sayı* mülkiyet**stil** nesne ve dolayısıyla görüntüleme formatı uygulanır. Bu yaklaşım daha hızlıdır. Aspose.Cells bileşeni tarafından desteklenen yerleşik sayı biçimleri aşağıda verilmiştir:

|**Değer**|**Tip**|**Dizeyi Biçimlendir**|
|:- |:- |:- |
|0 | Genel| Genel|
|1 | Ondalık|0 |
|2 | Ondalık|0.00 |
|3 | Ondalık|# ,##0
|
|4 | Ondalık|# ,##0.00
|
|5 | Para birimi|$#,##0;$-#,##0 |
|6 | Para birimi|$#,##0;$-#,##0 |
|7 | Para birimi|$#,##0.00;$-#,##0.00 |
|8 | Para birimi|$#,##0.00;$-#,##0.00 |
|9 | Yüzde|0% |
|10 | Yüzde|0.00% |
|11 | İlmi| 0.00E+00|
|12 |kesir|# ?/?
|
|13 |kesir|# */*
|
|14 | Tarih| a/g/yy|
|15 | Tarih| g-aa-yy|
|16 | Tarih| g-mmm|
|17 | Tarih| mmm-yy|
|18 | Zaman| s:dd AM/PM|
|19 | Zaman| s:dd:ss AM/PM|
|20 | Zaman| Hmm|
|21 | Zaman| s:dd:ss|
|22 | Zaman| aa/g/yy s:dd|
|37 | Para birimi|# ,##0;-#,##0
|
|38 | Para birimi|# ,##0;-#,##0
|
|39 | Para birimi|# ,##0.00;-#,##0.00
|
|40 | Para birimi|# ,##0.00;-#,##0.00
|
|41 | Muhasebe|_ * #,##0_ ;_ * "_ ;_ @_ |
|42 | Muhasebe|_ $* #,##0_ ;_ $* "_ ;_ @_ |
|43 | Muhasebe|_ * #,##0.00_ ;_ * "??_ ;_ @_ |
|44 | Muhasebe|_ $* #,##0.00_ ;_ $* "??_ ;_ @_ |
|45 | Zaman| dd:ss|
|46 | Zaman| sa :dd:ss|
|47 | Zaman| mm:ss.0|
|48 | İlmi|## 0.0E+00
|
|49 | Metin|@ |
## **Aspose.Cells Izgara Süit**
Bildiğimiz gibi iki Aspose.Cells Grid kontrolü var: Aspose.Cells.GridDesktop & Aspose.Cells.GridWeb. Her iki denetim de, her bir denetime göre aşağıdaki şekilde iki kısma ayrılan çok sayıda sayı biçimini destekler:

- Aspose.Cells.GridDesktop'ta Desteklenen Sayı Biçimleri
- Aspose.Cells.GridWeb'de Desteklenen Sayı Biçimleri
### **Aspose.Cells.GridDesktop'ta Desteklenen Sayı Biçimleri**
Aspose.Cells.GridWeb ayrıca aşağıda listelenen 59 tür sayı biçimini destekler:

|**dizin**|**Sayı Biçimleri**|
|:- |:- |
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
|13 |# */*
|
|14 | a/g/yy|
|15 | g-aa-yy|
|16 | g-mmm|
|17 | mmm-yy|
|18 | s:dd AM/PM|
|19 | s:dd:ss AM/PM|
|20 | Hmm|
|21 | s:dd:ss|
|22 | aa/g/yy s:dd|
|23 |\"$\"#,##0;(\"$\"#,##0) |
|24 |\"$\"#,##0.00;(\"$\"#,##0.00) |
|25 |\"$\"#,##0.00;(\"$\"#,##0.00) |
|26 |\"$\"#,##0.00_);(\"$\"#,##0.00) |
|27 |M月D日|
|28 |M月D日|
|29 |M月D日|
|30 |A/G/YY|
|31 |YYYY年M月D日|
|32 | 时 mm 分|
|33 |h\ 时 \"mm\" 分 \"ss\" 秒 \"|
|34 | tth 时 mm 分|
|35 |tth 时 mm 分 ss 秒|
|36 |YYYY年M月|
|37 |_(#,##0 );(#,##0) |
|38 |_(#,##0 );(#,##0) |
|39 |_(#,##0.00 );(#,##0.00) |
|40 |_(#,##0.00 );(#,##0.00) |
|41 |*(\"$\"* ***#,##0** **);*** **(\"$\"** *_(#,##0);* (\"$\"*\"-\" *);* (@_) |
|42 |*(* ***#,##0** **);*** **(** *_(#,##0);* (*-\" *);* (@_) |
|43 |*(* ***#,##0.00** **);*** **(** *_(#,##0.00);* (*-\"?? *);* (@_) |
|44 |*(\"$\"* ***#,##0.00** **);*** **(\"$\"** *_(#,##0.00);* (\"$\"*\"-\"?? *);* (@_) |
|45 | dd:ss|
|46 | s:dd:ss|
|47 | mm:ss.0|
|48 |## 0.0E+0
|
|49 |@ |
|50 |YYYY年M月|
|51 |M月D日|
|52 |YYYY年M月|
|53 |M月D日|
|54 |M月D日|
|55 | tth 时 mm 分|
|56 |tth 时 mm 分 ss 秒|
|57 |YYYY年M月|
|58 |M月D日|

{{% alert color="primary" %}} 

Bazı sayı biçimlerinde, 月 gibi bazı karakterleri fark edebilirsiniz. Bunlar aslında Çince karakterlerdir ve MS Excel'in Çince ve Japonca sürümlerinde kullanılabilir.

{{% /alert %}} 
### **Aspose.Cells.GridWeb'de Desteklenen Sayı Biçimleri**
Aspose.Cells.GridWeb ayrıca aşağıda listelenen 59 tür sayı biçimini destekler:

|**Sayı Biçimi Türleri**|**Sayı Biçimleri**|
|:- |:- |
| Genel| Genel|
| ondalık1|0 |
| ondalık2|0.00 |
| ondalık3|# ,##0
|
| ondalık4|# ,##0.00
|
| Para birimi1|$#,##0;$-#,##0 |
| Para birimi2|$#,##0;$-#,##0 |
| Para birimi3|$#,##0.00;$-#,##0.00 |
| Para birimi4|$#,##0.00;$-#,##0.00 |
| Para birimi5|# ,##0;-#,##0
|
| para birimi6|# ,##0;-#,##0
|
| para birimi7|# ,##0.00;-#,##0.00
|
| Para birimi8|# ,##0.00;-#,##0.00
|
| para birimi9|$#,##0;($#,##0) |
| Döviz10|$#,##0;($#,##0) |
| Döviz11|$#,##0.00;($#,##0.00) |
| Para birimi12|$#,##0.00;($#,##0.00) |
| Yüzde1|0% |
| Yüzde2|0.00% |
| bilimsel1| 0.00E+00|
| Bilimsel2|## 0.0E+00
|
| kesir1|# ?/?
|
| kesir2|# */*
|
| Tarih1| a/g/yy|
| Tarih2| g-aa-yy|
| Tarih3| g-mmm|
| Tarih4| mmm-yy|
| Zaman1| s:dd AM/PM|
| Zaman2| s:dd:ss AM/PM|
| Zaman3| Hmm|
| Zaman4| s:dd:ss|
| Zaman5| aa/g/yy s:dd|
| Zaman6| dd:ss|
| Zaman7| s: dd: ss|
| Zaman8| mm:ss.0|
| Muhasebe1|_ * #,##0_ ;_ * "_ ;_ @_ |
| Muhasebe2|_ $* #,##0_ ;_ $* "_ ;_ @_ |
| Muhasebe3|_ * #,##0.00_ ;_ * "??_ ;_ @_ |
| Muhasebe4|_ $* #,##0.00_ ;_ $* "??_ ;_ @_ |
| Metin|@ |
| DoğuTarihi1| YYYY?A?|
| DoğuTarihi2| Dr.|
| DoğuTarih3| Dr.|
| DoğuTarih4|A/G/YY|
| DoğuTarih5| YYYY?M?D?|
| DoğuTarih6| YYYY?A?|
| DoğuTarih7| YYYY?A?|
|DoğuTarihi8| Dr.|
| DoğuTarihi9| YYYY?A?|
| DoğuTarih10| Dr.|
| DoğuTarih11| Dr.|
| DoğuTarih12| YYYY?A?|
| DoğuTarih13| Dr.|
| Doğu Saati1| Hmm?|
| Doğu Saati2| h?mm?ss?|
| Doğu Saati3| mm?|
| Doğu Saati4| t?dd?ss?|
| Doğu Saati5| mm?|
| Doğu Saati6| t?dd?ss?|

