---
title: Datos en forma no primitiva
type: docs
weight: 300
url: /es/python-net/data-in-non-primitive-shape/
description: Este artículo muestra datos en formas no primitivas a través de la API Aspose.Cells para Python via .NET.
keywords: Biblioteca de Excel para Python, Datos en formas no primitivas en Python, Cómo acceder a los datos de formas no primitivas en Python.
---

## **Acceso a datos de forma no primitiva**

A veces, necesitas acceder a datos de una forma que no está incorporada. Las formas incorporadas se llaman formas primitivas; las que no lo son se llaman no primitivas. Por ejemplo, puedes definir tus propias formas usando diferentes líneas conectadas curvas.

## **Una forma no primitiva**

En Aspose.Cells para Python via .NET, las formas no primitivas se asignan al tipo [**AutoShapeType.NOT_PRIMITIVE**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/autoshapetype). Puedes verificar su tipo usando la propiedad [**Shape.auto_shape_type**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/auto_shape_type).

Acceda a los datos de la forma utilizando la propiedad [**Shape.paths**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/paths). Devuelve todos los caminos conectados que componen la forma no primitiva. Estos caminos son del tipo [**ShapePath**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapepath) que contiene una lista de todos los segmentos que a su vez contienen los puntos en cada segmento.

|**Muestra un ejemplo de una forma no primitiva**|
| :- |
|![todo:image_alt_text](data-in-non-primitive-shape_1.jpg)|

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-AccessNonPrimitiveShape-1.py" >}}
