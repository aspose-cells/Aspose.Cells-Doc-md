---
title: Dişli Türü Akıllı Sanat Şeklinden Metin Ayıklama
type: docs
weight: 500
url: /tr/net/extract-text-from-the-gear-type-smartart-shape/
---

## **Olası Kullanım Senaryoları**

Aspose.Cells, Dişli Türü Akıllı Sanat Şeklinden metin çıkarabilir. Bunun için öncelikle [**Shape.GetResultOfSmartArt()**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/methods/getresultofsmartart) yöntemini kullanarak Akıllı Sanat Şeklini Grup Şekline dönüştürmelisiniz. Ardından [**GroupShape.GetGroupedShapes()**](https://reference.aspose.com/cells/net/aspose.cells.drawing/groupshape/methods/getgroupedshapes) yöntemini kullanarak Grup Şeklini oluşturan Tüm Bireysel Şekillerin dizisini almalısınız. Son olarak, tüm Bireysel Şekilleri bir döngü içinde tek tek dolaşabilir ve [**Shape.Text**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/text) özelliğini kullanarak metinlerini çıkarabilirsiniz.

## **Dişli Türü Akıllı Sanat Şeklinden Metin Ayıklama**

Aşağıdaki örnek kod, Dişli Türü Akıllı Sanat Şeklini içeren [örnek Excel dosyasını](67338483.xlsx) yükler. Daha sonra yukarıda tartışıldığı gibi, bireysel şekillerinden metin çıkarır. Lütfen aşağıdaki kodun konsol çıktısına bakınız.

## **Örnek Kod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "DrawingObjects-ExtractTextFromGearTypeSmartArtShape.cs" >}}

## **Konsol Çıktısı**

{{< highlight java >}}

Gear Type Shape Text: Nice

Gear Type Shape Text: Good

Gear Type Shape Text: Excellent

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
