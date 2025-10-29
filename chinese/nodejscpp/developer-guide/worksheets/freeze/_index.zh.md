---  
title: 用Node.js与C++冻结Excel工作表的窗格  
linktitle: 冻结窗格  
type: docs  
weight: 190  
url: /zh/nodejs-cpp/how-to-freeze-panes-of-excel-worksheet  
description: 本文介绍如何使用Aspose.Cells for Node.js via C++编程冻结Excel工作表的窗格。  
keywords: 冻结窗格，冻结窗口。  
---  

## **介绍**  

 本文介绍如何冻结窗格。当你有大量数据在共同标题下时，滚动后无法看到标题行，且每条记录包含许多数据。通过冻结窗格，可以在滚动时仍然看到冻结的部分。你可以方便地看到顶部行或首列的标题。冻结和取消冻结窗格只会改变数据的视图，不会改变数据本身。  

## **在Excel中**  

**![Excel中的冻结窗格](Freeze-panes.png)**  

 1. 若要冻结窗格、冻结行列，先选中一个单元格（如B2）。  
2. 单击“查看”>“冻结窗格”  
3. 在下拉菜单上，单击“冻结窗格”  
 4. 向下或向右滚动时，第一行和第一列会被冻结。  

**![冻结窗格](Frozen-Panes.png)**  

如图所示，第1行和列A被冻结，第2行是第三行，第2个可见列是D。  

冻结窗格使您可以在查看大量数据时不必跟踪行或列标签。  

## **与Aspose.Cells for Node.js via C++一起冻结窗格**  
使用Aspose.Cells for Node.js via C++冻结窗格非常简单。请使用[**Worksheet.freezePanes(number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#freezePanes-number-number-number-number-)方法在选定单元格处冻结窗格。  
1.构建工作簿以打开文件或创建一个空文件。  
2. 使用Worksheet.freezePanes()方法冻结窗格。  
3.保存文件。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "Freeze.xlsx")); 
// Freezing panes at the cell B2
workbook.getWorksheets().get(0).freezePanes("B2", 1, 1);
// Saving the file
workbook.save("frozen.xlsx");
```  

附上[示例源Excel文件](Freeze.xlsx)。  

{{< app/cells/assistant language="nodejs-cpp" >}}
