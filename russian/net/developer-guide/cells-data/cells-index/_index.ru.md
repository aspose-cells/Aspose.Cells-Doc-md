---
title: Для получения индексов ячеек
type: docs
weight: 600
url: /ru/net/get-cells-index/
description: Узнайте, как получить строку или столбец по имени строки, столбца или ячеек. Преобразуйте имя ячейки в индекс строки и столбца с нулевой основой.
keywords: Получить индекс строки и столбца по имени ячейки, Получить индекс столбца по имени столбца, Получить индекс строки по имени строки, Получить индекс по имени ячейки. 
---

{{% alert color="primary" %}}
Представление Excel по умолчанию - это ссылка стиля A1, каждый столбец определен как A, B, C..., а ячейки называются A1, B2, C3... и так далее.
Возможно, вам захочется узнать, в какой строке и столбце находится эта ячейка.

{{% /alert %}}


## **Возможные сценарии использования**
Когда вам нужно обрабатывать конкретные данные на листе по индексу строки и столбца, вам нужно знать индексы строки и столбца этой конкретной ячейки. 
Aspose.Cells предлагает эту функцию для получения индекса строки и столбца по имени строки, столбца и ячейки. 
Aspose.Cells предоставляет следующие свойства и методы, чтобы помочь вам достичь своих целей.
- [**CellsHelper.CellNameToIndex**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/cellnametoindex)
- [**CellsHelper.ColumnIndexToName**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/columnindextoname)
- [**CellsHelper.ColumnNameToIndex**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/columnnametoindex)
- [**CellsHelper.RowIndexToName**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/rowindextoname)
- [**CellsHelper.RowNameToIndex**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/rownametoindex)

Примечание: Индексация в Aspose.Cells для .Net начинается с нуля, но идентификатор строки начинается с единицы в MS Excel.

## **Получить индексы ячеек с использованием Aspose.Cells**
Этот пример показывает, как:

1. Создать книгу и добавить некоторые данные.
1. Найдите конкретную ячейку на первом рабочем листе.
1. Получите индекс строки и столбца по имени ячейки.
1. Получите индекс столбца по имени столбца.
1. Получите индекс строки по имени строки.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-get-index.cs" >}}
