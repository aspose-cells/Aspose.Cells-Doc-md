---  
title: Set Worksheet Tab Color with Node.js via C++  
linktitle: Set Worksheet Tab Color  
type: docs  
weight: 120  
url: /nodejs-cpp/set-worksheet-tab-color/  
description: This article demonstrates sample code that sets the Excel worksheet Tab Color programmatically using Node.js via C++.  
keywords: set excel tab color Node.js via C++, code to set excel tab color Node.js via C++  
---  

{{% alert color="primary" %}}  

Aspose.Cells allows you to change the color of individual worksheet tabs to make them prominent from the rest. For example, you can make Expenses red, Sales green, Assets blue, etc.

{{% /alert %}}  
## **Setting Worksheet Tab Color with Microsoft Excel**  
1. Right-click a tab in the tab-sheet at the bottom of the current worksheet.  
1. Select **Tab color**.  
1. Select a color from the palette.  
1. Click **OK**.  
## **Setting Worksheet Tab Color with Aspose.Cells**  
The sample code below shows how to set tab color with Aspose.Cells.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Instantiate a new Workbook
// Open an Excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "Book1.xlsx"));

// Get the first worksheet in the book
const worksheet = workbook.getWorksheets().get(0);

// Set the tab color
worksheet.setTabColor(AsposeCells.Color.Red);

// Save the Excel file
workbook.save(path.join(dataDir, "worksheettabcolor.out.xls"));
```  
  
{{< app/cells/assistant language="nodejs-cpp" >}}