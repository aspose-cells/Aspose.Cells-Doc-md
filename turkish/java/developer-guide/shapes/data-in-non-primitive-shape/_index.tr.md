---
title: İlkel Olmayan Şekildeki Veriler
type: docs
weight: 500
url: /tr/java/data-in-non-primitive-shape/
---
## **İlkel Olmayan Şekildeki Verilere Erişme**

Bazen yerleşik olmayan bir şekildeki verilere erişmeniz gerekir. Yerleşik şekillere ilkel şekiller denir; olmayanlara ilkel olmayan denir. Örneğin, farklı eğri bağlantılı çizgiler kullanarak kendi şekillerinizi tanımlayabilirsiniz.

## **İlkel Olmayan Bir Şekil**

 Aspose.Cells'de, ilkel olmayan şekillere şu tür atanır:[**AutoShapeType.NOT_PRIMITIVE**](https://reference.aspose.com/cells/java/com.aspose.cells/autoshapetype#NOT_PRIMITIVE) . kullanarak türlerini kontrol edebilirsiniz.[**Shape.getAutoShapeType()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#AutoShapeType)yöntem.

 kullanarak şekil verilerine erişin.[**Shape.getPaths()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#Paths)yöntem. İlkel olmayan şekli oluşturan tüm bağlı yolları döndürür. Bu yollar, sırayla her parçadaki noktaları içeren tüm bölümlerin bir listesini tutan ShapePath türündedir.

Aşağıdaki kod parçacığı, kullanımını gösterir[**Shape.getPaths()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#Paths)ilkel olmayan şeklin yol bilgisine erişme yöntemi.

**İlkel olmayan bir şekle örnek gösterir** 

![yapılacaklar:resim_alternatif_Metin](data-in-non-primitive-shape_1.jpg)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-DrawingObjects-NonPrimitiveShape-1.java" >}}
