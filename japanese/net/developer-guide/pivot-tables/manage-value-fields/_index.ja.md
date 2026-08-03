---
title: Aspose.Cells for .NET でピボットテーブルの値フィールドを管理する
linktitle: 値フィールド
description: Aspose.Cells for .NET で、ピボットテーブルのデータ領域にベースフィールドを追加する方法、PivotField.Function を使用して集計関数を変更する方法、および値フィールドを行軸または列軸にプロットする方法を学習します。
keywords: Aspose.Cells, .NET, ピボットテーブル, 値フィールド, PivotField, PivotField.Function, データフィールド, PivotTable.ValuesField, Sum, Average
type: docs
weight: 230
url: /ja/net/manage-value-fields/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## データ領域へのフィールド追加
ベースフィールドをデータ（値）領域に追加することは、ピボットテーブルがソースデータを集計する方法を形成する最初のステップです。Aspose.Cells は `PivotTable.AddFieldToArea(PivotFieldType, string)` を提供しており、定数 `PivotFieldType.Data` とソース列名を受け取るオーバーロードです。データ領域にフィールドが追加されると、API はそれを `PivotTable.DataFields` コレクションに追加順に公開します。デフォルトでは、数値のソース列は `ConsolidationFunction.Sum` で集計され、数値以外の列のデフォルトは `Count` になります。
## 集計関数の変更
データ領域に配置された各フィールドは内部的に `PivotField` インスタンスとしてラップされ、その `Function` プロパティは `ConsolidationFunction` 列挙体の値を返します。同じ `Function` セッターを使用すると、`Sum`、`Count`、`Average`、`Max`、`Min`、`Product`、`StdDev`、`StdDevp`、`Var`、`Varp` を含む利用可能な集計間で切り替えることができます。
{{% alert color="primary" %}}
`Function` を変更しても集計のみに影響し、ソース列は変更されません。
{{% /alert %}}
したがって、あるデータフィールドを `Sum` のままにしておきながら、同じソース列を対象とする別のデータフィールドを追加して `Count` または `Average` を使用することもできます。これらはすべて単一のピボット内で実現できます。
## 値フィールドを行軸または列軸にプロットする
ピボットテーブルに 2 つ以上のデータフィールドが含まれている場合、Aspose.Cells は `PivotTable.ValuesField` という追加の仮想フィールドを公開します。この仮想フィールドは、データ領域に存在するすべてのデータフィールドの集計を表します。これを行領域または列領域にベースフィールドとしてドラッグすることができ、複数のメジャーを並べて配置する場合に便利です。
{{% alert color="primary" %}}
`PivotTable.ValuesField` は、値フィールドが存在しない場合、または 1 つしかない場合には機能しません。
{{% /alert %}}
以下のシナリオでは、同じピボット構造に対して、上記で説明した各機能を 3 つのエンドツーエンドの例で順に説明します。
## シナリオ 1 — ベースフィールドを値領域にドラッグする
このシナリオでは、既存のピボットテーブルのデータ領域に単一のベースフィールド（`Amount`）を配置する方法を示します。共有されるピボット構造では、`Category` と `Item` が行軸に、`Year` が列軸に配置されています。操作後、`Amount` はデータ領域に表示され、デフォルトでは `Amount` の `Sum` として計算されます。
```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
worksheet.Name = "Data";

// A1:D1のヘッダー
worksheet.Cells[0, 0].PutValue("Category");
worksheet.Cells[0, 1].PutValue("Item");
worksheet.Cells[0, 2].PutValue("Year");
worksheet.Cells[0, 3].PutValue("Amount");

// A2:D9のデータ行。jで分岐するネストされたループを使用
for (int i = 1; i <= 8; i++)
{
 for (int j = 0; j < 4; j++)
 {
 switch (j)
 {
 case 0:
 worksheet.Cells[i, j].PutValue(i <= 4 ? "Fruit" : "Vegetable");
 break;
 case 1:
 if (i == 1 || i == 2) worksheet.Cells[i, j].PutValue("Apple");
 else if (i == 3 || i == 4) worksheet.Cells[i, j].PutValue("Banana");
 else if (i == 5 || i == 6) worksheet.Cells[i, j].PutValue("Carrot");
 else worksheet.Cells[i, j].PutValue("Daikon");
 break;
 case 2:
 worksheet.Cells[i, j].PutValue(2020 + ((i - 1) % 2));
 break;
 case 3:
 if (i == 1) worksheet.Cells[i, j].PutValue(100);
 else if (i == 2) worksheet.Cells[i, j].PutValue(150);
 else if (i == 3) worksheet.Cells[i, j].PutValue(80);
 else if (i == 4) worksheet.Cells[i, j].PutValue(90);
 else if (i == 5) worksheet.Cells[i, j].PutValue(50);
 else if (i == 6) worksheet.Cells[i, j].PutValue(60);
 else if (i == 7) worksheet.Cells[i, j].PutValue(40);
 else worksheet.Cells[i, j].PutValue(45);
 break;
 }
 }
}

// F3にPivotTable1という名前のピボットテーブルを追加
int pivotIndex = worksheet.PivotTables.Add("A1:D9", "F3", "PivotTable1");
PivotTable pivotTable = worksheet.PivotTables[pivotIndex];

// ピボットレイアウト:行にCategoryとItem、列にYear、データフィールドにAmount
pivotTable.AddFieldToArea(PivotFieldType.Row, "Category");
pivotTable.AddFieldToArea(PivotFieldType.Row, "Item");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");

pivotTable.CalculateData();
workbook.Save("output_drag.xlsx");
```
## シナリオ 2 — 集計関数を変更する
このシナリオは、シナリオ 1 と同じピボット構造から始まりますが、`Amount` フィールドをデータ領域に 2 回追加します。両方のデータフィールドは同じソース列を参照しますが、2 番目のフィールドは `PivotField.Function` セッターを使用して上書きされ、デフォルトの `Sum` ではなく `Count` になります。
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

for (int i = 1; i <= 8; i++)
{
 for (int j = 0; j <= 3; j++)
 {
 if (j == 0)
 {
 worksheet.Cells[i, j].PutValue(i <= 5 ? "Fruit" : "Vegetable");
 }
 else if (j == 1)
 {
 string[] items = { "Apple", "Apple", "Banana", "Banana", "Carrot", "Carrot", "Daikon", "Daikon" };
 worksheet.Cells[i, j].PutValue(items[i - 1]);
 }
 else if (j == 2)
 {
 int[] years = { 2020, 2021, 2020, 2021, 2020, 2021, 2020, 2021 };
 worksheet.Cells[i, j].PutValue(years[i - 1]);
 }
 else
 {
 int[] amounts = { 100, 150, 80, 90, 50, 60, 40, 45 };
 worksheet.Cells[i, j].PutValue(amounts[i - 1]);
 }
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
## シナリオ 3 — 値フィールドを行軸または列軸にプロットする
2 つのデータフィールドが配置されると、`PivotTable.ValuesField` が使用可能になります。このシナリオでは、その集計用仮想フィールドを列領域にドラッグし、データ領域内のすべてのメジャーが `Year` の隣にそれぞれの列ブロックとして表示されるようにします。
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

string[] categories = { "Fruit", "Fruit", "Fruit", "Fruit", "Vegetable", "Vegetable", "Vegetable", "Vegetable" };
string[] items = { "Apple", "Apple", "Banana", "Banana", "Carrot", "Carrot", "Daikon", "Daikon" };
int[] years = { 2020, 2021, 2020, 2021, 2020, 2021, 2020, 2021 };
int[] amounts = { 100, 150, 80, 90, 50, 60, 40, 45 };

for (int i = 1; i <= 8; i++)
{
 for (int j = 0; j <= 3; j++)
 {
 if (j == 0) worksheet.Cells[i, j].PutValue(categories[i - 1]);
 else if (j == 1) worksheet.Cells[i, j].PutValue(items[i - 1]);
 else if (j == 2) worksheet.Cells[i, j].PutValue(years[i - 1]);
 else worksheet.Cells[i, j].PutValue(amounts[i - 1]);
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
これら 3 つのシナリオをまとめると、Aspose.Cells for .NET における値フィールド操作のあらゆる側面を網羅しています。デフォルトの `Sum` を用いた単一のデータフィールドから、仮想 `ValuesField` が行軸または列軸のレイアウトを制御する複数メジャーのピボットまでを取り扱います。

{{< app/cells/assistant language="csharp" >}}
