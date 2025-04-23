---
title: 用 Node.js 在 C++ 中创建工作簿和工作表范围命名
linktitle: 命名范围
type: docs
weight: 40
url: /zh/nodejs-cpp/create-workbook-and-worksheet-scoped-named-ranges/
description: 学习如何使用 Aspose.Cells for Node.js via C++ 创建工作簿和工作表范围命名。 
---

{{% alert color="primary" %}} 

Microsoft Excel 允许用户定义具有两种不同范围（工作簿（也称为全局范围）和工作表）的命名范围。

- 具有工作簿范围的命名范围可以通过简单地使用其名称从工作簿内的任何工作表中访问。
- 具有工作表范围的命名范围是通过在其创建的特定工作表的引用中访问的。

Aspose.Cells for Node.js via C++ 提供与 Microsoft Excel 相同的功能，用于添加工作簿和工作表范围内的命名范围。创建工作表范围命名范围时，应在命名范围中使用工作表引用，以将其指定为工作表范围命名范围。

{{% /alert %}} 
## **使用工作簿范围添加命名范围**


```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create a new Workbook object
const workbook = new AsposeCells.Workbook();

// Get first worksheet of the workbook
const sheet = workbook.getWorksheets().get(0);

// Get worksheet's cells collection
const cells = sheet.getCells();

// Create a range of Cells from Cell A1 to C10
const workbookScope = cells.createRange("A1", "C10");

// Assign the name to workbook scope named range
workbookScope.setName("workbookScope");

// Save the workbook
workbook.save(path.join(dataDir, "WorkbookScope.out.xlsx"));
```
## **使用工作表范围添加命名范围**


```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create a new Workbook object
const workbook = new AsposeCells.Workbook();

// Get first worksheet of the workbook
const sheet = workbook.getWorksheets().get(0);

// Get worksheet's cells collection
const cells = sheet.getCells();
// Create a range of Cells
const localRange = cells.createRange("A1", "C10");

// Assign name to range with sheet reference
localRange.setName("Sheet1!local");

// Save the workbook
workbook.save(path.join(dataDir, "output.out.xls"));
```

## **高级主题**
- [创建访问和复制命名区域](/cells/zh/nodejs-cpp/create-access-and-copy-named-ranges/)
- [格式和修改命名区域](/cells/zh/nodejs-cpp/format-and-modify-named-ranges/)
- [获取带有外部链接的范围](/cells/zh/nodejs-cpp/get-range-with-external-links/)
- [实现非连续范围](/cells/zh/nodejs-cpp/implementing-non-sequential-ranges/)


