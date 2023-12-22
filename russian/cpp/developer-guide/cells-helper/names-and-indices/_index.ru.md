---
title: Имена и индексы
type: docs
weight: 10
url: /ru/cpp/names-and-indices/
---
##  **Получить имя Cell из индексов строк и столбцов**
Можно найти имя ячейки по индексу строки и столбца. В этой статье объясняется, как это сделать.
 Aspose.Cells обеспечивает[CellsHelper::CellIndexToName](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/cellindextoname/) метод, который позволяет разработчикам получить имя ячейки, если они предоставили индекс строки и столбца.

{{% alert color="primary" %}} 

В отличие от Microsoft Excel, где индексы строк и столбцов начинаются с 1, Aspose.Cells начинает отсчет индексов строк и столбцов с 0.

{{% /alert %}} 

 Следующий пример кода иллюстрирует, как использовать[CellsHelper::CellIndexToName](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/cellindextoname/) для доступа к имени ячейки по известному индексу строки и столбца. Код генерирует следующий вывод.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-C-main-GetCellNameFromRowAndColumn-new.cpp" >}}
##  **Получить индексы строк и столбцов из имени Cell**
По ее названию можно найти индекс строки и столбца ячейки. В этой статье объясняется, как это сделать.
 Aspose.Cells обеспечивает[CellsHelper.CellNameToIndex](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/cellnametoindex/) метод, который позволяет разработчикам получить индекс строки и столбца из имени ячейки.

{{% alert color="primary" %}} 

В отличие от Microsoft Excel, где индексы строк и столбцов начинаются с 1, Aspose.Cells начинает отсчет индексов строк и столбцов с 0.

{{% /alert %}} 

 Следующий пример кода иллюстрирует, как использовать[CellsHelper::CellNameToIndex](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/cellnametoindex/)чтобы получить индекс строки и столбца из имени ячейки. Код генерирует следующий вывод.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-C-main-GetRowAndColumnFromCellName-new.cpp" >}}
