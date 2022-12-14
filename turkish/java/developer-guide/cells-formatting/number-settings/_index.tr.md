---
title: Sayı Ayarları
type: docs
weight: 10
url: /tr/java/cells-number-settings/
---
## **Sayıların ve Tarihlerin Görüntüleme Biçimlerini Ayarlama**

Microsoft Excel'in çok güçlü bir özelliği, kullanıcıların sayısal değerlerin ve tarihlerin görüntülenme biçimlerini ayarlamasına izin vermesidir. Sayısal verilerin ondalık, para birimi, yüzde, kesir veya muhasebe değerleri gibi farklı değerleri temsil etmek için kullanılabileceğini biliyoruz. Tüm bu sayısal değerler, temsil ettikleri bilgi türüne bağlı olarak farklı biçimlerde görüntülenir. Benzer şekilde, tarih veya saatin görüntülenebileceği birçok biçim vardır.
Aspose.Cells, bu işlevi destekler ve geliştiricilerin bir sayı veya tarih için herhangi bir görüntüleme formatı ayarlamasına izin verir.

## **Microsoft Excel'de Görüntü Biçimlerini Ayarlama**

Microsoft Excel'de görüntüleme biçimlerini ayarlamak için:

1. Herhangi bir hücreye sağ tıklayın.
1.  Seçme**Biçim Cells**. Herhangi bir değer türünün görüntü formatlarını ayarlamak için kullanılan bir iletişim kutusu görünecektir.

 İletişim kutusunun sol tarafında, aşağıdakiler gibi birçok değer kategorisi vardır:**Genel**, **Sayı**, **Para birimi**, **Muhasebe**, **Tarih**, **Zaman**, **Yüzde,**vb. Aspose.Cells, bu görüntüleme biçimlerinin tümünü destekler.

## **Yerleşik Sayı Biçimlerini Kullanma**

 Aspose.Cells, sayıların ve tarihlerin görüntülenme biçimlerini yapılandırmak için bazı yerleşik sayı biçimleri sunar. Tüm yerleşik sayı biçimlerine benzersiz sayısal değerler verilir. Geliştiriciler, istenen herhangi bir sayısal değeri atayabilir.[**Sayı**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Number) yöntemi[**stil**](https://reference.aspose.com/cells/java/com.aspose.cells/style) görüntüleme biçimini uygulamak için nesne. Bu yaklaşım hızlıdır. Aspose.Cells tarafından desteklenen yerleşik sayı biçimleri aşağıda listelenmiştir.

|**Değer**|**Tip**|**Dizeyi Biçimlendir**|
|:- |:- |:- |
|0|Genel|Genel|
|1|Ondalık|0|
|2|Ondalık|0.00|
|3|Ondalık|# ,##0
|
|4|Ondalık|# ,##0.00
|
|5|Para birimi|$#,##0;$-#,##0|
|6|Para birimi|$#,##0;[Kırmızı]$-#,##0|
|7|Para birimi|$#,##0.00;$-#,##0.00|
|8|Para birimi|$#,##0,00;[Kırmızı]$-#,##0,00|
|9|Yüzde|0%|
|10|Yüzde|0.00%|
|11|İlmi|0.00E+00|
|12|kesir|# ?/?
|
|13|kesir|# */*
|
|14|Tarih|a/g/yy|
|15|Tarih|g-aa-yy|
|16|Tarih|g-mmm|
|17|Tarih|mmm-yy|
|18|Zaman|s:dd AM/PM|
|19|Zaman|s:dd:ss AM/PM|
|20|Zaman|Hmm|
|21|Zaman|s:dd:ss|
|22|Zaman|aa/g/yy s:dd|
|37|Para birimi|# ,##0;-#,##0
|
|38|Para birimi|# ,##0;[Kırmızı]-#,##0
|
|39|Para birimi|# ,##0.00;-#,##0.00
|
|40|Para birimi|# ,##0,00;[Kırmızı]-#,##0,00
|
|41|Muhasebe|_ * #,##0_ ;_ * "_ ;_ @_|
|42|Muhasebe|_ $* #,##0_ ;_ $* "_ ;_ @_|
|43|Muhasebe|_ * #,##0.00_ ;_ * "??_ ;_ @_|
|44|Muhasebe|_ $* #,##0.00_ ;_ $* "??_ ;_ @_|
|45|Zaman|dd:ss|
|46|Zaman|sa :dd:ss|
|47|Zaman|mm:ss.0|
|48|İlmi|## 0.0E+00
|
|49|Metin|@|

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "UsingBuiltInNumberFormats-1.java" >}}

## **Özel Sayı Biçimlerini Kullanma**

Görüntüleme biçimini ayarlamak üzere kendi özelleştirilmiş biçim dizinizi tanımlamak için[**Gelenek**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Custom). Bu yaklaşım önceden ayarlanmış biçimleri kullanmak kadar hızlı değildir ancak daha esnektir.


{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "UsingCustomNumber-1.java" >}}

{{% alert color="primary" %}}

 Eğer kullanırsan[**Gelenek**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Custom) sayı formatını ayarlamak için, önceki herhangi bir format[**Sayı**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Number） is overridden and vice versa.

{{% /alert %}}

## **Advance topics**
- [Check Custom Number Format when Setting Style.Custom Property](/cells/java/check-custom-number-format-when-setting-style-custom-property/)
- [Çalışma Kitabı için Özel Ondalık Sayı ve Grup Ayırıcıları Belirtin](/cells/tr/java/specify-custom-number-decimal-and-group-separators-for-workbook/)
- [DBNum Özel Kalıp Biçimlendirmesini Belirleme](/cells/tr/java/specifying-dbnum-custom-pattern-formatting/)
