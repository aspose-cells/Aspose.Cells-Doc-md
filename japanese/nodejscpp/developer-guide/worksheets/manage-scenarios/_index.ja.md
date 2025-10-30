---
title: Node.jsを使ってワークシートからシナリオを作成、操作、削除する（C++経由）
linktitle: シナリオの管理
type: docs
weight: 190
url: /ja/nodejs-cpp/create-manipulate-or-remove-scenarios-from-worksheets/
description: Node.jsとC++ APIを使用してExcelワークシートからシナリオをプログラム的に作成、操作、削除する方法を学びます。
keywords: Node.js経由のシナリオ作成（C++）、Excelワークシートからシナリオを削除（Node.js+C++）、シナリオを操作（Node.js+C++）
---

{{% alert color="primary" %}}

時折、スプレッドシートでシナリオを作成、操作、または削除する必要があります。シナリオとは、1つ以上の数式によってリンクされた可変の入力セルを含む名前付きの'仮定'モデルです。シナリオを作成する前に、異なる値が挿入できるセルに依存する1つ以上の数式を含むワークシートの設計を行います。以下の例は、Aspose.CellsのAPIを使用してワークシートからシナリオを作成および削除する方法を示しています。

{{% /alert %}}

Aspose.Cellsには、例えば、[**ScenarioCollection**](https://reference.aspose.com/cells/nodejs-cpp/scenariocollection)、[**Scenario**](https://reference.aspose.com/cells/nodejs-cpp/scenario)、[**ScenarioInputCellCollection**](https://reference.aspose.com/cells/nodejs-cpp/scenarioinputcellcollection)、および[**ScenarioInputCell**](https://reference.aspose.com/cells/nodejs-cpp/scenarioinputcell)のクラスなど、いくつかの便利なクラスが提供されています。また、[**Worksheet.getScenarios()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getScenarios--)プロパティも提供されています。以下のサンプルコードは、いくつかのシナリオを含むXLSX形式のExcelファイルを開き、既存のシナリオを削除し、Excelファイルを保存する前にワークシートに新しいシナリオを追加します。この例では、シナリオを含む非常にシンプルなテンプレートファイルが使用されています。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Instantiate the Workbook
// Load an Excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "aspose-sample.xlsx"));
// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

if (worksheet.getScenarios().getCount() > 0) {
// Remove the existing first scenario from the sheet
worksheet.getScenarios().removeAt(0);

// Create a scenario
const i = worksheet.getScenarios().add("MyScenario");
// Get the scenario
const scenario = worksheet.getScenarios().get(i);
// Add comment to it
scenario.setComment("Test scenario is created.");
// Get the input cells for the scenario
const sic = scenario.getInputCells();
// Add the scenario on B4 (as changing cell) with default value
sic.add(3, 1, "1100000");

const outputFilePath = path.join(dataDir, "outBk_scenarios1.out.xlsx");

// Save the Excel file.
workbook.save(outputFilePath);
console.log("\nProcess completed successfully.\nFile saved at " + outputFilePath);
}
```
{{< app/cells/assistant language="nodejs-cpp" >}}
