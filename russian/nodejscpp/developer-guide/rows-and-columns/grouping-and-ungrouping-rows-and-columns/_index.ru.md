---
title: Группировка и разгруппировка строк и столбцов с помощью Node.js через C++
linktitle: Группировка и расгруппировка строк и столбцов
type: docs
weight: 50
url: /ru/nodejs-cpp/grouping-and-ungrouping-rows-and-columns/
description: Узнайте, как группировать и разгруппировать строки и столбцы в Excel с помощью Aspose.Cells for Node.js via C++.
--- 

## **Введение**

В файле Microsoft Excel можно создать контур для данных, чтобы можно было показать и скрыть уровни детализации одним щелчком мыши.

Щелкните на **Символы сводки**, 1,2,3, + и -, чтобы быстро отобразить только строки или столбцы, которые предоставляют сводки или заголовки для разделов в листе, или можно использовать символы, чтобы увидеть детали под отдельной сводкой или заголовком, как показано ниже на рисунке:

|**Группировка строк и столбцов.**|
| :- |
|![todo:image_alt_text](grouping-and-ungrouping-rows-and-columns_1.png)|

## **Управление группировкой строк и столбцов**

Aspose.Cells предоставляет класс [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), который представляет файл Microsoft Excel. Класс [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) содержит [**WorksheetCollection**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection), который обеспечивает доступ к каждому листу в файле Excel. Лист представлен классом [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). Класс [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) предоставляет коллекцию [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells), которая включает все ячейки листа.

Коллекция [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) предоставляет несколько методов для управления строками или столбцами в рабочем листе, некоторые из них рассматриваются ниже более подробно.

### **Группировка строк и столбцов**

Вы можете группировать строки или столбцы, вызвав методы [**groupRows(number, number, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#groupRows-number-number-boolean-) и [**groupColumns(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#groupColumns-number-number-) коллекции [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells). Оба метода принимают следующие параметры:

- Индекс первой строки/столбца в группе.
- Индекс последней строки/столбца в группе.
- Скрыто, логический параметр, указывающий, нужно ли скрыть строки/столбцы после группировки.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Reading the Excel file into a buffer
const fs = require("fs");
const fileContent = fs.readFileSync(filePath);

// Opening the Excel file through the buffer
const workbook = new AsposeCells.Workbook(fileContent);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Grouping first six rows (from 0 to 5) and making them hidden by passing true
worksheet.getCells().groupRows(0, 5, true);

// Grouping first three columns (from 0 to 2) and making them hidden by passing true
worksheet.getCells().groupColumns(0, 2, true);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xls"));
```

#### **Настройки группировки**

Microsoft Excel позволяет настроить параметры группировки для отображения:

- Сводные строки под деталями.
- Сводные столбцы справа от деталей.

Разработчики могут настраивать эти параметры группировки с помощью свойства [**getOutline()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getOutline--) класса [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet).

### **Итоговые строки под деталями**

Можно управлять отображением строк-сводок ниже деталей, установив свойство [**getSummaryRowBelow()**](https://reference.aspose.com/cells/nodejs-cpp/outline/#getSummaryRowBelow--) класса [**Outline**](https://reference.aspose.com/cells/nodejs-cpp/outline) в значение **true** или **false**.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);
const worksheet = workbook.getWorksheets().get(0);

// Grouping first six rows and first three columns
worksheet.getCells().groupRows(0, 5, true);
worksheet.getCells().groupColumns(0, 2, true);

// Setting SummaryRowBelow property to false
worksheet.getOutline().setSummaryRowBelow(false);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xls"));
```

### **Итоговые столбцы справа от деталей**

Разработчики также могут управлять отображением сводных столбцов справа от деталей, установив свойство [**getSummaryColumnRight()**](https://reference.aspose.com/cells/nodejs-cpp/outline/#getSummaryColumnRight--) класса [**Outline**](https://reference.aspose.com/cells/nodejs-cpp/outline) в значение **true** или **false**.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);
const worksheet = workbook.getWorksheets().get(0);

// Grouping first six rows and first three columns
worksheet.getCells().groupRows(0, 5, true);
worksheet.getCells().groupColumns(0, 2, true);

worksheet.getOutline().setSummaryColumnRight(true);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xls"));
```

## **Разгруппировка строк и столбцов**

Чтобы размонтировать любые сгруппированные строки или столбцы, вызовите методы [**ungroupRows(number, number, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#ungroupRows-number-number-boolean-) и [**ungroupColumns(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#ungroupColumns-number-number-) коллекции [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells). Оба метода принимают два параметра:

- Индекс первой строки/столбца, которую нужно разгруппировать.
- Индекс последней строки/столбца, которую нужно разгруппировать.

[**ungroupRows(number, number, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#ungroupRows-number-number-boolean-) имеет перегрузку, принимающую третий булевый параметр. Установка его в **true** удаляет всю сгруппированную информацию. В противном случае удаляется только внешняя группа.

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Reading Excel file into buffer
const buffer = fs.readFileSync(filePath);

// Instantiating a Workbook object with file content
const workbook = new AsposeCells.Workbook(buffer);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Ungrouping first six rows (from 0 to 5)
worksheet.getCells().ungroupRows(0, 5);

// Ungrouping first three columns (from 0 to 2)
worksheet.getCells().ungroupColumns(0, 2);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xls"));
```
