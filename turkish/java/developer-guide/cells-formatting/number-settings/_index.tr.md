---
title: Numara Ayarları
type: docs
weight: 10
url: /tr/java/cells-number-settings/
---
##  **Numbers ve Tarihlerin Görüntüleme Formatlarını Ayarlama**

Microsoft Excel'in çok güçlü bir özelliği, kullanıcıların sayısal değerlerin ve tarihlerin görüntülenme biçimlerini ayarlamasına olanak sağlamasıdır. Sayısal verilerin ondalık sayı, para birimi, yüzde, kesir veya muhasebe değerleri vb. gibi farklı değerleri temsil etmek için kullanılabileceğini biliyoruz. Tüm bu sayısal değerler, temsil ettiği bilgi türüne bağlı olarak farklı formatlarda görüntülenir. Benzer şekilde, tarih veya saatin görüntülenebileceği birçok format vardır.
Aspose.Cells bu işlevselliği destekler ve geliştiricilerin bir sayı veya tarih için herhangi bir görüntüleme biçimini ayarlamasına olanak tanır.

##  **Microsoft Excel'de Görüntü Formatlarını Ayarlama**

Microsoft Excel'de görüntü formatlarını ayarlamak için:

1. Herhangi bir hücreye sağ tıklayın.
1. *Biçim Cells**'i seçin. Her türlü değerin görüntü formatlarını ayarlamak için kullanılan bir iletişim kutusu görünecektir.

 İletişim kutusunun sol tarafında aşağıdaki gibi birçok değer kategorisi vardır:**Genel**, **Numara**, **Para birimi**, **Muhasebe**, **Tarih**, **Saat**, **Yüzde,**vb. Aspose.Cells bu ekran formatlarının tümünü destekler.

##  **Yerleşik Sayı Biçimlerini Kullanma**

Aspose.Cells, sayıların ve tarihlerin görüntülenme biçimlerini yapılandırmak için bazı yerleşik sayı biçimleri sunar. Tüm yerleşik sayı biçimlerine benzersiz sayısal değerler verilir. Geliştiriciler istenilen herhangi bir sayısal değeri atayabilir.[**Sayı**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Number) yöntemi[**Stil**](https://reference.aspose.com/cells/java/com.aspose.cells/style) Görüntüleme formatını uygulayacak nesne. Bu yaklaşım hızlıdır. Aspose.Cells tarafından desteklenen yerleşik sayı biçimleri aşağıda listelenmiştir.

|**Değer**|**Tip**|**Dizeyi Biçimlendir**|
| :- | :- | :- |
|0|General|Genel|
|1|Decimal|0|
|2|Decimal|0.00|
|3|Decimal|# ,##0
|
|4|Decimal|# ,##0.00
|
|5|Currency|$#,##0;$-#,##0|
|6|Currency|$#,##0;[Kırmızı]$-#,##0|
|7|Currency|$#,##0.00;$-#,##0.00|
|8|Currency|$#,##0.00;[Kırmızı]$-#,##0.00|
|9|Percentage|0%|
|10|Percentage|0.00%|
|11|Scientific|0.00E+00|
|12|Fraction|#  ?/?
|
|13|Fraction|#  */*
|
|14|Date|a/g/yyyy|
|15|Date|d-aaa-yy|
|16|Date|d-aa|
|17|Date|mmm-yy|
|18|Time|s:dd AM/PM|
|19|Time|s:dd:ss AM/PM|
|20|Time|Hmm|
|21|Time|s:dd:ss|
|22|Time|a/g/yy sa:dd|
|37|Currency|# ,##0;-#,##0
|
|38|Currency|# ,##0;[Kırmızı]-#,##0
|
|39|Currency|# ,##0.00;-#,##0.00
|
|40|Currency|# ,##0,00;[Kırmızı]-#,##0,00
|
|41|Accounting|_ * #,##0_ ;_ * "_ ;_ @_|
|42|Accounting|_ $* #,##0_ ;_ $* "_ ;_ @_|
|43|Accounting|_ * #,##0.00_ ;_ * "??_ ;_ @_|
|44|Accounting|_ $* #,##0.00_ ;_ $* "??_ ;_ @_|
|45|Time|aa:ss|
|46|Time|h :dd:ss|
|47|Time|mm:ss.0|
|48|Scientific|## 0.0E+00
|
|49|Text|@|

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "UsingBuiltInNumberFormats-1.java" >}}

##  **Özel Sayı Biçimlerini Kullanma**

 Görüntüleme biçimini ayarlamak amacıyla kendi özelleştirilmiş biçim dizinizi tanımlamak için[**Gelenek**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Custom). Bu yaklaşım önceden ayarlanmış formatları kullanmak kadar hızlı değildir ancak daha esnektir.


{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "UsingCustomNumber-1.java" >}}

{{% alert color="primary" %}}

 Eğer kullanırsan[**Gelenek**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Custom) sayı formatını ayarlamak için, önceki herhangi bir format kullanılarak ayarlanmıştır.[**Sayı**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Number） is overridden and vice versa.

{{% /alert %}}

## **Advance topics**
- [Check Custom Number Format when Setting Style.Custom Property](/cells/java/check-custom-number-format-when-setting-style-custom-property/)
- [Çalışma Kitabı için Özel Sayı Ondalık ve Grup Ayırıcılarını Belirtme](/cells/tr/java/specify-custom-number-decimal-and-group-separators-for-workbook/)
- [DBNum Özel Desen Biçimlendirmesini Belirleme](/cells/tr/java/specifying-dbnum-custom-pattern-formatting/)
