---  
title: 通过 Node.js + C++ 指定共享公式的最大行数  
linktitle: 指定共享公式的最大行数  
type: docs  
weight: 40  
url: /zh/nodejs-cpp/specify-maximum-rows-of-shared-formula/  
description: 学习如何使用 Aspose.Cells for Node.js via C++ 指定共享公式的最大行数。  
---  

## **可能的使用场景**  

 默认共享公式的最大行数是 64。可以设置任何数字，例如1000。不同的行数会影响共享公式的性能。因此，Aspose.Cells 提供了 [**WorkbookSettings.getMaxRowsOfSharedFormula()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getMaxRowsOfSharedFormula--) 属性，可以用来指定共享公式的最大行数。如果总行数超过设置的数值，共享公式将被拆分成多个共享公式，如下图所示。  

![todo:image_alt_text](specify-maximum-rows-of-shared-formula_1.png)  

## **指定共享公式的最大行数**  

以下示例代码演示了 [**WorkbookSettings.getMaxRowsOfSharedFormula()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getMaxRowsOfSharedFormula--) 属性的使用。它将共享公式的最大行数设置为 5，并在单元格 D1 中添加了 100 行的共享公式，保存为 [输出Excel文件](61767856.xlsx)。 若解压输出Excel文件内容并检查 *sheet1.xml*，你会看到共享公式每5行分割一次，如上述截图所示。  

## **示例代码**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

// Create a new workbook
const wb = new AsposeCells.Workbook();

// Set the max rows of shared formula to 5
wb.getSettings().setMaxRowsOfSharedFormula(5);

// Access first worksheet
const ws = wb.getWorksheets().get(0);

// Access cell D1
const cell = ws.getCells().get("D1");

// Set the shared formula in 100 rows
cell.setSharedFormula("=Sum(A1:A2)", 100, 1);

// Save the output Excel file
wb.save("outputSpecifyMaximumRowsOfSharedFormula.xlsx");
```  

