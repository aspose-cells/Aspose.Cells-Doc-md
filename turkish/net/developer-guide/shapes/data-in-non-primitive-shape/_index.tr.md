---
title: Non Primitive Şekildeki Veri
type: docs
weight: 300
url: /tr/net/data-in-non-primitive-shape/
---

## **Basit olmayan Şeklin Verilerine Erişmek**

Bazı durumlarda, yerleşik olmayan bir şekilden veriye erişmeniz gerekebilir. Yerleşik şekiller basit şekiller olarak adlandırılırken, diğerleri basit olmayan şekiller olarak adlandırılır. Örneğin, farklı eğri bağlantılı çizgiler kullanarak kendi şekillerinizi tanımlayabilirsiniz.

## **Basit Olmayan Bir Şekil**

Aspose.Cells'te primitif olmayan şekillere [**AutoShapeType.NotPrimitive**](https://reference.aspose.com/cells/net/aspose.cells.drawing/autoshapetype) türü atanır. Onların türünü [**Shape.AutoShapeType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/autoshapetype) özelliğini kullanarak kontrol edebilirsiniz.

Şekil verisine [**Shape.Paths**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/paths) özelliğini kullanarak erişin. Bu, primitif olmayan şekli oluşturan tüm bağlantılı yol segmentlerini döndürür. Bu yollar, her bir segmentteki noktaları içeren [**ShapePath**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapepath) türünden oluşan bir listeyi tutar.

|**Primitif Olmayan Bir Şeklin Örneğini Gösterir**|
| :- |
|![todo:image_alt_text](data-in-non-primitive-shape_1.jpg)|

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-AccessNonPrimitiveShape-1.cs" >}}
