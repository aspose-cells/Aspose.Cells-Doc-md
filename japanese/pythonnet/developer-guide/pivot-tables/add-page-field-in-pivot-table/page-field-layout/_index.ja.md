---
title: ピボットテーブルでページフィールドのレイアウトを変更する
linktitle: ピボットテーブルでページフィールドのレイアウトを変更する
description: Aspose.Cells for Python via .NET を使用してピボットテーブルのページフィールド領域のレイアウトを制御する方法を説明します。ピボットテーブル上部にあるページフィールドの表示順序、折り返し数、フィールド順序の設定を含みます。
keywords: Aspose.Cells, Python via .NET ライブラリ, スプレッドシート, ピボットテーブル, ページフィールド, ページフィールドの順序, ページフィールドの折り返し数, ページフィールドの移動
type: docs
weight: 191
url: /ja/python-net/change-page-field-layout/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
この記事は **Add Page Field in Pivot Table** の続きの記事です。ピボットテーブル上部にあるフィルターコントロールの帯であるページフィールド領域のレイアウトを、表示順序、折り返し数、フィールドの並び替えを含めて制御する方法を説明します。
{{% /alert %}}

## **Introduction**
Microsoft Excel のピボットテーブルには、テーブルの行/列/データ本体の上に位置する専用の **ページフィールド領域** があります。この領域はドロップダウンフィルターコントロールの帯としてレンダリングされ(ページフィールドごとに1つ)、エンドユーザーが年や地域などの条件でピボットをスライスするためにクリックする部分です。Aspose.Cells for Python via .NET は、この領域を `pivot_table.page_fields` コレクションでモデル化し、帯の視覚的なレイアウトを制御する3つのプロパティを公開しています。
- `pivot_table.page_field_order`(`PrintOrderType` 値)は、追加のページフィールドを既存のフィールドの *隣* に配置するか、 *下* に配置するかを決定します。
- `pivot_table.page_field_wrap_count` は、折り返す前に行または列ごとに配置されるページフィールドの数を設定します。
- `pivot_table.page_fields.move(curr_index, dest_index)` は、順序モードを変更せずにページフィールドを並び替えます。
この記事では、共有データセットに対してこれらの各操作を示す3つのコード例を紹介し、結果として得られるレイアウトを並べて比較できるようにします。

## **Source Data**
| Fruit  | Year | Region | Amount |
|--------|------|--------|--------|
| Apple  | 2022 | North  | 150    |
| Apple  | 2023 | North  | 180    |
| Banana | 2022 | South  | 120    |
| Banana | 2023 | South  | 140    |
| Cherry | 2022 | East   | 200    |
| Cherry | 2023 | East   | 220    |
| Grape  | 2022 | West   | 90     |
| Grape  | 2023 | West   | 110    |
8行すべてがすべてのコード例で同じ順序で入力されているため、シナリオ間でソースデータが変更されることはありません。ページフィールドのレイアウトプロパティのみが異なります。

## **Example 1: Over Then Down**
最初のシナリオでは、2つのページフィールド(`Year`、`Region`)をピボットテーブル上部の1行に横並びに表示するように設定します。`Fruit` を行軸に割り当て、`Year` を最初に、`Region` を2番目にページ軸に配置し(`add_field_to_area` 呼び出しの順序が開始インデックスを決定します)、データフィールドとして `Amount`(Sum)を追加してから、`page_field_order` を `PrintOrderType.OverThenDown` に設定し、`page_field_wrap_count = 2` に設定します。`OverThenDown` と折り返し数 2 を使用すると、2つのページフィールドはピボットテーブル上部の1行に横並びにレイアウトされるため、帯は幅2の1行を占めます。

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
# Headers (row 0)
pivot_data_cells[0, 0].put_value("Fruit")
pivot_data_cells[0, 1].put_value("Year")
pivot_data_cells[0, 2].put_value("Region")
pivot_data_cells[0, 3].put_value("Amount")
# Row 1: Apple, 2022, North, 150
pivot_data_cells[1, 0].put_value("Apple")
pivot_data_cells[1, 1].put_value(2022)
pivot_data_cells[1, 2].put_value("North")
pivot_data_cells[1, 3].put_value(150)
# Row 2: Apple, 2023, North, 180
pivot_data_cells[2, 0].put_value("Apple")
pivot_data_cells[2, 1].put_value(2023)
pivot_data_cells[2, 2].put_value("North")
pivot_data_cells[2, 3].put_value(180)
# Row 3: Banana, 2022, South, 120
pivot_data_cells[3, 0].put_value("Banana")
pivot_data_cells[3, 1].put_value(2022)
pivot_data_cells[3, 2].put_value("South")
pivot_data_cells[3, 3].put_value(120)
# Row 4: Banana, 2023, South, 140
pivot_data_cells[4, 0].put_value("Banana")
pivot_data_cells[4, 1].put_value(2023)
pivot_data_cells[4, 2].put_value("South")
pivot_data_cells[4, 3].put_value(140)
# Row 5: Cherry, 2022, East, 200
pivot_data_cells[5, 0].put_value("Cherry")
pivot_data_cells[5, 1].put_value(2022)
pivot_data_cells[5, 2].put_value("East")
pivot_data_cells[5, 3].put_value(200)
# Row 6: Cherry, 2023, East, 220
pivot_data_cells[6, 0].put_value("Cherry")
pivot_data_cells[6, 1].put_value(2023)
pivot_data_cells[6, 2].put_value("East")
pivot_data_cells[6, 3].put_value(220)
# Row 7: Grape, 2022, West, 90
pivot_data_cells[7, 0].put_value("Grape")
pivot_data_cells[7, 1].put_value(2022)
pivot_data_cells[7, 2].put_value("West")
pivot_data_cells[7, 3].put_value(90)
# Row 8: Grape, 2023, West, 110
pivot_data_cells[8, 0].put_value("Grape")
pivot_data_cells[8, 1].put_value(2023)
pivot_data_cells[8, 2].put_value("West")
pivot_data_cells[8, 3].put_value(110)
# Add PivotTableReport sheet
pivot_table_sheet_idx = worksheets.add("PivotTableReport")
pivot_table_sheet = worksheets[pivot_table_sheet_idx]
pivot_tables = pivot_table_sheet.pivot_tables
# Create pivot table sourced from PivotData!A1:D9 placed at A1 on PivotTableReport
pivot_index = pivot_tables.add("PivotData!A1:D9", "A1", "PivotTable1")
pivot_table = pivot_tables[pivot_index]
# Add fields
pivot_table.add_field_to_area(ac.PivotFieldType.ROW, 0)   # Fruit
pivot_table.add_field_to_area(ac.PivotFieldType.PAGE, 1)  # Year
pivot_table.add_field_to_area(ac.PivotFieldType.PAGE, 2)  # Region
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, 3)  # Amount
pivot_table.data_fields[0].function = ac.ConsolidationFunction.SUM
# Configure page field area layout: place page fields across first, wrap after every 2
pivot_table.page_field_order = ac.PrintOrderType.OVER_THEN_DOWN
pivot_table.page_field_wrap_count = 2
# Refresh and calculate
pivot_table.calculate_data()
# Save
workbook.save(os.path.join(data_dir, "pageFieldLayout_overThenDown.xlsx"))
```

## **Example 2: Down Then Over**
この例では、Example 1 とまったく同様に、`Fruit` を行軸に、`Year` と `Region` をページ軸に(`Year` を最初に)、`Amount`(Sum) をデータフィールドとして配置します。次に `page_field_order` を `PrintOrderType.DownThenOver` に設定し、`page_field_wrap_count` を `2` に設定します。`DownThenOver` と折り返し数 2 を使用すると、2つのページフィールドは垂直に積み重ねられ、`Year` が上、`Region` がすぐ下になり、ピボットテーブル上部に1列を形成します。したがって、帯は Example 1 とは対照的に、幅1の2行を占めます。

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

## **Example 3: Move a Page Field**
3番目のシナリオでは、このデータセットとフィールド割り当てをそのままにし、中立的なレイアウト(折り返し数 `2` の `OverThenDown`)を設定してから、`page_fields.move` 操作を示します。`move(0, 1)` 呼び出しは、インデックス 0(`Year`)のページフィールドを位置1に移動し、位置1にあったページフィールド(`Region`)を位置0にシフトします。この呼び出しの後、`Region` が最初のページフィールドになり、`Year` が2番目になります。折り返しと順序モードは変更されないため、帯は引き続き横並びにレンダリングされます。2つのドロップダウンの順序のみが入れ替わります。

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

## **Related Articles**
- [Add Page Field in Pivot Table](/cells/ja/python-net/add-page-field-in-pivot-table/) — ページフィールドをピボットテーブルに追加する方法を紹介する親ページです。
- [Row and Column Fields in Pivot Table](/cells/ja/python-net/row-and-column-fields/) — ここで示したページ軸の作業を補完する、行軸および列軸へのフィールドの割り当てについて説明しています。
- [Manage Value Fields in Pivot Table](/cells/ja/python-net/manage-value-fields/) — この記事で使用されている `Sum` 集計を含む、データ(値)領域の設定方法について説明しています。
- [Refresh Pivot Table](/cells/ja/python-net/refresh-pivot-table/) — ページフィールドの並び替え後に必要な `refresh_data` および `calculate_data` について説明しています。
- [Apply Style to Pivot Table](/cells/ja/python-net/apply-style-to-pivot-table/) — ページフィールドの帯をレイアウトした後に、レンダリングされたピボットテーブルを書式設定する方法を示します。

{{< app/cells/assistant language="python-net" >}}