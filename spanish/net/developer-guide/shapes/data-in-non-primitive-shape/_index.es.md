---
title: Datos en forma no primitiva
type: docs
weight: 300
url: /es/net/data-in-non-primitive-shape/
---
## **Acceso a datos de forma no primitiva**

A veces, necesita acceder a los datos desde una forma que no está integrada. Las formas integradas se denominan formas primitivas; los que no lo son se llaman no primitivos. Por ejemplo, puede definir sus propias formas usando diferentes líneas conectadas con curvas.

## **Una forma no primitiva**

 En Aspose.Cells, a las formas no primitivas se les asigna el tipo[**AutoShapeType.NotPrimitive**](https://reference.aspose.com/cells/net/aspose.cells.drawing/autoshapetype) . Puede verificar su tipo usando el[**Forma.AutoShapeType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/autoshapetype)propiedad.

 Acceda a los datos de la forma usando el[**Shape.Paths**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/paths)propiedad. Devuelve todos los caminos conectados que comprenden la forma no primitiva. Estos caminos son del tipo[**ruta de forma**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapepath)que contiene una lista de todos los segmentos que a su vez contienen los puntos en cada segmento.

|**Muestra un ejemplo de una forma no primitiva.**|
|:- |
|![todo:imagen_alternativa_texto](data-in-non-primitive-shape_1.jpg)|

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-AccessNonPrimitiveShape-1.cs" >}}
