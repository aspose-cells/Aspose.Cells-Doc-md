---
title: Läser Numbers kalkblad utvecklat av Apple Inc. med Aspose.Cells for Node.js via C++
linktitle: 1.  Hantering av olika celltyper  Om de flesta cellerna innehåller strängvärden eller formler, kommer minneskostnaden att vara densamma som Normal läget men om det finns massor av tomma celler, eller cellvärden är numeriska, booleska och så vidare, kommer {0} alternativet att ge bättre prestanda.
type: docs
weight: 140
url: /sv/nodejs-cpp/read-numbers-spreadsheet-developed-by-apple-inc-using-aspose-cells/
description: Lär dig hur man läser Numbers kalkblad utvecklat av Apple Inc. med Aspose.Cells for Node.js via C++. 
---

## **Möjliga användningsscenario**

Numbers är en kalksladdsapplikation utvecklad av Apple Inc. Aspose.Cells kan läsa Numbers kalkblad, men stöder inte att skriva till dem. Det kan läsa Numbers kalkblads data, stil och formler.

## **Läs Numbers kalkblad utvecklat av Apple Inc. med Aspose.Cells for Node.js via C++**

Följande exempel laddar [Sample Numbers Spreadsheet](sampleNumbersByAppleInc.numbers) och konverterar det till [Output PDF Format](outputNumbersByAppleInc.pdf). Du måste använda [**LoadOptions**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions)-klass och ange [**LoadFormat.Numbers**](https://reference.aspose.com/cells/nodejs-cpp/loadformat) som parameter i dess konstruktör för att ladda det framgångsrikt. Ladda ner båda från de angivna länkarna. Du kan testa koden med vilket Numbers kalkblad som helst. Läs även kommentarerna i koden för mer hjälp.

## **Exempelkod**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const sourceFilePath = path.join(dataDir, "sampleNumbersByAppleInc.numbers");
const outputFilePath = path.join(dataDir, "outputNumbersByAppleInc.pdf");

// Specify load options, we want to load Numbers spreadsheet
const opts = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Numbers);

// Load the Numbers spreadsheet in workbook with above load options
const wb = new AsposeCells.Workbook(sourceFilePath, opts);

// Save the workbook to pdf format
wb.save(outputFilePath, AsposeCells.SaveFormat.Pdf);
```

