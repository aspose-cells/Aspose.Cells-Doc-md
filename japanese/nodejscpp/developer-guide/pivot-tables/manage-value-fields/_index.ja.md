---
title: Aspose.Cells for Node.js via C++ でピボットテーブルの値フィールドを管理する
linktitle: Aspose.Cells for Node.js via C++ でピボットテーブルの値フィールドを管理する
description: Aspose.Cells for Node.js via C++ で、ピボットテーブルのデータ領域に基本フィールドを追加する方法、PivotField.Function で集計関数を変更する方法、値フィールドを Row または Column 軸にプロットする方法を学習します。
keywords: Aspose.Cells, Node.js via C++, ピボットテーブル, 値フィールド, PivotField, PivotField.Function, データフィールド, PivotTable.ValuesField, Sum, Average
type: docs
weight: 230
url: /ja/nodejs-cpp/manage-value-fields/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## データ領域へのフィールドの追加

基本フィールドをデータ（値）領域に追加することは、ピボットテーブルがソースデータをどのように集計するかを形作る最初のステップです。Aspose.Cells は `PivotTable.addFieldToArea(PivotFieldType, string)` を提供しており、これは定数 `PivotFieldType.Data` とソース列名を受け取るオーバーロードです。フィールドがデータ領域に追加されると、API は `PivotTable.getDataFields()` コレクションを通じてそれを公開し、フィールドが追加された順序で並びます。デフォルトでは、数値ソース列は `ConsolidationFunction.Sum` で集計され、非数値列は `Count` がデフォルトとなります。

## 集計関数の変更

データ領域に配置された各フィールドは内部的に `PivotField` インスタンスとしてラップされ、その `getFunction()` プロパティは `ConsolidationFunction` 列挙型の値を返します。同じ `setFunction()` セッターを使用すると、`Sum`、`Count`、`Average`、`Max`、`Min`、`Product`、`StdDev`、`StdDevp`、`Var`、`Varp` などの利用可能な集計を切り替えることができます。

集計関数の変更は集計結果のみに影響し、ソース列は変更されません。
{{% alert color="primary" %}}
{{% /alert %}}

したがって、1 つのデータフィールドを `Sum` のままにして、同じソース列を対象とするが `Count` または `Average` を使用する 2 つ目のデータフィールドを、単一のピボット内で追加することができます。

## 値フィールドを行または列の軸にプロットする

ピボットテーブルに 2 つ以上のデータフィールドが含まれている場合、Aspose.Cells は `PivotTable.getValuesField` という追加の仮想フィールドを公開します。この仮想フィールドは、データ領域に存在するすべてのデータフィールドの集計を表します。これを基本ピボットフィールドとして行領域または列領域にドラッグでき、複数のメジャーを並べて配置する場合に便利です。

`PivotTable.getValuesField()` は、値フィールドが存在しないか 1 つしかない場合は機能しません。

以下のシナリオでは、上記で説明した各機能を同じピボット構造に対して実証する 3 つのエンドツーエンドの例を順に紹介します。

## シナリオ 1 — 基本フィールドを値領域にドラッグする

このシナリオでは、単一の基本フィールド (`Amount`) を既存のピボットテーブルのデータ領域に配置する方法を示します。共有されるピボット構造は、`Category` と `Item` を行軸に配置し、`Year` を列軸に配置します。操作の後、`Amount` はデータ領域に表示され、デフォルトで `Amount` の `Sum` として計算されます。

```javascript
const AsposeCells = require("aspose.cells");

const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Data");

// A1:D1 のヘッダー
worksheet.getCells().get(0, 0).putValue("Category");
worksheet.getCells().get(0, 1).putValue("Item");
worksheet.getCells().get(0, 2).putValue("Year");
worksheet.getCells().get(0, 3).putValue("Amount");

// A2:D9 のデータ行（j で分岐するネストされたループを使用）
for (let i = 1; i <= 8; i++) {
 for (let j = 0; j < 4; j++) {
 switch (j) {
 case 0:
 worksheet.getCells().get(i, j).putValue(i <= 4 ? "Fruit" : "Vegetable");
 break;
 case 1:
 if (i === 1 || i === 2) worksheet.getCells().get(i, j).putValue("Apple");
 else if (i === 3 || i === 4) worksheet.getCells().get(i, j).putValue("Banana");
 else if (i === 5 || i === 6) worksheet.getCells().get(i, j).putValue("Carrot");
 else worksheet.getCells().get(i, j).putValue("Daikon");
 break;
 case 2:
 worksheet.getCells().get(i, j).putValue(2020 + ((i - 1) % 2));
 break;
 case 3:
 if (i === 1) worksheet.getCells().get(i, j).putValue(100);
 else if (i === 2) worksheet.getCells().get(i, j).putValue(150);
 else if (i === 3) worksheet.getCells().get(i, j).putValue(80);
 else if (i === 4) worksheet.getCells().get(i, j).putValue(90);
 else if (i === 5) worksheet.getCells().get(i, j).putValue(50);
 else if (i === 6) worksheet.getCells().get(i, j).putValue(60);
 else if (i === 7) worksheet.getCells().get(i, j).putValue(40);
 else worksheet.getCells().get(i, j).putValue(45);
 break;
 }
 }
}

// F3 に PivotTable1 という名前のピボットテーブルを追加
const pivotIndex = worksheet.getPivotTables().add("A1:D9", "F3", "PivotTable1");
const pivotTable = worksheet.getPivotTables().get(pivotIndex);

// ピボットレイアウト: 行に Category と Item、列に Year、データフィールドに Amount
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Row, "Category");
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Row, "Item");
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Data, "Amount");

pivotTable.calculateData();
workbook.save("output_drag.xlsx");
```
```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Data");

worksheet.getCells().get(0, 0).putValue("Category");
worksheet.getCells().get(0, 1).putValue("Item");
worksheet.getCells().get(0, 2).putValue("Year");
worksheet.getCells().get(0, 3).putValue("Amount");

for (let i = 1; i <= 8; i++)
{
 for (let j = 0; j <= 3; j++)
 {
 if (j == 0)
 {
 worksheet.getCells().get(i, j).putValue(i <= 5 ? "Fruit" : "Vegetable");
 }
 else if (j == 1)
 {
 let items = ["Apple", "Apple", "Banana", "Banana", "Carrot", "Carrot", "Daikon", "Daikon"];
 worksheet.getCells().get(i, j).putValue(items[i - 1]);
 }
 else if (j == 2)
 {
 let years = [2020, 2021, 2020, 2021, 2020, 2021, 2020, 2021];
 worksheet.getCells().get(i, j).putValue(years[i - 1]);
 }
 else
 {
 let amounts = [100, 150, 80, 90, 50, 60, 40, 45];
 worksheet.getCells().get(i, j).putValue(amounts[i - 1]);
 }
 }
}

let pivotIndex = worksheet.getPivotTables().add("A1:D9", "F3", "PivotTable1");
let pivotTable = worksheet.getPivotTables().get(pivotIndex);

pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Category");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Item");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");

pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

let countField = pivotTable.getDataFields().get(1);
countField.setFunction(AsposeCells.ConsolidationFunction.Count);

pivotTable.calculateData();

workbook.save("output_function.xlsx");
```
```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Data");

worksheet.getCells().get(0, 0).putValue("Category");
worksheet.getCells().get(0, 1).putValue("Item");
worksheet.getCells().get(0, 2).putValue("Year");
worksheet.getCells().get(0, 3).putValue("Amount");

let categories = ["Fruit", "Fruit", "Fruit", "Fruit", "Vegetable", "Vegetable", "Vegetable", "Vegetable"];
let items = ["Apple", "Apple", "Banana", "Banana", "Carrot", "Carrot", "Daikon", "Daikon"];
let years = [2020, 2021, 2020, 2021, 2020, 2021, 2020, 2021];
let amounts = [100, 150, 80, 90, 50, 60, 40, 45];

for (let i = 1; i <= 8; i++)
{
 for (let j = 0; j <= 3; j++)
 {
 if (j == 0) worksheet.getCells().get(i, j).putValue(categories[i - 1]);
 else if (j == 1) worksheet.getCells().get(i, j).putValue(items[i - 1]);
 else if (j == 2) worksheet.getCells().get(i, j).putValue(years[i - 1]);
 else worksheet.getCells().get(i, j).putValue(amounts[i - 1]);
 }
}

let pivotIndex = worksheet.getPivotTables().add("A1:D9", "F3", "PivotTable1");
let pivotTable = worksheet.getPivotTables().get(pivotIndex);

pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Category");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Item");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

pivotTable.getDataFields().get(1).setFunction(AsposeCells.ConsolidationFunction.Count);

pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, pivotTable.getValuesField().getName());

pivotTable.calculateData();
workbook.save("output_plot.xlsx");
```

これらの 3 つのシナリオを合わせると、デフォルトの `Sum` を持つ単一のデータフィールドから、仮想 `ValuesField` が行軸または列軸のレイアウトを制御する複数メジャーのピボットまで、Aspose.Cells for Node.js via C++ における値フィールド操作のすべての側面をカバーしています。

{{< app/cells/assistant language="nodejs-cpp" >}}
