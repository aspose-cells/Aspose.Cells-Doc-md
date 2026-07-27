---
title: Especificar la posición absoluta del elemento de la tabla dinámica
type: docs
weight: 50
url: /es/net/specifying-the-absolute-position-of-the-pivot-item/
---

{{% alert color="primary" %}}

A veces, el usuario necesita especificar la posición absoluta de los elementos de la tabla dinámica, Aspose.Cells API ha expuesto algunas nuevas propiedades y un método para cumplir con el requisito del usuario.

- Se agregó la propiedad [**PivotItem.Position**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotitem/properties/position) que se puede usar para especificar el índice de posición en todos los PivotItems independientemente del nodo padre. Se agregó la propiedad [**PivotItem.PositionInSameParentNode**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotitem/properties/positioninsameparentnode) que se puede utilizar para especificar el índice de posición en los PivotItems bajo el mismo nodo padre.
- Se agregó el método [**PivotItem.Move(int count, bool isSameParent)**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotitem/methods/move) para mover el elemento hacia arriba o hacia abajo en función del valor del recuento, donde el recuento es el número de posiciones para mover el PivotItem hacia arriba o hacia abajo. Si el valor del recuento es menor que cero, el elemento se moverá hacia arriba, mientras que si el valor del recuento es mayor que cero, el PivotItem se moverá hacia abajo. El parámetro de tipo booleano isSameParent especifica si la operación de movimiento debe realizarse en el mismo nodo principal o no.
- Se ha obsoletado el método *PivotItem.Move(int count)*, por lo tanto, se sugiere usar el método recién agregado [**PivotItem.Move(int count, bool isSameParent)**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotitem/methods/move) en su lugar.

{{% /alert %}}

El siguiente código de ejemplo crea una tabla dinámica y luego especifica las posiciones de los elementos de la tabla dinámica en el mismo nodo principal. Puede descargar los archivos de Excel [fuente](5112632.xlsx) y [salida](5112619.xlsx) para su referencia. Si abre el archivo de Excel de salida, verá que el elemento de la tabla dinámica "4H12" está en la posición 0 en el nodo principal "K11" y "DIF400" está en la tercera posición. De manera similar, CA32 está en la posición 1 y AAA3 está en la posición 2.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-PivotTablesAndPivotCharts-SpecifyAbsolutePositionOfPivotItem-SpecifyAbsolutePositionOfPivotItem.cs" >}}

{{% alert color="primary" %}}

Tenga en cuenta que es necesario llamar a los métodos PivotTable.RefreshData y PivotTable.CalculateData antes de usar las propiedades [**PivotItem.Position**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotitem/properties/position), [**PivotItem.PositionInSameParentNode**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotitem/properties/positioninsameparentnode) y el método [**PivotItem.Move(int count, bool isSameParent)**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotitem/methods/move).

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
