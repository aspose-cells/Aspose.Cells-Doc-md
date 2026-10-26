---
title: 在 Aspose.Cells for Python via Java 中添加数据透视表的行字段和列字段
linktitle: 在 Aspose.Cells for Python via Java 中添加数据透视表的行字段和列字段
description: Learn how to add base fields to the row and column regions of a pivot table and control pivot field subtotals using PivotField.setSubtotals in Aspose.Cells for Python via Java.
keywords: Aspose.Cells, Python via Java, 数据透视表, 行字段, 列字段, PivotField, setSubtotals, PivotFieldSubtotalType, 小计
type: docs
weight: 220
url: /zh/python-java/pivot-table-add-row-and-column-fields/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Adding a Field to the Row or Column Region**
`PivotTable.addFieldToArea(PivotFieldType fieldType, String fieldName)` 方法将基础字段从源数据移动到四个数据透视区域之一。`fieldType` 参数接受以下 `PivotFieldType` 值之一。
- `ROW` — 垂直显示在左侧的字段
- `COLUMN` — 水平显示在顶部的字段
- `DATA` — 其值被聚合的字段
- `PAGE` — 用作报表筛选器的字段
字段的嵌套顺序很重要。先将 `Category` 添加到行区域,然后再添加 `Item`,会生成一个外层分组为 `Category`、内层分组为 `Item` 的数据透视表。反转顺序则会使层次结构反转。

## **Pivot Field Subtotals**
`PivotField.setSubtotals(PivotFieldSubtotalType subtotalType, boolean shown)` 方法控制哪些小计行显示在透视字段上。每次调用都会独立切换一种小计类型。传递 `shown = true` 会显示小计,而 `shown = false` 会隐藏小计。由于每次调用仅影响一种类型,因此使用不同的 `subtotalType` 值多次调用该方法可以构建自定义的小计子集。
`PivotFieldSubtotalType` 枚举定义了可用的小计种类。
- `AUTOMATIC` — Aspose.Cells 选择默认选项(通常对数值字段为 `SUM`)
- `NONE` — 抑制所有小计行
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
只有当行区域(或列区域)中包含两个或更多数据透视字段时,小计才会呈现。单个字段没有可供小计的有意义内容,因此在这种情况下 `setSubtotals` 调用不会有可见效果。因此,本文在每个示例中放置两个行字段(`Category` 在外层,`Item` 在内层),以便显示每个 `Category` 组之间的小计边界。
{{% /alert %}}

## **Scenario 1 — Automatic (Default) Subtotals**
如果完全不调用 `setSubtotals`,Aspose.Cells 会将 `AUTOMATIC` 选项应用于数值字段。以下示例通过在外层 `Category` 行字段上调用 `setSubtotals(PivotFieldSubtotalType.AUTOMATIC, true)` 来显式确认此行为。

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
pivotTable = worksheet.getPivotTables().add("A1:D9", 2, 5)
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
调用 `setSubtotals(PivotFieldSubtotalType.NONE, true)` 会从数据透视表中移除所有小计行,仅保留字段行和底部的总计行。当您希望获取原始分组数据而没有任何汇总行时,这非常有用。

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
pivotTable = worksheet.getPivotTables().add("A1:D9", 2, 5)
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
您不仅限于使用单一小计类型。每次 `setSubtotals` 调用独立作用于一种类型,因此两次调用该方法(一次使用 `SUM`,一次使用 `AVERAGE`)将为每个 `Category` 组生成包含两种小计行的自定义子集。

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
pivotTable = pivotTables.add("A1:D9", 2, 5)
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
这三种场景仅在 `setSubtotals` 调用上有所不同；其余部分——数据集、字段及其所分配的区域——完全相同，这使得各布局之间可直接进行比较。
- **字段放置。** `PivotTable.addFieldToArea(PivotFieldType.ROW, fieldName)` 会将源列移入某一区域。在同一区域内，调用的顺序即为显示顺序，因此首次调用生成最外层分组。子总计需要同一区域中存在两个或更多字段：若仅有一个字段，则组间无内容可供计算子总计。
- **场景 1——自动子总计。** 若不调用 `setSubtotals`，则由 Excel 自行决定采用其默认的子总计方式，该方式仅对数值字段生效；若显式调用 `setSubtotals` 并传入 `PivotFieldSubtotalType.AUTOMATIC`，则明确记录该默认选项，而非使其隐含存在。
- **场景 2——无子总计。** 对字段调用 `setSubtotals` 并传入 `PivotFieldSubtotalType.NONE`，会关闭默认子总计设置，此时数据透视表仍保留字段行和总计行，但不会插入 Excel 默认会在其中插入的子总计行。
- **场景 3——选择性子总计。** 每次调用仅切换一种子总计类型，且多次调用会累加而非相互覆盖；因此，先以 `PivotFieldSubtotalType.SUM` 调用一次、再以 `PivotFieldSubtotalType.AVERAGE` 调用一次后，二者将同时生效，数据透视表将呈现“求和”子总计、“平均值”子总计及总计行。

{{% alert color="primary" %}}
子总计设置与行区域并无绑定关系；对 `PivotTable.ColumnFields` 中获取的字段执行同样的 `setSubtotals` 调用，即可在列轴上生成相同的三种布局，因为该设置属于数据透视字段本身，而非其所在的轴。
{{% /alert %}}

## **Related Articles**
- [数据透视表中的页字段](/cells/zh/python-java/add-page-field-in-pivot-table/)
- [在 Aspose.Cells for Python via Java 中刷新数据透视表](/cells/zh/python-java/refresh-pivot-table/)
- [将样式应用于数据透视表](/cells/zh/python-java/apply-style-to-pivot-table/)

{{< app/cells/assistant language="python" >}}