---
title: Çalışma Sayfası İçindeki Şekil ile Metni Döndürme
type: docs
weight: 1300
url: /tr/python-net/rotate-text-with-shape-inside-the-worksheet/
---

## **Olası Kullanım Senaryoları**

Microsoft Excel kullanarak herhangi bir şeklin içine metin ekleyebilirsiniz. Microsoft Excel 2003'ü kullanan eski bir şekil eklerseniz, metin şekille birlikte dönmeyecektir. Ancak Microsoft Excel'in daha yeni sürümlerini kullanarak (2007, 2010, 2013 veya 2016 vb.) şekil eklerseniz, metin şekille birlikte döner. Metnin şekille birlikte dönüp dönmeyeceğini [**ShapeTextAlignment.rotate_text_with_shape**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing.texts/shapetextalignment/rotate_text_with_shape) özelliğini kullanarak kontrol edebilirsiniz. Bunun varsayılan değeri **true**'dur, yani metin şekille birlikte döner ama **false** olarak ayarlarsanız, metin şekille birlikte dönmez.

## **Çalışma Sayfası İçindeki Şekil ile Metni Döndürme**

Aşağıdaki örnek kod, metni şekille birlikte döndüren bir üçgen şekli içeren [örnek Excel dosyasını](64716896.xlsx) yükler. Örnek Excel dosyasını Microsoft Excel'de açarsanız ve üçgen şeklini döndürürseniz, metin de onunla birlikte döner. Kod, ardından [**ShapeTextAlignment.rotate_text_with_shape**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing.texts/shapetextalignment/rotate_text_with_shape) özelliğini **false** olarak ayarlar ve [çıktı Excel dosyasına](64716897.xlsx) kaydeder. Şimdi çıktı Excel dosyasını Microsoft Excel'de açarsanız ve üçgen şeklini döndürürseniz, metin onunla birlikte dönmez. Lütfen, çıktı Excel dosyasındaki kodun etkisini gösteren ekran görüntüsüne aşağıdan bakınız.

![todo:image_alt_text](rotate-text-with-shape-inside-the-worksheet_1.png)

## **Örnek Kod**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-Text-Options-RotateTextWithShapeInsideWorksheet.py" >}}
