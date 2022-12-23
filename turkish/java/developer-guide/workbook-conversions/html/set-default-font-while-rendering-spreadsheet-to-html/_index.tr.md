---
title: Elektronik tablo oluşturulurken Varsayılan Yazı Tipini HTML olarak ayarlayın
type: docs
weight: 830
url: /tr/java/set-default-font-while-rendering-spreadsheet-to/
---
{{% alert color="primary" %}} 

 Aspose.Cells, e-tabloyu işlerken varsayılan yazı tipini HTML olarak ayarlamanıza olanak tanır. Lütfen şunu kullanın:[HtmlSaveOptions.DefaultFontName](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#DefaultFontName)bu amaç için. Bu özellik, bir e-tabloda geçersiz veya mevcut olmayan yazı tiplerine sahip bazı hücreler olduğunda kullanışlıdır. Daha sonra bu hücreler, ile belirtilen bir yazı tipinde işlenecektir.[HtmlSaveOptions.DefaultFontName](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#DefaultFontName) Emlak.

{{% /alert %}} 
## **Elektronik tablo oluşturulurken Varsayılan Yazı Tipini HTML olarak ayarlayın**
Aşağıdaki örnek kod, bir çalışma kitabı oluşturur ve ilk çalışma sayfasının B4 hücresine bir miktar metin ekler ve yazı tipini bilinmeyen/var olmayan bir yazı tipine ayarlar. Ardından, Courier New, Arial, Times New Roman, vb. gibi farklı varsayılan yazı tipi adlarını ayarlayarak çalışma kitabını HTML'de kaydeder.

 Ekran görüntüsü, farklı varsayılan yazı tipi adlarını ayarlamanın etkisini gösterir.[HtmlSaveOptions.DefaultFontName](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#DefaultFontName)Emlak.

![yapılacaklar:resim_alternatif_metin](set-default-font-while-rendering-spreadsheet-to-html_1.png)

 kodu oluşturur[Courier New ile çıktı HTML dosyası](5472568) ,[Arial ile HTML çıktısı](5472567) ve[çıktı HTML dosyası Times New Roman ile](5472565).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-files-utility-SetDefaultFontWhileRenderingSpreadsheetToHTML-.java" >}}
