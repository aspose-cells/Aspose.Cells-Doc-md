---
title: Datos en forma no primitiva
type: docs
weight: 300
url: /es/net/data-in-non-primitive-shape/
---

## **Acceso a datos de forma no primitiva**

A veces, necesitas acceder a datos de una forma que no está incorporada. Las formas incorporadas se llaman formas primitivas; las que no lo son se llaman no primitivas. Por ejemplo, puedes definir tus propias formas usando diferentes líneas conectadas curvas.

## **Una forma no primitiva**

En Aspose.Cells, a las formas no primitivas se les asigna el tipo [**AutoShapeType.NotPrimitive**](https://reference.aspose.com/cells/net/aspose.cells.drawing/autoshapetype). Puede verificar su tipo utilizando la propiedad [**Shape.AutoShapeType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/autoshapetype).

Acceda a los datos de la forma utilizando la propiedad [**Shape.Paths**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/paths). Devuelve todos los caminos conectados que componen la forma no primitiva. Estos caminos son del tipo [**ShapePath**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapepath) que contiene una lista de todos los segmentos que a su vez contienen los puntos en cada segmento.

|**Muestra un ejemplo de una forma no primitiva**|
| :- |
|![todo:image_alt_text](data-in-non-primitive-shape_1.jpg)|

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-AccessNonPrimitiveShape-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
