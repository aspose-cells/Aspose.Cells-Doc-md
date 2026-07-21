---
title: Especificando la posición absoluta del elemento de la tabla dinámica con Golang a través de C++
linktitle: Especificar la posición absoluta del elemento de la tabla dinámica
type: docs
weight: 50
url: /es/go-cpp/specifying-the-absolute-position-of-the-pivot-item/
description: Aprende cómo especificar la posición absoluta de los ítems de pivote en C++ usando Aspose.Cells.
---

{{% alert color="primary" %}}

A veces, los usuarios necesitan especificar la posición absoluta de los ítems de pivote. La API de Aspose.Cells ha expuesto algunas propiedades nuevas y un método para lograr este requisito.

- Se agregó la propiedad [**PivotItem.GetPosition()**](https://reference.aspose.com/cells/go-cpp/pivotitem/getposition/) que se puede usar para especificar el índice de posición en todos los PivotItems independientemente del nodo padre. Se agregó la propiedad [**PivotItem.GetPositionInSameParentNode()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotitem/getpositioninsameparentnode/) que se puede utilizar para especificar el índice de posición en los PivotItems bajo el mismo nodo padre.
- Se añadió el método [**PivotItem.Move(int count, bool isSameParent)**](https://reference.aspose.com/cells/go-cpp/pivotitem/move/) para mover el ítem hacia arriba o abajo basado en un valor de conteo, donde el contador es la cantidad de posiciones para mover el PivotItem hacia arriba o abajo. Si el valor del conteo es menor que cero, el ítem se moverá hacia arriba; si el valor es mayor que cero, el PivotItem se moverá hacia abajo. El parámetro booleano `isSameParent` especifica si la operación de movimiento debe realizarse en el mismo nodo padre o no.
- El método `PivotItem.Move(int count)` ha quedado obsoleto; por lo tanto, se recomienda usar el método [**PivotItem.Move(int count, bool isSameParent)**](https://reference.aspose.com/cells/go-cpp/pivotitem/move/) recién añadido.

{{% /alert %}}

El siguiente código de ejemplo crea una tabla dinámica y luego especifica las posiciones de los ítems de pivote en el mismo nodo padre. Puedes descargar los archivos de Excel [original](5112632.xlsx) y [de salida](5112619.xlsx) para referencia. Si abres el archivo Excel de salida, verás que el ítem de pivote "4H12" está en la posición 0 en el padre "K11" y "DIF400" está en la posición 3. De manera similar, CA32 está en la posición 1 y AAA3 en la posición 2.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SpecifyingTheAbsolutePositionOfThePivotItem.go" >}}
{{% alert color="primary" %}}

Ten en cuenta que es necesario llamar a los métodos `PivotTable.RefreshData` y `PivotTable.CalculateData` antes de usar [**PivotItem.GetPosition()**](https://reference.aspose.com/cells/go-cpp/pivotitem/getposition/), [**PivotItem.GetPositionInSameParentNode()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotitem/getpositioninsameparentnode/) y [**PivotItem.Move(int count, bool isSameParent)**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotitem/move/).

{{% /alert %}}
