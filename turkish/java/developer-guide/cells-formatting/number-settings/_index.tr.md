---
title: Sayı Ayarları
type: docs
weight: 10
url: /tr/java/cells-number-settings/
---

## **Sayıların ve Tarihlerin Görüntü Biçimleri Ayarlama**

Microsoft Excel'in çok güçlü bir özelliği, kullanıcıların sayısal değerlerin ve tarihlerin görüntüleme formatlarını ayarlamasına izin vermesidir. Sayısal verilerin ondalık, para birimi, yüzde, kesir veya muhasebe değerleri gibi farklı değerleri temsil etmek için kullanılabileceğini biliyoruz. Tüm bu sayısal değerler, temsil ettiği bilginin türüne bağlı olarak farklı formatlarda görüntülenir. Benzer şekilde, bir tarih veya zamanın görüntülenebileceği birçok format bulunmaktadır.
Aspose.Cells bu işlevselliği destekler ve geliştiricilere bir numaranın veya tarihin herhangi bir görüntüleme formatını ayarlama izni verir.

## **Microsoft Excel'de Görüntüleme Biçimlerini Ayarlama**

Microsoft Excel'de görüntüleme formatlarını ayarlamak için:

1. Herhangi bir hücreye sağ tıklayın.
1. **Hücre Biçimi**'ni seçin. Bir diyalog kutusu görünecek ve buradan her türlü değerin görüntüleme formatlarını ayarlamak için kullanılacaktır.

Diğer bölümde, **Genel**, **Sayı**, **Para Birimi**, **Muhasebe**, **Tarih**, **Zaman**, **Yüzde** gibi birçok kategori değeri bulunmaktadır. Aspose.Cells tüm bu görüntüleme formatlarını destekler.

## **Yerleşik Sayı Biçimleri Kullanmak**

Aspose.Cells, sayıların ve tarihlerin görüntüleme biçimlerini yapılandırmak için bazı yerleşik sayı biçimleri sunar. Tüm yerleşik sayı biçimleri benzersiz sayısal değerler verilmiştir. Geliştiriciler, görüntüleme biçimini uygulamak için istenen herhangi bir sayısal değeri [**Number**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Number) yönteminin [**Style**](https://reference.aspose.com/cells/java/com.aspose.cells/style) nesnesine atayabilir. Bu yaklaşım hızlıdır. Aspose.Cells tarafından desteklenen yerleşik sayı biçimleri aşağıda listelenmiştir.

|**Değer**|**Tür**|**Biçim Dizesi**|
| :- | :- | :- |
|0|General|General|
|1|Decimal|0|
|2|Decimal|0.00|
|3|Decimal|#,##0|
|4|Decimal|#,##0.00|
|5|Currency|$#,##0;$-#,##0|
|6|Currency|$#,##0;[Red]$-#,##0|
|7|Currency|$#,##0.00;$-#,##0.00|
|8|Currency|$#,##0.00;[Red]$-#,##0.00|
|9|Percentage|0%|
|10|Percentage|0.00%|
|11|Scientific|0.00E+00|
|12|Fraction|# ?/?|
|13|Fraction|# */*|
|14|Date|m/d/yyyy|
|15|Date|d-mmm-yy|
|16|Date|d-mmm|
|17|Date|mmm-yy|
|18|Time|h:mm AM/PM|
|19|Time|h:mm:ss AM/PM|
|20|Time|h:mm|
|21|Time|h:mm:ss|
|22|Time|m/d/yy h:mm|
|37|Currency|#,##0;-#,##0|
|38|Currency|#,##0;[Red]-#,##0|
|39|Currency|#,##0.00;-#,##0.00|
|40|Currency|#,##0.00;[Red]-#,##0.00|
|41|Accounting|_ * #,##0_ ;_ * "_ ;_ @_|
|42|Accounting|_ $* #,##0_ ;_ $* "_ ;_ @_|
|43|Accounting|_ * #,##0.00_ ;_ * "??_ ;_ @_|
|44|Accounting|_ $* #,##0.00_ ;_ $* "??_ ;_ @_|
|45|Time|mm:ss|
|46|Time|h :mm:ss|
|47|Time|mm:ss.0|
|48|Scientific|##0.0E+00|
|49|Text|@|

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "UsingBuiltInNumberFormats-1.java" >}}

## **Özel Sayı Biçimleri Kullanımı**

Görüntüleme biçimini belirlemek için özel bir biçim dizesi tanımlamak için [**Custom**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Custom) kullanın. Bu yaklaşım, önceden belirlenmiş biçimler kullanmaktan daha hızlı değildir, ancak daha esnektir.


{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "UsingCustomNumber-1.java" >}}

{{% alert color="primary" %}}

Sayı biçimini belirlemek için [**Custom**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Custom) kullanırsanız, [**Sayı**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Number） kullanılarak belirlenmiş herhangi bir önceki biçim geçersiz kılır ve tam tersi de geçerlidir.

{{% /alert %}}

## **Gelişmiş Konular**
- [Stil.Oluştur Özelliğini Ayarlayarak Özel Sayı Formatını Kontrol Edin](/cells/tr/java/check-custom-number-format-when-setting-style-custom-property/)
- [Çalışmabook için Özel Sayı Ondalık ve Grup Ayraçlarını Belirleme](/cells/tr/java/specify-custom-number-decimal-and-group-separators-for-workbook/)
- [DBNum Özel Desen Biçimlendirmesini Belirleme](/cells/tr/java/specifying-dbnum-custom-pattern-formatting/)
