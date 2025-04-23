---
title: Användning av FunktionText i Aspose.Cells for Node.js via C++
linktitle: Använda FormulaText funktion i Aspose.Cells
description: Denna artikel introducerar hur man använder FunktionText funktionen i Aspose.Cells biblioteket för att bearbeta formler i Microsoft Excel. Lär dig att få och ställa in formeltext för celler och spara modifierade Excel filer med Node.js via C++.
keywords: Aspose.Cells, Excel, FunktionText funktioner Node.js via C++
type: docs
weight: 60
url: /sv/nodejs-cpp/using-formulatext-function-in-aspose-cells/
---

{{% alert color="primary" %}} 

FunktionText är en Excel 2013 och senare funktion. Den stöds inte av tidigare versioner som Excel 2010 eller 2007 osv. Som namnet antyder skriver den ut texten för formeln som finns i en given cell. Denna artikel visar hur du använder denna funktion med Aspose.Cells for Node.js via C++.

{{% /alert %}} 

Följande kod visar användningen av FunktionText med Aspose.Cells for Node.js via C++. Koden skriver först en formel i cell A1 och skriver sedan ut formelns text med FunktionText i cell A2.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Create a workbook object
// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Put some formula in cell A1
const cellA1 = worksheet.getCells().get("A1");
cellA1.setFormula("=Sum(B1:B10)");

// Get the text of the formula in cell A2 using FORMULATEXT function
const cellA2 = worksheet.getCells().get("A2");
cellA2.setFormula("=FormulaText(A1)");

// Calculate the workbook
workbook.calculateFormula();

// Print the results of A2, It will now print the text of the formula inside cell A1
console.log(cellA2.getStringValue());
```
## **Konsoloutput**
Här är konsoloutputen från ovanstående exempelkod.

{{< highlight java >}}

 =SUM(B1:B10)

{{< /highlight >}}
