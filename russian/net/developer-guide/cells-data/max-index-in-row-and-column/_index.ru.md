---
title: Получить максимальный индекс столбца в строке и максимальный индекс строки в столбце
type: docs
weight: 600
url: /ru/net/get-max-index-in-row-and-column/
description: Узнайте, как получить максимальный индекс столбца в строке и максимальный индекс строки в столбце с помощью Aspose.Cells for .NET API.
keywords: Get Max Column Index in Row, Get Max Row Index in Column, Get Max Data Column Index in Row, Get Max Data Row Index in Column. 
---
##  **Возможные сценарии использования**
Если вам нужно манипулировать только некоторыми данными в строках или столбцах, вам необходимо знать диапазон данных строк и столбцов. Aspose.Cells предлагает эту функцию. Чтобы получить максимальный индекс столбца в строке, вы можете получить[Row.LastCell](https://reference.aspose.com/cells/net/aspose.cells/row/lastcell/) и[Row.LastDataCell](https://reference.aspose.com/cells/net/aspose.cells/row/lastdatacell/) свойства, а затем используйте[Cell.Column](https://reference.aspose.com/cells/net/aspose.cells/cell/column/) свойство для получения максимального индекса столбца и максимального индекса столбца данных. Но чтобы получить максимальный индекс строки и максимальный индекс данных строки в столбце, вам необходимо создать диапазон в столбце, затем пройти по нему, чтобы найти последнюю ячейку, и, наконец, получить[Cell.Row](https://reference.aspose.com/cells/net/aspose.cells/cell/row/) атрибут ячейки.

Aspose.Cells предоставляет следующие свойства и методы, которые помогут вам достичь ваших целей.
- [**Row.LastCell**](https://reference.aspose.com/cells/net/aspose.cells/row/lastcell/)
- [**Row.LastDataCell**](https://reference.aspose.com/cells/net/aspose.cells/row/lastdatacell/)
- [**Cell.Column**](https://reference.aspose.com/cells/net/aspose.cells/cell/column/)
- [**Cell.Row**](https://reference.aspose.com/cells/net/aspose.cells/cell/row/)

##  **Получите максимальный индекс столбца в строке и максимальный индекс строки в столбце, используя Aspose.Cells**
В этом примере показано, как:

1.  Загрузите[образец файла](sample.xlsx).
1. Получите строку, для которой необходимо получить максимальный индекс столбца и максимальный индекс столбца данных.
1.  Получать[Cell.Column](https://reference.aspose.com/cells/net/aspose.cells/cell/column/) атрибут ячейки.
1. Создайте диапазон на основе столбца.
1. Получите итератор и пройдите диапазон.
1.  Получать[Cell.Row](https://reference.aspose.com/cells/net/aspose.cells/cell/row/) атрибут ячейки.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-max-index-of-row-and-column.cs" >}}