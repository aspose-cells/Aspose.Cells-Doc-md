---
title: Upptäck sammanslagna celler i ett kalkylblad med Node.js via C++
linktitle: Upptäck sammanfogade celler i ett arbetsblad
description: Lär dig hur du upptäcker sammanslagna celler i ett kalkylblad med Aspose.Cells for Node.js via C++. Denna artikel visar hur du använder biblioteket för att identifiera och manipulera sammanslagna celler.
keywords: Aspose.Cells, Kalkylblad, Sammanfoga celler, Upptäck, Identifiera, Operera Node.js via C++
type: docs
weight: 80
url: /sv/nodejs-cpp/detect-merged-cells-in-a-worksheet/
---

{{% alert color="primary" %}}

Den här artikeln ger information om hur man får sammanfogade cellområden i ett arbetsblad.

Aspose.Cells for Node.js via C++ låter dig hämta sammanslagna cellområden i ett kalkylblad. Du kan också upplösa ( dela upp) dem. Den här artikeln visar den enklaste koden med **Aspose.Cells API** för att utföra uppgiften.

{{% /alert %}}

 Komponenten tillhandahåller [**Cells.getMergedAreas()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getMergedAreas--) metoden som kan hämta alla sammanslagna celler. Följande kodexempel visar hur du upptäcker sammanslagna celler i ett kalkylblad.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "SampleInput.xlsx");

// Instantiate a new Workbook
// Open an existing excel file
const wkBook = new AsposeCells.Workbook(filePath);
// Get a worksheet in the workbook
const wkSheet = wkBook.getWorksheets().get("Sheet2");
// Clear its contents
wkSheet.getCells().clear();

// Get merged areas
const areas = wkSheet.getCells().getMergedAreas();

// Check if areas is null or not
if (!areas || areas.length === 0) {
console.warn("No merged areas to unmerge.");
return;
}

// Define some variables
let frow, fcol, erow, ecol, trows, tcols;
// Loop through the arraylist and get each cellarea
// To unmerge it
for (let i = 0; i < areas.length; i++) {
frow = areas[i].startRow;
fcol = areas[i].startColumn;
erow = areas[i].endRow;
ecol = areas[i].endColumn;

trows = erow - frow + 1;
tcols = ecol - fcol + 1;
wkSheet.getCells().unMerge(frow, fcol, trows, tcols);
}

const outputFilePath = path.join(dataDir, "MergeTrial.out.xlsx");
// Save the excel file
wkBook.save(outputFilePath);
```
