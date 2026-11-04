---
title: ピボットテーブルの一部をフォーマット
linktitle: ピボットテーブルの一部をフォーマット
description: Aspose.Cells for .NET で PivotTable.Format を使用して、Semantic PivotArea 領域または CellArea 四角形にスタイルを適用し、PivotTable.PivotFormats に保存された書式をピボットテーブルの更新時に保持します。
keywords: Aspose.Cells, ピボットテーブル, 書式設定, PivotArea, CellArea, PivotTable.Format, PivotFormats, PivotTableSelectionType, LabelOnly, DataOnly, SelectField, FormatAll, C#
type: docs
weight: 20
url: /ja/net/format-part-of-pivot-table/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **使用シナリオ**
`PivotTable.FormatAll` はピボットテーブル全体に単一のスタイルを適用します（親ページで説明しています）。ラベル、値、合計、またはレポートの特定領域を区別しません。  
実際には、ピボットテーブルの一部だけを強調表示したい場合が多いです。一般的な対象には、特定の行フィールドに属するラベル、あるフィールドが生成する値セル、総計行、あるいは最初の 2 行のような任意の矩形が含まれます。  
ピボットテーブルのワークシート上のセルに直接スタイルを適用しても同等にはなりません。Excel はピボットテーブルの書式を通常のセルスタイルレコードではなく、セマンティックな `PivotArea` 領域として保存します。`PivotArea` の書式はフィールドのラベルやデータ値といった領域に結び付けられ、ピボットテーブルが再計算、更新、拡張されると再解決されます。一方、セルに直接書き込まれたスタイルはそのセル位置に固定され、ピボットモデルによって追跡されません。  
Aspose.Cells は完全な `PivotTable.Format` オーバーロード ファミリーを公開しており、両方の書式設定方法が利用可能です:
- `Format(PivotArea, Style)` は `PivotArea.Select` または `PivotArea.SelectField` で構築されたセマンティック領域にスタイルを固定します。
- `Format(CellArea, Style)` はピボットテーブル内のワークシート矩形にスタイルを固定します。
- `Format(int row, int column, Style)` は単一セルを対象とします。
- `FormatAll(Style)` はピボットテーブル全体をフォーマットします。

## **Pivot Area をフォーマットする**
Semantic 領域のワークフローは、ハイライトがフィールドやレポートの領域に追従する必要がある場合に推奨されます。
1. `new PivotArea(pivotTable)` で `PivotArea` を作成します。このオブジェクトは対象のピボットテーブルに属する Semantic 領域を表します。  
2. `PivotArea.Select(PivotFieldType axisType, int fieldPosition, PivotTableSelectionType selectionType)` を使用して、指定軸上のゼロベース位置でフィールドを選択します。  
   - `PivotTableSelectionType.DataAndLabel` はラベルとデータの両方を選択します。  
   - `PivotTableSelectionType.LabelOnly` はフィールドのラベルのみを選択します。  
   - `PivotTableSelectionType.DataOnly` はフィールドのデータセルのみを選択します。  
3. `PivotArea.SelectField(PivotFieldType axisType, string fieldName)` でフィールド名を指定して選択します。行フィールドを名前で選択すると、領域はそのフィールドのアイテムが生成する値セルへと解決されます。  
4. `Workbook.CreateStyle()` で `Style` を作成し、フォント、前景色、単色背景パターンを設定し、`PivotTable.Format(area, style)` に渡します。  
5. `PivotArea` の各オーバーロード呼び出しは `PivotTable.PivotFormats` に `PivotTableFormat` エントリを 1 つ追加します。  
6. フィールドに固定された書式はピボットデータの計算時に描画されます。したがって、書式を適用した後に `PivotTable.CalculateData()` を呼び出してスタイルを表示させます。  
以下の例は小規模なフルーツ販売ピボットテーブルを構築し、`Fruit` 行ラベルを `PivotArea.Select` と `PivotTableSelectionType.LabelOnly` でスタイル付けし、同じ行フィールドが生成する値セルを `PivotArea.SelectField` でスタイル付けし、最後にピボットテーブルを再計算して両方のスタイルを描画します。

```csharp
using System;
using System.Drawing;
using Aspose.Cells;
using Aspose.Cells.Pivot;
Workbook workbook = new Workbook();
Worksheet sheet = workbook.Worksheets[0];
Cells cells = sheet.Cells;
// Fruit sales data
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
// Bold yellow fill on the row field's label cells
Style labelStyle = workbook.CreateStyle();
labelStyle.Font.IsBold = true;
labelStyle.ForegroundColor = Color.Yellow;
labelStyle.Pattern = BackgroundType.Solid;
PivotArea labelArea = new PivotArea(pivotTable);
labelArea.Select(PivotFieldType.Row, 0, PivotTableSelectionType.LabelOnly);
pivotTable.Format(labelArea, labelStyle);
// Light green fill on the value cells the row field produces
Style valueStyle = workbook.CreateStyle();
valueStyle.ForegroundColor = Color.LightGreen;
valueStyle.Pattern = BackgroundType.Solid;
PivotArea valueArea = new PivotArea(pivotTable);
valueArea.SelectField(PivotFieldType.Row, "Fruit");
pivotTable.Format(valueArea, valueStyle);
// Field-anchored formats are painted when the data is calculated
pivotTable.CalculateData();
// Label cells E4:E6 are now bold on yellow, value cells F4:F6 are light green
workbook.Save("FormatPivotArea.xlsx");
```

## **ピボットテーブルの Cell Area をフォーマットする**
対象領域が Semantic ピボット領域ではなく、単純なワークシート矩形である場合は `PivotTable.Format(CellArea, Style)` を使用します。  
`CellArea` は `StartRow`, `StartColumn`, `EndRow`, `EndColumn` プロパティで記述されます。これらの値はゼロベースのワークシート座標で、終了座標は矩形に含まれる最後の行と列を示すため、開始位置から終了位置までのセルがすべて対象になります。  
フィールドに固定された書式とは異なり、`CellArea` の書式は直ちにセルに適用されます。スタイルを表示させるために `CalculateData()` を再度呼び出す必要はありません。  
`CellArea` 矩形はラベルセルと値セルを同時に含むことができます。次のセクションでは、Aspose.Cells と Excel がその矩形を内部でどのように表現しているかを説明します。  
以下の例はピボットテーブルの矩形 `E4:F5` に斜体・淡青色のスタイルを適用し、再計算せずにワークブックを保存します。

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
// Highlight the first two fruit rows (the rectangle E4:F5)
Style highlightStyle = workbook.CreateStyle();
highlightStyle.Font.IsItalic = true;
highlightStyle.ForegroundColor = Color.FromArgb(0xFF, 0x99, 0xCC, 0xFF);
highlightStyle.Pattern = BackgroundType.Solid;
CellArea rectangle = new CellArea { StartRow = 3, StartColumn = 4, EndRow = 4, EndColumn = 5 };
pivotTable.Format(rectangle, highlightStyle);
// E4:F5 is italic on light blue immediately, no recalculation needed
workbook.Save("FormatPivotCellArea.xlsx");
```

## **Pivot Area と Cell Area のマッピング**
Excel はピボットテーブルの書式を通常のワークシートセルスタイルレコードではなく `pivotArea` レコードとして保存します。Aspose.Cells も同じモデルを使用しているため、書式要求は内部でピボット領域に変換されます。  
ユーザーが提供した `CellArea` と内部に保存されるピボット領域の関係は、双方向に多対多です。  
- 1 つの `CellArea` は複数のピボット領域を生成することがあります。矩形がラベルセルと値セルの両方を含む場合、ラベル書式とデータ書式に分割されます。ピボットモデルはラベル書式とデータ書式を独立して扱うためです。  
- 1 つのピボット領域は、非連続なアイテムを持つフィールドや総計行など、複数の離散した `CellArea` インスタンスに解決されることがあります。そのため `PivotArea.GetCellAreas()` は単一の矩形ではなくコレクションを返します。  
`PivotTable.Format` を通じて実行されたすべての書式操作は `PivotTable.PivotFormats` に記録されます。各 `PivotTableFormat` エントリは関連付けられた `PivotArea` と適用された `Style` を公開します。`PivotArea` のオーバーロードは呼び出しごとに 1 つのエントリを追加しますが、異なる Semantic 領域を含む `CellArea` は複数のエントリを追加することがあります。  
保存された領域を区別するために、各 `PivotArea` は `OnlyLabel` と `OnlyData` フラグを公開しています。以下の例はラベルと値の両方をカバーする単一矩形をフォーマットし、`PivotTable.PivotFormats` を調査して、各保存されたピボット領域が解決する `CellArea` 座標を出力します。

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
Style highlightStyle = workbook.CreateStyle();
highlightStyle.Font.IsItalic = true;
highlightStyle.ForegroundColor = Color.FromArgb(0xFF, 0x99, 0xCC, 0xFF);
highlightStyle.Pattern = BackgroundType.Solid;
// ONE rectangle in...
CellArea rectangle = new CellArea { StartRow = 3, StartColumn = 4, EndRow = 4, EndColumn = 5 };
pivotTable.Format(rectangle, highlightStyle);
// ...TWO semantic pivot areas out: the label part and the data part are stored separately
Console.WriteLine("Stored formats: " + pivotTable.PivotFormats.Count);
for (int i = 0; i < pivotTable.PivotFormats.Count; i++)
{
    PivotArea storedArea = pivotTable.PivotFormats[i].PivotArea;
    Console.WriteLine($"Format {i}: OnlyLabel={storedArea.OnlyLabel}, OnlyData={storedArea.OnlyData}");
    foreach (CellArea resolved in storedArea.GetCellAreas())
        Console.WriteLine($"    rows {resolved.StartRow + 1}-{resolved.EndRow + 1}, columns {resolved.StartColumn + 1}-{resolved.EndColumn + 1}");
}
// This prints:
// Stored formats: 2
// Format 0: OnlyLabel=True, OnlyData=False
//     rows 4-5, columns 5-5        (E4:E5, the label part)
// Format 1: OnlyLabel=False, OnlyData=True
//     rows 4-5, columns 6-6        (F4:F5, the data part)
workbook.Save("FormatPivotAreasMap.xlsx");
```

{{% alert color="primary" %}}
書式が通常のセルスタイルではなくピボット領域として保存されるため、再計算や更新時にも維持されます。ピボットテーブルを `PivotTable.RefreshData` で更新したり、`CalculateData` で再計算したり、保存して再読み込みしたりしても、すべての保存されたピボット領域は現在の位置に再解決され、スタイルが再適用されます。
{{% /alert %}}

ハイライトをフィールドや Semantic 領域に結び付けてリフレッシュ間で保持したい場合は `Select` または `SelectField` で構築した `PivotArea` を使用し、現在のピボットテーブルレイアウト内の固定矩形をフォーマットしたい場合は `CellArea` を使用してください。単一セルを対象にする場合は `Format(int row, int column, Style)` オーバーロードを利用します。ピボットテーブル全体を一括で再スタイル化したいときは、親ページで説明している `FormatAll` を使用します。

## **Related Articles**
- [ピボットテーブルへのスタイル適用](/cells/ja/net/apply-style-to-pivot-table/)
- [ピボットテーブルの行および列フィールドの追加](/cells/ja/net/pivot-table-add-row-and-column-fields/)
- [ピボットテーブルの値フィールドの管理](/cells/ja/net/manage-value-fields/)
- [ピボットテーブルの更新](/cells/ja/net/refresh-pivot-table/)

{{< app/cells/assistant language="csharp" >}}