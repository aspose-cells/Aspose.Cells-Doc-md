---
title: Obtener índice Cells
type: docs
weight: 600
url: /es/net/get-cells-index/
description: Aprenda cómo obtener una fila o columna por el nombre de la fila, columna o celdas. Convierta el nombre de la celda en un índice de fila y columna de base cero.
keywords: Get Row index and Column index by the name of the cell, Get Column index by the name of the column, Get Row index by the name of the row, Get the index by the name of cell. 
---
{{% alert color="primary" %}}
La vista predeterminada de Excel es la referencia de estilo A1, cada columna se define como A, B, C...., y las celdas se denominan A1, B2, C3... y así sucesivamente.
Es posible que desee saber en qué fila y columna se encuentra esta celda.

{{% /alert %}}


##  **Posibles escenarios de uso**
 Cuando solo necesita manipular datos específicos en la hoja de trabajo por índice de fila y columna, necesita conocer los índices de columna y columna de esa celda específica.
 Aspose.Cells ofrece esta función para obtener el índice de filas y columnas por el nombre de la fila, columna y celda.
Aspose.Cells proporciona las siguientes propiedades y métodos para ayudarle a alcanzar sus objetivos.
- [**CellsHelper.CellNameToIndex**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/cellnametoindex)
- [**CellsHelper.ColumnIndexToName**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/columnindextoname)
- [**CellsHelper.ColumnNameToIndex**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/columnnametoindex)
- [**CellsHelper.RowIndexToName**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/rowindextoname)
- [**CellsHelper.RowNameToIndex**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/rownametoindex)

Nota: La indexación está basada en cero en Aspose.Cells para .Net, pero la identificación de Row está basada en uno en MS Excel.

##  **Obtenga Cells índices usando Aspose.Cells**
Este ejemplo muestra cómo:

1. Cree un libro de trabajo y agregue algunos datos.
1. Busque la celda específica en la primera hoja de trabajo.
1. Obtenga el índice de fila y el índice de columna por el nombre de la celda.
1. Obtenga el índice de columna por el nombre de la columna.
1. Obtenga el índice de fila por el nombre de la fila.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-get-index.cs" >}}