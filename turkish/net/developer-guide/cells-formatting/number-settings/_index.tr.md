---
title: Sayı Ayarları
description: Aspose.Cells, elektronik tablo, hücre numara ayarları, biçimlendirme, yönetim, Sayı ve Tarih Formatları
keywords: Sayı ve Tarih Formatlarını Ayarlamanın Yolu
type: docs
weight: 10
url: /tr/net/cells-number-settings/
---

## **Sayı ve Tarih Formatlarının Görüntülemesini Nasıl Ayarlayabilirsiniz**

Microsoft Excel'in çok güçlü bir özelliği, kullanıcıların sayısal değerlerin ve tarihlerin görüntüleme formatlarını ayarlamasına izin vermesidir. Sayısal verilerin ondalık, para birimi, yüzde, kesir veya muhasebe değerleri gibi farklı değerleri temsil etmek için kullanılabileceğini biliyoruz. Tüm bu sayısal değerler, temsil ettiği bilginin türüne bağlı olarak farklı formatlarda görüntülenir. Benzer şekilde, bir tarih veya zamanın görüntülenebileceği birçok format bulunmaktadır.
Aspose.Cells bu işlevselliği destekler ve geliştiricilere bir numaranın veya tarihin herhangi bir görüntüleme formatını ayarlama izni verir.

### **Microsoft Excel'de Görüntüleme Formatlarını Nasıl Ayarlayabilirsiniz**

Microsoft Excel'de görüntüleme formatlarını ayarlamak için:

1. Herhangi bir hücreye sağ tıklayın.
1. **Hücre Biçimi**'ni seçin. Bir diyalog kutusu görünecek ve buradan her türlü değerin görüntüleme formatlarını ayarlamak için kullanılacaktır.

Diğer bölümde, **Genel**, **Sayı**, **Para Birimi**, **Muhasebe**, **Tarih**, **Zaman**, **Yüzde** gibi birçok kategori değeri bulunmaktadır. Aspose.Cells tüm bu görüntüleme formatlarını destekler.

Aspose.Cells, Microsoft Excel dosyasını temsil eden bir sınıf olan [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) sunar. [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) sınıfı, Excel dosyasındaki her bir çalışma sayfasına erişim sağlayan bir koleksiyon içerir. Bir çalışma sayfası [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) sınıfı tarafından temsil edilir. [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıfı, bir koleksiyon sağlar. [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıfı, bir koleksiyon sağlar. [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) koleksiyonundaki her öğe, [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) sınıfının bir nesnesini temsil eder.

Aspose.Cells, [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) sınıfı için [**GetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle) ve [**SetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle) yöntemlerini sağlar. Bu yöntemler, bir hücrenin biçimlendirilmesini almak ve ayarlamak için kullanılır. [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) sınıfı, sayıların ve tarihlerin görüntüleme formatlarıyla ilgili bazı kullanışlı özellikler sağlar.

### **Dahili Sayı Formatlarının Nasıl Kullanılacağı**

Aspose.Cells, sayıların ve tarihlerin görüntüleme formatlarını yapılandırmak için bazı dahili sayı formatları sunar. Bu dahili sayı formatları, [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) nesnesinin [**Number**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/number) özelliğini kullanarak uygulanabilir. Tüm dahili sayı formatları benzersiz sayısal değerlere sahiptir. Geliştiriciler, istenen herhangi bir sayısal değeri [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) nesnesinin [**Number**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/number) özelliğine atayarak görüntüleme formatını uygulayabilir. Bu yaklaşım hızlıdır. Aspose.Cells tarafından desteklenen dahili sayı formatları aşağıda listelenmiştir.

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

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-SettingDisplayFormats-UsingBuiltInNumberFormats-1.cs" >}}

### **Özel Sayı Formatları Nasıl Kullanılır**

Görüntüleme formatını ayarlama için kendi özel biçim dizinizi tanımlamak için [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) nesnesinin [**Custom**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/custom) özelliğini kullanın. Bu yaklaşım, önceden belirlenmiş formatları kullanmaktan daha hızlı olmasa da daha esnektir.


{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-SettingDisplayFormats-UsingCustomNumber-1.cs" >}}

{{% alert color="primary" %}}

[**Custom**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/custom) özelliğini kullanarak sayı formatını ayarlarsanız, [**Number**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/number) özelliğini kullanarak ayarlanan önceki biçim üzerine yazılır ve aynısı geçerlidir.

{{% /alert %}}

## **Gelişmiş Konular**
- [Stil.Oluştur Özelliğini Ayarlayarak Özel Sayı Formatını Kontrol Edin](/cells/tr/net/check-custom-number-format-when-setting-style-custom-property/)
- [Desteklenen Sayı Formatları Listesi](/cells/tr/net/list-of-supported-number-formats/)
- [Özel Tarih Format Deseni g ve ge mm dd'yi Dönüştürme](/cells/tr/net/render-custom-date-format-pattern-g-and-ge-mm-dd/)
- [Çalışmabook için Özel Sayı Ondalık ve Grup Ayraçlarını Belirleme](/cells/tr/net/specify-custom-number-decimal-and-group-separators-for-workbook/)
- [DBNum Özel Desen Biçimlendirmesini Belirleme](/cells/tr/net/specifying-dbnum-custom-pattern-formatting/)
{{< app/cells/assistant language="csharp" >}}
