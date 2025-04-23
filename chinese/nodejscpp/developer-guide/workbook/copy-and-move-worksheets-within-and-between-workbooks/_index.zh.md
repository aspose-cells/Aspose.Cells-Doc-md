---
title: 在工作簿内或之间复制和移动工作表，使用Node.js和C++
linktitle: 复制和移动工作表在工作簿内和工作簿之间
type: docs
weight: 80
url: /zh/nodejs-cpp/copy-and-move-worksheets-within-and-between-workbooks/
description: 学习如何使用Aspose.Cells for Node.js via C++在工作簿内或之间复制和移动工作表。高效管理你的工作簿结构。
---

{{% alert color="primary" %}}

有时，您可能需要具有相同格式和数据输入的许多工作表。例如，如果您使用季度预算，可能希望创建一个包含具有相同列标题、行标题和公式的工作表的工作簿。有一种方法可以做到这一点：先创建一个工作表，然后将其复制三次。

Aspose.Cells for Node.js via C++支持复制或移动工作表，涉及数据、格式、表格、矩阵、图表、图片及其他对象，复制的精度最高。

{{% /alert %}}

## **复制和移动工作表**

### **在工作簿内复制工作表**

所有示例的初始步骤都是相同的。

1. 在Microsoft Excel中创建两个带有一些数据的工作簿。对于本示例，我们在Microsoft Excel中创建了两个新工作簿，并为工作表输入了一些数据。

- FirstWorkbook.xlsx（3 个工作表）。
- SecondWorkbook.xlsx（1 个工作表）。

1. 下载并安装 Aspose.Cells：
   [下载Aspose.Cells for Node.js via C++](https://downloads.aspose.com/cells/nodejs-cpp)。
   1. 在您的开发计算机上安装它。
      所有 [Aspose](http://www.aspose.com/) 组件在安装后都是以评估模式运行。 评估模式没有时间限制，只会在生成的文档中添加水印。
1. 创建一个项目：
   1. 启动你的开发环境。
   1. 创建新的控制台应用程序。
1. 添加引用：
   1. 向项目添加对 Aspose.Cells 的引用。
      例如，添加对 ...\Program Files\Aspose\Aspose.Cells\Bin\NodeJs\Aspose.Cells.dll 的引用
1. 在工作簿内复制工作表
   第一个示例将 FirstWorkbook.xlsx 内的第一个工作表（Copy）复制。

执行代码后，名为 Copy 的工作表将在 FirstWorkbook.xlsx 中复制并命名为 Last Sheet。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Open a file into the first book.
const excelWorkbook1 = new AsposeCells.Workbook(path.join(dataDir, "FirstWorkbook.xlsx"));

// Copy the first sheet of the first book within the workbook
excelWorkbook1.getWorksheets().get(2).copy(excelWorkbook1.getWorksheets().get("Copy"));

// Save the file.
excelWorkbook1.save(path.join(dataDir, "FirstWorkbookCopied_out.xlsx"));
```

### **工作簿内移动工作表**

以下代码显示了如何将工作簿内的工作表从一个位置移动到另一个位置。执行代码后，Move 工作表从 FirstWorkbook.xlsx 的索引 1 移动到索引 2。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "FirstWorkbook.xlsx");
// Open a file into the first book.
const excelWorkbook2 = new AsposeCells.Workbook(filePath);

// Move the sheet
const worksheets = excelWorkbook2.getWorksheets();
const worksheet = worksheets.get(0);
worksheet.moveTo(1);

// Save the file.
excelWorkbook2.save(path.join(dataDir, "FirstWorkbookMoved_out.xlsx"));
```

### **在工作簿之间复制工作表**

执行代码会将名为 Copy 的工作表复制到 SecondWorkbook.xlsx 中，并命名为 Sheet2。

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const excelWorkbook3 = new AsposeCells.Workbook();
const excelWorkbook4 = new AsposeCells.Workbook();

// Create source worksheet
excelWorkbook3.getWorksheets().add("Copy");

// Add new worksheet into second Workbook
excelWorkbook4.getWorksheets().add();

// Copy the first sheet of the first book into second book.
excelWorkbook4.getWorksheets().get(1).copy(excelWorkbook3.getWorksheets().get("Copy"));

// Save the file.
excelWorkbook4.save(path.join(dataDir, "CopyWorksheetsBetweenWorkbooks_out.xlsx"));
```

### **在工作簿之间移动工作表**

执行代码后，工作表名为 Move 从 FirstWorkbook.xlsx 移动到 SecondWorkbook.xlsx，并命名为 Sheet3。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create new workbooks instead of opening existing files
const excelWorkbook5 = new AsposeCells.Workbook();
const excelWorkbook6 = new AsposeCells.Workbook();

// Add New Worksheet
excelWorkbook6.getWorksheets().add();

// Copy the sheet from first book into second book.
excelWorkbook6.getWorksheets().get(0).copy(excelWorkbook5.getWorksheets().get(0));

// Remove the copied worksheet from first workbook
excelWorkbook5.getWorksheets().removeAt(0);

// Save the file.
excelWorkbook5.save(path.join(dataDir, "FirstWorkbookWithMove_out.xlsx"));

// Save the file.
excelWorkbook6.save(path.join(dataDir, "SecondWorkbookWithMove_out.xlsx"));
```
