---
title: ピボットテーブルへのスタイルの適用
linktitle: ピボットテーブルへのスタイルの適用
description: Aspose.Cells for Java でピボットテーブルに組み込みスタイルとカスタムスタイルを適用する方法を学びます。レガシー XLS の自動書式、Excel 2007+ のモダンな名前付きスタイル、カスタム ピボットテーブル スタイル、FormatAll ショートカットについて説明します。
keywords: Aspose.Cells, Java, ピボットテーブル, スタイル, PivotTableStyleType, AutoFormatType, FormatAll, カスタムスタイル, PivotTableStyleName, TableStyles
type: docs
weight: 200
url: /ja/java/apply-style-to-pivot-table/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells は、レガシーのピボット自動書式（`.xls` ファイル向け）と、モダンな名前付きまたはカスタム ピボットテーブル スタイル（`.xlsx`、`.xlsm`、`.xlsb` ファイル向け）の両方をサポートします。使用する API は、ワークブックの読み込み元の形式ではなく、保存先のファイル形式によって決まります。

{{% /alert %}}

## **はじめに**

Aspose.Cells は、ピボットテーブル向けに 2 つの並列スタイル API を提供します。これらの選択は、読み込み元の形式ではなく、ワークブックの保存先の形式によって決まります。`.xls` ファイルから読み込んだワークブックを `.xlsx` として再保存する場合、レガシー API ではなく、モダン スタイルの API が適用されます。

レガシー `.xls` 出力の場合は、`PivotTable.AutoFormatType` プロパティと `com.aspose.cells.PivotTableAutoFormatType` 列挙型を使用します。この API は、クラシック Excel がピボットテーブル用に提供していた自動書式ピッカーに対応します。

モダンな `.xlsx`、`.xlsm`、`.xlsb` 出力の場合、2 種類のスタイル API が利用可能です。

- `PivotTable.PivotTableStyleType` は組み込みの名前付きスタイル（明暗テーマ、Excel 2017 で追加されたスタイルを含む）のいずれかを選択します。これらのプリセットは読み取り専用です。
- `PivotTable.PivotTableStyleName` は、`Workbook.getWorksheets().getTableStyles().addPivotTableStyle(...)` を通じて自分で定義したカスタムスタイルを選択します。プリセットで提供される色、罫線、フォント以外を変更したい場合は、カスタムスタイルが必要です。

さらに、`PivotTable.formatAll(Style)` は、単一の `Style` オブジェクトをピボットのすべてのセルに適用するショートカットで、上記のいずれかのスタイル名 API で設定された内容を上書きします。これは、基になるテーマに関係なく統一された外観が必要な場合に役立ちます。

## **レガシー XLS プリセット自動書式の適用**

`PivotTable.AutoFormatType` は、`com.aspose.cells.PivotTableAutoFormatType` 列挙型の値を受け取ります。利用可能な値は `REPORT_1` ～ `REPORT_10`、`CLASSIC`、および `TABLE_1` ～ `TABLE_10` です。

{{% alert color="primary" %}}

`AutoFormatType` が有効になるのは、ワークブックが `.xls` として保存される場合のみです。同じワークブックを `.xlsx`、`.xlsm`、または `.xlsb` として保存すると、Excel はこのプロパティを無視し、`PivotTableStyleType` と `PivotTableStyleName` の設定にフォールバックします。

{{% /alert %}}

次の例では、新しいワークブックを読み込み、Fruit/Year/Amount のサンプル データを入力し、ピボットテーブルを追加して `PivotTableAutoFormatType.REPORT_5` を適用し、結果を `.xls` として保存します。

```java
import com.aspose.cells.*;

// シナリオ 1: レガシー XLS プリセット自動書式を適用する
// 使用中の API: PivotTable.AutoFormatType
// 対象ファイル形式: .xls (レガシー)
// 完全なサンプルとデータファイルについては、https://github.com/aspose-cells/Aspose.Cells-for-Java を参照してください

// 新しいワークブックを作成する
Workbook workbook = new Workbook();

// 最初のワークシートを取得する
Worksheet sheet = workbook.getWorksheets().get(0);

// ヘッダー行 (Fruit, Year, Amount) を含むソースデータを入力する
// および 2020 年と 2021 年の grape、blueberry、kiwi、cherry を含む 9 行のデータ
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

// 出力先セル E3 に "Pivot1" という名前のピボットテーブルをソース範囲 A1:C10 を使用して追加する
int pivotIndex = sheet.getPivotTables().add("A1:C10", "E3", "Pivot1");
PivotTable pivotTable = sheet.getPivotTables().get(pivotIndex);

// フィールドを割り当てる: Fruit -> 行、Year -> 列、Amount -> データ
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");

// レガシー XLS プリセット自動書式 "Report5" を適用する
// 注意: このプロパティは .xls として保存する場合にのみ有効です。
// .xlsx/.xlsm/.xlsb として保存する場合、Excel は AutoFormatType を無視し、
// PivotTableStyleType / PivotTableStyleName で指定されたものを使用します。
pivotTable.setAutoFormatType(PivotTableAutoFormatType.REPORT_5);

// ワークブックをレガシー .xls 形式で保存する
workbook.save("output.xls");
```

## **モダンな名前付きプリセット ピボットテーブル スタイルの適用**

`PivotTable.PivotTableStyleType` は、`com.aspose.cells.PivotTableStyleType` 列挙型の値を受け取ります。この列挙型には、明テーマ `PIVOT_TABLE_STYLE_LIGHT_1` ～ `PIVOT_TABLE_STYLE_LIGHT_28` および暗テーマ `PIVOT_TABLE_STYLE_DARK_1` ～ `PIVOT_TABLE_STYLE_DARK_28` が含まれます。Excel 2017 で追加されたスタイル（明暗テーマの第二弾）も同じ列挙型からアクセスできます。

これは、モダン ファイル形式に対して推奨される API です。レガシーの自動書式とは異なり、ここで選択したスタイルは Excel によって忠実にレンダリングされ、他の Office ツールとのラウンドトリップでも保持されます。

次の例では、同じ Fruit/Year/Amount データを使用し、同一のピボットテーブルを作成して `PIVOT_TABLE_STYLE_DARK_1` を適用し、ワークブックを `.xlsx` として保存します。

```java
import com.aspose.cells.*;

// シナリオ 2: モダンな Excel 2007+ の名前付きプリセット ピボットスタイルを適用する
// 使用中の API: PivotTable.PivotTableStyleType
// 対象ファイル形式: .xlsx / .xlsm / .xlsb
// 完全なサンプルとデータファイルについては、https://github.com/aspose-cells/Aspose.Cells-for-Java を参照してください

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);

// ヘッダー行: 果物 / 年 / 金額
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");

// 果物 / 年 / 金額の9行のデータ
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
int pivotIndex = worksheet.getPivotTables().add("A1:C10", "E3", "Pivot1");
PivotTable pivotTable = worksheet.getPivotTables().get(pivotIndex);

// ピボットフィールドを割り当て: 果物 → 行エリア、年 → 列エリア、金額 → データエリア
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");

// モダンな Excel 2007+ の名前付きプリセットのピボットスタイルを適用します。
// PivotTableStyleType は .xlsx / .xlsm / .xlsb ファイル用の正しい API です。
// これらの形式では AutoFormatType は Excel によって無視されます。
pivotTable.setPivotTableStyleType(PivotTableStyleType.PIVOT_TABLE_STYLE_DARK_1);

// 最新の .xlsx として保存 - これは PivotTableStyleType が意味を持つ形式です。
workbook.save("output.xlsx");
```

## **カスタム ピボットテーブル スタイルの定義と適用**

組み込みのプリセットは変更できません。色、罫線、フォントを上書きする必要がある場合は、必ずカスタム ピボットスタイルを定義する必要があります。ワークフローは 3 つのステップで構成されます。

1. `Workbook.getWorksheets().getTableStyles().addPivotTableStyle(String name)` を介して、ワークブックの `TableStyles` コレクションにカスタムスタイルを追加します。これにより、新しく作成されたスタイルのインデックスが返されます。
2. `TableStyle.getTableStyleElements().add(TableStyleElementType)` を通じて要素（`WholeTable` や `GrandTotalRow` など）を追加し、`TableStyleElement.setElementStyle(Style)` を介して各要素に `Style` を割り当てて、スタイルを構成します。
3. `PivotTable.PivotTableStyleName` をスタイルの名前に設定して、カスタムスタイルをピボットに適用します。ここでは `PivotTableStyleType` を使用しないでください。このプロパティは組み込みプリセットを選択するためです。

{{% alert color="primary" %}}

`PivotTableStyleName` と `PivotTableStyleType` は互換性がありません。組み込みプリセットには `PivotTableStyleType` を、`addPivotTableStyle` を通じて定義したカスタムスタイルには `PivotTableStyleName` を使用してください。両方を設定しても問題ありませんが、意図したソースに合致する一方のみがレンダリングされます。

{{% /alert %}}

利用可能な `TableStyleElementType` の値には、`WHOLE_TABLE`、`FIRST_ROW`、`LAST_ROW`、`FIRST_COLUMN`、`LAST_COLUMN`、`GRAND_TOTAL_ROW`、`GRAND_TOTAL_COLUMN`、`PAGE_FIELD_LABELS`、および `PAGE_FIELD_VALUES` があります。

次の例では、`WholeTable` に細い黒い罫線、`GrandTotalRow` に太字の赤いフォントを持つカスタム ピボットスタイルを定義し、`PivotTableStyleName` を介して適用して `.xlsx` として保存します。

```java
import com.aspose.cells.*;

// シナリオ 3: カスタム ピボットテーブル スタイルを定義して適用する
// 使用中の API: PivotTable.PivotTableStyleName + TableStyles.addPivotTableStyle
// 対象ファイル形式: .xlsx / .xlsm / .xlsb
// 完全なサンプルとデータファイルについては、https://github.com/aspose-cells/Aspose.Cells-for-Java を参照してください

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);

// ソースデータを設定: ヘッダー行 + 9データ行 (A1:C10)
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

// A1:C10をソースとするピボットテーブルをE3に配置し、「Pivot1」という名前で追加
int pivotIndex = worksheet.getPivotTables().add("A1:C10", "E3", "Pivot1");
PivotTable pivotTable = worksheet.getPivotTables().get(pivotIndex);

pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");

// ステップ1: 新しいカスタムピボットテーブルスタイルを登録し、そのインデックスを取得
int styleIndex = workbook.getWorksheets().getTableStyles().addPivotTableStyle("CustomPivotStyle");
TableStyle tableStyle = workbook.getWorksheets().getTableStyles().get(styleIndex);

// ステップ2: WholeTable要素を追加し、4辺すべてに細い黒の罫線を適用
int wholeTableElementIndex = tableStyle.getTableStyleElements().add(TableStyleElementType.WHOLE_TABLE);
TableStyleElement wholeTableElement = tableStyle.getTableStyleElements().get(wholeTableElementIndex);
Style wholeTableStyle = workbook.createStyle();
BorderCollection borders = wholeTableStyle.getBorders();
Border borderTop = borders.getByBorderType(BorderType.TOP_BORDER);
borderTop.setLineStyle(CellBorderType.THIN);
borderTop.setColor(Color.getBlack());
Border borderBottom = borders.getByBorderType(BorderType.BOTTOM_BORDER);
borderBottom.setLineStyle(CellBorderType.THIN);
borderBottom.setColor(Color.getBlack());
Border borderLeft = borders.getByBorderType(BorderType.LEFT_BORDER);
borderLeft.setLineStyle(CellBorderType.THIN);
borderLeft.setColor(Color.getBlack());
Border borderRight = borders.getByBorderType(BorderType.RIGHT_BORDER);
borderRight.setLineStyle(CellBorderType.THIN);
borderRight.setColor(Color.getBlack());
wholeTableElement.setElementStyle(wholeTableStyle);

// ステップ3: GrandTotalRow要素を追加し、太字の赤いフォントを適用
int grandTotalElementIndex = tableStyle.getTableStyleElements().add(TableStyleElementType.GRAND_TOTAL_ROW);
TableStyleElement grandTotalElement = tableStyle.getTableStyleElements().get(grandTotalElementIndex);
Style grandTotalStyle = workbook.createStyle();
grandTotalStyle.getFont().setBold(true);
grandTotalStyle.getFont().setColor(Color.getRed());
grandTotalElement.setElementStyle(grandTotalStyle);

// ステップ4: カスタムスタイルを名前で適用（組み込みプリセット用のPivotTableStyleTypeではなく）
pivotTable.setPivotTableStyleName("CustomPivotStyle");

workbook.save("output.xlsx");
```

## **FormatAll を使用してすべてのピボット セルに 1 つのスタイルを適用する**

`PivotTable.formatAll(Style)` は、データ領域、行と列のヘッダー、合計を含むピボットテーブルのすべてのセルに、単一の `Style` オブジェクトを適用するショートカットです。`PivotTableStyleType` または `PivotTableStyleName` を通じて以前に設定された内容はすべて上書きされます。

{{% alert color="primary" %}}

`FormatAll` は `PivotTableStyleType` と `PivotTableStyleName` の両方を上書きします。ピボット全体でテーマ非依存の統一された外観が必要な場合にのみ使用してください。

{{% /alert %}}

次の例では、黄色の単色塗りつぶし、太字の濃い青色のフォント、およびすべての辺に細い黒い罫線を持つ `Style` を作成し、それを `formatAll` で適用して `.xlsx` として保存します。

```java
import com.aspose.cells.*;

// シナリオ 4: 1 つのスタイルを FormatAll ですべてのピボット セルに適用する
// 使用中の API: PivotTable.formatAll
// 対象ファイル形式: .xlsx / .xlsm / .xlsb
// 完全なサンプルとデータファイルについては、https://github.com/aspose-cells/Aspose.Cells-for-Java を参照してください

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);

// ソースデータを入力: ヘッダー行 (1行目) + 9行のデータ行 (2～10行目)
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
int pivotIndex = worksheet.getPivotTables().add("A1:C10", "E3", "Pivot1");
PivotTable pivotTable = worksheet.getPivotTables().get(pivotIndex);

// ピボットフィールドを割り当て: Fruit -> 行エリア、Year -> 列エリア、Amount -> データエリア
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");

// ピボットテーブルのすべてのセルに強制的に適用する Style を作成
Style style = workbook.createStyle();
style.setForegroundColor(Color.getYellow());
style.setPattern(BackgroundType.SOLID);
style.getFont().setBold(true);
style.getFont().setColor(Color.getDarkBlue());

style.getBorders().getByBorderType(BorderType.TOP_BORDER).setLineStyle(CellBorderType.THIN);
style.getBorders().getByBorderType(BorderType.TOP_BORDER).setColor(Color.getBlack());

style.getBorders().getByBorderType(BorderType.BOTTOM_BORDER).setLineStyle(CellBorderType.THIN);
style.getBorders().getByBorderType(BorderType.BOTTOM_BORDER).setColor(Color.getBlack());

style.getBorders().getByBorderType(BorderType.LEFT_BORDER).setLineStyle(CellBorderType.THIN);
style.getBorders().getByBorderType(BorderType.LEFT_BORDER).setColor(Color.getBlack());

style.getBorders().getByBorderType(BorderType.RIGHT_BORDER).setLineStyle(CellBorderType.THIN);
style.getBorders().getByBorderType(BorderType.RIGHT_BORDER).setColor(Color.getBlack());

// formatAll を適用: この単一のスタイルをピボットテーブルのすべてのセルに強制的に適用し、
// 以前に設定された PivotTableStyleType / PivotTableStyleName を上書きする
pivotTable.formatAll(style);

// ワークブックを最新の .xlsx 形式で保存
workbook.save("output.xlsx");
```

## **どのスタイル API を使用すべきか？**

スタイル API の選択は、保存先のファイル形式によって異なります。下の表をクイック リファレンスとしてご利用ください。

| 対象ファイル形式 | 使用する API | メモ |
|---|---|---|
| `.xls`（レガシー） | `PivotTable.AutoFormatType` | `com.aspose.cells.PivotTableAutoFormatType` の値（例: `REPORT_1`～`REPORT_10`、`CLASSIC`、`TABLE_1`～`TABLE_10`）。モダン形式で保存する場合は無視されます。 |
| `.xlsx` / `.xlsm` / `.xlsb`（モダン、組み込みスタイル） | `PivotTable.PivotTableStyleType` | `com.aspose.cells.PivotTableStyleType` の値（明暗テーマ、Excel 2017 の追加分を含む）。 |
| `.xlsx` / `.xlsm` / `.xlsb`（モダン、カスタムスタイル） | `PivotTable.PivotTableStyleName` + `Worksheets.TableStyles.addPivotTableStyle(...)` | 組み込みプリセットでは不十分な場合に使用します。`TableStyleElement.setElementStyle(...)` 経由で設定します。 |
| 任意の形式（統一上書き） | `PivotTable.formatAll(Style)` | ピボット全体の他のすべてのスタイル設定を上書きするショートカット。 |

迷った場合は `.xlsx` として保存し、組み込みテーマには `PivotTableStyleType` を、カスタムテーマには `PivotTableStyleName` を使用してください。

## **関連記事**

- [Aspose.Cells for Java でのピボットテーブルの更新](/cells/ja/java/refresh-pivot-table/)

{{< app/cells/assistant language="java" >}}