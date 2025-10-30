---
title: Dişli Türü Akıllı Sanat Şeklinden Metin Ayıklama
type: docs
weight: 500
url: /tr/python-net/extract-text-from-the-gear-type-smartart-shape/
---

## **Olası Kullanım Senaryoları**

Aspose.Cells, Dişli Türü Akıllı Sanat Şeklinden metin çıkarabilir. Bunun için öncelikle [**Shape.get_result_of_smart_art()**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/get_result_of_smart_art) yöntemini kullanarak Akıllı Sanat Şeklini Grup Şekline dönüştürmelisiniz. Ardından [**GroupShape.get_grouped_shapes()**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/groupshape/get_grouped_shapes) yöntemini kullanarak Grup Şeklini oluşturan Tüm Bireysel Şekillerin dizisini almalısınız. Son olarak, tüm Bireysel Şekilleri bir döngü içinde tek tek dolaşabilir ve [**Shape.text**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/text) özelliğini kullanarak metinlerini çıkarabilirsiniz.

## **Dişli Türü Akıllı Sanat Şeklinden Metin Ayıklama**

Aşağıdaki örnek kod, Dişli Türü Akıllı Sanat Şeklini içeren [örnek Excel dosyasını](67338483.xlsx) yükler. Daha sonra yukarıda tartışıldığı gibi, bireysel şekillerinden metin çıkarır. Lütfen aşağıdaki kodun konsol çıktısına bakınız.

## **Örnek Kod**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-ExtractTextFromGearTypeSmartArtShape.py" >}}

## **Konsol Çıktısı**

{{< highlight java >}}

Gear Type Shape Text: Nice

Gear Type Shape Text: Good

Gear Type Shape Text: Excellent

{{< /highlight >}}
{{< app/cells/assistant language="python-net" >}}
