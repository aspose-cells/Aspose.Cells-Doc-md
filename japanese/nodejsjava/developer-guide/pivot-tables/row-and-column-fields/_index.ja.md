---
title: Aspose.Cells for Node.js via Java でピボットテーブルの行と列のフィールドを追加する
linktitle: Aspose.Cells for Node.js via Java でピボットテーブルの行と列のフィールドを追加する
description: Aspose.Cells for Node.js via Java で、ピボットテーブルの行および列領域に基本フィールドを追加し、PivotField.setSubtotals を使用してピボットフィールドの小計を制御する方法を学習します。
keywords: Aspose.Cells, Node.js, Java, ピボットテーブル, 行フィールド, 列フィールド, PivotField, setSubtotals, PivotFieldSubtotalType, 小計
type: docs
weight: 220
url: /ja/nodejs-java/pivot-table-add-row-and-column-fields/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Adding a Field to the Row or Column Region**
`PivotTable.addFieldToArea(PivotFieldType fieldType, String fieldName)` メソッドは、ソースデータから基本フィールドを 4 つのピボット領域のいずれかに移動します。`fieldType` 引数には、次の `PivotFieldType` 値のいずれかを指定します。
- `ROW` — 左側に縦に配置されるフィールド
- `COLUMN` — 上部に横に配置されるフィールド
- `DATA` — 値が集計されるフィールド
- `PAGE` — レポートフィルターとして使用されるフィールド
フィールドのネスト順序は重要です。最初に `Category` を行領域に追加し、その後 `Item` を追加すると、外側のグループ化が `Category`、内側のグループ化が `Item` であるピボットが生成されます。順序を逆にした場合、階層も逆になります。

## **Pivot Field Subtotals**
`PivotField.setSubtotals(PivotFieldSubtotalType subtotalType, boolean shown)` メソッドは、ピボットフィールドに表示される小計行を制御します。各呼び出しは、1 つの小計タイプを個別に切り替えます。`shown = true` を渡すと小計が表示され、`shown = false` を渡すと非表示になります。各呼び出しは 1 つのタイプにのみ影響するため、異なる `subtotalType` 値でメソッドを複数回呼び出すことで、小計のカスタムサブセットを構築できます。
`PivotFieldSubtotalType` 列挙型は、利用可能な小計の種類を定義します。
- `AUTOMATIC` — Aspose.Cells がデフォルトの選択を行います（通常は数値フィールドに対して `SUM`）
- `NONE` — すべての小計行を抑制します
- `SUM`
- `COUNT`
- `AVERAGE`
- `MAX`
- `MIN`
- `PRODUCT`
- `STD_DEV`
- `STD_DEVP`
- `VAR`
- `VARP`

{{% alert color="primary" %}}
小計は、行領域（または列領域）に 2 つ以上のピボットフィールドがある場合にのみレンダリングされます。フィールドが 1 つだけの場合、その間で意味のある小計を計算する対象がないため、`setSubtotals` 呼び出しは視覚的な効果を持ちません。したがって、この記事では、各 `Category` グループ間の小計境界が明確に見えるように、すべての例で 2 つの行フィールド（外側が `Category`、内側が `Item`）を使用しています。
{{% /alert %}}

## **Scenario 1 — Automatic (Default) Subtotals**
`setSubtotals` をまったく呼び出さない場合、Aspose.Cells は数値フィールドに対して `AUTOMATIC` の選択を適用します。次の例は、外側の `Category` 行フィールドに対して `setSubtotals(PivotFieldSubtotalType.AUTOMATIC, true)` を呼び出すことで、この動作を明示的に確認します。

```javascript
const AsposeCells = require("aspose.cells");
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
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Category");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Item");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Amount");
let categoryField = pivotTable.getRowFields().get(0);
categoryField.setSubtotals(AsposeCells.PivotFieldSubtotalType.AUTOMATIC, true);
pivotTable.calculateData();
workbook.save("output_automatic.xlsx");
```

## **Scenario 2 — Suppressing All Subtotals (None)**
`setSubtotals(PivotFieldSubtotalType.NONE, true)` を呼び出すと、ピボットからすべての小計行が削除され、フィールド行と最下部の総計のみが残ります。これは、集計行のない生のグループ化データが必要な場合に便利です。

```javascript
const AsposeCells = require("aspose.cells");
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Data");
let headers = ["Category", "Item", "Year", "Amount"];
for (let j = 0; j < headers.length; j++)
{
    worksheet.getCells().get(0, j).putValue(headers[j]);
}
let data = [
    ["Fruit", "Apple", 2020, 100],
    ["Fruit", "Apple", 2021, 150],
    ["Fruit", "Banana", 2020, 80],
    ["Fruit", "Banana", 2021, 90],
    ["Vegetable", "Carrot", 2020, 50],
    ["Vegetable", "Carrot", 2021, 60],
    ["Vegetable", "Daikon", 2020, 40],
    ["Vegetable", "Daikon", 2021, 45]
];
for (let i = 0; i < data.length; i++)
{
    for (let j = 0; j < data[i].length; j++)
    {
        worksheet.getCells().get(i + 1, j).putValue(data[i][j]);
    }
}
let pivotIndex = worksheet.getPivotTables().add("A1:D9", "F3", "PivotTable1");
let pivotTable = worksheet.getPivotTables().get(pivotIndex);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Category");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Item");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Amount");
let categoryField = pivotTable.getRowFields().get(0);
categoryField.setSubtotals(AsposeCells.PivotFieldSubtotalType.NONE, true);
pivotTable.calculateData();
workbook.save("output_none.xlsx");
```

## **Scenario 3 — Custom Subtotal Subset (Sum + Average)**
1 つの小計タイプに限定されません。各 `setSubtotals` 呼び出しは 1 つのタイプに対して独立して動作するため、`SUM` と `AVERAGE` のそれぞれでメソッドを 2 回呼び出すことで、各 `Category` グループに対して 2 つの小計行からなるカスタムサブセットが生成されます。

```javascript
const AsposeCells = require("aspose.cells");
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
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Category");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Item");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Amount");
let categoryField = pivotTable.getRowFields().get(0);
categoryField.setSubtotals(AsposeCells.PivotFieldSubtotalType.SUM, true);
categoryField.setSubtotals(AsposeCells.PivotFieldSubtotalType.AVERAGE, true);
pivotTable.calculateData();
workbook.save("output_custom.xlsx");
```

## **Recap**

这三个场景唯一的不同在于 `setSubtotals` メソッドの呼び出しのみです。その他の点（データセット、フィールド、およびそれらが割り当てられるエリア）はすべて同一であり、これがレイアウトを直接比較可能にする理由です。
- **フィールドの配置**。`PivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, fieldName)` は、ソース列を特定のエリアへ移動させます。同一のエリア内では、このメソッド呼び出しの順序が表示順序となります。そのため、最初の呼び出しが最も外側のグループとして表示されます。 subtotal（小計）を設定するには、同一エリア内に2つ以上のフィールドが必要です。フィールドが1つだけの場合、グループ間には小計を算出する対象が存在しなくなります。
- **シナリオ1 — 自動小計**。`setSubtotals` を呼び出さない場合、小計の設定はExcelに任されます。Excelは数値フィールドに対して独自のデフォルト小計を適用します。一方、`AsposeCells.PivotFieldSubtotalType.AUTOMATIC` を指定して `setSubtotals` を呼び出すと、その選択が明示的に記録され、暗黙的な状態ではなくなります。
- **シナリオ2 — 小計なし**。`AsposeCells.PivotFieldSubtotalType.NONE` を指定して `setSubtotals` を呼び出すと、デフォルトの小計設定が無効になります。これによりピボットテーブルはフィールドの行と合計行を保持しつつ、Excelが本来それらの間に挿入していた小計行を削除します。
- **シナリオ3 — 選択的適用**。各 `setSubtotals` の呼び出しは、正確に1つの小計タイプをトグル（切り替え）します。また、呼び出しは互いに上書きするのではなく蓄積されます。そのため、`AsposeCells.PivotFieldSubtotalType.SUM` で一度、`AsposeCells.PivotFieldSubtotalType.AVERAGE` で一度呼び出すと、両方が有効となり、ピボットテーブルには合計（Sum）小計、平均（Average）小計、および合計行がすべて表示されます。

{{% alert color="primary" %}}
小計に関する設定は、必ずしも行エリアに固有のものではありません。`PivotTable.ColumnFields` から取得したフィールドに対して同様の `setSubtotals` を呼び出すと、列軸上でも同じ3つのレイアウトが生成されます。なぜなら、この設定は軸の種類ではなく、ピボットフィールド自身に属するからです。
{{% /alert %}}
## **Related Articles**
- [ピボットテーブルのページフィールド](/cells/ja/nodejs-java/add-page-field-in-pivot-table/)
- [Aspose.Cells for Node.js via Java でのピボットテーブルの更新](/cells/ja/nodejs-java/refresh-pivot-table/)
- [ピボットテーブルへのスタイルの適用](/cells/ja/nodejs-java/apply-style-to-pivot-table/)

{{< app/cells/assistant language="nodejs-java" >}}