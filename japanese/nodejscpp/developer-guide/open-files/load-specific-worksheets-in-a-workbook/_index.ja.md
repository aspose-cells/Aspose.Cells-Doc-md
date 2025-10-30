---
title: 特定のシートだけを読み込む：Node.jsとC++
linktitle: ワークブック内の特定のワークシートのみをロードする
type: docs
weight: 100
url: /ja/nodejs-cpp/load-specific-worksheets-in-a-workbook/
description: Aspose.Cells for Node.js via C++ を使用して、特定のワークシートを読み込む方法を学びます。パフォーマンスの向上とメモリ消費の削減に役立ちます。
---

{{% alert color="primary" %}}

Aspose.Cellsはデフォルトでスプレッドシート全体をメモリに読み込みます。特定のシートのみをロードすることも可能です。これはパフォーマンスが向上し、メモリをより少なく消費することができる点で有用です。大きなワークブックを扱う際や多くのワークシートからなる場合に有用です。

{{% /alert %}}

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Define a new Workbook.
let workbook;

// Load the workbook with the specified worksheet only.
const loadOptions = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Xlsx);
loadOptions.setLoadFilter(new CustomLoad());

// Create the workbook.
workbook = new AsposeCells.Workbook(path.join(dataDir, "TestData.xlsx"), loadOptions);

// Perform your desired task.

// Save the workbook.
workbook.save(path.join(dataDir, "outputFile.out.xlsx"));
```

CustomLoadクラスの実装例です。

```javascript
const AsposeCells = require("aspose.cells.node");

class CustomLoad extends AsposeCells.LoadFilter {
startSheet(sheet) {
if (sheet.getName() === "Sheet2") {
// Load everything from worksheet "Sheet2"
this.setLoadDataFilterOptions(AsposeCells.LoadDataFilterOptions.All);
} else {
// Load nothing
this.setLoadDataFilterOptions(AsposeCells.LoadDataFilterOptions.Structure);
}
}
}
```


{{< app/cells/assistant language="nodejs-cpp" >}}
