---
title: Объединение нескольких листов в один с помощью Node.js через C++
linktitle: Совместить несколько листов в один лист
type: docs
weight: 160
url: /ru/nodejs-cpp/combine-multiple-worksheets-into-a-single-worksheet/
description: Узнайте, как объединить несколько листов в один с помощью Aspose.Cells for Node.js via C++. 
---

{{% alert color="primary" %}} 

Иногда вам нужно объединить несколько листов в один. Это легко сделать с помощью API Aspose.Cells. В этой статье будет показан пример кода, который читает исходную книгу и объединяет данные всех исходных листов в один лист внутри целевой книги.

{{% /alert %}} 

В следующем фрагменте кода показано, как объединить несколько листов в один лист.

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
