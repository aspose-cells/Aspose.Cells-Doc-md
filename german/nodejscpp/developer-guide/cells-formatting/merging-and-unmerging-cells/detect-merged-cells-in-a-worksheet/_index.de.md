---
title: Merged Cells in einem Arbeitsblatt mit Node.js über C++ erkennen
linktitle: Erkennen von zusammengeführten Zellen in einem Arbeitsblatt
description: Erfahren Sie, wie Sie verschmolzene Zellen in einem Arbeitsblatt mit Aspose.Cells for Node.js via C++ erkennen. Dieser Artikel zeigt, wie Sie die Bibliothek verwenden, um verschmolzene Zellen zu identifizieren und zu manipulieren.
keywords: Aspose.Cells, Arbeitsblatt, Zellen zusammenführen, Erkennen, Identifizieren, Betrieb Node.js über C++
type: docs
weight: 80
url: /de/nodejs-cpp/detect-merged-cells-in-a-worksheet/
---

{{% alert color="primary" %}}

Dieser Artikel enthält Informationen dazu, wie man zusammengeführte Zellenbereiche in einem Arbeitsblatt erhält.

Aspose.Cells for Node.js via C++ ermöglicht es Ihnen, zusammengeführte Zellbereiche in einem Arbeitsblatt zu erhalten. Sie können sie auch entkoppeln (aufteilen). Dieser Artikel zeigt den einfachsten Code mit der **Aspose.Cells API** für diese Aufgabe.

{{% /alert %}}

Die Komponente bietet die [**Cells.getMergedAreas()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getMergedAreas--) Methode, mit der alle zusammengeführten Zellen ermittelt werden können. Das folgende Codebeispiel zeigt, wie zusammengeführte Zellen in einem Arbeitsblatt erkannt werden.

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
{{< app/cells/assistant language="nodejs-cpp" >}}
