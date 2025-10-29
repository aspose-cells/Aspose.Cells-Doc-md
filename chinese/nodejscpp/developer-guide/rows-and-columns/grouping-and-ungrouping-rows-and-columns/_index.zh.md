---
title: 使用 Node.js 和 C++ 对行和列进行分组与取消分组
linktitle: 行和列的分组和取消分组
type: docs
weight: 50
url: /zh/nodejs-cpp/grouping-and-ungrouping-rows-and-columns/
description: 了解如何使用 Aspose.Cells for Node.js via C++ 在 Excel 中对行列进行分组和取消分组。
--- 

## **介绍**

在 Microsoft Excel 文件中，您可以创建一个数据大纲，以便通过单击鼠标来显示和隐藏不同级别的细节。

单击**大纲符号**1、2、3、+和- 快速显示工作表中仅提供摘要或标题部分的行或列，或者您可使用符号查看摘要或标题下的详细信息，如下图所示:

|**分组行和列**|
| :- |
|![todo:image_alt_text](grouping-and-ungrouping-rows-and-columns_1.png)|

## **行和列的分组管理**

Aspose.Cells 提供一个类 [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)，代表一个 Microsoft Excel 文件。[**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) 类包含一个 [**WorksheetCollection**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection)，允许访问 Excel 文件中的每个工作表。工作表由 [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) 类表示。[**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) 类提供一个 [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) 集合，表示工作表中的所有单元格。

[**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) 集合提供多个管理工作表中行或列的方法，以下部分做了更详细的介绍。

### **分组行和列**

可以通过调用 [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) 集合的 [**groupRows(number, number, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#groupRows-number-number-boolean-) 和 [**groupColumns(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#groupColumns-number-number-) 方法对行或列进行分组。这两个方法都接受以下参数：

- 第一个行/列索引，即组中的第一行或列。
- 最后一个行/列索引，即组中的最后一行或列。
- 是否隐藏，一个布尔参数，指定是否在分组后隐藏行/列。

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

#### **分组设置**

Microsoft Excel 允许您配置用于显示的分组设置：

- 详细信息下面的摘要行。
- 详细信息右侧的摘要列。

开发者可以使用 [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) 类的 [**getOutline()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getOutline--) 属性配置这些分组设置。

### **将摘要行显示在详细信息下方**

可以通过将 [**getSummaryRowBelow()**](https://reference.aspose.com/cells/nodejs-cpp/outline/#getSummaryRowBelow--) 类的 [**Outline**](https://reference.aspose.com/cells/nodejs-cpp/outline) 属性设置为 **true** 或 **false** 来控制是否在详细信息下方显示汇总行。

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

### **将摘要列显示在详细信息右侧**

开发者也可以通过将 [**Outline**](https://reference.aspose.com/cells/nodejs-cpp/outline) 类的 [**getSummaryColumnRight()**](https://reference.aspose.com/cells/nodejs-cpp/outline/#getSummaryColumnRight--) 属性设为 **true** 或 **false** 来控制在详细信息右侧显示汇总列。

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

## **取消分组行和列**

若要取消分组的行或列，调用 [**ungroupColumns(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#ungroupColumns-number-number-) 集合的 [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) 和 [**ungroupRows(number, number, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#ungroupRows-number-number-boolean-) 方法。这两个方法都需要两个参数：

- 第一个行或列索引，即要取消分组的第一行/列。
- 最后一个行或列索引，即要取消分组的最后一行/列。

[**ungroupRows(number, number, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#ungroupRows-number-number-boolean-) 提供了一个重载，可以接受一个布尔值作为第三参数。将其设为 **true** 会删除所有分组信息；否则只删除外层分组信息。

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
{{< app/cells/assistant language="nodejs-cpp" >}}
