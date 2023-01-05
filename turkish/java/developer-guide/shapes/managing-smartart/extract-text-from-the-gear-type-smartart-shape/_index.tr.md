---
title: Dişli Tipi SmartArt Şeklinden Metin Çıkarma
type: docs
weight: 130
url: /tr/java/extract-text-from-the-gear-type-smartart-shape/
---
## **Olası Kullanım Senaryoları**

Aspose.Cells, Gear Type Smart Art Shape'den metin çıkarabilir. Bunu yapmak için önce Smart Art Shape'i kullanarak Group Shape'e dönüştürmelisiniz.[**Shape.getResultOfSmartArt()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#getResultOfSmartArt()) yöntem. Ardından, Grup Şeklini oluşturan tüm Bireysel Şekillerin dizisini kullanarak almalısınız.[**GroupShape.getGroupedShapes()**](https://reference.aspose.com/cells/java/com.aspose.cells/groupshape#getGroupedShapes()) yöntem. Son olarak, tüm Bireysel Şekilleri bir döngüde birer birer yineleyebilir ve metinlerini kullanarak ayıklayabilirsiniz.[**şekil.metin**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#Text)Emlak.

## **Dişli Tipi SmartArt Şeklinden Metin Çıkarma**

Aşağıdaki örnek kod,[örnek excel dosyası](67338510.xlsx)Gear Type Smart Art Shape'i içerir. Ardından, yukarıda tartışıldığı gibi metni tek tek şekillerinden çıkarır. Lütfen referans için aşağıda verilen kodun konsol çıktısına bakın.

## **Basit kod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "DrawingObjects-ExtractTextFromGearTypeSmartArtShape.java" >}}

## **Konsol Çıkışı**

{{< highlight "java" >}}

Gear Type Shape Text: Nice Gear Type Shape Text: Good Gear Type Shape Text: Excellent

{{< /highlight >}}
