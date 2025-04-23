---
title: 使用Node.js通过C++将单元格添加到Microsoft Excel公式监视窗口的方法
linktitle: 将单元格添加到Microsoft Excel公式监视窗口
description: 如何使用 Aspose.Cells 库通过 Node.js 和 C++ 向 Excel 的公式监视窗口添加单元格。通过加载已有的 Excel 文件或创建新文件，我们可以对其中的单元格进行操作并设置公式。最后，将修改后的 Excel 文件保存到磁盘。
keywords: Aspose.Cells，Excel，公式监控窗口，单元格，通过C++的Node.js添加
type: docs
weight: 60
url: /zh/nodejs-cpp/add-cells-to-microsoft-excel-formula-watch-window/
---

## **可能的使用场景**

Microsoft Excel的监控窗口是一个方便的工具，可在窗口中观察单元格值及其公式。你可以通过点击*公式 > 监控窗口*在Microsoft Excel中打开*监控窗口*。它有*添加监控*按钮，用于添加待检查的单元格。同样，你可以使用[**CellWatchCollection.add(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cellwatchcollection/#add-number-number-)方法通过Aspose.Cells API将单元格添加到*监控窗口*。

## **将单元格添加到Microsoft Excel公式监视窗口**

以下示例代码设置了单元格C1和E1的公式，并将它们添加到监控窗口。然后将工作簿保存为[输出Excel文件](67338481.xlsx)。如果你打开输出Excel文件并查看*监控窗口*，你将看到两个单元格，如截图所示。

![todo:image_alt_text](add-cells-to-microsoft-excel-formula-watch-window_1.png)

## **示例代码**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

// Create empty workbook.
const wb = new AsposeCells.Workbook();

// Access first worksheet.
const ws = wb.getWorksheets().get(0);

// Put some integer values in cell A1 and A2.
ws.getCells().get("A1").putValue(10);
ws.getCells().get("A2").putValue(30);

// Access cell C1 and set its formula.
const c1 = ws.getCells().get("C1");
c1.setFormula("=Sum(A1,A2)");

// Add cell C1 into cell watches by name.
ws.getCellWatches().add(c1.getName());

// Access cell E1 and set its formula.
const e1 = ws.getCells().get("E1");
e1.setFormula("=A2*A1");

// Add cell E1 into cell watches by its row and column indices.
ws.getCellWatches().add(e1.getRow(), e1.getColumn());

// Save workbook to output XLSX format.
wb.save("outputAddCellsToMicrosoftExcelFormulaWatchWindow.xlsx", AsposeCells.SaveFormat.Xlsx);
```
