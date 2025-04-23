---
title: Datos en forma no primitiva
type: docs
weight: 500
url: /es/java/data-in-non-primitive-shape/
---

## **Acceso a datos de forma no primitiva**

A veces, necesitas acceder a datos de una forma que no está incorporada. Las formas incorporadas se llaman formas primitivas; las que no lo son se llaman no primitivas. Por ejemplo, puedes definir tus propias formas usando diferentes líneas conectadas curvas.

## **Una forma no primitiva**

En Aspose.Cells, se asigna el tipo [**AutoShapeType.NOT_PRIMITIVE**](https://reference.aspose.com/cells/java/com.aspose.cells/autoshapetype#NOT-PRIMITIVE) a las formas no primitivas. Puedes verificar su tipo usando el método [**Shape.getAutoShapeType()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#AutoShapeType).

Acceda a los datos de forma utilizando el método [**Shape.getPaths()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#Paths). Devuelve todos los trazados conectados que conforman la forma no primitiva. Estos trazados son del tipo ShapePath que contiene una lista de todos los segmentos que a su vez contienen los puntos en cada segmento.

El siguiente fragmento de código demuestra el uso del método [**Shape.getPaths()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#Paths) para acceder a la información de trazado de una forma no primitiva.

**Muestra un ejemplo de una forma no primitiva** 

![todo:image_alt_text](data-in-non-primitive-shape_1.jpg)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-DrawingObjects-NonPrimitiveShape-1.java" >}}
{{< app/cells/assistant language="java" >}}
