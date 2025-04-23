---
title: Node.js via C++によるワークシート内の結合セルの検出
linktitle: ワークシート内の結合セルを検出
description: Aspose.Cells for Node.js via C++を使用してワークシート内の結合セルを検出する方法を学びます。この方法では、ライブラリを使用して結合セルを特定および操作します。
keywords: Aspose.Cells、ワークシート、セルの結合、検出、特定、操作、Node.js via C++
type: docs
weight: 80
url: /ja/nodejs-cpp/detect-merged-cells-in-a-worksheet/
---

{{% alert color="primary" %}}

この記事では、ワークシート内の結合セル領域を取得する方法について説明しています。

Aspose.Cells for Node.js via C++は、ワークシート内の結合セル範囲を取得できます。解除（分割）も可能です。この記事では、**Aspose.Cells API**を使用した最もシンプルなコード例を示します。

{{% /alert %}}

このコンポーネントは、すべての結合セルを取得できる[**Cells.getMergedAreas()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getMergedAreas--)メソッドを提供します。以下のコード例は、ワークシート内の結合セルを検出する方法を示しています。

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
