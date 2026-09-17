---
title: Aspose.Cells for .NET でピボットテーブルの値フィールドを管理する
linktitle: Aspose.Cells for .NET でピボットテーブルの値フィールドを管理する
description: Aspose.Cells for .NET で、ピボットテーブルのデータ領域に基本フィールドを追加する方法、PivotField.Function を使用して集計関数を変更する方法、および値フィールドを行軸または列軸にプロットする方法を学習します。
keywords: Aspose.Cells, .NET, pivot table, value field, PivotField, PivotField.Function, data field, PivotTable.ValuesField, Sum, Average
type: docs
weight: 230
url: /ja/net/manage-value-fields/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## データ領域へのフィールドの追加
基本フィールドをデータ（値）領域に追加することは、ピボットテーブルがソース データを集計する方法を形作る最初のステップです。Aspose.Cells は、定数 `PivotFieldType.Data` とソース列名を受け取るオーバーロード `PivotTable.AddFieldToArea(PivotFieldType, string)` を提供します。データ領域にフィールドが追加されると、API は `PivotTable.DataFields` コレクションを通じてフィールドを公開し、フィールドが追加された順序で格納されます。デフォルトでは、数値型のソース列は `ConsolidationFunction.Sum` で集計され、非数値列は `Count` が既定値となります。

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
int pivotIndex = worksheet.PivotTables.Add("A1:D9", "F3", "PivotTable1");
PivotTable pivotTable = worksheet.PivotTables[pivotIndex];
pivotTable.AddFieldToArea(PivotFieldType.Row, "Category");
pivotTable.AddFieldToArea(PivotFieldType.Row, "Item");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
pivotTable.CalculateData();
workbook.Save("output_drag.xlsx");
```

## 集計関数の変更
フィールドがデータ領域に配置されると、Aspose.Cells は `PivotTable.DataFields` 内の `PivotField` オブジェクトを通じてフィールドを公開します。各 `PivotField` には `ConsolidationFunction` 型の書き込み可能な `Function` プロパティがあり、そのフィールドの基になる値に適用される集計を制御します。`ConsolidationFunction` は `Sum`、`Count`、`Average`、`Max`、`Min`、`Product`、`StdDev`、`StdDevp`、`Var`、`Varp` のメンバーを持つ列挙型です。最初の 6 つは実際の使用例の大多数をカバーし、最後の 4 つは分散分析に役立つ統計的な集計です。

{{% alert color="primary" %}}
`Function` を変更しても集計にのみ影響し、ソース列やピボットの行/列構造は変更されません。既存のデータ フィールドの集計を切り替えるには、`pivotTable.DataFields[i].Function = ConsolidationFunction.<X>;` を設定してから `pivotTable.CalculateData()` を呼び出してピボットを再描画します。
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
int pivotIndex = worksheet.PivotTables.Add("A1:D9", "F3", "PivotTable1");
PivotTable pivotTable = worksheet.PivotTables[pivotIndex];
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

## 値フィールドを行軸または列軸にプロットする
ピボットテーブルに 2 つ以上のデータ フィールドが含まれている場合、Aspose.Cells は `PivotTable.ValuesField` という追加の仮想フィールドを公開します。この仮想フィールドは、データ領域に配置されたすべてのデータ フィールドの集計を表します。これは基本ピボット フィールドとして行領域または列領域にドラッグでき、複数のメジャーを並べて配置する場合に役立ちます。

{{% alert color="primary" %}}
`PivotTable.ValuesField` は、値フィールドが 0 個または 1 個しかない場合は機能しません。
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
int pivotIndex = worksheet.PivotTables.Add("A1:D9", "F3", "PivotTable1");
PivotTable pivotTable = worksheet.PivotTables[pivotIndex];
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