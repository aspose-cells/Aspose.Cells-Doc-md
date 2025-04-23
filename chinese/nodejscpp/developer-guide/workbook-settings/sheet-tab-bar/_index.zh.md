---  
title: 如何用Node.js通过C++控制工作表标签栏  
linktitle: 如何控制选项卡工具栏  
type: docs  
weight: 600  
url: /zh/nodejs-cpp/how-to-control-sheet-tab-bar/  
description: 学习如何使用Aspose.Cells for Node.js via C++控制工作表标签栏。  
keywords: 如何用C++通过Node.js控制工作表标签栏  
---  

## **可能的使用场景**  
当你需要调整Excel工作表栏的显示时，需要了解如何控制工作表标签栏，例如隐藏或显示标签栏、更改单个标签栏宽度、设置第一个可见标签等。Aspose.Cells for Node.js via C++支持这些功能。Aspose.Cells提供了以下属性和方法帮助你实现目标。

- [**WorkbookSettings.getShowTabs()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getShowTabs--)
- [**WorkbookSettings.getSheetTabBarWidth()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getSheetTabBarWidth--)
- [**WorkbookSettings.getFirstVisibleTab()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getFirstVisibleTab--)

## **如何用Aspose.Cells for Node.js via C++控制工作表标签栏**  
此示例演示如何：

1. 创建一个工作簿。
1. 在第一个工作表中的单元格中添加数据。
1. 显示工作表标签并设置标签栏的宽度。

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook();

// Obtaining the reference of the newly added worksheet
const ws = workbook.getWorksheets().get(0);
const cells = ws.getCells();

// Setting the value to the cells
let cell = cells.get("A1");
cell.putValue("Fruit");
cell = cells.get("B1");
cell.putValue("Count");
cell = cells.get("C1");
cell.putValue("Price");

cell = cells.get("A2");
cell.putValue("Apple");
cell = cells.get("A3");
cell.putValue("Mango");
cell = cells.get("A4");
cell.putValue("Blackberry");
cell = cells.get("A5");
cell.putValue("Cherry");

// Display the sheet tab and set the width of the tab bar
workbook.getSettings().setShowTabs(true);
workbook.getSettings().setSheetTabBarWidth(150);

workbook.save("out.xlsx");
```

结果文件预览：  
<br>  
<image src="result.png" width="70%" />  


