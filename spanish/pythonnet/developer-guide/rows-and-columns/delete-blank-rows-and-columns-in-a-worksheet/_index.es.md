---
title: Eliminar Filas y Columnas en Blanco en una Hoja de Cálculo
type: docs
weight: 300
url: /es/python-net/delete-blank-rows-and-columns-in-a-worksheet/
description: Este artículo describe cómo eliminar filas y columnas en blanco en una hoja de cálculo con la biblioteca Aspose.Cells para Python via .NET.
keywords: Python Excel Library, Eliminación de filas en blanco en Python, Eliminar filas en blanco en Python, Eliminación de columnas en blanco en Python, Eliminar columnas en blanco en Python, Eliminar o quitar filas y columnas en blanco en Python.
---

{{% alert color="primary" %}}

Es posible eliminar todas las filas y columnas en blanco de una hoja de cálculo. Esto es útil, por ejemplo, al generar un archivo PDF a partir de un archivo de Microsoft Excel y se desea convertir solo las filas y columnas que contienen datos u objetos relacionados.

Use los siguientes métodos de Aspose.Cells para eliminar filas y columnas vacías:

1. Para eliminar filas en blanco, utilice el método [**Cells.delete_blank_rows()**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/delete_blank_rows). Tenga en cuenta que, para las filas en blanco que se eliminarán, no solo es necesario que [**Row.is_blank**](https://reference.aspose.com/cells/python-net/aspose.cells/row/is_blank/) sea verdadero, sino que también no debe haber comentarios visibles definidos para ninguna celda en esas filas, y no debe haber una tabla dinámica cuyo rango se interseque con ellas.
1. Para eliminar columnas en blanco, utilice el método [**Cells.delete_blank_columns()**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/delete_blank_columns).

{{% /alert %}}

## Código C# para eliminar filas en blanco

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-DeletingBlankRows-1.py" >}}

## Código C# para eliminar columnas en blanco

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-DeletingBlankColumns-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
