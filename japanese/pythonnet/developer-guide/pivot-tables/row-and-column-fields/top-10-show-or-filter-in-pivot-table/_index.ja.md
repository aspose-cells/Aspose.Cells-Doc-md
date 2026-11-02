---
title: ピボットテーブルで上位 10 件を表示またはフィルター
linktitle: ピボットテーブルで上位 10 件を表示またはフィルター
description: Aspose.Cells for Python via .NET を使用して、ピボットフィールドの項目を上位または下位に基づいて表示する方法を学びます。このinfectedPieceでは、Excel 97-2003 の top_10_auto_show メソッド、top_10_auto_show_settings によるオプションの読み取り、および filter_top10 による Excel 2007-365 の上位 10 件フィルターについて説明します。
keywords: Aspose.Cells, Python via .NET, ピボットテーブル, 上位 10 件, 自動表示, top_10_auto_show, top_10_auto_show_settings, PivotFieldTop10AutoShowSettings, filter_top10, PivotFilterType, PivotField, Python
type: docs
weight: 20
url: /ja/python-net/top-10-show-or-filter-in-pivot-table/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **考えられる利用シナリオ**
行フィールドのすべての項目を一覧表示するピボットテーブルは、フィールドに数十の項目がある場合は読み取りにくくなります。上位または下位と判定された項目のみを残す上位 10 件レポートは、「売上による上位 5 製品」や「販売件数による下位 3 地域」など、順位レポートで必要とされる機能そのものです。Aspose.Cells はこの機能のために 2 つのメカニズムをサポートしており、それぞれ Microsoft Excel の 2 つの世代に対応します。
- **Excel 97-2003 の自動表示** — `PivotField.top_10_auto_show()` メソッドです。これはピボットフィールドに直接保存される従来の「上位または下位 N 件を表示」設定です。初期のピボットテーブル形式の一部であるため、旧バージョンを含むすべての Excel バージョンで動作します。
- **Excel 2007-365 の上位 10 件フィルター** — `PivotField.filter_top10()` メソッドです。これは、フィールドメニューの「値フィルター」で利用できる新しい上位 10 件の値フィルターです。フィールドに関連付けられた `PivotFilter` オブジェクトとして保存され、項目数またはパーセントに基づく順位付けを提供します。

## **Excel 97-2003 における上位 10 件の表示 (top_10_auto_show)**
従来の自動表示は、`PivotField.top_10_auto_show(bool is_auto_show, bool is_top, int count, int rank_by)` を 1 回呼び出すことで設定します。
- `is_auto_show` — フィールドの自動表示設定を有効または無効にします。
- `is_top` — `True` の場合は順位が最も高い項目（上位）を保持し、`False` の場合は順位が最も低い項目（下位）を保持します。
- `count` — 保持する項目数です。例として、従来の上位 10 件レポートでは 10 を指定します。
- `rank_by` — 項目を順位付けする基準となる**データフィールド**の 0 始まりのインデックスです。フィールド自体を基準に項目を順位付けする場合は -1 を渡します。
順位付けは、値フィールドまたはフィールド自体を基準に実行できます。以下に 2 つの例を示します。

### **値フィールドによる順位付け**
`Sales` の合計などの通常の値フィールドを使用して、行フィールドの項目を順位付けできます。次の例では、行フィールド (`Sport`) とデータフィールド (`Sales`) を 1 つずつ持つピボットテーブルを作成し、売上上位 2 件のスポーツを表示します。`Sales` の合計はインデックス 0 のデータフィールドであるため、`rank_by` は 0 になります。

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.cells.get("A1").put_value("Sport")
worksheet.cells.get("B1").put_value("Quarter")
worksheet.cells.get("C1").put_value("Sales")
sports = ["Golf", "Tennis", "Rugby", "Cricket", "Boxing"]
row = 2
for sport in sports:
    for quarter in range(1, 4):
        worksheet.cells.get(row, 0).put_value(sport)
        worksheet.cells.get(row, 1).put_value("Qtr" + str(quarter))
        worksheet.cells.get(row, 2).put_value(1000 + 777 * row)
        row += 1
pivot_table = worksheet.pivot_tables.add("A1:C16", 2, 5)
pivot_table.add_field_to_area(PivotFieldType.ROW, "Sport")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Sales")
pivot_table.calculate_data()
sport_field = pivot_table.row_fields[0]
# 「Sum of Sales」で上位2項目を表示する（データフィールドのインデックス0）
sport_field.top_10_auto_show(True, True, 2, 0)
pivot_table.calculate_data()
workbook.save("output-top10-by-value-field.xlsx")
```

### **フィールド自体による順位付け**
フィールドの項目を、そのフィールド自体を基準に順位付けすることもできます。`rank_by` には -1 を渡します。この場合、追加のデータフィールドは不要です。フィールドが行領域または列領域に配置されていれば十分です。次の例では、フィールド自体を基準に順位付けした下位 3 件のスポーツを表示します。この設定を保存すると、-1 がこの形式の既定値であるため、`rank_by` 属性はピボットテーブル XML から省略され、`top_10_auto_show_settings.rank_by` から -1 が読み返されます。

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.cells.get("A1").put_value("Sport")
worksheet.cells.get("B1").put_value("Quarter")
worksheet.cells.get("C1").put_value("Sales")
sports = ["Golf", "Tennis", "Rugby", "Cricket", "Boxing"]
row = 2
for sport in sports:
    for quarter in range(1, 4):
        worksheet.cells.get(row, 0).put_value(sport)
        worksheet.cells.get(row, 1).put_value("Qtr" + str(quarter))
        worksheet.cells.get(row, 2).put_value(1000 + 777 * row)
        row += 1
pivot_table = worksheet.pivot_tables.add("A1:C16", 2, 5)
pivot_table.add_field_to_area(PivotFieldType.ROW, "Sport")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Sales")
pivot_table.calculate_data()
sport_field = pivot_table.row_fields[0]
sport_field.top_10_auto_show(True, False, 3, -1)
pivot_table.calculate_data()
workbook.save("output-top10-by-field-itself.xlsx")
```

## **現在のオプションの読み取り (top_10_auto_show_settings)**
`PivotField.top_10_auto_show_settings` プロパティは、フィールドに現在保存されている自動表示オプションを公開する `PivotFieldTop10AutoShowSettings` オブジェクトを返します。これを使用すると、既存のワークブックや、直前に設定したピボットテーブルの項目がどのように表示されるかを確認できます。ファイルから読み込んだワークブックも対象です。

```python
import aspose.cells as ac
workbook = ac.Workbook("output-top10-by-value-field.xlsx")
pivot_table = workbook.worksheets[0].pivot_tables[0]
sport_field = pivot_table.row_fields[0]
settings = sport_field.top_10_auto_show_settings
print("AutoShow enabled: " + str(settings.is_auto_show))
print("Direction: " + ("Top" if settings.is_top else "Bottom"))
print("Item count: " + str(settings.auto_show_count))
print("Ranking data field index: " + str(settings.rank_by))
```

この 4 つのプロパティは、ピボットテーブル XML に書き込まれる従来の自動表示属性 (`autoShow`、`topAutoShow`、`itemPageCount`、`rankBy`) に対応しています。したがって、読み返される値は、旧バージョンを含め、すべての Excel バージョンで有効となります。

## **注記**

{{% alert color="primary" %}}
- `PivotField` の直接プロパティである `is_auto_show`、`is_ascend_show`、`auto_show_count`、`auto_show_field` は、廃止済みとマークされています。代わりに `top_10_auto_show_settings` オブジェクトを使用してください。`is_auto_show` は `top_10_auto_show_settings.is_auto_show` に、`is_ascend_show` は `top_10_auto_show_settings.is_top` に、`auto_show_count` は `top_10_auto_show_settings.auto_show_count` に、`auto_show_field` は `top_10_auto_show_settings.rank_by` に対応します。設定を変更するには、`top_10_auto_show()` メソッドを使用します。
- `top_10_auto_show` は行フィールドと列フィールドで機能します。ページ（フィルター）領域のみにあるフィールドは、項目がピボットテーブルの本体に配置されないため、この方法では順位付けできません。
{{% /alert %}}

## **Excel 2007-365：上位 10 件フィルター (filter_top10)**
Excel 2007 以降では、フィールドメニューの「値フィルター」→「上位 10 件...」から、上位 10 件を値フィルターとして利用できます。Aspose.Cells では、この機能は `PivotField.filter_top10(int value_field_index, PivotFilterType type, bool is_top, int item_count)` メソッドを使用して実装され、作成された `PivotFilter` が返されます。
- `value_field_index` — 集計値に基づいて項目を順位付けするデータフィールドの 0 始まりのインデックスです。
- `type` — `item_count` の意味を指定します。`PivotFilterType.COUNT` は固定数の項目を保持します（ダイアログの「アイテム」オプション）。`PivotFilterType.PERCENT` は項目の一定割合を保持します。この場合、`item_count` 自体がパーセント値です。30 を指定すると上位 30 パーセントを保持します。`PivotFilterType.SUM` は累積値の到達割合に基づいて順位付けします。
- `is_top` — 上位の場合は `True`、下位の場合は `False` です。
- `item_count` — 「上位 N 件」の N に相当します。その単位は `type` によって異なります。

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType, PivotFilterType
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.cells.get("A1").put_value("Sport")
worksheet.cells.get("B1").put_value("Quarter")
worksheet.cells.get("C1").put_value("Sales")
sports = ["Golf", "Tennis", "Rugby", "Cricket", "Boxing"]
row = 2
for sport in sports:
    for quarter in range(1, 4):
        worksheet.cells.get(row, 0).put_value(sport)
        worksheet.cells.get(row, 1).put_value("Qtr" + str(quarter))
        worksheet.cells.get(row, 2).put_value(1000 + 777 * row)
        row += 1
pivot_table = worksheet.pivot_tables.add("A1:C16", 2, 5)
pivot_table.add_field_to_area(PivotFieldType.ROW, "Sport")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Sales")
pivot_table.calculate_data()
sport_field = pivot_table.row_fields[0]
# Top 10 フィルター — "Sum of Sales" に基づいて先頭 2 項目を保持（データフィールドのインデックス 0）
filter = sport_field.filter_top10(0, PivotFilterType.COUNT, True, 2)
# 代わりにパーセントベースのフィルターを使用する場合は、項目の先頭 30 パーセントを保持します:
# sport_field.filter_top10(0, PivotFilterType.PERCENT, True, 30)
pivot_table.pivot_cache.refresh()
pivot_table.calculate_data()
workbook.save("output-top10-filter.xlsx")
```

{{% alert color="primary" %}}
`top_10_auto_show` と `filter_top10` は別々の機能です。自動表示は、ピボットフィールドに設定された従来の `autoShow` 属性群を書き出し、Excel 97 を含むすべての Excel バージョンで尊重されます。`filter_top10` は新しい `PivotFilter` エントリを書き出すため、Excel 2007 以降が必要です。古いバージョンの Excel でワークブックを開くと、新しいフィルターを使用しているピボットテーブルは、フォールバックとしてすべての項目を表示します。旧バージョンのツールで往復処理する必要があるドキュメントでは `top_10_auto_show` を使用してください。Excel 2007 以降のワークブックでは `filter_top10` を使用してください。`filter_top10` は他の値フィルターと組み合わせることができるためです。
{{% /alert %}}

## **関連記事**
- [ラベルまたは値によるピボットテーブルのフィルター](/cells/ja/python-net/filter-by-label-or-value-of-pivot-table/)
- [ピボットテーブルに行フィールドと列フィールドを追加](/cells/ja/python-net/pivot-table-add-row-and-column-fields/)
- [ピボットテーブル内でピボットフィールドをグループ化](/cells/ja/python-net/group-pivot-fields-in-the-pivot-table/)
- [ピボットテーブルの更新](/cells/ja/python-net/refresh-pivot-table/)
- [ピボットテーブルにページフィールドを追加](/cells/ja/python-net/add-page-field-in-pivot-table/)

{{< app/cells/assistant language="python-net" >}}