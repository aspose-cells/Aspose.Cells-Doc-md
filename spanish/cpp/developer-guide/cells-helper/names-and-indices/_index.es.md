---
title: Nombres e índices
type: docs
weight: 10
url: /es/cpp/names-and-indices/
---
## **Obtenga el nombre Cell de los índices de fila y columna**
Es posible encontrar el nombre de una celda dado el índice de fila y columna. Este artículo explica cómo.
Aspose.Cells proporciona el método ICellsHelper.CellIndexToName_i que permite a los desarrolladores obtener el nombre de una celda si proporcionan el índice de fila y columna.

{{% alert color="primary" %}} 

diferencia de Microsoft Excel, donde los índices de fila y columna comienzan desde 1, Aspose.Cells comienza a contar los índices de fila y columna desde 0.

{{% /alert %}} 

El siguiente código de ejemplo ilustra cómo usar ICellsHelper.CellIndexToName_i para acceder al nombre de una celda dado un índice de fila y columna conocido. El código genera el siguiente resultado.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-C-main-GetCellNameFromRowAndColumn.cpp" >}}
## **Obtener índices de fila y columna de Cell Nombre**
Es posible encontrar un índice de fila y columna de la celda a partir de su nombre. Este artículo explica cómo.
Aspose.Cells proporciona el método ICellsHelper.CellNameToIndex_i que permite a los desarrolladores obtener un índice de fila y columna del nombre de la celda.

{{% alert color="primary" %}} 

diferencia de Microsoft Excel, donde los índices de fila y columna comienzan desde 1, Aspose.Cells comienza a contar los índices de fila y columna desde 0.

{{% /alert %}} 

El siguiente código de ejemplo ilustra cómo usar CellsHelper.CellNameToIndex para obtener el índice de fila y columna del nombre de la celda. El código genera el siguiente resultado.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-C-main-GetRowAndColumnFromCellName.cpp" >}}
