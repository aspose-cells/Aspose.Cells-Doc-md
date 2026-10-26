---
title: Aspose.Cells for .NET でピボットテーブルの値フィールドを管理する
linktitle: Aspose.Cells for .NET でピボットテーブルの値フィールドを管理する
description: Aspose.Cells for .NET で、ピボットテーブルのデータ領域に基本フィールドを追加する方法、PivotField.Function で集計関数を変更する方法、値フィールドを行軸または列軸に配置する方法を学びます。
keywords: Aspose.Cells, .NET, ピボットテーブル, 値フィールド, PivotField, PivotField.Function, データフィールド, PivotTable.ValuesField, Sum, Average
type: docs
weight: 230
url: /ja/net/manage-value-fields/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## データ領域へのフィールドの追加
データ（値）領域に基本フィールドを追加することは、ピボットテーブルでソースデータを集計する方法を定義する最初の手順です。Aspose.Cells には `PivotTable.AddFieldToArea(PivotFieldType, string)` オーバーロードがあり、定数 `PivotFieldType.Data` とソース列名を受け付けます。フィールドをデータ領域に追加すると、API は `PivotTable.DataFields` コレクションにフィールドを公開し、フィールドは追加した順序で並びます。デフォルトでは、数値型のソース列は `ConsolidationFunction.Sum` で集計されます。一方、数値以外のソース列の既定の集計は `Count` になります。

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
    { "Fruit",     "Banana", 2020,  80 },
    { "Fruit",     "Banana", 2021,  90 },
    { "Vegetable", "Carrot", 2020,  50 },
    { "Vegetable", "Carrot", 2021,  60 },
    { "Vegetable", "Daikon", 2020,  40 },
    { "Vegetable", "Daikon", 2021,  45 }
};
for (int i = 0; i < data.GetLength(0); i++)
{
    for (int j = 0; j < data.GetLength(1); j++)
    {
        worksheet.Cells[i + 1, j].PutValue(data[i, j]);
    }
}
PivotTable pivotTable = worksheet.PivotTables.Add("A1:D9", 2, 5);
pivotTable.AddFieldToArea(PivotFieldType.Row, "Category");
pivotTable.AddFieldToArea(PivotFieldType.Row, "Item");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
pivotTable.CalculateData();
workbook.Save("output_drag.xlsx");
```

## 集計関数の変更
データ領域にフィールドを追加すると、Aspose.Cells では `PivotTable.DataFields` 内の `PivotField` オブジェクトからそのフィールドにアクセスできます。各 `PivotField` には、`ConsolidationFunction` 型の書き込み可能な `Function` プロパティがあり、そのフィールドの基となる値に適用される集計を制御します。`ConsolidationFunction` は、`Sum`、`Count`、`Average`、`Max`、`Min`、`Product`、`StdDev`、`StdDevp`、`Var`、`Varp` をメンバーとする列挙型です。最初の 6 つは実務での使用例の大部分をカバーし、最後の 4 つは分散分析に役立つ統計集計です。

{{% alert color="primary" %}}
`Function` を変更しても集計方法だけが変わり、ソース列とピボットテーブルの行/列構造は変更されません。既存のデータフィールドの集計方法を変更するには、`pivotTable.DataFields[i].Function = ConsolidationFunction.<X>;` を設定してから `pivotTable.CalculateData()` を呼び出し、ピボットテーブルを再描画します。
{{% /alert %}}

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
    { "Fruit",     "Banana", 2020,  80 },
    { "Fruit",     "Banana", 2021,  90 },
    { "Vegetable", "Carrot", 2020,  50 },
    { "Vegetable", "Carrot", 2021,  60 },
    { "Vegetable", "Daikon", 2020,  40 },
    { "Vegetable", "Daikon", 2021,  45 }
};
for (int i = 0; i < data.GetLength(0); i++)
{
    for (int j = 0; j < data.GetLength(1); j++)
    {
        worksheet.Cells[i + 1, j].PutValue(data[i, j]);
    }
}
PivotTable pivotTable = worksheet.PivotTables.Add("A1:D9", 2, 5);
pivotTable.AddFieldToArea(PivotFieldType.Row, "Category");
pivotTable.AddFieldToArea(PivotFieldType.Row, "Item");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
PivotField countField = pivotTable.DataFields[1];
countField.Function = ConsolidationFunction.Count;
pivotTable.CalculateData();
workbook.Save("output_function.xlsx");
```

## 値フィールドを行軸または列軸に配置する
ピボットテーブルに 2 つ以上のデータフィールドが含まれている場合、Aspose.Cells は `PivotTable.ValuesField` という追加の仮想フィールドを公開します。この仮想フィールドは、データ領域にあるすべてのデータフィールドの集計を表し、基本ピボットフィールドとして行領域または列領域にドラッグできます。複数の指標を並べて表示する場合に便利です。

{{% alert color="primary" %}}
`PivotTable.ValuesField` は、値フィールドがない場合や 1 つしかない場合には機能しません。
{{% /alert %}}

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
    { "Fruit",     "Banana", 2020,  80 },
    { "Fruit",     "Banana", 2021,  90 },
    { "Vegetable", "Carrot", 2020,  50 },
    { "Vegetable", "Carrot", 2021,  60 },
    { "Vegetable", "Daikon", 2020,  40 },
    { "Vegetable", "Daikon", 2021,  45 }
};
for (int i = 0; i < data.GetLength(0); i++)
{
    for (int j = 0; j < data.GetLength(1); j++)
    {
        worksheet.Cells[i + 1, j].PutValue(data[i, j]);
    }
}
PivotTable pivotTable = worksheet.PivotTables.Add("A1:D9", 2, 5);
pivotTable.AddFieldToArea(PivotFieldType.Row, "Category");
pivotTable.AddFieldToArea(PivotFieldType.Row, "Item");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
pivotTable.DataFields[1].Function = ConsolidationFunction.Count;
pivotTable.AddFieldToArea(PivotFieldType.Column, pivotTable.ValuesField.Name);
pivotTable.CalculateData();
workbook.Save("output_plot.xlsx");
```

{{< app/cells/assistant language="csharp" >}}