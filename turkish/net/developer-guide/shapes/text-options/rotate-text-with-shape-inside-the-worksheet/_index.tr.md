---
title: Çalışma Sayfasının İçinde Şekilli Metni Döndürme
type: docs
weight: 1300
url: /tr/net/rotate-text-with-shape-inside-the-worksheet/
---
## **Olası Kullanım Senaryoları**

Microsoft Excel'i kullanarak herhangi bir şeklin içine metin ekleyebilirsiniz. Çok eski Microsoft Excel 2003'ü kullanarak şekil eklerseniz, metin şekil ile birlikte dönmeyecektir. Ancak, 2007, 2010, 2013 veya 2016 gibi Microsoft Excel'in daha yeni sürümlerini kullanarak şekil eklerseniz, metin şekille birlikte döner. Metnin şekille birlikte dönüp dönmeyeceğini kontrol edebilirsiniz.[**ShapeTextAlignment.RotateTextWithShape**](https://reference.aspose.com/cells/net/aspose.cells.drawing.texts/shapetextalignment/properties/rotatetextwithshape) Emlak. Bunun varsayılan değeri**doğru**bu, metnin şekille birlikte döneceği anlamına gelir, ancak**YANLIŞ**, metin şekille birlikte dönmez.

## **Çalışma Sayfasının İçinde Şekilli Metni Döndürme**

 Aşağıdaki örnek kod,[örnek excel dosyası](64716896.xlsx) üçgen şekle sahip olan ve metni şekille birlikte dönen. Örnek Excel dosyasını Microsoft Excel'de açıp üçgen şeklini döndürürseniz metin de onunla birlikte döner. Kod daha sonra ayarlar[**ShapeTextAlignment.RotateTextWithShape**](https://reference.aspose.com/cells/net/aspose.cells.drawing.texts/shapetextalignment/properties/rotatetextwithshape) olarak mülkiyet**YANLIŞ** olarak kaydeder ve[çıktı excel dosyası](64716897.xlsx). Şimdi çıktı Excel dosyasını Microsoft Excel'de açarsanız ve üçgen şeklini döndürürseniz, metin onunla birlikte dönmez. Referans için lütfen kodun örnek Excel dosyası üzerindeki etkisini gösteren aşağıdaki ekran görüntüsüne bakın.

![yapılacaklar:resim_alternatif_metin](rotate-text-with-shape-inside-the-worksheet_1.png)

## **Basit kod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "DrawingObjects-RotateTextWithShapeInsideWorksheet.cs" >}}
