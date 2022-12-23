---
title: Sayı Ayarları
type: docs
weight: 10
url: /tr/net/cells-number-settings/
---
## **Numbers ve Tarihlerin Görüntüleme Biçimlerini Ayarlama**

Microsoft Excel'in çok güçlü bir özelliği, kullanıcıların sayısal değerlerin ve tarihlerin görüntülenme biçimlerini ayarlamasına izin vermesidir. Sayısal verilerin ondalık, para birimi, yüzde, kesir veya muhasebe değerleri gibi farklı değerleri temsil etmek için kullanılabileceğini biliyoruz. Tüm bu sayısal değerler, temsil ettikleri bilgi türüne bağlı olarak farklı biçimlerde görüntülenir. Benzer şekilde, tarih veya saatin görüntülenebileceği birçok biçim vardır.
Aspose.Cells, bu işlevi destekler ve geliştiricilerin bir sayı veya tarih için herhangi bir görüntüleme formatı ayarlamasına izin verir.

### **Microsoft Excel'de Görüntü Biçimlerini Ayarlama**

Microsoft Excel'de görüntüleme biçimlerini ayarlamak için:

1. Herhangi bir hücreye sağ tıklayın.
1.  Seçme**Biçim Cells**. Herhangi bir değer türünün görüntü formatlarını ayarlamak için kullanılan bir iletişim kutusu görünecektir.

 İletişim kutusunun sol tarafında, aşağıdakiler gibi birçok değer kategorisi vardır:**Genel**, **Sayı**, **Para birimi**, **Muhasebe**, **Tarih**, **Zaman**, **Yüzde,**vb. Aspose.Cells, bu görüntüleme biçimlerinin tümünü destekler.

 Aspose.Cells bir sınıf sağlar,[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook) bu bir Microsoft Excel dosyasını temsil eder. bu[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook) sınıf bir içerir[**çalışma sayfaları**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) Excel dosyasındaki her çalışma sayfasına erişim sağlayan koleksiyon. Bir çalışma sayfası şununla temsil edilir:[**Çalışma kağıdı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıf. bu[**Çalışma kağıdı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıf bir sağlar[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) Toplamak. İçindeki her öğe[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) koleksiyon bir nesneyi temsil eder[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)sınıf.

 Aspose.Cells sağlar[**Stil Al**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle) ve[**SetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle) için yöntemler[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) sınıf. Bu yöntemler, bir hücrenin biçimlendirmesini almak ve ayarlamak için kullanılır. bu[**stil**](https://reference.aspose.com/cells/net/aspose.cells/style)class, sayıların ve tarihlerin görüntü biçimleriyle ilgilenmek için bazı yararlı özellikler sağlar.

### **Yerleşik Sayı Biçimlerini Kullanma**

 Aspose.Cells, sayıların ve tarihlerin görüntülenme biçimlerini yapılandırmak için bazı yerleşik sayı biçimleri sunar. Bu yerleşik sayı biçimleri kullanılarak uygulanabilir.[**Sayı**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/number) mülkiyeti[**stil**](https://reference.aspose.com/cells/net/aspose.cells/style) nesne. Tüm yerleşik sayı biçimlerine benzersiz sayısal değerler verilir. Geliştiriciler, istenen herhangi bir sayısal değeri atayabilir.[**Sayı**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/number) mülkiyeti[**stil**](https://reference.aspose.com/cells/net/aspose.cells/style)görüntüleme biçimini uygulamak için nesne. Bu yaklaşım hızlıdır. Aspose.Cells tarafından desteklenen yerleşik sayı biçimleri aşağıda listelenmiştir.

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

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-SettingDisplayFormats-UsingBuiltInNumberFormats-1.cs" >}}

### **Özel Sayı Biçimlerini Kullanma**

Görüntüleme biçimini ayarlamak üzere kendi özelleştirilmiş biçim dizinizi tanımlamak için[**stil**](https://reference.aspose.com/cells/net/aspose.cells/style) nesnenin[**Gelenek**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/custom)Emlak. Bu yaklaşım önceden ayarlanmış biçimleri kullanmak kadar hızlı değildir ancak daha esnektir.


{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-SettingDisplayFormats-UsingCustomNumber-1.cs" >}}

{{% alert color="primary" %}}

 Eğer kullanırsan[**Gelenek**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/custom) özelliği kullanılarak ayarlanan herhangi bir önceki biçim, sayı biçimini ayarlamak için[**Sayı**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/number)özellik geçersiz kılınır ve bunun tersi de geçerlidir.

{{% /alert %}}

## **ileri konular**
- [Style.Custom Özelliğini Ayarlarken Özel Sayı Formatını Kontrol Edin](/cells/tr/net/check-custom-number-format-when-setting-style-custom-property/)
- [Desteklenen Sayı Biçimlerinin Listesi](/cells/tr/net/list-of-supported-number-formats/)
- [Render Özel Tarih Biçimi Desen g ve ge mm dd](/cells/tr/net/render-custom-date-format-pattern-g-and-ge-mm-dd/)
- [Çalışma Kitabı için Özel Ondalık Sayı ve Grup Ayırıcıları Belirtin](/cells/tr/net/specify-custom-number-decimal-and-group-separators-for-workbook/)
- [DBNum Özel Kalıp Biçimlendirmesini Belirleme](/cells/tr/net/specifying-dbnum-custom-pattern-formatting/)
