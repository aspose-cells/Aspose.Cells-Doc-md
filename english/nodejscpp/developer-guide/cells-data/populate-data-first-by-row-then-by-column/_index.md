---  
title: Populate Data First by Row then by Column with Node.js via C++  
linktitle: Populate Data First by Row then by Column  
type: docs  
weight: 1000  
url: /nodejs-cpp/populate-data-first-by-row-then-by-column/  
description: Learn how to Populate Data First by Row then by Column through the Aspose.Cells for Node.js via C++ API.  
keywords: Populate Data First by Row then by Column Node.js via C++, Insert Data First by Row then by Column Node.js via C++, Add Data First by Row then by Column Node.js via C++, High performance data insertion Node.js via C++, High performance data addition Node.js via C++  
---  

{{% alert color="primary" %}}  

Populating a spreadsheet with data first by row and then by column improves the overall performance.  

{{% /alert %}}  

Putting data in the sequence A1, B1, A2, B2 is faster than A1, A2, B1, B2. If there are many cells in a worksheet and you follow the second sequence, that is, you're filling the data row by row, this tip can make the program much faster.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create a workbook
const workbook = new AsposeCells.Workbook();

// Populate Data into Cells
const cells = workbook.getWorksheets().get(0).getCells();
cells.get("A1").putValue("data1");
cells.get("B1").putValue("data2");
cells.get("A2").putValue("data3");
cells.get("B2").putValue("data4");

// Save workbook
workbook.save(path.join(dataDir, "output_out.xlsx"));
```  
  