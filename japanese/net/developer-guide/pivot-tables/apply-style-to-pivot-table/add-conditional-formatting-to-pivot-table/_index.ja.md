---
title: ピボットテーブルに条件付き書式を追加する
linktitle: ピボットテーブルに条件付き書式を追加する
description: Aspose.Cells for .NET でピボットテーブルに条件付き書式を追加します。ApplyTo と PivotConditionFormatScopeType スコープでデータ領域にルールをアンカーするか、AddCellArea と PivotAreas で対象を定義し、FormatConditions.AddCondition を使用してルールとスタイルを適用します。
keywords: Aspose.Cells, ピボットテーブル, 条件付き書式, PivotConditionalFormat, ConditionalFormats, ApplyTo, PivotConditionFormatScopeType, Data, Field, Selection, AddCellArea, PivotAreas, AddPivotArea, FormatConditions, AddCondition, FormatConditionType, C#
type: docs
weight: 30
url: /ja/net/add-conditional-formatting-to-pivot-table/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **考えられる使用シナリオ**
親ページおよび兄弟ページで説明されているスタイルは静的です。`PivotArea` または `CellArea` 領域は一度適用され、値が何であってもその書式が保持されます。条件付き書式はルール駆動の対応物であり、200 を超える金額をハイライトしたり、中央値の 50% をシェードしたり、下位のアイテムにフラグを付けたりできます。ハイライトはピボットテーブルが再計算または再描画されるたびに値に合わせて更新されます。  
Aspose.Cells では、ピボットテーブルの条件付き書式は `PivotTable.ConditionalFormats` コレクションに格納されます。各エントリは `PivotConditionalFormat` であり、次の 2 つの質問に独立して答えます。
- **ルールの適用対象はどこですか？** 対象領域は `ApplyTo(int row, int column, PivotConditionFormatScopeType scope)` で定義できます。このメソッドは Excel の UI にあるスコープ選択と同等です。または `AddCellArea(CellArea)` と `PivotAreas` コレクションを使用して領域を明示的に指定します。
- **ルールのテスト内容は何ですか？** `FormatConditions` に対して `FormatConditionCollection.AddCondition(FormatConditionType type, OperatorType operatorType, string formula1, string formula2)` を使用して 1 つ以上の条件を追加し、各条件に固有の `Style` を設定します。

{{% alert color="primary" %}}
`FormatConditionCollection.Add(CellArea cellArea, FormatConditionType type, OperatorType operatorType, string formula1, string formula2)` または `FormatConditionCollection.AddArea(CellArea)` をピボット条件付き書式の `FormatConditions` オブジェクトで呼び出さないでください。これら 2 つのオーバーロードは通常のワークシート条件付き書式 API から継承されたものであり、ピボットテーブルでは機能しません。セル領域はピボット領域に変換されず、リクエストは黙って無視されます。領域は必ず `PivotConditionalFormat` 自体で (`ApplyTo`、`AddCellArea`、または `PivotAreas`) 定義し、`AddCondition` のいずれかのオーバーロードでルールを追加してください。
{{% /alert %}}

## **スコープを使用してルールを適用する（Excel UI の方法）**
最初の方法は、Excel のユーザーインターフェイスと同様にルールを配置します。ピボットテーブルのセルは 0 基準のワークシート座標で名前付けされ、`PivotConditionFormatScopeType` スコープが Aspose.Cells に対してそのセルからルールがどこまで適用されるかを指示します。
- `PivotConditionFormatScopeType.Data` - ピボットテーブルが生成するすべての値セル（総計を含む）。
- `PivotConditionFormatScopeType.Field` - そのセルが指すフィールドに属する値セル（総計は除外）。セルは行フィールドラベルなどのフィールドセルである必要があり、値セルを渡すと例外がスローされます。
- `PivotConditionFormatScopeType.Selection` - セルが選択する交差点の値セルのみで、通常は単一の値セルです。
以下の例では、E3 を左上隅とするフルーツ販売ピボットテーブルを作成し、`Data` スコープでセル F4（行 3、列 5）に条件付き書式をアンカーし、200 を超える金額を背景赤・文字白・太字でハイライトします。Apple が 220、Banana が 330、Cherry が 200、総計が 750 の場合、ルールは F4、F5、F7 を塗りつぶします。解決された領域はデータ列全体の F4:F7 であり、条件を満たすセルだけがハイライトされます。

```csharp
using System;
using System.Drawing;
using Aspose.Cells;
using Aspose.Cells.Pivot;
Workbook workbook = new Workbook();
Worksheet sheet = workbook.Worksheets[0];
Cells cells = sheet.Cells;
string[] fruits = { "Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry" };
int[] years = { 2024, 2024, 2025, 2025, 2024, 2025 };
int[] amounts = { 100, 150, 120, 180, 90, 110 };
cells["A1"].PutValue("Fruit");
cells["B1"].PutValue("Year");
cells["C1"].PutValue("Amount");
for (int i = 0; i < fruits.Length; i++)
{
    cells[i + 1, 0].PutValue(fruits[i]);
    cells[i + 1, 1].PutValue(years[i]);
    cells[i + 1, 2].PutValue(amounts[i]);
}
// Pivot table with its top-left corner at E3
PivotTable pivotTable = sheet.PivotTables.Add("=A1:C7", 2, 4);
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
pivotTable.CalculateData();
// Anchor the conditional format at F4 (row 3, column 5) with the Data scope
int index = pivotTable.ConditionalFormats.Add();
PivotConditionalFormat format = pivotTable.ConditionalFormats[index];
format.ApplyTo(3, 5, PivotConditionFormatScopeType.Data);
// Rule - highlight amounts greater than 200
int conditionIndex = format.FormatConditions.AddCondition(
    FormatConditionType.CellValue, OperatorType.GreaterThan, "200", null);
Style style = workbook.CreateStyle();
style.Font.IsBold = true;
style.Font.Color = Color.White;
style.ForegroundColor = Color.Red;
style.Pattern = BackgroundType.Solid;
format.FormatConditions[conditionIndex].Style = style;
workbook.Save("PivotConditionalFormatData.xlsx");
```

同じルールを行フィールドラベル E4（行 3、列 4）に `Field` スコープでアンカーすると、対象は F4:F6 となります（総計行を除く同じデータ列）。`Selection` スコープで F4 にアンカーすると、対象は F4 のみになります。

## **領域を手動で定義する**
スコープ選択を省略し、`PivotConditionalFormat` 上で領域を明示的に名前付けする方法です。

### **AddCellArea を使用したワークシートの矩形**
`AddCellArea(CellArea)` は、指定された矩形をルールのターゲットとして記録します。座標は 0 基準のワークシート座標であり、領域は提供された矩形そのものです。データ列への拡張や総計ロジックはありません。現在のピボットレイアウトで興味のあるセルが既知の固定矩形である場合に使用します。

```csharp
using System;
using System.Drawing;
using Aspose.Cells;
using Aspose.Cells.Pivot;
Workbook workbook = new Workbook();
Worksheet sheet = workbook.Worksheets[0];
Cells cells = sheet.Cells;
string[] fruits = { "Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry" };
int[] years = { 2024, 2024, 2025, 2025, 2024, 2025 };
int[] amounts = { 100, 150, 120, 180, 90, 110 };
cells["A1"].PutValue("Fruit");
cells["B1"].PutValue("Year");
cells["C1"].PutValue("Amount");
for (int i = 0; i < fruits.Length; i++)
{
    cells[i + 1, 0].PutValue(fruits[i]);
    cells[i + 1, 1].PutValue(years[i]);
    cells[i + 1, 2].PutValue(amounts[i]);
}
PivotTable pivotTable = sheet.PivotTables.Add("=A1:C7", 2, 4);
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
pivotTable.CalculateData();
// Target the rectangle F4:F6 (the value cells without the grand total)
int index = pivotTable.ConditionalFormats.Add();
PivotConditionalFormat format = pivotTable.ConditionalFormats[index];
format.AddCellArea(new CellArea { StartRow = 3, StartColumn = 5, EndRow = 5, EndColumn = 5 });
// Rule - italic on light yellow for amounts between 150 and 300
int conditionIndex = format.FormatConditions.AddCondition(
    FormatConditionType.CellValue, OperatorType.Between, "150", "300");
Style style = workbook.CreateStyle();
style.Font.IsItalic = true;
style.ForegroundColor = Color.LightYellow;
style.Pattern = BackgroundType.Solid;
format.FormatConditions[conditionIndex].Style = style;
workbook.Save("PivotConditionalFormatCellArea.xlsx");
```

### **PivotAreas を使用した意味的ピボット領域**
`PivotAreas` は、兄弟ページで静的スタイルに使用されているのと同じ意味的領域モデルです。`PivotArea` を作成し、`Select` または `SelectField` でフィールドまたは領域を選択し、`PivotAreas.AddPivotArea(PivotArea)` で追加します。意味的領域はフィールドに紐付いているため、ピボットテーブルが再描画されレイアウトが変わっても条件付き書式はフィールドに追随します。`PivotAreas.Add(PivotArea)` のオーバーロードもコンパイルは通りますが、廃止予定としてマークされているため `AddPivotArea` を使用してください。

```csharp
using System;
using System.Drawing;
using Aspose.Cells;
using Aspose.Cells.Pivot;
Workbook workbook = new Workbook();
Worksheet sheet = workbook.Worksheets[0];
Cells cells = sheet.Cells;
string[] fruits = { "Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry" };
int[] years = { 2024, 2024, 2025, 2025, 2024, 2025 };
int[] amounts = { 100, 150, 120, 180, 90, 110 };
cells["A1"].PutValue("Fruit");
cells["B1"].PutValue("Year");
cells["C1"].PutValue("Amount");
for (int i = 0; i < fruits.Length; i++)
{
    cells[i + 1, 0].PutValue(fruits[i]);
    cells[i + 1, 1].PutValue(years[i]);
    cells[i + 1, 2].PutValue(amounts[i]);
}
PivotTable pivotTable = sheet.PivotTables.Add("=A1:C7", 2, 4);
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
pivotTable.CalculateData();
// Attach the rule to the Amount data field as a semantic region
int index = pivotTable.ConditionalFormats.Add();
PivotConditionalFormat format = pivotTable.ConditionalFormats[index];
PivotArea area = new PivotArea(pivotTable);
area.SelectField(PivotFieldType.Data, "Amount");
format.PivotAreas.AddPivotArea(area);
// Rule - grey text for amounts below 150
int conditionIndex = format.FormatConditions.AddCondition(
    FormatConditionType.CellValue, OperatorType.LessThan, "150", null);
Style style = workbook.CreateStyle();
style.Font.Color = Color.Gray;
format.FormatConditions[conditionIndex].Style = style;
workbook.Save("PivotConditionalFormatPivotArea.xlsx");
```

## **ルールの保存場所と再読み込み時の持続性**
`ConditionalFormats.Add()` の呼び出しごとに、ピボットテーブルに `PivotConditionalFormat` が 1 つ追加されます。条件、その数式、スタイルはワークブックに保存されます。下の例でファイルを再度開くと、同じルールがタイプ、演算子、数式がそのまま保持された状態で表示され、`GetCellAreas()` が同じ領域を報告します。条件がまったく設定されていないエントリは、ワークブックが保存される際に削除されます。これは、Excel がルールのない条件付き書式を破棄するのと同様です。

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;
Workbook workbook = new Workbook("PivotConditionalFormatData.xlsx");
PivotTable pivotTable = workbook.Worksheets[0].PivotTables[0];
Console.WriteLine("Conditional formats: " + pivotTable.ConditionalFormats.Count);
for (int i = 0; i < pivotTable.ConditionalFormats.Count; i++)
{
    PivotConditionalFormat format = pivotTable.ConditionalFormats[i];
    for (int j = 0; j < format.FormatConditions.Count; j++)
    {
        FormatCondition condition = format.FormatConditions[j];
        Console.WriteLine($"Format {i}: {condition.Type} {condition.Operator} formula1={condition.Formula1}");
    }
    foreach (CellArea area in format.GetCellAreas())
        Console.WriteLine($"    rows {area.StartRow + 1}-{area.EndRow + 1}, columns {area.StartColumn + 1}-{area.EndColumn + 1}");
}
// This prints:
// Conditional formats: 1
// Format 0: CellValue GreaterThan formula1==200
//     rows 4-7, columns 6-6        (F4:F7, the resolved data region)
```

## **Related Articles**
- [ピボットテーブルへのスタイル適用](/cells/ja/net/apply-style-to-pivot-table/)
- [ピボットテーブルの一部の書式設定](/cells/ja/net/format-part-of-pivot-table/)
- [ピボットテーブルのトップ 10 表示またはフィルター](/cells/ja/net/top-10-show-or-filter-in-pivot-table/)
- [ラベルまたは値によるピボットテーブルのフィルタリング](/cells/ja/net/filter-by-label-or-value-of-pivot-table/)

{{< app/cells/assistant language="csharp" >}}