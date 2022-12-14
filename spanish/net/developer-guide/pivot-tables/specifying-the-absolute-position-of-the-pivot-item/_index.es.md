---
title: Especificación de la posición absoluta del elemento pivote
type: docs
weight: 50
url: /es/net/specifying-the-absolute-position-of-the-pivot-item/
---
{{% alert color="primary" %}}

A veces, el usuario necesita especificar la posición absoluta de los elementos pivote, Aspose.Cells API ha expuesto algunas propiedades nuevas y un método para cumplir con los requisitos del usuario.

-  Adicional[**PivotItem.Posición**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotitem/properties/position) propiedad que se puede usar para especificar el índice de posición en todos los PivotItems independientemente del nodo principal. Adicional[**PivotItem.PositionInSameParentNode**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotitem/properties/positioninsameparentnode) propiedad que se puede usar para especificar el índice de posición en PivotItems en el mismo nodo principal.
-  Adicional[**PivotItem.Move(int count, bool isSameParent)**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotitem/methods/move)para mover el elemento hacia arriba o hacia abajo en función del valor de conteo, donde conteo es el número de posiciones para mover el PivotItem hacia arriba o hacia abajo. Si el valor de conteo es menor que cero, el elemento se moverá hacia arriba donde, como si el valor de conteo fuera mayor que cero, PivotItem se moverá hacia abajo, el parámetro de tipo booleano isSameParent especifica si la operación de movimiento debe realizarse en el mismo nodo principal O no.
-  Obsoleto el*PivotItem.Move(recuento int)* por lo tanto, se sugiere utilizar el método recién agregado[**PivotItem.Move(int count, bool isSameParent)**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotitem/methods/move) en cambio.

{{% /alert %}}

 El siguiente código de ejemplo crea una tabla dinámica y luego especifica las posiciones de los elementos dinámicos en el mismo nodo principal. Puedes descargar el[Excel fuente](5112632.xlsx) y[Excel de salida](5112619.xlsx) archivos para su referencia. Si abre el archivo de salida de Excel, verá que el elemento pivote "4H12" está en la posición 0 en el padre "K11" y "DIF400" está en la tercera posición. De manera similar, CA32 está en la posición 1 y AAA3 está en la posición 2

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-PivotTablesAndPivotCharts-SpecifyAbsolutePositionOfPivotItem-SpecifyAbsolutePositionOfPivotItem.cs" >}}

{{% alert color="primary" %}}

Tenga en cuenta que es necesario llamar a los métodos PivotTable.RefreshData y PivotTable.CalculateData antes de usar[**PivotItem.Posición**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotitem/properties/position), [**PivotItem.PositionInSameParentNode**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotitem/properties/positioninsameparentnode) propiedades y[**PivotItem.Move(int count, bool isSameParent)**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotitem/methods/move) método.

{{% /alert %}}
