---
title: Aspose.Cells for Python via .NET でピボットテーブルにスタイルを適用する
linktitle: Aspose.Cells for Python via .NET でピボットテーブルにスタイルを適用する
description: Aspose.Cells for Python via .NET でピボットテーブルに組み込みスタイルとカスタムスタイルを適用する方法を学びます。レガシー XLS の自動書式、Excel 2007 以降のモダンな名前付きスタイル、カスタム ピボットテーブル スタイル、FormatAll ショートカットについて説明します。
keywords: Aspose.Cells Python via .NET ピボットテーブル スタイル, PivotTableStyleType, AutoFormatType, FormatAll, カスタム スタイル, PivotTableStyleName, TableStyles
type: docs
weight: 200
url: /ja/python-net/apply-style-to-pivot-table/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells は、レガシーのピボット自動書式 (`.xls` ファイル向け) と、モダンな名前付きピボットテーブル スタイルまたはカスタム スタイル (`.xlsx`、`.xlsm`、`.xlsb` ファイル向け) の両方を適用することをサポートします。呼び出す API は、ワークブックを読み込んだ形式ではなく、保存先のファイル形式によって決まります。
{{% /alert %}}

## **概要**
Aspose.Cells は、ピボットテーブル用に 2 つの並列スタイル API を提供します。どちらを使用するかは、ワークブックを読み込んだ形式ではなく、保存先のファイル形式によって決まります。`.xls` ファイルから読み込んだワークブックを `.xlsx` として再保存する場合、レガシー API ではなくモダンなスタイル API が適用されます。
- `PivotTable.pivot_table_style_type` は、組み込みの名前付きスタイル (ライト テーマとダーク テーマ、Excel 2017 で追加されたスタイルを含む) のいずれかを選択します。これらのプリセットは読み取り専用です。
- `PivotTable.pivot_table_style_name` は、`workbook.worksheets.table_styles.add_pivot_table_style(...)` を使用して独自に定義したカスタム スタイルを選択します。プリセットで提供される範囲を超えて色、罫線、フォントを変更したい場合は、カスタム スタイルが必要です。
さらに、`PivotTable.format_all(Style)` は、単一の `Style` オブジェクトをピボットのすべてのセルに適用するショートカットであり、上記のいずれかのスタイル名 API で設定された内容を上書きします。これは、基になるテーマに関係なく均一な外観が必要な場合に役立ちます。

## **レガシー XLS のプリセット自動書式を適用する**
`PivotTable.auto_format_type` は、`aspose.cells.pivot.PivotTableAutoFormatType` 列挙体の値を受け取ります。利用可能な値は、`REPORT_1` 〜 `REPORT_10`、`CLASSIC`、`TABLE_1` 〜 `TABLE_10` です。
次の例では、新しいワークブックを読み込み、Fruit/Year/Amount のサンプル データを入力し、ピボットテーブルを追加して `PivotTableAutoFormatType.REPORT5` を適用し、結果を `.xls` として保存します。

{{% alert color="primary" %}}
**なぜ列フィールドがないのか？** Report シリーズ自動書式 (`Report1` 〜 `Report10`、`Table1` 〜 `Table10`) は、クラシック Excel で行フィールドと値のみの **単一次元のピボットテーブル** 向けに設計されており、列フィールド ヘッダー用の組み込みスタイルがありません。ピボットに列フィールドが必要な場合は、代わりに [シナリオ 2](#apply-a-modern-named-preset-pivot-table-style) のモダンな `PivotTableStyleType` プリセットを使用してください。これは、モダン Excel が使用する二次元レイアウト向けに設計されています。
{{% /alert %}}

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType
from aspose.cells.pivot import PivotTableAutoFormatType
# シナリオ 1: 従来の XLS プリセット自動フォーマットを適用する
# 使用中の API: PivotTable.AutoFormatType
# ターゲットファイル形式: .xls (従来)
# 完全な例とデータファイルについては、https://github.com/aspose-cells/Aspose.Cells-for-.NET を参照してください
# 新しいワークブックを作成する
workbook = ac.Workbook()
# 最初のワークシートを取得する
sheet = workbook.worksheets[0]
# ヘッダー行 (Fruit, Year, Amount) でソースデータを入力する
# 2020年と2021年にわたる grape、blueberry、kiwi、cherry の 9 データ行
sheet.cells.get(0, 0).put_value("Fruit")
sheet.cells.get(0, 1).put_value("Year")
sheet.cells.get(0, 2).put_value("Amount")
sheet.cells.get(1, 0).put_value("grape")
sheet.cells.get(1, 1).put_value(2020)
sheet.cells.get(1, 2).put_value(50)
sheet.cells.get(2, 0).put_value("blueberry")
sheet.cells.get(2, 1).put_value(2020)
sheet.cells.get(2, 2).put_value(30)
sheet.cells.get(3, 0).put_value("kiwi")
sheet.cells.get(3, 1).put_value(2020)
sheet.cells.get(3, 2).put_value(25)
sheet.cells.get(4, 0).put_value("cherry")
sheet.cells.get(4, 1).put_value(2020)
sheet.cells.get(4, 2).put_value(40)
sheet.cells.get(5, 0).put_value("grape")
sheet.cells.get(5, 1).put_value(2021)
sheet.cells.get(5, 2).put_value(60)
sheet.cells.get(6, 0).put_value("blueberry")
sheet.cells.get(6, 1).put_value(2021)
sheet.cells.get(6, 2).put_value(35)
sheet.cells.get(7, 0).put_value("kiwi")
sheet.cells.get(7, 1).put_value(2021)
sheet.cells.get(7, 2).put_value(28)
sheet.cells.get(8, 0).put_value("cherry")
sheet.cells.get(8, 1).put_value(2021)
sheet.cells.get(8, 2).put_value(45)
sheet.cells.get(9, 0).put_value("grape")
sheet.cells.get(9, 1).put_value(2020)
sheet.cells.get(9, 2).put_value(45)
# 宛先セル E3 に "Pivot1" という名前のピボットテーブルを、ソース範囲 A1:C10 を使用して追加する
pivot_index = sheet.pivot_tables.add("A1:C10", "E3", "Pivot1")
pivot_table = sheet.pivot_tables[pivot_index]
# フィールドを割り当てる: Fruit -> 行、Amount -> データ
pivot_table.add_field_to_area(PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")
# 従来の XLS プリセット自動フォーマット "Report5" を適用する
# 注意: このプロパティは .xls として保存する場合にのみ意味があります。
# .xlsx/.xlsm/.xlsb として保存された場合、Excel は AutoFormatType を無視します
# PivotTableStyleType / PivotTableStyleName が指定するものを使用します。
pivot_table.auto_format_type = PivotTableAutoFormatType.REPORT5
# ワークブックを従来の .xls 形式で保存する
workbook.save("output.xls")
```

## **モダンな名前付きプリセット ピボットテーブル スタイルを適用する**

`pivot_table.pivot_table_style_type` は、Excel 2007 でピボットテーブルに導入された組み込みの名前付きスタイルから 1 つを選択します。`PivotTableStyleType` 列挙型は、3 つのテーマファミリーを公開しています。`PIVOT_TABLE_STYLE_LIGHT1` から `PIVOT_TABLE_STYLE_LIGHT28` までのライトファミリー、`PIVOT_TABLE_STYLE_MEDIUM1` から `PIVOT_TABLE_STYLE_MEDIUM28` までのメディアファミリー、`PIVOT_TABLE_STYLE_DARK1` から `PIVOT_TABLE_STYLE_DARK28` までのダークファミリーです。また、`None` と `Custom` も定義しています。各ファミリーで番号が大きいメンバーは、Excel 2017 で追加されたスタイルです。
これらのプリセットは読み取り専用です。プリセットprovidesの範囲を超えて色、罫線、またはフォントを変更する必要がある場合は、代わりにカスタムピボットスタイルを定義する必要があります。詳細については、[シナリオ 3](#define-and-apply-a-custom-pivot-table-style) を参照してください。

{{% alert color="primary" %}}
**なぜ現代のプリセットを使用し、レポートシリーズの自動形式を使用しないのでしょうか？** `PivotTableAutoFormatType` の `Report1` から `Report10` まで、および `Table1` から `Table10` までの値は、ピボットの列フィールドより前に定義されたものです。そのため、列フィールドの見出しに対するスタイル設定が含まれず、Excel はこれらの見出しにスタイルを適用せずに表示します。`PivotTableStyleType` のプリセットは、現代の Excel が使用する二次元レイアウト向けに設計されており、行フィールドと列フィールドの見出しに同じようにスタイルを適用します。
{{% /alert %}}

このシナリオでは、シナリオ 1 の Fruit/Year/Amount データセットを再利用し、`PivotFieldType.COLUMN` を使用して `Fruit` 行フィールドに加えて `Year` を列領域に追加し、`pivot_table.pivot_table_style_type` でダークテーマのプリセット `PIVOT_TABLE_STYLE_DARK1` を適用します。結果は、`PivotTableStyleType` が有意義な形式である `.xlsx` として保存します。

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType, PivotTableStyleType
# Scenario 2: Apply a modern Excel 2007+ named preset style using PivotTableStyleType.
# Target file format: .xlsx. PivotTableStyleType lives in aspose.cells.pivot,
# so it is imported explicitly alongside PivotFieldType.
# GitHub reference: https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Examples/CSharp/PivotTables/ApplyStyleToPivotTable2.cs
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
# Header row: Fruit / Year / Amount
worksheet.cells.get("A1").put_value("Fruit")
worksheet.cells.get("B1").put_value("Year")
worksheet.cells.get("C1").put_value("Amount")
# 9 data rows of Fruit / Year / Amount
worksheet.cells.get("A2").put_value("Grape")
worksheet.cells.get("B2").put_value(2020)
worksheet.cells.get("C2").put_value(100)
worksheet.cells.get("A3").put_value("Blueberry")
worksheet.cells.get("B3").put_value(2020)
worksheet.cells.get("C3").put_value(150)
worksheet.cells.get("A4").put_value("Kiwi")
worksheet.cells.get("B4").put_value(2020)
worksheet.cells.get("C4").put_value(200)
worksheet.cells.get("A5").put_value("Cherry")
worksheet.cells.get("B5").put_value(2020)
worksheet.cells.get("C5").put_value(180)
worksheet.cells.get("A6").put_value("Grape")
worksheet.cells.get("B6").put_value(2021)
worksheet.cells.get("C6").put_value(120)
worksheet.cells.get("A7").put_value("Blueberry")
worksheet.cells.get("B7").put_value(2021)
worksheet.cells.get("C7").put_value(170)
worksheet.cells.get("A8").put_value("Kiwi")
worksheet.cells.get("B8").put_value(2021)
worksheet.cells.get("C8").put_value(210)
worksheet.cells.get("A9").put_value("Cherry")
worksheet.cells.get("B9").put_value(2021)
worksheet.cells.get("C9").put_value(190)
worksheet.cells.get("A10").put_value("Grape")
worksheet.cells.get("B10").put_value(2021)
worksheet.cells.get("C10").put_value(130)
# Add a pivot table at E3 named "Pivot1", sourced from A1:C10
pivot_index = worksheet.pivot_tables.add("A1:C10", "E3", "Pivot1")
pivot_table = worksheet.pivot_tables[pivot_index]
# Assign pivot fields: Fruit -> Row area, Year -> Column area, Amount -> Data area
pivot_table.add_field_to_area(PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")
# Apply a modern Excel 2007+ named preset pivot style.
# PivotTableStyleType is the correct API for .xlsx / .xlsm / .xlsb files; AutoFormatType
# is ignored by Excel for those formats. PIVOT_TABLE_STYLE_DARK1 belongs to the dark-theme
# family (PIVOT_TABLE_STYLE_DARK1..PIVOT_TABLE_STYLE_DARK28), and the same enum also exposes
# the newer Excel 2017 themes (PIVOT_TABLE_STYLE_LIGHT1..LIGHT28 / DARK1..DARK28).
pivot_table.pivot_table_style_type = PivotTableStyleType.PIVOT_TABLE_STYLE_DARK1
# Save as modern .xlsx — this is the format for which PivotTableStyleType is meaningful.
workbook.save("output.xlsx")
```
## **カスタム ピボットテーブル スタイルを定義して適用する**
組み込みプリセットは変更できません。色、罫線、フォントを上書きする必要がある場合は、カスタム ピボット スタイルを定義する必要があります。ワークフローは 3 つの手順で構成されています。
1. `workbook.worksheets.table_styles.add_pivot_table_style(name)` を介して、ワークブックの `table_styles` コレクションにカスタム スタイルを追加します。これは、新しく作成されたスタイルのインデックスを返します。
2. `table_style.table_style_elements.add(TableStyleElementType)` を介して要素 (`WHOLE_TABLE` や `GRAND_TOTAL_ROW` など) を追加してスタイルを構成し、`table_style_element.set_element_style(Style)` を介して各要素に `Style` を割り当てます。
3. `PivotTable.pivot_table_style_name` をスタイルの名前に設定して、カスタム スタイルをピボットに適用します。ここでは `pivot_table_style_type` を使用しないでください。このプロパティは組み込みプリセットを選択するためです。

{{% alert color="primary" %}}
`pivot_table_style_name` と `pivot_table_style_type` は互いに交換できません。組み込みプリセットには `pivot_table_style_type` を、`add_pivot_table_style` を通じて定義したカスタム スタイルには `pivot_table_style_name` を使用してください。両方を設定しても問題ありませんが、意図したソースに一致する一方のみがレンダリングされます。
利用可能な `TableStyleElementType` の値には、`WHOLE_TABLE`、`FIRST_ROW`、`LAST_ROW`、`FIRST_COLUMN`、`LAST_COLUMN`、`GRAND_TOTAL_ROW`、`GRAND_TOTAL_COLUMN`、`PAGE_FIELD_LABELS`、`PAGE_FIELD_VALUES` があります。
次の例では、`WHOLE_TABLE` に細い黒い罫線、`GRAND_TOTAL_ROW` に太字の赤いフォントを持つカスタム ピボット スタイルを定義し、`pivot_table_style_name` を介して適用し、`.xlsx` として保存します。
{{% /alert %}}

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType
from aspose.cells.tables import TableStyleElementType
from aspose.pydrawing import Color
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
# ソースデータを入力: ヘッダー行 + 9データ行 (A1:C10)
worksheet.cells.get("A1").put_value("Fruit")
worksheet.cells.get("B1").put_value("Year")
worksheet.cells.get("C1").put_value("Amount")
worksheet.cells.get("A2").put_value("Grape")
worksheet.cells.get("B2").put_value(2020)
worksheet.cells.get("C2").put_value(100)
worksheet.cells.get("A3").put_value("Blueberry")
worksheet.cells.get("B3").put_value(2020)
worksheet.cells.get("C3").put_value(200)
worksheet.cells.get("A4").put_value("Kiwi")
worksheet.cells.get("B4").put_value(2020)
worksheet.cells.get("C4").put_value(300)
worksheet.cells.get("A5").put_value("Cherry")
worksheet.cells.get("B5").put_value(2020)
worksheet.cells.get("C5").put_value(400)
worksheet.cells.get("A6").put_value("Grape")
worksheet.cells.get("B6").put_value(2021)
worksheet.cells.get("C6").put_value(500)
worksheet.cells.get("A7").put_value("Blueberry")
worksheet.cells.get("B7").put_value(2021)
worksheet.cells.get("C7").put_value(600)
worksheet.cells.get("A8").put_value("Kiwi")
worksheet.cells.get("B8").put_value(2021)
worksheet.cells.get("C8").put_value(700)
worksheet.cells.get("A9").put_value("Cherry")
worksheet.cells.get("B9").put_value(2021)
worksheet.cells.get("C9").put_value(800)
worksheet.cells.get("A10").put_value("Grape")
worksheet.cells.get("B10").put_value(2021)
worksheet.cells.get("C10").put_value(900)
# A1:C10 をソースとし、E3 に配置される「Pivot1」という名前のピボットテーブルを追加
pivot_index = worksheet.pivot_tables.add("A1:C10", "E3", "Pivot1")
pivot_table = worksheet.pivot_tables[pivot_index]
pivot_table.add_field_to_area(PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")
# ステップ 1: 新しいカスタムピボットテーブルスタイルを登録し、インデックスを取得
style_index = workbook.worksheets.table_styles.add_pivot_table_style("CustomPivotStyle")
table_style = workbook.worksheets.table_styles[style_index]
# ステップ 2: WholeTable 要素を追加し、4辺すべてに細い黒枠線を適用
whole_table_element_index = table_style.table_style_elements.add(TableStyleElementType.WHOLE_TABLE)
whole_table_element = table_style.table_style_elements[whole_table_element_index]
whole_table_style = workbook.create_style()
whole_table_style.borders.get(ac.BorderType.TOP_BORDER).line_style = ac.CellBorderType.THIN
whole_table_style.borders.get(ac.BorderType.TOP_BORDER).color = Color.black
whole_table_style.borders.get(ac.BorderType.BOTTOM_BORDER).line_style = ac.CellBorderType.THIN
whole_table_style.borders.get(ac.BorderType.BOTTOM_BORDER).color = Color.black
whole_table_style.borders.get(ac.BorderType.LEFT_BORDER).line_style = ac.CellBorderType.THIN
whole_table_style.borders.get(ac.BorderType.LEFT_BORDER).color = Color.black
whole_table_style.borders.get(ac.BorderType.RIGHT_BORDER).line_style = ac.CellBorderType.THIN
whole_table_style.borders.get(ac.BorderType.RIGHT_BORDER).color = Color.black
whole_table_element.set_element_style(whole_table_style)
# ステップ 3: GrandTotalRow 要素を追加し、太字の赤色フォントを適用
grand_total_element_index = table_style.table_style_elements.add(TableStyleElementType.GRAND_TOTAL_ROW)
grand_total_element = table_style.table_style_elements[grand_total_element_index]
grand_total_style = workbook.create_style()
grand_total_style.font.is_bold = True
grand_total_style.font.color = Color.red
grand_total_element.set_element_style(grand_total_style)
# ステップ 4: カスタムスタイルを名前で適用 (組み込みプリセット用の PivotTableStyleType ではない)
pivot_table.pivot_table_style_name = "CustomPivotStyle"
workbook.save("output.xlsx")
```

## **format_all を使用して 1 つのスタイルをすべてのピボット セルに適用する**
`PivotTable.format_all(Style)` は、データ領域、行および列ヘッダー、合計を含む、ピボット テーブルのすべてのセルに単一の `Style` オブジェクトを適用するショートカットです。`pivot_table_style_type` または `pivot_table_style_name` を介して以前に設定された内容はすべて上書きされます。

{{% alert color="primary" %}}
`format_all` は `pivot_table_style_type` と `pivot_table_style_name` の両方を上書きします。ピボット全体で均一なテーマ非依存の外観が必要な場合にのみ使用してください。
次の例では、黄色の単色塗りつぶし、太字の濃い青色のフォント、すべての辺に細い黒い罫線を持つ `Style` を作成し、`format_all` で適用して `.xlsx` として保存します。
{{% /alert %}}

```python
from aspose.pydrawing import Color
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType
from aspose.cells import BackgroundType, CellBorderType, BorderType
# シナリオ 4: format_all を使用して、すべてのピボットテーブルセルに単一のスタイルを適用する
# 使用中の API: PivotTable.format_all(Style)
# 対象形式: .xlsx
# GitHub リファレンス: Aspose.Cells-for-.NET リポジトリを参照 — ピボットテーブルのスタイル設定例
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
# ソースデータを設定: ヘッダー行(1 行目)+ 9 つのデータ行(2 ～ 10 行目)
worksheet.cells.get("A1").put_value("Fruit")
worksheet.cells.get("B1").put_value("Year")
worksheet.cells.get("C1").put_value("Amount")
worksheet.cells.get("A2").put_value("Grape")
worksheet.cells.get("B2").put_value(2020)
worksheet.cells.get("C2").put_value(5000)
worksheet.cells.get("A3").put_value("Blueberry")
worksheet.cells.get("B3").put_value(2020)
worksheet.cells.get("C3").put_value(3000)
worksheet.cells.get("A4").put_value("Kiwi")
worksheet.cells.get("B4").put_value(2020)
worksheet.cells.get("C4").put_value(4000)
worksheet.cells.get("A5").put_value("Cherry")
worksheet.cells.get("B5").put_value(2020)
worksheet.cells.get("C5").put_value(2000)
worksheet.cells.get("A6").put_value("Grape")
worksheet.cells.get("B6").put_value(2021)
worksheet.cells.get("C6").put_value(6000)
worksheet.cells.get("A7").put_value("Blueberry")
worksheet.cells.get("B7").put_value(2021)
worksheet.cells.get("C7").put_value(3500)
worksheet.cells.get("A8").put_value("Kiwi")
worksheet.cells.get("B8").put_value(2021)
worksheet.cells.get("C8").put_value(4500)
worksheet.cells.get("A9").put_value("Cherry")
worksheet.cells.get("B9").put_value(2021)
worksheet.cells.get("C9").put_value(2500)
worksheet.cells.get("A10").put_value("Grape")
worksheet.cells.get("B10").put_value(2021)
worksheet.cells.get("C10").put_value(5500)
# ピボットテーブルを追加: ソース範囲 A1:C10、配置先のセル E3、名前 "Pivot1"
pivot_index = worksheet.pivot_tables.add("A1:C10", "E3", "Pivot1")
pivot_table = worksheet.pivot_tables[pivot_index]
# ピボットフィールドを割り当て: Fruit -> 行エリア、Year -> 列エリア、Amount -> データエリア
pivot_table.add_field_to_area(PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")
# ピボットテーブルのすべてのセルに強制適用される Style を作成
style = workbook.create_style()
style.foreground_color = Color.yellow
style.pattern = BackgroundType.SOLID
style.font.is_bold = True
style.font.color = Color.dark_blue
style.borders.get(BorderType.TOP_BORDER).line_style = CellBorderType.THIN
style.borders.get(BorderType.TOP_BORDER).color = Color.black
style.borders.get(BorderType.BOTTOM_BORDER).line_style = CellBorderType.THIN
style.borders.get(BorderType.BOTTOM_BORDER).color = Color.black
style.borders.get(BorderType.LEFT_BORDER).line_style = CellBorderType.THIN
style.borders.get(BorderType.LEFT_BORDER).color = Color.black
style.borders.get(BorderType.RIGHT_BORDER).line_style = CellBorderType.THIN
style.borders.get(BorderType.RIGHT_BORDER).color = Color.black
# format_all を適用: この単一のスタイルをピボットテーブルのすべてのセルに強制適用し、
# 以前に設定された PivotTableStyleType / PivotTableStyleName を上書きする
pivot_table.format_all(style)
# ワークブックを最新の .xlsx 形式で保存
workbook.save("output.xlsx")
```

## **どのスタイル API を使用すべきか？**
スタイル API の選択は、保存先のファイル形式によって異なります。次の表をクイック リファレンスとして使用してください。
| 保存先のファイル形式 | 使用する API | メモ |
|---|---|---|
| `.xls` (レガシー) | `PivotTable.auto_format_type` | `aspose.cells.pivot.PivotTableAutoFormatType` の値 (例: `REPORT_1` 〜 `REPORT_10`、`CLASSIC`、`TABLE_1` 〜 `TABLE_10`)。モダン形式で保存する場合は無視されます。 |
| `.xlsx` / `.xlsm` / `.xlsb` (モダン、組み込みスタイル) | `PivotTable.pivot_table_style_type` | `aspose.cells.PivotTableStyleType` の値 (ライト/ダーク テーマ、Excel 2017 で追加されたものを含む)。 |
| `.xlsx` / `.xlsm` / `.xlsb` (モダン、カスタム スタイル) | `PivotTable.pivot_table_style_name` + `worksheets.table_styles.add_pivot_table_style(...)` | 組み込みプリセットでは不十分な場合に使用します。`table_style_element.set_element_style(...)` を介して構成します。 |
| 任意の形式 (均一な上書き) | `PivotTable.format_all(Style)` | ピボット全体の他のすべてのスタイル設定を上書きするショートカット。 |
迷った場合は、`.xlsx` として保存し、組み込みテーマには `pivot_table_style_type` を、カスタム テーマには `pivot_table_style_name` を使用してください。


{{< app/cells/assistant language="python-net" >}}