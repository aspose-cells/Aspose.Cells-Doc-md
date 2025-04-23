---
title: Elektronik tabloyu HTML e dönüştürürken varsayılan yazı tipini ayarlayın
type: docs
weight: 370
url: /tr/net/set-default-font-while-rendering-spreadsheet-to/
---

{{% alert color="primary" %}}

Aspose.Cells, elektronik tabloyu HTML'e dönüştürürken varsayılan yazı tipini ayarlamanıza olanak tanır. Bu amaçla [**HtmlSaveOptions.DefaultFontName**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/defaultfontname) özelliğini kullanın. Bu özellik, elektronik tabloda geçersiz veya mevcut olmayan yazı tiplerine sahip hücreler varsa kullanışlıdır. O zaman bu hücreler [**HtmlSaveOptions.DefaultFontName**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/defaultfontname) özelliği ile belirtilen bir yazı tipinde oluşturulacaktır.

{{% /alert %}}

## Elektronik tabloyu HTML'e dönüştürürken varsayılan yazı tipini ayarlayın

Aşağıdaki örnek kod bir çalışma kitabı oluşturur, ilk çalışma sayfasının B4 hücresine bir metin ekler ve yazı tipini bilinmeyen/bulunmayan bir yazı tipine ayarlar. Daha sonra, çalışma kitabını farklı varsayılan yazı tipi adları olarak Courier New, Arial, Times New Roman vb. ayarlayarak HTML olarak kaydeder.

Ekran görüntüsü, [**HtmlSaveOptions.DefaultFontName**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/defaultfontname) özelliği aracılığıyla farklı varsayılan yazı tipi adları ayarlamanın etkisini göstermektedir.

![todo:image_alt_text](set-default-font-while-rendering-spreadsheet-to-html_1.png)

Kod, [Courier New ile](5115516), [Arial ile](5115518) ve [Times New Roman ile](5115517) çıktı HTML dosyasını oluşturur.

## Örnek Kod

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-SetDefaultFontWhileRendering-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
