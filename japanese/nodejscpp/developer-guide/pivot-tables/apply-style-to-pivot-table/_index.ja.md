---
title: Aspose.Cells for .NET でピボットテーブルにスタイルを適用する
linktitle: ピボットテーブルにスタイルを適用
description: Aspose.Cells for Node.js via C++でピボットテーブルに組み込みスタイルおよびカスタムスタイルを適用する方法を学びます。レガシーXLSの自動書式、モダンExcel 2007+の名前付きスタイル、カスタムピボットテーブルスタイル、FormatAllショートカットについて解説します。
keywords: Aspose.Cells Node.js via C++ ピボットテーブル スタイル, PivotTableStyleType, AutoFormatType, FormatAll, カスタムスタイル, PivotTableStyleName, TableStyles
type: docs
weight: 200
url: /ja/nodejs-cpp/apply-style-to-pivot-table/
ai_search_scope: cells_nodejs_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---


{{% alert color="primary" %}}

Aspose.Cells は、レガシーのピボットテーブル自動書式（`.xls` ファイル向け）と、モダンな名前付きまたはカスタムのピボットテーブルスタイル（`.xlsx`、`.xlsm`、`.xlsb` ファイル向け）の両方を適用することをサポートします。呼び出すべき API は、ワークブックの読み込み元のフォーマットではなく、保存先のファイルフォーマットによって決まります。

{{% /alert %}}

## **はじめに**

Aspose.Cells は、ピボットテーブル向けに 2 つの並列なスタイル API を提供します。これらの使い分けは、読み込み元のフォーマットではなく、ワークブックの保存先のフォーマットによって決まります。`.xls` ファイルから読み込まれたワークブックを `.xlsx` として再保存する場合、レガシー API ではなく、モダンなスタイル API が適用されます。

レガシーの `.xls` 出力の場合は、`PivotTable.AutoFormatType` プロパティを `Aspose.Cells.Pivot.PivotTableAutoFormatType` 列挙体と共に使用してください。この API は、従来の Excel でピボットテーブル向けに提供されていた自動書式ピッカーに対応します。

モダンの `.xlsx`、`.xlsm`、`.xlsb` 出力の場合は、2 種類のスタイル API が利用可能です。

- `PivotTable.PivotTableStyleType` は、組み込みの名前付きスタイル（ライトテーマおよびダークテーマ。Excel 2017 で追加されたスタイルを含む）のいずれかを選択します。これらのプリセットは読み取り専用です。
- `PivotTable.PivotTableStyleName` は、`Workbook.Worksheets.TableStyles.AddPivotTableStyle(...)` を通じて独自に定義したカスタムスタイルを選択します。プリセットで提供される範囲を超えて、色、罫線、フォントをカスタマイズする場合は、カスタムスタイルが必要です。

さらに、`PivotTable.FormatAll(Style)` は、単一の `Style` オブジェクトをピボットのすべてのセルに適用するショートカットであり、上記いずれかのスタイル名 API で行った設定をすべて上書きします。これは、基盤となるテーマに関係なく均一な外観が必要な場合に便利です。

## **レガシー XLS プリセット自動書式の適用**

`PivotTable.AutoFormatType` は、`Aspose.Cells.Pivot.PivotTableAutoFormatType` 列挙体の値を受け取ります。利用可能な値は `Report1` から `Report10`、`Classic`、`Table1` から `Table10` です。

{{% alert color="primary" %}}

`AutoFormatType` は、ワークブックが `.xls` として保存される場合にのみ有効です。同じワークブックが `.xlsx`、`.xlsm`、または `.xlsb` として保存される場合、Excel はこのプロパティを無視し、`PivotTableStyleType` および `PivotTableStyleName` の設定にフォールバックします。

{{% /alert %}}

次の例では、新しいワークブックを読み込み、Fruit/Year/Amount のサンプルデータを入力し、ピボットテーブルを追加して、`PivotTableAutoFormatType.Report5` を適用し、結果を `.xls` として保存します。

{{% alert color="primary" %}}

**列フィールドがないのはなぜですか？** Report シリーズの自動書式（`Report1`〜`Report10`、`Table1`〜`Table10`）は、従来の Excel で**単一次元のピボットテーブル**（行フィールドと値のみ）のために設計されたものであり、列フィールドのヘッダーに対する組み込みのスタイル設定はありません。ピボットテーブルに列フィールドが必要な場合は、代わりに下のシナリオ 2 のモダンな `PivotTableStyleType` プリセットを使用してください。これらはモダンな Excel が使用する二次元レイアウト向けに設計されています。

{{% /alert %}}

```javascript
const AsposeCells = require("aspose.cells");

// シナリオ 1: レガシー XLS プリセット自動フォーマットを適用する
// 使用中の API: PivotTable.AutoFormatType
// 対象ファイル形式: .xls（レガシー）
// 完全なサンプルとデータファイルについては、https://github.com/aspose-cells/Aspose.Cells-for-.NET を参照してください

// 新しいワークブックを作成
const workbook = new AsposeCells.Workbook();

// 最初のワークシートを取得
const sheet = workbook.getWorksheets().get(0);

// ヘッダー行（Fruit、Year、Amount）と、
// 2020年と2021年にわたる grape、blueberry、kiwi、cherry の9行のデータでソースデータを設定
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

// セル E3 に「Pivot1」という名前のピボットテーブルをソース範囲 A1:C10 を使用して追加
const pivotIndex = sheet.getPivotTables().add("A1:C10", "E3", "Pivot1");
const pivotTable = sheet.getPivotTables().get(pivotIndex);

// フィールドを割り当て: Fruit → 行、Year → 列、Amount → データ
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// レガシー XLS プリセット自動フォーマット「Report5」を適用
// 注意: このプロパティは .xls 形式で保存する場合にのみ有効です。
// .xlsx/.xlsm/.xlsb として保存する場合、Excel は AutoFormatType を無視し、
// PivotTableStyleType / PivotTableStyleName で指定されたものを使用します。
pivotTable.setAutoFormatType(AsposeCells.PivotTableAutoFormatType.Report5);

// ワークブックをレガシー .xls 形式で保存
workbook.save("output.xls");
```

## **モダンの名前付きプリセットピボットテーブルスタイルの適用**

`PivotTable.PivotTableStyleType` は、`Aspose.Cells.PivotTableStyleType` 列挙体の値を受け取ります。この列挙体は、ライトテーマの `PivotTableStyleLight1` から `PivotTableStyleLight28`、およびダークテーマの `PivotTableStyleDark1` から `PivotTableStyleDark28` を網羅しています。Excel 2017 で追加されたスタイル（ライトテーマおよびダークテーマの第二波）も、同じ列挙体からアクセスできます。

これは、モダンなファイルフォーマットに対して推奨される API です。レガシーの自動書式と異なり、ここで選択されたスタイルは Excel によって忠実にレンダリングされ、他の Office ツールとのラウンドトリップでも保持されます。

次の例では、同じ Fruit/Year/Amount データを使用して、同じピボットテーブルを作成し、`PivotTableStyleDark1` を適用し、ワークブックを `.xlsx` として保存します。

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);

// ヘッダー行: 果物 / 年 / 金額
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");

// 果物 / 年 / 金額の9つのデータ行
worksheet.getCells().get("A2").putValue("Grape");
worksheet.getCells().get("B2").putValue(2020);
worksheet.getCells().get("C2").putValue(100);

worksheet.getCells().get("A3").putValue("Blueberry");
worksheet.getCells().get("B3").putValue(2020);
worksheet.getCells().get("C3").putValue(150);

worksheet.getCells().get("A4").putValue("Kiwi");
worksheet.getCells().get("B4").putValue(2020);
worksheet.getCells().get("C4").putValue(200);

worksheet.getCells().get("A5").putValue("Cherry");
worksheet.getCells().get("B5").putValue(2020);
worksheet.getCells().get("C5").putValue(180);

worksheet.getCells().get("A6").putValue("Grape");
worksheet.getCells().get("B6").putValue(2021);
worksheet.getCells().get("C6").putValue(120);

worksheet.getCells().get("A7").putValue("Blueberry");
worksheet.getCells().get("B7").putValue(2021);
worksheet.getCells().get("C7").putValue(170);

worksheet.getCells().get("A8").putValue("Kiwi");
worksheet.getCells().get("B8").putValue(2021);
worksheet.getCells().get("C8").putValue(210);

worksheet.getCells().get("A9").putValue("Cherry");
worksheet.getCells().get("B9").putValue(2021);
worksheet.getCells().get("C9").putValue(190);

worksheet.getCells().get("A10").putValue("Grape");
worksheet.getCells().get("B10").putValue(2021);
worksheet.getCells().get("C10").putValue(130);

// E3に「Pivot1」という名前のピボットテーブルを追加し、データソースはA1:C10
let pivotIndex = worksheet.getPivotTables().add("A1:C10", "E3", "Pivot1");
let pivotTable = worksheet.getPivotTables().get(pivotIndex);

// ピボットフィールドを割り当て: 果物 → 行エリア、年 → 列エリア、金額 → データエリア
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// モダンなExcel 2007+の名前付きプリセットピボットスタイルを適用する。
// PivotTableStyleTypeは.xlsx / .xlsm / .xlsbファイル用の正しいAPIであり、
// AutoFormatTypeはこれらの形式ではExcelに無視される。
// PivotTableStyleDark1はダークテーマファミリー
// (PivotTableStyleDark1..PivotTableStyleDark28)に属し、同じ列挙型には
// 新しいExcel 2017のライト/ダークテーマ
// (PivotTableStyleLight1..Light28 / Dark1..Dark28)も含まれている。
pivotTable.setPivotTableStyleType(AsposeCells.PivotTableStyleType.PivotTableStyleDark1);

// モダンな.xlsxとして保存する — これはPivotTableStyleTypeが意味を持つ形式である。
workbook.save("output.xlsx");
```

## **カスタムピボットテーブルスタイルの定義と適用**

組み込みのプリセットは変更できません。色、罫線、フォントを上書きする必要がある場合は、必ずカスタムピボットスタイルを定義する必要があります。ワークフローは次の 3 ステップで構成されます。

1. `Workbook.Worksheets.TableStyles.AddPivotTableStyle(string name)` を通じて、ワークブックの `TableStyles` コレクションにカスタムスタイルを追加します。これにより、新しく作成されたスタイルのインデックスが返されます。
2. `TableStyle.TableStyleElements.Add(TableStyleElementType)` で要素（`WholeTable` や `GrandTotalRow` など）を追加し、`TableStyleElement.SetElementStyle(Style)` を通じて各要素に `Style` を割り当てることで、スタイルを設定します。
3. `PivotTable.PivotTableStyleName` をそのスタイルの名前に設定することで、カスタムスタイルをピボットに適用します。このプロパティは組み込みプリセットを選択するものであるため、ここでは `PivotTableStyleType` を使用しないでください。

{{% alert color="primary" %}}

`PivotTableStyleName` と `PivotTableStyleType` は互いに置き換えできません。組み込みプリセットには `PivotTableStyleType` を、`AddPivotTableStyle` で定義したカスタムスタイルには `PivotTableStyleName` を使用してください。両方設定しても問題ありませんが、想定したソースと一致する側のみがレンダリングされます。

{{% /alert %}}

利用可能な `TableStyleElementType` の値には、`WholeTable`、`FirstRow`、`LastRow`、`FirstColumn`、`LastColumn`、`GrandTotalRow`、`GrandTotalColumn`、`PageFieldLabels`、`PageFieldValues` が含まれます。

次の例では、`WholeTable` に細い黒色の罫線を持ち、`GrandTotalRow` に太字の赤色フォントを持つカスタムピボットスタイルを定義し、`PivotTableStyleName` を通じてそれを適用して、`.xlsx` として保存します。

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);

// ソースデータを入力: ヘッダー行 + 9 データ行 (A1:C10)
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");

worksheet.getCells().get("A2").putValue("Grape");
worksheet.getCells().get("B2").putValue(2020_Cells").get("C2").putValue(100);

worksheet.getCells().get("A3").putValue("Blueberry");
worksheet.getCells().get("B3").putValue(2020_Cells").get("C3").putValue(200);

worksheet.getCells().get("A4").putValue("Kiwi");
worksheet.getCells().get("B4").putValue(2020_Cells").get("C4").putValue(300);

worksheet.getCells().get("A5").putValue("Cherry");
worksheet.getCells().get("B5").putValue(2020_Cells").get("C5").putValue(400);

worksheet.getCells().get("A6").putValue("Grape");
worksheet.getCells().get("B6").putValue(2021_Cells").get("C6").putValue(500);

worksheet.getCells().get("A7").putValue("Blueberry");
worksheet.getCells().get("B7").putValue(2021_Cells").get("C7").putValue(600);

worksheet.getCells().get("A8").putValue("Kiwi");
worksheet.getCells().get("B8").putValue(2021_Cells").get("C8").putValue(700);

worksheet.getCells().get("A9").putValue("Cherry");
worksheet.getCells().get("B9").putValue(2021_Cells").get("C9").putValue(800);

worksheet.getCells().get("A10").putValue("Grape");
worksheet.getCells().get("B10").putValue(2021_Cells").get("C10").putValue(900);

// ピボットテーブルを追加: ソース A1:C10、配置 E3、名前 "Pivot1"
let pivotIndex = worksheet.getPivotTables().add("A1:C10", "E3", "Pivot1");
let pivotTable = worksheet.getPivotTables().get(pivotIndex);

pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// ステップ 1: 新しいカスタム ピボットテーブル スタイルを登録し、インデックスを取得する
let styleIndex = workbook.getWorksheets().getTableStyles().addPivotTableStyle("CustomPivotStyle");
let tableStyle = workbook.getWorksheets().getTableStyles().get(styleIndex);

// ステップ 2: WholeTable 要素を追加し、4 辺すべてに細い黒い罫線を適用する
let wholeTableElementIndex = tableStyle.getTableStyleElements().add(AsposeCells.TableStyleElementType.WholeTable));
let wholeTableElement = tableStyle.getTableStyleElements().get(wholeTableElementIndex_Workbook.createStyle();
wholeTableStyle.getBorders().get(AsposeCells.BorderType.TopBorder).setLineStyle(AsposeCells.CellBorderType.Thin));
wholeTableStyle.getBorders().get(AsposeCells.BorderType.TopBorder).setColor(AsposeCells.Color.Black));
wholeTableStyle.getBorders().get(AsposeCells.BorderType.BottomBorder).setLineStyle(AsposeCells.CellBorderType.Thin));
wholeTableStyle.getBorders().get(AsposeCells.BorderType.BottomBorder).setColor(AsposeCells.Color.Black));
wholeTableStyle.getBorders().get(AsposeCells.BorderType.LeftBorder).setLineStyle(AsposeCells.CellBorderType.Thin));
wholeTableStyle.getBorders().get(AsposeCells.BorderType.LeftBorder).setColor(AsposeCells.Color.Black));
wholeTableStyle.getBorders().get(AsposeCells.BorderType.RightBorder).setLineStyle(AsposeCells.CellBorderType.Thin));
wholeTableStyle.getBorders().get(AsposeCells.BorderType.RightBorder).setColor(AsposeCells.Color.Black));
wholeTableElement.setElementStyle(wholeTableStyle);

// ステップ 3: GrandTotalRow 要素を追加し、太字の赤いフォントを適用する
let grandTotalElementIndex = tableStyle.getTableStyleElements().add(AsposeCells.TableStyleElementType.GrandTotalRow));
let grandTotalElement = tableStyle.getTableStyleElements().get(grandTotalElementIndex_Workbook.createStyle();
grandTotalStyle.getFont().setIsBold(true));
grandTotalStyle.getFont().setColor(AsposeCells.Color.Red));
grandTotalElement.setElementStyle(grandTotalStyle);

// ステップ 4: カスタム スタイルを名前で適用する (組み込みプリセット用の PivotTableStyleType ではなく、名前で指定する点に注意)
pivotTable.setPivotTableStyleName("CustomPivotStyle");

workbook.save("output.xlsx");
```

## **FormatAll を使用して 1 つのスタイルをすべてのピボットセルに適用**

`PivotTable.FormatAll(Style)` は、データ領域、行と列のヘッダー、および集計を含む、ピボットテーブルのすべてのセルに単一の `Style` オブジェクトを適用するショートカットです。`PivotTableStyleType` または `PivotTableStyleName` を通じて以前に設定された内容はすべて上書きされます。

{{% alert color="primary" %}}

`FormatAll` は `PivotTableStyleType` と `PivotTableStyleName` の両方を上書きします。ピボット全体にわたって、テーマに依存しない均一な外観が必要な場合にのみ使用してください。

{{% /alert %}}

次の例では、黄色の単色塗りつぶし、太字の濃紺フォント、およびすべての辺に細い黒色の罫線を持つ `Style` を作成し、それを `FormatAll` で適用して、`.xlsx` として保存します。

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);

// ソースデータを入力する：ヘッダー行（1行目）+ データ9行（2～10行目）
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");

worksheet.getCells().get("A2").putValue("Grape");
worksheet.getCells().get("B2").putValue(2020).putValue(2020);

worksheet.getCells().get("A3").putValue("Blueberry");
worksheet.getCells().get("B3").putValue(2020);

worksheet.getCells().get("A4").putValue("Kiwi");
worksheet.getCells().get("B4").putValue(2020);

worksheet.getCells().get("A5").putValue("Cherry");
worksheet.getCells().get("B5").putValue(2020);

worksheet.getCells().get("A6").putValue("Grape");
worksheet.getCells().get("B6").putValue(2021);

worksheet.getCells().get("A7").putValue("Blueberry");
worksheet.getCells().get("B7").putValue(2021);

worksheet.getCells().get("A8").putValue("Kiwi");
worksheet.getCells().get("B8").putValue(2021);

worksheet.getCells().get("A9").putValue("Cherry");
worksheet.getCells().get("B9").putValue(2021);

worksheet.getCells().get("A10").putValue("Grape");
worksheet.getCells().get("B10").putValue(2021);

let pivotIndex = worksheet.getPivotTables().add("A1:C10", "E3", "Pivot1");
let pivotTable = worksheet.getPivotTables().get(pivotIndex);

pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// ピボットテーブルのすべてのセルに強制的に適用される Style を作成する
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

// FormatAll を適用する：この単一のスタイルをピボットテーブルのすべてのセルに強制的に適用し、
// 以前に設定された PivotTableStyleType / PivotTableStyleName をすべて上書きする
pivotTable.formatAll(style);

// ワークブックを最新の .xlsx 形式で保存する
workbook.save("output.xlsx");
```

## **どのスタイル API を使用すべきか？**

スタイル API の選択は、保存先のファイルフォーマットによって決まります。次の表をクイックリファレンスとしてご利用ください。

| 保存先のファイルフォーマット | 使用する API | メモ |
|---|---|---|
| `.xls`（レガシー） | `PivotTable.AutoFormatType` | `Aspose.Cells.Pivot.PivotTableAutoFormatType` の値（例：`Report1`–`Report10`、`Classic`、`Table1`–`Table10`）。モダンなフォーマットで保存する場合は無視されます。 |
| `.xlsx` / `.xlsm` / `.xlsb`（モダン、組み込みスタイル） | `PivotTable.PivotTableStyleType` | `Aspose.Cells.PivotTableStyleType` の値（ライト／ダークテーマ。Excel 2017 で追加されたものを含む）。 |
| `.xlsx` / `.xlsm` / `.xlsb`（モダン、カスタムスタイル） | `PivotTable.PivotTableStyleName` + `Worksheets.TableStyles.AddPivotTableStyle(...)` | 組み込みプリセットでは不十分な場合に使用します。`TableStyleElement.SetElementStyle(...)` を通じて設定します。 |
| 任意のフォーマット（均一な上書き） | `PivotTable.FormatAll(Style)` | ピボット全体にわたる他のすべてのスタイル設定を上書きするショートカット。 |

迷った場合は、`.xlsx` として保存し、組み込みテーマには `PivotTableStyleType` を、カスタムテーマには `PivotTableStyleName` を使用してください。

## **関連記事**

- [Refreshing Pivot Tables in Aspose.Cells for Node.js via C++](/cells/ja/nodejs-cpp/refresh-pivot-table/)

{{< app/cells/assistant language="javascript" >}}
