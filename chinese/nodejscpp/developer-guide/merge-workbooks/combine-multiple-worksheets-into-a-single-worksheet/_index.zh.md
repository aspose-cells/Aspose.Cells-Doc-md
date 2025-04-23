---
title: 使用 Node.js 通过 C++ 将多个工作表合并为一个工作表
linktitle: 将多个工作表合并为单个工作表
type: docs
weight: 160
url: /zh/nodejs-cpp/combine-multiple-worksheets-into-a-single-worksheet/
description: 学习如何使用 Aspose.Cells for Node.js via C++ 将多个工作表合并为一个工作表。 
---

{{% alert color="primary" %}} 

有时候，您需要将多个工作表合并成一个工作表。通过使用 Aspose.Cells API，可以轻松实现这一目标。本文将展示一个代码示例，该示例读取源工作簿，并将所有源工作表的数据合并到目标工作簿中的一个工作表中。

{{% /alert %}} 

以下代码片段向您展示了如何将多个工作表合并为单个工作表。

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
