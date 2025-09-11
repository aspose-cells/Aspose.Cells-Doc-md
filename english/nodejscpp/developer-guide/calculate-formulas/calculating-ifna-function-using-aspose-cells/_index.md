---
title: Calculating IFNA function using Aspose.Cells for Node.js via C++
description: How to calculate IFNA functions using the Aspose.Cells library for Node.js via C++. Load an existing Excel file or create a new one, and calculate the IFNA function to get the result. Finally, save the modified Excel file to disk.
keywords: Aspose.Cells, Excel, IFNA functions, calculations Node.js via C++
type: docs
weight: 40
url: /nodejs-cpp/calculating-ifna-function-using-aspose-cells/
---

{{% alert color="primary" %}} 

Aspose.Cells supports the calculation of the IFNA Excel function. The IFNA function returns the value you specify if the formula returns the #N/A error value; otherwise, it returns the result of the formula.

{{% /alert %}} 
## **Calculating IFNA function using Aspose.Cells for Node.js via C++**
The following sample code illustrates the calculation of the IFNA function using Aspose.Cells for Node.js via C++.


```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Create new workbook
// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Add data for VLOOKUP
worksheet.getCells().get("A1").putValue("Apple");
worksheet.getCells().get("A2").putValue("Orange");
worksheet.getCells().get("A3").putValue("Banana");

// Access cell A5 and A6
const cellA5 = worksheet.getCells().get("A5");
const cellA6 = worksheet.getCells().get("A6");

// Assign IFNA formula to A5 and A6
cellA5.setFormula('=IFNA(VLOOKUP("Pear",$A$1:$A$3,1,0),"Not found")');
cellA6.setFormula('=IFNA(VLOOKUP("Orange",$A$1:$A$3,1,0),"Not found")');

// Calculate the formula of workbook
workbook.calculateFormula();

// Print the values of A5 and A6
console.log(cellA5.getStringValue());
console.log(cellA6.getStringValue());
```
## **Console Output**
Here is the console output of the above sample code.

{{< highlight javascript >}}
 Not found

Orange
{{< /highlight >}}
{{< app/cells/assistant language="nodejs-cpp" >}}