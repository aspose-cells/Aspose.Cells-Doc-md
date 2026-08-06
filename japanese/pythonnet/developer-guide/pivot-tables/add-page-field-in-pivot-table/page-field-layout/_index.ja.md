---
title: ピボットテーブルでページフィールドのレイアウトを変更する
linktitle: ピボットテーブルでページフィールドのレイアウトを変更する
description: Aspose.Cells for Python via .NET を使用して、ピボットテーブルのページフィールド領域のレイアウト（表示順、折り返し数、ページフィールドの並び順）を制御する方法を学習します。
keywords: Aspose.Cells, Python via .NET ライブラリ, スプレッドシート, ピボットテーブル, ページフィールド, ページフィールドの順序, ページフィールドの折り返し数, ページフィールドの移動
type: docs
weight: 191
url: /ja/python-net/change-page-field-layout/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---
{{% alert color="primary" %}}
この記事は **Add Page Field in Pivot Table** トピックの内容を引き継ぐものです。ページフィールド領域（ピボットテーブル上部に表示されるフィルターコントロールの帯）のレイアウトを、表示順、折り返し数、フィールドの並び替えを含めて制御する方法を説明します。
{{% /alert %}}
## **概要**
Microsoft Excel のピボットテーブルには、行/列/データ本体の上部に位置する専用の **ページフィールド領域** が存在します。この領域はページフィールドごとに 1 つのドロップダウンフィルターコントロールとして表示され、エンドユーザーが年や地域などの条件でピボットを絞り込む際にクリックする部分です。Aspose.Cells for Python via .NET では、この領域を `pivot_table.page_fields` コレクションとしてモデル化し、帯の視覚的なレイアウトを制御する 3 つのプロパティを公開しています。
- `pivot_table.page_field_order`（`PrintOrderType` 値）は、追加のページフィールドを既存のフィールドの **横** に配置するか **下** に配置するかを決定します。
- `pivot_table.page_field_wrap_count` は、折り返しまでに 1 行または 1 列に配置するページフィールドの数を設定します。
- `pivot_table.page_fields.move(curr_index, dest_index)` は、並び順モードを変更せずにページフィールドの順序を変更します。
この記事を通じて、共有データセットに対してこれらの操作をそれぞれ示す 3 つのコード例を確認し、結果を並べて比較できるようにします。
## **ソースデータ**
以下の 3 つの例では、次の 8 行の売上データを `PivotData` という名前のワークシートに読み込みます。データには、ページフィールドの候補（`Year`、`Region`）が 2 つ、行フィールドの候補（`Fruit`）が 1 つ、メジャー（`Amount`）が 1 つ含まれており、ページフィールドの帯を検証するうえで意味のある構成になっています。
8 行すべてのデータは、すべてのコード例で同じ順序で入力されています。ソースデータはシナリオ間で変わらず、変更されるのはページフィールドのレイアウトプロパティだけです。
## **例 1: Over Then Down**
最初のシナリオでは、2 つのページフィールド（`Year`、`Region`）をピボットテーブル上部の **1 行に横並びで** 表示するよう設定します。`Fruit` を行軸に割り当て、ページ軸には `Year` を先頭、`Region` を 2 番目に配置し（`add_field_to_area` を呼び出す順序が開始インデックスを決定します）、`Amount`（Sum）をデータフィールドとして追加します。続いて、`page_field_order` を `PrintOrderType.OverThenDown` に、`page_field_wrap_count` を `2` に設定します。`OverThenDown` と折り返し数 2 の組み合わせにより、2 つのページフィールドはピボットテーブル上部の 1 行に横並びで配置され、帯は幅 2 の 1 行を占めます。
```python
import os
import aspose.cells as ac

data_dir = "output"
if not os.path.exists(data_dir):
    os.makedirs(data_dir, exist_ok=True)

workbook = ac.Workbook()
worksheets = workbook.worksheets

pivot_data_idx = worksheets.add("PivotData")
pivot_data_sheet = worksheets[pivot_data_idx]
pivot_data_cells = pivot_data_sheet.cells

# ヘッダー (0行目)
pivot_data_cells[0, 0].put_value("Fruit")
pivot_data_cells[0, 1].put_value("Year")
pivot_data_cells[0, 2].put_value("Region")
pivot_data_cells[0, 3].put_value("Amount")

# 1行目: Apple, 2022, North, 150
pivot_data_cells[1, 0].put_value("Apple")
pivot_data_cells[1, 1].put_value(2022)
pivot_data_cells[1, 2].put_value("North")
pivot_data_cells[1, 3].put_value(150)

# 2行目: Apple, 2023, North, 180
pivot_data_cells[2, 0].put_value("Apple")
pivot_data_cells[2, 1].put_value(2023)
pivot_data_cells[2, 2].put_value("North")
pivot_data_cells[2, 3].put_value(180)

# 3行目: Banana, 2022, South, 120
pivot_data_cells[3, 0].put_value("Banana")
pivot_data_cells[3, 1].put_value(2022)
pivot_data_cells[3, 2].put_value("South")
pivot_data_cells[3, 3].put_value(120)

# 4行目: Banana, 2023, South, 140
pivot_data_cells[4, 0].put_value("Banana")
pivot_data_cells[4, 1].put_value(2023)
pivot_data_cells[4, 2].put_value("South")
pivot_data_cells[4, 3].put_value(140)

# 5行目: Cherry, 2022, East, 200
pivot_data_cells[5, 0].put_value("Cherry")
pivot_data_cells[5, 1].put_value(2022)
pivot_data_cells[5, 2].put_value("East")
pivot_data_cells[5, 3].put_value(200)

# 6行目: Cherry, 2023, East, 220
pivot_data_cells[6, 0].put_value("Cherry")
pivot_data_cells[6, 1].put_value(2023)
pivot_data_cells[6, 2].put_value("East")
pivot_data_cells[6, 3].put_value(220)

# 7行目: Grape, 2022, West, 90
pivot_data_cells[7, 0].put_value("Grape")
pivot_data_cells[7, 1].put_value(2022)
pivot_data_cells[7, 2].put_value("West")
pivot_data_cells[7, 3].put_value(90)

# 8行目: Grape, 2023, West, 110
pivot_data_cells[8, 0].put_value("Grape")
pivot_data_cells[8, 1].put_value(2023)
pivot_data_cells[8, 2].put_value("West")
pivot_data_cells[8, 3].put_value(110)

# PivotTableReportシートを追加
pivot_table_sheet_idx = worksheets.add("PivotTableReport")
pivot_table_sheet = worksheets[pivot_table_sheet_idx]
pivot_tables = pivot_table_sheet.pivot_tables

# PivotData!A1:D9 をデータソースとし、PivotTableReport の A1 に配置するピボットテーブルを作成
pivot_index = pivot_tables.add("PivotData!A1:D9", "A1", "PivotTable1")
pivot_table = pivot_tables[pivot_index]

# フィールドを追加
pivot_table.add_field_to_area(ac.PivotFieldType.ROW, 0)   # Fruit
pivot_table.add_field_to_area(ac.PivotFieldType.PAGE, 1)  # Year
pivot_table.add_field_to_area(ac.PivotFieldType.PAGE, 2)  # Region
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, 3)  # Amount
pivot_table.data_fields[0].function = ac.ConsolidationFunction.SUM

# ページフィールドエリアのレイアウトを設定: ページフィールドを横方向に先に配置し、2つごとに改行する
pivot_table.page_field_order = ac.PrintOrderType.OVER_THEN_DOWN
pivot_table.page_field_wrap_count = 2

# 更新して計算する
pivot_table.calculate_data()

# 保存
workbook.save(os.path.join(data_dir, "pageFieldLayout_overThenDown.xlsx"))
```
## **例 2: Down Then Over**
この例では、`Fruit` を行軸に、`Year` と `Region` をページ軸に（`Year` を先に）配置し、`Amount`（Sum）をデータフィールドとして設定します。これは例 1 とまったく同じ構成です。続いて、`page_field_order` を `PrintOrderType.DownThenOver` に、`page_field_wrap_count` を `2` に設定します。`DownThenOver` と折り返し数 2 の組み合わせにより、2 つのページフィールドは縦に積み上げられ、`Year` が上、`Region` がその直下に配置され、ピボットテーブル上部の 1 列を構成します。したがって、帯は例 1 とは対照的に、幅 1 で 2 行を占めます。
```python
import aspose.cells as ac

workbook = ac.Workbook()
pivot_data = workbook.worksheets[0]
pivot_data.name = "PivotData"
pivot_report_idx = workbook.worksheets.add("PivotTableReport")
pivot_report = workbook.worksheets[pivot_report_idx]

headers = ["Fruit", "Year", "Region", "Amount"]
for c in range(len(headers)):
    pivot_data.cells[0, c].put_value(headers[c])

data = [
    ["Apple", 2022, "North", 150],
    ["Apple", 2023, "North", 180],
    ["Banana", 2022, "South", 120],
    ["Banana", 2023, "South", 140],
    ["Cherry", 2022, "East", 200],
    ["Cherry", 2023, "East", 220],
    ["Grape", 2022, "West", 90],
    ["Grape", 2023, "West", 110]
]

for r in range(len(data)):
    for c in range(len(data[r])):
        pivot_data.cells[r + 1, c].put_value(data[r][c])

idx = pivot_report.pivot_tables.add("PivotData!A1:D9", "A1", "PivotTable")
pivot_table = pivot_report.pivot_tables[idx]

pivot_table.add_field_to_area(ac.PivotFieldType.ROW, 0)
pivot_table.add_field_to_area(ac.PivotFieldType.PAGE, 1)
pivot_table.add_field_to_area(ac.PivotFieldType.PAGE, 2)
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, 3)

pivot_table.page_field_order = ac.PrintOrderType.DOWN_THEN_OVER
pivot_table.page_field_wrap_count = 2

pivot_table.calculate_data()

workbook.save("pageFieldLayout_downThenOver.xlsx")
```
## **例 3: ページフィールドの移動**
3 つ目のシナリオでは、このデータセットとフィールドの割り当てを維持し、中立的なレイアウト（折り返し数 `2` の `OverThenDown`）を設定した上で、`page_fields.move` 操作を実演します。`move(0, 1)` の呼び出しにより、インデックス 0 のページフィールド（`Year`）が位置 1 に移動し、元々位置 1 にあったページフィールド（`Region`）が位置 0 にシフトします。この呼び出しの後、`Region` が 1 番目のページフィールドになり、`Year` が 2 番目になります。折り返しと順序のモードは変更されていないため、帯は引き続き横並びでレンダリングされますが、2 つのドロップダウンの順序のみが入れ替わります。
```python
import aspose.cells as ac

workbook = ac.Workbook()

data_sheet = workbook.worksheets[0]
data_sheet.name = "PivotData"

data_sheet.cells["A1"].put_value("Fruit")
data_sheet.cells["B1"].put_value("Year")
data_sheet.cells["C1"].put_value("Region")
data_sheet.cells["D1"].put_value("Amount")

data_sheet.cells["A2"].put_value("Apple")
data_sheet.cells["B2"].put_value(2022)
data_sheet.cells["C2"].put_value("North")
data_sheet.cells["D2"].put_value(150)

data_sheet.cells["A3"].put_value("Apple")
data_sheet.cells["B3"].put_value(2023)
data_sheet.cells["C3"].put_value("North")
data_sheet.cells["D3"].put_value(180)

data_sheet.cells["A4"].put_value("Banana")
data_sheet.cells["B4"].put_value(2022)
data_sheet.cells["C4"].put_value("South")
data_sheet.cells["D4"].put_value(120)

data_sheet.cells["A5"].put_value("Banana")
data_sheet.cells["B5"].put_value(2023)
data_sheet.cells["C5"].put_value("South")
data_sheet.cells["D5"].put_value(140)

data_sheet.cells["A6"].put_value("Cherry")
data_sheet.cells["B6"].put_value(2022)
data_sheet.cells["C6"].put_value("East")
data_sheet.cells["D6"].put_value(200)

data_sheet.cells["A7"].put_value("Cherry")
data_sheet.cells["B7"].put_value(2023)
data_sheet.cells["C7"].put_value("East")
data_sheet.cells["D7"].put_value(220)

data_sheet.cells["A8"].put_value("Grape")
data_sheet.cells["B8"].put_value(2022)
data_sheet.cells["C8"].put_value("West")
data_sheet.cells["D8"].put_value(90)

data_sheet.cells["A9"].put_value("Grape")
data_sheet.cells["B9"].put_value(2023)
data_sheet.cells["C9"].put_value("West")
data_sheet.cells["D9"].put_value(110)

pivot_sheet_idx = workbook.worksheets.add("PivotTableReport")
pivot_sheet = workbook.worksheets[pivot_sheet_idx]

pivot_idx = pivot_sheet.pivot_tables.add("PivotData!A1:D9", "A3", "PivotTable")
pivot_table = pivot_sheet.pivot_tables[pivot_idx]

pivot_table.add_field_to_area(ac.PivotFieldType.ROW, 0)
pivot_table.add_field_to_area(ac.PivotFieldType.PAGE, 1)
pivot_table.add_field_to_area(ac.PivotFieldType.PAGE, 2)
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, 3)

pivot_table.page_field_order = ac.PrintOrderType.OVER_THEN_DOWN
pivot_table.page_field_wrap_count = 2

pivot_table.page_fields.move(0, 1)

pivot_table.calculate_data()

workbook.save("pageFieldLayout_move.xlsx")
```
## **関連記事**
- [ピボットテーブルにページフィールドを追加する](/cells/ja/python-net/add-page-field-in-pivot-table/) — ページフィールドをピボットテーブルに追加する方法を説明した親ページです。
- [ピボットテーブルの行フィールドと列フィールド](/cells/ja/python-net/row-and-column-fields/) — 行軸と列軸へのフィールドの割り当てについて説明しており、ここで扱うページ軸の作業を補完します。
- [ピボットテーブルの値フィールドを管理する](/cells/ja/python-net/manage-value-fields/) — データ（値）領域の設定方法を説明します。本記事で使用した `Sum` 集計も含みます。
- [ピボットテーブルを更新する](/cells/ja/python-net/refresh-pivot-table/) — ページフィールドの並び替え後に必要な `refresh_data` と `calculate_data` について説明します。
- [ピボットテーブルにスタイルを適用する](/cells/ja/python-net/apply-style-to-pivot-table/) — ページフィールドの帯をレイアウトした後、ピボットテーブルに書式を適用する方法を紹介します。
{{< app/cells/assistant language="python-net" >}}