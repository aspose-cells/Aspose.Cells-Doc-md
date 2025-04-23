---
title: Удаление пустых строк и столбцов в листе с помощью Node.js через C++
linktitle: Удаление пустых строк и столбцов в листе
type: docs
weight: 300
url: /ru/nodejs-cpp/delete-blank-rows-and-columns-in-a-worksheet/
description: Узнайте, как удалить все пустые строки и столбцы из листа с помощью Aspose.Cells for Node.js via C++. 
---

{{% alert color="primary" %}}

Возможно удалить все пустые строки и столбцы из листа. Это полезно, например, при генерации PDF-файла из файла Microsoft Excel и желании преобразовать только строки и столбцы, содержащие данные или связанные объекты.

Используйте следующие методы Aspose.Cells для удаления пустых строк и столбцов:

1. Для удаления пустых строк используйте метод [**Cells.deleteBlankRows()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#deleteBlankRows--). Обратите внимание, для удаляемых пустых строк требуется, чтобы [**Row.isBlank()**](https://reference.aspose.com/cells/nodejs-cpp/row/#isBlank--) был равен true, а также не должно быть видимых комментариев для любой ячейки в этих строках, и не должно быть сводной таблицы, диапазон которой пересекается с ними.
2. Для удаления пустых столбцов используйте метод [**Cells.deleteBlankColumns()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#deleteBlankColumns--).

{{% /alert %}}

## Код Node.js для удаления пустых строк

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "SampleInput.xlsx");

// Open an existing excel file.
const wb = new AsposeCells.Workbook(filePath);

// Create a Worksheets object with reference to
// The sheets of the Workbook.
const sheets = wb.getWorksheets();

// Get first Worksheet from WorksheetCollection
const sheet = sheets.get(0);

// Delete the Blank Rows from the worksheet
sheet.getCells().deleteBlankRows();

// Save the excel file.
wb.save(path.join(dataDir, "mybook.out.xlsx"));
```

## Код Node.js для удаления пустых столбцов

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Open an existing excel file.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "SampleInput.xlsx"));

// Create a Worksheets object with reference to the sheets of the Workbook.
const sheets = workbook.getWorksheets();

// Get first Worksheet from WorksheetCollection
const sheet = sheets.get(0);

// Delete the Blank Columns from the worksheet
sheet.getCells().deleteBlankColumns();

// Save the excel file.
workbook.save(path.join(dataDir, "mybook.out.xlsx"));
```
