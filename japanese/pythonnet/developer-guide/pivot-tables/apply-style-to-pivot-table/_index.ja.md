---
title: ピボットテーブルへのスタイルの適用
linktitle: ピボットテーブルへのスタイルの適用
description: Aspose.Cells for Python via .NET でレガシー XLS 自動書式からモダン Excel 2007+ の名前付きスタイル、カスタム ピボットテーブル スタイル、FormatAll ショートカットまで、ピボットテーブルに組み込みおよびカスタム スタイルを適用する方法を学習します。
keywords: Aspose.Cells Python via .NET ピボットテーブル スタイル, PivotTableStyleType, AutoFormatType, FormatAll, カスタム スタイル, PivotTableStyleName, TableStyles
type: docs
weight: 200
url: /ja/python-net/apply-style-to-pivot-table/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells は、レガシーのピボット自動書式 (`.xls` ファイル向け) と、モダンな名前付きまたはカスタム ピボットテーブル スタイル (`.xlsx`、`.xlsm`、`.xlsb` ファイル向け) の両方の適用をサポートしています。使用する API は、ワークブックを読み込んだ形式ではなく、ワークブックを保存するファイル形式によって決まります。

{{% /alert %}}

## **はじめに**

Aspose.Cells は、ピボットテーブル用の 2 つのパラレル スタイル API を提供します。どちらを選択するかは、読み込んだ形式ではなく、ワークブックを保存するファイル形式によって決まります。`.xls` ファイルから読み込んだワークブックを `.xlsx` として再保存する場合、レガシー API ではなくモダン スタイル API が適用されます。

レガシー `.xls` 出力の場合は、`PivotTable.auto_format_type` プロパティと `aspose.cells.pivot.PivotTableAutoFormatType` 列挙型を組み合わせて使用します。この API は、クラシック Excel でピボットテーブル用に提供されていた自動書式ピッカーに対応しています。

モダン `.xlsx`、`.xlsm`、`.xlsb` 出力の場合は、スタイル API の 2 種類が利用可能です。

- `PivotTable.pivot_table_style_type` は、組み込みの名前付きスタイル (Excel 2017 で追加されたスタイルを含む、ライト テーマとダーク テーマ) のいずれかを選択します。これらのプリセットは読み取り専用です。
- `PivotTable.pivot_table_style_name` は、`workbook.worksheets.table_styles.add_pivot_table_style(...)` を使用して自分で定義したカスタム スタイルを選択します。プリセットで提供される範囲を超えて色、罫線、フォントを変更する場合は、カスタム スタイルが必要です。

さらに、`PivotTable.format_all(Style)` は、単一の `Style` オブジェクトをピボットのすべてのセルに適用するショートカットで、上記のスタイル名 API で設定された内容をすべて上書きします。これは、基になるテーマに関係なく均一な外観が必要な場合に役立ちます。

## **レガシー XLS プリセット自動書式を適用する**

`PivotTable.auto_format_type` は、`aspose.cells.pivot.PivotTableAutoFormatType` 列挙型の値を受け取ります。利用可能な値は `REPORT_1` ～ `REPORT_10`、`CLASSIC`、および `TABLE_1` ～ `TABLE_10` です。

{{% alert color="primary" %}}

`auto_format_type` は、ワークブックが `.xls` として保存される場合にのみ有効です。同じワークブックが `.xlsx`、`.xlsm`、または `.xlsb` として保存される場合、Excel はこのプロパティを無視し、`pivot_table_style_type` および `pivot_table_style_name` 設定にフォールバックします。

{{% /alert %}}

次の例では、新しいワークブックを読み込み、Fruit/Year/Amount のサンプル データを設定し、ピボットテーブルを追加して、`PivotTableAutoFormatType.REPORT_5` を適用し、結果を `.xls` として保存します。

{{% alert color="primary" %}}

**列フィールドがないのはなぜですか？** Report シリーズの自動書式（`Report1`〜`Report10`、`Table1`〜`Table10`）は、従来の Excel で**単一次元のピボットテーブル**（行フィールドと値のみ）のために設計されたものであり、列フィールドのヘッダーに対する組み込みのスタイル設定はありません。ピボットテーブルに列フィールドが必要な場合は、代わりに下のシナリオ 2 のモダンな `PivotTableStyleType` プリセットを使用してください。これらはモダンな Excel が使用する二次元レイアウト向けに設計されています。

{{% /alert %}}

```python
import aspose.cells as ac

# シナリオ 1: レガシー XLS プレセット自動フォーマットを適用する
# 使用中の API: PivotTable.AutoFormatType
# 対象ファイル形式: .xls (レガシー)
# 完全な例とデータファイルについては、https://github.com/aspose-cells/Aspose.Cells-for-.NET を参照してください

# 新しいワークブックを作成
workbook = ac.Workbook()

# 最初のワークシートを取得
sheet = workbook.worksheets[0]

# ソースデータに見出し行 (Fruit, Year, Amount) と
# 2020年と2021年にわたる grape、blueberry、kiwi、cherry の 9 データ行を入力
sheet.cells[0, 0].put_value("Fruit")
sheet.cells[0, 1].put_value("Year")
sheet.cells[0, 2].put_value("Amount")

sheet.cells[1, 0].put_value("grape")
sheet.cells[1, 1].put_value(2020)
sheet.cells[1, 2].put_value(50)

sheet.cells[2, 0].put_value("blueberry")
sheet.cells[2, 1].put_value(2020)
sheet.cells[2, 2].put_value(30)

sheet.cells[3, 0].put_value("kiwi")
sheet.cells[3, 1].put_value(2020)
sheet.cells[3, 2].put_value(25)

sheet.cells[4, 0].put_value("cherry")
sheet.cells[4, 1].put_value(2020)
sheet.cells[4, 2].put_value(40)

sheet.cells[5, 0].put_value("grape")
sheet.cells[5, 1].put_value(2021)
sheet.cells[5, 2].put_value(60)

sheet.cells[6, 0].put_value("blueberry")
sheet.cells[6, 1].put_value(2021)
sheet.cells[6, 2].put_value(35)

sheet.cells[7, 0].put_value("kiwi")
sheet.cells[7, 1].put_value(2021)
sheet.cells[7, 2].put_value(28)

sheet.cells[8, 0].put_value("cherry")
sheet.cells[8, 1].put_value(2021)
sheet.cells[8, 2].put_value(45)

sheet.cells[9, 0].put_value("grape")
sheet.cells[9, 1].put_value(2020)
sheet.cells[9, 2].put_value(45)

# 宛先セル E3 に "Pivot1" という名前のピボットテーブルをソース範囲 A1:C10 を使用して追加
pivot_index = sheet.pivot_tables.add("A1:C10", "E3", "Pivot1")
pivot_table = sheet.pivot_tables[pivot_index]

# フィールドを割り当て: Fruit -> Rows、Year -> Columns、Amount -> Data
pivot_table.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, "Amount")

# レガシー XLS プレセット自動フォーマット "Report5" を適用
# 注: このプロパティは .xls 形式で保存する場合にのみ有効です。
# .xlsx/.xlsm/.xlsb として保存する場合、Excel は AutoFormatType を無視し、
# PivotTableStyleType / PivotTableStyleName で指定された形式を使用します。
pivot_table.auto_format_type = ac.PivotTableAutoFormatType.REPORT5

# ワークブックをレガシー .xls 形式で保存
workbook.save("output.xls")
```

## **モダンな名前付きプリセット ピボットテーブル スタイルを適用する**

`PivotTable.pivot_table_style_type` は、`aspose.cells.PivotTableStyleType` 列挙型の値を受け取ります。この列挙型には、ライト テーマの `PIVOT_TABLE_STYLE_LIGHT_1` ～ `PIVOT_TABLE_STYLE_LIGHT_28` と、ダーク テーマの `PIVOT_TABLE_STYLE_DARK_1` ～ `PIVOT_TABLE_STYLE_DARK_28` が含まれます。Excel 2017 で追加されたスタイル (ライトとダーク テーマの第二波) も同じ列挙型からアクセスできます。

これは、モダンなファイル形式に対して推奨される API です。レガシー自動書式とは異なり、ここで選択されたスタイルは Excel によって忠実にレンダリングされ、他の Office ツールとのラウンドトリップでも保持されます。

次の例では、同じ Fruit/Year/Amount データを使用し、同じピボットテーブルを作成して、`PIVOT_TABLE_STYLE_DARK_1` を適用し、ワークブックを `.xlsx` として保存します。

```python
import aspose.cells as ac

# シナリオ 2: PivotTableStyleType を使用してモダンな Excel 2007+ の名前付き定義済みスタイルを適用します。
# 対象ファイル形式: .xlsx。PivotTableStyleType 列挙型は Aspose.Cells 名前空間に存在します
# (Aspose.Cells.Pivot ではありません) — そのため追加の using は必要ありません。
# GitHub リファレンス: https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Examples/CSharp/PivotTables/ApplyStyleToPivotTable2.cs

workbook = ac.Workbook()
worksheet = workbook.worksheets[0]

# ヘッダー行: Fruit / Year / Amount
worksheet.cells["A1"].put_value("Fruit")
worksheet.cells["B1"].put_value("Year")
worksheet.cells["C1"].put_value("Amount")

# Fruit / Year / Amount の 9 データ行
worksheet.cells["A2"].put_value("Grape")
worksheet.cells["B2"].put_value(2020)
worksheet.cells["C2"].put_value(100)

worksheet.cells["A3"].put_value("Blueberry")
worksheet.cells["B3"].put_value(2020)
worksheet.cells["C3"].put_value(150)

worksheet.cells["A4"].put_value("Kiwi")
worksheet.cells["B4"].put_value(2020)
worksheet.cells["C4"].put_value(200)

worksheet.cells["A5"].put_value("Cherry")
worksheet.cells["B5"].put_value(2020)
worksheet.cells["C5"].put_value(180)

worksheet.cells["A6"].put_value("Grape")
worksheet.cells["B6"].put_value(2021)
worksheet.cells["C6"].put_value(120)

worksheet.cells["A7"].put_value("Blueberry")
worksheet.cells["B7"].put_value(2021)
worksheet.cells["C7"].put_value(170)

worksheet.cells["A8"].put_value("Kiwi")
worksheet.cells["B8"].put_value(2021)
worksheet.cells["C8"].put_value(210)

worksheet.cells["A9"].put_value("Cherry")
worksheet.cells["B9"].put_value(2021)
worksheet.cells["C9"].put_value(190)

worksheet.cells["A10"].put_value("Grape")
worksheet.cells["B10"].put_value(2021)
worksheet.cells["C10"].put_value(130)

# E3 に "Pivot1" という名前で、A1:C10 をソースとするピボットテーブルを追加します
pivot_index = worksheet.pivot_tables.add("A1:C10", "E3", "Pivot1")
pivot_table = worksheet.pivot_tables[pivot_index]

# ピボットフィールドを割り当てます: Fruit → 行エリア、Year → 列エリア、Amount → データエリア
pivot_table.add_field_to_area(ac.PivotFieldType.Row, "Fruit")
pivot_table.add_field_to_area(ac.PivotFieldType.Column, "Year")
pivot_table.add_field_to_area(ac.PivotFieldType.Data, "Amount")

# モダンな Excel 2007+ の名前付き定義済みピボットスタイルを適用します。
# PivotTableStyleType は .xlsx / .xlsm / .xlsb ファイル用の正しい API です。AutoFormatType は
# これらの形式では Excel に無視されます。PivotTableStyleDark1 はダークテーマファミリー
# (PivotTableStyleDark1..PivotTableStyleDark28) に属し、同じ列挙型には新しい Excel 2017 の
# ライト/ダークテーマ (PivotTableStyleLight1..Light28 / Dark1..Dark28) も公開されています。
pivot_table.pivot_table_style_type = ac.PivotTableStyleType.PivotTableStyleDark1

# モダンな .xlsx として保存します — これは PivotTableStyleType が意味を持つ形式です。
workbook.save("output.xlsx")
```

## **カスタム ピボットテーブル スタイルを定義して適用する**

組み込みプリセットは変更できません。色、罫線、フォントをオーバーライドする必要がある場合は、必ずカスタム ピボット スタイルを定義する必要があります。ワークフローは 3 つの手順で構成されます。

1. `workbook.worksheets.table_styles.add_pivot_table_style(name)` 経由で、ワークブックの `table_styles` コレクションにカスタム スタイルを追加します。新しく作成されたスタイルのインデックスが返されます。
2. `table_style.table_style_elements.add(TableStyleElementType)` 経由で要素 (`WHOLE_TABLE` や `GRAND_TOTAL_ROW` など) を追加し、`table_style_element.set_element_style(Style)` 経由で各要素に `Style` を割り当てることで、スタイルを設定します。
3. `PivotTable.pivot_table_style_name` をスタイルの名前に設定することで、カスタム スタイルをピボットに適用します。ここでは `pivot_table_style_type` を使用しないでください。このプロパティは組み込みプリセットを選択するためです。

{{% alert color="primary" %}}

`pivot_table_style_name` と `pivot_table_style_type` は互いに交換できません。組み込みプリセットには `pivot_table_style_type` を、`add_pivot_table_style` で定義したカスタム スタイルには `pivot_table_style_name` を使用してください。両方を設定しても問題ありませんが、想定されるソースに対応する側のみがレンダリングされます。

{{% /alert %}}

利用可能な `TableStyleElementType` 値には、`WHOLE_TABLE`、`FIRST_ROW`、`LAST_ROW`、`FIRST_COLUMN`、`LAST_COLUMN`、`GRAND_TOTAL_ROW`、`GRAND_TOTAL_COLUMN`、`PAGE_FIELD_LABELS`、`PAGE_FIELD_VALUES` が含まれます。

次の例では、`WHOLE_TABLE` に細い黒の罫線、`GRAND_TOTAL_ROW` に太字の赤いフォントを持つカスタム ピボット スタイルを定義し、`pivot_table_style_name` 経由で適用して `.xlsx` として保存します。

```python
import aspose.cells as ac
import System.Drawing

workbook = ac.Workbook()
worksheet = workbook.worksheets[0]

# ソースデータを設定：ヘッダー行 + 9データ行 (A1:C10)
worksheet.cells["A1"].put_value("Fruit")
worksheet.cells["B1"].put_value("Year")
worksheet.cells["C1"].put_value("Amount")

worksheet.cells["A2"].put_value("Grape")
worksheet.cells["B2"].put_value(2020)
worksheet.cells["C2"].put_value(100)

worksheet.cells["A3"].put_value("Blueberry")
worksheet.cells["B3"].put_value(2020)
worksheet.cells["C3"].put_value(200)

worksheet.cells["A4"].put_value("Kiwi")
worksheet.cells["B4"].put_value(2020)
worksheet.cells["C4"].put_value(300)

worksheet.cells["A5"].put_value("Cherry")
worksheet.cells["B5"].put_value(2020)
worksheet.cells["C5"].put_value(400)

worksheet.cells["A6"].put_value("Grape")
worksheet.cells["B6"].put_value(2021)
worksheet.cells["C6"].put_value(500)

worksheet.cells["A7"].put_value("Blueberry")
worksheet.cells["B7"].put_value(2021)
worksheet.cells["C7"].put_value(600)

worksheet.cells["A8"].put_value("Kiwi")
worksheet.cells["B8"].put_value(2021)
worksheet.cells["C8"].put_value(700)

worksheet.cells["A9"].put_value("Cherry")
worksheet.cells["B9"].put_value(2021)
worksheet.cells["C9"].put_value(800)

worksheet.cells["A10"].put_value("Grape")
worksheet.cells["B10"].put_value(2021)
worksheet.cells["C10"].put_value(900)

# A1:C10をソースとし、E3に配置される「Pivot1」という名前のピボットテーブルを追加
pivot_index = worksheet.pivot_tables.add("A1:C10", "E3", "Pivot1")
pivot_table = worksheet.pivot_tables[pivot_index]

pivot_table.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(ac.PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, "Amount")

# ステップ1：新しいカスタムピボットテーブルスタイルを登録し、そのインデックスを取得
style_index = workbook.worksheets.table_styles.add_pivot_table_style("CustomPivotStyle")
table_style = workbook.worksheets.table_styles[style_index]

# ステップ2：WholeTable要素を追加し、4辺すべてに細い黒色の境界線を適用
whole_table_element_index = table_style.table_style_elements.add(ac.TableStyleElementType.WHOLE_TABLE)
whole_table_element = table_style.table_style_elements[whole_table_element_index]
whole_table_style = workbook.create_style()
whole_table_style.borders[ac.BorderType.TOP_BORDER].line_style = ac.CellBorderType.THIN
whole_table_style.borders[ac.BorderType.TOP_BORDER].color = System.Drawing.Color.Black
whole_table_style.borders[ac.BorderType.BOTTOM_BORDER].line_style = ac.CellBorderType.THIN
whole_table_style.borders[ac.BorderType.BOTTOM_BORDER].color = System.Drawing.Color.Black
whole_table_style.borders[ac.BorderType.LEFT_BORDER].line_style = ac.CellBorderType.THIN
whole_table_style.borders[ac.BorderType.LEFT_BORDER].color = System.Drawing.Color.Black
whole_table_style.borders[ac.BorderType.RIGHT_BORDER].line_style = ac.CellBorderType.THIN
whole_table_style.borders[ac.BorderType.RIGHT_BORDER].color = System.Drawing.Color.Black
whole_table_element.set_element_style(whole_table_style)

# ステップ3：GrandTotalRow要素を追加し、太字の赤色フォントを適用
grand_total_element_index = table_style.table_style_elements.add(ac.TableStyleElementType.GRAND_TOTAL_ROW)
grand_total_element = table_style.table_style_elements[grand_total_element_index]
grand_total_style = workbook.create_style()
grand_total_style.font.is_bold = True
grand_total_style.font.color = System.Drawing.Color.Red
grand_total_element.set_element_style(grand_total_style)

# ステップ4：名前でカスタムスタイルを適用（PivotTableStyleTypeではなく、ビルトインプリセット用です）
pivot_table.pivot_table_style_name = "CustomPivotStyle"

workbook.save("output.xlsx")
```

## **FormatAll を使用してすべてのピボット セルに 1 つのスタイルを適用する**

`PivotTable.format_all(Style)` は、データ領域、行ヘッダーと列ヘッダー、合計を含む、ピボットテーブルのすべてのセルに単一の `Style` オブジェクトを適用するショートカットです。`pivot_table_style_type` または `pivot_table_style_name` 経由で以前に設定された内容はすべて上書きされます。

{{% alert color="primary" %}}

`format_all` は `pivot_table_style_type` と `pivot_table_style_name` の両方を上書きします。テーマに関係なく、ピボット全体で均一な外観が必要な場合にのみ使用してください。

{{% /alert %}}

次の例では、黄色の単色塗りつぶし、太字のダークブルー フォント、およびすべての辺に細い黒の罫線を持つ `Style` を作成し、`format_all` で適用して、`.xlsx` として保存します。

```python
from System.Drawing import Color
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType
from aspose.cells import BackgroundType, CellBorderType, BorderType

# シナリオ 4: FormatAll API を使用してすべてのピボットテーブルセルに単一のスタイルを適用
# 使用中の API: PivotTable.FormatAll(Style)
# 出力形式: .xlsx
# GitHub リファレンス: Aspose.Cells-for-.NET リポジトリのピボットテーブルスタイル例を参照

workbook = ac.Workbook()
worksheet = workbook.worksheets[0]

# ソースデータを入力: ヘッダー行 (1 行目) + データ 9 行 (2 ～ 10 行目)
worksheet.cells["A1"].put_value("Fruit")
worksheet.cells["B1"].put_value("Year")
worksheet.cells["C1"].put_value("Amount")

worksheet.cells["A2"].put_value("Grape")
worksheet.cells["B2"].put_value(2020)
worksheet.cells["C2"].put_value(5000)

worksheet.cells["A3"].put_value("Blueberry")
worksheet.cells["B3"].put_value(2020)
worksheet.cells["C3"].put_value(3000)

worksheet.cells["A4"].put_value("Kiwi")
worksheet.cells["B4"].put_value(2020)
worksheet.cells["C4"].put_value(4000)

worksheet.cells["A5"].put_value("Cherry")
worksheet.cells["B5"].put_value(2020)
worksheet.cells["C5"].put_value(2000)

worksheet.cells["A6"].put_value("Grape")
worksheet.cells["B6"].put_value(2021)
worksheet.cells["C6"].put_value(6000)

worksheet.cells["A7"].put_value("Blueberry")
worksheet.cells["B7"].put_value(2021)
worksheet.cells["C7"].put_value(3500)

worksheet.cells["A8"].put_value("Kiwi")
worksheet.cells["B8"].put_value(2021)
worksheet.cells["C8"].put_value(4500)

worksheet.cells["A9"].put_value("Cherry")
worksheet.cells["B9"].put_value(2021)
worksheet.cells["C9"].put_value(2500)

worksheet.cells["A10"].put_value("Grape")
worksheet.cells["B10"].put_value(2021)
worksheet.cells["C10"].put_value(5500)

# ピボットテーブルを追加: ソース範囲 A1:C10、配置先セル E3、名前 "Pivot1"
pivot_index = worksheet.pivot_tables.add("A1:C10", "E3", "Pivot1")
pivot_table = worksheet.pivot_tables[pivot_index]

# ピボットフィールドを割り当て: Fruit → 行エリア、Year → 列エリア、Amount → データエリア
pivot_table.add_field_to_area(PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")

# ピボットテーブルのすべてのセルに強制適用する Style を作成
style = workbook.create_style()
style.foreground_color = Color.Yellow
style.pattern = BackgroundType.SOLID
style.font.is_bold = True
style.font.color = Color.DarkBlue
style.borders[BorderType.TOP_BORDER].line_style = CellBorderType.THIN
style.borders[BorderType.TOP_BORDER].color = Color.Black
style.borders[BorderType.BOTTOM_BORDER].line_style = CellBorderType.THIN
style.borders[BorderType.BOTTOM_BORDER].color = Color.Black
style.borders[BorderType.LEFT_BORDER].line_style = CellBorderType.THIN
style.borders[BorderType.LEFT_BORDER].color = Color.Black
style.borders[BorderType.RIGHT_BORDER].line_style = CellBorderType.THIN
style.borders[BorderType.RIGHT_BORDER].color = Color.Black

# FormatAll を適用: この単一のスタイルをピボットテーブルのすべてのセルに強制適用し、
# 以前に設定された PivotTableStyleType / PivotTableStyleName を上書きします
pivot_table.format_all(style)

# ワークブックを最新の .xlsx 形式で保存
workbook.save("output.xlsx")
```

## **どのスタイル API を使用すべきですか?**

スタイル API の選択は、保存先のファイル形式によって異なります。次の表をクイック リファレンスとして使用してください。

| 対象ファイル形式 | 使用する API | メモ |
|---|---|---|
| `.xls` (レガシー) | `PivotTable.auto_format_type` | `aspose.cells.pivot.PivotTableAutoFormatType` の値 (例: `REPORT_1`～`REPORT_10`、`CLASSIC`、`TABLE_1`～`TABLE_10`)。モダン形式で保存する場合は無視されます。 |
| `.xlsx` / `.xlsm` / `.xlsb` (モダン、組み込みスタイル) | `PivotTable.pivot_table_style_type` | `aspose.cells.PivotTableStyleType` の値 (Excel 2017 の追加を含むライト/ダーク テーマ)。 |
| `.xlsx` / `.xlsm` / `.xlsb` (モダン、カスタム スタイル) | `PivotTable.pivot_table_style_name` + `worksheets.table_styles.add_pivot_table_style(...)` | 組み込みプリセットでは不十分な場合に使用します。`table_style_element.set_element_style(...)` 経由で設定します。 |
| 任意の形式 (均一な上書き) | `PivotTable.format_all(Style)` | ピボット全体で他のすべてのスタイル設定を上書きするショートカット。 |

迷う場合は、`.xlsx` として保存し、組み込みテーマには `pivot_table_style_type` を、カスタム テーマには `pivot_table_style_name` を使用してください。

## **関連記事**

- [Aspose.Cells for Python via .NET でピボットテーブルを更新する](/cells/ja/python-net/refresh-pivot-table/)

{{< app/cells/assistant language="python" >}}
