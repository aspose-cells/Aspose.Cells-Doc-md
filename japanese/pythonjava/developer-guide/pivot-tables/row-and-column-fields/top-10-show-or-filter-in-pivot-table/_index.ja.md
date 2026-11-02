---
title: ピボットテーブルで上位10件を表示またはフィルター処理
linktitle: ピボットテーブルで上位10件を表示またはフィルター処理
description: Aspose.Cells for Python via Java を使用して、ピボットフィールドの上位または下位の項目のみを表示する方法を学びます。この記事では、Excel 97-2003 の top10AutoShow メソッド、Top10AutoShowSettings によるオプションの読み取り、Excel 2007-365 の filterTop10 による上位10件のフィルター処理について説明します。
keywords: Aspose.Cells for Python via Java, ピボットテーブル, 上位10件, 自動表示, top10AutoShow, Top10AutoShowSettings, PivotFieldTop10AutoShowSettings, filterTop10, PivotFilterType, PivotField, Python
type: docs
weight: 20
url: /ja/python-java/top-10-show-or-filter-in-pivot-table/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **考えられる利用シナリオ**
行フィールドのすべての項目を一覧表示するピボットテーブルは、そのフィールドに数十の項目がある場合は読み取りにくくなります。Top 10 レポートでは、上位または下位の項目だけを残せるため、「売上上位5製品」や「販売数下位3地域」のような順位レポートに最適です。Aspose.Cells はこの用途に対応する2つのメカニズムをサポートしており、それぞれ Microsoft Excel の2つの世代に対応しています。
- **Excel 97-2003 の AutoShow** — `PivotField.top10AutoShow()` メソッドです。これは、ピボットフィールドに直接保存される従来型の「上位/下位 N 件を表示」設定です。元のピボットテーブル形式の一部であるため、新旧のすべての Excel バージョンで動作します。
- **Excel 2007-365 の上位10件フィルター** — `PivotField.filterTop10()` メソッドです。これは、フィールドメニューの「値フィルター」に含まれる新しい上位10件の値フィルターです。フィールドに適用された `PivotFilter` オブジェクトとして保存され、項目数またはパーセントに基づくランキングを提供します。

## **Excel 97-2003 での上位10件の表示 (top10AutoShow)**
従来型の AutoShow は、`PivotField.top10AutoShow(boolean isAutoShow, boolean isTop, int count, int rankBy)` を1回呼び出すことで設定できます。
- `isAutoShow` — フィールドの AutoShow 設定を有効または無効にします。
- `isTop` — `True` の場合は上位項目を維持し、`False` の場合は下位項目を維持します。
- `count` — 維持する項目数です。たとえば、従来型の Top 10 レポートでは10を指定します。
- `rankBy` — 項目を順位付けする**データフィールド**の0始まりのインデックスです。項目をフィールド自体で順位付けするには -1 を指定します。
順位付けは値フィールドまたはフィールド自体に基づいて実行できます。以下に、代表的な2つの方法を示します。

### **値フィールドによる順位付け**
行フィールドの項目を、`Sales` の合計などの通常の値フィールドで順位付けします。次の例では、行フィールド (`Sport`) とデータフィールド (`Sales`) をそれぞれ1つ持つピボットテーブルを作成し、売上上位2件のスポーツを表示します。「`Sales` の合計」はインデックス0にあるデータフィールドであるため、`rankBy` は0です。

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, PivotFieldType
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
worksheet.getCells().get("A1").putValue("Sport")
worksheet.getCells().get("B1").putValue("Quarter")
worksheet.getCells().get("C1").putValue("Sales")
sports = ["Golf", "Tennis", "Rugby", "Cricket", "Boxing"]
row = 2
for sport in sports:
    for quarter in range(1, 4):
        worksheet.getCells().get(row, 0).putValue(sport)
        worksheet.getCells().get(row, 1).putValue("Qtr" + str(quarter))
        worksheet.getCells().get(row, 2).putValue(1000 + 777 * row)
        row += 1
pivot_table = worksheet.getPivotTables().add("A1:C16", 2, 5)
pivot_table.addFieldToArea(PivotFieldType.ROW, "Sport")
pivot_table.addFieldToArea(PivotFieldType.DATA, "Sales")
pivot_table.calculateData()
sport_field = pivot_table.getRowFields().get(0)
sport_field.setAutoShow(True)
sport_field.setAutoShowCount(2)
sport_field.setAutoShowField(2)
pivot_table.calculateData()
workbook.save("output-top10-by-value-field.xlsx")
jpype.shutdownJVM()
```

### **フィールド自体による順位付け**
フィールド自体で順位付けすることもできます。この場合は `rankBy` に -1 を指定します。この方法では追加のデータフィールドは不要であり、フィールドを行（または列）領域に配置するだけです。次の例では、フィールド自体で順位付けした下位3件のスポーツを表示します。この設定を保存すると、-1 はこの形式の既定値であるため、`rankBy` 属性はピボットテーブル XML から省略されます。また、`Top10AutoShowSettings.getRankBy()` で -1 が読み取られます。

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
worksheet.getCells().get("A1").putValue("Sport")
worksheet.getCells().get("B1").putValue("Quarter")
worksheet.getCells().get("C1").putValue("Sales")
sports = ["Golf", "Tennis", "Rugby", "Cricket", "Boxing"]
row = 2
for sport in sports:
    for quarter in range(1, 4):
        worksheet.getCells().get(row, 0).putValue(sport)
        worksheet.getCells().get(row, 1).putValue("Qtr" + str(quarter))
        worksheet.getCells().get(row, 2).putValue(1000 + 777 * row)
        row += 1
pivot_table = worksheet.getPivotTables().add("A1:C16", 2, 5)
pivot_table.addFieldToArea(PivotFieldType.ROW, "Sport")
pivot_table.addFieldToArea(PivotFieldType.DATA, "Sales")
pivot_table.calculateData()
sport_field = pivot_table.getRowFields().get(0)
# フィールド自体でランキングされた下位3つの項目を表示する（rankBy = -1）
sport_field.top10AutoShow(True, False, 3, -1)
pivot_table.calculateData()
workbook.save("output-top10-by-field-itself.xlsx")
jpype.shutdownJVM()
```

## **現在のオプションの読み取り (Top10AutoShowSettings)**
`PivotField.getTop10AutoShowSettings()` メソッドは、フィールドに現在保存されている AutoShow オプションを表す `PivotFieldTop10AutoShowSettings` オブジェクトを返します。既存のワークブックや直前に設定したピボットテーブルで項目がどのように表示されるかを確認できます。ファイルから読み込んだワークブックも対象です。

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat
workbook = Workbook("output-top10-by-value-field.xlsx")
pivot_table = workbook.getWorksheets().get(0).getPivotTables().get(0)
sport_field = pivot_table.getRowFields()[0]
settings = sport_field.getTop10AutoShowSettings()
print("AutoShow enabled: " + str(settings.isAutoShow()))
print("Direction: " + ("Top" if settings.isTop() else "Bottom"))
print("Item count: " + str(settings.getAutoShowCount()))
print("Ranking data field index: " + str(settings.getRankBy()))
jpype.shutdownJVM()
```

4つのプロパティは、ピボットテーブル XML に書き込まれる従来型の AutoShow 属性 (`autoShow`、`topAutoShow`、`itemPageCount`、`rankBy`) に対応しています。したがって、読み取られた値は、すべての Excel バージョンで有効な設定値です。

## **注記**

{{% alert color="primary" %}}
- `PivotField` の直接アクセサーである `isAutoShow()`、`isAscendShow()`、`getAutoShowCount()`、`getAutoShowField()` は非推奨としてマークされています。代わりに `Top10AutoShowSettings` オブジェクトを使用してください。`PivotField.isAutoShow()` は `Top10AutoShowSettings.isAutoShow()` に、`PivotField.isAscendShow()` は `Top10AutoShowSettings.isTop()` に、`PivotField.getAutoShowCount()` は `Top10AutoShowSettings.getAutoShowCount()` に、`PivotField.getAutoShowField()` は `Top10AutoShowSettings.getRankBy()` に相当します。設定を変更するには、`top10AutoShow()` メソッドを使用してください。
- `top10AutoShow` は行フィールドと列フィールドで使用できます。ページ（フィルター）領域にのみ配置されているフィールドは、その項目がピボットテーブルの本体部分に配置されないため、この方法では順位付けできません。
{{% /alert %}}

## **Excel 2007-365: 上位10件のフィルター (filterTop10)**
新しい Excel バージョンでは、フィールドメニューの「値フィルター」→「上位10件...」から上位10件のフィルターを設定できます。Aspose.Cells では、この機能は `PivotField.filterTop10(int valueFieldIndex, PivotFilterType type, boolean isTop, int itemCount)` メソッドで表されます。このメソッドは、作成された `PivotFilter` を返します。
- `valueFieldIndex` — 集計値によって項目を順位付けするデータフィールドの0始まりのインデックスです。
- `type` — `itemCount` の意味を指定します。`PivotFilterType.COUNT` は固定数の項目を残します（ダイアログの「項目」オプション）。`PivotFilterType.PERCENT` は項目の指定割合を残します。そのため `itemCount` は割合自体を示します。30と指定すると、上位30%を残します。`PivotFilterType.SUM` は累積値によるカバレッジに基づいて順位付けします。
- `isTop` — 上位の場合は `True`、下位の場合は `False` です。
- `itemCount` — 上位 N 件における N を表します。その単位は `type` によって異なります。

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType, PivotFilterType
try:
    workbook = Workbook()
    worksheet = workbook.getWorksheets().get(0)
    worksheet.getCells().get("A1").putValue("Sport")
    worksheet.getCells().get("B1").putValue("Quarter")
    worksheet.getCells().get("C1").putValue("Sales")
    sports = ["Golf", "Tennis", "Rugby", "Cricket", "Boxing"]
    row = 2
    for sport in sports:
        for quarter in range(1, 4):
            worksheet.getCells().get(row, 0).putValue(sport)
            worksheet.getCells().get(row, 1).putValue("Qtr" + str(quarter))
            worksheet.getCells().get(row, 2).putValue(1000 + 777 * row)
            row += 1
    pivot_table = worksheet.getPivotTables().add("A1:C16", 2, 5)
    pivot_table.addFieldToArea(PivotFieldType.ROW, "Sport")
    pivot_table.addFieldToArea(PivotFieldType.DATA, "Sales")
    pivot_table.calculateData()
    sport_field = pivot_table.getRowFields().get(0)
    # Top 10 フィルター — 「Sum of Sales」で上位2項目を保持します（データフィールドインデックス 0）
    filter = sport_field.filterTop10(0, PivotFilterType.COUNT, True, 2)
    # パーセンテージベースのフィルターを使用する場合は、項目の上位30%を保持します:
    # sport_field.filterTop10(0, PivotFilterType.PERCENT, True, 30)
    pivot_table.getPivotCache().refresh()
    pivot_table.calculateData()
    workbook.save("output-top10-filter.xlsx")
finally:
    jpype.shutdownJVM()
```

{{% alert color="primary" %}}
`top10AutoShow` と `filterTop10` は別々の機能です。AutoShow は、ピボットフィールドに従来型の `autoShow` 属性一式を書き込むため、Excel 97以降のすべての Excel バージョンで適用されます。`filterTop10` は新しい `PivotFilter` エントリを書き込むため、Excel 2007以降が必要です。古い Excel バージョンでワークブックを開くと、新しいフィルターを使用しているピボットテーブルは、すべての項目を表示するフォールバック動作になります。レガシートゥールとのラウンドトリップが必要な文書では `top10AutoShow` を、新しいワークブックでは、他の値フィルターと組み合わせて使用できる `filterTop10` を使用してください。
{{% /alert %}}

## **関連記事**
- [ラベルまたは値によるピボットテーブルのフィルター処理](/cells/ja/python-java/filter-by-label-or-value-of-pivot-table/)
- [ピボットテーブルに行と列のフィールドを追加](/cells/ja/python-java/pivot-table-add-row-and-column-fields/)
- [ピボットテーブル内でピボットフィールドをグループ化](/cells/ja/python-java/group-pivot-fields-in-the-pivot-table/)
- [ピボットテーブルの更新](/cells/ja/python-java/refresh-pivot-table/)
- [ピボットテーブルにページフィールドを追加](/cells/ja/python-java/add-page-field-in-pivot-table/)

{{< app/cells/assistant language="python" >}}