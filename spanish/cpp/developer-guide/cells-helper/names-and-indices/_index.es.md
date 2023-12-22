---
title: Nombres e índices
type: docs
weight: 10
url: /es/cpp/names-and-indices/
---
##  **Obtenga el nombre Cell de los índices de filas y columnas**
Es posible encontrar el nombre de una celda según el índice de fila y columna. Este artículo explica cómo.
 Aspose.Cells proporciona la[CellsHelper::CellIndexToName](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/cellindextoname/) método que permite a los desarrolladores obtener el nombre de una celda si proporcionan el índice de fila y columna.

{{% alert color="primary" %}} 

A diferencia de Microsoft Excel, donde los índices de filas y columnas comienzan desde 1, Aspose.Cells comienza a contar los índices de filas y columnas desde 0.

{{% /alert %}} 

 El siguiente código de muestra ilustra cómo utilizar[CellsHelper::CellIndexToName](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/cellindextoname/) para acceder al nombre de una celda dado un índice de fila y columna conocido. El código genera el siguiente resultado.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-C-main-GetCellNameFromRowAndColumn-new.cpp" >}}
##  **Obtener índices de filas y columnas del nombre Cell**
Es posible encontrar un índice de fila y columna de la celda a partir de su nombre. Este artículo explica cómo.
 Aspose.Cells proporciona la[CellsHelper.CellNameToIndex](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/cellnametoindex/) método que permite a los desarrolladores obtener un índice de filas y columnas a partir del nombre de la celda.

{{% alert color="primary" %}} 

A diferencia de Microsoft Excel, donde los índices de filas y columnas comienzan desde 1, Aspose.Cells comienza a contar los índices de filas y columnas desde 0.

{{% /alert %}} 

 El siguiente código de muestra ilustra cómo utilizar[CellsHelper::CellNameToIndex](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/cellnametoindex/)para obtener el índice de fila y columna del nombre de la celda. El código genera el siguiente resultado.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-C-main-GetRowAndColumnFromCellName-new.cpp" >}}
