---
title: ピボットテーブルへのスタイルの適用
linktitle: ピボットテーブルへのスタイルの適用
description: Aspose.Cells for Node.js via Java でピボットテーブルに組み込みスタイルおよびカスタムスタイルを適用する方法を学びます。従来の XLS オートフォーマット、Excel 2007 以降の名前付きスタイル、カスタムピボットテーブルスタイル、FormatAll ショートカットについて解説します。
keywords: Aspose.Cells Node.js via Java, ピボットテーブル, スタイル, PivotTableStyleType, AutoFormatType, FormatAll, カスタムスタイル, PivotTableStyleName, TableStyles
type: docs
weight: 200
url: /ja/nodejs-java/apply-style-to-pivot-table/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells は、従来のピボットオートフォーマット（`.xls` ファイル向け）と、モダンな名前付きまたはカスタムピボットテーブルスタイル（`.xlsx`、`.xlsm`、`.xlsb` ファイル向け）の両方を適用することをサポートします。使用すべき API は、ワークブックが読み込まれた形式ではなく、保存されるファイル形式によって決まります。

{{% /alert %}}

## **概要**

Aspose.Cells は、ピボットテーブル向けに 2 つの並列スタイル API を提供します。これらの選択は、ワークブックを読み込んだ形式ではなく、保存先のファイル形式によって決まります。`.xls` ファイルから読み込まれたワークブックを `.xlsx` として再保存することができ、その場合は従来の API ではなくモダンなスタイル API が適用されます。

従来の `.xls` 出力の場合は、`PivotTable.autoFormatType` プロパティを `Aspose.Cells.Pivot.PivotTableAutoFormatType` 列挙体と一緒に使用してください。この API は、従来の Excel がピボットテーブル用に提供していたオートフォーマットピッカーに対応します。

モダンな `.xlsx`、`.xlsm`、`.xlsb` 出力の場合は、2 種類のスタイル API が利用可能です。

- `PivotTable.pivotTableStyleType` は、組み込みの名前付きスタイル（Excel 2017 で追加されたスタイルを含むライトテーマおよびダークテーマ）を選択します。これらのプリセットは読み取り専用です。
- `PivotTable.pivotTableStyleName` は、`Worksheets.getTableStyles().addPivotTableStyle(...)` を通じて自分で定義したカスタムスタイルを選択します。プリセットで提供される範囲を超えて色、罫線、フォントを変更したい場合は、カスタムスタイルが必要です。

さらに、`PivotTable.formatAll(Style)` は、単一の `Style` オブジェクトをピボットのすべてのセルに適用するショートカットであり、上記のスタイル名 API を通じて設定された内容をすべて上書きします。これは、基になるテーマに関係なく均一な外観が必要な場合に便利です。

## **従来の XLS プリセットオートフォーマットの適用**

`PivotTable.autoFormatType` は、`Aspose.Cells.Pivot.PivotTableAutoFormatType` 列挙体からの値を受け取ります。利用可能な値は `Report1` から `Report10`、`Classic`、および `Table1` から `Table10` です。

{{% alert color="primary" %}}

`autoFormatType` は、ワークブックが `.xls` として保存される場合にのみ有効です。同じワークブックが `.xlsx`、`.xlsm`、または `.xlsb` として保存される場合、Excel はこのプロパティを無視し、`pivotTableStyleType` および `pivotTableStyleName` の設定にフォールバックします。

{{% /alert %}}

次の例では、新しいワークブックを読み込み、Fruit/Year/Amount のサンプルデータを入力し、ピボットテーブルを追加して `PivotTableAutoFormatType.Report5` を適用し、結果を `.xls` として保存します。

```javascript
let workbook = new AsposeCells.Workbook();

// 最初のワークシートを取得する
let sheet = workbook.getWorksheets().get(0);

// ヘッダー行（Fruit、Year、Amount）を含むソースデータを入力する
// および2020年と2021年にわたるgrape、blueberry、kiwi、cherryをカバーする9つのデータ行
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

// 宛先セルE3に「Pivot1」という名前のピボットテーブルをソース範囲A1:C10を使用して追加する
let pivotIndex = sheet.getPivotTables().add("A1:C10", "E3", "Pivot1");
let pivotTable = sheet.getPivotTables().get(pivotIndex);

// フィールドを割り当てる：Fruit → 行、Year → 列、Amount → データ
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Amount");

// レガシーXLSのプリセット自動フォーマット「Report5」を適用する
// 注：このプロパティは.xlsとして保存する場合にのみ有効です。
// .xlsx/.xlsm/.xlsbとして保存する場合、ExcelはAutoFormatTypeを無視します
// およびPivotTableStyleType / PivotTableStyleNameで指定されたものを使用します。
pivotTable.setAutoFormatType(AsposeCells.PivotTableAutoFormatType.REPORT_5);

// ワークブックをレガシー.xls形式で保存する
workbook.save("output.xls");
```

## **モダンな名前付きプリセットピボットテーブルスタイルの適用**

`PivotTable.pivotTableStyleType` は、`Aspose.Cells.PivotTableStyleType` 列挙体からの値を受け取ります。この列挙体は、ライトテーマの `PivotTableStyleLight1` から `PivotTableStyleLight28`、およびダークテーマの `PivotTableStyleDark1` から `PivotTableStyleDark28` をカバーしています。Excel 2017 で追加されたスタイル（ライトテーマおよびダークテーマの第 2 波）も同じ列挙体からアクセスできます。

これは、モダンなファイル形式に対して推奨される API です。従来のオートフォーマットとは異なり、ここで選択されたスタイルは Excel によって忠実にレンダリングされ、他の Office ツールを介したラウンドトリップでも保持されます。

次の例では、同じ Fruit/Year/Amount データを使用し、同じピボットテーブルを作成し、`PivotTableStyleDark1` を適用して、ワークブックを `.xlsx` として保存します。

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);

// ヘッダー行: 果物 / 年 / 数量
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");

// 果物 / 年 / 数量のデータ9行
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

// "Pivot1" という名前のピボットテーブルを E3 に追加する(データソースは A1:C10)
let pivotIndex = worksheet.getPivotTables().add("A1:C10", "E3", "Pivot1");
let pivotTable = worksheet.getPivotTables().get(pivotIndex);

// ピボットフィールドを割り当てる: Fruit → 行エリア、Year → 列エリア、Amount → データエリア
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Amount");

// モダンな Excel 2007+ の名前付きプリセットピボットスタイルを適用する。
// PivotTableStyleType は .xlsx / .xlsm / .xlsb ファイル用の正しい API である。AutoFormatType は
// これらの形式では Excel によって無視される。PivotTableStyleDark1 はダークテーマ
// ファミリー (PivotTableStyleDark1..PivotTableStyleDark28) に属し、同じ列挙型は
// 新しい Excel 2017 のライト/ダークテーマ (PivotTableStyleLight1..Light28 / Dark1..Dark28) も公開している。
pivotTable.setPivotTableStyleType(AsposeCells.PivotTableStyleType.PIVOT_TABLE_STYLE_DARK_1);

// モダンな .xlsx として保存する — これは PivotTableStyleType が意味を持つ形式である。
workbook.save("output.xlsx");
```

## **カスタムピボットテーブルスタイルの定義と適用**

組み込みのプリセットは変更できません。色、罫線、またはフォントをオーバーライドする必要がある場合は、必ずカスタムピボットスタイルを定義する必要があります。ワークフローは次の 3 つのステップで構成されます。

1. `Worksheets.getTableStyles().addPivotTableStyle(String name)` を介して、ワークブックの `TableStyles` コレクションにカスタムスタイルを追加します。これにより、新しく作成されたスタイルのインデックスが返されます。
2. `TableStyle.tableStyleElements.add(TableStyleElementType)` を通じて要素（`WholeTable` や `GrandTotalRow` など）を追加し、`TableStyleElement.setElementStyle(Style)` を介して各要素に `Style` を割り当てて、スタイルを設定します。
3. `PivotTable.pivotTableStyleName` をスタイルの名前に設定して、カスタムスタイルをピボットに適用します。このプロパティは組み込みプリセットを選択するため、ここでは `pivotTableStyleType` を使用しないでください。

{{% alert color="primary" %}}

`pivotTableStyleName` と `pivotTableStyleType` は互いに置き換え可能ではありません。組み込みプリセットには `pivotTableStyleType` を、`addPivotTableStyle` を通じて定義したカスタムスタイルには `pivotTableStyleName` を使用してください。両方を設定しても問題ありませんが、レンダリングされるのは意図したソースに合致する方のみです。

{{% /alert %}}

利用可能な `TableStyleElementType` の値には、`WholeTable`、`FirstRow`、`LastRow`、`FirstColumn`、`LastColumn`、`GrandTotalRow`、`GrandTotalColumn`、`PageFieldLabels`、および `PageFieldValues` が含まれます。

次の例では、`WholeTable` に細い黒い罫線、`GrandTotalRow` に太字の赤いフォントを持つカスタムピボットスタイルを定義し、`pivotTableStyleName` を介してそれを適用して `.xlsx` として保存します。

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);

// 元データを設定: ヘッダー行 + 9行のデータ (A1:C10)
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

// A1:C10 をデータソースとし、E3 を起点とする "Pivot1" という名前のピボットテーブルを追加
let pivotIndex = worksheet.getPivotTables().add("A1:C10", "E3", "Pivot1");
let pivotTable = worksheet.getPivotTables().get(pivotIndex);

pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Amount");

// ステップ 1: 新しいカスタムピボットテーブルスタイルを登録し、そのインデックスを取得
let styleIndex = workbook.getWorksheets().getTableStyles().addPivotTableStyle("CustomPivotStyle");
let tableStyle = workbook.getWorksheets().getTableStyles().get(styleIndex);

// ステップ 2: WholeTable 要素を追加し、4辺すべてに細い黒い枠線を適用
let wholeTableElementIndex = tableStyle.getTableStyleElements().add(AsposeCells.TableStyleElementType.WHOLE_TABLE);
let wholeTableElement = tableStyle.getTableStyleElements().get(wholeTableElementIndex);
let wholeTableStyle = workbook.createStyle();
let topBorder = wholeTableStyle.getBorders().get(AsposeCells.BorderType.TOP_BORDER);
topBorder.setLineStyle(AsposeCells.CellBorderType.THIN);
topBorder.setColor(AsposeCells.Color.BLACK);

let bottomBorder = wholeTableStyle.getBorders().get(AsposeCells.BorderType.BOTTOM_BORDER);
bottomBorder.setLineStyle(AsposeCells.CellBorderType.THIN);
bottomBorder.setColor(AsposeCells.Color.BLACK);

let leftBorder = wholeTableStyle.getBorders().get(AsposeCells.BorderType.LEFT_BORDER);
leftBorder.setLineStyle(AsposeCells.CellBorderType.THIN);
leftBorder.setColor(AsposeCells.Color.BLACK);

let rightBorder = wholeTableStyle.getBorders().get(AsposeCells.BorderType.RIGHT_BORDER);
rightBorder.setLineStyle(AsposeCells.CellBorderType.THIN);
rightBorder.setColor(AsposeCells.Color.BLACK);

wholeTableElement.setElementStyle(wholeTableStyle);

// ステップ 3: GrandTotalRow 要素を追加し、太字の赤いフォントを適用
let grandTotalElementIndex = tableStyle.getTableStyleElements().add(AsposeCells.TableStyleElementType.GRAND_TOTAL_ROW);
let grandTotalElement = tableStyle.getTableStyleElements().get(grandTotalElementIndex);
let grandTotalStyle = workbook.createStyle();
grandTotalStyle.getFont().setBold(true);
grandTotalStyle.getFont().setColor(AsposeCells.Color.RED);
grandTotalElement.setElementStyle(grandTotalStyle);

// ステップ 4: 名前でカスタムスタイルを適用(組み込みプリセット用の PivotTableStyleType ではなく)
pivotTable.setPivotTableStyleName("CustomPivotStyle");

workbook.save("output.xlsx");
```

## **FormatAll を使用したすべてのピボットセルへの単一スタイルの適用**

`PivotTable.formatAll(Style)` は、単一の `Style` オブジェクトをデータエリア、行と列のヘッダー、および集計を含むピボットテーブルのすべてのセルに適用するショートカットです。`pivotTableStyleType` または `pivotTableStyleName` を介して以前に設定された内容はすべて上書きされます。

{{% alert color="primary" %}}

`formatAll` は `pivotTableStyleType` と `pivotTableStyleName` の両方を上書きします。ピボット全体でテーマに関係なく均一な外観が必要な場合にのみ使用してください。

{{% /alert %}}

次の例では、黄色の単色塗りつぶし、太字のダークブルーフォント、およびすべての辺に細い黒い罫線を持つ `Style` を作成し、それを `formatAll` で適用して `.xlsx` として保存します。

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);

// ソースデータを入力: ヘッダー行（1行目）+ 9行のデータ（2〜10行目）
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

// ピボットテーブルを追加: ソース範囲 A1:C10、配置先セル E3、名前 "Pivot1"
let pivotIndex = worksheet.getPivotTables().add("A1:C10", "E3", "Pivot1");
let pivotTable = worksheet.getPivotTables().get(pivotIndex);

// ピボットフィールドを割り当て: Fruit → 行エリア、Year → 列エリア、Amount → データエリア
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// ピボットテーブルのすべてのセルに強制適用するスタイルを構築
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

// FormatAll を適用: この単一のスタイルをピボットテーブルのすべてのセルに強制適用し、
// 以前に設定された PivotTableStyleType / PivotTableStyleName を上書きする
pivotTable.formatAll(style);

// ワークブックを最新の .xlsx 形式で保存
workbook.save("output.xlsx");
```

## **どのスタイル API を使用すべきですか？**

スタイル API の選択は、保存先のファイル形式によって異なります。以下の表をクイックリファレンスとしてご利用ください。

| 対象のファイル形式 | 使用する API | メモ |
|---|---|---|
| `.xls`（従来形式） | `PivotTable.autoFormatType` | `Aspose.Cells.Pivot.PivotTableAutoFormatType` からの値（例: `Report1`–`Report10`、`Classic`、`Table1`–`Table10`）。モダン形式で保存する場合は無視されます。 |
| `.xlsx` / `.xlsm` / `.xlsb`（モダン形式、組み込みスタイル） | `PivotTable.pivotTableStyleType` | `Aspose.Cells.PivotTableStyleType` からの値（Excel 2017 で追加されたものを含むライト/ダークテーマ）。 |
| `.xlsx` / `.xlsm` / `.xlsb`（モダン形式、カスタムスタイル） | `PivotTable.pivotTableStyleName` + `Worksheets.getTableStyles().addPivotTableStyle(...)` | 組み込みプリセットでは不十分な場合に使用します。`TableStyleElement.setElementStyle(...)` を介して設定します。 |
| 任意の形式（均一なオーバーライド） | `PivotTable.formatAll(Style)` | ピボット全体で他のすべてのスタイル設定をオーバーライドするショートカットです。 |

迷った場合は、`.xlsx` として保存し、組み込みテーマには `pivotTableStyleType` を、カスタムテーマには `pivotTableStyleName` を使用してください。

## **関連記事**

- [Aspose.Cells for Node.js via Java でのピボットテーブルの更新](/cells/ja/nodejs-java/refresh-pivot-table/)

{{< app/cells/assistant language="javascript" >}}