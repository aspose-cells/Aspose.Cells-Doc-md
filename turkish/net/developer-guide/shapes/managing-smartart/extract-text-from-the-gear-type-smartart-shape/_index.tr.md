---
title: Dişli Tipi SmartArt Şeklinden Metin Çıkarma
type: docs
weight: 500
url: /tr/net/extract-text-from-the-gear-type-smartart-shape/
---
## **Olası Kullanım Senaryoları**

 Aspose.Cells, Gear Type Smart Art Shape'den metin çıkarabilir. Bunu yapmak için önce Smart Art Shape'i kullanarak Group Shape'e dönüştürmelisiniz.[**Shape.GetResultOfSmartArt()**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/methods/getresultofsmartart) yöntem. Ardından, Grup Şeklini oluşturan tüm Bireysel Şekillerin dizisini kullanarak almalısınız.[**GroupShape.GetGroupedShapes()**](https://reference.aspose.com/cells/net/aspose.cells.drawing/groupshape/methods/getgroupedshapes) yöntem. Son olarak, tüm Bireysel Şekilleri bir döngüde birer birer yineleyebilir ve metinlerini kullanarak ayıklayabilirsiniz.[**şekil.metin**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/text)Emlak.

## **Dişli Tipi SmartArt Şeklinden Metin Çıkarma**

 Aşağıdaki örnek kod,[örnek excel dosyası](67338483.xlsx) Gear Type Smart Art Shape'i içerir. Ardından, yukarıda tartışıldığı gibi metni tek tek şekillerinden çıkarır. Lütfen referans için aşağıda verilen kodun konsol çıktısına bakın.

## **Basit kod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "DrawingObjects-ExtractTextFromGearTypeSmartArtShape.cs" >}}

## **Konsol Çıkışı**

{{< highlight "java" >}}

Gear Type Shape Text: Nice

Gear Type Shape Text: Good

Gear Type Shape Text: Excellent

{{< /highlight >}}
