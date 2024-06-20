---
title: Non Primitive Şekildeki Veri
type: docs
weight: 500
url: /tr/java/data-in-non-primitive-shape/
---

## **Basit olmayan Şeklin Verilerine Erişmek**

Bazı durumlarda, yerleşik olmayan bir şekilden veriye erişmeniz gerekebilir. Yerleşik şekiller basit şekiller olarak adlandırılırken, diğerleri basit olmayan şekiller olarak adlandırılır. Örneğin, farklı eğri bağlantılı çizgiler kullanarak kendi şekillerinizi tanımlayabilirsiniz.

## **Basit Olmayan Bir Şekil**

Aspose.Cells'de basit olmayan şekiller [**AutoShapeType.NOT_PRIMITIVE**](https://reference.aspose.com/cells/java/com.aspose.cells/autoshapetype#NOT_PRIMITIVE) türüne atanır. Bunların türünü [**Shape.getAutoShapeType()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#AutoShapeType) yöntemi kullanarak kontrol edebilirsiniz.

Şekil verilerine [**Shape.getPaths()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#Paths) yöntemini kullanarak erişin. Bu, basit olmayan şekli oluşturan tüm bağlantılı yolları döndürür. Bu yollar, her bir segmentteki noktaları içeren bir liste tutan ShapePath türündedir.

Aşağıdaki kod örneği, basit olmayan şeklin yol bilgilerine erişmek için [**Shape.getPaths()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#Paths) yönteminin kullanımını göstermektedir.

**Basit olmayan bir şeklin örneğini gösterir** 

![todo:image_alt_text](data-in-non-primitive-shape_1.jpg)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-DrawingObjects-NonPrimitiveShape-1.java" >}}
