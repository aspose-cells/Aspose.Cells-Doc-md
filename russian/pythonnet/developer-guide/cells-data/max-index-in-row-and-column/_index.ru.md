---
title: Получить максимальный индекс столбца в строке и максимальный индекс строки в столбце
type: docs
weight: 600
url: /ru/python-net/get-max-index-in-row-and-column/
description: Узнайте, как получить максимальный индекс столбца в строке и максимальный индекс строки в столбце через Aspose.Cells для Python via .NET API.
keywords: Python Excel Library, Python Get Max Column Index in Row, Python Get Max Row Index in Column, Python Get Max Data Column Index in Row, Python Get Max Data Row Index in Column. 
---

## **Возможные сценарии использования**
Когда вам нужно только изменить некоторые данные в строках или столбцах, вам необходимо знать диапазон данных строк и столбцов. Aspose.Cells для Python via .NET предлагает эту возможность. Чтобы получить максимальный индекс столбца в строке, вы можете получить свойства [Row.last_cell](https://reference.aspose.com/cells/python-net/aspose.cells/row/last_cell/) и [Row.last_data_cell](https://reference.aspose.com/cells/python-net/aspose.cells/row/last_data_cell/) и затем использовать свойство [Cell.column](https://reference.aspose.com/cells/python-net/aspose.cells/cell/column/) для получения максимального индекса столбца и максимального индекса данных столбца. Но для получения максимального индекса строки и максимального индекса строки данных в столбце, вам необходимо создать диапазон в столбце, затем пройти по диапазону, чтобы найти последнюю ячейку, а затем получить атрибут [Cell.row](https://reference.aspose.com/cells/python-net/aspose.cells/cell/row/).

Aspose.Cells для Python via .NET предоставляет следующие свойства и методы, чтобы помочь вам достичь ваших целей.
- [**Row.last_cell**](https://reference.aspose.com/cells/python-net/aspose.cells/row/last_cell/)
- [**Row.last_data_cell**](https://reference.aspose.com/cells/python-net/aspose.cells/row/last_data_cell/)
- [**Cell.column**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/column/)
- [**Cell.row**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/row/)

## **Получите максимальный индекс столбца в строке и максимальный индекс строки в столбце с использованием Aspose.Cells для Python Excel Library**
Этот пример показывает, как:

1. Загрузите [образец файла](sample.xlsx).
1. Получите строку, которая нуждается в получении максимального индекса столбца и максимального индекса данных столбца.
1. Получите атрибут [Cell.column](https://reference.aspose.com/cells/python-net/aspose.cells/cell/column/) на ячейке.
1. Создайте диапазон на основе столбца.
1. Получите итератор и пройдите по диапазону.
1. Получите атрибут [Cell.row](https://reference.aspose.com/cells/python-net/aspose.cells/cell/row/) на ячейке.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-Cells-max-index-of-row-and-column.py" >}}
{{< app/cells/assistant language="python-net" >}}
