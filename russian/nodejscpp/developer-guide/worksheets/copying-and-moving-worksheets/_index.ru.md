---
title: Копирование и перемещение листов с помощью Node.js через C++
linktitle: Копирование и перемещение рабочих листов
type: docs
weight: 10
url: /ru/nodejs-cpp/copying-and-moving-worksheets/
description: Эта статья включает пример кода и описывает, как программно копировать и перемещать листы внутри рабочей книги Excel и между рабочими книгами Excel с помощью API Node.js и C++.
keywords: копировать лист Node.js, переместить лист Node.js
---

{{% alert color="primary" %}}

Иногда вам действительно нужно несколько рабочих листов с общим форматированием и данными. Например, если вы работаете с квартальными бюджетами, вам может потребоваться создать книгу с листами, содержащими одинаковые заголовки столбцов, заголовки строк и формулы. Есть способ сделать это: создав один лист, а затем скопировав его.

Aspose.Cells for Node.js via C++ поддерживает копирование и перемещение листов внутри или между рабочими книгами. Листы с данными, форматированием, таблицами, матрицами, графиками, изображениями и другими объектами копируются с наибольшей точностью.

{{% /alert %}}

## **Перемещение или копирование листов с использованием Microsoft Excel**

Ниже приведены шаги для копирования и перемещения листов внутри или между книгами в Microsoft Excel.

1. Чтобы переместить или скопировать листы в другую рабочую книгу, откройте рабочую книгу, которая будет получать листы.
1. Переключитесь на рабочую книгу, которая содержит листы, которые вы хотите переместить или скопировать, а затем выберите листы.
1. На меню **Правка** щелкните **Переместить или скопировать лист**.
1. В диалоговом окне **В книгу** щелкните книгу, которая получит листы.
1. Чтобы переместить или скопировать выбранные листы в новую книгу, щелкните **Новая книга**.
1. В поле **Перед листом** щелкните лист, перед которым вы хотите вставить перемещенные или скопированные листы.
1. Чтобы скопировать листы вместо их перемещения, выберите флажок **Создать копию**.

### **Копировать листы внутри рабочей книги с помощью Aspose.Cells for Node.js via C++**

Aspose.Cells предоставляет перегруженный метод [**Aspose.Cells.WorksheetCollection.addCopy()**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#addCopy-number-), который используется для добавления листа в коллекцию и копирования данных с существующего листа. Одна версия метода принимает индекс исходного листа в качестве параметра. Другая версия принимает имя исходного листа.

В следующем примере показано, как скопировать существующий лист в рамках рабочей книги.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const inputPath = path.join(dataDir, "book1.xls");

// Open an existing Excel file.
const wb = new AsposeCells.Workbook(inputPath);

// Create a Worksheets object with reference to
// the sheets of the Workbook.
const sheets = wb.getWorksheets();

// Copy data to a new sheet from an existing
// sheet within the Workbook.
sheets.addCopy("Sheet1");

// Save the Excel file.
wb.save(path.join(dataDir, "CopyWithinWorkbook_out.xls"));
```

### **Копировать листы между рабочими книгами**

Aspose.Cells предоставляет метод, [**Worksheet.copy(Worksheet)**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#copy-worksheet-), используемый для копирования данных и форматирования из исходного листа в другой лист внутри или между рабочими книгами. Метод принимает объект исходного листа в качестве параметра.

В следующем примере показано, как скопировать лист из одной рабочей книги в другую рабочую книгу.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const inputPath = path.join(dataDir, "book1.xls");

// Create a Workbook.
// Open a file into the first book.
const excelWorkbook0 = new AsposeCells.Workbook(inputPath);

// Create another Workbook.
const excelWorkbook1 = new AsposeCells.Workbook();

// Copy the first sheet of the first book into second book.
excelWorkbook1.getWorksheets().get(0).copy(excelWorkbook0.getWorksheets().get(0));

// Save the file.
excelWorkbook1.save(path.join(dataDir, "CopyWorksheetsBetweenWorkbooks_out.xls"));
```

В следующем примере показано, как скопировать лист из одной рабочей книги в другую рабочую книгу.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create a new Workbook.
const excelWorkbook0 = new AsposeCells.Workbook();

// Get the first worksheet in the book.
const ws0 = excelWorkbook0.getWorksheets().get(0);

// Put some data into header rows (A1:A4)
for (let i = 0; i < 5; i++) {
ws0.getCells().get(i, 0).putValue(`Header Row ${i}`);
}

// Put some detail data (A5:A999)
for (let i = 5; i < 1000; i++) {
ws0.getCells().get(i, 0).putValue(`Detail Row ${i}`);
}

// Define a pagesetup object based on the first worksheet.
const pagesetup = ws0.getPageSetup();

// The first five rows are repeated in each page...
// It can be seen in print preview.
pagesetup.setPrintTitleRows("$1:$5");

// Create another Workbook.
const excelWorkbook1 = new AsposeCells.Workbook();

// Get the first worksheet in the book.
const ws1 = excelWorkbook1.getWorksheets().get(0);

// Name the worksheet.
ws1.setName("MySheet");

// Copy data from the first worksheet of the first workbook into the
// first worksheet of the second workbook.
ws1.copy(ws0);

// Save the excel file.
excelWorkbook1.save(path.join(dataDir, "CopyWorksheetFromWorkbookToOther_out.xls"));
```

### **Перемещение листов в рамках рабочей книги**

Aspose.Cells предоставляет метод [**Aspose.Cells.Worksheet.moveTo()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#moveto-number-), используемый для перемещения листа в другое место в той же таблице. Метод принимает индекс целевого листа в качестве параметра.

В следующем примере показано, как переместить лист в другое место внутри рабочей книги.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const inputPath = path.join(dataDir, "sample1.xlsx");

// Open an existing excel file.
const wb = new AsposeCells.Workbook(inputPath);

// Create a Worksheets object with reference to the sheets of the Workbook.
const sheets = wb.getWorksheets();

// Get the first worksheet.
const worksheet = sheets.get(0);

// Move the first sheet to the third position in the workbook.
worksheet.moveTo(2);

// Save the excel file.
wb.save(path.join(dataDir, "MoveWorksheet_out.xls"));
```
