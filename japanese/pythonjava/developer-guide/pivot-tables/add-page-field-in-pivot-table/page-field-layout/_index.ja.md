---
title: ピボットテーブルでページフィールドのレイアウトを変更する
linktitle: ピボットテーブルでページフィールドのレイアウトを変更する
description: Aspose.Cells for Python via Java を使用して、ピボットテーブルのページフィールド領域のレイアウトを制御する方法を学びます。表示順序、折り返し数、ピボットテーブル上部にあるページフィールドのフィールド順序の設定を含みます。
keywords: Aspose.Cells for Python via Java, Python Java ライブラリ, スプレッドシート, ピボットテーブル, ページフィールド, ページフィールドの順序, ページフィールドの折り返し数, ページフィールドの移動
type: docs
weight: 191
url: /ja/python-java/change-page-field-layout/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
この記事は **ピボットテーブルにページフィールドを追加する** トピックの続編です。表示順序、折り返し数、フィールドの並び替えなど、ピボットテーブル上部のフィルターコントロールの帯であるページフィールド領域のレイアウトを制御する方法を説明します。
{{% /alert %}}

## **Introduction**
Microsoft Excel のピボットテーブルには、テーブルの行/列/データ本体の上に位置する専用の **ページフィールド領域** があります。この領域はドロップダウンフィルターコントロールの帯として描画され (ページフィールドごとに 1 つ)、エンドユーザーが年や地域などの条件でピボットをスライスするためにクリックする部分です。Aspose.Cells for Python via Java は、この領域を `pivot_table.page_fields` コレクションを通じてモデル化し、帯の視覚的なレイアウトを制御する 3 つのプロパティを公開しています。
- `pivot_table.page_field_order` (`Aspose.Cells.PrintOrderType` の値) は、追加のページフィールドを既存のフィールドの *隣* に配置するか、*下* に配置するかを決定します。
- `pivot_table.page_field_wrap_count` は、折り返し前に行または列ごとに配置されるページフィールドの数を設定します。
- `pivot_table.page_fields.move(curr_index, dest_index)` は、順序モードを変更せずにページフィールドを並び替えます。
この記事では、共有データセットに対してこれらの各操作を実演する 3 つのコード例を順に説明し、結果を並べて比較できるようにします。

## **Source Data**
| 果物  | 年  | 地域  | 数量  |
|--------|------|--------|--------|
| リンゴ  | 2022 | 北部  | 150    |
| リンゴ  | 2023 | 北部  | 180    |
| バナナ | 2022 | 南部  | 120    |
| バナナ | 2023 | 南部  | 140    |
| さくらんぼ | 2022 | 東部   | 200    |
| さくらんぼ | 2023 | 東部   | 220    |
| ぶどう  | 2022 | 西部   | 90     |
| ぶどう  | 2023 | 西部   | 110    |
8 行すべてがすべてのコード例で同じ順序で入力されているため、シナリオ間でソースデータが変更されることはありません。変更されるのはページフィールドのレイアウトプロパティのみです。

## **Example 1: Over Then Down**
最初のシナリオでは、2 つのページフィールド (`Year`、`Region`) をピボットテーブル上部の **1 行に横並びで** 表示するように設定します。`Fruit` を行軸に割り当て、ページ軸には `Year` を最初に、`Region` を 2 番目に配置し (`add_field_to_area` 呼び出しの順序が開始インデックスを決定します)、データフィールドとして `Amount` (合計) を追加します。次に、`page_field_order` を `PrintOrderType.OVER_THEN_DOWN` に設定し、`page_field_wrap_count = 2` とします。`OVER_THEN_DOWN` と折り返し数 2 により、2 つのページフィールドはピボットテーブル上部の 1 行に横並びでレイアウトされるため、帯は幅 2 の 1 行を占めます。

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, WorksheetCollection, Worksheet, Cells, PivotTableCollection, PivotTable, PivotFieldType, ConsolidationFunction, PrintOrderType
dataDir = "output"
if not os.path.exists(dataDir):
    os.makedirs(dataDir, exist_ok=True)
workbook = Workbook()
worksheets = workbook.getWorksheets()
pivotDataIdx = worksheets.add("PivotData")
pivotDataSheet = worksheets.get(pivotDataIdx)
pivotDataCells = pivotDataSheet.getCells()
# Headers (row 0)
pivotDataCells.get(0, 0).putValue("Fruit")
pivotDataCells.get(0, 1).putValue("Year")
pivotDataCells.get(0, 2).putValue("Region")
pivotDataCells.get(0, 3).putValue("Amount")
# Row 1: Apple, 2022, North, 150
pivotDataCells.get(1, 0).putValue("Apple")
pivotDataCells.get(1, 1).putValue(2022)
pivotDataCells.get(1, 2).putValue("North")
pivotDataCells.get(1, 3).putValue(150)
# Row 2: Apple, 2023, North, 180
pivotDataCells.get(2, 0).putValue("Apple")
pivotDataCells.get(2, 1).putValue(2023)
pivotDataCells.get(2, 2).putValue("North")
pivotDataCells.get(2, 3).putValue(180)
# Row 3: Banana, 2022, South, 120
pivotDataCells.get(3, 0).putValue("Banana")
pivotDataCells.get(3, 1).putValue(2022)
pivotDataCells.get(3, 2).putValue("South")
pivotDataCells.get(3, 3).putValue(120)
# Row 4: Banana, 2023, South, 140
pivotDataCells.get(4, 0).putValue("Banana")
pivotDataCells.get(4, 1).putValue(2023)
pivotDataCells.get(4, 2).putValue("South")
pivotDataCells.get(4, 3).putValue(140)
# Row 5: Cherry, 2022, East, 200
pivotDataCells.get(5, 0).putValue("Cherry")
pivotDataCells.get(5, 1).putValue(2022)
pivotDataCells.get(5, 2).putValue("East")
pivotDataCells.get(5, 3).putValue(200)
# Row 6: Cherry, 2023, East, 220
pivotDataCells.get(6, 0).putValue("Cherry")
pivotDataCells.get(6, 1).putValue(2023)
pivotDataCells.get(6, 2).putValue("East")
pivotDataCells.get(6, 3).putValue(220)
# Row 7: Grape, 2022, West, 90
pivotDataCells.get(7, 0).putValue("Grape")
pivotDataCells.get(7, 1).putValue(2022)
pivotDataCells.get(7, 2).putValue("West")
pivotDataCells.get(7, 3).putValue(90)
# Row 8: Grape, 2023, West, 110
pivotDataCells.get(8, 0).putValue("Grape")
pivotDataCells.get(8, 1).putValue(2023)
pivotDataCells.get(8, 2).putValue("West")
pivotDataCells.get(8, 3).putValue(110)
# Add PivotTableReport sheet
pivotTableSheetIdx = worksheets.add("PivotTableReport")
pivotTableSheet = worksheets.get(pivotTableSheetIdx)
pivotTables = pivotTableSheet.getPivotTables()
# Create pivot table sourced from PivotData!A1:D9 placed at A1 on PivotTableReport
pivotIndex = pivotTables.add("PivotData!A1:D9", "A1", "PivotTable1")
pivotTable = pivotTables.get(pivotIndex)
# Add fields
pivotTable.addFieldToArea(PivotFieldType.ROW, 0)   # Fruit
pivotTable.addFieldToArea(PivotFieldType.PAGE, 1)  # Year
pivotTable.addFieldToArea(PivotFieldType.PAGE, 2)  # Region
pivotTable.addFieldToArea(PivotFieldType.DATA, 3)  # Amount
pivotTable.getDataFields().get(0).setFunction(ConsolidationFunction.SUM)
# Configure page field area layout: place page fields across first, wrap after every 2
pivotTable.setPageFieldOrder(PrintOrderType.OVER_THEN_DOWN)
pivotTable.setPageFieldWrapCount(2)
# Refresh and calculate
pivotTable.calculateData()
# Save
workbook.save(os.path.join(dataDir, "pageFieldLayout_overThenDown.xlsx"))
jpype.shutdownJVM()
```

## **Example 2: Down Then Over**
この例では、例 1 とまったく同様に、`Fruit` を行軸に、`Year` と `Region` をページ軸に (`Year` が最初)、`Amount` (合計) をデータフィールドとして配置します。次に、`page_field_order` を `PrintOrderType.DOWN_THEN_OVER` に、`page_field_wrap_count` を `2` に設定します。`DOWN_THEN_OVER` と折り返し数 2 により、2 つのページフィールドは垂直に積み上げられ、`Year` が上に、`Region` がその直下に配置され、ピボットテーブル上部に 1 列を形成します。したがって、帯は幅 1 で高さ 2 行を占め、例 1 とは対照的になります。

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, PivotFieldType, PrintOrderType
workbook = Workbook()
pivotData = workbook.getWorksheets().get(0)
pivotData.setName("PivotData")
pivotReportIdx = workbook.getWorksheets().add("PivotTableReport")
pivotReport = workbook.getWorksheets().get(pivotReportIdx)
headers = ["Fruit", "Year", "Region", "Amount"]
for c in range(len(headers)):
    pivotData.getCells().get(0, c).putValue(headers[c])
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
        pivotData.getCells().get(r + 1, c).putValue(data[r][c])
idx = pivotReport.getPivotTables().add("PivotData!A1:D9", "A1", "PivotTable")
pivotTable = pivotReport.getPivotTables().get(idx)
pivotTable.addFieldToArea(PivotFieldType.ROW, 0)
pivotTable.addFieldToArea(PivotFieldType.PAGE, 1)
pivotTable.addFieldToArea(PivotFieldType.PAGE, 2)
pivotTable.addFieldToArea(PivotFieldType.DATA, 3)
pivotTable.setPageFieldOrder(PrintOrderType.DOWN_THEN_OVER)
pivotTable.setPageFieldWrapCount(2)
pivotTable.calculateData()
workbook.save("pageFieldLayout_downThenOver.xlsx")
jpype.shutdownJVM()
```

## **Example 3: Move a Page Field**
3 番目のシナリオでは、このデータセットとフィールド割り当てを維持し、中立的なレイアウト (`OVER_THEN_DOWN` と折り返し数 `2`) を設定してから、`page_fields.move` 操作を実演します。`move(0, 1)` 呼び出しは、インデックス 0 にあるページフィールド (`Year`) を位置 1 に移動し、位置 1 にあったページフィールド (`Region`) を位置 0 にシフトします。この呼び出しの後、`Region` が最初のページフィールドとなり、`Year` が 2 番目のページフィールドとなります。折り返しと順序モードは変更されていないため、帯は依然として横並びにレンダリングされます。2 つのドロップダウンの順序のみが入れ替わっています。

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType, PrintOrderType
workbook = Workbook()
dataSheet = workbook.getWorksheets().get(0)
dataSheet.setName("PivotData")
dataSheet.getCells().get("A1").putValue("Fruit")
dataSheet.getCells().get("B1").putValue("Year")
dataSheet.getCells().get("C1").putValue("Region")
dataSheet.getCells().get("D1").putValue("Amount")
dataSheet.getCells().get("A2").putValue("Apple")
dataSheet.getCells().get("B2").putValue(2022)
dataSheet.getCells().get("C2").putValue("North")
dataSheet.getCells().get("D2").putValue(150)
dataSheet.getCells().get("A3").putValue("Apple")
dataSheet.getCells().get("B3").putValue(2023)
dataSheet.getCells().get("C3").putValue("North")
dataSheet.getCells().get("D3").putValue(180)
dataSheet.getCells().get("A4").putValue("Banana")
dataSheet.getCells().get("B4").putValue(2022)
dataSheet.getCells().get("C4").putValue("South")
dataSheet.getCells().get("D4").putValue(120)
dataSheet.getCells().get("A5").putValue("Banana")
dataSheet.getCells().get("B5").putValue(2023)
dataSheet.getCells().get("C5").putValue("South")
dataSheet.getCells().get("D5").putValue(140)
dataSheet.getCells().get("A6").putValue("Cherry")
dataSheet.getCells().get("B6").putValue(2022)
dataSheet.getCells().get("C6").putValue("East")
dataSheet.getCells().get("D6").putValue(200)
dataSheet.getCells().get("A7").putValue("Cherry")
dataSheet.getCells().get("B7").putValue(2023)
dataSheet.getCells().get("C7").putValue("East")
dataSheet.getCells().get("D7").putValue(220)
dataSheet.getCells().get("A8").putValue("Grape")
dataSheet.getCells().get("B8").putValue(2022)
dataSheet.getCells().get("C8").putValue("West")
dataSheet.getCells().get("D8").putValue(90)
dataSheet.getCells().get("A9").putValue("Grape")
dataSheet.getCells().get("B9").putValue(2023)
dataSheet.getCells().get("C9").putValue("West")
dataSheet.getCells().get("D9").putValue(110)
pivotSheetIdx = workbook.getWorksheets().add("PivotTableReport")
pivotSheet = workbook.getWorksheets().get(pivotSheetIdx)
pivotIdx = pivotSheet.getPivotTables().add("PivotData!A1:D9", "A3", "PivotTable")
pivotTable = pivotSheet.getPivotTables().get(pivotIdx)
pivotTable.addFieldToArea(PivotFieldType.ROW, 0)
pivotTable.addFieldToArea(PivotFieldType.PAGE, 1)
pivotTable.addFieldToArea(PivotFieldType.PAGE, 2)
pivotTable.addFieldToArea(PivotFieldType.DATA, 3)
pivotTable.setPageFieldOrder(PrintOrderType.OVER_THEN_DOWN)
pivotTable.setPageFieldWrapCount(2)
pivotTable.getPageFields().move(0, 1)
pivotTable.calculateData()
workbook.save("pageFieldLayout_move.xlsx")
jpype.shutdownJVM()
```

## **Related Articles**
- [ピボットテーブルにページフィールドを追加する](/cells/ja/python-java/add-page-field-in-pivot-table/) — ピボットテーブルへのページフィールドの追加方法を説明する親ページです。
- [ピボットテーブルの行フィールドと列フィールド](/cells/ja/python-java/row-and-column-fields/) — ここで示すページ軸の作業を補完する、行軸と列軸へのフィールドの割り当てについて説明します。
- [ピボットテーブルの値フィールドを管理する](/cells/ja/python-java/manage-value-fields/) — この記事で使用されている `SUM` 集計を含む、データ (値) 領域の設定方法を説明します。
- [ピボットテーブルの更新](/cells/ja/python-java/refresh-pivot-table/) — ページフィールドの並び替え後に必要な `refresh_data` と `calculate_data` について説明します。
- [ピボットテーブルにスタイルを適用する](/cells/ja/python-java/apply-style-to-pivot-table/) — ページフィールドの帯がレイアウトされた後、レンダリングされたピボットテーブルを書式設定する方法を示します。

{{< app/cells/assistant language="python" >}}