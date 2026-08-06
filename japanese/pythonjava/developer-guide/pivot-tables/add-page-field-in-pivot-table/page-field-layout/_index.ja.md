---
title: ピボットテーブルでページフィールドのレイアウトを変更する
linktitle: ピボットテーブルでページフィールドのレイアウトを変更する
description: Aspose.Cells for Python via Java を使用して、ピボットテーブルのページフィールド領域のレイアウト(表示順、改行数、ページフィールドの並び替えなど)を制御する方法を説明します。
keywords: Aspose.Cells for Python via Java, Python Java ライブラリ, スプレッドシート, ピボットテーブル, ページフィールド, ページフィールドの順序, ページフィールドの改行数, ページフィールドの移動
type: docs
weight: 191
url: /ja/python-java/change-page-field-layout/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---
{{% alert color="primary" %}}
本記事は **Add Page Field in Pivot Table** の続きです。ページフィールド領域(ピボットテーブルの上部にあるフィルターコントロールの帯)のレイアウト(表示順、改行数、フィールドの並び替え)を制御する方法を説明します。
{{% /alert %}}
## **はじめに**
Microsoft Excel のピボットテーブルには、テーブルの行/列/データ本体の上に位置する専用の **ページフィールド領域** があります。この領域はページフィールドごとに 1 つずつ配置されたドロップダウンフィルターコントロールの帯としてレンダリングされ、エンドユーザーがここをクリックして年や地域などの条件でピボットをスライスします。Aspose.Cells for Python via Java では、この領域を `pivot_table.page_fields` コレクションでモデル化し、帯の視覚的なレイアウトを制御する 3 つのプロパティを公開しています。
- `pivot_table.page_field_order`(`Aspose.Cells.PrintOrderType` の値)は、追加のページフィールドを既存のフィールドの *横* に配置するか、*下* に配置するかを決定します。
- `pivot_table.page_field_wrap_count` は、折り返し前に 1 行または 1 列に配置するページフィールドの数を設定します。
- `pivot_table.page_fields.move(curr_index, dest_index)` は、順序モードを変更せずにページフィールドを並べ替えます。
本記事では、共有データセットに対してこれら 3 つの操作をそれぞれ示す 3 つのコード例を順に解説し、それぞれのレイアウトを並べて比較できるようにします。
## **ソースデータ**
以下の 3 つの例では、すべて次の 8 行の売上データを `PivotData` という名前のワークシートに読み込みます。データには 2 つのページフィールド候補(`Year`、`Region`)、1 つの行フィールド候補(`Fruit`)、1 つのメジャー(`Amount`)が含まれており、ページフィールドの帯を検証する意味のあるものとなっています。
8 行すべてが各コード例で同じ順序で入力されるため、シナリオ間でソースデータが変動することはありません。異なるのはページフィールドのレイアウトプロパティのみです。
## **例 1:Over Then Down**
最初のシナリオでは、2 つのページフィールド(`Year`、`Region`)をピボットテーブルの上部で **1 行に横並び** で表示するように構成します。`Fruit` を行軸に割り当て、`Year` を最初に、`Region` を 2 番目にページ軸に配置し(`add_field_to_area` を呼び出す順序が開始インデックスを決定します)、`Amount`(Sum)をデータフィールドとして追加します。その後、`page_field_order` を `PrintOrderType.OVER_THEN_DOWN` に、`page_field_wrap_count` を `2` に設定します。`OVER_THEN_DOWN` と改行数 2 の組み合わせにより、2 つのページフィールドはピボットテーブルの上部で 1 行に横並びに配置されるため、帯は幅 2 の 1 行を占有します。
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

# ヘッダー（行0）
pivotDataCells.get(0, 0).putValue("Fruit")
pivotDataCells.get(0, 1).putValue("Year")
pivotDataCells.get(0, 2).putValue("Region")
pivotDataCells.get(0, 3).putValue("Amount")

# 行1: りんご、2022年、北、150
pivotDataCells.get(1, 0).putValue("Apple")
pivotDataCells.get(1, 1).putValue(2022)
pivotDataCells.get(1, 2).putValue("North")
pivotDataCells.get(1, 3).putValue(150)

# 行2: りんご、2023年、北、180
pivotDataCells.get(2, 0).putValue("Apple")
pivotDataCells.get(2, 1).putValue(2023)
pivotDataCells.get(2, 2).putValue("North")
pivotDataCells.get(2, 3).putValue(180)

# 行3: バナナ、2022年、南、120
pivotDataCells.get(3, 0).putValue("Banana")
pivotDataCells.get(3, 1).putValue(2022)
pivotDataCells.get(3, 2).putValue("South")
pivotDataCells.get(3, 3).putValue(120)

# 行4: バナナ、2023年、南、140
pivotDataCells.get(4, 0).putValue("Banana")
pivotDataCells.get(4, 1).putValue(2023)
pivotDataCells.get(4, 2).putValue("South")
pivotDataCells.get(4, 3).putValue(140)

# 行5: さくらんぼ、2022年、東、200
pivotDataCells.get(5, 0).putValue("Cherry")
pivotDataCells.get(5, 1).putValue(2022)
pivotDataCells.get(5, 2).putValue("East")
pivotDataCells.get(5, 3).putValue(200)

# 行6: さくらんぼ、2023年、東、220
pivotDataCells.get(6, 0).putValue("Cherry")
pivotDataCells.get(6, 1).putValue(2023)
pivotDataCells.get(6, 2).putValue("East")
pivotDataCells.get(6, 3).putValue(220)

# 行7: ぶどう、2022年、西、90
pivotDataCells.get(7, 0).putValue("Grape")
pivotDataCells.get(7, 1).putValue(2022)
pivotDataCells.get(7, 2).putValue("West")
pivotDataCells.get(7, 3).putValue(90)

# 行8: ぶどう、2023年、西、110
pivotDataCells.get(8, 0).putValue("Grape")
pivotDataCells.get(8, 1).putValue(2023)
pivotDataCells.get(8, 2).putValue("West")
pivotDataCells.get(8, 3).putValue(110)

# PivotTableReportシートを追加
pivotTableSheetIdx = worksheets.add("PivotTableReport")
pivotTableSheet = worksheets.get(pivotTableSheetIdx)
pivotTables = pivotTableSheet.getPivotTables()

# PivotData!A1:D9をデータソースとし、PivotTableReportのA1に配置するピボットテーブルを作成
pivotIndex = pivotTables.add("PivotData!A1:D9", "A1", "PivotTable1")
pivotTable = pivotTables.get(pivotIndex)

# フィールドを追加
pivotTable.addFieldToArea(PivotFieldType.ROW, 0)   # 果物
pivotTable.addFieldToArea(PivotFieldType.PAGE, 1)  # 年
pivotTable.addFieldToArea(PivotFieldType.PAGE, 2)  # 地域
pivotTable.addFieldToArea(PivotFieldType.DATA, 3)  # 数量
pivotTable.getDataFields().get(0).setFunction(ConsolidationFunction.SUM)

# ページフィールド領域のレイアウトを設定：ページフィールドを横方向に配置し、2つごとに折り返す
pivotTable.setPageFieldOrder(PrintOrderType.OVER_THEN_DOWN)
pivotTable.setPageFieldWrapCount(2)

# 更新と計算
pivotTable.calculateData()

# 保存
workbook.save(os.path.join(dataDir, "pageFieldLayout_overThenDown.xlsx"))

jpype.shutdownJVM()
```
## **例 2:Down Then Over**
この例では、例 1 とまったく同じく、`Fruit` を行軸に、`Year` と `Region` をページ軸に(`Year` を最初に)、`Amount`(Sum)をデータフィールドとして配置します。その後、`page_field_order` を `PrintOrderType.DOWN_THEN_OVER` に、`page_field_wrap_count` を `2` に設定します。`DOWN_THEN_OVER` と改行数 2 の組み合わせにより、2 つのページフィールドは縦に積み重ねられ、`Year` が上、`Region` が直下に配置され、ピボットテーブルの上部で 1 列を形成します。したがって、帯は例 1 とは対照的に、幅 1 で 2 行を占有します。
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
## **例 3:ページフィールドの移動**
3 番目のシナリオでは、同じデータセットとフィールド割り当てを維持し、中立的なレイアウト(`OVER_THEN_DOWN`、改行数 `2`)を設定してから、`page_fields.move` 操作を示します。`move(0, 1)` の呼び出しにより、インデックス 0(`Year`)のページフィールドが位置 1 に移動し、位置 1 にあったページフィールド(`Region`)が位置 0 にシフトします。この呼び出しの後、`Region` が最初のページフィールドとなり、`Year` が 2 番目となります。折り返しと順序モードは変更されないため、帯は引き続き横並びにレンダリングされます。2 つのドロップダウンの順序のみが入れ替わります。
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
## **関連記事**
- [Add Page Field in Pivot Table](/cells/ja/python-java/add-page-field-in-pivot-table/) — ピボットテーブルにページフィールドを追加する方法を紹介する親ページです。
- [Row and Column Fields in Pivot Table](/cells/ja/python-java/row-and-column-fields/) — ここで示したページ軸の作業を補完する、行軸と列軸へのフィールドの割り当てについて説明します。
- [Manage Value Fields in Pivot Table](/cells/ja/python-java/manage-value-fields/) — 本記事で使用している `SUM` 集計を含め、データ(値)領域の構成方法を説明します。
- [Refresh Pivot Table](/cells/ja/python-java/refresh-pivot-table/) — ページフィールドの並べ替え後に必要な `refresh_data` と `calculate_data` について説明します。
- [Apply Style to Pivot Table](/cells/ja/python-java/apply-style-to-pivot-table/) — ページフィールドの帯が配置された後にレンダリングされたピボットテーブルを書式設定する方法を示します。
{{< app/cells/assistant language="python" >}}