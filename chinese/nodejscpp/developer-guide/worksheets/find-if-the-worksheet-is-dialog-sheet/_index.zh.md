---
title: 用Node.js通过C++判断工作表是否为对话框工作表
linktitle: 查找工作表是否为对话框工作表
type: docs
weight: 90
url: /zh/nodejs-cpp/find-if-the-worksheet-is-dialog-sheet/
description: 本文提供判断Excel工作表是否为对话框工作表的说明和示例代码，使用Aspose.Cells for Node.js via C++。
keywords: 用Node.js与C++查找Excel工作表的对话框类型，识别对话框工作表
---

## **可能的使用场景**

对话框工作表是包含对话框的旧格式工作表。此类工作表可以由老版本的Excel（如2003）插入，如截图所示，也可以通过VBA在较新版本（如Excel 2016）中插入。

![todo:image_alt_text](find-if-the-worksheet-is-dialog-sheet_1.png)

你可以找到工作表是否为对话框工作表的方法，使用Aspose.Cells for Node.js via C++提供的[**Worksheet.getType()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getType--)属性。如果返回枚举值[**SheetType.Dialog**](https://reference.aspose.com/cells/nodejs-cpp/sheettype)，则说明你处理的是对话框工作表。

## **查找工作表是否为对话框工作表**

以下示例代码加载了包含对话框工作表的示例Excel文件（64716820.xlsx）。它检查[**Worksheet.getType()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getType--)属性，将其与[**SheetType.Dialog**](https://reference.aspose.com/cells/nodejs-cpp/sheettype)比较，然后输出信息。请参阅下面的控制台输出以获取更多帮助。

## **示例代码**

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleFindIfWorksheetIsDialogSheet.xlsx");

// Load Excel file containing Dialog Sheet
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet
const ws = workbook.getWorksheets().get(0);

// Find if the sheet type is dialog and print the message
if (ws.getType() === AsposeCells.SheetType.Dialog) {
console.log("Worksheet is a Dialog Sheet.");
}
```

## **控制台输出**

{{< highlight js >}}

Worksheet is a Dialog Sheet.

{{< /highlight >}}
