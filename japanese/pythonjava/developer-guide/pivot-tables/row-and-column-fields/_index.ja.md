---
title: Aspose.Cells for Python via Java でピボットテーブルの行フィールドと列フィールドを追加する
linktitle: Aspose.Cells for Python via Java でピボットテーブルの行フィールドと列フィールドを追加する
description: Aspose.Cells for Python via Java で、ピボットテーブルの行領域および列領域にベースフィールドを追加する方法と、PivotField.setSubtotals を使用してピボットフィールドの小計を制御する方法を学びます。
keywords: Aspose.Cells, Python via Java, ピボットテーブル, 行フィールド, 列フィールド, PivotField, setSubtotals, PivotFieldSubtotalType, 小計
type: docs
weight: 220
url: /ja/python-java/pivot-table-add-row-and-column-fields/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Adding a Field to the Row or Column Region**
`PivotTable.addFieldToArea(PivotFieldType fieldType, String fieldName)` メソッドは、ベースフィールドをソースデータから4つのピボット領域のいずれかに移動します。`fieldType` 引数は次の `PivotFieldType` 値のいずれかを受け付けます。
- `ROW` — 左側に縦に配置されるフィールド
- `COLUMN` — 上部に水平に配置されるフィールド
- `DATA` — 値を集計するフィールド
- `PAGE` — レポートフィルターとして使用されるフィールド
フィールドのネスト順序は重要です。最初に `Category` を行領域に追加し、次に `Item` を追加すると、外側のグループ化が `Category`、内側のグループ化が `Item` となるピボットが作成されます。順序を逆にした場合は階層も逆になります。

## **Pivot Field Subtotals**
`PivotField.setSubtotals(PivotFieldSubtotalType subtotalType, boolean shown)` メソッドは、ピボットフィールドに表示される小計行を制御します。各呼び出しは1つの小計タイプを独立して切り替えます。`shown = true` を渡すと小計が表示され、`shown = false` を渡すと非表示になります。各呼び出しは1つのタイプのみに影響するため、異なる `subtotalType` 値でメソッドを複数回呼び出すことで、小計のカスタムサブセットを構築できます。
`PivotFieldSubtotalType` 列挙型は、利用可能な小計の種類を定義します。
- `AUTOMATIC` — Aspose.Cells がデフォルトの選択を行います（通常、数値フィールドには `SUM`）
- `NONE` — すべての小計行を抑制します
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
小計は、行領域（または列領域）に2つ以上のピボットフィールドがある場合にのみ表示されます。フィールドが1つだけの場合、小計を計算する意味のある対象が存在しないため、その状況では `setSubtotals` の呼び出しは目に見える効果を持ちません。そのため、この記事のすべての例では2つの行フィールド（外側が `Category`、内側が `Item`）を配置し、各 `Category` グループ間の小計の境界が見えるようにしています。
{{% /alert %}}

## **Scenario 1 — Automatic (Default) Subtotals**
`setSubtotals` をまったく呼び出さない場合、Aspose.Cells は数値フィールドに `AUTOMATIC` 選択を適用します。次の例では、外側の `Category` 行フィールドに対して `setSubtotals(PivotFieldSubtotalType.AUTOMATIC, true)` を呼び出すことで、この動作を明示的に確認しています。

```python
import jpype
import asposecells
jpype.startJVM()
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

## **Scenario 2 — Suppressing All Subtotals (None)**
`setSubtotals(PivotFieldSubtotalType.NONE, true)` を呼び出すと、ピボットからすべての小計行が削除され、フィールド行と最下部にある総計のみが残ります。これは、集計行のない生のグループ化データが必要な場合に便利です。

```python
import jpype
import asposecells
jpype.startJVM()
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

## **Scenario 3 — Custom Subtotal Subset (Sum + Average)**
単一の小計タイプに限定されません。各 `setSubtotals` 呼び出しは1つのタイプに対して独立して動作するため、`SUM` と `AVERAGE` でそれぞれ1回ずつ、合計2回メソッドを呼び出すことで、各 `Category` グループに対して2つの小計行からなるカスタムサブセットが生成されます。

```python
import jpype
import asposecells
jpype.startJVM()
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
pivotTable.addFieldToArea(PivotFieldType.ROW, "Category")
pivotTable.addFieldToArea(PivotFieldType.ROW, "Item")
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year")
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount")
categoryField = pivotTable.getRowFields().get(0)
categoryField.setSubtotals(PivotFieldSubtotalType.SUM, True)
categoryField.setSubtotals(PivotFieldSubtotalType.AVERAGE, True)
pivotTable.calculateData()
workbook.save("output_custom.xlsx")
jpype.shutdownJVM()
```

## **Recap**

この3つのシナリオは、`setSubtotals`メソッドの呼び出しの有無という1点のみが異なります。データセット、フィールド、およびそれらが割り当てられる領域はすべて同じであり、これによりレイアウトを直接比較できるようになります。
- **フィールドの配置。** `PivotTable.addFieldToArea(PivotFieldType.ROW, fieldName)` はソース列を領域内に移動します。1つの領域内では、メソッド呼び出しの順序が表示順序となります。そのため、最初の呼び出しが最も外側のグループになります。小計には、同じ領域内に2つ以上のフィールドが必要です。フィールドが1つの場合、グループ間に小計を置く対象が存在しません。
- **シナリオ1 — 自動小計。** `setSubtotals` を呼び出さない場合、選択はExcelに委ねられ、Excelは数値フィールドに対して独自の既定の小計を適用します。`PivotFieldSubtotalType.AUTOMATIC` を指定して`setSubtotals` を呼び出すと、この選択を明示的に記録します。
- **シナリオ2 — 小計なし。** `PivotFieldSubtotalType.NONE` を指定して`setSubtotals` を呼び出すと、既定の小計が無効になります。この場合、ピボットテーブルはフィールド行と合計行は維持しますが、Excelが otherwise に挿入していた小計行は除外されます。
- **シナリオ3 — 選択されたサブセット。** 各呼び出しは正確に1つの小計タイプを切り替え、呼び出しは互いにリセットするのではなく蓄積されます。そのため、`PivotFieldSubtotalType.SUM` を1回、`PivotFieldSubtotalType.AVERAGE` を1回呼び出すと、両方とも有効のままとなり、ピボットテーブルは「合計」小計、「平均」小計、および合計行をすべて表示します。

{{% alert color="primary" %}}
小計に関する設定は、行領域に固有のものではありません。`PivotTable.ColumnFields` から取得したフィールドに対して同じ`setSubtotals` の呼び出しを行うと、列軸上でも同じ3つのレイアウトが生成されます。なぜなら、この設定は軸ではなくピボットフィールド自体に属しているからです。
{{% /alert %}}
## **Related Articles**
- [ピボットテーブルのページフィールド](/cells/ja/python-java/add-page-field-in-pivot-table/)
- [Aspose.Cells for Python via Java でピボットテーブルを更新する](/cells/ja/python-java/refresh-pivot-table/)
- [ピボットテーブルにスタイルを適用する](/cells/ja/python-java/apply-style-to-pivot-table/)

{{< app/cells/assistant language="python" >}}