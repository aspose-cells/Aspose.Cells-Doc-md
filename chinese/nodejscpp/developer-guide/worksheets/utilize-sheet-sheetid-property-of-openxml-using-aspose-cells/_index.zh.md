---
title: 利用OpenXml的Sheet.SheetId属性使用Aspose.Cells for Node.js via C++
linktitle: 使用 Aspose.Cells 利用 OpenXml 的 Sheet.SheetId 属性
type: docs
weight: 200
url: /zh/nodejs-cpp/utilize-sheet-sheetid-property-of-openxml-using-aspose-cells/
description: 本文演示了如何利用Aspose.Cells for Node.js via C++以编程方式使用OpenXml的Sheet.SheetId属性操作Excel。
keywords: 使用C++通过Node.js操作OpenXml的sheet id属性，操作Excel工作表的ID
---

## **可能的使用场景**

*Sheet.SheetId* 属性在 *DocumentFormat.OpenXml.Spreadsheet* 模块中可用，是 OpenXml 的一部分。你可以在 *workbook.xml* 中看到此属性及其值，如下图所示。Aspose.Cells 提供了等效的属性 [**Worksheet.getTabId()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getTabId--)。

![todo:image_alt_text](utilize-sheet-sheetid-property-of-openxml-using-aspose-cells_1.png)

## **使用 Aspose.Cells for Node.js via C++ 利用 OpenXml 的 Sheet.SheetId 属性**

以下示例代码加载了[示例Excel文件](51740716.xlsx)，读取其表格或标签ID，然后将其分配为新的标签ID并保存为[输出Excel文件](51740717.xlsx)。还请参见下方给出的代码的控制台输出作为参考。

## **示例代码**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleSheetId.xlsx");

// Load source Excel file
const wb = new AsposeCells.Workbook(filePath);

// Access first worksheet
const ws = wb.getWorksheets().get(0);

// Print its Sheet or Tab Id on console
console.log("Sheet or Tab Id: " + ws.getTabId());

// Change Sheet or Tab Id
ws.setTabId(358);

// Save the workbook
wb.save("outputSheetId.xlsx");
```

## **控制台输出**

{{< highlight text >}}

Sheet or Tab Id: 1297

{{< /highlight >}}
