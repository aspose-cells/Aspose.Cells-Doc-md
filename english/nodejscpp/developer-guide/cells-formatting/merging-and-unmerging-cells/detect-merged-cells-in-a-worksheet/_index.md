---
title: Detect Merged Cells in a Worksheet with Node.js via C++
linktitle: Detect Merged Cells in a Worksheet
description: Learn how to detect merged cells in a worksheet using Aspose.Cells for Node.js via C++. This article will show you how to use the library to identify and manipulate merged cells.
keywords: Aspose.Cells, Worksheet, Merge Cells, Detect, Identify, Operate Node.js via C++
type: docs
weight: 80
url: /nodejs-cpp/detect-merged-cells-in-a-worksheet/
---

{{% alert color="primary" %}}

This article provides information on how to get merged cell areas in a worksheet.

Aspose.Cells for Node.js via C++ allows you to get merged cell areas in a worksheet. You can unmerge (split) them too. This article shows the simplest code using **Aspose.Cells API** to perform the task.

{{% /alert %}}

The component provides the [**Cells.getMergedAreas()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getMergedAreas--) method which can get all merged cells. The following code sample shows you how to detect merged cells in a worksheet.

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