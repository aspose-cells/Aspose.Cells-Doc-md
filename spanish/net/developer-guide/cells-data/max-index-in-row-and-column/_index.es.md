---
title: Obtener el índice de columna máximo en fila y el índice de fila máximo en columna
type: docs
weight: 600
url: /es/net/get-max-index-in-row-and-column/
description: Aprenda cómo obtener el índice de columna máximo en fila y el índice de fila máximo en columna a través de la API Aspose.Cells for .NET.
keywords: Obtener el índice de columna máximo en fila, obtener el índice de fila máximo en columna, obtener el índice de columna de datos máximo en fila, obtener el índice de fila de datos máximo en columna. 
---

## **Escenarios de uso posibles**
Cuando solo necesita manipular algunos datos en las filas o columnas, es necesario conocer el rango de datos de las filas y columnas. Aspose.Cells ofrece esta función. Para obtener el índice de columna máximo en una fila, puede obtener las propiedades [Row.LastCell](https://reference.aspose.com/cells/net/aspose.cells/row/lastcell/) y [Row.LastDataCell](https://reference.aspose.com/cells/net/aspose.cells/row/lastdatacell/), y luego usar la propiedad [Cell.Column](https://reference.aspose.com/cells/net/aspose.cells/cell/column/) para obtener el índice de columna máximo y el índice de columna de datos máximo. Pero para obtener el índice de fila máximo e índice de fila de datos máximo en una columna, es necesario crear un rango en la columna, luego recorrer el rango para encontrar la última celda y finalmente obtener el atributo [Cell.Row](https://reference.aspose.com/cells/net/aspose.cells/cell/row/) en la celda.

Aspose.Cells proporciona las siguientes propiedades y métodos para ayudarlo a alcanzar sus metas.
- [**Row.LastCell**](https://reference.aspose.com/cells/net/aspose.cells/row/lastcell/)
- [**Row.LastDataCell**](https://reference.aspose.com/cells/net/aspose.cells/row/lastdatacell/)
- [**Cell.Column**](https://reference.aspose.com/cells/net/aspose.cells/cell/column/)
- [**Cell.Row**](https://reference.aspose.com/cells/net/aspose.cells/cell/row/)

## **Obtener el índice de columna máximo en fila y el índice de fila máximo en columna usando Aspose.Cells**
Este ejemplo muestra cómo:

1. Cargar el [archivo de muestra](sample.xlsx).
1. Obtener la fila que necesita obtener el índice de columna máximo e índice de columna de datos máximo.
1. Obtener el atributo [Cell.Column](https://reference.aspose.com/cells/net/aspose.cells/cell/column/) en la celda.
1. Crear un rango basado en la columna.
1. Obtener el iterador y recorrer el rango.
1. Obtener el atributo [Cell.Row](https://reference.aspose.com/cells/net/aspose.cells/cell/row/) en la celda.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-max-index-of-row-and-column.cs" >}}
{{< app/cells/assistant language="csharp" >}}
