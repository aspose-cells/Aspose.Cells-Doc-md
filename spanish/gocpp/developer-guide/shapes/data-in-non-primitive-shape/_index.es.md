---
title: Datos en formas no primitivas con Golang a través de C++
linktitle: Datos en forma no primitiva
type: docs
weight: 300
url: /es/go-cpp/data-in-non-primitive-shape/
description: Acceder y manipular datos en formas no primitivas usando Aspose.Cells con Golang a través de C++.
---

## **Acceso a datos de forma no primitiva**

A veces, necesitas acceder a datos de una forma que no está incorporada. Las formas incorporadas se llaman formas primitivas; las que no lo son se llaman no primitivas. Por ejemplo, puedes definir tus propias formas usando diferentes líneas conectadas curvas.

## **Una forma no primitiva**

En Aspose.Cells, a las formas no primitivas se les asigna el tipo [**AutoShapeType.NotPrimitive**](https://reference.aspose.com/cells/go-cpp/autoshapetype/). Puede verificar su tipo utilizando la propiedad [**Shape.AutoShapeType**](https://reference.aspose.com/cells/go-cpp/autoshapetype/).

Acceda a los datos de la forma utilizando la propiedad [**Shape.GetPaths()**](https://reference.aspose.com/cells/go-cpp/shape/getpaths/). Devuelve todos los caminos conectados que componen la forma no primitiva. Estos caminos son del tipo [**ShapePath**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapepath/) que contiene una lista de todos los segmentos que a su vez contienen los puntos en cada segmento.

|**Muestra un ejemplo de una forma no primitiva**|
| :- |
|![todo:image_alt_text](data-in-non-primitive-shape_1.jpg)|

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DataInNonPrimitiveShape.go" >}}
