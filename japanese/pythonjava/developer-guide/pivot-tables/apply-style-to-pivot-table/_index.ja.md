---
title: Aspose.Cells for Python via Java でピボットテーブルにスタイルを適用する
linktitle: Aspose.Cells for Python via Java でピボットテーブルにスタイルを適用する
description: Aspose.Cells for Python via Java でピボットテーブルに組み込みおよびカスタムスタイルを適用する方法を説明します。レガシー XLS 自動フォーマット、モダン Excel 2007+ の名前付きスタイル、カスタムピボットテーブルスタイル、FormatAll ショートカットについて解説します。
keywords: Aspose.Cells Python via Java ピボットテーブルスタイル, PivotTableStyleType, AutoFormatType, FormatAll, カスタムスタイル, PivotTableStyleName, TableStyles
type: docs
weight: 200
url: /ja/python-java/apply-style-to-pivot-table/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells は、レガシーのピボット自動フォーマット(`.xls` ファイル向け)と、モダンな名前付きまたはカスタムのピボットテーブルスタイル(`.xlsx`、`.xlsm`、`.xlsb` ファイル向け)の両方の適用をサポートします。使用する API は、ワークブックを読み込んだ形式ではなく、保存先のファイル形式によって決まります。
{{% /alert %}}

## **はじめに**
Aspose.Cells はピボットテーブル用に 2 つの並列スタイル API を提供します。どちらを選択するかは、読み込み元の形式ではなく、ワークブックの保存先のファイル形式によって決まります。`.xls` ファイルから読み込んだワークブックを `.xlsx` として再保存することができ、その場合はレガシーのスタイル API ではなく、モダンなスタイル API が適用されます。
- `pivotTable.setPivotTableStyleType(int)` は、組み込みの名前付きスタイル(明テーマ・暗テーマ、Excel 2017 で追加されたスタイルを含む)を選択します。これらのプリセットは読み取り専用です。
- `pivotTable.setPivotTableStyleName(String)` は、`workbook.getWorksheets().getTableStyles().addPivotTableStyle(String)` で定義したカスタムスタイルを選択します。プリセットで提供される範囲を超えて、色、罫線、フォントを変更したい場合は、カスタムスタイルが必要です。
さらに、`pivotTable.formatAll(Style)` は、単一の `Style` オブジェクトをピボットのすべてのセルに適用し、上記のいずれかのスタイル名 API で設定された内容を上書きするショートカットです。基になるテーマに関係なく均一な外観が必要な場合に便利です。

## **レガシー XLS プリセット自動フォーマットの適用**
ピボットテーブルの `setAutoFormatType` メソッドは、`com.aspose.cells.pivot.PivotTableAutoFormatType` 列挙の値を受け付けます。使用可能な値は `REPORT_1` から `REPORT_10`、`CLASSIC`、および `TABLE_1` から `TABLE_10` です。
次の例では、新しいワークブックを読み込み、Fruit/Year/Amount のサンプルデータを設定し、ピボットテーブルを追加して `PivotTableAutoFormatType.REPORT_5` を適用し、結果を `.xls` として保存します。

{{% alert color="primary" %}}
**なぜ列フィールドがないのか?** レポートシリーズの自動フォーマット(`Report1`～`Report10`、`Table1`～`Table10`)は、クラシック Excel で行フィールドと値のみの**単一ディメンションのピボットテーブル**向けに設計されており、列フィールドヘッダー用の組み込みスタイルがありません。ピボットに列フィールドが必要な場合は、モダン Excel で使用される 2D レイアウト向けに設計された、[シナリオ 2](#apply-a-modern-named-preset-pivot-table-style) のモダンな `PivotTableStyleType` プリセットを使用してください。
{{% /alert %}}

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, PivotFieldType, PivotTableAutoFormatType
# シナリオ 1: レガシー XLS プリセット自動フォーマットを適用する
# 使用中の API: PivotTable.AutoFormatType
# ターゲットファイル形式: .xls(レガシー)
# 完全なサンプルとデータファイルについては、https://github.com/aspose-cells/Aspose.Cells-for-.NET を参照してください
# 新しいワークブックを作成する
workbook = Workbook()
# 最初のワークシートを取得する
sheet = workbook.getWorksheets().get(0)
# ソースデータにヘッダー行(Fruit、Year、Amount)と、
# 2020年と2021年にわたる grape、blueberry、kiwi、cherry をカバーする9行のデータを作成する
sheet.getCells().get(0, 0).putValue("Fruit")
sheet.getCells().get(0, 1).putValue("Year")
sheet.getCells().get(0, 2).putValue("Amount")
sheet.getCells().get(1, 0).putValue("grape")
sheet.getCells().get(1, 1).putValue(2020)
sheet.getCells().get(1, 2).putValue(50)
sheet.getCells().get(2, 0).putValue("blueberry")
sheet.getCells().get(2, 1).putValue(2020)
sheet.getCells().get(2, 2).putValue(30)
sheet.getCells().get(3, 0).putValue("kiwi")
sheet.getCells().get(3, 1).putValue(2020)
sheet.getCells().get(3, 2).putValue(25)
sheet.getCells().get(4, 0).putValue("cherry")
sheet.getCells().get(4, 1).putValue(2020)
sheet.getCells().get(4, 2).putValue(40)
sheet.getCells().get(5, 0).putValue("grape")
sheet.getCells().get(5, 1).putValue(2021)
sheet.getCells().get(5, 2).putValue(60)
sheet.getCells().get(6, 0).putValue("blueberry")
sheet.getCells().get(6, 1).putValue(2021)
sheet.getCells().get(6, 2).putValue(35)
sheet.getCells().get(7, 0).putValue("kiwi")
sheet.getCells().get(7, 1).putValue(2021)
sheet.getCells().get(7, 2).putValue(28)
sheet.getCells().get(8, 0).putValue("cherry")
sheet.getCells().get(8, 1).putValue(2021)
sheet.getCells().get(8, 2).putValue(45)
sheet.getCells().get(9, 0).putValue("grape")
sheet.getCells().get(9, 1).putValue(2020)
sheet.getCells().get(9, 2).putValue(45)
# セル E3 に、ソース範囲 A1:C10 を使用して「Pivot1」という名前のピボットテーブルを追加する
pivotIndex = sheet.getPivotTables().add("A1:C10", "E3", "Pivot1")
pivotTable = sheet.getPivotTables().get(pivotIndex)
# フィールドを割り当てる: Fruit → 行、Amount → データ
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount")
# レガシー XLS プリセット自動フォーマット「Report5」を適用する
# 注: このプロパティは .xls として保存する場合にのみ意味を持ちます。
# .xlsx/.xlsm/.xlsb として保存する場合、Excel は AutoFormatType を無視し、
# PivotTableStyleType / PivotTableStyleName で指定されたものを使用します。
pivotTable.setAutoFormatType(PivotTableAutoFormatType.REPORT_5)
# ワークブックをレガシー .xls 形式で保存する
workbook.save("output.xls")
jpype.shutdownJVM()
```

## **モダンな名前付きプリセットピボットテーブルスタイルの適用**

`pivotTable.setPivotTableStyleType(int)` は、Excel 2007 でピボット テーブルに導入された組み込みの名前付きスタイルの 1 つを選択します。`PivotTableStyleType` 列挙型は、3 つのテーマ ファミリーを公開しています。`PIVOT_TABLE_STYLE_LIGHT1` から `PIVOT_TABLE_STYLE_LIGHT28` までのライト ファミリー、`PIVOT_TABLE_STYLE_MEDIUM1` から `PIVOT_TABLE_STYLE_MEDIUM28` までのミディアム ファミリー、`PIVOT_TABLE_STYLE_DARK1` から `PIVOT_TABLE_STYLE_DARK_28` までのダーク ファミリーです。また、`None` と `Custom` も定義しています。各ファミリーで番号が大きいメンバーは、Excel 2017 で追加されたスタイルです。
これらのプリセットは読み取り専用です。プリセットが提供する範囲を超えて、色、罫線、またはフォントを変更する必要がある場合は、代わりにカスタム ピボット スタイルを定義する必要があります。[シナリオ 3](#define-and-apply-a-custom-pivot-table-style) に示す通りです。

{{% alert color="primary" %}}
**なぜモダンなプリセットを使用し、レポート シリーズの自動フォーマットを使用しないのですか?** `PivotTableAutoFormatType` の `Report1` から `Report10` まで、および `Table1` から `Table10` までの値は、ピボット列フィールドより前に作成されたものなので、列フィールド ヘッダー向けのスタイルが含まれていません。そのため、Excel はそれらのヘッダーをスタイルなしで表示します。`PivotTableStyleType` のプリセットは、現代の Excel が使用する 2 次元レイアウト向けに設計されており、行フィールド ヘッダーと列フィールド ヘッダーの両方にスタイルを適用します。
{{% /alert %}}

このシナリオでは、シナリオ 1 の Fruit/Year/Amount データセットを再利用し、`PivotFieldType.COLUMN` を使用して `Fruit` 行フィールドに加えて `Year` を列領域に追加し、`pivotTable.setPivotTableStyleType` でダークテーマのプリセット `PIVOT_TABLE_STYLE_DARK1` を適用し、結果を `.xlsx` として保存します。`PivotTableStyleType` が有効となる形式です。

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotTableStyleType, PivotFieldType
# Scenario 2: Apply a modern Excel 2007+ named preset style using PivotTableStyleType.
# Target file format: .xlsx. The PivotTableStyleType enum lives in the Aspose.Cells namespace
# GitHub reference: https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Examples/CSharp/PivotTables/ApplyStyleToPivotTable2.cs
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
# Header row: Fruit / Year / Amount
worksheet.getCells().get("A1").putValue("Fruit")
worksheet.getCells().get("B1").putValue("Year")
worksheet.getCells().get("C1").putValue("Amount")
# 9 data rows of Fruit / Year / Amount
worksheet.getCells().get("A2").putValue("Grape")
worksheet.getCells().get("B2").putValue(2020)
worksheet.getCells().get("C2").putValue(100)
worksheet.getCells().get("A3").putValue("Blueberry")
worksheet.getCells().get("B3").putValue(2020)
worksheet.getCells().get("C3").putValue(150)
worksheet.getCells().get("A4").putValue("Kiwi")
worksheet.getCells().get("B4").putValue(2020)
worksheet.getCells().get("C4").putValue(200)
worksheet.getCells().get("A5").putValue("Cherry")
worksheet.getCells().get("B5").putValue(2020)
worksheet.getCells().get("C5").putValue(180)
worksheet.getCells().get("A6").putValue("Grape")
worksheet.getCells().get("B6").putValue(2021)
worksheet.getCells().get("C6").putValue(120)
worksheet.getCells().get("A7").putValue("Blueberry")
worksheet.getCells().get("B7").putValue(2021)
worksheet.getCells().get("C7").putValue(170)
worksheet.getCells().get("A8").putValue("Kiwi")
worksheet.getCells().get("B8").putValue(2021)
worksheet.getCells().get("C8").putValue(210)
worksheet.getCells().get("A9").putValue("Cherry")
worksheet.getCells().get("B9").putValue(2021)
worksheet.getCells().get("C9").putValue(190)
worksheet.getCells().get("A10").putValue("Grape")
worksheet.getCells().get("B10").putValue(2021)
worksheet.getCells().get("C10").putValue(130)
# Add a pivot table at E3 named "Pivot1", sourced from A1:C10
pivotIndex = worksheet.getPivotTables().add("A1:C10", "E3", "Pivot1")
pivotTable = worksheet.getPivotTables().get(pivotIndex)
# Assign pivot fields: Fruit -> Row area, Year -> Column area, Amount -> Data area
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year")
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount")
# Apply a modern Excel 2007+ named preset pivot style.
# PivotTableStyleType is the correct API for .xlsx / .xlsm / .xlsb files; AutoFormatType
# is ignored by Excel for those formats. PivotTableStyleDark1 belongs to the dark-theme
# family (PivotTableStyleDark1..PivotTableStyleDark28), and the same enum also exposes the
# newer Excel 2017 light/dark themes (PivotTableStyleLight1..Light28 / Dark1..Dark28).
pivotTable.setPivotTableStyleType(PivotTableStyleType.PIVOT_TABLE_STYLE_DARK_1)
# Save as modern .xlsx — this is the format for which PivotTableStyleType is meaningful.
workbook.save("output.xlsx")
jpype.shutdownJVM()
```
## **カスタムピボットテーブルスタイルの定義と適用**
組み込みプリセットは変更できません。色、罫線、フォントを上書きする必要がある場合は、必ずカスタムピボットスタイルを定義する必要があります。ワークフローは次の 3 ステップで構成されます。
1. `workbook.getWorksheets().getTableStyles().addPivotTableStyle(String name)` を使用して、ワークブックの `TableStyles` コレクションにカスタムスタイルを追加します。これにより、新しく作成されたスタイルのインデックスが返されます。
2. `tableStyle.getTableStyleElements().add(TableStyleElementType)` で要素(例: `WHOLE_TABLE` や `GRAND_TOTAL_ROW`)を追加し、`tableStyleElement.setElementStyle(Style)` で各要素に `Style` を割り当てることで、スタイルを構成します。
3. `pivotTable.setPivotTableStyleName(String)` をスタイル名で呼び出して、カスタムスタイルをピボットに適用します。ここでは `setPivotTableStyleType` を使用しないでください。このメソッドは組み込みプリセットを選択するためのものです。

{{% alert color="primary" %}}
`setPivotTableStyleName` と `setPivotTableStyleType` は互いに置き換え可能ではありません。組み込みプリセットには `setPivotTableStyleType` を、`addPivotTableStyle` を使用して定義したカスタムスタイルには `setPivotTableStyleName` を使用してください。両方とも設定しても問題ありませんが、意図したソースと一致する方のみがレンダリングされます。
使用可能な `TableStyleElementType` の値には、`WHOLE_TABLE`、`FIRST_ROW`、`LAST_ROW`、`FIRST_COLUMN`、`LAST_COLUMN`、`GRAND_TOTAL_ROW`、`GRAND_TOTAL_COLUMN`、`PAGE_FIELD_LABELS`、および `PAGE_FIELD_VALUES` が含まれます。
次の例では、`WHOLE_TABLE` に細い黒い罫線、`GRAND_TOTAL_ROW` に太字の赤いフォントを持つカスタムピボットスタイルを定義し、`setPivotTableStyleName` で適用して `.xlsx` として保存します。
{{% /alert %}}

```python
import jpype
import jpype.imports
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat
from asposecells.api import PivotFieldType, TableStyleElementType, BorderType, CellBorderType
from asposecells.api import Color
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
# ソースデータを入力: ヘッダー行 + 9行のデータ (A1:C10)
worksheet.getCells().get("A1").putValue("Fruit")
worksheet.getCells().get("B1").putValue("Year")
worksheet.getCells().get("C1").putValue("Amount")
worksheet.getCells().get("A2").putValue("Grape")
worksheet.getCells().get("B2").putValue(2020)
worksheet.getCells().get("C2").putValue(100)
worksheet.getCells().get("A3").putValue("Blueberry")
worksheet.getCells().get("B3").putValue(2020)
worksheet.getCells().get("C3").putValue(200)
worksheet.getCells().get("A4").putValue("Kiwi")
worksheet.getCells().get("B4").putValue(2020)
worksheet.getCells().get("C4").putValue(300)
worksheet.getCells().get("A5").putValue("Cherry")
worksheet.getCells().get("B5").putValue(2020)
worksheet.getCells().get("C5").putValue(400)
worksheet.getCells().get("A6").putValue("Grape")
worksheet.getCells().get("B6").putValue(2021)
worksheet.getCells().get("C6").putValue(500)
worksheet.getCells().get("A7").putValue("Blueberry")
worksheet.getCells().get("B7").putValue(2021)
worksheet.getCells().get("C7").putValue(600)
worksheet.getCells().get("A8").putValue("Kiwi")
worksheet.getCells().get("B8").putValue(2021)
worksheet.getCells().get("C8").putValue(700)
worksheet.getCells().get("A9").putValue("Cherry")
worksheet.getCells().get("B9").putValue(2021)
worksheet.getCells().get("C9").putValue(800)
worksheet.getCells().get("A10").putValue("Grape")
worksheet.getCells().get("B10").putValue(2021)
worksheet.getCells().get("C10").putValue(900)
# A1:C10 をソースとするピボットテーブルを E3 に「Pivot1」という名前で追加
pivotIndex = worksheet.getPivotTables().add("A1:C10", "E3", "Pivot1")
pivotTable = worksheet.getPivotTables().get(pivotIndex)
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year")
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount")
# ステップ 1: 新しいカスタムピボットテーブルスタイルを登録し、そのインデックスを取得
styleIndex = workbook.getWorksheets().getTableStyles().addPivotTableStyle("CustomPivotStyle")
tableStyle = workbook.getWorksheets().getTableStyles().get(styleIndex)
# ステップ 2: WholeTable 要素を追加し、4辺すべてに細い黒の罫線を適用
wholeTableElementIndex = tableStyle.getTableStyleElements().add(TableStyleElementType.WHOLE_TABLE)
wholeTableElement = tableStyle.getTableStyleElements().get(wholeTableElementIndex)
wholeTableStyle = workbook.createStyle()
wholeTableStyle.getBorders().getByBorderType(BorderType.TOP_BORDER).setLineStyle(CellBorderType.THIN)
wholeTableStyle.getBorders().getByBorderType(BorderType.TOP_BORDER).setColor(Color.getBlack())
wholeTableStyle.getBorders().getByBorderType(BorderType.BOTTOM_BORDER).setLineStyle(CellBorderType.THIN)
wholeTableStyle.getBorders().getByBorderType(BorderType.BOTTOM_BORDER).setColor(Color.getBlack())
wholeTableStyle.getBorders().getByBorderType(BorderType.LEFT_BORDER).setLineStyle(CellBorderType.THIN)
wholeTableStyle.getBorders().getByBorderType(BorderType.LEFT_BORDER).setColor(Color.getBlack())
wholeTableStyle.getBorders().getByBorderType(BorderType.RIGHT_BORDER).setLineStyle(CellBorderType.THIN)
wholeTableStyle.getBorders().getByBorderType(BorderType.RIGHT_BORDER).setColor(Color.getBlack())
wholeTableElement.setElementStyle(wholeTableStyle)
# ステップ 3: GrandTotalRow 要素を追加し、太字の赤いフォントを適用
grandTotalElementIndex = tableStyle.getTableStyleElements().add(TableStyleElementType.GRAND_TOTAL_ROW)
grandTotalElement = tableStyle.getTableStyleElements().get(grandTotalElementIndex)
grandTotalStyle = workbook.createStyle()
grandTotalStyle.getFont().setBold(True)
grandTotalStyle.getFont().setColor(Color.getRed())
grandTotalElement.setElementStyle(grandTotalStyle)
# ステップ 4: カスタムスタイルを名前で適用(組み込みプリセット用の PivotTableStyleType では無い)
pivotTable.setPivotTableStyleName("CustomPivotStyle")
workbook.save("output.xlsx")
jpype.shutdownJVM()
```

## **formatAll を使用してすべてのピボットセルに 1 つのスタイルを適用する**
`pivotTable.formatAll(Style)` は、データ領域、行ヘッダーと列ヘッダー、合計を含むピボットテーブル全体のすべてのセルに単一の `Style` オブジェクトを適用するショートカットです。`setPivotTableStyleType` または `setPivotTableStyleName` で以前に設定した内容はすべて上書きされます。

{{% alert color="primary" %}}
`formatAll` は `setPivotTableStyleType` と `setPivotTableStyleName` の両方を上書きします。ピボット全体でテーマ非依存の均一な外観が必要な場合にのみ使用してください。
次の例では、黄色の単色塗りつぶし、太字の濃紺フォント、すべての辺に細い黒い罫線を持つ `Style` を作成し、`formatAll` で適用して `.xlsx` として保存します。
{{% /alert %}}

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, Style
from asposecells.api import Color
from asposecells.api import PivotTable, PivotFieldType
from asposecells.api import BorderType, CellBorderType, BackgroundType
# シナリオ 4: formatAll を使用してすべてのピボットテーブルセルに単一のスタイルを適用
# 使用中の API: PivotTable.formatAll(Style)
# ターゲット形式: .xlsx
# GitHub リファレンス: Aspose.Cells-for-.NET リポジトリを参照 — ピボットテーブルのスタイル設定例
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
# ソースデータを設定: ヘッダー行 (1行目) + 9データ行 (2～10行目)
worksheet.getCells().get("A1").putValue("Fruit")
worksheet.getCells().get("B1").putValue("Year")
worksheet.getCells().get("C1").putValue("Amount")
worksheet.getCells().get("A2").putValue("Grape")
worksheet.getCells().get("B2").putValue(2020)
worksheet.getCells().get("C2").putValue(5000)
worksheet.getCells().get("A3").putValue("Blueberry")
worksheet.getCells().get("B3").putValue(2020)
worksheet.getCells().get("C3").putValue(3000)
worksheet.getCells().get("A4").putValue("Kiwi")
worksheet.getCells().get("B4").putValue(2020)
worksheet.getCells().get("C4").putValue(4000)
worksheet.getCells().get("A5").putValue("Cherry")
worksheet.getCells().get("B5").putValue(2020)
worksheet.getCells().get("C5").putValue(2000)
worksheet.getCells().get("A6").putValue("Grape")
worksheet.getCells().get("B6").putValue(2021)
worksheet.getCells().get("C6").putValue(6000)
worksheet.getCells().get("A7").putValue("Blueberry")
worksheet.getCells().get("B7").putValue(2021)
worksheet.getCells().get("C7").putValue(3500)
worksheet.getCells().get("A8").putValue("Kiwi")
worksheet.getCells().get("B8").putValue(2021)
worksheet.getCells().get("C8").putValue(4500)
worksheet.getCells().get("A9").putValue("Cherry")
worksheet.getCells().get("B9").putValue(2021)
worksheet.getCells().get("C9").putValue(2500)
worksheet.getCells().get("A10").putValue("Grape")
worksheet.getCells().get("B10").putValue(2021)
worksheet.getCells().get("C10").putValue(5500)
# ピボットテーブルを追加: ソース範囲 A1:C10、配置先セル E3、名前 "Pivot1"
pivotIndex = worksheet.getPivotTables().add("A1:C10", "E3", "Pivot1")
pivotTable = worksheet.getPivotTables().get(pivotIndex)
# ピボットフィールドを割り当て: Fruit -> 行エリア、Year -> 列エリア、Amount -> データエリア
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year")
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount")
# ピボットテーブルのすべてのセルに強制適用されるスタイルを構築
style = workbook.createStyle()
style.setForegroundColor(Color.fromArgb(70, 130, 180))
style.setPattern(BackgroundType.SOLID)
style.getFont().setBold(True)
style.getFont().setColor(Color.getDarkBlue())
style.getBorders().getByBorderType(BorderType.TOP_BORDER).setLineStyle(CellBorderType.THIN)
style.getBorders().getByBorderType(BorderType.TOP_BORDER).setColor(Color.getBlack())
style.getBorders().getByBorderType(BorderType.BOTTOM_BORDER).setLineStyle(CellBorderType.THIN)
style.getBorders().getByBorderType(BorderType.BOTTOM_BORDER).setColor(Color.getBlack())
style.getBorders().getByBorderType(BorderType.LEFT_BORDER).setLineStyle(CellBorderType.THIN)
style.getBorders().getByBorderType(BorderType.LEFT_BORDER).setColor(Color.getBlack())
style.getBorders().getByBorderType(BorderType.RIGHT_BORDER).setLineStyle(CellBorderType.THIN)
style.getBorders().getByBorderType(BorderType.RIGHT_BORDER).setColor(Color.getBlack())
# formatAll を適用: この単一のスタイルをピボットテーブルのすべてのセルに強制し、
# 以前に設定された PivotTableStyleType / PivotTableStyleName をすべて上書きします
pivotTable.formatAll(style)
# ワークブックを最新の .xlsx 形式で保存
workbook.save("output.xlsx")
jpype.shutdownJVM()
```

## **どのスタイル API を使用すべきか?**
スタイル API の選択は、保存先のファイル形式によって異なります。次の表をクイックリファレンスとしてご利用ください。
| 対象ファイル形式 | 使用する API | メモ |
|---|---|---|
| `.xls`(レガシー) | `pivotTable.setAutoFormatType(int)` | `com.aspose.cells.pivot.PivotTableAutoFormatType` の値(例: `REPORT_1`～`REPORT_10`、`CLASSIC`、`TABLE_1`～`TABLE_10`)。モダン形式で保存する場合は無視されます。 |
| `.xlsx` / `.xlsm` / `.xlsb`(モダン、組み込みスタイル) | `pivotTable.setPivotTableStyleType(int)` | `com.aspose.cells.PivotTableStyleType` の値(明テーマ/暗テーマ、Excel 2017 の追加を含む)。 |
| `.xlsx` / `.xlsm` / `.xlsb`(モダン、カスタムスタイル) | `pivotTable.setPivotTableStyleName(String)` + `tableStyles.addPivotTableStyle(String)` | 組み込みプリセットでは不十分な場合に使用します。`tableStyleElement.setElementStyle(Style)` で構成します。 |
| 任意の形式(均一な上書き) | `pivotTable.formatAll(Style)` | ピボット全体の他のすべてのスタイル設定を上書きするショートカット。 |
迷う場合は、`.xlsx` として保存し、組み込みテーマには `setPivotTableStyleType` を、カスタムテーマには `setPivotTableStyleName` を使用してください。


{{< app/cells/assistant language="python" >}}