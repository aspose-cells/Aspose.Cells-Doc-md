---
title: 通过 C++ 使用 Node.js 将 JSON 转换为Excel
linktitle: 转换 JSON 为 Excel
type: docs
weight: 300
url: /zh/nodejs-cpp/convert-json-to-excel/
description: 学习如何使用Aspose.Cells for Node.js via C++将JSON转换为Excel文件。
keywords: 使用Node.js通过C++导入没有Office 2013、Office 2016、Office 2019和Office 365的JSON。
---

{{% alert color="primary" %}}

Aspose.Cells 支持将JSON（JavaScript对象表示法）文件转换为Excel工作簿。

{{% /alert %}}

## **将JSON转换为Excel工作簿**
不用担心如何将JSON转换为Excel文件，因为Aspose.Cells for Node.js via C++提供了最佳解决方案。Aspose.Cells API支持将JSON格式转换为电子表格。您可以使用 [**JsonLoadOptions**](https://reference.aspose.com/cells/nodejs-cpp/jsonloadoptions) 类指定导入JSON到工作簿的其他设置。

以下示例演示了将JSON导入Excel工作簿的代码。请查看代码以将[source file](sample.json)转换为代码生成的xlsx文件。

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

以下代码示例，使用 JsonLoadOptions 类指定额外设置，演示导入JSON到Excel工作簿。请参考代码将【源文件】(sample.json) 转换为Excel文件。

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

以下代码示例演示将JSON字符串导入Excel工作簿。您也可以在导入JSON时指定布局位置。请参考代码将JSON字符串转换为生成的xlsx文件。

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
