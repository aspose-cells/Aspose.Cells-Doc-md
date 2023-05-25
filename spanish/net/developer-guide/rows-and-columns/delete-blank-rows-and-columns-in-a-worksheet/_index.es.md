---
title: Eliminar filas y columnas en blanco en una hoja de cálculo
type: docs
weight: 300
url: /es/net/delete-blank-rows-and-columns-in-a-worksheet/
---
{{% alert color="primary" %}}

Es posible eliminar todas las filas y columnas en blanco de una hoja de cálculo. Esto es útil cuando, por ejemplo, genera un archivo PDF a partir de un archivo de Excel Microsoft y desea convertir solo filas y columnas que contienen datos u objetos relacionados.

Utilice los siguientes métodos Aspose.Cells para eliminar filas y columnas vacías:

1.  Para eliminar filas en blanco, utilice el[**Cells. Eliminar filas en blanco ()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deleteblankrows) método. Tenga en cuenta que para las filas en blanco que se eliminarán, no solo se requiere que[**Row.IsBlank**](https://reference.aspose.com/cells/net/aspose.cells/row/isblank/) debe ser verdadero, pero tampoco debe haber ningún comentario visible definido para ninguna celda en esas filas, y ninguna tabla dinámica cuyo rango se cruce con ellas.
1.  Para eliminar columnas en blanco, utilice el[**Cells. Eliminar columnas en blanco ()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deleteblankcolumns) método.

{{% /alert %}}

##  C# código para eliminar filas en blanco

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-DeleteBlankRowsColumns-DeletingBlankRows-1.cs" >}}

##  C# código para eliminar columnas en blanco

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-DeleteBlankRowsColumns-DeletingBlankColumns-1.cs" >}}
