---
title: Конвертировать JSON в Excel с помощью Node.js через C++
linktitle: Конвертировать JSON в Excel
type: docs
weight: 300
url: /ru/nodejs-cpp/convert-json-to-excel/
description: Узнайте, как конвертировать JSON в файл Excel с помощью Aspose.Cells for Node.js via C++.
keywords: Импорт JSON без Office 2013, Office 2016, Office 2019 и Office 365 с помощью Node.js через C++.
---

{{% alert color="primary" %}}

Aspose.Cells поддерживает преобразование файла JSON (JavaScript Object Notation) в рабочую книгу Excel.

{{% /alert %}}

## **Преобразование JSON в книгу Excel**
Нет необходимости гадать, как преобразовать JSON в файл Excel, потому что Aspose.Cells for Node.js via C++ предоставляет лучшее решение. API Aspose.Cells поддерживает преобразование JSON в таблицы. Вы можете использовать класс [**JsonLoadOptions**](https://reference.aspose.com/cells/nodejs-cpp/jsonloadoptions), чтобы задать дополнительные параметры для импорта JSON в рабочую книгу.

В следующем примере кода демонстрируется импорт JSON в книгу Excel. Пожалуйста, ознакомьтесь с кодом для преобразования [исходного файла](sample.json) в файл xlsx, сгенерированный кодом для справки.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.json");
// create a Workbook object
const wb = new AsposeCells.Workbook(filePath);

// save file to xlsx format
wb.save("sample_out.xlsx");
```

Следующий пример кода демонстрирует импорт JSON в рабочую книгу Excel с использованием класса JsonLoadOptions для задания дополнительных настроек. Ознакомьтесь с кодом для преобразования [исходного файла](sample.json) в xlsx-файл, сгенерированный кодом, для справки.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.json");

// Create an options of loading the file.
const options = new AsposeCells.JsonLoadOptions();
options.setMultipleWorksheets(true);

// Loads the workbook from JSON file
const book = new AsposeCells.Workbook(filePath, options);

// Save file to xlsx format
book.save("sample_out.xlsx");
```

Следующий пример демонстрирует импорт строки JSON в рабочую книгу Excel. Также можно указать расположение раскладки при импорте JSON. Ознакомьтесь с кодом для преобразования строки JSON в xlsx-файл, сгенерированный кодом, для справки.

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const inputJson = JSON.stringify([
{ BEFORE: 'before cell', TEST: 'asd1', AFTER: 'after cell' },
{ BEFORE: 'before cell', TEST: 'asd2', AFTER: 'after cell' },
{ BEFORE: 'before cell', TEST: 'asd3', AFTER: 'after cell' },
{ BEFORE: 'before cell', TEST: 'asd4', AFTER: 'after cell' }
]);
const sheetName = "Sheet1";
const row = 3;
const column = 2;

// create a Workbook object
const book = new AsposeCells.Workbook();
const worksheet = book.getWorksheets().get(sheetName);

// set JsonLayoutOptions to treat Arrays as Table
const jsonLayoutOptions = new AsposeCells.JsonLayoutOptions();
jsonLayoutOptions.setArrayAsTable(true);

AsposeCells.JsonUtility.importData(inputJson, worksheet.getCells(), row, column, jsonLayoutOptions);

// save file to xlsx format
book.save("out.xlsx");
```
{{< app/cells/assistant language="nodejs-cpp" >}}
