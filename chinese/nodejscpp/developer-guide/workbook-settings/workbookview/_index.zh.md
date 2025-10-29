---
title: 如何用Node.js通过C++控制工作簿视图
linktitle: 如何控制工作簿视图
type: docs
weight: 600
url: /zh/nodejs-cpp/how-to-control-workbook-view/
description: 了解如何通过Aspose.Cells for Node.js via C++ API控制工作簿视图。
keywords: 如何通过C++在Node.js中控制工作簿视图、设置Excel视图、操作工作簿视图、设置工作簿视图、控制Excel视图。
---

## **可能的使用场景**
当需要调整Excel页面显示时，你需要了解如何控制各个模块，如水平和垂直滚动条、是否隐藏打开的Excel文件等。Aspose.Cells for Node.js via C++提供了此功能。Aspose.Cells for Node.js via C++提供了以下属性和方法，帮助你实现目标。

- [**WorkbookSettings.isHScrollBarVisible()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#isHScrollBarVisible--)
- [**WorkbookSettings.isVScrollBarVisible()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#isVScrollBarVisible--)
- [**WorkbookSettings.isHidden()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#isHidden--)
- [**WorkbookSettings.isMinimized()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#isMinimized--)
- [**WorkbookSettings.getWindowHeight()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getWindowHeight--)
- [**WorkbookSettings.getWindowWidth()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getWindowWidth--)
- [**WorkbookSettings.getWindowLeft()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getWindowLeft--)
- [**WorkbookSettings.getWindowTop()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getWindowTop--)

## **如何使用Aspose.Cells for Node.js via C++控制工作簿视图**
此示例演示如何：

1. 创建一个工作簿。
1. 在第一个工作表中的单元格中添加数据。
1. 隐藏工作簿视图的水平和垂直滚动条。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

// Instantiating an Workbook object
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

cell = cells.get("B2");
cell.putValue(5);
cell = cells.get("B3");
cell.putValue(3);
cell = cells.get("B4");
cell.putValue(6);
cell = cells.get("B5");
cell.putValue(4);

cell = cells.get("C2");
cell.putValue(5);
cell = cells.get("C3");
cell.putValue(20);
cell = cells.get("C4");
cell.putValue(30);
cell = cells.get("C5");
cell.putValue(60);

cell = cells.get("E10");
const temp = workbook.createStyle();
temp.getFont().setColor(AsposeCells.Color.Red);
cell.setStyle(temp);

// Hide horizontal and vertical scrollbars
workbook.getSettings().setIsHScrollBarVisible(false);
workbook.getSettings().setIsVScrollBarVisible(false);

workbook.save("out.xlsx");
```

结果文件预览：
<br>
<image src="result.png" width="70%" />

{{< app/cells/assistant language="nodejs-cpp" >}}
