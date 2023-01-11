﻿---
title: Имена и индексы
type: docs
weight: 10
url: /ru/cpp/names-and-indices/
---
## **Получить имя Cell из индексов строк и столбцов**
Можно найти имя ячейки по индексу строки и столбца. В этой статье объясняется, как.
Aspose.Cells предоставляет метод ICellsHelper.CellIndexToName_i, который позволяет разработчикам получить имя ячейки, если они предоставляют индекс строки и столбца.

{{% alert color="primary" %}} 

В отличие от Microsoft Excel, где индексы строк и столбцов начинаются с 1, Aspose.Cells начинает подсчет индексов строк и столбцов с 0.

{{% /alert %}} 

В следующем примере кода показано, как использовать ICellsHelper.CellIndexToName_i для доступа к имени ячейки с известным индексом строки и столбца. Код генерирует следующий вывод.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-C-main-GetCellNameFromRowAndColumn.cpp" >}}
## **Получить индексы строк и столбцов из имени Cell**
Можно найти индекс строки и столбца ячейки по ее имени. В этой статье объясняется, как.
Aspose.Cells предоставляет метод ICellsHelper.CellNameToIndex_i, который позволяет разработчикам получить индекс строки и столбца из имени ячейки.

{{% alert color="primary" %}} 

В отличие от Microsoft Excel, где индексы строк и столбцов начинаются с 1, Aspose.Cells начинает подсчет индексов строк и столбцов с 0.

{{% /alert %}} 

В следующем примере кода показано, как использовать CellsHelper.CellNameToIndex для получения индекса строки и столбца из имени ячейки. Код генерирует следующий вывод.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-C-main-GetRowAndColumnFromCellName.cpp" >}}