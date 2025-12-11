---  
title: Set Worksheet Tab Color with Node.js via C++  
linktitle: Set Worksheet Tab Color  
type: docs  
weight: 120  
url: /nodejs-cpp/set-worksheet-tab-color/  
description: This article demonstrates sample code that sets the Excel worksheet tab color programmatically using Node.js via C++.  
keywords: set excel tab color Node.js via C++, code to set excel tab color Node.js via C++  
ai_search_scope: cells_nodejscpp  
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"  
---  

{{% alert color="primary" %}}  

Aspose.Cells allows you to change the color of individual worksheet tabs to make them stand out from the rest. For example, you can make Expenses red, Sales green, Assets blue, etc.  

{{% /alert %}}  

## **Setting Worksheet Tab Color with Microsoft Excel**  

1. Right‑click a tab on the sheet tab bar at the bottom of the workbook.  
2. Select **Tab Color**.  
3. Choose a color from the palette.  
4. Click **OK**.  

## **Setting Worksheet Tab Color with Aspose.Cells**  

The sample code below shows how to set the tab color with Aspose.Cells.  

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
