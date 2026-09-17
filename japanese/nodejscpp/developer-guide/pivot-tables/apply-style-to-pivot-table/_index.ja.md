---
title: Aspose.Cells for Node.js via C++ でピボットテーブルにスタイルを適用する
linktitle: Aspose.Cells for Node.js via C++ でピボットテーブルにスタイルを適用する
description: Aspose.Cells for Node.js via C++ を使用して、レガシー XLS の自動書式、最新の Excel 2007+ 名前付きスタイル、カスタムのピボットテーブルスタイル、および FormatAll ショートカットなど、組み込みおよびカスタムのスタイルをピボットテーブルに適用する方法を学びます。
keywords: Aspose.Cells for Node.js via C++ ピボットテーブル スタイル, PivotTableStyleType, AutoFormatType, FormatAll, カスタムスタイル, PivotTableStyleName, TableStyles
type: docs
weight: 200
url: /ja/nodejs-cpp/apply-style-to-pivot-table/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells は、レガシーのピボット自動書式（`.xls` ファイル向け）と、最新の名前付きまたはカスタムのピボットテーブルスタイル（`.xlsx`、`.xlsm`、`.xlsb` ファイル向け）の両方の適用をサポートしています。呼び出すべき API は、ワークブックの読み込み元形式ではなく、保存先のファイル形式によって決まります。
{{% /alert %}}

## **概要**
Aspose.Cells は、ピボットテーブルに対して並列に機能する 2 つのスタイル API を提供しています。どちらを使用するかは、読み込み元の形式ではなく、ワークブックの保存先のファイル形式によって決まります。`.xls` ファイルから読み込んだワークブックを `.xlsx` として再保存する場合、レガシーのスタイル API ではなく、最新のスタイル API が適用されます。
- `PivotTable.PivotTableStyleType` は、組み込みの名前付きスタイル（明テーマおよび暗テーマ、Excel 2017 で追加されたスタイルを含む）のいずれかを選択します。これらのプリセットは読み取り専用です。
- `PivotTable.PivotTableStyleName` は、`Workbook.Worksheets.TableStyles.AddPivotTableStyle(...)` を使用して自身で定義したカスタムスタイルを選択します。プリセットで提供される色、罫線、フォント以外の変更が必要な場合は、カスタムスタイルが必要です。
さらに、`PivotTable.FormatAll(Style)` は、単一の `Style` オブジェクトをピボット内のすべてのセルに適用するショートカットであり、上記のいずれかのスタイル名 API によって設定された内容を上書きします。これは、基になるテーマに関係なく均一な外観が必要な場合に便利です。

## **レガシー XLS のプリセット自動書式を適用する**
`PivotTable.AutoFormatType` は、`Aspose.Cells.Pivot.PivotTableAutoFormatType` 列挙体の値を受け取ります。利用可能な値は、`Report1` から `Report10`、`Classic`、および `Table1` から `Table10` です。
次の例では、新しいワークブックを読み込み、Fruit/Year/Amount のサンプルデータを入力し、ピボットテーブルを追加し、`PivotTableAutoFormatType.Report5` を適用して、結果を `.xls` として保存します。

{{% alert color="primary" %}}
**なぜ列フィールドがないのでしょうか？** Report シリーズの自動書式（`Report1` から `Report10`、`Table1` から `Table10`）は、旧バージョンの Excel において、**単一次元のピボットテーブル**（行フィールドと値のみを持つ）向けに設計されています。これらの自動書式には、列フィールドヘッダー用の組み込みスタイルがありません。ピボットテーブルに列フィールドが必要な場合は、最新の Excel で使用される二次元レイアウト用に設計されている、[シナリオ 2](#apply-a-modern-named-preset-pivot-table-style) の最新の `PivotTableStyleType` プリセットを使用してください。
{{% /alert %}}

```javascript
const AsposeCells = require("aspose.cells");
// シナリオ1: レガシー XLS プリセット自動フォーマットを適用する
// 使用中の API: PivotTable.AutoFormatType
// 対象ファイル形式: .xls (レガシー)
// 完全なサンプルとデータファイルについては、https://github.com/aspose-cells/Aspose.Cells-for-.NET を参照してください
// 新しいワークブックを作成する
const workbook = new AsposeCells.Workbook();
// 最初のワークシートを取得する
const sheet = workbook.getWorksheets().get(0);
// ヘッダー行 (Fruit, Year, Amount) を含むソースデータを設定する
// および2020年と2021年にわたる grape、blueberry、kiwi、cherry をカバーする9行のデータ
sheet.getCells().get(0, 0).putValue("Fruit");
sheet.getCells().get(0, 1).putValue("Year");
sheet.getCells().get(0, 2).putValue("Amount");
sheet.getCells().get(1, 0).putValue("grape");
sheet.getCells().get(1, 1).putValue(2020);
sheet.getCells().get(1, 2).putValue(50);
sheet.getCells().get(2, 0).putValue("blueberry");
sheet.getCells().get(2, 1).putValue(2020);
sheet.getCells().get(2, 2).putValue(30);
sheet.getCells().get(3, 0).putValue("kiwi");
sheet.getCells().get(3, 1).putValue(2020);
sheet.getCells().get(3, 2).putValue(25);
sheet.getCells().get(4, 0).putValue("cherry");
sheet.getCells().get(4, 1).putValue(2020);
sheet.getCells().get(4, 2).putValue(40);
sheet.getCells().get(5, 0).putValue("grape");
sheet.getCells().get(5, 1).putValue(2021);
sheet.getCells().get(5, 2).putValue(60);
sheet.getCells().get(6, 0).putValue("blueberry");
sheet.getCells().get(6, 1).putValue(2021);
sheet.getCells().get(6, 2).putValue(35);
sheet.getCells().get(7, 0).putValue("kiwi");
sheet.getCells().get(7, 1).putValue(2021);
sheet.getCells().get(7, 2).putValue(28);
sheet.getCells().get(8, 0).putValue("cherry");
sheet.getCells().get(8, 1).putValue(2021);
sheet.getCells().get(8, 2).putValue(45);
sheet.getCells().get(9, 0).putValue("grape");
sheet.getCells().get(9, 1).putValue(2020);
sheet.getCells().get(9, 2).putValue(45);
// 宛先セル E3 に "Pivot1" という名前のピボットテーブルを、ソース範囲 A1:C10 を使用して追加する
const pivotIndex = sheet.getPivotTables().add("A1:C10", "E3", "Pivot1");
const pivotTable = sheet.getPivotTables().get(pivotIndex);
// フィールドを割り当てる: Fruit -> 行、Amount -> データ
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
// レガシー XLS プリセット自動フォーマット "Report5" を適用する
// 注意: このプロパティは .xls として保存する場合にのみ有効です。
// .xlsx/.xlsm/.xlsb として保存する場合、Excel は AutoFormatType を無視し、
// PivotTableStyleType / PivotTableStyleName で指定されたものを使用します。
pivotTable.setAutoFormatType(AsposeCells.PivotTableAutoFormatType.Report5);
// レガシー .xls 形式でワークブックを保存する
workbook.save("output.xls");
```

## **最新の名前付きプリセットピボットテーブルスタイルを適用する**

## **カスタムのピボットテーブルスタイルを定義して適用する**
組み込みのプリセットは変更できません。色、罫線、フォントを上書きする必要がある場合は、常にカスタムのピボットスタイルを定義する必要があります。ワークフローは次の 3 ステップで構成されます。
1. `Workbook.Worksheets.TableStyles.AddPivotTableStyle(string name)` を介して、ワークブックの `TableStyles` コレクションにカスタムスタイルを追加します。これにより、新しく作成されたスタイルのインデックスが返されます。
2. `TableStyle.TableStyleElements.Add(TableStyleElementType)` を通じて要素（`WholeTable` や `GrandTotalRow` など）を追加し、`TableStyleElement.SetElementStyle(Style)` を介して各要素に `Style` を割り当てることで、スタイルを構成します。
3. `PivotTable.PivotTableStyleName` をスタイルの名前に設定することで、カスタムスタイルをピボットテーブルに適用します。このプロパティは組み込みプリセットを選択するため、ここで `PivotTableStyleType` を使用しないでください。

{{% alert color="primary" %}}
`PivotTableStyleName` と `PivotTableStyleType` は互換性がありません。組み込みプリセットには `PivotTableStyleType` を、`AddPivotTableStyle` を通じて定義したカスタムスタイルには `PivotTableStyleName` を使用してください。両方を設定しても問題ありませんが、レンダリングされるのは目的のソースに合致する一方のみです。
{{% /alert %}}

利用可能な `TableStyleElementType` の値には、`WholeTable`、`FirstRow`、`LastRow`、`FirstColumn`、`LastColumn`、`GrandTotalRow`、`GrandTotalColumn`、`PageFieldLabels`、および `PageFieldValues` が含まれます。
次の例では、`WholeTable` に細い黒の罫線を持ち、`GrandTotalRow` に太字の赤フォントを持つカスタムピボットスタイルを定義し、`PivotTableStyleName` を介してそれを適用して `.xlsx` として保存します。

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
// 元データを入力: ヘッダー行 + 9行のデータ (A1:C10)
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");
worksheet.getCells().get("A2").putValue("Grape");
worksheet.getCells().get("B2").putValue(2020);
worksheet.getCells().get("C2").putValue(100);
worksheet.getCells().get("A3").putValue("Blueberry");
worksheet.getCells().get("B3").putValue(2020);
worksheet.getCells().get("C3").putValue(200);
worksheet.getCells().get("A4").putValue("Kiwi");
worksheet.getCells().get("B4").putValue(2020);
worksheet.getCells().get("C4").putValue(300);
worksheet.getCells().get("A5").putValue("Cherry");
worksheet.getCells().get("B5").putValue(2020);
worksheet.getCells().get("C5").putValue(400);
worksheet.getCells().get("A6").putValue("Grape");
worksheet.getCells().get("B6").putValue(2021);
worksheet.getCells().get("C6").putValue(500);
worksheet.getCells().get("A7").putValue("Blueberry");
worksheet.getCells().get("B7").putValue(2021);
worksheet.getCells().get("C7").putValue(600);
worksheet.getCells().get("A8").putValue("Kiwi");
worksheet.getCells().get("B8").putValue(2021);
worksheet.getCells().get("C8").putValue(700);
worksheet.getCells().get("A9").putValue("Cherry");
worksheet.getCells().get("B9").putValue(2021);
worksheet.getCells().get("C9").putValue(800);
worksheet.getCells().get("A10").putValue("Grape");
worksheet.getCells().get("B10").putValue(2021);
worksheet.getCells().get("C10").putValue(900);
// A1:C10 をソースとするピボットテーブルを E3 に「Pivot1」という名前で追加
let pivotIndex = worksheet.getPivotTables().add("A1:C10", "E3", "Pivot1");
let pivotTable = worksheet.getPivotTables().get(pivotIndex);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
// ステップ 1: 新しいカスタムピボットテーブルスタイルを登録し、そのインデックスを取得
let styleIndex = workbook.getWorksheets().getTableStyles().addPivotTableStyle("CustomPivotStyle");
let tableStyle = workbook.getWorksheets().getTableStyles().get(styleIndex);
// ステップ 2: WholeTable 要素を追加し、4辺すべてに細い黒の罫線を適用
let wholeTableElementIndex = tableStyle.getTableStyleElements().add(AsposeCells.TableStyleElementType.WholeTable);
let wholeTableElement = tableStyle.getTableStyleElements().get(wholeTableElementIndex);
let wholeTableStyle = workbook.createStyle();
wholeTableStyle.getBorders().get(AsposeCells.BorderType.TopBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
wholeTableStyle.getBorders().get(AsposeCells.BorderType.TopBorder).setColor(AsposeCells.Color.Black);
wholeTableStyle.getBorders().get(AsposeCells.BorderType.BottomBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
wholeTableStyle.getBorders().get(AsposeCells.BorderType.BottomBorder).setColor(AsposeCells.Color.Black);
wholeTableStyle.getBorders().get(AsposeCells.BorderType.LeftBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
wholeTableStyle.getBorders().get(AsposeCells.BorderType.LeftBorder).setColor(AsposeCells.Color.Black);
wholeTableStyle.getBorders().get(AsposeCells.BorderType.RightBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
wholeTableStyle.getBorders().get(AsposeCells.BorderType.RightBorder).setColor(AsposeCells.Color.Black);
wholeTableElement.setElementStyle(wholeTableStyle);
// ステップ 3: GrandTotalRow 要素を追加し、太字の赤いフォントを適用
let grandTotalElementIndex = tableStyle.getTableStyleElements().add(AsposeCells.TableStyleElementType.GrandTotalRow);
let grandTotalElement = tableStyle.getTableStyleElements().get(grandTotalElementIndex);
let grandTotalStyle = workbook.createStyle();
grandTotalStyle.getFont().setIsBold(true);
grandTotalStyle.getFont().setColor(AsposeCells.Color.Red);
grandTotalElement.setElementStyle(grandTotalStyle);
// ステップ 4: 名前でカスタムスタイルを適用 (PivotTableStyleType ではなく、これは組み込みプリセット用)
pivotTable.setPivotTableStyleName("CustomPivotStyle");
workbook.save("output.xlsx");
```

## **FormatAll を使用してすべてのピボットセルに 1 つのスタイルを適用する**
`PivotTable.FormatAll(Style)` は、データ領域、行と列のヘッダー、および集計を含む、ピボットテーブルのすべてのセルに単一の `Style` オブジェクトを適用するショートカットです。`PivotTableStyleType` または `PivotTableStyleName` を介して以前に設定された内容はすべて上書きされます。

{{% alert color="primary" %}}
`FormatAll` は、`PivotTableStyleType` と `PivotTableStyleName` の両方を上書きします。ピボットテーブル全体にわたり、テーマ非依存の均一な外観が必要な場合にのみ使用してください。
{{% /alert %}}

次の例では、黄色の単色塗りつぶし、太字の濃紺フォント、および全辺に細い黒の罫線を持つ `Style` を作成し、`FormatAll` で適用して `.xlsx` として保存します。

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
// ソースデータを入力: ヘッダー行（1行目）+ 9行のデータ（2～10行目）
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");
worksheet.getCells().get("A2").putValue("Grape");
worksheet.getCells().get("B2").putValue(2020);
worksheet.getCells().get("C2").putValue(5000);
worksheet.getCells().get("A3").putValue("Blueberry");
worksheet.getCells().get("B3").putValue(2020);
worksheet.getCells().get("C3").putValue(3000);
worksheet.getCells().get("A4").putValue("Kiwi");
worksheet.getCells().get("B4").putValue(2020);
worksheet.getCells().get("C4").putValue(4000);
worksheet.getCells().get("A5").putValue("Cherry");
worksheet.getCells().get("B5").putValue(2020);
worksheet.getCells().get("C5").putValue(2000);
worksheet.getCells().get("A6").putValue("Grape");
worksheet.getCells().get("B6").putValue(2021);
worksheet.getCells().get("C6").putValue(6000);
worksheet.getCells().get("A7").putValue("Blueberry");
worksheet.getCells().get("B7").putValue(2021);
worksheet.getCells().get("C7").putValue(3500);
worksheet.getCells().get("A8").putValue("Kiwi");
worksheet.getCells().get("B8").putValue(2021);
worksheet.getCells().get("C8").putValue(4500);
worksheet.getCells().get("A9").putValue("Cherry");
worksheet.getCells().get("B9").putValue(2021);
worksheet.getCells().get("C9").putValue(2500);
worksheet.getCells().get("A10").putValue("Grape");
worksheet.getCells().get("B10").putValue(2021);
worksheet.getCells().get("C10").putValue(5500);
// ピボット表の追加: ソース範囲 A1:C10、配置先のセル E3、名前 "Pivot1"
let pivotIndex = worksheet.getPivotTables().add("A1:C10", "E3", "Pivot1");
let pivotTable = worksheet.getPivotTables().get(pivotIndex);
// ピボットフィールドの割り当て: Fruit → 行エリア、Year → 列エリア、Amount → データエリア
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
// ピボット表の全セルに強制適用するスタイルを作成
let style = workbook.createStyle();
style.setForegroundColor(AsposeCells.Color.Yellow);
style.setPattern(AsposeCells.BackgroundType.Solid);
style.getFont().setIsBold(true);
style.getFont().setColor(AsposeCells.Color.DarkBlue);
style.getBorders().get(AsposeCells.BorderType.TopBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
style.getBorders().get(AsposeCells.BorderType.TopBorder).setColor(AsposeCells.Color.Black);
style.getBorders().get(AsposeCells.BorderType.BottomBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
style.getBorders().get(AsposeCells.BorderType.BottomBorder).setColor(AsposeCells.Color.Black);
style.getBorders().get(AsposeCells.BorderType.LeftBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
style.getBorders().get(AsposeCells.BorderType.LeftBorder).setColor(AsposeCells.Color.Black);
style.getBorders().get(AsposeCells.BorderType.RightBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
style.getBorders().get(AsposeCells.BorderType.RightBorder).setColor(AsposeCells.Color.Black);
// FormatAll を適用: この単一のスタイルをピボット表の全セルに強制し、
// 既に設定されている PivotTableStyleType / PivotTableStyleName を上書きします
pivotTable.formatAll(style);
// ワークブックを最新の .xlsx 形式で保存
workbook.save("output.xlsx");
```

## **どのスタイル API を使用すべきか？**
スタイル API の選択は、保存先のファイル形式によって異なります。以下の表をクイックリファレンスとしてご活用ください。
| 保存先のファイル形式 | 使用する API | 備考 |
|---|---|---|
| `.xls`（レガシー） | `PivotTable.AutoFormatType` | `Aspose.Cells.Pivot.PivotTableAutoFormatType` の値（例：`Report1`～`Report10`、`Classic`、`Table1`～`Table10`）。最新の形式で保存する場合は無視されます。 |
| `.xlsx` / `.xlsm` / `.xlsb`（最新の組み込みスタイル） | `PivotTable.PivotTableStyleType` | `Aspose.Cells.PivotTableStyleType` の値（明/暗テーマ、Excel 2017 で追加されたものを含む）。 |
| `.xlsx` / `.xlsm` / `.xlsb`（最新のカスタムスタイル） | `PivotTable.PivotTableStyleName` + `Worksheets.TableStyles.AddPivotTableStyle(...)` | 組み込みのプリセットでは不十分な場合に使用します。`TableStyleElement.SetElementStyle(...)` を介して構成します。 |
| 任意の形式（一律の上書き） | `PivotTable.FormatAll(Style)` | ピボットテーブル全体にわたって他のすべてのスタイル設定を上書きするショートカット。 |
迷った場合は、`.xlsx` として保存し、組み込みテーマには `PivotTableStyleType` を、カスタムテーマには `PivotTableStyleName` を使用してください。

{{< app/cells/assistant language="nodejs-cpp" >}}