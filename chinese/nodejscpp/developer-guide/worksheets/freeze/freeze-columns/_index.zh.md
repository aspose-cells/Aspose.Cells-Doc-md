---  
title: 使用 Node.js 和 C++ 冻结 Excel 工作表的首列  
linktitle: 冻结列  
type: docs  
weight: 190  
url: /zh/nodejs-cpp/how-to-freeze-columns-of-excel-worksheet  
description: 学习如何以编程方式使用 Aspose.Cells for Node.js via C++ 冻结 Excel 工作表的左列。  
keywords: 冻结左侧列，冻结首列，锁定列  
---  

## **介绍**  

在本文中，我们将学习如何冻结左列。当一行中有大量数据时，你可能无法在横向滚动时看到左边的列。你可以冻结并锁定首列，使其即使在滚动其他数据时仍然可见。这样可以轻松查看左列的标题。  

## **Excel中的冻结列**  

**![在Excel中冻结左侧列](freeze-columns.png)**  

1. 如果您想冻结左列，则首先选择需要冻结的列下面的列。
2. 单击“查看”>“冻结窗格”
3. 在下拉菜单上，单击“冻结第一列”
4. 滚动时，第一列始终显示在左侧视图中。

**![冻结列](frozen-columns.png)**  

如你所见，第1列已被冻结，当你横向滚动时，首列始终锁定在视图顶部。

冻结列让你无需担心，轻松查看你的长数据。

## **使用 Aspose.Cells for Node.js via C++ 冻结列**  
使用Aspose.Cells for Node.js via C++冻结第一列非常简单。  
请使用[**Worksheet.freezePanes(number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#freezePanes-number-number-number-number-)方法在选定的列上冻结列。  
1.构建工作簿以打开文件或创建一个空文件。
2. 使用Worksheet.freezePanes()方法冻结第一列。
3.保存文件。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Freeze.xlsx");
// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook(filePath);
// Freezing panes at the second column
workbook.getWorksheets().get(0).freezePanes("B1", 0, 1);
// Saving the file
workbook.save("frozen.xlsx");
```  

附上[示例源Excel文件](Freeze.xlsx)。  

{{< app/cells/assistant language="nodejs-cpp" >}}
