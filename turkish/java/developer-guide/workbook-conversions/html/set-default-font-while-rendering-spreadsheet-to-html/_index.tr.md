---
title: Elektronik tabloyu HTML e dönüştürürken varsayılan yazı tipini ayarlayın
type: docs
weight: 830
url: /tr/java/set-default-font-while-rendering-spreadsheet-to/
---

{{% alert color="primary" %}} 

Aspose.Cells, elektronik tabloyu HTML olarak oluştururken varsayılan yazı tipini ayarlamanıza olanak sağlar. Bu amaçla [HtmlSaveOptions.DefaultFontName](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#DefaultFontName) kullanın. Bu özellik, elektronik tabloda geçersiz veya mevcut olmayan yazı tipleri bulunan hücreler olduğunda kullanışlıdır. Bu durumda, bu hücreler [HtmlSaveOptions.DefaultFontName](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#DefaultFontName) özelliği ile belirtilen yazı tipinde görüntülenir.

{{% /alert %}} 
## **HTML olarak elektronik tabloyu oluştururken varsayılan yazı tipini ayarlayın**
Aşağıdaki örnek kod bir çalışma kitabı oluşturur, ilk çalışma sayfasının B4 hücresine bir metin ekler ve yazı tipini bilinmeyen/bulunmayan bir yazı tipine ayarlar. Daha sonra, çalışma kitabını farklı varsayılan yazı tipi adları olarak Courier New, Arial, Times New Roman vb. ayarlayarak HTML olarak kaydeder.

Ekran görüntüsü, [HtmlSaveOptions.DefaultFontName](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#DefaultFontName) özelliği aracılığıyla farklı varsayılan yazı tiplerinin etkisini göstermektedir.

![todo:image_alt_text](set-default-font-while-rendering-spreadsheet-to-html_1.png)

Kod, [Courier New ile üretilen çıktı HTML dosyası](5472568), [Arial ile üretilen çıktı HTML dosyası](5472567) ve [Times New Roman ile üretilen çıktı HTML dosyası](5472565) oluşturur.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-files-utility-SetDefaultFontWhileRenderingSpreadsheetToHTML-.java" >}}
