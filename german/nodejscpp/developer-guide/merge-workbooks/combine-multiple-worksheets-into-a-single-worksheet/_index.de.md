---
title: Mehrere Arbeitsblätter mit Node.js via C++ zu einem einzigen Arbeitsblatt zusammenfassen
linktitle: Mehrere Arbeitsblätter zu einem einzigen Arbeitsblatt zusammenfassen
type: docs
weight: 160
url: /de/nodejs-cpp/combine-multiple-worksheets-into-a-single-worksheet/
description: Lernen Sie, wie man mehrere Arbeitsblätter mit Aspose.Cells for Node.js via C++ in ein einzelnes Arbeitsblatt zusammenführt. 
---

{{% alert color="primary" %}} 

Manchmal müssen mehrere Arbeitsblätter in einem einzigen Arbeitsblatt zusammengeführt werden. Dies kann einfach über die Aspose.Cells API erreicht werden. In diesem Artikel wird Ihnen ein Codebeispiel gezeigt, das eine Quellarbeitsmappe liest und die Daten aller Quellarbeitsblätter in einem Zieltabellenblatt innerhalb einer Ziellarbeitsmappe zusammenführt.

{{% /alert %}} 

Der folgende Code-Schnipsel zeigt Ihnen, wie Sie mehrere Arbeitsblätter in ein einziges Arbeitsblatt kombinieren können.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "SampleInput.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

const destWorkbook = new AsposeCells.Workbook();
const destSheet = destWorkbook.getWorksheets().get(0);

let TotalRowCount = 0;

for (let i = 0; i < workbook.getWorksheets().getCount(); i++) {
const sourceSheet = workbook.getWorksheets().get(i);

const sourceRange = sourceSheet.getCells().getMaxDisplayRange();
const destRange = destSheet.getCells().createRange(
sourceRange.getFirstRow() + TotalRowCount,
sourceRange.getFirstColumn(),
sourceRange.getRowCount(),
sourceRange.getColumnCount()
);

destRange.copy(sourceRange);
TotalRowCount += sourceRange.getRowCount();
}

const outputFilePath = path.join(dataDir, "Output.out.xlsx");
destWorkbook.save(outputFilePath);
``` 
{{< app/cells/assistant language="nodejs-cpp" >}}
