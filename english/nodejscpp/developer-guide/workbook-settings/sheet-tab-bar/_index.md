---  
title: How to Control Sheet Tab Bar with Node.js via C++  
linktitle: How to Control Sheet Tab Bar  
type: docs  
weight: 600  
url: /nodejs-cpp/how-to-control-sheet-tab-bar/  
description: Learn how to control the sheet tab bar using Aspose.Cells for Node.js via C++.  
keywords: How to Control Sheet Tab Bar Node.js via C++, Operate Sheet Tab Bar Node.js via C++, Set Sheet Tab Bar Node.js via C++, Control Sheet Tab Bar Node.js via C++.  
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---  

## **Possible Usage Scenarios**  
When you need to adjust the display of Excel sheet bar, you need to know how to control the sheet tab bar, such as hiding or showing the sheet tab bar, changing the sheet tab bar width, specifying the first visible tab, and so on. Aspose.Cells for Node.js via C++ supports these features. Aspose.Cells provides the following properties and methods to help you achieve your goals.

- [**WorkbookSettings.getShowTabs()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getShowTabs--)
- [**WorkbookSettings.getSheetTabBarWidth()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getSheetTabBarWidth--)
- [**WorkbookSettings.getFirstVisibleTab()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getFirstVisibleTab--)

## **How to Control Sheet Tab Bar using Aspose.Cells for Node.js via C++**  
This example shows how to:

1. Create a workbook.
1. Add data to cells in the first worksheet.
1. Display the sheet tab and set the width of the tab bar.

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

Result file preview:  
<br>  
<image src="result.png" width="70%" />  

  
{{< app/cells/assistant language="nodejs-cpp" >}}
