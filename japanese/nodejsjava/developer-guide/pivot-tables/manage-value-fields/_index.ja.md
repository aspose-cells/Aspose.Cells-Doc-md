---
title: Aspose.Cells for Node.js via Java における値フィールド
linktitle: Aspose.Cells for Node.js via Java における値フィールド
description: Aspose.Cells for Node.js via Java における、ピボットテーブルのデータ領域へのベースフィールドの追加、PivotField.Function による集計関数の変更、行または列の軸への値フィールドのプロット方法について学びます。
keywords: Aspose.Cells, Node.js via Java, ピボットテーブル, 値フィールド, PivotField, PivotField.Function, データフィールド, PivotTable.ValuesField, 合計, 平均
type: docs
weight: 230
url: /ja/nodejs-java/manage-value-fields/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

値フィールドは、すべてのピボットテーブルの中核をなす存在であり、ソースデータを集計する数値的な集計値です。Aspose.Cells for Node.js via Java では、`PivotTable.addFieldToArea` を使ってベースフィールドを追加することでピボットテーブルのデータ領域が構成され、その領域に配置された各フィールドは独自の集計関数を持つことができます。2 つ以上のデータフィールドが存在する場合、Aspose.Cells は特別な集計フィールド `PivotTable.getValuesField()` を公開し、これをベースフィールドとして行または列の軸にプロットすることで、レイアウト内での値フィールドの表示方法をより細かく制御できます。
## データ領域へのフィールドの追加
ベースフィールドをデータ（値）領域に追加することは、ピボットテーブルがソースデータを集計する方法を形作るための最初のステップです。Aspose.Cells は `PivotTable.addFieldToArea(PivotFieldType, string)` を提供しており、定数 `PivotFieldType.DATA` とソース列名を受け取るオーバーロードになっています。フィールドがデータ領域に追加されると、API はそのフィールドを `PivotTable.getDataFields()` コレクションに追加順に公開します。デフォルトでは、数値型のソース列は `ConsolidationFunction.SUM` で集計され、非数値型の列は `COUNT` が既定値となります。

```javascript
const AsposeCells = require("aspose.cells");

const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Data");

const headers = ["Category", "Item", "Year", "Amount"];
for (let j = 0; j < headers.length; j++) {
    worksheet.getCells().get(0, j).putValue(headers[j]);
}

const data = [
    ["Fruit",     "Apple",  2020, 100],
    ["Fruit",     "Apple",  2021, 150],
    ["Fruit",     "Banana", 2020,  80],
    ["Fruit",     "Banana", 2021,  90],
    ["Vegetable", "Carrot", 2020,  50],
    ["Vegetable", "Carrot", 2021,  60],
    ["Vegetable", "Daikon", 2020,  40],
    ["Vegetable", "Daikon", 2021,  45]
];
for (let i = 0; i < data.length; i++) {
    for (let j = 0; j < data[i].length; j++) {
        worksheet.getCells().get(i + 1, j).putValue(data[i][j]);
    }
}

const pivotIndex = worksheet.getPivotTables().add("A1:D9", "F3", "PivotTable1");
const pivotTable = worksheet.getPivotTables().get(pivotIndex);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Category");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Item");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

pivotTable.calculateData();
workbook.save("output_drag.xlsx");
```

## 集計関数の変更
データ領域に配置された各フィールドは内部的に `PivotField` インスタンスとしてラップされており、その `getFunction()` プロパティは `ConsolidationFunction` 列挙体の値を返します。同じ `setFunction()` セッターを使用すると、利用可能な集計関数（`SUM`、`COUNT`、`AVERAGE`、`MAX`、`MIN`、`PRODUCT`、`STD_DEV`、`STD_DEVP`、`VAR`、`VARP` など）を切り替えることができます。
{{% alert color="primary" %}}
`Function` を変更しても影響するのは集計のみであり、ソース列は変更されません。
{{% /alert %}}
したがって、一方のデータフィールドを `SUM` のままにして、同じソース列を対象とするものの `COUNT` や `AVERAGE` を使用する 2 つ目のデータフィールドを、1 つのピボット内で追加することができます。

```javascript
const AsposeCells = require("aspose.cells");

const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Data");

const headers = ["Category", "Item", "Year", "Amount"];
for (let j = 0; j < headers.length; j++) {
    worksheet.getCells().get(0, j).putValue(headers[j]);
}

const data = [
    ["Fruit",     "Apple",  2020, 100],
    ["Fruit",     "Apple",  2021, 150],
    ["Fruit",     "Banana", 2020,  80],
    ["Fruit",     "Banana", 2021,  90],
    ["Vegetable", "Carrot", 2020,  50],
    ["Vegetable", "Carrot", 2021,  60],
    ["Vegetable", "Daikon", 2020,  40],
    ["Vegetable", "Daikon", 2021,  45]
];
for (let i = 0; i < data.length; i++) {
    for (let j = 0; j < data[i].length; j++) {
        worksheet.getCells().get(i + 1, j).putValue(data[i][j]);
    }
}

const pivotIndex = worksheet.getPivotTables().add("A1:D9", "F3", "PivotTable1");
const pivotTable = worksheet.getPivotTables().get(pivotIndex);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Category");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Item");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.getDataFields().get(1).setFunction(AsposeCells.ConsolidationFunction.Count);

pivotTable.calculateData();
workbook.save("output_function.xlsx");
```

## 行または列の軸への値フィールドのプロット
ピボットテーブルに 2 つ以上のデータフィールドが含まれる場合、Aspose.Cells は `PivotTable.getValuesField()` という追加の仮想フィールドを公開します。この仮想フィールドは、データ領域に存在するすべてのデータフィールドの集計を表します。ベースピボットフィールドとして行領域または列領域にドラッグすることができ、複数のメジャーを並べて配置する場合に便利です。
{{% alert color="primary" %}}
`PivotTable.getValuesField()` は、値フィールドが 0 個または 1 個しかない場合は機能しません。
{{% /alert %}}
以下のシナリオでは、上記の各機能を同じピボット構造に対して段階的に示す 3 つのエンドツーエンドの例を紹介します。

```javascript
const AsposeCells = require("aspose.cells");

const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Data");

const headers = ["Category", "Item", "Year", "Amount"];
for (let j = 0; j < headers.length; j++) {
    worksheet.getCells().get(0, j).putValue(headers[j]);
}

const data = [
    ["Fruit",     "Apple",  2020, 100],
    ["Fruit",     "Apple",  2021, 150],
    ["Fruit",     "Banana", 2020,  80],
    ["Fruit",     "Banana", 2021,  90],
    ["Vegetable", "Carrot", 2020,  50],
    ["Vegetable", "Carrot", 2021,  60],
    ["Vegetable", "Daikon", 2020,  40],
    ["Vegetable", "Daikon", 2021,  45]
];
for (let i = 0; i < data.length; i++) {
    for (let j = 0; j < data[i].length; j++) {
        worksheet.getCells().get(i + 1, j).putValue(data[i][j]);
    }
}

const pivotIndex = worksheet.getPivotTables().add("A1:D9", "F3", "PivotTable1");
const pivotTable = worksheet.getPivotTables().get(pivotIndex);
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

{{< app/cells/assistant language="javascript" >}}