---
title: Aspose.Cells for Node.js via C++ でピボットテーブルの行フィールドと列フィールドを追加する
linktitle: 行フィールドと列フィールド
description: Learn how to add base fields to the row and column regions of a pivot table and control pivot field subtotals using PivotField.SetSubtotals in Aspose.Cells for Node.js via C++
keywords: Aspose.Cells, Node.js, C++, pivot table, row field, column field, PivotField, SetSubtotals, PivotFieldSubtotalType, subtotals
type: docs
weight: 220
url: /ja/nodejs-cpp/pivot-table-add-row-and-column-fields/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **行領域または列領域へのフィールドの追加**

`PivotTable.AddFieldToArea(PivotFieldType fieldType, string fieldName)` メソッドは、ソースデータのベースフィールドを 4 つのピボット領域のいずれかに移動します。`fieldType` 引数は、次の `PivotFieldType` 値のいずれかを受け入れます。

- `Row` — 左側に縦方向に配置されるフィールド
- `Column` — 上部に横方向に配置されるフィールド
- `Data` — 値が集計されるフィールド
- `Page` — レポートフィルターとして使用されるフィールド

フィールドを追加した後は、`PivotTable.RowFields` プロパティと `PivotTable.ColumnFields` プロパティを介してアクセスできます。各プロパティは `PivotFieldCollection` を返します。`RowFields` のインデックス 0 のフィールドは最も外側の行フィールドであり、以降のインデックスはその内側にネストされているフィールドを表します。同じインデックスの規則が `ColumnFields` にも適用されます。

フィールドのネスト順序は重要です。最初に `Category` を行領域に追加し、次に `Item` を追加すると、外側のグループが `Category` で内側のグループが `Item` となるピボットが生成されます。順序を逆にすると階層も逆になります。

## **ピボットフィールドの小計**

`PivotField.SetSubtotals(PivotFieldSubtotalType subtotalType, bool shown)` メソッドは、ピボットフィールドに表示される小計行を制御します。各呼び出しは、単一の小計タイプのみを独立して切り替えます。`shown = true` を渡すと小計が表示され、`shown = false` を渡すと非表示になります。各呼び出しは 1 つのタイプにのみ影響を与えるため、異なる `subtotalType` 値でメソッドを複数回呼び出すことで、小計のカスタムサブセットを構築できます。

`PivotFieldSubtotalType` 列挙型は、利用可能な小計の種類を定義します。

- `Automatic` — Aspose.Cells がデフォルトの選択（通常、数値フィールドでは `Sum`）を適用します
- `None` — すべての小計行を抑制します
- `Sum`
- `Count`
- `Average`
- `Max`
- `Min`
- `Product`
- `StdDev`
- `StdDevp`
- `Var`
- `Varp`

{{% alert color="primary" %}}
小計は、行領域（または列領域）に 2 つ以上のピボットフィールドがある場合にのみ表示されます。単一のフィールドではその間に集計する対象がないため、そのケースでは `SetSubtotals` の呼び出しは目に見える効果を持ちません。したがって、この記事ではすべての例で 2 つの行フィールド（外側 `Category`、内側 `Item`）を配置し、各 `Category` グループ間の小計の境界が見えるようにしています。
{{% /alert %}}

## **シナリオ 1 — 自動（デフォルト）の小計**

`SetSubtotals` を一度も呼び出さない場合、Aspose.Cells は数値フィールドに対して `Automatic` 選択を適用します。次の例では、外側の `Category` 行フィールドで `SetSubtotals(PivotFieldSubtotalType.Automatic, true)` を呼び出すことで、この動作を明示的に確認しています。

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Data");

worksheet.getCells().get(0, 0).putValue("Category");
worksheet.getCells().get(0, 1).putValue("Item");
worksheet.getCells().get(0, 2).putValue("Year");
worksheet.getCells().get(0, 3).putValue("Amount");

worksheet.getCells().get(1, 0).putValue("Fruit");
worksheet.getCells().get(1, 1).putValue("Apple");
worksheet.getCells().get(1, 2).putValue(2020);
worksheet.getCells().get(1, 3).putValue(100);

worksheet.getCells().get(2, 0).putValue("Fruit");
worksheet.getCells().get(2, 1).putValue("Apple");
worksheet.getCells().get(2, 2).putValue(2021);
worksheet.getCells().get(2, 3).putValue(150);

worksheet.getCells().get(3, 0).putValue("Fruit");
worksheet.getCells().get(3, 1).putValue("Banana");
worksheet.getCells().get(3, 2).putValue(2020);
worksheet.getCells().get(3, 3).putValue(80);

worksheet.getCells().get(4, 0).putValue("Fruit");
worksheet.getCells().get(4, 1).putValue("Banana");
worksheet.getCells().get(4, 2).putValue(2021);
worksheet.getCells().get(4, 3).putValue(90);

worksheet.getCells().get(5, 0).putValue("Vegetable");
worksheet.getCells().get(5, 1).putValue("Carrot");
worksheet.getCells().get(5, 2).putValue(2020);
worksheet.getCells().get(5, 3).putValue(50);

worksheet.getCells().get(6, 0).putValue("Vegetable");
worksheet.getCells().get(6, 1).putValue("Carrot");
worksheet.getCells().get(6, 2).putValue(2021);
worksheet.getCells().get(6, 3).putValue(60);

worksheet.getCells().get(7, 0).putValue("Vegetable");
worksheet.getCells().get(7, 1).putValue("Daikon");
worksheet.getCells().get(7, 2).putValue(2020);
worksheet.getCells().get(7, 3).putValue(40);

worksheet.getCells().get(8, 0).putValue("Vegetable");
worksheet.getCells().get(8, 1).putValue("Daikon");
worksheet.getCells().get(8, 2).putValue(2021);
worksheet.getCells().get(8, 3).putValue(45);

let pivotIndex = worksheet.getPivotTables().add("A1:D9", "F3", "PivotTable1");
let pivotTable = worksheet.getPivotTables().get(pivotIndex);

pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Category");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Item");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

let categoryField = pivotTable.getRowFields().get(0);
categoryField.setSubtotals(AsposeCells.PivotFieldSubtotalType.Automatic, true);

pivotTable.calculateData();

workbook.save("output_automatic.xlsx");
```

## **シナリオ 2 — すべての小計の抑制（None）**

`SetSubtotals(PivotFieldSubtotalType.None, true)` を呼び出すと、ピボットからすべての小計行が削除され、フィールド行と下部の総計だけが残ります。これは、集計行のない生のグループ化データだけを扱いたい場合に便利です。

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
    ["Fruit",     "Banana", 2020, 80],
    ["Fruit",     "Banana", 2021, 90],
    ["Vegetable", "Carrot", 2020, 50],
    ["Vegetable", "Carrot", 2021, 60],
    ["Vegetable", "Daikon", 2020, 40],
    ["Vegetable", "Daikon", 2021, 45]
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

const categoryField = pivotTable.getRowFields().get(0);
categoryField.setSubtotals(AsposeCells.PivotFieldSubtotalType.None, true);
pivotTable.calculateData();

workbook.save("output_none.xlsx");
```

## **シナリオ 3 — カスタム小計サブセット（Sum + Average）**

単一の小計タイプに限定されるわけではありません。各 `SetSubtotals` 呼び出しは 1 つのタイプに対して独立して動作するため、`Sum` で 1 回、`Average` で 1 回とメソッドを 2 回呼び出すことで、各 `Category` グループに対して 2 行の小計（カスタムサブセット）が生成されます。

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Data");

worksheet.getCells().get("A1").putValue("Category");
worksheet.getCells().get("B1").putValue("Item");
worksheet.getCells().get("C1").putValue("Year");
worksheet.getCells().get("D1").putValue("Amount");

worksheet.getCells().get(1, 0).putValue("Fruit");
worksheet.getCells().get(1, 1).putValue("Apple");
worksheet.getCells().get(1, 2).putValue(2020);
worksheet.getCells().get(1, 3).putValue(100);

worksheet.getCells().get(2, 0).putValue("Fruit");
worksheet.getCells().get(2, 1).putValue("Apple");
worksheet.getCells().get(2, 2).putValue(2021);
worksheet.getCells().get(2, 3).putValue(150);

worksheet.getCells().get(3, 0).putValue("Fruit");
worksheet.getCells().get(3, 1).putValue("Banana");
worksheet.getCells().get(3, 2).putValue(2020);
worksheet.getCells().get(3, 3).putValue(80);

worksheet.getCells().get(4, 0).putValue("Fruit");
worksheet.getCells().get(4, 1).putValue("Banana");
worksheet.getCells().get(4, 2).putValue(2021);
worksheet.getCells().get(4, 3).putValue(90);

worksheet.getCells().get(5, 0).putValue("Vegetable");
worksheet.getCells().get(5, 1).putValue("Carrot");
worksheet.getCells().get(5, 2).putValue(2020);
worksheet.getCells().get(5, 3).putValue(50);

worksheet.getCells().get(6, 0).putValue("Vegetable");
worksheet.getCells().get(6, 1).putValue("Carrot");
worksheet.getCells().get(6, 2).putValue(2021);
worksheet.getCells().get(6, 3).putValue(60);

worksheet.getCells().get(7, 0).putValue("Vegetable");
worksheet.getCells().get(7, 1).putValue("Daikon");
worksheet.getCells().get(7, 2).putValue(2020);
worksheet.getCells().get(7, 3).putValue(40);

worksheet.getCells().get(8, 0).putValue("Vegetable");
worksheet.getCells().get(8, 1).putValue("Daikon");
worksheet.getCells().get(8, 2).putValue(2021);
worksheet.getCells().get(8, 3).putValue(45);

let pivotTables = worksheet.getPivotTables();
let pivotIndex = pivotTables.add("A1:D9", "F3", "PivotTable1");
let pivotTable = pivotTables.get(pivotIndex);

pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Category");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Item");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

let categoryField = pivotTable.getRowFields().get(0);
categoryField.setSubtotals(AsposeCells.PivotFieldSubtotalType.Sum, true);
categoryField.setSubtotals(AsposeCells.PivotFieldSubtotalType.Average, true);

pivotTable.calculateData();

workbook.save("output_custom.xlsx");
```
## **まとめ**

上記の 3 つのシナリオは、データセットとピボットテーブルの構造が共通しています。相違点は、外側の `Category` 行フィールドに適用する `SetSubtotals` 呼び出しだけです。「2 フィールドルール」を忘れないでください。領域にフィールドが 1 つしかない場合は小計を挟む対象が存在しないため、`SetSubtotals` の効果を視覚的に確認したいときは、行領域または列領域に必ず 2 つ以上のフィールドを配置してください。

## **関連記事**

- [Page Fields in Pivot Tables](/cells/ja/nodejs-cpp/add-page-field-in-pivot-table/)
- [Refreshing Pivot Tables in Aspose.Cells for Node.js via C++](/cells/ja/nodejs-cpp/refresh-pivot-table/)
- [Applying Styles to Pivot Tables](/cells/ja/nodejs-cpp/apply-style-to-pivot-table/)

{{< app/cells/assistant language="nodejs-cpp" >}}
