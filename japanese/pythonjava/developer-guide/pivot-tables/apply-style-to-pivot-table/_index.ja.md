---
title: ピボットテーブルへのスタイルの適用
linktitle: ピボットテーブルへのスタイルの適用
description: Aspose.Cells for Python via Java でピボットテーブルに組み込みスタイルとカスタムスタイルを適用する方法を学びます。レガシー XLS のオートフォーマット、Excel 2007+ のモダンな名前付きスタイル、カスタムピボットテーブルスタイル、FormatAll ショートカットをカバーします。
keywords: Aspose.Cells Python via Java ピボットテーブル スタイル, PivotTableStyleType, AutoFormatType, FormatAll, カスタム スタイル, PivotTableStyleName, TableStyles
type: docs
weight: 200
url: /ja/python-java/apply-style-to-pivot-table/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells は、レガシーのピボットオートフォーマット（`.xls` ファイル向け）と、モダンな名前付きまたはカスタムのピボットテーブルスタイル（`.xlsx`、`.xlsm`、`.xlsb` ファイル向け）の両方をサポートしています。使用する API は、ワークブックを読み込んだ形式ではなく、保存先のファイル形式によって決まります。

{{% /alert %}}

## **概要**

Aspose.Cells は、ピボットテーブル向けに 2 つの並列スタイル API を提供します。これらのどちらを使用するかは、ワークブックを読み込んだ形式ではなく、保存先のファイル形式によって決まります。`.xls` ファイルから読み込んだワークブックを `.xlsx` として再保存することも可能で、その場合はレガシーのスタイル API ではなく、モダンなスタイル API が適用されます。

レガシーの `.xls` 出力の場合は、`pivotTable.setAutoFormatType(int)` メソッドを `com.aspose.cells.pivot.PivotTableAutoFormatType` 列挙型とともに使用します。この API は、旧バージョンの Excel でピボットテーブル用に提供されていたオートフォーマットピッカーに対応しています。

モダンの `.xlsx`、`.xlsm`、`.xlsb` 出力の場合は、2 種類のスタイル API を利用できます。

- `pivotTable.setPivotTableStyleType(int)` は、組み込みの名前付きスタイル（ライトテーマおよびダークテーマ、Excel 2017 で追加されたスタイルを含む）の中から 1 つを選択します。これらのプリセットは読み取り専用です。
- `pivotTable.setPivotTableStyleName(String)` は、`workbook.getWorksheets().getTableStyles().addPivotTableStyle(String)` を通じて自分で定義したカスタムスタイルを選択します。プリセットで提供される色、罫線、フォント以外の変更が必要な場合は、カスタムスタイルが必須です。

さらに、`pivotTable.formatAll(Style)` はショートカットであり、単一の `Style` オブジェクトをピボットのすべてのセルに適用し、上記のいずれかのスタイル名 API で設定された内容を上書きします。基になるテーマに関係なく統一された外観が必要な場合に便利です。

## **レガシー XLS プリセットオートフォーマットの適用**

ピボットテーブルの `setAutoFormatType` メソッドは、`com.aspose.cells.pivot.PivotTableAutoFormatType` 列挙型の値を受け取ります。利用可能な値は `REPORT_1` ～ `REPORT_10`、`CLASSIC`、`TABLE_1` ～ `TABLE_10` です。

{{% alert color="primary" %}}

`setAutoFormatType` は、ワークブックが `.xls` として保存される場合にのみ有効です。同じワークブックが `.xlsx`、`.xlsm`、`.xlsb` として保存される場合、Excel はこの設定を無視し、`setPivotTableStyleType` と `setPivotTableStyleName` の設定にフォールバックします。

{{% /alert %}}

次の例では、新しいワークブックを読み込み、Fruit/Year/Amount のサンプルデータを入力し、ピボットテーブルを追加し、`PivotTableAutoFormatType.REPORT_5` を適用して、結果を `.xls` として保存します。

{{% alert color="primary" %}}

**列フィールドがないのはなぜですか？** Report シリーズの自動書式（`Report1`〜`Report10`、`Table1`〜`Table10`）は、従来の Excel で**単一次元のピボットテーブル**（行フィールドと値のみ）のために設計されたものであり、列フィールドのヘッダーに対する組み込みのスタイル設定はありません。ピボットテーブルに列フィールドが必要な場合は、代わりに下のシナリオ 2 のモダンな `PivotTableStyleType` プリセットを使用してください。これらはモダンな Excel が使用する二次元レイアウト向けに設計されています。

{{% /alert %}}

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, PivotFieldType, PivotTableAutoFormatType

# シナリオ 1: レガシー XLS プリセット自動書式を適用する
# 使用中の API: PivotTable.AutoFormatType
# 対象ファイル形式: .xls (レガシー)
# 完全なサンプルとデータファイルについては、https://github.com/aspose-cells/Aspose.Cells-for-Python-via-Java を参照してください

# 新しいワークブックを作成
workbook = Workbook()

# 最初のワークシートを取得
sheet = workbook.getWorksheets().get(0)

# ヘッダー行 (Fruit, Year, Amount) と
# 2020 年および 2021 年の grape、blueberry、kiwi、cherry をカバーする 9 つのデータ行を含むソースデータを設定
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

# 出力セル E3 に「Pivot1」という名前のピボットテーブルをソース範囲 A1:C10 を使用して追加
pivotIndex = sheet.getPivotTables().add("A1:C10", "E3", "Pivot1")
pivotTable = sheet.getPivotTables().get(pivotIndex)

# フィールドを割り当て: Fruit -> 行、Year -> 列、Amount -> データ
pivotTable.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.Data, "Amount")

# レガシー XLS プリセット自動書式「Report5」を適用
# 注: このプロパティは .xls 形式で保存する場合にのみ有効です。
# .xlsx/.xlsm/.xlsb として保存する場合、Excel は AutoFormatType を無視し、
# PivotTableStyleType / PivotTableStyleName で指定された値を使用します。
pivotTable.setAutoFormatType(PivotTableAutoFormatType.Report5)

# ワークブックをレガシー .xls 形式で保存
workbook.save("output.xls")

jpype.shutdownJVM()
```

## **モダンな名前付きプリセットピボットテーブルスタイルの適用**

ピボットテーブルの `setPivotTableStyleType` メソッドは、`com.aspose.cells.PivotTableStyleType` 列挙型の値を受け取ります。この列挙型は、ライトテーマ `PIVOT_TABLE_STYLE_LIGHT_1` ～ `PIVOT_TABLE_STYLE_LIGHT_28` と、ダークテーマ `PIVOT_TABLE_STYLE_DARK_1` ～ `PIVOT_TABLE_STYLE_DARK_28` をカバーしています。Excel 2017 で追加されたスタイル（ライトテーマとダークテーマの第二波）は、同じ列挙型を通じてアクセスできます。

これは、モダンなファイル形式に対して推奨される API です。レガシーのオートフォーマットとは異なり、ここで選択されたスタイルは Excel によって忠実にレンダリングされ、他の Office ツールとのラウンドトリップでも維持されます。

次の例では、同じ Fruit/Year/Amount データを使用し、同じピボットテーブルを作成し、`PivotTableStyleType.PIVOT_TABLE_STYLE_DARK_1` を適用して、ワークブックを `.xlsx` として保存します。

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotTableStyleType, PivotFieldType

# シナリオ 2: PivotTableStyleType を使用して Excel 2007+ のモダンな名前付きプリセットスタイルを適用します。
# 対象ファイル形式: .xlsx。PivotTableStyleType 列挙型は Aspose.Cells 名前空間に存在します
# (Aspose.Cells.Pivot ではなく) — そのため、追加の using は必要ありません。
# GitHub reference: https://github.com/aspose-cells/Aspose.Cells-for-Python-via-Java

workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)

# ヘッダー行: Fruit / Year / Amount
worksheet.getCells().get("A1").putValue("Fruit")
worksheet.getCells().get("B1").putValue("Year")
worksheet.getCells().get("C1").putValue("Amount")

# Fruit / Year / Amount の 9 件のデータ行
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

# E3 に「Pivot1」という名前のピボットテーブルを追加し、データソースは A1:C10
pivotIndex = worksheet.getPivotTables().add("A1:C10", "E3", "Pivot1")
pivotTable = worksheet.getPivotTables().get(pivotIndex)

# ピボットフィールドを割り当て: Fruit → 行エリア、Year → 列エリア、Amount → データエリア
pivotTable.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.Column, "Year")
pivotTable.addFieldToArea(PivotFieldType.Data, "Amount")

# Excel 2007+ のモダンな名前付きプリセットピボットスタイルを適用します。
# PivotTableStyleType は .xlsx / .xlsm / .xlsb ファイル用の正しい API です。AutoFormatType は
# これらの形式では Excel によって無視されます。PivotTableStyleDark1 はダークテーマ
# ファミリー (PivotTableStyleDark1..PivotTableStyleDark28) に属し、同じ列挙型は新しい
# Excel 2017 のライト/ダークテーマ (PivotTableStyleLight1..Light28 / Dark1..Dark28) も公開しています。
pivotTable.setPivotTableStyleType(PivotTableStyleType.PivotTableStyleDark1)

# モダンな .xlsx として保存 — これは PivotTableStyleType が意味を持つ形式です。
workbook.save("output.xlsx")

jpype.shutdownJVM()
```

## **カスタムピボットテーブルスタイルの定義と適用**

組み込みプリセットは変更できません。色、罫線、フォントを上書きする必要がある場合は、必ずカスタムピボットスタイルを定義する必要があります。ワークフローは次の 3 ステップで構成されます。

1. `workbook.getWorksheets().getTableStyles().addPivotTableStyle(String name)` を使用して、ワークブックの `TableStyles` コレクションにカスタムスタイルを追加します。これは新しく作成されたスタイルのインデックスを返します。
2. `tableStyle.getTableStyleElements().add(TableStyleElementType)` を通じて要素（`WHOLE_TABLE` や `GRAND_TOTAL_ROW` など）を追加し、`tableStyleElement.setElementStyle(Style)` を通じて各要素に `Style` を割り当てて、スタイルを設定します。
3. スタイル名とともに `pivotTable.setPivotTableStyleName(String)` を呼び出して、カスタムスタイルをピボットに適用します。ここでは `setPivotTableStyleType` を使用しないでください。このメソッドは組み込みプリセットを選択するためです。

{{% alert color="primary" %}}

`setPivotTableStyleName` と `setPivotTableStyleType` は相互に置き換え可能な関係ではありません。組み込みプリセットには `setPivotTableStyleType` を、`addPivotTableStyle` を通じて定義したカスタムスタイルには `setPivotTableStyleName` を使用してください。両方を設定しても問題ありませんが、意図したソースに合致する一方のみがレンダリングされます。

{{% /alert %}}

利用可能な `TableStyleElementType` の値には、`WHOLE_TABLE`、`FIRST_ROW`、`LAST_ROW`、`FIRST_COLUMN`、`LAST_COLUMN`、`GRAND_TOTAL_ROW`、`GRAND_TOTAL_COLUMN`、`PAGE_FIELD_LABELS`、`PAGE_FIELD_VALUES` が含まれます。

次の例では、`WHOLE_TABLE` に細い黒い罫線を持ち、`GRAND_TOTAL_ROW` に太字の赤いフォントを持つカスタムピボットスタイルを定義し、`setPivotTableStyleName` を通じて適用して、`.xlsx` として保存します。

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat
from asposecells.api import PivotFieldType, TableStyleElementType, BorderType, CellBorderType
from java.awt import Color

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

# A1:C10をソースとするピボットテーブルを追加、E3に配置、名前は "Pivot1"
pivotIndex = worksheet.getPivotTables().add("A1:C10", "E3", "Pivot1")
pivotTable = worksheet.getPivotTables().get(pivotIndex)

pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year")
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount")

# ステップ1: 新しいカスタムピボットテーブルスタイルを登録し、そのインデックスを取得
styleIndex = workbook.getWorksheets().getTableStyles().addPivotTableStyle("CustomPivotStyle")
tableStyle = workbook.getWorksheets().getTableStyles().get(styleIndex)

# ステップ2: WholeTable要素を追加し、4辺すべてに細い黒い罫線を適用
wholeTableElementIndex = tableStyle.getTableStyleElements().add(TableStyleElementType.WHOLE_TABLE)
wholeTableElement = tableStyle.getTableStyleElements().get(wholeTableElementIndex)
wholeTableStyle = workbook.createStyle()
wholeTableStyle.getBorders().get(BorderType.TOP_BORDER).setLineStyle(CellBorderType.THIN)
wholeTableStyle.getBorders().get(BorderType.TOP_BORDER).setColor(Color.BLACK)
wholeTableStyle.getBorders().get(BorderType.BOTTOM_BORDER).setLineStyle(CellBorderType.THIN)
wholeTableStyle.getBorders().get(BorderType.BOTTOM_BORDER).setColor(Color.BLACK)
wholeTableStyle.getBorders().get(BorderType.LEFT_BORDER).setLineStyle(CellBorderType.THIN)
wholeTableStyle.getBorders().get(BorderType.LEFT_BORDER).setColor(Color.BLACK)
wholeTableStyle.getBorders().get(BorderType.RIGHT_BORDER).setLineStyle(CellBorderType.THIN)
wholeTableStyle.getBorders().get(BorderType.RIGHT_BORDER).setColor(Color.BLACK)
wholeTableElement.setElementStyle(wholeTableStyle)

# ステップ3: GrandTotalRow要素を追加し、太字の赤いフォントを適用
grandTotalElementIndex = tableStyle.getTableStyleElements().add(TableStyleElementType.GRAND_TOTAL_ROW)
grandTotalElement = tableStyle.getTableStyleElements().get(grandTotalElementIndex)
grandTotalStyle = workbook.createStyle()
grandTotalStyle.getFont().setBold(True)
grandTotalStyle.getFont().setColor(Color.RED)
grandTotalElement.setElementStyle(grandTotalStyle)

# ステップ4: カスタムスタイルを名前で適用 (PivotTableStyleTypeではない、これは組み込みプリセット用)
pivotTable.setPivotTableStyleName("CustomPivotStyle")

workbook.save("output.xlsx")

jpype.shutdownJVM()
```

## **FormatAll を使用したすべてのピボットセルへの 1 つのスタイルの適用**

`pivotTable.formatAll(Style)` はショートカットであり、単一の `Style` オブジェクトをピボットテーブルのすべてのセル（データ領域、行と列のヘッダー、および集計セルを含む）に適用します。`setPivotTableStyleType` または `setPivotTableStyleName` を通じて以前に設定された内容はすべて上書きされます。

{{% alert color="primary" %}}

`formatAll` は `setPivotTableStyleType` と `setPivotTableStyleName` の両方を上書きします。ピボット全体でテーマ非依存の統一された外観が必要な場合にのみ使用してください。

{{% /alert %}}

次の例では、黄色の単色塗りつぶし、太字の濃紺フォント、およびすべての辺に細い黒い罫線を持つ `Style` を作成し、それを `formatAll` で適用して、`.xlsx` として保存します。

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, Style
from asposecells.api import Color
from asposecells.api import PivotTable, PivotFieldType
from asposecells.api import BorderType, CellBorderType, BackgroundType

# シナリオ 4: FormatAll を使用してすべてのピボットテーブルセルに単一のスタイルを適用
# 使用中の API: PivotTable.FormatAll(Style)
# ターゲット形式: .xlsx
# GitHub リファレンス: Aspose.Cells-for-Python-via-Java リポジトリを参照 — ピボットテーブルのスタイル設定例

workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)

# ソースデータを入力: ヘッダー行 (行 1) + 9 データ行 (行 2-10)
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

# ピボットテーブルのすべてのセルに強制する Style を作成
style = workbook.createStyle()
style.setForegroundColor(Color.YELLOW)
style.setPattern(BackgroundType.SOLID)
style.getFont().setIsBold(True)
style.getFont().setColor(Color.DARK_BLUE)
style.getBorders().get(BorderType.TOP_BORDER).setLineStyle(CellBorderType.THIN)
style.getBorders().get(BorderType.TOP_BORDER).setColor(Color.BLACK)
style.getBorders().get(BorderType.BOTTOM_BORDER).setLineStyle(CellBorderType.THIN)
style.getBorders().get(BorderType.BOTTOM_BORDER).setColor(Color.BLACK)
style.getBorders().get(BorderType.LEFT_BORDER).setLineStyle(CellBorderType.THIN)
style.getBorders().get(BorderType.LEFT_BORDER).setColor(Color.BLACK)
style.getBorders().get(BorderType.RIGHT_BORDER).setLineStyle(CellBorderType.THIN)
style.getBorders().get(BorderType.RIGHT_BORDER).setColor(Color.BLACK)

# FormatAll を適用: この単一のスタイルをピボットテーブルのすべてのセルに強制し、
# 以前に設定された PivotTableStyleType / PivotTableStyleName をすべて上書きします
pivotTable.formatAll(style)

# ワークブックを最新の .xlsx 形式で保存
workbook.save("output.xlsx")

jpype.shutdownJVM()
```

## **どのスタイル API を使用すべきか？**

スタイル API の選択は、保存先のファイル形式によって決まります。以下の表をクイックリファレンスとして使用してください。

| 対象ファイル形式 | 使用する API | メモ |
|---|---|---|
| `.xls`（レガシー） | `pivotTable.setAutoFormatType(int)` | `com.aspose.cells.pivot.PivotTableAutoFormatType` の値（例: `REPORT_1`–`REPORT_10`、`CLASSIC`、`TABLE_1`–`TABLE_10`）。モダン形式で保存する場合は無視されます。 |
| `.xlsx` / `.xlsm` / `.xlsb`（モダン、組み込みスタイル） | `pivotTable.setPivotTableStyleType(int)` | `com.aspose.cells.PivotTableStyleType` の値（ライト/ダークテーマ、Excel 2017 で追加されたものを含む）。 |
| `.xlsx` / `.xlsm` / `.xlsb`（モダン、カスタムスタイル） | `pivotTable.setPivotTableStyleName(String)` + `tableStyles.addPivotTableStyle(String)` | 組み込みプリセットでは不十分な場合に使用します。`tableStyleElement.setElementStyle(Style)` を通じて設定します。 |
| すべての形式（統一上書き） | `pivotTable.formatAll(Style)` | ピボット全体の他のすべてのスタイル設定を上書きするショートカットです。 |

迷った場合は、`.xlsx` として保存し、組み込みテーマには `setPivotTableStyleType` を、カスタムテーマには `setPivotTableStyleName` を使用してください。

## **関連記事**

- [Aspose.Cells for Aspose.Cells for Python via Java でのピボットテーブルの更新](/cells/ja/python-java/refresh-pivot-table/)

{{< app/cells/assistant language="python" >}}