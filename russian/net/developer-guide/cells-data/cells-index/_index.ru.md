---
title: Получить индекс Cells
type: docs
weight: 600
url: /ru/net/get-cells-index/
description: Узнайте, как получить строку или столбец по имени строки, столбца или ячеек. Преобразуйте имя ячейки в индекс строки и столбца, отсчитываемый от нуля.
keywords: Get Row index and Column index by the name of the cell, Get Column index by the name of the column, Get Row index by the name of the row, Get the index by the name of cell. 
---
{{% alert color="primary" %}}
Представление Excel по умолчанию представляет собой ссылку на стиль A1: каждый столбец определяется как A, B, C...., а ячейки называются A1, B2, C3... и так далее.
Возможно, вам захочется узнать, в какой строке и столбце находится эта ячейка.

{{% /alert %}}


##  **Возможные сценарии использования**
 Если вам нужно манипулировать определенными данными на листе только по индексу строки и столбца, вам необходимо знать индексы столбца и столбца этой конкретной ячейки.
 Aspose.Cells предлагает эту функцию для получения индекса строки и столбца по имени строки, столбца и ячейки.
Aspose.Cells предоставляет следующие свойства и методы, которые помогут вам достичь ваших целей.
- [**CellsHelper.CellNameToIndex**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/cellnametoindex)
- [**CellsHelper.ColumnIndexToName**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/columnindextoname)
- [**CellsHelper.ColumnNameToIndex**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/columnnametoindex)
- [**CellsHelper.RowIndexToName**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/rowindextoname)
- [**CellsHelper.RowNameToIndex**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/rownametoindex)

Примечание. Индексация начинается с нуля в Aspose.Cells для .Net, но идентификатор строки начинается с единицы в MS Excel.

##  **Получите индексы Cells, используя Aspose.Cells.**
В этом примере показано, как:

1. Создайте книгу и добавьте некоторые данные.
1. Найдите конкретную ячейку на первом листе.
1. Получите индекс строки и индекс столбца по имени ячейки.
1. Получить индекс столбца по имени столбца.
1. Получить индекс строки по имени строки.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-get-index.cs" >}}