---
title: Aspose.Cells for Python via Java でピボットテーブルの行フィールドと列フィールドを追加する
linktitle: 行フィールドと列フィールド
description: Learn how to add base fields to the row and column regions of a pivot table and control pivot field subtotals using PivotField.setSubtotals in Aspose.Cells for Python via Java.
keywords: Aspose.Cells, Python via Java, pivot table, row field, column field, PivotField, setSubtotals, PivotFieldSubtotalType, subtotals
type: docs
weight: 220
url: /ja/python-java/pivot-table-add-row-and-column-fields/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **行領域または列領域へのフィールドの追加**

`PivotTable.addFieldToArea(PivotFieldType fieldType, String fieldName)` メソッドは、ソースデータから基本フィールドを4つのピボット領域のいずれかに移動します。`fieldType` 引数は、以下の `PivotFieldType` 値のいずれかを受け入れます。

- `ROW` — フィールドを左側に縦方向に配置
- `COLUMN` — フィールドを上部に横方向に配置
- `DATA` — 値を集約するフィールド
- `PAGE` — レポートフィルタとして使用されるフィールド

フィールドを追加した後、`PivotTable.getRowFields()` メソッドと `PivotTable.getColumnFields()` メソッドを使用してフィールドにアクセスできます。各メソッドは `PivotFieldCollection` を返します。`RowFields` のインデックス 0 にあるフィールドは最も外側の行フィールドであり、後続のインデックスはその内側にネストされたフィールドを表します。同じインデックスの規則が `ColumnFields` にも適用されます。

フィールドのネスト順序は重要です。最初に `Category` を行領域に追加し、その後 `Item` を追加すると、外側のグループ化が `Category`、内側のグループ化が `Item` となるピボットテーブルが作成されます。順序を逆にすると階層も逆になります。

## **ピボットフィールドの小計**

`PivotField.setSubtotals(PivotFieldSubtotalType subtotalType, boolean shown)` メソッドは、ピボットフィールドに表示される小計行を制御します。呼び出しごとに、単一の小計タイプを独立して切り替えられます。`shown = true` を渡すと小計が表示され、`shown = false` を渡すと非表示になります。各呼び出しは1つのタイプにのみ影響するため、異なる `subtotalType` 値を使用してメソッドを複数回呼び出すことで、小計のカスタムサブセットを構築できます。

`PivotFieldSubtotalType` 列挙型は、利用可能な小計の種類を定義します。

- `AUTOMATIC` — Aspose.Cells がデフォルトの選択を行います（通常、数値フィールドには `SUM`）
- `NONE` — すべての小計行を抑制
- `SUM`
- `COUNT`
- `AVERAGE`
- `MAX`
- `MIN`
- `PRODUCT`
- `STD_DEV`
- `STD_DEVP`
- `VAR`
- `VARP`

{{% alert color="primary" %}}
小計は、行領域（または列領域）に2つ以上のピボットフィールドがある場合にのみ表示されます。単一のフィールドはその間に意味のある小計を持たないため、その場合 `setSubtotals` の呼び出しは視覚的な効果を持ちません。したがって、この記事では各 `Category` グループの間の小計の境界が表示されるように、すべての例で2つの行フィールド（外側 `Category`、内側 `Item`）を配置しています。
{{% /alert %}}

## **シナリオ 1 — 自動（デフォルト）の小計**

`setSubtotals` をまったく呼び出さない場合、Aspose.Cells は数値フィールドに `AUTOMATIC` 設定を適用します。次の例では、外側の `Category` 行フィールドに対して `setSubtotals(PivotFieldSubtotalType.AUTOMATIC, true)` を呼び出すことで、この動作を明示的に確認しています。

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, PivotTable, PivotField, PivotFieldType, PivotFieldSubtotalType

workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
worksheet.setName("Data")

worksheet.getCells().get(0, 0).putValue("Category")
worksheet.getCells().get(0, 1).putValue("Item")
worksheet.getCells().get(0, 2).putValue("Year")
worksheet.getCells().get(0, 3).putValue("Amount")

worksheet.getCells().get(1, 0).putValue("Fruit")
worksheet.getCells().get(1, 1).putValue("Apple")
worksheet.getCells().get(1, 2).putValue(2020)
worksheet.getCells().get(1, 3).putValue(100)

worksheet.getCells().get(2, 0).putValue("Fruit")
worksheet.getCells().get(2, 1).putValue("Apple")
worksheet.getCells().get(2, 2).putValue(2021)
worksheet.getCells().get(2, 3).putValue(150)

worksheet.getCells().get(3, 0).putValue("Fruit")
worksheet.getCells().get(3, 1).putValue("Banana")
worksheet.getCells().get(3, 2).putValue(2020)
worksheet.getCells().get(3, 3).putValue(80)

worksheet.getCells().get(4, 0).putValue("Fruit")
worksheet.getCells().get(4, 1).putValue("Banana")
worksheet.getCells().get(4, 2).putValue(2021)
worksheet.getCells().get(4, 3).putValue(90)

worksheet.getCells().get(5, 0).putValue("Vegetable")
worksheet.getCells().get(5, 1).putValue("Carrot")
worksheet.getCells().get(5, 2).putValue(2020)
worksheet.getCells().get(5, 3).putValue(50)

worksheet.getCells().get(6, 0).putValue("Vegetable")
worksheet.getCells().get(6, 1).putValue("Carrot")
worksheet.getCells().get(6, 2).putValue(2021)
worksheet.getCells().get(6, 3).putValue(60)

worksheet.getCells().get(7, 0).putValue("Vegetable")
worksheet.getCells().get(7, 1).putValue("Daikon")
worksheet.getCells().get(7, 2).putValue(2020)
worksheet.getCells().get(7, 3).putValue(40)

worksheet.getCells().get(8, 0).putValue("Vegetable")
worksheet.getCells().get(8, 1).putValue("Daikon")
worksheet.getCells().get(8, 2).putValue(2021)
worksheet.getCells().get(8, 3).putValue(45)

pivotIndex = worksheet.getPivotTables().add("A1:D9", "F3", "PivotTable1")
pivotTable = worksheet.getPivotTables().get(pivotIndex)

pivotTable.addFieldToArea(PivotFieldType.ROW, "Category")
pivotTable.addFieldToArea(PivotFieldType.ROW, "Item")
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year")
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount")

categoryField = pivotTable.getRowFields().get(0)
categoryField.setSubtotals(PivotFieldSubtotalType.AUTOMATIC, True)

pivotTable.calculateData()

workbook.save("output_automatic.xlsx")

jpype.shutdownJVM()
```

## **シナリオ 2 — すべての小計を抑制（None）**

`setSubtotals(PivotFieldSubtotalType.NONE, true)` を呼び出すと、ピボットテーブルからすべての小計行が削除され、フィールド行と最下部の総計のみが残ります。これは、集計行のない生のグループ化データが必要な場合に便利です。

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType, PivotFieldSubtotalType

workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
worksheet.setName("Data")

headers = ["Category", "Item", "Year", "Amount"]
for j in range(len(headers)):
    worksheet.getCells().get(0, j).putValue(headers[j])

data = [
    ["Fruit",     "Apple",  2020, 100],
    ["Fruit",     "Apple",  2021, 150],
    ["Fruit",     "Banana", 2020, 80 ],
    ["Fruit",     "Banana", 2021, 90 ],
    ["Vegetable", "Carrot", 2020, 50 ],
    ["Vegetable", "Carrot", 2021, 60 ],
    ["Vegetable", "Daikon", 2020, 40 ],
    ["Vegetable", "Daikon", 2021, 45 ]
]

for i in range(len(data)):
    for j in range(len(data[0])):
        worksheet.getCells().get(i + 1, j).putValue(data[i][j])

pivotIndex = worksheet.getPivotTables().add("A1:D9", "F3", "PivotTable1")
pivotTable = worksheet.getPivotTables().get(pivotIndex)

pivotTable.addFieldToArea(PivotFieldType.ROW, "Category")
pivotTable.addFieldToArea(PivotFieldType.ROW, "Item")
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year")
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount")

categoryField = pivotTable.getRowFields().get(0)
categoryField.setSubtotals(PivotFieldSubtotalType.NONE, True)
pivotTable.calculateData()

workbook.save("output_none.xlsx")

jpype.shutdownJVM()
```

## **シナリオ 3 — カスタム小計サブセット（Sum + Average）**

単一の小計タイプに限定されません。各 `setSubtotals` 呼び出しは1つのタイプに対して独立して動作するため、メソッドを2回呼び出す（1回は `SUM`、もう1回は `AVERAGE`）ことで、各 `Category` グループに対して2つの小計行のカスタムサブセットが生成されます。

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotTableCollection, PivotTable, PivotFieldType, PivotField, PivotFieldSubtotalType

workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
worksheet.setName("Data")

worksheet.getCells().get("A1").putValue("Category")
worksheet.getCells().get("B1").putValue("Item")
worksheet.getCells().get("C1").putValue("Year")
worksheet.getCells().get("D1").putValue("Amount")

worksheet.getCells().get(1, 0).putValue("Fruit")
worksheet.getCells().get(1, 1).putValue("Apple")
worksheet.getCells().get(1, 2).putValue(2020)
worksheet.getCells().get(1, 3).putValue(100)

worksheet.getCells().get(2, 0).putValue("Fruit")
worksheet.getCells().get(2, 1).putValue("Apple")
worksheet.getCells().get(2, 2).putValue(2021)
worksheet.getCells().get(2, 3).putValue(150)

worksheet.getCells().get(3, 0).putValue("Fruit")
worksheet.getCells().get(3, 1).putValue("Banana")
worksheet.getCells().get(3, 2).putValue(2020)
worksheet.getCells().get(3, 3).putValue(80)

worksheet.getCells().get(4, 0).putValue("Fruit")
worksheet.getCells().get(4, 1).putValue("Banana")
worksheet.getCells().get(4, 2).putValue(2021)
worksheet.getCells().get(4, 3).putValue(90)

worksheet.getCells().get(5, 0).putValue("Vegetable")
worksheet.getCells().get(5, 1).putValue("Carrot")
worksheet.getCells().get(5, 2).putValue(2020)
worksheet.getCells().get(5, 3).putValue(50)

worksheet.getCells().get(6, 0).putValue("Vegetable")
worksheet.getCells().get(6, 1).putValue("Carrot")
worksheet.getCells().get(6, 2).putValue(2021)
worksheet.getCells().get(6, 3).putValue(60)

worksheet.getCells().get(7, 0).putValue("Vegetable")
worksheet.getCells().get(7, 1).putValue("Daikon")
worksheet.getCells().get(7, 2).putValue(2020)
worksheet.getCells().get(7, 3).putValue(40)

worksheet.getCells().get(8, 0).putValue("Vegetable")
worksheet.getCells().get(8, 1).putValue("Daikon")
worksheet.getCells().get(8, 2).putValue(2021)
worksheet.getCells().get(8, 3).putValue(45)

pivotTables = worksheet.getPivotTables()
pivotIndex = pivotTables.add("A1:D9", "F3", "PivotTable1")
pivotTable = pivotTables.get(pivotIndex)

pivotTable.addFieldToArea(PivotFieldType.Row, "Category")
pivotTable.addFieldToArea(PivotFieldType.Row, "Item")
pivotTable.addFieldToArea(PivotFieldType.Column, "Year")
pivotTable.addFieldToArea(PivotFieldType.Data, "Amount")

categoryField = pivotTable.getRowFields().get(0)
categoryField.setSubtotals(PivotFieldSubtotalType.Sum, True)
categoryField.setSubtotals(PivotFieldSubtotalType.Average, True)

pivotTable.calculateData()

workbook.save("output_custom.xlsx")

jpype.shutdownJVM()
```
## **まとめ**

上記の3つのシナリオは、同じデータセットとピボットテーブル構造を共有しています。シナリオ間の唯一の違いは、外側の `Category` 行フィールドに適用される `setSubtotals` 呼び出しです。2つのフィールドのルールを覚えておいてください。領域に単一のフィールドがある場合、その間に小計を行う対象がないため、`setSubtotals` が視覚的な効果を持つようにする必要があるときは、常に行領域または列領域に少なくとも2つのフィールドを配置してください。

## **関連記事**

- [ピボットテーブルのページフィールド](/cells/ja/python-java/add-page-field-in-pivot-table/)
- [Aspose.Cells for Python via Java でのピボットテーブルの更新](/cells/ja/python-java/refresh-pivot-table/)
- [ピボットテーブルへのスタイルの適用](/cells/ja/python-java/apply-style-to-pivot-table/)

{{< app/cells/assistant language="python" >}}
