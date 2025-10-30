---
title: Non Primitive Şekildeki Veri
type: docs
weight: 300
url: /tr/python-net/data-in-non-primitive-shape/
description: Bu makale, Aspose.Cells for Python via .NET API kullanarak Veri nin Basit Olmayan Şekil aracılığıyla gösterilmesini sağlar.
keywords: Python Excel Kütüphanesi, Python da Basit Olmayan Şekil İçinde Veri, Python da Basit Olmayan Şekil Verisine Nasıl Erişilir.
---

## **Basit olmayan Şeklin Verilerine Erişmek**

Bazı durumlarda, yerleşik olmayan bir şekilden veriye erişmeniz gerekebilir. Yerleşik şekiller basit şekiller olarak adlandırılırken, diğerleri basit olmayan şekiller olarak adlandırılır. Örneğin, farklı eğri bağlantılı çizgiler kullanarak kendi şekillerinizi tanımlayabilirsiniz.

## **Basit Olmayan Bir Şekil**

Aspose.Cells for Python via .NET'de, temel şekiller [**AutoShapeType.NOT_PRIMITIVE**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/autoshapetype) tipi ile atanır. Türlerini [**Shape.auto_shape_type**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/auto_shape_type) özelliği kullanarak kontrol edebilirsiniz.

Şekil verisine [**Shape.paths**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/paths) özelliğini kullanarak erişin. Bu, primitif olmayan şekli oluşturan tüm bağlantılı yol segmentlerini döndürür. Bu yollar, her bir segmentteki noktaları içeren [**ShapePath**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapepath) türünden oluşan bir listeyi tutar.

|**Primitif Olmayan Bir Şeklin Örneğini Gösterir**|
| :- |
|![todo:image_alt_text](data-in-non-primitive-shape_1.jpg)|

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-AccessNonPrimitiveShape-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
