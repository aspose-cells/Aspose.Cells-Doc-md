---
title: İlkel Olmayan Şekildeki Veriler
type: docs
weight: 300
url: /tr/net/data-in-non-primitive-shape/
---
## **İlkel Olmayan Şekildeki Verilere Erişme**

Bazen yerleşik olmayan bir şekildeki verilere erişmeniz gerekir. Yerleşik şekillere ilkel şekiller denir; olmayanlara ilkel olmayan denir. Örneğin, farklı eğri bağlantılı çizgiler kullanarak kendi şekillerinizi tanımlayabilirsiniz.

## **İlkel Olmayan Bir Şekil**

 Aspose.Cells'de, ilkel olmayan şekillere şu tür atanır:[**AutoShapeType.NotPrimitive**](https://reference.aspose.com/cells/net/aspose.cells.drawing/autoshapetype) . kullanarak türlerini kontrol edebilirsiniz.[**Shape.AutoShapeType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/autoshapetype)Emlak.

 kullanarak şekil verilerine erişin.[**Şekil.Yollar**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/paths)Emlak. İlkel olmayan şekli oluşturan tüm bağlı yolları döndürür. Bu yollar şu türdendir:[**Şekil Yolu**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapepath)bu, sırayla her segmentteki noktaları içeren tüm segmentlerin bir listesini tutar.

|**İlkel olmayan bir şekle örnek gösterir**|
|:- |
|![yapılacaklar:resim_alternatif_Metin](data-in-non-primitive-shape_1.jpg)|

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-AccessNonPrimitiveShape-1.cs" >}}
