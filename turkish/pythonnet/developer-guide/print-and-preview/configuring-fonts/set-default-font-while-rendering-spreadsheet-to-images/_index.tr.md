---
title: Yaygın Olarak Kullanılan Yazı tipini Resimlere Dönüştürürken Belirleme
type: docs
weight: 360
url: /tr/python-net/set-default-font-while-rendering-spreadsheet-to-images/
---

{{% alert color="primary" %}}

Yayımlama sırasında elektronik tabloları görüntü olarak oluşturmak için [**ImageOrPrintOptions.default_font**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/default_font) özelliğini kullanın. Bu özellik, elektronik tablonun varsayılan yazı tipi karakterlerinizi oluşturamadığında yalnızca etkilidir. [**ImageOrPrintOptions.default_font**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/default_font) özelliği ile belirtilen varsayılan yazı tipi, geçersiz veya var olmayan yazı tiplerine sahip tüm hücreler için kullanılır.

{{% /alert %}}

## Yayımlama Sırasında Varsayılan Yazı Tipini Ayarlayın

Aşağıdaki örnek kod, bir worbook oluşturur, ilk çalışma sayfasının A4 hücresine bir metin ekler ve yazı tipini geçersiz veya varolmayan bir yazı tipine ayarlar. Ardından, çalışma sayfasının iki görüntüsünü alır. İlk görüntü, [**ImageOrPrintOptions.default_font**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/default_font) özelliğini *Courier New* olarak ayarlama ile alınır ve ikinci görüntü, [**ImageOrPrintOptions.default_font**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/default_font) özelliğini *Times New Roman* olarak ayarlama ile alınır.

Bu, [**ImageOrPrintOptions.default_font**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/default_font) özelliğini *Courier New* olarak ayarladıktan sonraki çıktı görüntüsüdür.

![todo:image_alt_text](1.png)

Bu, [**ImageOrPrintOptions.default_font**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/default_font) özelliğini *Times New Roman* olarak ayarladıktan sonraki çıktı görüntüsüdür.

![todo:image_alt_text](2.png)

## Örnek Kod

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-SetDefaultFontWhileRenderingSpreadsheet-1.cs" >}}

{{< app/cells/assistant language="python-net" >}}
