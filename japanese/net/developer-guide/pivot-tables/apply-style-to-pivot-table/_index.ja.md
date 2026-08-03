---
title: Aspose.Cells for .NET でピボットテーブルにスタイルを適用する
linktitle: ピボットテーブルにスタイルを適用
description: Aspose.Cells for .NETでピボットテーブルに組み込みスタイルおよびカスタムスタイルを適用する方法を学びます。レガシーXLSの自動書式、モダンExcel 2007+の名前付きスタイル、カスタムピボットテーブルスタイル、FormatAllショートカットについて解説します。
keywords: Aspose.Cells .NET ピボットテーブル スタイル, PivotTableStyleType, AutoFormatType, FormatAll, カスタムスタイル, PivotTableStyleName, TableStyles
type: docs
weight: 200
url: /ja/net/apply-style-to-pivot-table/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cellsは、レガシーピボット自動書式（`.xls`ファイル向け）と、モダンな名前付きまたはカスタムピボットテーブルスタイル（`.xlsx`、`.xlsm`、`.xlsb`ファイル向け）の両方の適用をサポートしています。使用すべきAPIは、ワークブックを読み込んだ形式ではなく、保存先のファイル形式によって決まります。

{{% /alert %}}

## **はじめに**

Aspose.Cellsはピボットテーブル用に2つの並列スタイルAPIを公開しています。これらの選択は、ワークブックの読み込み元ではなく、保存先のファイル形式によって決まります。`.xls`ファイルから読み込まれたワークブックを`.xlsx`として再保存することができ、その場合はレガシーAPIではなくモダンスタイルAPIが適用されます。

レガシー`.xls`出力の場合は、`PivotTable.AutoFormatType`プロパティを`Aspose.Cells.Pivot.PivotTableAutoFormatType`列挙型と一緒に使用してください。このAPIは、クラシックExcelでピボットテーブル用に提供されていた自動書式ピッカーに対応しています。

モダン`.xlsx`、`.xlsm`、`.xlsb`出力の場合は、2種類のスタイルAPIを利用できます。

- `PivotTable.PivotTableStyleType`は、組み込みの名前付きスタイル（Excel 2017で追加されたスタイルを含むライトテーマおよびダークテーマ）の中から1つを選択します。これらのプリセットは読み取り専用です。
- `PivotTable.PivotTableStyleName`は、`Workbook.Worksheets.TableStyles.AddPivotTableStyle(...)`で定義したカスタムスタイルを選択します。プリセットで提供される色、罫線、フォントを超えて変更を加えたい場合は、必ずカスタムスタイルが必要になります。

さらに、`PivotTable.FormatAll(Style)`は、単一の`Style`オブジェクトをピボットのすべてのセルに適用するショートカットで、上記のスタイル名APIで設定された内容をすべて上書きします。これは、基になるテーマに関係なく均一な外観が必要な場合に便利です。

## **レガシーXLSプリセット自動書式の適用**

`PivotTable.AutoFormatType`は、`Aspose.Cells.Pivot.PivotTableAutoFormatType`列挙型の値を受け取ります。利用可能な値は`Report1`から`Report10`、`Classic`、および`Table1`から`Table10`です。

{{% alert color="primary" %}}

`AutoFormatType`は、ワークブックが`.xls`として保存される場合にのみ有効です。同じワークブックが`.xlsx`、`.xlsm`、または`.xlsb`として保存された場合、Excelはこのプロパティを無視し、`PivotTableStyleType`および`PivotTableStyleName`の設定にフォールバックします。

{{% /alert %}}

次の例では、新しいワークブックを読み込み、Fruit/Year/Amountサンプルデータを設定し、ピボットテーブルを追加して`PivotTableAutoFormatType.Report5`を適用し、結果を`.xls`として保存します。

{{% alert color="primary" %}}

**列フィールドがないのはなぜですか？** Report シリーズの自動書式（`Report1`〜`Report10`、`Table1`〜`Table10`）は、従来の Excel で**単一次元のピボットテーブル**（行フィールドと値のみ）のために設計されたものであり、列フィールドのヘッダーに対する組み込みのスタイル設定はありません。ピボットテーブルに列フィールドが必要な場合は、代わりに下のシナリオ 2 のモダンな `PivotTableStyleType` プリセットを使用してください。これらはモダンな Excel が使用する二次元レイアウト向けに設計されています。

{{% /alert %}}

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;

// シナリオ1: レガシー XLS プリセット自動書式を適用する
// 使用する API: PivotTable.AutoFormatType
// ターゲットファイル形式: .xls (レガシー)
// 完全なサンプルとデータファイルについては、https://github.com/aspose-cells/Aspose.Cells-for-.NET を参照してください

// 新しいワークブックを作成する
Workbook workbook = new Workbook();

// 最初のワークシートを取得する
Worksheet sheet = workbook.Worksheets[0];

// ヘッダー行 (Fruit, Year, Amount) を含むソースデータを入力する
// および 2020 年と 2021 年にわたる grape、blueberry、kiwi、cherry をカバーする 9 つのデータ行
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

// 移動先セル E3 に "Pivot1" という名前のピボットテーブルを、ソース範囲 A1:C10 を使用して追加する
int pivotIndex = sheet.PivotTables.Add("A1:C10", "E3", "Pivot1");
PivotTable pivotTable = sheet.PivotTables[pivotIndex];

// フィールドを割り当てる: Fruit -> 行、Year -> 列、Amount -> データ
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");

// レガシー XLS プリセット自動書式 "Report5" を適用する
// 注: このプロパティは .xls として保存する場合にのみ有効です。
// .xlsx/.xlsm/.xlsb として保存する場合、Excel は AutoFormatType を無視し、
// PivotTableStyleType / PivotTableStyleName で指定された内容を使用します。
pivotTable.AutoFormatType = PivotTableAutoFormatType.Report5;

// ワークブックをレガシー .xls 形式で保存する
workbook.Save("output.xls");
```

## **モダンな名前付きプリセットピボットテーブルスタイルの適用**

`PivotTable.PivotTableStyleType`は、`Aspose.Cells.PivotTableStyleType`列挙型の値を受け取ります。この列挙型は、ライトテーマの`PivotTableStyleLight1`から`PivotTableStyleLight28`、およびダークテーマの`PivotTableStyleDark1`から`PivotTableStyleDark28`をカバーしています。Excel 2017で追加されたスタイル（第2波のライトおよびダークテーマ）も同じ列挙型からアクセスできます。

これは、モダンファイル形式に対して推奨されるAPIです。レガシー自動書式とは異なり、ここで選択されたスタイルはExcelによって忠実にレンダリングされ、他のOfficeツールとのラウンドトリップ後も維持されます。

次の例では、同じFruit/Year/Amountデータを使用し、同じピボットテーブルを作成して`PivotTableStyleDark1`を適用し、ワークブックを`.xlsx`として保存します。

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;

// シナリオ 2: PivotTableStyleType を使用してモダンな Excel 2007+ の名前付き定義済みスタイルを適用します。
// 対象ファイル形式: .xlsx。PivotTableStyleType 列挙型は Aspose.Cells 名前空間にあります
// (Aspose.Cells.Pivot ではありません) — そのため追加の using は不要です。
// GitHub リファレンス: https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Examples/CSharp/PivotTables/ApplyStyleToPivotTable2.cs

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];

// ヘッダー行: Fruit / Year / Amount
worksheet.Cells["A1"].PutValue("Fruit");
worksheet.Cells["B1"].PutValue("Year");
worksheet.Cells["C1"].PutValue("Amount");

// Fruit / Year / Amount の 9 件のデータ行
worksheet.Cells["A2"].PutValue("Grape");
worksheet.Cells["B2"].PutValue(2020);
worksheet.Cells["C2"].PutValue(100);

worksheet.Cells["A3"].PutValue("Blueberry");
worksheet.Cells["B3"].PutValue(2020);
worksheet.Cells["C3"].PutValue(150);

worksheet.Cells["A4"].PutValue("Kiwi");
worksheet.Cells["B4"].PutValue(2020);
worksheet.Cells["C4"].PutValue(200);

worksheet.Cells["A5"].PutValue("Cherry");
worksheet.Cells["B5"].PutValue(2020);
worksheet.Cells["C5"].PutValue(180);

worksheet.Cells["A6"].PutValue("Grape");
worksheet.Cells["B6"].PutValue(2021);
worksheet.Cells["C6"].PutValue(120);

worksheet.Cells["A7"].PutValue("Blueberry");
worksheet.Cells["B7"].PutValue(2021);
worksheet.Cells["C7"].PutValue(170);

worksheet.Cells["A8"].PutValue("Kiwi");
worksheet.Cells["B8"].PutValue(2021);
worksheet.Cells["C8"].PutValue(210);

worksheet.Cells["A9"].PutValue("Cherry");
worksheet.Cells["B9"].PutValue(2021);
worksheet.Cells["C9"].PutValue(190);

worksheet.Cells["A10"].PutValue("Grape");
worksheet.Cells["B10"].PutValue(2021);
worksheet.Cells["C10"].PutValue(130);

// E3 に "Pivot1" という名前のピボットテーブルを追加し、データソースは A1:C10 とする
int pivotIndex = worksheet.PivotTables.Add("A1:C10", "E3", "Pivot1");
PivotTable pivotTable = worksheet.PivotTables[pivotIndex];

// ピボットフィールドを割り当てる: Fruit -> 行エリア、Year -> 列エリア、Amount -> データエリア
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");

// モダンな Excel 2007+ の名前付き定義済みピボットスタイルを適用します。
// PivotTableStyleType は .xlsx / .xlsm / .xlsb ファイルに対して正しい API です。AutoFormatType は
// これらの形式では Excel によって無視されます。PivotTableStyleDark1 はダークテーマファミリー
// (PivotTableStyleDark1..PivotTableStyleDark28) に属し、同じ列挙型には新しい Excel 2017 の
// ライト/ダークテーマ (PivotTableStyleLight1..Light28 / Dark1..Dark28) も公開されています。
pivotTable.PivotTableStyleType = PivotTableStyleType.PivotTableStyleDark1;

// モダンな .xlsx として保存 — これは PivotTableStyleType が意味を持つ形式です。
workbook.Save("output.xlsx");
```

## **カスタムピボットテーブルスタイルの定義と適用**

組み込みプリセットは変更できません。色、罫線、またはフォントを上書きする必要がある場合は、必ずカスタムピボットスタイルを定義する必要があります。ワークフローは3つのステップで構成されます。

1. `Workbook.Worksheets.TableStyles.AddPivotTableStyle(string name)`を使用して、ワークブックの`TableStyles`コレクションにカスタムスタイルを追加します。これにより、新しく作成されたスタイルのインデックスが返されます。
2. `TableStyle.TableStyleElements.Add(TableStyleElementType)`で要素（`WholeTable`や`GrandTotalRow`など）を追加し、`TableStyleElement.SetElementStyle(Style)`で各要素に`Style`を割り当てることで、スタイルを構成します。
3. `PivotTable.PivotTableStyleName`にスタイル名を設定して、カスタムスタイルをピボットに適用します。このプロパティは組み込みプリセットを選択するため、ここでは`PivotTableStyleType`を使用しないでください。

{{% alert color="primary" %}}

`PivotTableStyleName`と`PivotTableStyleType`は置き換え可能ではありません。組み込みプリセットには`PivotTableStyleType`を、`AddPivotTableStyle`で定義したカスタムスタイルには`PivotTableStyleName`を使用してください。両方を設定しても害はありませんが、意図したソースと一致する一方のみがレンダリングされます。

{{% /alert %}}

利用可能な`TableStyleElementType`の値には、`WholeTable`、`FirstRow`、`LastRow`、`FirstColumn`、`LastColumn`、`GrandTotalRow`、`GrandTotalColumn`、`PageFieldLabels`、`PageFieldValues`があります。

次の例では、`WholeTable`に細い黒の罫線を、`GrandTotalRow`に太字の赤いフォントを持つカスタムピボットスタイルを定義し、`PivotTableStyleName`を介して適用して、`.xlsx`として保存します。

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;
using System.Drawing;

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];

// ソースデータを設定: ヘッダー行 + 9 データ行 (A1:C10)
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

// A1:C10 をソースとするピボットテーブルを E3 に配置し、"Pivot1" という名前を付ける
int pivotIndex = worksheet.PivotTables.Add("A1:C10", "E3", "Pivot1");
PivotTable pivotTable = worksheet.PivotTables[pivotIndex];

pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");

// ステップ 1: 新しいカスタムピボットテーブルスタイルを登録し、そのインデックスを取得する
int styleIndex = workbook.Worksheets.TableStyles.AddPivotTableStyle("CustomPivotStyle");
TableStyle tableStyle = workbook.Worksheets.TableStyles[styleIndex];

// ステップ 2: WholeTable 要素を追加し、4 辺すべてに細い黒色の境界線を適用する
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

// ステップ 3: GrandTotalRow 要素を追加し、太字の赤色フォントを適用する
int grandTotalElementIndex = tableStyle.TableStyleElements.Add(TableStyleElementType.GrandTotalRow);
TableStyleElement grandTotalElement = tableStyle.TableStyleElements[grandTotalElementIndex];
Style grandTotalStyle = workbook.CreateStyle();
grandTotalStyle.Font.IsBold = true;
grandTotalStyle.Font.Color = Color.Red;
grandTotalElement.SetElementStyle(grandTotalStyle);

// ステップ 4: カスタムスタイルを名前で適用する (組み込みプリセット用の PivotTableStyleType ではなく)
pivotTable.PivotTableStyleName = "CustomPivotStyle";

workbook.Save("output.xlsx");
```

## **FormatAll で1つのスタイルをすべてのピボットセルに適用する**

`PivotTable.FormatAll(Style)`は、データエリア、行と列のヘッダー、集計を含むピボットテーブルのすべてのセルに単一の`Style`オブジェクトを適用するショートカットです。`PivotTableStyleType`または`PivotTableStyleName`を介して以前に設定された内容はすべて上書きされます。

{{% alert color="primary" %}}

`FormatAll`は`PivotTableStyleType`と`PivotTableStyleName`の両方を上書きします。ピボット全体でテーマに関係なく均一な外観が必要な場合にのみ使用してください。

{{% /alert %}}

次の例では、黄色の単色塗りつぶし、太字のダークブルーフォント、すべての辺に細い黒の罫線を持つ`Style`を作成し、`FormatAll`で適用して、`.xlsx`として保存します。

```csharp
using System;
using System.Drawing;
using System.IO;
using Aspose.Cells;
using Aspose.Cells.Pivot;

// シナリオ4: FormatAllを使用して、すべてのピボットテーブルセルに単一のスタイルを適用
// 使用API: PivotTable.FormatAll(Style)
// 対象形式: .xlsx
// GitHubリファレンス: Aspose.Cells-for-.NETリポジトリを参照 — ピボットテーブルスタイリングの例

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];

// ソースデータを入力: ヘッダー行(1行目) + データ9行(2～10行目)
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

// ピボットテーブルを追加: ソース範囲 A1:C10、配置先セル E3、名前 "Pivot1"
int pivotIndex = worksheet.PivotTables.Add("A1:C10", "E3", "Pivot1");
PivotTable pivotTable = worksheet.PivotTables[pivotIndex];

// ピボットフィールドを割り当て: Fruit → 行エリア、Year → 列エリア、Amount → データエリア
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");

// ピボットテーブルのすべてのセルに強制適用するStyleを構築
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

// FormatAllを適用: この単一のスタイルをピボットテーブルのすべてのセルに強制適用し、
// 以前に設定された PivotTableStyleType / PivotTableStyleName を上書きします
pivotTable.FormatAll(style);

// モダンな .xlsx 形式でワークブックを保存
workbook.Save("output.xlsx");
```

## **どのスタイルAPIを使用すべきですか?**

スタイルAPIの選択は、保存先のファイル形式によって異なります。下の表をクイックリファレンスとしてご活用ください。

| 保存先のファイル形式 | 使用するAPI | 備考 |
|---|---|---|
| `.xls`（レガシー） | `PivotTable.AutoFormatType` | `Aspose.Cells.Pivot.PivotTableAutoFormatType`の値（例：`Report1`～`Report10`、`Classic`、`Table1`～`Table10`）。モダン形式で保存する場合は無視されます。 |
| `.xlsx` / `.xlsm` / `.xlsb`（モダン、組み込みスタイル） | `PivotTable.PivotTableStyleType` | `Aspose.Cells.PivotTableStyleType`の値（Excel 2017で追加されたものを含むライト/ダークテーマ）。 |
| `.xlsx` / `.xlsm` / `.xlsb`（モダン、カスタムスタイル） | `PivotTable.PivotTableStyleName` + `Worksheets.TableStyles.AddPivotTableStyle(...)` | 組み込みプリセットでは不十分な場合に使用します。`TableStyleElement.SetElementStyle(...)`で設定します。 |
| 任意の形式（一律上書き） | `PivotTable.FormatAll(Style)` | ピボット全体の他のすべてのスタイル設定を上書きするショートカットです。 |

迷った場合は、`.xlsx`として保存し、組み込みテーマには`PivotTableStyleType`を、カスタムテーマには`PivotTableStyleName`を使用してください。

## **関連記事**

- [Aspose.Cells for .NETでピボットテーブルを更新する](/cells/ja/net/refresh-pivot-table/)

{{< app/cells/assistant language="csharp" >}}