---
title: Aspose.Cells for Node.js via C++でピボットテーブルの行フィールドと列フィールドを追加する
linktitle: Aspose.Cells for Node.js via C++でピボットテーブルの行フィールドと列フィールドを追加する
description: Aspose.Cells for Node.js via C++でピボットテーブルの行領域と列領域に基本フィールドを追加する方法と、PivotField.SetSubtotalsを使用してピボットフィールドの小計を制御する方法を学びます。
keywords: Aspose.Cells, Node.js, C++, ピボットテーブル, 行フィールド, 列フィールド, PivotField, SetSubtotals, PivotFieldSubtotalType, 小計
type: docs
weight: 220
url: /ja/nodejs-cpp/pivot-table-add-row-and-column-fields/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **行領域または列領域へのフィールドの追加**
`PivotTable.AddFieldToArea(PivotFieldType fieldType, string fieldName)` メソッドは、基本フィールドをソースデータからピボットテーブルの4つの領域のいずれかへ移動します。`fieldType` 引数には、次のいずれかの `PivotFieldType` 値を指定できます。
- `Row` — 左側に垂直方向に配置されるフィールド
- `Column` — 上側に水平方向に配置されるフィールド
- `Data` — 値を集計するフィールド
- `Page` — レポートフィルターとして使用するフィールド
フィールドの入れ子順序は重要です。最初に行領域へ `Category` を追加し、その後 `Item` を追加すると、外側のグループが `Category`、内側のグループが `Item` であるピボットが作成されます。順序を逆にすると、階層も逆になります。

## **ピボットフィールドの小計**
`PivotField.setSubtotals(PivotFieldSubtotalType subtotalType, bool shown)` メソッドは、どの小計行を表示するかを制御します。各呼び出しは、1つの小計タイプを独立して切り替えます。`shown = true` を渡すと小計が表示され、`shown = false` を渡すと非表示になります。各呼び出しが1つのタイプだけに影響するため、異なる `subtotalType` 値を指定してこのメソッドを複数回呼び出すと、選択した小計のサブセットを構成できます。
`PivotFieldSubtotalType` 列挙型は、利用可能な小計の種類を定義します。
- `Automatic` — Aspose.Cells が既定の選択を行います（数値フィールドでは通常 `Sum`）
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
小計行は、行領域（または列領域）に2つ以上のピボットフィールドがある場合のみ表示されます。フィールドが1つだけの場合は、小計の算出対象がないため、`setSubtotals` を呼び出しても表示上の効果はありません。そのため、この디자인では、すべての例で2つの行フィールド（外側は `Category`、内側は `Item`）を使用し、各 `Category` グループごとの小計境界が明確になるようにしています。
{{% /alert %}}

## **シナリオ 1 — 自動（デフォルト）の小計**
`setSubtotals` を一度も呼び出さない場合、Aspose.Cells は数値フィールドに `Automatic` の選択を適用します。以下の例では、外側の `Category` 行フィールドに対して `setSubtotals(PivotFieldSubtotalType.Automatic, true)` を明示的に呼び出すことで、この動作を確認します。

```javascript
const AsposeCells = require("aspose.cells.node");
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
`setSubtotals(PivotFieldSubtotalType.None, true)` を呼び出すと、ピボットからすべての小計行が削除され、フィールド行と最下部の総計だけが残ります。これは、集計行を含まず、グループ化されたデータだけを表示したい場合に便利です。

```javascript
const AsposeCells = require("aspose.cells.node");
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

## **シナリオ 3 — カスタム小計のサブセット（Sum + Average）**
小計タイプを1種類に限定する必要はありません。`setSubtotals` の各呼び出しは1つの小計タイプに独立して適用されます。このメソッドを `Sum` と `Average` を指定してそれぞれ1回ずつ呼び出すと、各 `Category` グループ用に、選択した2つの小計行から成るカスタム小計のサブセットが作成されます。

```javascript
const AsposeCells = require("aspose.cells.node");
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

この3つのシナリオの違いは、`setSubtotals`メソッドの呼び出し方のみです。データセット、フィールド、およびそれらが割り当てられるエリアはすべて同一であり、これによりレイアウトを直接比較可能となっています。
- **フィールドの配置**：`PivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, fieldName)` は、ソース列をエリア内に移動します。同じエリア内では、メソッド呼び出しの順序が表示順序となります。そのため、最初の呼び出しが最も外側のグループになります。サブtotalCountを適用するには、同じエリア内に2つ以上のフィールドが必要です。フィールドが1つしかない場合、グループ間にはサブトータルを適用する対象が存在しません。
- **シナリオ1 — 自動サブトータル**：`setSubtotals` を呼び出さない場合、サブトータルの選択はExcelに委ねられ、数値フィールドに対してExcel独自の既定のサブトータルが適用されます。一方、`AsposeCells.PivotFieldSubtotalType.Automatic` を指定して `setSubtotals` を呼び出すと、この選択が明示的に記録されます。
- **シナリオ2 — サブトータルなし**：`AsposeCells.PivotFieldSubtotalType.None` を指定して `setSubtotals` を呼び出すと、既定のサブトータルが無効になります。この場合、ピボットテーブルはフィールド行と総計行は保持しますが、 otherwise Excel がそれらの間に挿入するサブトータル行は削除されます。
- **シナリオ3 — 選択されたサブセット**：各呼び出しは、ちょうど1つのサブトータルタイプを切り替え、かつ呼び出しは累積して他方をリセットしません。そのため、`AsposeCells.PivotFieldSubtotalType.Sum` を1回呼び出し、`AsposeCells.PivotFieldSubtotalType.Average` をもう1回呼び出すと、両方とも有効となり、ピボットテーブルは「合計」のサブトータル、「平均」のサブトータル、および総計がすべて表示されます。

{{% alert color="primary" %}}
サブトータルに関する設定は、行エリアに特有のものではありません。`PivotTable.ColumnFields` から取得したフィールドに対して同じ `setSubtotals` の呼び出しを行うと、列軸上でも同様の3つのレイアウトが生成されます。なぜなら、この設定は軸ではなくピボットフィールド自体に属しているからです。
{{% /alert %}}
## **関連記事**
- [ピボットテーブルのページフィールド](/cells/ja/nodejs-cpp/add-page-field-in-pivot-table/)
- [Aspose.Cells for Node.js via C++でピボットテーブルを更新](/cells/ja/nodejs-cpp/refresh-pivot-table/)
- [ピボットテーブルにスタイルを適用](/cells/ja/nodejs-cpp/apply-style-to-pivot-table/)

{{< app/cells/assistant language="nodejs-cpp" >}}