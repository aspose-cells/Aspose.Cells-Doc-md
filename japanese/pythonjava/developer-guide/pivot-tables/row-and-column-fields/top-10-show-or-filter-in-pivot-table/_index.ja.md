---
title: ピボットテーブルで上位10件の表示またはフィルター
linktitle: ピボットテーブルで上位10件の表示またはフィルター
description: Aspose.Cells for Python via Javaでピボットフィールドの上位または下位の項目のみを表示する方法を学びます。本記事ではExcel 97-2003のtop10AutoShowメソッド、Top10AutoShowSettingsを使用したオプションの取得、Excel 2007-365のfilterTop10によるトップ10フィルターについて解説します。
keywords: Aspose.Cells for Python via Java, ピボットテーブル, 上位10, 自動表示, top10AutoShow, Top10AutoShowSettings, PivotFieldTop10AutoShowSettings, filterTop10, PivotFilterType, PivotField, Python
type: docs
weight: 20
url: /ja/python-java/top-10-show-or-filter-in-pivot-table/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **使用シナリオ**
行フィールドのすべての項目を列挙するピボットテーブルは、メンバーが数十ある場合、読み取りにくくなります。トップ10レポートは、最も高いまたは低いランクの項目だけを保持し、ランク付けレポートに最適です――「売上高上位5商品」や「販売件数下位3地域」などです。Aspose.Cellsはこの目的のために2つのメカニズムをサポートしており、Microsoft Excelの2つの世代に対応しています。
- **Excel 97-2003 AutoShow** — `PivotField.top10AutoShow()` メソッド。ピボットフィールドに直接保存される古典的な「上位/下位 N 項目を表示」設定です。元のピボットテーブル形式の一部であるため、古いバージョンでも新しいバージョンでもすべてのExcelで動作します。
- **Excel 2007-365 Top 10 Filter** — `PivotField.filterTop10()` メソッド。フィールドメニューの「値フィルター」配下にあるモダンなトップ10値フィルターです。`PivotFilter` オブジェクトとしてフィールドに添付され、項目数またはパーセンテージによるランク付けを提供します。

## **Excel 97-2003 のトップ10表示 (top10AutoShow)**
古典的な AutoShow は、`PivotField.top10AutoShow(boolean isAutoShow, boolean isTop, int count, int rankBy)` の 1 回の呼び出しで構成します。
- `isAutoShow` — フィールドの AutoShow 設定を有効または無効にします。
- `isTop` — `True` は上位項目 (Top) を保持し、`False` は下位項目 (Bottom) を保持します。
- `count` — 保持する項目数。たとえばクラシックなトップ10レポートでは 10 を指定します。
- `rankBy` — アイテムをランク付けする **データ フィールド** のゼロベースインデックス。フィールド自体でランク付けする場合は -1 を渡します。
ランク付けは値フィールドまたはフィールド自体によって行うことができます。以下に2つの自然なバリエーションを示します。

### **値フィールドでランク付け**
売上合計などの通常の値フィールドで行フィールドの項目をランク付けします。次の例は、行フィールド (`Sport`) とデータフィールド (`Sales`) を持つピボットテーブルを作成し、売上上位 2 スポーツを表示します。`rankBy` は「売上合計」がインデックス 0 のデータフィールドであるため 0 です。

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
sport_field.top10AutoShow(True, True, 2, 0)
pivot_table.calculateData()
workbook.save("output-top10-by-value-field.xlsx")
jpype.shutdownJVM()
```

### **フィールド自体でランク付け**
フィールド自体でランク付けすることも可能です――`rankBy` に -1 を渡します。このバリエーションでは追加のデータフィールドは不要で、フィールドは行（または列）領域に配置されているだけで構いません。次の例は、フィールド自体でランク付けした下位 3 スポーツを表示します。この設定が保存されると、`rankBy` 属性はデフォルト値 -1 のためピボットテーブル XML から省略され、`Top10AutoShowSettings.getRankBy()` は -1 を返します。

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
# Show the bottom 3 items ranked by the field itself (rankBy = -1)
sport_field.top10AutoShow(True, False, 3, -1)
pivot_table.calculateData()
workbook.save("output-top10-by-field-itself.xlsx")
jpype.shutdownJVM()
```

## **現在のオプションの取得 (Top10AutoShowSettings)**
`PivotField.getTop10AutoShowSettings()` メソッドは、フィールドに現在保存されている AutoShow オプションを表す `PivotFieldTop10AutoShowSettings` オブジェクトを返します。これを使用して、既存のワークブックや、直前に設定したピボットテーブルがどのように項目を表示するか（ファイルからロードしたワークブックを含む）を確認できます。

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

4 つのプロパティは、ピボットテーブル XML に書き込まれる古典的な AutoShow 属性 (`autoShow`、`topAutoShow`、`itemPageCount`、`rankBy`) に対応しているため、読み戻された値はすべての Excel バージョンで正しく解釈されます。

## **注意**

{{% alert color="primary" %}}
- 直接の `PivotField` アクセサ `isAutoShow()`、`isAscendShow()`、`getAutoShowCount()`、`getAutoShowField()` は廃止予定です。代わりに `Top10AutoShowSettings` オブジェクトを使用してください：`PivotField.isAutoShow()` は `Top10AutoShowSettings.isAutoShow()` に、`PivotField.isAscendShow()` は `Top10AutoShowSettings.isTop()` に、`PivotField.getAutoShowCount()` は `Top10AutoShowSettings.getAutoShowCount()` に、`PivotField.getAutoShowField()` は `Top10AutoShowSettings.getRankBy()` に置き換わります。設定を変更するサポートされた方法は `top10AutoShow()` メソッドです。
- `top10AutoShow` は行フィールドおよび列フィールドで動作します。ページ（フィルター）領域にのみ配置されたフィールドは、ピボット本体に項目が展開されないためこの方法でランク付けできません。
{{% /alert %}}

## **Excel 2007-365: トップ10フィルター (filterTop10)**
モダンな Excel バージョンでは、トップ10がフィールドメニューの「値フィルター」（Top 10…）として提供されます。Aspose.Cells はこれを `PivotField.filterTop10(int valueFieldIndex, PivotFilterType type, boolean isTop, int itemCount)` メソッドでモデル化し、作成された `PivotFilter` を返します。
- `valueFieldIndex` — 項目をランク付けする集計値を持つデータフィールドのゼロベースインデックス。
- `type` — `itemCount` の意味を指定します。`PivotFilterType.COUNT` は固定項目数（ダイアログの Items オプション）を保持し、`PivotFilterType.PERCENT` は項目のパーセンテージを保持します（例: 30 は上位 30 %）。`PivotFilterType.SUM` は累積値カバレッジでランク付けします。
- `isTop` — `True` は上位、`False` は下位を表します。
- `itemCount` — Top N の N 値で、単位は `type` に依存します。

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
    # Top 10 Filter — keep the top 2 items by "Sum of Sales" (data field index 0)
    filter = sport_field.filterTop10(0, PivotFilterType.COUNT, True, 2)
    # For a percentage-based filter instead, keep the top 30 percent of the items:
    # sport_field.filterTop10(0, PivotFilterType.PERCENT, True, 30)
    pivot_table.getPivotCache().refresh()
    pivot_table.calculateData()
    workbook.save("output-top10-filter.xlsx")
finally:
    jpype.shutdownJVM()
```

{{% alert color="primary" %}}
`top10AutoShow` と `filterTop10` は別々の機能です。AutoShow はピボットフィールドに古典的な `autoShow` 属性を書き込み、Excel 97 以降のすべてのバージョンで認識されます。`filterTop10` はモダンな `PivotFilter` エントリを書き込み、Excel 2007 以降が必要です。古い Excel バージョンでワークブックを開くと、モダンフィルターを使用したピボットテーブルは全項目が表示されるようにフォールバックします。レガシー環境との往復が必要な文書では `top10AutoShow` を、モダンなワークブックでは他の値フィルターと組み合わせやすい `filterTop10` を推奨します。
{{% /alert %}}

## **関連記事**
- [ラベルまたは値によるピボットテーブルのフィルタリング](/cells/ja/python-java/filter-by-label-or-value-of-pivot-table/)
- [ピボットテーブルの行および列フィールドの追加](/cells/ja/python-java/pivot-table-add-row-and-column-fields/)
- [ピボットテーブル内でのピボットフィールドのグループ化](/cells/ja/python-java/group-pivot-fields-in-the-pivot-table/)
- [ピボットテーブルの更新](/cells/ja/python-java/refresh-pivot-table/)
- [ピボットテーブルにページフィールドを追加](/cells/ja/python-java/add-page-field-in-pivot-table/)

{{< app/cells/assistant language="python" >}}