---
title: Aspose.Cells for .NET でピボットテーブルの行フィールドと列フィールドを追加する
linktitle: 行フィールドと列フィールド
description: Learn how to add base fields to the row and column regions of a pivot table and control pivot field subtotals using PivotField.setSubtotals in Aspose.Cells for Node.js via Java
keywords: Aspose.Cells, Node.js, Java, pivot table, row field, column field, PivotField, setSubtotals, PivotFieldSubtotalType, subtotals
type: docs
weight: 220
url: /ja/nodejs-java/pivot-table-add-row-column-fields/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **行領域または列領域へのフィールドの追加**

`PivotTable.addFieldToArea(PivotFieldType fieldType, String fieldName)` メソッドは、ソースデータからベースフィールドを 4 つのピボット領域のいずれかに移動します。`fieldType` 引数は次の `PivotFieldType` 値のいずれかを受け付けます。

- `ROW` — 左側に垂直に配置されるフィールド
- `COLUMN` — 上部に水平に配置されるフィールド
- `DATA` — 値が集計されるフィールド
- `PAGE` — レポートフィルタとして使用されるフィールド

フィールドを追加した後、`PivotTable.getRowFields()` プロパティと `PivotTable.getColumnFields()` プロパティを通じてアクセスできます。各プロパティは `PivotFieldCollection` を返します。`RowFields` のインデックス 0 のフィールドが最外部の行フィールドであり、後続のインデックスはその内側にネストされたフィールドを表します。同じインデックス規約が `ColumnFields` にも適用されます。

フィールドのネスト順序は重要です。最初に `Category` を行領域に追加し、次に `Item` を追加すると、外側のグループ化が `Category` で内側のグループ化が `Item` になるピボットが作成されます。順序を逆にすると階層も逆になります。

## **ピボットフィールドの小計**

`PivotField.setSubtotals(PivotFieldSubtotalType subtotalType, boolean shown)` メソッドは、ピボットフィールドに表示される小計行を制御します。各呼び出しは 1 つの小計タイプを独立して切り替えます。`shown = true` を渡すと小計が表示され、`shown = false` を渡すと非表示になります。各呼び出しは 1 つのタイプにのみ影響するため、異なる `subtotalType` 値で複数回メソッドを呼び出すことで、小計のカスタムサブセットを構築できます。

`PivotFieldSubtotalType` 列挙型は利用可能な小計の種類を定義します。

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
小計は、行領域（または列領域）に 2 つ以上のピボットフィールドがある場合にのみ表示されます。単一のフィールドでは意味のある小計を計算する対象がないため、その場合は `setSubtotals` の呼び出しは目に見える効果を持ちません。したがって、この記事では、各 `Category` グループ間の小計の境界が見えるように、すべての例で 2 つの行フィールド（外側が `Category`、内側が `Item`）を配置しています。
{{% /alert %}}

## **シナリオ 1 — 自動（デフォルト）の小計**

`setSubtotals` をまったく呼び出さない場合、Aspose.Cells は数値フィールドに `AUTOMATIC` 選択を適用します。次の例は、外側の `Category` 行フィールドに対して `setSubtotals(PivotFieldSubtotalType.AUTOMATIC, true)` を呼び出すことで、この動作を明示的に確認します。

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

`setSubtotals(PivotFieldSubtotalType.NONE, true)` を呼び出すと、ピボットからすべての小計行が削除され、フィールド行と最下部の総計のみが残ります。これは、集計行なしで生のグループ化されたデータが必要な場合に便利です。

```javascript
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

pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Category");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Item");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

let categoryField = pivotTable.getRowFields().get(0);
categoryField.setSubtotals(AsposeCells.PivotFieldSubtotalType.None, true);
pivotTable.calculateData();

workbook.save("output_none.xlsx");
```

## **シナリオ 3 — カスタム小計サブセット（Sum + Average）**

1 つの小計タイプに限定されません。各 `setSubtotals` 呼び出しは 1 つのタイプに対して独立して動作するため、`SUM` で 1 回、`AVERAGE` で 1 回と 2 回メソッドを呼び出すことで、各 `Category` グループに対して 2 つの小計行のカスタムサブセットが生成されます。

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

上記の 3 つのシナリオは、同じデータセットとピボットテーブル構造を共有しています。它们的唯一区别在于应用于外部 `Category` 行字段的 `setSubtotals` 调用。2 つのフィールドのルールを覚えておいてください。領域に単一のフィールドがある場合、小計を計算する対象がないため、`setSubtotals` が目に見える効果を持つようにするには、常に行領域または列領域に少なくとも 2 つのフィールドを配置してください。

## **関連記事**

- [ピボットテーブルのページフィールド](/cells/ja/nodejs-java/add-page-field-in-pivot-table/)
- [Aspose.Cells for Node.js via Java でのピボットテーブルの更新](/cells/ja/nodejs-java/refresh-pivot-table/)
- [ピボットテーブルへのスタイルの適用](/cells/ja/nodejs-java/apply-style-to-pivot-table/)

{{< app/cells/assistant language="csharp" >}}
