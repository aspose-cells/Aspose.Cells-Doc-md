---
title: Eliminar Filas y Columnas en Blanco en una Hoja de Cálculo
type: docs
weight: 300
url: /es/net/delete-blank-rows-and-columns-in-a-worksheet/
---

{{% alert color="primary" %}}

Es posible eliminar todas las filas y columnas en blanco de una hoja de cálculo. Esto es útil, por ejemplo, al generar un archivo PDF a partir de un archivo de Microsoft Excel y se desea convertir solo las filas y columnas que contienen datos u objetos relacionados.

Use los siguientes métodos de Aspose.Cells para eliminar filas y columnas vacías:

1. Para eliminar filas en blanco, utilice el método [**Cells.DeleteBlankRows()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deleteblankrows). Tenga en cuenta que, para las filas en blanco que se eliminarán, no solo es necesario que [**Row.IsBlank**](https://reference.aspose.com/cells/net/aspose.cells/row/isblank/) sea verdadero, sino que también no debe haber comentarios visibles definidos para ninguna celda en esas filas, y no debe haber una tabla dinámica cuyo rango se interseque con ellas.
1. Para eliminar columnas en blanco, utilice el método [**Cells.DeleteBlankColumns()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deleteblankcolumns).

{{% /alert %}}

## Código C# para eliminar filas en blanco

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-DeleteBlankRowsColumns-DeletingBlankRows-1.cs" >}}

## Código C# para eliminar columnas en blanco

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-DeleteBlankRowsColumns-DeletingBlankColumns-1.cs" >}}
