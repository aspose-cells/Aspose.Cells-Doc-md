---
title: Yaygın Olarak Kullanılan Yazı tipini Resimlere Dönüştürürken Belirleme
type: docs
weight: 360
url: /tr/net/set-default-font-while-rendering-spreadsheet-to-images/
---

{{% alert color="primary" %}}

Yayımlama sırasında elektronik tabloları görüntü olarak oluşturmak için [**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/defaultfont) özelliğini kullanın. Bu özellik, elektronik tablonun varsayılan yazı tipi karakterlerinizi oluşturamadığında yalnızca etkilidir. [**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/defaultfont) özelliği ile belirtilen varsayılan yazı tipi, geçersiz veya var olmayan yazı tiplerine sahip tüm hücreler için kullanılır.

{{% /alert %}}

## Yayımlama Sırasında Varsayılan Yazı Tipini Ayarlayın

Aşağıdaki örnek kod, bir worbook oluşturur, ilk çalışma sayfasının A4 hücresine bir metin ekler ve yazı tipini geçersiz veya varolmayan bir yazı tipine ayarlar. Ardından, çalışma sayfasının iki görüntüsünü alır. İlk görüntü, [**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/defaultfont) özelliğini *Courier New* olarak ayarlama ile alınır ve ikinci görüntü, [**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/defaultfont) özelliğini *Times New Roman* olarak ayarlama ile alınır.

Bu, [**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/defaultfont) özelliğini *Courier New* olarak ayarladıktan sonraki çıktı görüntüsüdür.

![todo:image_alt_text](set-default-font-while-rendering-spreadsheet-to-images_1.png)

Bu, [**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/defaultfont) özelliğini *Times New Roman* olarak ayarladıktan sonraki çıktı görüntüsüdür.

![todo:image_alt_text](set-default-font-while-rendering-spreadsheet-to-images_2.png)

## Örnek Kod

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-SetDefaultFontWhileRenderingSpreadsheet-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
