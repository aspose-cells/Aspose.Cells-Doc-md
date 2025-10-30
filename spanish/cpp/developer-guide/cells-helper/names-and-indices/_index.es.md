---
title: Nombres e Índices
type: docs
weight: 10
url: /es/cpp/names-and-indices/
---

## **Obtener el nombre de celda a partir de los índices de fila y columna**
Es posible encontrar el nombre de una celda dado el índice de fila y columna. Este artículo explica cómo.
Aspose.Cells provee el método [CellsHelper::CellIndexToName](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/cellindextoname/) que permite a los desarrolladores obtener el nombre de una celda si proporcionan el índice de fila y columna.

{{% alert color="primary" %}} 

A diferencia de Microsoft Excel, donde los índices de fila y columna comienzan desde 1, Aspose.Cells comienza a contar los índices de fila y columna desde 0.

{{% /alert %}} 

El siguiente código de ejemplo ilustra cómo utilizar [CellsHelper::CellIndexToName](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/cellindextoname/) para acceder al nombre de una celda dado un índice de fila y columna conocido. El código genera la siguiente salida.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-C-main-GetCellNameFromRowAndColumn-new.cpp" >}}
## **Obtener Índices de Fila y Columna a partir del Nombre de la Celda**
Es posible encontrar un índice de fila y columna de la celda a partir de su nombre. Este artículo explica cómo.
Aspose.Cells proporciona el método [CellsHelper.CellNameToIndex](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/cellnametoindex/), que permite a los desarrolladores obtener un índice de fila y columna a partir del nombre de la celda.

{{% alert color="primary" %}} 

A diferencia de Microsoft Excel, donde los índices de fila y columna comienzan desde 1, Aspose.Cells comienza a contar los índices de fila y columna desde 0.

{{% /alert %}} 

El siguiente código de ejemplo ilustra cómo usar [CellsHelper::CellNameToIndex](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/cellnametoindex/) para obtener el índice de fila y columna a partir del nombre de la celda. El código genera la siguiente salida.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-C-main-GetRowAndColumnFromCellName-new.cpp" >}}
{{< app/cells/assistant language="cpp" >}}
