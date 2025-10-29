---
title: Имена и индексы
type: docs
weight: 10
url: /ru/cpp/names-and-indices/
---

## **Получить имя ячейки по индексам строки и столбца**
Возможно определить имя ячейки по индексам строки и столбца. В этой статье объясняется как это сделать.
Aspose.Cells предоставляет метод [CellsHelper::CellIndexToName](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/cellindextoname/), позволяющий разработчикам получить имя ячейки, если они предоставили индекс строки и столбца.

{{% alert color="primary" %}} 

В отличие от Microsoft Excel, где индексы строк и столбцов начинаются с 1, Aspose.Cells начинает считать индексы строк и столбцов с 0.

{{% /alert %}} 

В следующем примере кода показано, как использовать [CellsHelper::CellIndexToName](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/cellindextoname/) для доступа к имени ячейки при известном индексе строки и столбца. Код генерирует следующий вывод.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-C-main-GetCellNameFromRowAndColumn-new.cpp" >}}
## **Получить индексы строки и столбца из имени ячейки**
Возможно определить индекс строки и столбца ячейки по ее имени. В этой статье объясняется как это сделать.
Aspose.Cells предоставляет метод [CellsHelper.CellNameToIndex](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/cellnametoindex/), позволяющий разработчикам получить индекс строки и столбца из имени ячейки.

{{% alert color="primary" %}} 

В отличие от Microsoft Excel, где индексы строк и столбцов начинаются с 1, Aspose.Cells начинает считать индексы строк и столбцов с 0.

{{% /alert %}} 

В следующем примере кода показано, как использовать [CellsHelper::CellNameToIndex](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/cellnametoindex/) для получения индекса строки и столбца по имени ячейки. Код генерирует следующий вывод.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-C-main-GetRowAndColumnFromCellName-new.cpp" >}}
{{< app/cells/assistant language="cpp" >}}
