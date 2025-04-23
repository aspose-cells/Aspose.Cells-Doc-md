---
title: Kombinera flera arbetsblad till ett enda med Node.js via C++
linktitle: Kombinera flera arkmallar till ett enda ark
type: docs
weight: 160
url: /sv/nodejs-cpp/combine-multiple-worksheets-into-a-single-worksheet/
description: Lär dig hur du kombinerar flera arbetsblad till ett enda med Aspose.Cells for Node.js via C++. 
---

{{% alert color="primary" %}} 

Ibland behöver du kombinera flera kalkylblad till ett enda kalkylblad. Detta kan enkelt uppnås med Aspose.Cells API. Den här artikeln visar ett kodexempel som läser in en källbok och kombinerar datan från alla källkalkylblad till ett enda kalkylblad i en målbok.

{{% /alert %}} 

Följande kodsnutt visar hur du kombinerar flera arkmallar till ett enda ark.

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
