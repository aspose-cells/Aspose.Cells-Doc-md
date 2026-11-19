---
title: Aspose.Cells for Java でピボットテーブルにスタイルを適用する
linktitle: Aspose.Cells for Java でピボットテーブルにスタイルを適用する
description: Aspose.Cells for Java でピボットテーブルに組み込みスタイルとカスタムスタイルを適用する方法を説明します。レガシー XLS の自動書式、Excel 2007 以降のモダンな名前付きスタイル、カスタムピボットテーブルスタイル、formatAll ショートカットについて解説します。
keywords: Aspose.Cells Java ピボットテーブル スタイル, PivotTableStyleType, AutoFormatType, FormatAll, カスタムスタイル, PivotTableStyleName, TableStyles
type: docs
weight: 200
url: /ja/java/apply-style-to-pivot-table/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells は、レガシーなピボットの自動書式（`.xls` ファイル向け）と、モダンな名前付きまたはカスタムのピボットテーブルスタイル（`.xlsx`、`.xlsm`、`.xlsb` ファイル向け）の両方の適用をサポートしています。使用する API は、ワークブックの読み込み元形式ではなく、保存先のファイル形式によって決まります。
{{% /alert %}}

## **はじめに**
Aspose.Cells は、ピボットテーブル向けに 2 つの並列なスタイル API を提供しています。これらのどちらを使うかは、ワークブックの読み込み元形式ではなく、保存先のファイル形式によって決まります。`.xls` ファイルから読み込んだワークブックを `.xlsx` として再保存する場合、レガシーなスタイル API ではなく、モダンなスタイル API が適用されます。
- `PivotTable.PivotTableStyleType` は、組み込みの名前付きスタイル（ライトテーマおよびダークテーマ、Excel 2017 で追加されたスタイルを含む）を選択します。これらのプリセットは読み取り専用です。
- `PivotTable.PivotTableStyleName` は、`Workbook.getWorksheets().getTableStyles().addPivotTableStyle(...)` を通じて独自に定義したカスタムスタイルを選択します。プリセットで提供される色、罫線、フォント以外の変更が必要な場合は、カスタムスタイルが必須となります。
さらに、`PivotTable.formatAll(Style)` は、単一の `Style` オブジェクトをピボットのすべてのセルに適用し、上記いずれかのスタイル名 API で設定された内容をすべて上書きするショートカットです。テーマに関係なく統一された外観が必要な場合に便利です。

## **レガシー XLS のプリセット自動書式を適用する**
`PivotTable.AutoFormatType` は、`com.aspose.cells.PivotTableAutoFormatType` 列挙の値を受け取ります。利用可能な値は、`REPORT_1` から `REPORT_10`、`CLASSIC`、および `TABLE_1` から `TABLE_10` です。
次の例では、新しいワークブックを作成し、Fruit/Year/Amount のサンプルデータを入力し、ピボットテーブルを追加して `PivotTableAutoFormatType.REPORT_5` を適用し、結果を `.xls` として保存します。

{{% alert color="primary" %}}
**なぜ列フィールドがないのか?** Report シリーズ（`Report1` から `Report10`、`Table1` から `Table10`）の自動書式は、従来の Excel において、行フィールドと値のみを持つ**単一次元のピボットテーブル**向けに設計されており、列フィールドヘッダーのスタイルは組み込まれていません。ピボットに列フィールドが必要な場合は、代わりに [シナリオ 2](#apply-a-modern-named-preset-pivot-table-style) のモダンな `PivotTableStyleType` プリセットを使用してください。これらはモダンな Excel で使用される 2 次元レイアウト向けに設計されています。
{{% /alert %}}

```java
import com.aspose.cells.*;
// Scenario 1: Apply a legacy XLS preset autoformat
// API in use: PivotTable.AutoFormatType
// Target file format: .xls (legacy)
// For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-.NET
// Create a new workbook
Workbook workbook = new Workbook();
// Get the first worksheet
Worksheet sheet = workbook.getWorksheets().get(0);
// Populate the source data with header row (Fruit, Year, Amount)
// and 9 data rows covering grape, blueberry, kiwi, cherry across 2020 and 2021
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
// Add a pivot table at destination cell E3, using source range A1:C10
PivotTable pivotTable = sheet.getPivotTables().add("A1:C10", 2, 4);
// Assign fields: Fruit -> Rows, Amount -> Data
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
// Apply the legacy XLS preset autoformat "Report5"
// Note: This property is only meaningful when saving as .xls.
// When saved as .xlsx/.xlsm/.xlsb, Excel ignores AutoFormatType
// and uses whatever PivotTableStyleType / PivotTableStyleName specifies.
pivotTable.setAutoFormatType(PivotTableAutoFormatType.REPORT_5);
// Save the workbook in legacy .xls format
workbook.save("output.xls");
```

## **モダンな名前付きプリセットのピボットテーブルスタイルを適用する**
`PivotTable.setPivotTableStyleType(int)` は、Excel 2007 でピボットテーブルに導入された組み込みの名前付きスタイルのいずれかを選択します。`PivotTableStyleType` 列挙型は、3 つのテーマファミリーを公開しています。`PIVOT_TABLE_STYLE_LIGHT1` から `PIVOT_TABLE_STYLE_LIGHT28` までのライトファミリー、`PIVOT_TABLE_STYLE_MEDIUM1` から `PIVOT_TABLE_STYLE_MEDIUM28` までの中間ファミリー、`PIVOT_TABLE_STYLE_DARK1` から `PIVOT_TABLE_STYLE_DARK_28` までのダークファミリーです。また、`None` と `Custom` も定義しています。各ファミリーで番号が大きいメンバーは、Excel 2017 で追加されたスタイルです。
これらのプリセットは読み取り専用です。色、罫線、またはフォントをプリセットの範囲を超えて変更する必要がある場合は、代わりにカスタムピボットスタイルを定義する必要があります。これは [シナリオ 3](#define-and-apply-a-custom-pivot-table-style) で示されています。

{{% alert color="primary" %}}
**なぜ現代のプリセットを使用し、レポートシリーズのオートフォーマットを使用しないのですか？** `PivotTableAutoFormatType` の `Report1` から `Report10` までの値と `Table1` から `Table10` までの値は、ピボット列フィールドより前に定義されたもので、列フィールドヘッダーのスタイル指定がないため、Excel はそれらのヘッダーをスタイルなしで表示します。`PivotTableStyleType` のプリセットは、现代の Excel が使用する二次元レイアウト向けに設計されており、行フィールドヘッダーと列フィールドヘッダーの両方にスタイルを適用します。
{{% /alert %}}

このシナリオでは、シナリオ 1 の Fruit/Year/Amount データセットを再利用し、`PivotFieldType.COLUMN` を使用して `Year` を列エリアに追加します。列エリアには `Fruit` 行フィールドが配置されているため、`Year` はその行フィールドの隣に追加されます。次に、`pivotTable.setPivotTableStyleType` を使用してダークテーマのプリセット `PIVOT_TABLE_STYLE_DARK1` を適用し、結果を `.xlsx` として保存します。これは `PivotTableStyleType` が意味を持つ形式です。

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
// Header row: Fruit / Year / Amount
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");
// 9 data rows of Fruit / Year / Amount
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
// Add a pivot table at E3, sourced from A1:C10
PivotTable pivotTable = worksheet.getPivotTables().add("A1:C10", 2, 4);
// Assign pivot fields: Fruit -> Row area, Year -> Column area, Amount -> Data area
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
// Apply a modern Excel 2007+ named preset pivot style.
// PivotTableStyleType is the correct API for .xlsx / .xlsm / .xlsb files; AutoFormatType
// is ignored by Excel for those formats. PivotTableStyleDark1 belongs to the dark-theme
// family (PivotTableStyleDark1..PivotTableStyleDark28), and the same enum also exposes the
// newer Excel 2017 light/dark themes (PivotTableStyleLight1..Light28 / Dark1..Dark28).
pivotTable.setPivotTableStyleType(PivotTableStyleType.PIVOT_TABLE_STYLE_DARK_1);
// Save as modern .xlsx - this is the format for which PivotTableStyleType is meaningful.
workbook.save("output.xlsx");
```

## **カスタムピボットテーブルスタイルを定義して適用する**
組み込みのプリセットは変更できません。色、罫線、フォントを上書きする必要がある場合は、必ずカスタムピボットスタイルを定義する必要があります。ワークフローは次の 3 ステップで構成されます。
1. `Workbook.getWorksheets().getTableStyles().addPivotTableStyle(String name)` を呼び出して、ワークブックの `TableStyles` コレクションにカスタムスタイルを追加します。これは新しく作成されたスタイルのインデックスを返します。
2. `TableStyle.getTableStyleElements().add(TableStyleElementType)` を通じて要素（`WholeTable` や `GrandTotalRow` など）を追加し、`TableStyleElement.setElementStyle(Style)` を介して各要素に `Style` を割り当てることで、スタイルを設定します。
3. `PivotTable.PivotTableStyleName` にスタイル名を設定して、カスタムスタイルをピボットに適用します。ここでは `PivotTableStyleType` を使用しないでください。このプロパティは組み込みプリセットを選択するためのものだからです。

{{% alert color="primary" %}}
`PivotTableStyleName` と `PivotTableStyleType` は相互に置き換え可能なものではありません。組み込みプリセットには `PivotTableStyleType` を、`addPivotTableStyle` を通じて定義したカスタムスタイルには `PivotTableStyleName` を使用してください。両方を設定しても害はありませんが、意図したソースに合致する一方のみがレンダリングされます。
利用可能な `TableStyleElementType` の値には、`WHOLE_TABLE`、`FIRST_ROW`、`LAST_ROW`、`FIRST_COLUMN`、`LAST_COLUMN`、`GRAND_TOTAL_ROW`、`GRAND_TOTAL_COLUMN`、`PAGE_FIELD_LABELS`、`PAGE_FIELD_VALUES` が含まれます。
次の例では、`WholeTable` に細い黒色の罫線、`GrandTotalRow` に太字の赤色のフォントを持つカスタムピボットスタイルを定義し、`PivotTableStyleName` を介してそれを適用して `.xlsx` として保存します。
{{% /alert %}}

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
// Populate source data: header row + 9 data rows (A1:C10)
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
// Add pivot table sourced from A1:C10, anchored at E3
PivotTable pivotTable = worksheet.getPivotTables().add("A1:C10", 2, 4);
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
// Step 1: register a new custom pivot table style and capture its index
int styleIndex = workbook.getWorksheets().getTableStyles().addPivotTableStyle("CustomPivotStyle");
TableStyle tableStyle = workbook.getWorksheets().getTableStyles().get(styleIndex);
// Step 2: add a WholeTable element and apply thin black borders on all four sides
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
// Step 3: add a GrandTotalRow element and apply bold red font
int grandTotalElementIndex = tableStyle.getTableStyleElements().add(TableStyleElementType.GRAND_TOTAL_ROW);
TableStyleElement grandTotalElement = tableStyle.getTableStyleElements().get(grandTotalElementIndex);
Style grandTotalStyle = workbook.createStyle();
grandTotalStyle.getFont().setBold(true);
grandTotalStyle.getFont().setColor(Color.getRed());
grandTotalElement.setElementStyle(grandTotalStyle);
// Step 4: apply the custom style by name (NOT by PivotTableStyleType, which is for built-in presets)
pivotTable.setPivotTableStyleName("CustomPivotStyle");
workbook.save("output.xlsx");
```

## **formatAll を使用してすべてのピボットセルに 1 つのスタイルを適用する**
`PivotTable.formatAll(Style)` は、データ領域、行/列ヘッダー、合計を含むピボットテーブルのすべてのセルに単一の `Style` オブジェクトを適用するショートカットです。`PivotTableStyleType` または `PivotTableStyleName` を介して以前に設定された内容はすべて上書きされます。

{{% alert color="primary" %}}
`formatAll` は `PivotTableStyleType` と `PivotTableStyleName` の両方を上書きします。テーマに関係なく、ピボット全体で統一された外観が必要な場合にのみ使用してください。
次の例では、黄色の単色塗りつぶし、太字の濃紺フォント、すべての辺に細い黒色の罫線を持つ `Style` を作成し、`formatAll` で適用して `.xlsx` として保存します。
{{% /alert %}}

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
// Populate source data: header row (row 1) + 9 data rows (rows 2-10)
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
// Add pivot table: source range A1:C10, destination cell E3
PivotTable pivotTable = worksheet.getPivotTables().add("A1:C10", 2, 4);
// Assign pivot fields: Fruit -> Row area, Year -> Column area, Amount -> Data area
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
// Build a Style that will be forced onto every cell of the pivot table
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
// Apply formatAll: forces this single style onto every cell of the pivot table,
// overriding any PivotTableStyleType / PivotTableStyleName previously set
pivotTable.formatAll(style);
// Save the workbook in the modern .xlsx format
workbook.save("output.xlsx");
```

## **どのスタイル API を使用すべきか?**
スタイル API の選択は、保存先のファイル形式によって異なります。下の表をクイックリファレンスとしてご活用ください。
| 保存先のファイル形式 | 使用する API | メモ |
|---|---|---|
| `.xls`（レガシー） | `PivotTable.AutoFormatType` | `com.aspose.cells.PivotTableAutoFormatType` の値（例: `REPORT_1`～`REPORT_10`、`CLASSIC`、`TABLE_1`～`TABLE_10`）。モダン形式で保存する場合は無視されます。 |
| `.xlsx` / `.xlsm` / `.xlsb`（モダン、組み込みスタイル） | `PivotTable.PivotTableStyleType` | `com.aspose.cells.PivotTableStyleType` の値（ライト/ダークテーマ、Excel 2017 で追加されたものを含む）。 |
| `.xlsx` / `.xlsm` / `.xlsb`（モダン、カスタムスタイル） | `PivotTable.PivotTableStyleName` + `Worksheets.TableStyles.addPivotTableStyle(...)` | 組み込みプリセットで足りない場合に使用します。`TableStyleElement.setElementStyle(...)` を介して設定します。 |
| すべての形式（統一上書き） | `PivotTable.formatAll(Style)` | ピボット全体の他のすべてのスタイル設定を上書きするショートカット。 |
判断に迷った場合は、`.xlsx` として保存し、組み込みテーマには `PivotTableStyleType` を、カスタムテーマには `PivotTableStyleName` を使用してください。

{{< app/cells/assistant language="java" >}}