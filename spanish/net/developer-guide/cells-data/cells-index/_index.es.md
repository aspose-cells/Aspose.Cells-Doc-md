---
title: Obtener el índice de celdas
type: docs
weight: 600
url: /es/net/get-cells-index/
description: Aprende cómo obtener la fila o columna por el nombre de la fila, columna o celdas. Convierte el nombre de la celda a índice de fila y columna basado en cero.
keywords: Obtener el índice de fila y columna por el nombre de la celda, Obtener el índice de columna por el nombre de la columna, Obtener el índice de fila por el nombre de la fila, Obtener el índice por el nombre de la celda. 
---

{{% alert color="primary" %}}
La vista predeterminada de Excel es la referencia de estilo A1, cada columna se define como A, B, C..., y las celdas se nombran como A1, B2, C3... y así sucesivamente.
Es posible que desee saber en qué fila y columna se encuentra esta celda.

{{% /alert %}}


## **Escenarios de uso posibles**
Cuando solo necesita manipular un dato específico en la hoja de cálculo por índice de fila y columna, necesita saber los índices de fila y columna de esa celda específica. 
Aspose.Cells ofrece esta funcionalidad para obtener el índice de fila y columna por el nombre de la fila, columna y celda. 
Aspose.Cells proporciona las siguientes propiedades y métodos para ayudarlo a alcanzar sus metas.
- [**CellsHelper.CellNameToIndex**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/cellnametoindex)
- [**CellsHelper.ColumnIndexToName**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/columnindextoname)
- [**CellsHelper.ColumnNameToIndex**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/columnnametoindex)
- [**CellsHelper.RowIndexToName**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/rowindextoname)
- [**CellsHelper.RowNameToIndex**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/rownametoindex)

Nota: El indexado es basado en cero en Aspose.Cells para .Net, pero el id de la Fila es basado en uno en MS Excel.

## **Obtener Índices de Celdas usando Aspose.Cells**
Este ejemplo muestra cómo:

1. Crear un libro de trabajo y agregar algunos datos.
1. Encontrar la celda específica en la primera hoja de trabajo.
1. Obtener el índice de fila e índice de columna por el nombre de la celda.
1. Obtener el índice de columna por el nombre de la columna.
1. Obtener el índice de fila por el nombre de la fila.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-get-index.cs" >}}
{{< app/cells/assistant language="csharp" >}}
