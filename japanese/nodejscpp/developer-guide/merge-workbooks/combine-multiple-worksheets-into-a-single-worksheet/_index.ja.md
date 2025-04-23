---
title: Node.jsを利用して複数のワークシートを一つのワークシートに結合
linktitle: 複数のワークシートを1つのワークシートに結合する
type: docs
weight: 160
url: /ja/nodejs-cpp/combine-multiple-worksheets-into-a-single-worksheet/
description: Aspose.Cells for Node.js via C++を使った複数のワークシートの結合方法を学びます。 
---

{{% alert color="primary" %}} 

複数のワークシートを1つのワークシートに結合する必要がある場合があります。Aspose.Cells APIを使用すれば簡単に実現できます。この記事では、ソースブックを読み込み、すべてのソースワークシートのデータを目的のワークブック内の単一のワークシートに結合するコード例を紹介します。

{{% /alert %}} 

以下のコードスニペットでは、複数のワークシートを1つのワークシートに結合する方法が示されています。

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
