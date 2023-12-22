---
title: PDF çıktısında ve görüntüde dizenin nasıl çaprazlanacağını belirtin
type: docs
weight: 120
url: /tr/python-net/specify-how-to-cross-string-in-output-pdf-and-image/
description: PDF çıkışındaki dizeyi ve Aspose.Cells for Python via .NET API ile görüntüyü nasıl çaprazlayacağınızı öğrenin.
keywords: Python Cross String in output PDF and image
---
##  **Olası Kullanım Senaryoları**

Bir hücre metin veya dize içeriyorsa ancak bu hücrenin genişliğinden daha büyükse, sonraki sütundaki sonraki hücre boş veya boşsa dize taşar. Excel dosyanızı PDF/Resim içerisine kaydettiğinizde çapraz tipini belirterek bu taşmayı kontrol edebilirsiniz.[**MetinÇapraz Türü**](https://reference.aspose.com/cells/python-net/aspose.cells/textcrosstype/)numaralandırma. Aşağıdaki değerlere sahiptir

- *TextCrossType.DEFAULT**: Sonraki hücreye bağlı olan metni MS Excel gibi görüntüler. Bir sonraki hücre boşsa, dize kesişecek veya kesilecektir.

- *TextCrossType.CROSS_KEEP**: Dizeyi, MS Excel'in dışa aktardığı PDF/Image gibi görüntüler

- *TextCrossType.CROSS_OVERRIDE**: Diğer hücreleri çaprazlayarak tüm metni görüntüleyin ve çapraz hücrelerdeki metni geçersiz kılın

- *TextCrossType.STRICT_IN_CELL**: Yalnızca hücre genişliği dahilindeki dizeyi görüntüler.

##  **TextCrossType kullanarak PDF/Image çıktısında dizenin nasıl geçileceğini belirtin**

Aşağıdaki örnek kod, örnek Excel dosyasını yükler ve farklı bir değer belirterek PDF/Resim biçiminde kaydeder.[**MetinÇapraz Türü**](https://reference.aspose.com/cells/python-net/aspose.cells/textcrosstype/)Örnek Excel dosyası ve çıktı dosyaları aşağıdaki bağlantılardan indirilebilir:

[sampleCrossType.xlsx](81920905.xlsx)

[çıktıCrossType.pdf](81920903.pdf)

[çıktıCrossType.png](81920904.png)

###  Basit kod

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-RenderUsingTextCrossType-1.py" >}}
