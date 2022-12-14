---
title: Datos en forma no primitiva
type: docs
weight: 500
url: /es/java/data-in-non-primitive-shape/
---
## **Acceso a datos de forma no primitiva**

A veces, necesita acceder a los datos desde una forma que no está integrada. Las formas integradas se denominan formas primitivas; los que no lo son se llaman no primitivos. Por ejemplo, puede definir sus propias formas usando diferentes líneas conectadas con curvas.

## **Una forma no primitiva**

 En Aspose.Cells, a las formas no primitivas se les asigna el tipo[**AutoShapeType.NOT_PRIMITIVE**](https://reference.aspose.com/cells/java/com.aspose.cells/autoshapetype#NOT_PRIMITIVE) . Puede verificar su tipo usando el[**Forma.getAutoShapeType()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#AutoShapeType)método.

 Acceda a los datos de la forma usando el[**Forma.getPaths()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#Paths)método. Devuelve todos los caminos conectados que comprenden la forma no primitiva. Estas rutas son del tipo ShapePath que contiene una lista de todos los segmentos que, a su vez, contienen los puntos de cada segmento.

El siguiente fragmento de código demuestra el uso de[**Forma.getPaths()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#Paths)método para acceder a información de ruta de forma no primitiva.

**Muestra un ejemplo de una forma no primitiva.** 

![todo:imagen_alternativa_texto](data-in-non-primitive-shape_1.jpg)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-DrawingObjects-NonPrimitiveShape-1.java" >}}
