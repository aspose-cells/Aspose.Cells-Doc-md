---
title: Получить максимальный индекс столбца в строке и максимальный индекс строки в столбце
type: docs
weight: 600
url: /ru/net/get-max-index-in-row-and-column/
description: Узнайте, как получить максимальный индекс столбца в строке и максимальный индекс строки в столбце через API Aspose.Cells for .NET
keywords: Получите максимальный индекс столбца в строке, получите максимальный индекс строки в столбце, получите максимальный индекс данных столбца в строке, получите максимальный индекс строки данных в столбце 
---

## **Возможные сценарии использования**
Когда вам нужно обрабатывать некоторые данные по строкам или столбцам, вам нужно знать диапазон данных по строкам и столбцам. Aspose.Cells предлагает эту функцию. Чтобы получить максимальный индекс столбца в строке, вы можете получить свойства [Row.LastCell](https://reference.aspose.com/cells/net/aspose.cells/row/lastcell/) и [Row.LastDataCell](https://reference.aspose.com/cells/net/aspose.cells/row/lastdatacell/), а затем использовать свойство [Cell.Column](https://reference.aspose.com/cells/net/aspose.cells/cell/column/) для получения максимального индекса столбца и максимального индекса данных столбца. Но чтобы получить максимальный индекс строки и максимальный индекс строки данных в столбце, вам нужно создать диапазон в столбце, затем пройти по диапазону, чтобы найти последнюю ячейку, и наконец получить атрибут [Cell.Row](https://reference.aspose.com/cells/net/aspose.cells/cell/row/) на ячейке.

Aspose.Cells предоставляет следующие свойства и методы, чтобы помочь вам достичь своих целей.
- [**Row.LastCell**](https://reference.aspose.com/cells/net/aspose.cells/row/lastcell/)
- [**Row.LastDataCell**](https://reference.aspose.com/cells/net/aspose.cells/row/lastdatacell/)
- [**Cell.Column**](https://reference.aspose.com/cells/net/aspose.cells/cell/column/)
- [**Cell.Row**](https://reference.aspose.com/cells/net/aspose.cells/cell/row/)

## **Получите максимальный индекс столбца в строке и максимальный индекс строки в столбце, используя Aspose.Cells**
Этот пример показывает, как:

1. Загрузите [образец файла](sample.xlsx).
1. Получите строку, которая нуждается в получении максимального индекса столбца и максимального индекса данных столбца.
1. Получите атрибут [Cell.Column](https://reference.aspose.com/cells/net/aspose.cells/cell/column/) на ячейке
1. Создайте диапазон на основе столбца.
1. Получите итератор и пройдите по диапазону.
1. Получите атрибут [Cell.Row](https://reference.aspose.com/cells/net/aspose.cells/cell/row/) на ячейке

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-max-index-of-row-and-column.cs" >}}
