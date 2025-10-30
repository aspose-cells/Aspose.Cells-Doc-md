---
title: Golang ile C++ kullanarak Primitif olmayan Şekil içindeki veriler
linktitle: Non Primitive Şekildeki Veri
type: docs
weight: 300
url: /tr/go-cpp/data-in-non-primitive-shape/
description: Aspose.Cells kullanarak Golang ile C++ üzerinden primitif olmayan şekillerdeki verileri erişin ve yönetin
---

## **Basit olmayan Şeklin Verilerine Erişmek**

Bazı durumlarda, yerleşik olmayan bir şekilden veriye erişmeniz gerekebilir. Yerleşik şekiller basit şekiller olarak adlandırılırken, diğerleri basit olmayan şekiller olarak adlandırılır. Örneğin, farklı eğri bağlantılı çizgiler kullanarak kendi şekillerinizi tanımlayabilirsiniz.

## **Basit Olmayan Bir Şekil**

Aspose.Cells'te primitif olmayan şekillere [**AutoShapeType.NotPrimitive**](https://reference.aspose.com/cells/go-cpp/autoshapetype/) türü atanır. Onların türünü [**Shape.AutoShapeType**](https://reference.aspose.com/cells/go-cpp/autoshapetype/) özelliğini kullanarak kontrol edebilirsiniz.

Şekil verisine [**Shape.GetPaths()**](https://reference.aspose.com/cells/go-cpp/shape/getpaths/) özelliğini kullanarak erişin. Bu, primitif olmayan şekli oluşturan tüm bağlantılı yol segmentlerini döndürür. Bu yollar, her bir segmentteki noktaları içeren [**ShapePath**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapepath/) türünden oluşan bir listeyi tutar.

|**Primitif Olmayan Bir Şeklin Örneğini Gösterir**|
| :- |
|![todo:image_alt_text](data-in-non-primitive-shape_1.jpg)|

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DataInNonPrimitiveShape.go" >}}
