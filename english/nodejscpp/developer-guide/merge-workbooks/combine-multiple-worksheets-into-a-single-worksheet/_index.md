---
title: Combine Multiple Worksheets into a Single Worksheet with Node.js via C++
linktitle: Combine Multiple Worksheets into a Single Worksheet
type: docs
weight: 160
url: /nodejs-cpp/combine-multiple-worksheets-into-a-single-worksheet/
description: Learn how to combine multiple worksheets into a single worksheet using Aspose.Cells for Node.js via C++. 
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}} 

Sometimes, you need to combine multiple worksheets into a single worksheet. This can easily be achieved using Aspose.Cells API. This article will show you a code example that reads a source workbook and combines the data of all source worksheets into a single worksheet inside a destination workbook.

{{% /alert %}} 

The following code snippet shows you how to combine multiple worksheets into a single worksheet.

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
