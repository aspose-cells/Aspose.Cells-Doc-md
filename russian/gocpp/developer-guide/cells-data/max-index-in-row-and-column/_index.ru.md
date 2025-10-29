---
title: Получить максимальный индекс столбца в строке и максимальный индекс строки в столбце с Golang через C++
linktitle: Получить максимальный индекс столбца в строке и максимальный индекс строки в столбце
type: docs
weight: 600
url: /ru/go-cpp/get-max-index-in-row-and-column/
description: Узнайте, как получить максимальный индекс столбца в строке и максимальный индекс строки в столбце через API Aspose.Cells for C++.
keywords: Получите максимальный индекс столбца в строке, получите максимальный индекс строки в столбце, получите максимальный индекс данных столбца в строке, получите максимальный индекс строки данных в столбце
---

## **Возможные сценарии использования**
Когда необходимо лишь управлять некоторыми данными по строкам или столбцам, нужно знать диапазон данных строк и столбцов. Aspose.Cells предоставляет эту возможность. Для получения максимального индекса столбца в строке можно получить свойства [Row.GetLastCell()](https://reference.aspose.com/cells/go-cpp/row/getlastcell/) и [Row.GetLastDataCell()](https://reference.aspose.com/cells/cpp/aspose.cells/row/getlastdatacell/), а затем использовать свойство [Cell.GetColumn()](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getcolumn/), чтобы получить максимальный индекс столбца и максимальный индекс данных столбца. Но чтобы получить максимальный индекс строки и индекс данных строки в столбце, нужно создать диапазон по столбцу, затем пройти по диапазону, чтобы найти последнюю ячейку, и, наконец, воспользоваться атрибутом [Cell.GetRow()](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getrow/), чтобы получить номер строки.

Aspose.Cells предоставляет следующие свойства и методы, чтобы помочь вам достичь своих целей.
- [**Row.GetLastCell()**](https://reference.aspose.com/cells/go-cpp/row/getlastcell/)
- [**Row.GetLastDataCell()**](https://reference.aspose.com/cells/go-cpp/row/getlastdatacell/)
- [**Cell.GetColumn()**](https://reference.aspose.com/cells/go-cpp/cell/getcolumn/)
- [**Cell.GetRow()**](https://reference.aspose.com/cells/go-cpp/cell/getrow/)

## **Получите максимальный индекс столбца в строке и максимальный индекс строки в столбце, используя Aspose.Cells**
Этот пример показывает, как:

1. Загрузите [образец файла](sample.xlsx).
1. Получите строку, которая нуждается в получении максимального индекса столбца и максимального индекса данных столбца.
1. Получить атрибут [Cell.GetColumn()](https://reference.aspose.com/cells/go-cpp/cell/getcolumn/) ячейки.
1. Создайте диапазон на основе столбца.
1. Получите итератор и пройдите по диапазону.
1. Получить атрибут [Cell.GetRow()](https://reference.aspose.com/cells/go-cpp/cell/getrow/) ячейки.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-MaxIndexInRowAndColumn.go" >}}
