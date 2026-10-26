---
title: Aspose.Cells for Python via Java を使用してピボットテーブルにフィルターフィールドを追加
linktitle: Aspose.Cells for Python via Java を使用してピボットテーブルにフィルターフィールドを追加
description: Aspose.Cells for Python via Java を使用して、ピボットテーブルにフィルターフィールドを追加して設定する方法を学びます。フィルターフィールドの追加、単一選択フィルター、および複数選択フィルターを扱います。
keywords: Aspose.Cells, Python, Java, ピボットテーブル, フィルターフィールド, PivotFieldType.PAGE, PageFields, IsMultipleItemSelectionAllowed, CurrentPageItem, PivotItem, IsHidden, フィルター
type: docs
weight: 250
url: /ja/python-java/add-page-field-in-pivot-table/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells は、ピボットテーブルのフィルターフィールドに関するライフサイクル全体を備えています。便利な高位レベル API または下位レベルの `page_fields` コレクションを通じてフィルターフィールドを追加できるほか、単一選択モードでフィルターを操作したり、フィルターをクリアしてすべてのフィルター項目を表示したり、フィールドを複数選択に切り替えて Excel のチェックボックス UI で複数のフィルター項目を一度に選択したりできます。
{{% /alert %}}

## **Introduction**
フィルターフィールドは、ピボットテーブル本体に表示するソースデータの*どの部分集合*かを制御するピボットフィールドです。Excel では、レンダリングされたピボットテーブルの先頭にあるドロップダウンとしてエンドユーザーに表示されます。利用者が利用可能なフィルター項目のいずれかを選択すると、その項目に属するレコードのみが要約されるようにピボットテーブル本体が再構築されます。ピボットフィールドが `PivotFieldType.ROW`、`PivotFieldType.COLUMN`、または `PivotFieldType.DATA` としてではなく、`PivotFieldType.PAGE` として登録されると、フィルターフィールドになります。

## **Adding a Filter Field**

### Adding a Filter Field with add_field_to_area
次の例では、小さな Fruit / Year / Amount データセットを作成し、E3 セルにピボットテーブルを配置します。`Fruit` を行領域、`Amount` をデータ領域、`Year` をフィルター領域に配置し、ピボットテーブルを更新してワークブックを保存します。

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, PivotFieldType
# Create a new workbook
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
worksheet.setName("Data")
# Set up the header row
worksheet.getCells().get("A1").putValue("Fruit")
worksheet.getCells().get("B1").putValue("Year")
worksheet.getCells().get("C1").putValue("Amount")
# Populate 9 rows of sample data: Fruit, Year, Amount
data = [
    ["apple", 2020, 100],
    ["banana", 2021, 200],
    ["apple", 2021, 150],
    ["grape", 2020, 120],
    ["orange", 2022, 180],
    ["banana", 2020, 90],
    ["grape", 2021, 130],
    ["apple", 2022, 170],
    ["orange", 2021, 110]
]
for i in range(len(data)):
    worksheet.getCells().get(i + 1, 0).putValue(data[i][0])
    worksheet.getCells().get(i + 1, 1).putValue(data[i][1])
    worksheet.getCells().get(i + 1, 2).putValue(data[i][2])
# Add a pivot table anchored at cell E3
pivotTable = worksheet.getPivotTables().add("A1:C10", 2, 4)
# Add fields to their areas: Fruit as Row, Amount as Data, Year as Page field
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount")
pivotTable.addFieldToArea(PivotFieldType.PAGE, "Year")
# Refresh and calculate the pivot table data
pivotTable.calculateData()
# Save the workbook
workbook.save("pageFieldSample.xlsx")
jpype.shutdownJVM()
```

### Adding a Filter Field with page_fields.add
すでに `PivotField` インスタンスを操作している場合は、そのインスタンスを `PivotTable.page_fields.add` に直接渡すことができます。ピボットテーブルとフィルターフィールドの構成は前のシナリオとまったく同じですが、最後のフィルター領域への登録のみ、下位レベルの API 呼び出しに置き換わります。

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotTable, PivotField, PivotFieldType
# — The pivot table and page field are constructed exactly as in
#   Scenario 1a (Fruit/Year/Amount data, pivot at E3, Fruit→Row,
#   Amount→Data). Below we obtain the Year PivotField from the
#   BaseFields collection and pass it to PageFields.Add — the
#   low-level alternative to AddFieldToArea. The result is
#   functionally identical to Scenario 1a.
workbook = Workbook()
sheet = workbook.getWorksheets().get(0)
# Headers
sheet.getCells().get("A1").putValue("Fruit")
sheet.getCells().get("B1").putValue("Year")
sheet.getCells().get("C1").putValue("Amount")
# Sample data (9 rows)
sheet.getCells().get("A2").putValue("apple");    sheet.getCells().get("B2").putValue("2020"); sheet.getCells().get("C2").putValue(100)
sheet.getCells().get("A3").putValue("apple");    sheet.getCells().get("B3").putValue("2021"); sheet.getCells().get("C3").putValue(150)
sheet.getCells().get("A4").putValue("apple");    sheet.getCells().get("B4").putValue("2022"); sheet.getCells().get("C4").putValue(200)
sheet.getCells().get("A5").putValue("grape");    sheet.getCells().get("B5").putValue("2020"); sheet.getCells().get("C5").putValue(300)
sheet.getCells().get("A6").putValue("grape");    sheet.getCells().get("B6").putValue("2021"); sheet.getCells().get("C6").putValue(400)
sheet.getCells().get("A7").putValue("grape");    sheet.getCells().get("B7").putValue("2022"); sheet.getCells().get("C7").putValue(500)
sheet.getCells().get("A8").putValue("blueberry"); sheet.getCells().get("B8").putValue("2020"); sheet.getCells().get("C8").putValue(250)
sheet.getCells().get("A9").putValue("blueberry"); sheet.getCells().get("B9").putValue("2021"); sheet.getCells().get("C9").putValue(350)
sheet.getCells().get("A10").putValue("blueberry");sheet.getCells().get("B10").putValue("2022"); sheet.getCells().get("C10").putValue(450)
# Add pivot table at E3 covering A1:C10
pivotTable = sheet.getPivotTables().add("A1:C10", 2, 4)
# Fruit -> Row, Amount -> Data (Year will go to Page below)
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount")
# Low-level approach: grab the existing Year PivotField from BaseFields
# and register it in the Page area via PageFields.Add(PivotField).
yearField = pivotTable.getBaseFields().get("Year")
pivotTable.getPageFields().add(yearField)
# Refresh so the new page field is reflected in the saved workbook
pivotTable.calculateData()
workbook.save("output.xlsx")
jpype.shutdownJVM()
```

## **Single-Select Filtering (Showing One Filter Item)**
デフォルトの単一選択動作では、フィルターフィールドは 1 つのドロップダウンとして描画され、`PivotField.current_page_item` の整数値によって、どのフィルター項目でピボットテーブル本体を構成かが決まります。特定のインデックスを代入すると、その項目だけを選択します。特別な番兵値 `0x7FFD`（10 進数では 32765）を代入すると、フィルターがクリアされ、すべてのフィルター項目が同時に要約されます。単一選択はデフォルトの動作であるため、明示的に有効にする必要はありません。

### Showing All Items
`current_page_item` を特殊な値 `0x7FFD` に設定すると、フィルターをクリアした場合と等しくなります。ピボットテーブル本体は、フィルターが適用されていない場合と同様に、すべてのフィルター項目を要約します。

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType
# Create a new workbook
workbook = Workbook()
sheet = workbook.getWorksheets().get(0)
# Populate Fruit/Year/Amount data
sheet.getCells().get("A1").putValue("Fruit")
sheet.getCells().get("B1").putValue("Year")
sheet.getCells().get("C1").putValue("Amount")
data = [
    ["Apple", 2022, 100],
    ["Apple", 2023, 150],
    ["Banana", 2022, 80],
    ["Banana", 2023, 120],
    ["Cherry", 2022, 200],
    ["Cherry", 2023, 250]
]
for r in range(len(data)):
    for c in range(len(data[r])):
        sheet.getCells().get(r + 1, c).putValue(data[r][c])
# Create pivot table at E3
pivotTables = sheet.getPivotTables()
pivotTable = pivotTables.add("=A1:C7", 2, 4)
# Configure pivot fields: Fruit→Row, Amount→Data, Year→Page
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount")
pivotTable.addFieldToArea(PivotFieldType.PAGE, "Year")
pivotTable.calculateData()
# Clear the page filter so every item in the page field is visible.
# 0x7FFD (decimal 32765) is the special sentinel value that means "all items" —
# equivalent to selecting "(All)" in Excel's page-field dropdown.
pivotTable.getPageFields().get(0).setCurrentPageItem(0x7FFD)
workbook.save("output.xlsx")
jpype.shutdownJVM()
```

### Showing One Specific Item
`current_page_item` を実際のインデックスに設定すると、そのフィルター項目だけを選択します。このインデックスは、フィルターフィールドの項目を並べ替えたリスト内での項目の位置です。したがって、例えば `1` は、並べ替え後の 2 番目の項目を選択します。

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType
# Create workbook
workbook = Workbook()
sheet = workbook.getWorksheets().get(0)
cells = sheet.getCells()
# Add sample data (Fruit/Year/Amount)
cells.get("A1").putValue("Fruit")
cells.get("B1").putValue("Year")
cells.get("C1").putValue("Amount")
cells.get("A2").putValue("Apple")
cells.get("B2").putValue("2020")
cells.get("C2").putValue("100")
cells.get("A3").putValue("Apple")
cells.get("B3").putValue("2021")
cells.get("C3").putValue("150")
cells.get("A4").putValue("Banana")
cells.get("B4").putValue("2020")
cells.get("C4").putValue("200")
cells.get("A5").putValue("Banana")
cells.get("B5").putValue("2021")
cells.get("C5").putValue("250")
# Add pivot table at E3
pivotTables = sheet.getPivotTables()
pivotTable = pivotTables.add("A1:C5", 2, 4)
# Add fields: Fruit→Row, Amount→Data, Year→Page
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount")
pivotTable.addFieldToArea(PivotFieldType.PAGE, "Year")
# Page-field-specific operations
pivotTable.getPageFields().get(0).setCurrentPageItem(1) # 1 = second item in sorted order (e.g. "2021")
# Refresh and calculate pivot table
pivotTable.calculateData()
workbook.save("output.xlsx")
jpype.shutdownJVM()
```

## **Multi-Select Filtering**
複数選択フィルターでは、フィルターのドロップダウンがチェックボックスのリストになり、エンドユーザーが複数のフィルター項目を同時に選択できます。Aspose.Cells には、連携して動作する 2 つのプロパティがあります。複数選択 UI を有効にするには、まず `PivotField.is_multiple_item_selection_allowed` を `True` に設定する必要があります。有効化後、`PivotItem.is_hidden` によって、チェックボックスのリストに表示する項目を制御できます。これにより、すべての項目を表示するか、特定の項目だけを許可リストに含めるかを選択できます。

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType
import os
import re
# — The pivot table and page field are constructed exactly as in
#   Scenario 1a (Fruit/Year/Amount data, pivot at E3, Fruit→Row,
#   Amount→Data, Year→Page via AddFieldToArea).
#   Below we apply multi-select filtering on the page field.
workbook = Workbook()
sheet = workbook.getWorksheets().get(0)
cells = sheet.getCells()
# Sample data: Fruit | Year | Amount
cells.get(0, 0).putValue("Fruit")
cells.get(0, 1).putValue("Year")
cells.get(0, 2).putValue("Amount")
data = [
    ["apple",  "2019", "100"],
    ["apple",  "2020", "150"],
    ["apple",  "2021", "200"],
    ["banana", "2019", "110"],
    ["banana", "2020", "160"],
    ["banana", "2021", "210"],
    ["grape",  "2019", "120"],
    ["grape",  "2020", "170"],
    ["grape",  "2021", "220"]
]
for i in range(len(data)):
    cells.get(i + 1, 0).putValue(data[i][0])
    cells.get(i + 1, 1).putValue(int(data[i][1]))
    cells.get(i + 1, 2).putValue(int(data[i][2]))
pivotSheet = workbook.getWorksheets().add("Pivot")
pivots = pivotSheet.getPivotTables()
pivotTable = pivots.add("A1:C10", 2, 4)
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount")
pivotTable.addFieldToArea(PivotFieldType.PAGE, "Year")
# — Enable multi-select on the page field
pivotTable.getPageFields().get(0).setMultipleItemSelectionAllowed(True)
# Part A — select ALL items (make every item visible)
pivotItems = pivotTable.getPageFields().get(0).getPivotItems()
for i in range(pivotItems.getCount()):
    pivotItems.get(i).setHidden(False)
# Part B — select only specific items by source value
for i in range(pivotItems.getCount()):
    value = pivotItems.get(i).getStringValue()
    if value == "2020" or value == "grape" or value == "blueberry":
        pivotItems.get(i).setHidden(False)
    else:
        pivotItems.get(i).setHidden(True)
pivotTable.calculateData()
workbook.save("output.xlsx")
jpype.shutdownJVM()
```

> **注記:** `PivotItem.is_hidden` を使用して複数選択フィルターを構成する場合、**少なくとも 1 つの `PivotItem` を表示したままにする必要があります**（`is_hidden == False`）。すべての項目を非表示にした場合、Excel はファイルの開画時にクラッシュするか、空のピボットテーブルを描画します。複数選択の許可リストにソースデータの項目が少なくとも 1 つ含まれていることを必ず確認してください。

## **Which API and Which Mode Should I Use?**
以下の表に、各 API およびモードを使用する場合をまとめています。すべてのシナリオを詳しく読まずに、適切な組み合わせを選択できます。
| シナリオ / ユースケース | 推奨 API | 使用するプロパティ | 注記 |
|---|---|---|---|
| ソース列名によってフィルターフィールドを追加する（最も一般的） | `PivotTable.add_field_to_area(PivotFieldType.PAGE, "fieldName")` | 該当なし | 高位レベルの API により 1 行で追加できます。`PivotField` 参照が必要でない限り、これを使用します。 |
| `PivotField` オブジェクトが既に取得済みの場合にフィルターフィールドを追加する | `PivotTable.page_fields.add(PivotField)` | 該当なし | フィールド オブジェクトを別の場所から取得した場合、または再利用が必要な場合に使用します。 |
| 1 つのフィルター項目に絞り込む（デフォルト モード） | `PivotField.current_page_item` | 特定のインデックスに設定 | 例えば、`1` は並べ替え後のリストで 2 番目の項目を表示します。 |
| すべての項目を表示する / フィルターをクリアする | `PivotField.current_page_item` | `0x7FFD` に設定 | 特殊な値 `0x7FFD`（10 進数では 32765）は、「すべての項目」を表す番兵値です。 |
| Excel で複数選択 UI を有効にする | `PivotField.is_multiple_item_selection_allowed` | `True` に設定 | `is_hidden` による設定が有効になる前に必要です。 |
| 複数選択リスト内の個別の項目を非表示にする / 表示する | `PivotItem.is_hidden` | 項目ごとに設定 | 少なくとも 1 つの項目を表示したままにする必要があります（`is_hidden == False`）。 |

{{% alert color="primary" %}}
複数選択フィルターを構成するときは、必ず表示状態の制約を牢记してください。複数選択フィルターフィールド内のすべての `PivotItem` を非表示にした場合、Excel は開画時にクラッシュするか、空のピボットテーブルを描画します。ソースデータに基づいて許可リストを構成し、少なくとも 1 つの項目を表示したままにしてください。これにより、保存したワークブックをすべての環境で確実に開けます。
{{% /alert %}}

{{< app/cells/assistant language="python" >}}