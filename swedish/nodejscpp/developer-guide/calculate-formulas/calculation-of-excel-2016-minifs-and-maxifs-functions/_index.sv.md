---
title: Beräkning av Excel 2016 MINIFS och MAXIFS funktioner med Node.js via C++
description: Denna artikel introducerar hur man använder Aspose.Cells biblioteket för att beräkna MINIFS och MAXIFS funktioner i Microsoft Excel 2016 med Node.js via C++. Ladda en befintlig Excel fil eller skapa en ny, använd sedan Aspose.Cells metoder för att beräkna dessa funktioner och spara resultaten till disk.
keywords: Aspose.Cells, Excel, 2016, MINIFS funktion, MAXIFS funktion, beräkning Node.js via C++
type: docs
weight: 300
url: /sv/nodejs-cpp/calculation-of-excel-2016-minifs-and-maxifs-functions/
---

## **Möjliga användningsscenario**
Microsoft Excel 2016 stöder MINIFS- och MAXIFS-funktionerna. Dessa funktioner stöds inte i Excel 2013 eller tidigare versioner. Aspose.Cells for Node.js via C++ stöder också beräkningen av dessa funktioner. Följande skärmdump visar hur dessa funktioner används. Läs de röda kommentarerna i skärmbilderna för att förstå hur dessa funktioner fungerar.

![todo:image_alt_text](calculation-of-excel-2016-minifs-and-maxifs-functions_1.png)

## **Beräkning av Excel 2016 MINIFS och MAXIFS funktioner**
Följande exempelkod laddar [exempel excelfilen](5115149.xlsx) och anropar metoden [Workbook.calculateFormula()](https://reference.aspose.com/cells/nodejs-cpp/workbook/#calculateFormula--) för att utföra formelberäkningen via Aspose.Cells for Node.js via C++, och sparar sedan resultaten i [output PDF](5115154.pdf).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const sourceFilePath = path.join(dataDir, "sampleMINIFSAndMAXIFS.xlsx");

// Load your source workbook containing MINIFS and MAXIFS functions
const workbook = new AsposeCells.Workbook(sourceFilePath);

// Perform Aspose.Cells formula calculation
workbook.calculateFormula();

// Save the calculations result in pdf format
const options = new AsposeCells.PdfSaveOptions();
options.setOnePagePerSheet(true);
const outputFilePath = path.join(dataDir, "outputMINIFSAndMAXIFS.pdf");
workbook.save(outputFilePath, options);
```
{{< app/cells/assistant language="nodejs-cpp" >}}
