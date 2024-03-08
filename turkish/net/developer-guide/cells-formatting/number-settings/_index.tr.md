---
title: Numara Ayarları
description: Aspose.Cells, birçok farklı hücre numarası ayarını destekleyen elektronik tablo dosyalarıyla çalışmaya yönelik bir .NET kitaplığıdır. Bu makale, kullanıcıların elektronik tablodaki sayı biçimini gerektiği gibi ayarlayabilmeleri için hücrelerin sayı ayarlarını yönetmek için Aspose.Cells kitaplığının nasıl kullanılacağını tanıtacaktır.
keywords: Aspose.Cells, .NET library, electronic spreadsheet, cell number settings, formatting, management, Formats of Numbers and Dates
type: docs
weight: 10
url: /tr/net/cells-number-settings/
---
##  **Numbers ve Tarihlerin Görüntülenme Formatları Nasıl Ayarlanır**

Microsoft Excel'in çok güçlü bir özelliği, kullanıcıların sayısal değerlerin ve tarihlerin görüntülenme biçimlerini ayarlamasına olanak sağlamasıdır. Sayısal verilerin ondalık sayı, para birimi, yüzde, kesir veya muhasebe değerleri vb. gibi farklı değerleri temsil etmek için kullanılabileceğini biliyoruz. Tüm bu sayısal değerler, temsil ettiği bilgi türüne bağlı olarak farklı formatlarda görüntülenir. Benzer şekilde, tarih veya saatin görüntülenebileceği birçok format vardır.
Aspose.Cells bu işlevselliği destekler ve geliştiricilerin bir sayı veya tarih için herhangi bir görüntüleme biçimini ayarlamasına olanak tanır.

###  **Microsoft Excel'de Görüntü Formatları Nasıl Ayarlanır**

Microsoft Excel'de görüntü formatlarını ayarlamak için:

1. Herhangi bir hücreye sağ tıklayın.
1. *Biçim Cells**'i seçin. Her türlü değerin görüntü formatlarını ayarlamak için kullanılan bir iletişim kutusu görünecektir.

 İletişim kutusunun sol tarafında aşağıdaki gibi birçok değer kategorisi vardır:**Genel**, **Numara**, **Para birimi**, **Muhasebe**, **Tarih**, **Saat**, **Yüzde,**vb. Aspose.Cells bu ekran formatlarının tümünü destekler.

 Aspose.Cells bir sınıf sağlar,[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook) bu bir Microsoft Excel dosyasını temsil eder.[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook) sınıf bir içerir[**Çalışma sayfaları**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) Excel dosyasındaki her çalışma sayfasına erişime izin veren koleksiyon. Bir çalışma sayfası şu şekilde temsil edilir:[**Çalışma kağıdı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıf.[**Çalışma kağıdı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıf sağlar[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) Toplamak. İçindeki her öğe[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) koleksiyon bir nesneyi temsil eder[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)sınıf.

 Aspose.Cells sağlar[**GetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle) Ve[**SetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle) için yöntemler[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) sınıf. Bu yöntemler bir hücrenin biçimlendirmesini almak ve ayarlamak için kullanılır.[**Stil**](https://reference.aspose.com/cells/net/aspose.cells/style)sınıf, sayıların ve tarihlerin görüntülenme biçimleriyle ilgilenmek için bazı yararlı özellikler sağlar.

###  **Yerleşik Sayı Biçimleri Nasıl Kullanılır?**

 Aspose.Cells, sayıların ve tarihlerin görüntülenme biçimlerini yapılandırmak için bazı yerleşik sayı biçimleri sunar. Bu yerleşik sayı biçimleri aşağıdakiler kullanılarak uygulanabilir:[**Sayı**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/number) mülkiyeti[**Stil**](https://reference.aspose.com/cells/net/aspose.cells/style) nesne. Tüm yerleşik sayı biçimlerine benzersiz sayısal değerler verilir. Geliştiriciler istenilen herhangi bir sayısal değeri atayabilir.[**Sayı**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/number) mülkiyeti[**Stil**](https://reference.aspose.com/cells/net/aspose.cells/style)Görüntüleme formatını uygulayacak nesne. Bu yaklaşım hızlıdır. Aspose.Cells tarafından desteklenen yerleşik sayı biçimleri aşağıda listelenmiştir.

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

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-SettingDisplayFormats-UsingBuiltInNumberFormats-1.cs" >}}

###  **Özel Sayı Formatları Nasıl Kullanılır?**

 Görüntüleme biçimini ayarlamak amacıyla kendi özelleştirilmiş biçim dizinizi tanımlamak için[**Stil**](https://reference.aspose.com/cells/net/aspose.cells/style) nesnenin[**Gelenek**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/custom)mülk. Bu yaklaşım önceden ayarlanmış formatları kullanmak kadar hızlı değildir ancak daha esnektir.


{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-SettingDisplayFormats-UsingCustomNumber-1.cs" >}}

{{% alert color="primary" %}}

 Eğer kullanırsan[**Gelenek**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/custom) sayı biçimini ayarlama özelliği, kullanılarak ayarlanan önceki herhangi bir biçim[**Sayı**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/number)özellik geçersiz kılınır ve bunun tersi de geçerlidir.

{{% /alert %}}

##  **İleri konular**
- [Style.Custom Özelliğini Ayarlarken Özel Sayı Formatını Kontrol Edin](/cells/tr/net/check-custom-number-format-when-setting-style-custom-property/)
- [Desteklenen Sayı Formatlarının Listesi](/cells/tr/net/list-of-supported-number-formats/)
- [Özel Tarih Biçimi Desenini Oluştur g ve ge mm dd](/cells/tr/net/render-custom-date-format-pattern-g-and-ge-mm-dd/)
- [Çalışma Kitabı için Özel Sayı Ondalık ve Grup Ayırıcılarını Belirtme](/cells/tr/net/specify-custom-number-decimal-and-group-separators-for-workbook/)
- [DBNum Özel Desen Biçimlendirmesini Belirleme](/cells/tr/net/specifying-dbnum-custom-pattern-formatting/)
