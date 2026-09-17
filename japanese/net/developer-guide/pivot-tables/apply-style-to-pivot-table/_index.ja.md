---
title: Aspose.Cells for .Net でピボットテーブルにスタイルを適用
linktitle: Aspose.Cells for .Net でピボットテーブルにスタイルを適用
description: Aspose.Cells for .Net でピボットテーブルに組み込みおよびカスタムスタイルを適用する方法を説明します。レガシー XLS 自動書式、Excel 2007 以降の最新の名前付きスタイル、カスタムピボットテーブルスタイル、および FormatAll ショートカットを扱います。
keywords: Aspose.Cells, .NET, ピボットテーブルのスタイル, PivotTableStyleType, AutoFormatType, FormatAll, カスタムスタイル, PivotTableStyleName, TableStyles
type: docs
weight: 200
url: /ja/net/apply-style-to-pivot-table/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells は、レガシーピボット自動書式（`.xls` ファイル向け）と最新の名前付きまたはカスタムピボットテーブルスタイル（`.xlsx`、`.xlsm`、`.xlsb` ファイル向け）の両方の適用をサポートしています。使用すべき API は、ワークブックの読み込み元形式ではなく、保存先のファイル形式によって決まります。
{{% /alert %}}

## **Introduction**
Aspose.Cells は、ピボットテーブル用に 2 つの並列スタイル API を提供します。どちらを選択するかは、ワークブックの読み込み元形式ではなく、保存先のファイル形式によって決まります。`.xls` ファイルから読み込まれたワークブックを `.xlsx` として再保存することも可能で、その場合はレガシー API ではなく最新のスタイル API が適用されます。
- `PivotTable.PivotTableStyleType` は、組み込みの名前付きスタイル（Excel 2017 で追加されたスタイルを含むライト/ダークテーマ）のいずれかを選択します。これらのプリセットは読み取り専用です。
- `PivotTable.PivotTableStyleName` は、`Workbook.Worksheets.TableStyles.AddPivotTableStyle(...)` を通じて自分で定義したカスタムスタイルを選択します。プリセットで提供される範囲を超えて、色、罫線、またはフォントを変更したい場合は、カスタムスタイルが必要です。
さらに、`PivotTable.FormatAll(Style)` は、単一の `Style` オブジェクトをピボットのすべてのセルに適用するショートカットであり、上記のいずれかのスタイル名 API で設定された内容を上書きします。これは、基になるテーマに関係なく均一な外観が必要な場合に役立ちます。

## **Apply a Legacy XLS Preset Autoformat**
`PivotTable.AutoFormatType` は、`Aspose.Cells.Pivot.PivotTableAutoFormatType` 列挙体からの値を受け取ります。利用可能な値は、`Report1` ～ `Report10`、`Classic`、および `Table1` ～ `Table10` です。
次の例では、新しいワークブックを読み込み、Fruit/Year/Amount のサンプルデータを入力し、ピボットテーブルを追加して `PivotTableAutoFormatType.Report5` を適用し、結果を `.xls` として保存します。

{{% alert color="primary" %}}
**なぜ列フィールドがないのか？** Report シリーズの自動書式（`Report1` ～ `Report10`、`Table1` ～ `Table10`）は、クラシック Excel で行フィールドと値のみを持つ **1 次元のピボットテーブル** 用に設計されており、列フィールドヘッダー用の組み込みスタイリングがありません。ピボットテーブルに列フィールドが必要な場合は、代わりに [シナリオ 2](#apply-a-modern-named-preset-pivot-table-style) の最新の `PivotTableStyleType` プリセットを使用してください。これは、最新の Excel で使用される 2 次元レイアウト向けに設計されています。
{{% /alert %}}

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;
// Scenario 1: Apply a legacy XLS preset autoformat
// API in use: PivotTable.AutoFormatType
// Target file format: .xls (legacy)
// For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-.NET
// Create a new workbook
Workbook workbook = new Workbook();
// Get the first worksheet
Worksheet sheet = workbook.Worksheets[0];
// Populate the source data with header row (Fruit, Year, Amount)
// and 9 data rows covering grape, blueberry, kiwi, cherry across 2020 and 2021
sheet.Cells[0, 0].PutValue("Fruit");
sheet.Cells[0, 1].PutValue("Year");
sheet.Cells[0, 2].PutValue("Amount");
sheet.Cells[1, 0].PutValue("grape");
sheet.Cells[1, 1].PutValue(2020);
sheet.Cells[1, 2].PutValue(50);
sheet.Cells[2, 0].PutValue("blueberry");
sheet.Cells[2, 1].PutValue(2020);
sheet.Cells[2, 2].PutValue(30);
sheet.Cells[3, 0].PutValue("kiwi");
sheet.Cells[3, 1].PutValue(2020);
sheet.Cells[3, 2].PutValue(25);
sheet.Cells[4, 0].PutValue("cherry");
sheet.Cells[4, 1].PutValue(2020);
sheet.Cells[4, 2].PutValue(40);
sheet.Cells[5, 0].PutValue("grape");
sheet.Cells[5, 1].PutValue(2021);
sheet.Cells[5, 2].PutValue(60);
sheet.Cells[6, 0].PutValue("blueberry");
sheet.Cells[6, 1].PutValue(2021);
sheet.Cells[6, 2].PutValue(35);
sheet.Cells[7, 0].PutValue("kiwi");
sheet.Cells[7, 1].PutValue(2021);
sheet.Cells[7, 2].PutValue(28);
sheet.Cells[8, 0].PutValue("cherry");
sheet.Cells[8, 1].PutValue(2021);
sheet.Cells[8, 2].PutValue(45);
sheet.Cells[9, 0].PutValue("grape");
sheet.Cells[9, 1].PutValue(2020);
sheet.Cells[9, 2].PutValue(45);
// Add a pivot table at destination cell E3, named "Pivot1", using source range A1:C10
int pivotIndex = sheet.PivotTables.Add("A1:C10", "E3", "Pivot1");
PivotTable pivotTable = sheet.PivotTables[pivotIndex];
// Assign fields: Fruit -> Rows, Amount -> Data
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
// Apply the legacy XLS preset autoformat "Report5"
// Note: This property is only meaningful when saving as .xls.
// When saved as .xlsx/.xlsm/.xlsb, Excel ignores AutoFormatType
// and uses whatever PivotTableStyleType / PivotTableStyleName specifies.
pivotTable.AutoFormatType = PivotTableAutoFormatType.Report5;
// Save the workbook in legacy .xls format
workbook.Save("output.xls");
```

## **Apply a Modern Named Preset Pivot Table Style**

## **Define and Apply a Custom Pivot Table Style**
組み込みプリセットは変更できません。色、罫線、またはフォントを上書きする必要がある場合は、カスタムピボットスタイルを定義する必要があります。ワークフローは次の3ステップで構成されます。
1. `Workbook.Worksheets.TableStyles.AddPivotTableStyle(string name)` を使用して、カスタムスタイルをワークブックの `TableStyles` コレクションに追加します。新たに作成されたスタイルのインデックスが返されます。
2. `TableStyle.TableStyleElements.Add(TableStyleElementType)` を通じて要素（`WholeTable` や `GrandTotalRow` など）を追加してスタイルを設定し、`TableStyleElement.SetElementStyle(Style)` を通じて各要素に `Style` を割り当てます。
3. `PivotTable.PivotTableStyleName` をスタイルの名前に設定して、カスタムスタイルをピボットテーブルに適用します。このプロパティは組み込みプリセットを選択するため、ここでは `PivotTableStyleType` を使用しないでください。

{{% alert color="primary" %}}
`PivotTableStyleName` と `PivotTableStyleType` は互換的に使用できません。組み込みプリセットには `PivotTableStyleType` を、`AddPivotTableStyle` で定義したカスタムスタイルには `PivotTableStyleName` を使用してください。両方を設定しても問題ありませんが、意図したソースに一致する一方だけが描画されます。
{{% /alert %}}

使用できる `TableStyleElementType` の値には、`WholeTable`、`FirstRow`、`LastRow`、`FirstColumn`、`LastColumn`、`GrandTotalRow`、`GrandTotalColumn`、`PageFieldLabels`、および `PageFieldValues` が含まれます。
次の例では、`WholeTable` に細い黒色の罫線、`GrandTotalRow` に太字の赤色フォントを指定してカスタムピボットスタイルを定義し、`PivotTableStyleName` を使用して適用し、`.xlsx` として保存します。

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;
using System.Drawing;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
// Populate source data: header row + 9 data rows (A1:C10)
worksheet.Cells["A1"].PutValue("Fruit");
worksheet.Cells["B1"].PutValue("Year");
worksheet.Cells["C1"].PutValue("Amount");
worksheet.Cells["A2"].PutValue("Grape");
worksheet.Cells["B2"].PutValue(2020);
worksheet.Cells["C2"].PutValue(100);
worksheet.Cells["A3"].PutValue("Blueberry");
worksheet.Cells["B3"].PutValue(2020);
worksheet.Cells["C3"].PutValue(200);
worksheet.Cells["A4"].PutValue("Kiwi");
worksheet.Cells["B4"].PutValue(2020);
worksheet.Cells["C4"].PutValue(300);
worksheet.Cells["A5"].PutValue("Cherry");
worksheet.Cells["B5"].PutValue(2020);
worksheet.Cells["C5"].PutValue(400);
worksheet.Cells["A6"].PutValue("Grape");
worksheet.Cells["B6"].PutValue(2021);
worksheet.Cells["C6"].PutValue(500);
worksheet.Cells["A7"].PutValue("Blueberry");
worksheet.Cells["B7"].PutValue(2021);
worksheet.Cells["C7"].PutValue(600);
worksheet.Cells["A8"].PutValue("Kiwi");
worksheet.Cells["B8"].PutValue(2021);
worksheet.Cells["C8"].PutValue(700);
worksheet.Cells["A9"].PutValue("Cherry");
worksheet.Cells["B9"].PutValue(2021);
worksheet.Cells["C9"].PutValue(800);
worksheet.Cells["A10"].PutValue("Grape");
worksheet.Cells["B10"].PutValue(2021);
worksheet.Cells["C10"].PutValue(900);
// Add pivot table sourced from A1:C10, anchored at E3, named "Pivot1"
int pivotIndex = worksheet.PivotTables.Add("A1:C10", "E3", "Pivot1");
PivotTable pivotTable = worksheet.PivotTables[pivotIndex];
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
// Step 1: register a new custom pivot table style and capture its index
int styleIndex = workbook.Worksheets.TableStyles.AddPivotTableStyle("CustomPivotStyle");
TableStyle tableStyle = workbook.Worksheets.TableStyles[styleIndex];
// Step 2: add a WholeTable element and apply thin black borders on all four sides
int wholeTableElementIndex = tableStyle.TableStyleElements.Add(TableStyleElementType.WholeTable);
TableStyleElement wholeTableElement = tableStyle.TableStyleElements[wholeTableElementIndex];
Style wholeTableStyle = workbook.CreateStyle();
wholeTableStyle.Borders[BorderType.TopBorder].LineStyle = CellBorderType.Thin;
wholeTableStyle.Borders[BorderType.TopBorder].Color = Color.Black;
wholeTableStyle.Borders[BorderType.BottomBorder].LineStyle = CellBorderType.Thin;
wholeTableStyle.Borders[BorderType.BottomBorder].Color = Color.Black;
wholeTableStyle.Borders[BorderType.LeftBorder].LineStyle = CellBorderType.Thin;
wholeTableStyle.Borders[BorderType.LeftBorder].Color = Color.Black;
wholeTableStyle.Borders[BorderType.RightBorder].LineStyle = CellBorderType.Thin;
wholeTableStyle.Borders[BorderType.RightBorder].Color = Color.Black;
wholeTableElement.SetElementStyle(wholeTableStyle);
// Step 3: add a GrandTotalRow element and apply bold red font
int grandTotalElementIndex = tableStyle.TableStyleElements.Add(TableStyleElementType.GrandTotalRow);
TableStyleElement grandTotalElement = tableStyle.TableStyleElements[grandTotalElementIndex];
Style grandTotalStyle = workbook.CreateStyle();
grandTotalStyle.Font.IsBold = true;
grandTotalStyle.Font.Color = Color.Red;
grandTotalElement.SetElementStyle(grandTotalStyle);
// Step 4: apply the custom style by name (NOT by PivotTableStyleType, which is for built-in presets)
pivotTable.PivotTableStyleName = "CustomPivotStyle";
workbook.Save("output.xlsx");
```

## **Apply One Style to Every Pivot Cell with FormatAll**
`PivotTable.FormatAll(Style)` は、1つの `Style` オブジェクトをピボットテーブルのすべてのセルに適用するショートカットです。これには、データ領域、行および列の見出し、集計が含まれます。`PivotTableStyleType` または `PivotTableStyleName` によって以前に設定された内容はすべて上書きされます。

{{% alert color="primary" %}}
`FormatAll` は、`PivotTableStyleType` と `PivotTableStyleName` の両方を上書きします。ピボットテーブル全体に、テーマに関係なく均一な外観が必要な場合にのみ使用してください。
{{% /alert %}}

次の例では、黄色の単色塗りつぶし、太字の濃青色フォント、および全辺に細い黒色の罫線を持つ `Style` を作成し、`FormatAll` を使用して適用し、`.xlsx` として保存します。

```csharp
using System;
using System.Drawing;
using System.IO;
using Aspose.Cells;
using Aspose.Cells.Pivot;
// Scenario 4: Apply a single Style to every pivot table cell using FormatAll
// API in use: PivotTable.FormatAll(Style)
// Target format: .xlsx
// GitHub reference: see Aspose.Cells-for-.NET repository — pivot table styling examples
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
// Populate source data: header row (row 1) + 9 data rows (rows 2-10)
worksheet.Cells["A1"].PutValue("Fruit");
worksheet.Cells["B1"].PutValue("Year");
worksheet.Cells["C1"].PutValue("Amount");
worksheet.Cells["A2"].PutValue("Grape");
worksheet.Cells["B2"].PutValue(2020);
worksheet.Cells["C2"].PutValue(5000);
worksheet.Cells["A3"].PutValue("Blueberry");
worksheet.Cells["B3"].PutValue(2020);
worksheet.Cells["C3"].PutValue(3000);
worksheet.Cells["A4"].PutValue("Kiwi");
worksheet.Cells["B4"].PutValue(2020);
worksheet.Cells["C4"].PutValue(4000);
worksheet.Cells["A5"].PutValue("Cherry");
worksheet.Cells["B5"].PutValue(2020);
worksheet.Cells["C5"].PutValue(2000);
worksheet.Cells["A6"].PutValue("Grape");
worksheet.Cells["B6"].PutValue(2021);
worksheet.Cells["C6"].PutValue(6000);
worksheet.Cells["A7"].PutValue("Blueberry");
worksheet.Cells["B7"].PutValue(2021);
worksheet.Cells["C7"].PutValue(3500);
worksheet.Cells["A8"].PutValue("Kiwi");
worksheet.Cells["B8"].PutValue(2021);
worksheet.Cells["C8"].PutValue(4500);
worksheet.Cells["A9"].PutValue("Cherry");
worksheet.Cells["B9"].PutValue(2021);
worksheet.Cells["C9"].PutValue(2500);
worksheet.Cells["A10"].PutValue("Grape");
worksheet.Cells["B10"].PutValue(2021);
worksheet.Cells["C10"].PutValue(5500);
// Add pivot table: source range A1:C10, destination cell E3, name "Pivot1"
int pivotIndex = worksheet.PivotTables.Add("A1:C10", "E3", "Pivot1");
PivotTable pivotTable = worksheet.PivotTables[pivotIndex];
// Assign pivot fields: Fruit -> Row area, Year -> Column area, Amount -> Data area
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
// Build a Style that will be forced onto every cell of the pivot table
Style style = workbook.CreateStyle();
style.ForegroundColor = Color.Yellow;
style.Pattern = BackgroundType.Solid;
style.Font.IsBold = true;
style.Font.Color = Color.DarkBlue;
style.Borders[BorderType.TopBorder].LineStyle = CellBorderType.Thin;
style.Borders[BorderType.TopBorder].Color = Color.Black;
style.Borders[BorderType.BottomBorder].LineStyle = CellBorderType.Thin;
style.Borders[BorderType.BottomBorder].Color = Color.Black;
style.Borders[BorderType.LeftBorder].LineStyle = CellBorderType.Thin;
style.Borders[BorderType.LeftBorder].Color = Color.Black;
style.Borders[BorderType.RightBorder].LineStyle = CellBorderType.Thin;
style.Borders[BorderType.RightBorder].Color = Color.Black;
// Apply FormatAll: forces this single style onto every cell of the pivot table,
// overriding any PivotTableStyleType / PivotTableStyleName previously set
pivotTable.FormatAll(style);
// Save the workbook in the modern .xlsx format
workbook.Save("output.xlsx");
```

## **Which Style API Should I Use?**
スタイル API の選択は、保存先のファイル形式によって異なります。次の表をクイックリファレンスとして使用してください。
| 対象ファイル形式 | 使用する API | 注記 |
|---|---|---|
| `.xls`（レガシー） | `PivotTable.AutoFormatType` | `Aspose.Cells.Pivot.PivotTableAutoFormatType` の値（例：`Report1`～`Report10`、`Classic`、`Table1`～`Table10`）。最新の形式で保存する場合は無視されます。 |
| `.xlsx` / `.xlsm` / `.xlsb`（最新の組み込みスタイル） | `PivotTable.PivotTableStyleType` | `Aspose.Cells.PivotTableStyleType` の値（Excel 2017 で追加されたものを含むライト/ダークテーマ）。 |
| `.xlsx` / `.xlsm` / `.xlsb`（最新のカスタムスタイル） | `PivotTable.PivotTableStyleName` + `Worksheets.TableStyles.AddPivotTableStyle(...)` | 組み込みプリセットで十分な機能を実現できない場合に使用します。`TableStyleElement.SetElementStyle(...)` を通じて設定します。 |
| あらゆる形式（均一な上書き） | `PivotTable.FormatAll(Style)` | ピボットテーブル全体の他のすべてのスタイル設定を上書きするショートカットです。 |
判断に迷った場合は、`.xlsx` として保存し、組み込みテーマには `PivotTableStyleType` を、カスタムテーマには `PivotTableStyleName` を使用してください。

## Related Articles
- [Aspose.Cells for .Net でピボットテーブルの行および列フィールドを追加](/cells/ja/net/pivot-table-add-row-and-column-fields/)
- [Aspose.Cells for .Net でピボットテーブルの値フィールドを管理](/cells/ja/net/manage-value-fields/)
- [Aspose.Cells for .Net でピボットテーブルを更新](/cells/ja/net/refresh-pivot-table/)

{{< app/cells/assistant language="csharp" >}}