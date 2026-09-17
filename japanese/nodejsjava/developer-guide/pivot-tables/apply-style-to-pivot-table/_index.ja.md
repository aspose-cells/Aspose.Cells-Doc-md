---
title: Aspose.Cells for Node.js via Java でピボットテーブルにスタイルを適用する
linktitle: Aspose.Cells for Node.js via Java でピボットテーブルにスタイルを適用する
description: Aspose.Cells for Node.js via Java でピボットテーブルに組み込みスタイルとカスタムスタイルを適用する方法を学びます。従来の XLS 自動書式、Excel 2007 以降のモダンな名前付きスタイル、カスタムピボットテーブルスタイル、FormatAll ショートカットについて説明します。
keywords: Aspose.Cells, Node.js via Java, ピボットテーブルスタイル, PivotTableStyleType, AutoFormatType, FormatAll, カスタムスタイル, PivotTableStyleName, TableStyles
type: docs
weight: 200
url: /ja/nodejs-java/apply-style-to-pivot-table/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells は、従来のピボット自動書式(`.xls` ファイル向け)と、モダンな名前付きまたはカスタムピボットテーブルスタイル(`.xlsx`、`.xlsm`、`.xlsb` ファイル向け)の両方を適用できます。使用する API は、ワークブックの読み込み元ではなく、保存先のファイル形式によって決まります。
{{% /alert %}}

## **はじめに**
Aspose.Cells は、ピボットテーブル用の 2 つの並行スタイル API を提供します。どちらを使用するかは、読み込み元の形式ではなく、ワークブックの保存先形式によって決まります。`.xls` ファイルから読み込んだワークブックを `.xlsx` として再保存する場合、従来のスタイル API ではなく、モダンなスタイル API が適用されます。
- `PivotTable.pivotTableStyleType` は、組み込みの名前付きスタイル(ライトテーマおよびダークテーマ。Excel 2017 で追加されたスタイルを含む)のいずれかを選択します。これらのプリセットは読み取り専用です。
- `PivotTable.pivotTableStyleName` は、`Worksheets.getTableStyles().addPivotTableStyle(...)` を通じて自分で定義したカスタムスタイルを選択します。プリセットで提供される範囲を超えて色、罫線、フォントを変更する必要がある場合は、カスタムスタイルが必要です。
さらに、`PivotTable.formatAll(Style)` は、単一の `Style` オブジェクトをピボットのすべてのセルに適用するショートカットであり、上記のいずれかのスタイル名 API で設定された内容を上書きします。基になるテーマに関係なく統一された外観が必要な場合に便利です。

## **従来の XLS プリセット自動書式を適用する**
`PivotTable.autoFormatType` は、`Aspose.Cells.Pivot.PivotTableAutoFormatType` 列挙体の値を受け取ります。利用可能な値は、`Report1` から `Report10`、`Classic`、`Table1` から `Table10` です。
次の例では、新しいワークブックを読み込み、Fruit/Year/Amount のサンプルデータを設定し、ピボットテーブルを追加して `PivotTableAutoFormatType.Report5` を適用し、結果を `.xls` として保存します。

{{% alert color="primary" %}}
**なぜ列フィールドがないのですか?** Report シリーズの自動書式(`Report1` から `Report10`、`Table1` から `Table10`)は、クラシック Excel で行フィールドと値のみを持つ**一次元のピボットテーブル**用に設計されており、列フィールドヘッダーの組み込みスタイルはありません。ピボットに列フィールドが必要な場合は、[シナリオ 2](#apply-a-modern-named-preset-pivot-table-style) のモダンな `PivotTableStyleType` プリセットを使用してください。これらは、モダン Excel で使用される二次元レイアウト向けに設計されています。
{{% /alert %}}

```javascript
let workbook = new AsposeCells.Workbook();
// 最初のワークシートを取得する
let sheet = workbook.getWorksheets().get(0);
// ソースデータにヘッダー行（Fruit、Year、Amount）を入力する
// および2020年と2021年にわたるgrape、blueberry、kiwi、cherryの9つのデータ行
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
// ソース範囲A1:C10を使用して、宛先セルE3に「Pivot1」という名前のピボットテーブルを追加する
let pivotIndex = sheet.getPivotTables().add("A1:C10", "E3", "Pivot1");
let pivotTable = sheet.getPivotTables().get(pivotIndex);
// フィールドを割り当てる：Fruit → 行、Amount → データ
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Amount");
// レガシーXLSプリセット自動フォーマット「Report5」を適用する
// 注：このプロパティは.xlsとして保存する場合にのみ有効です。
// .xlsx/.xlsm/.xlsbとして保存する場合、ExcelはAutoFormatTypeを無視します
// およびPivotTableStyleType / PivotTableStyleNameで指定されたものを使用します。
pivotTable.setAutoFormatType(AsposeCells.PivotTableAutoFormatType.REPORT_5);
// ワークブックをレガシー.xls形式で保存する
workbook.save("output.xls");
```

## **モダンな名前付きプリセットのピボットテーブルスタイルを適用する**

## **カスタムピボットテーブルスタイルを定義して適用する**
組み込みプリセットは変更できません。色、罫線、フォントを上書きする必要がある場合は、カスタムピボットスタイルを定義する必要があります。ワークフローは 3 つのステップで構成されます。
1. `Worksheets.getTableStyles().addPivotTableStyle(String name)` を使用して、ワークブックの `TableStyles` コレクションにカスタムスタイルを追加します。新しく作成されたスタイルのインデックスが返されます。
2. `TableStyle.tableStyleElements.add(TableStyleElementType)` を通じて要素(`WholeTable` や `GrandTotalRow` など)を追加し、`TableStyleElement.setElementStyle(Style)` を介して各要素に `Style` を割り当てて、スタイルを構成します。
3. `PivotTable.pivotTableStyleName` をスタイルの名前に設定して、カスタムスタイルをピボットに適用します。このプロパティは組み込みプリセットを選択するため、ここでは `pivotTableStyleType` を使用しないでください。

{{% alert color="primary" %}}
`pivotTableStyleName` と `pivotTableStyleType` は互換性がありません。組み込みプリセットには `pivotTableStyleType` を使用し、`addPivotTableStyle` を通じて定義したカスタムスタイルには `pivotTableStyleName` を使用します。両方を設定しても害はありませんが、意図したソースに一致する側のみがレンダリングされます。
{{% /alert %}}

利用可能な `TableStyleElementType` の値には、`WholeTable`、`FirstRow`、`LastRow`、`FirstColumn`、`LastColumn`、`GrandTotalRow`、`GrandTotalColumn`、`PageFieldLabels`、`PageFieldValues` が含まれます。
次の例では、`WholeTable` に細い黒の罫線、`GrandTotalRow` に太字の赤いフォントを持つカスタムピボットスタイルを定義し、`pivotTableStyleName` を介して適用して `.xlsx` として保存します。

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
// ソースデータを設定：ヘッダー行 + 9データ行 (A1:C10)
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
// A1:C10をソースとするピボットテーブルをE3に配置、名前を"Pivot1"とする
let pivotIndex = worksheet.getPivotTables().add("A1:C10", "E3", "Pivot1");
let pivotTable = worksheet.getPivotTables().get(pivotIndex);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Amount");
// ステップ1：新しいカスタムピボットテーブルスタイルを登録し、インデックスを取得する
let styleIndex = workbook.getWorksheets().getTableStyles().addPivotTableStyle("CustomPivotStyle");
let tableStyle = workbook.getWorksheets().getTableStyles().get(styleIndex);
// ステップ2：WholeTable要素を追加し、4辺すべてに細い黒枠線を適用する
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
// ステップ3：GrandTotalRow要素を追加し、太字の赤色フォントを適用する
let grandTotalElementIndex = tableStyle.getTableStyleElements().add(AsposeCells.TableStyleElementType.GRAND_TOTAL_ROW);
let grandTotalElement = tableStyle.getTableStyleElements().get(grandTotalElementIndex);
let grandTotalStyle = workbook.createStyle();
grandTotalStyle.getFont().setBold(true);
grandTotalStyle.getFont().setColor(AsposeCells.Color.RED);
grandTotalElement.setElementStyle(grandTotalStyle);
// ステップ4：名前でカスタムスタイルを適用する（PivotTableStyleTypeではない、これは組み込みプリセット用）
pivotTable.setPivotTableStyleName("CustomPivotStyle");
workbook.save("output.xlsx");
```

## **FormatAll を使用してすべてのピボットセルに 1 つのスタイルを適用する**
`PivotTable.formatAll(Style)` は、ピボットテーブルのすべてのセル(データ領域、行ヘッダーと列ヘッダー、集計を含む)に単一の `Style` オブジェクトを適用するショートカットです。以前に `pivotTableStyleType` または `pivotTableStyleName` を介して設定された内容はすべて上書きされます。

{{% alert color="primary" %}}
`formatAll` は `pivotTableStyleType` と `pivotTableStyleName` の両方を上書きします。ピボット全体でテーマに関係なく統一された外観が必要な場合にのみ使用してください。
{{% /alert %}}

次の例では、黄色の単色塗りつぶし、太字の濃紺フォント、すべての辺に細い黒の罫線を持つ `Style` を作成し、`formatAll` で適用して `.xlsx` として保存します。

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
// ソースデータを入力: ヘッダー行 (1行目) + 9データ行 (2～10行目)
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
// ピボットフィールドを割り当て: Fruit -> 行エリア、Year -> 列エリア、Amount -> データエリア
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
// ピボットテーブルの全セルに強制適用されるStyleを構築
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
// FormatAllを適用: この単一のスタイルをピボットテーブルの全セルに強制適用し、
// 以前に設定された PivotTableStyleType / PivotTableStyleName をすべて上書きします
pivotTable.formatAll(style);
// ワークブックを最新の .xlsx 形式で保存
workbook.save("output.xlsx");
```

## **どのスタイル API を使用すべきか?**
スタイル API の選択は、保存先のファイル形式によって異なります。以下の表をクイックリファレンスとしてご利用ください。
| 保存先のファイル形式 | 使用する API | 注意事項 |
|---|---|---|
| `.xls`(従来形式) | `PivotTable.autoFormatType` | `Aspose.Cells.Pivot.PivotTableAutoFormatType` の値(例: `Report1`–`Report10`、`Classic`、`Table1`–`Table10`)。モダン形式で保存する場合は無視されます。 |
| `.xlsx` / `.xlsm` / `.xlsb`(モダン形式、組み込みスタイル) | `PivotTable.pivotTableStyleType` | `Aspose.Cells.PivotTableStyleType` の値(ライト/ダークテーマ。Excel 2017 で追加されたものを含む)。 |
| `.xlsx` / `.xlsm` / `.xlsb`(モダン形式、カスタムスタイル) | `PivotTable.pivotTableStyleName` + `Worksheets.getTableStyles().addPivotTableStyle(...)` | 組み込みプリセットだけでは不十分な場合に使用します。`TableStyleElement.setElementStyle(...)` を介して設定します。 |
| 任意の形式(統一上書き) | `PivotTable.formatAll(Style)` | ピボット全体の他のすべてのスタイル設定を上書きするショートカットです。 |
判断に迷う場合は、`.xlsx` として保存し、組み込みテーマには `pivotTableStyleType` を、カスタムテーマには `pivotTableStyleName` を使用してください。

{{< app/cells/assistant language="nodejs-java" >}}