---
title: Aspose.Cells for .NET でピボットテーブルの行フィールドと列フィールドを追加する
linktitle: Aspose.Cells for .NET でピボットテーブルの行フィールドと列フィールドを追加する
description: Aspose.Cells for .NET でピボットテーブルに行フィールドと列フィールドを追加し、PivotField.SetSubtotals と PivotFieldSubtotalType を使用してピボットフィールドの小計を制御する方法を学びます。
keywords: Aspose.Cells, .NET, ピボットテーブル, 行フィールド, 列フィールド, PivotField, SetSubtotals, PivotFieldSubtotalType, 小計, C#, Excel ピボットテーブル
type: docs
weight: 220
url: /ja/net/pivot-table-add-row-and-column-fields/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Adding a Field to the Row or Column Region**
`PivotTable.AddFieldToArea(PivotFieldType fieldType, string fieldName)` メソッドは、ソースデータから基本フィールドを 4 つのピボット領域のいずれかに移動します。`fieldType` 引数は、次の `PivotFieldType` 値のいずれかを受け入れます。
- `Row` — 左側に縦方向に配置されるフィールド
- `Column` — 上部に横方向に配置されるフィールド
- `Data` — 値が集計されるフィールド
- `Page` — レポートフィルターとして使用されるフィールド
フィールドのネスト順序は重要です。最初に `Category` を行領域に追加し、次に `Item` を追加すると、外側のグループ化が `Category`、内側のグループ化が `Item` となるピボットが生成されます。順序を逆順にすると階層が逆になります。

## **Pivot Field Subtotals**
`PivotField.SetSubtotals(PivotFieldSubtotalType subtotalType, bool shown)` メソッドは、ピボットフィールドに表示される小計行を制御します。各呼び出しは、1 つの小計タイプのみを個別に切り替えます。`shown = true` を渡すと小計が表示され、`shown = false` を渡すと非表示になります。各呼び出しは 1 つのタイプにのみ影響を与えるため、異なる `subtotalType` 値でメソッドを複数回呼び出すことで、小計のカスタムサブセットを構築できます。
`PivotFieldSubtotalType` 列挙型は、利用可能な小計の種類を定義します。
- `Automatic` — Aspose.Cells がデフォルトの選択（通常は数値フィールドの場合は `Sum`）を行う
- `None` — すべての小計行を抑制する
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
小計は、行領域（または列領域）に 2 つ以上のピボットフィールドがある場合にのみレンダリングされます。フィールドが 1 つしかない場合は小計を計算する意味がないため、その場合 `SetSubtotals` 呼び出しは視覚的な効果を持ちません。したがって、この記事では、すべての例で 2 つの行フィールド（外側 `Category`、内側 `Item`）を配置し、各 `Category` グループ間の小計境界が見えるようにしています。
{{% /alert %}}

## **Scenario 1 — Automatic (Default) Subtotals**
`SetSubtotals` をまったく呼び出さない場合、Aspose.Cells は数値フィールドに `Automatic` 選択を適用します。次の例では、外側の `Category` 行フィールドに対して `SetSubtotals(PivotFieldSubtotalType.Automatic, true)` を呼び出すことで、この動作を明示的に確認しています。

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
worksheet.Name = "Data";
worksheet.Cells[0, 0].PutValue("Category");
worksheet.Cells[0, 1].PutValue("Item");
worksheet.Cells[0, 2].PutValue("Year");
worksheet.Cells[0, 3].PutValue("Amount");
worksheet.Cells[1, 0].PutValue("Fruit");
worksheet.Cells[1, 1].PutValue("Apple");
worksheet.Cells[1, 2].PutValue(2020);
worksheet.Cells[1, 3].PutValue(100);
worksheet.Cells[2, 0].PutValue("Fruit");
worksheet.Cells[2, 1].PutValue("Apple");
worksheet.Cells[2, 2].PutValue(2021);
worksheet.Cells[2, 3].PutValue(150);
worksheet.Cells[3, 0].PutValue("Fruit");
worksheet.Cells[3, 1].PutValue("Banana");
worksheet.Cells[3, 2].PutValue(2020);
worksheet.Cells[3, 3].PutValue(80);
worksheet.Cells[4, 0].PutValue("Fruit");
worksheet.Cells[4, 1].PutValue("Banana");
worksheet.Cells[4, 2].PutValue(2021);
worksheet.Cells[4, 3].PutValue(90);
worksheet.Cells[5, 0].PutValue("Vegetable");
worksheet.Cells[5, 1].PutValue("Carrot");
worksheet.Cells[5, 2].PutValue(2020);
worksheet.Cells[5, 3].PutValue(50);
worksheet.Cells[6, 0].PutValue("Vegetable");
worksheet.Cells[6, 1].PutValue("Carrot");
worksheet.Cells[6, 2].PutValue(2021);
worksheet.Cells[6, 3].PutValue(60);
worksheet.Cells[7, 0].PutValue("Vegetable");
worksheet.Cells[7, 1].PutValue("Daikon");
worksheet.Cells[7, 2].PutValue(2020);
worksheet.Cells[7, 3].PutValue(40);
worksheet.Cells[8, 0].PutValue("Vegetable");
worksheet.Cells[8, 1].PutValue("Daikon");
worksheet.Cells[8, 2].PutValue(2021);
worksheet.Cells[8, 3].PutValue(45);
int pivotIndex = worksheet.PivotTables.Add("A1:D9", "F3", "PivotTable1");
PivotTable pivotTable = worksheet.PivotTables[pivotIndex];
pivotTable.AddFieldToArea(PivotFieldType.Row, "Category");
pivotTable.AddFieldToArea(PivotFieldType.Row, "Item");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
PivotField categoryField = pivotTable.RowFields[0];
categoryField.SetSubtotals(PivotFieldSubtotalType.Automatic, true);
pivotTable.CalculateData();
workbook.Save("output_automatic.xlsx");
```

## **Scenario 2 — Suppressing All Subtotals (None)**
`SetSubtotals(PivotFieldSubtotalType.None, true)` を呼び出すと、ピボットからすべての小計行が削除され、フィールド行と最下部の総計のみが残ります。これは、集計行のない生のグループ化されたデータを必要とする場合に便利です。

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
worksheet.Name = "Data";
string[] headers = { "Category", "Item", "Year", "Amount" };
for (int j = 0; j < headers.Length; j++)
{
    worksheet.Cells[0, j].PutValue(headers[j]);
}
object[,] data = {
    { "Fruit",     "Apple",  2020, 100 },
    { "Fruit",     "Apple",  2021, 150 },
    { "Fruit",     "Banana", 2020, 80  },
    { "Fruit",     "Banana", 2021, 90  },
    { "Vegetable", "Carrot", 2020, 50  },
    { "Vegetable", "Carrot", 2021, 60  },
    { "Vegetable", "Daikon", 2020, 40  },
    { "Vegetable", "Daikon", 2021, 45  }
};
for (int i = 0; i < data.GetLength(0); i++)
{
    for (int j = 0; j < data.GetLength(1); j++)
    {
        worksheet.Cells[i + 1, j].PutValue(data[i, j]);
    }
}
int pivotIndex = worksheet.PivotTables.Add("A1:D9", "F3", "PivotTable1");
PivotTable pivotTable = worksheet.PivotTables[pivotIndex];
pivotTable.AddFieldToArea(PivotFieldType.Row, "Category");
pivotTable.AddFieldToArea(PivotFieldType.Row, "Item");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
PivotField categoryField = pivotTable.RowFields[0];
categoryField.SetSubtotals(PivotFieldSubtotalType.None, true);
pivotTable.CalculateData();
workbook.Save("output_none.xlsx");
```

## **Scenario 3 — Custom Subtotal Subset (Sum + Average)**
1 つの小計タイプに限定されません。各 `SetSubtotals` 呼び出しは 1 つのタイプに対して独立して動作するため、メソッドを 2 回呼び出す（`Sum` で 1 回、`Average` で 1 回）ことで、各 `Category` グループの 2 つの小計行のカスタムサブセットが生成されます。

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
worksheet.Name = "Data";
worksheet.Cells["A1"].PutValue("Category");
worksheet.Cells["B1"].PutValue("Item");
worksheet.Cells["C1"].PutValue("Year");
worksheet.Cells["D1"].PutValue("Amount");
worksheet.Cells[1, 0].PutValue("Fruit");
worksheet.Cells[1, 1].PutValue("Apple");
worksheet.Cells[1, 2].PutValue(2020);
worksheet.Cells[1, 3].PutValue(100);
worksheet.Cells[2, 0].PutValue("Fruit");
worksheet.Cells[2, 1].PutValue("Apple");
worksheet.Cells[2, 2].PutValue(2021);
worksheet.Cells[2, 3].PutValue(150);
worksheet.Cells[3, 0].PutValue("Fruit");
worksheet.Cells[3, 1].PutValue("Banana");
worksheet.Cells[3, 2].PutValue(2020);
worksheet.Cells[3, 3].PutValue(80);
worksheet.Cells[4, 0].PutValue("Fruit");
worksheet.Cells[4, 1].PutValue("Banana");
worksheet.Cells[4, 2].PutValue(2021);
worksheet.Cells[4, 3].PutValue(90);
worksheet.Cells[5, 0].PutValue("Vegetable");
worksheet.Cells[5, 1].PutValue("Carrot");
worksheet.Cells[5, 2].PutValue(2020);
worksheet.Cells[5, 3].PutValue(50);
worksheet.Cells[6, 0].PutValue("Vegetable");
worksheet.Cells[6, 1].PutValue("Carrot");
worksheet.Cells[6, 2].PutValue(2021);
worksheet.Cells[6, 3].PutValue(60);
worksheet.Cells[7, 0].PutValue("Vegetable");
worksheet.Cells[7, 1].PutValue("Daikon");
worksheet.Cells[7, 2].PutValue(2020);
worksheet.Cells[7, 3].PutValue(40);
worksheet.Cells[8, 0].PutValue("Vegetable");
worksheet.Cells[8, 1].PutValue("Daikon");
worksheet.Cells[8, 2].PutValue(2021);
worksheet.Cells[8, 3].PutValue(45);
PivotTableCollection pivotTables = worksheet.PivotTables;
int pivotIndex = pivotTables.Add("A1:D9", "F3", "PivotTable1");
PivotTable pivotTable = pivotTables[pivotIndex];
pivotTable.AddFieldToArea(PivotFieldType.Row, "Category");
pivotTable.AddFieldToArea(PivotFieldType.Row, "Item");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
PivotField categoryField = pivotTable.RowFields[0];
categoryField.SetSubtotals(PivotFieldSubtotalType.Sum, true);
categoryField.SetSubtotals(PivotFieldSubtotalType.Average, true);
pivotTable.CalculateData();
workbook.Save("output_custom.xlsx");
```

## **Recap**

## **Related Articles**
- [ピボットテーブルのページフィールド](/cells/ja/net/add-page-field-in-pivot-table/)
- [Aspose.Cells for .NET でピボットテーブルを更新する](/cells/ja/net/refresh-pivot-table/)
- [ピボットテーブルにスタイルを適用する](/cells/ja/net/apply-style-to-pivot-table/)

{{< app/cells/assistant language="csharp" >}}