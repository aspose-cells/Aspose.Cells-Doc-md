---
title: Получить максимальный индекс столбца в строке и максимальный индекс строки в столбце
type: docs
weight: 600
url: /ru/nodejs-cpp/get-max-index-in-row-and-column/
description: Узнайте, как получить максимальный индекс столбца в строке и максимальный индекс строки в столбце через API Aspose.Cells for Node.js via C++.
keywords: Получение максимального индекса столбца в строке через Node.js с помощью C++, получение максимального индекса строки в столбце через C++, получение максимального индекса данных в строке через C++, получения максимального индекса данных в столбце через C++.
---

## **Возможные сценарии использования**
Когда необходимо просто манипулировать некоторыми данными в строках или столбцах, важно знать диапазон данных. Aspose.Cells for Node.js via C++ предлагает эту возможность. Для получения максимального индекса столбца в строке можно использовать методы [**Row.getLastCell()**](https://reference.aspose.com/cells/nodejs-cpp/row/#getLastCell--) и [**Row.getLastDataCell()**](https://reference.aspose.com/cells/nodejs-cpp/row/#getLastDataCell--), а затем использовать метод [**Cell.getColumn()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getColumn--) для получения максимального индекса столбца и максимального индекса данных в столбце. Однако для получения максимального индекса строки и максимального индекса данных строки в столбце необходимо создать диапазон по столбцу, пройти по диапазону, чтобы найти последнюю ячейку, и, наконец, вызвать метод [**Cell.getRow()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getRow--) на ячейке.

Aspose.Cells for Node.js via C++ предоставляет следующие свойства и методы, которые помогают вам достигнуть ваших целей.
- [**Row.getLastCell()**](https://reference.aspose.com/cells/nodejs-cpp/row/#getLastCell--)
- [**Row.getLastDataCell()**](https://reference.aspose.com/cells/nodejs-cpp/row/#getLastDataCell--)
- [**Cell.getColumn()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getColumn--)
- [**Cell.getRow()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getRow--)

## **Получение максимального индекса столбца в строке и максимального индекса строки в столбце**
Этот пример показывает, как:

1. Загрузите [образец файла](sample.xlsx).
1. Получите строку, которая нуждается в получении максимального индекса столбца и максимального индекса данных столбца.
1. Вызовите метод [**Cell.getColumn()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getColumn--) на ячейке.
1. Создайте диапазон на основе столбца.
1. Получите итератор и пройдите по диапазону.
1. Вызовите метод [**Cell.getRow()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getRow--) на ячейке.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-max-index-in-row-and-column.js" >}}

