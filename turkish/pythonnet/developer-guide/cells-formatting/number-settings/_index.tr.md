---
title: Sayı Ayarları
description: Aspose.Cells, hücre sayı ayarlarını destekleyen ve elektronik tablo dosyalarıyla çalışmak için kullanılan bir Python kütüphanesidir. Bu makale, hücrelerin sayı ayarlarını yönetmek için Aspose.Cells kütüphanesinin nasıl kullanılacağını tanıtacaktır, böylece kullanıcılar gerek duydukları gibi sayı biçimini ayarlayabilirler.
keywords: Aspose.Cells, Python kütüphanesi, elektronik tablo, hücre sayı ayarları, biçimlendirme, yönetim, Sayı ve Tarih Biçimleri
type: docs
weight: 10
url: /tr/python-net/cells-number-settings/
---

## **Sayı ve Tarih Formatlarının Görüntülemesini Nasıl Ayarlayabilirsiniz**

Microsoft Excel'in çok güçlü bir özelliği, kullanıcıların sayısal değerlerin ve tarihlerin görüntüleme formatlarını ayarlamasına izin vermesidir. Sayısal verilerin ondalık, para birimi, yüzde, kesir veya muhasebe değerleri gibi farklı değerleri temsil etmek için kullanılabileceğini biliyoruz. Tüm bu sayısal değerler, temsil ettiği bilginin türüne bağlı olarak farklı formatlarda görüntülenir. Benzer şekilde, bir tarih veya zamanın görüntülenebileceği birçok format bulunmaktadır.
Aspose.Cells for Python via .NET bu işlevselliği destekler ve geliştiricilerin herhangi bir sayı veya tarihin gösterim biçimini ayarlamasına izin verir.

### **Microsoft Excel'de Görüntüleme Formatlarını Nasıl Ayarlayabilirsiniz**

Microsoft Excel'de görüntüleme formatlarını ayarlamak için:

1. Herhangi bir hücreye sağ tıklayın.
1. **Hücre Biçimi**'ni seçin. Bir diyalog kutusu görünecek ve buradan her türlü değerin görüntüleme formatlarını ayarlamak için kullanılacaktır.

İletişim kutusunun sol tarafında, **Genel**, **Sayı**, **Para Birimi**, **Muhasebe**, **Tarih**, **Saat**, **Yüzde** gibi çeşitli değer kategorileri vardır. Aspose.Cells for Python via .NET, bunların tüm görünüm biçimlerini destekler.

Aspose.Cells for Python via .NET, Microsoft Excel dosyasını temsil eden [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) adlı bir sınıf sağlar. [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) sınıfı, Excel dosyasındaki her çalışma sayfasına erişim sağlayan bir [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets) koleksiyonu içerir. Bir çalışma sayfası, [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) sınıfı ile temsil edilir. [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) sınıfı, bir [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells) koleksiyonu sağlar. [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells) koleksiyonundaki her öğe, bir [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell) sınıfı nesnesini temsil eder.

Aspose.Cells for Python via .NET, [**get_style**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_style) ve [**set_style**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/set_style) yöntemlerini sağlar. Bu yöntemler, hücrenin biçimlendirmesini almak ve ayarlamak için kullanılır. [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) sınıfı, sayıların ve tarihlerin görüntü biçimleriyle ilgilenen bazı kullanışlı özellikler sağlar.

### **Dahili Sayı Formatlarının Nasıl Kullanılacağı**

Aspose.Cells for Python via .NET, bu işlevselliği sağlar ve geliştiricilerin herhangi bir sayı veya tarihin gösterim biçimini ayarlamasına izin verir.

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

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-UsingBuiltInNumberFormats-1.py" >}}

### **Özel Sayı Formatları Nasıl Kullanılır**

Görüntüleme formatını ayarlama için kendi özel biçim dizinizi tanımlamak için [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) nesnesinin [**custom**](https://reference.aspose.com/cells/python-net/aspose.cells/style/custom) özelliğini kullanın. Bu yaklaşım, önceden belirlenmiş formatları kullanmaktan daha hızlı olmasa da daha esnektir.


{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-UsingCustomNumber-1.py" >}}

{{% alert color="primary" %}}

[**custom**](https://reference.aspose.com/cells/python-net/aspose.cells/style/custom) özelliğini kullanarak sayı formatını ayarlarsanız, [**number**](https://reference.aspose.com/cells/python-net/aspose.cells/style/number) özelliğini kullanarak ayarlanan önceki biçim üzerine yazılır ve aynısı geçerlidir.

{{% /alert %}}

## **Gelişmiş Konular**
- [Stil.Oluştur Özelliğini Ayarlayarak Özel Sayı Formatını Kontrol Edin](/cells/tr/python-net/check-custom-number-format-when-setting-style-custom-property/)
- [Desteklenen Sayı Formatları Listesi](/cells/tr/python-net/list-of-supported-number-formats/)
- [Özel Tarih Format Deseni g ve ge mm dd'yi Dönüştürme](/cells/tr/python-net/render-custom-date-format-pattern-g-and-ge-mm-dd/)
- [Çalışmabook için Özel Sayı Ondalık ve Grup Ayraçlarını Belirleme](/cells/tr/python-net/specify-custom-number-decimal-and-group-separators-for-workbook/)
- [DBNum Özel Desen Biçimlendirmesini Belirleme](/cells/tr/python-net/specifying-dbnum-custom-pattern-formatting/)

