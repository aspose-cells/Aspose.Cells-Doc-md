---
title: Nombres e Índices
type: docs
weight: 10
url: /es/go-cpp/names-and-indices/
---

## **Obtener el nombre de celda a partir de los índices de fila y columna**

Es posible encontrar el nombre de una celda dado el índice de fila y columna. Este artículo explica cómo.
Aspose.Cells proporciona el método [CellsHelper_CellIndexToName](https://reference.aspose.com/cells/go-cpp/cellshelper/cellshelper_cellindextoname/), que permite a los desarrolladores obtener el nombre de una celda si proporcionan el índice de fila y columna.

{{% alert color="primary" %}}

A diferencia de Microsoft Excel, donde los índices de fila y columna comienzan desde 1, Aspose.Cells comienza a contar los índices de fila y columna desde 0.

{{% /alert %}}

El siguiente código de ejemplo ilustra cómo usar [CellsHelper_CellIndexToName](https://reference.aspose.com/cells/go-cpp/cellshelper/cellshelper_cellindextoname/) para acceder al nombre de una celda dado un índice de fila y columna conocidos. El código genera la siguiente salida.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-GetCellNameFromRowAndColumn.go" >}}

## **Obtener Índices de Fila y Columna a partir del Nombre de la Celda**

Es posible encontrar un índice de fila y columna de la celda a partir de su nombre. Este artículo explica cómo.
Aspose.Cells proporciona el método [CellsHelper_CellNameToIndex](https://reference.aspose.com/cells/go-cpp/cellshelper/cellshelper_cellnametoindex/), que permite a los desarrolladores obtener un índice de fila y columna desde el nombre de la celda.

{{% alert color="primary" %}}

A diferencia de Microsoft Excel, donde los índices de fila y columna comienzan desde 1, Aspose.Cells comienza a contar los índices de fila y columna desde 0.

{{% /alert %}}

El siguiente código de ejemplo ilustra cómo usar [CellsHelper_CellNameToIndex](https://reference.aspose.com/cells/go-cpp/cellshelper/cellshelper_cellnametoindex/) para obtener el índice de fila y columna desde el nombre de la celda. El código genera la siguiente salida.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-GetRowAndColumnFromCellName.go" >}}
