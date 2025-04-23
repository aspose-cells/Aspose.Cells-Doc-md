---
title: Имена и индексы
type: docs
weight: 10
url: /ru/go-cpp/names-and-indices/
---

## **Получить имя ячейки по индексам строки и столбца**

Возможно определить имя ячейки по индексам строки и столбца. В этой статье объясняется как это сделать.
Aspose.Cells предоставляет метод [CellsHelper_CellIndexToName](https://reference.aspose.com/cells/go-cpp/cellshelper/cellshelper_cellindextoname/), который позволяет разработчикам получить имя ячейки, если они укажут номер строки и столбца.

{{% alert color="primary" %}}

В отличие от Microsoft Excel, где индексы строк и столбцов начинаются с 1, Aspose.Cells начинает считать индексы строк и столбцов с 0.

{{% /alert %}}

Следующий пример кода демонстрирует, как использовать [CellsHelper_CellIndexToName](https://reference.aspose.com/cells/go-cpp/cellshelper/cellshelper_cellindextoname/), чтобы получить имя ячейки, зная её индекс строки и столбца. Код выводит следующий результат.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-GetCellNameFromRowAndColumn.go" >}}

## **Получить индексы строки и столбца из имени ячейки**

Возможно определить индекс строки и столбца ячейки по ее имени. В этой статье объясняется как это сделать.
Aspose.Cells предоставляет метод [CellsHelper_CellNameToIndex](https://reference.aspose.com/cells/go-cpp/cellshelper/cellshelper_cellnametoindex/), который позволяет разработчикам получать индексы строки и столбца по имени ячейки.

{{% alert color="primary" %}}

В отличие от Microsoft Excel, где индексы строк и столбцов начинаются с 1, Aspose.Cells начинает считать индексы строк и столбцов с 0.

{{% /alert %}}

Следующий пример кода показывает, как использовать [CellsHelper_CellNameToIndex](https://reference.aspose.com/cells/go-cpp/cellshelper/cellshelper_cellnametoindex/), чтобы получить индекс строки и столбца по имени ячейки. Код выводит следующий результат.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-GetRowAndColumnFromCellName.go" >}}
