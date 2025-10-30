---
title: Beräkning av IFNA funktion med Aspose.Cells for Node.js via C++
description: Hur man beräknar IFNA funktioner med Aspose.Cells biblioteket för Node.js via C++. Ladda en befintlig Excel fil eller skapa en ny, och beräkna IFNA funktionen för att få resultatet. Slutligen sparar du den modifierade Excel filen till disk.
keywords: Aspose.Cells, Excel, IFNA funktioner, beräkningar Node.js via C++
type: docs
weight: 40
url: /sv/nodejs-cpp/calculating-ifna-function-using-aspose-cells/
---

{{% alert color="primary" %}} 

Aspose.Cells stöder beräkning av IFNA Excel-funktionen. Funktionen RETURNERAR det värde du specificerar om formeln returnerar #N/A felvärdet; annars returnerar den resultatet av formeln.

{{% /alert %}} 
## **Beräkning av IFNA-funktion med Aspose.Cells for Node.js via C++**
Följande exempel kod visar beräkningen av IFNA-funktionen med Aspose.Cells for Node.js via C++.


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
## **Konsoloutput**
Här är konsoloutputen från ovanstående exempelkod.

{{< highlight javascript >}}
 Not found

Orange
{{< /highlight >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
