---
title: E-tabloyu HTML olarak işlerken Varsayılan Yazı Tipini Ayarla
type: docs
weight: 370
url: /tr/net/set-default-font-while-rendering-spreadsheet-to/
---
{{% alert color="primary" %}}

 Aspose.Cells, e-tabloyu HTML'ye dönüştürürken varsayılan yazı tipini ayarlamanıza olanak tanır. lütfen[**HtmlSaveOptions.DefaultFontName**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/defaultfontname) bu amaç için. Bu özellik, bir e-tabloda geçersiz veya mevcut olmayan yazı tiplerine sahip bazı hücreler olduğunda kullanışlıdır. Daha sonra bu hücreler, belirtilen bir yazı tipinde işlenecektir.[**HtmlSaveOptions.DefaultFontName**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/defaultfontname) Emlak.

{{% /alert %}}

## E-tabloyu HTML olarak işlerken Varsayılan Yazı Tipini Ayarla

Aşağıdaki örnek kod, bir çalışma kitabı oluşturur ve ilk çalışma sayfasının B4 hücresine bir miktar metin ekler ve yazı tipini bilinmeyen/var olmayan bir yazı tipine ayarlar. Ardından, Courier New, Arial, Times New Roman, vb. gibi farklı varsayılan yazı tipi adlarını ayarlayarak çalışma kitabını HTML'ye kaydeder.

 Ekran görüntüsü, farklı varsayılan yazı tipi adlarını ayarlamanın etkisini gösterir.[**HtmlSaveOptions.DefaultFontName**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/defaultfontname)Emlak.

![yapılacaklar:resim_alternatif_Metin](set-default-font-while-rendering-spreadsheet-to-html_1.png)

 kodu oluşturur[Courier New ile çıktı HTML dosyası](5115516) ,[Arial ile HTML çıktısı](5115518) , ve[Times New Roman ile çıktı HTML dosyası](5115517).

## Basit kod

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-SetDefaultFontWhileRendering-1.cs" >}}
