---
title: 数据透视字段项目的离散分组
linktitle: 离散分组
description: 了解如何通过 Java 使用 Aspose.Cells for Python，并使用 DiscreteGroupItem 和 PivotFieldGroupOptions.getDiscreteGroupItems 将数据透视字段项目分组为水果和蔬菜等自定义命名组。
keywords: Aspose.Cells, 数据透视表, 离散分组, DiscreteGroupItem, PivotFieldGroupOptions, 对数据透视字段项目进行分组, 自定义组, PivotField.group, 通过 Java 使用 Python, Excel 数据透视表
type: docs
weight: 90
url: /zh/python-java/discrete-group-pivot-fields/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **可能的使用场景**
- 自动分组根据数据类型归类项目，例如将日期归为月份和季度，或将数字归为数值区间。离散分组解决的是相反的问题，即将特定的、互不相关的项目归入自定义命名组，例如将产品归为水果和蔬菜、将商店归为区域或将账户归为分区。Aspose.Cells 通过 `DiscreteGroupItem` 类和 `PivotFieldGroupOptions.getDiscreteGroupItems()` 方法提供离散分组功能。
- 一个 `DiscreteGroupItem` 由组名和归属于该组的项目组成。可以通过两种方式识别这些项目：按名称（`DiscreteGroupItem("fruit", ["grape", "cherry"])`）或按其在源数据中的从零开始的位置（`DiscreteGroupItem("fruit", [0, 3])`）。两种形式产生相同的结果。
- 若要将离散分组应用于数据透视表行区域或列区域中的字段，请将相应选项传递给 `PivotField.group(PivotFieldGroupOptions)`。

## **按项目名称对数据透视字段项目进行分组**
以下示例构建了一个小型销售列表（`product`、`date` 和 `amount`），并基于该列表创建数据透视表，将 `product` 放在行区域、`date` 放在列区域、`amount` 放在值区域，然后按项目名称定义两个自定义组：水果（葡萄、樱桃）和蔬菜（胡萝卜、马铃薯）。结果呈现两级行布局：组名位于外层，原始项目嵌套在其下方，因此可分别按自定义组和单个项目查看趋势。

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import (
    Workbook,
    Worksheet,
    Cells,
    Range,
    SaveFormat,
    DiscreteGroupItem,
    PivotFieldGroupOptions,
    PivotFieldType,
    PivotTableStyleType,
)
GregorianCalendar = jpype.JPackage("java.util").GregorianCalendar
def create_date(year, month, day):
    calendar = GregorianCalendar(year, month - 1, day)
    return calendar.getTime()
wb = Workbook()
sheet = wb.getWorksheets().get(0)
cells = sheet.getCells()
cells.get(0, 0).putValue("product")
cells.get(1, 0).putValue("grape")
cells.get(2, 0).putValue("carrot")
cells.get(3, 0).putValue("potato")
cells.get(4, 0).putValue("cherry")
date_style = wb.createStyle()
date_style.setCustom("m/d/yyyy")
cells.get(0, 1).putValue("date")
cells.get(1, 1).putValue(create_date(2021, 2, 5))
cells.get(2, 1).putValue(create_date(2022, 3, 8))
cells.get(3, 1).putValue(create_date(2023, 4, 10))
cells.get(4, 1).putValue(create_date(2024, 5, 16))
for r in range(1, 5):
    cells.get(r, 1).setStyle(date_style)
cells.get(0, 2).putValue("amount")
cells.get(1, 2).putValue(50.0)
cells.get(2, 2).putValue(60.0)
cells.get(3, 2).putValue(70.0)
cells.get(4, 2).putValue(80.0)
# Add a pivot table with the destination cell A12 (row 11, column 0)
pivot_table = sheet.getPivotTables().add("=Sheet1!A1:C5", 11, 0)
pivot_table.addFieldToArea(PivotFieldType.ROW, "product")
pivot_table.addFieldToArea(PivotFieldType.COLUMN, "date")
pivot_table.addFieldToArea(PivotFieldType.DATA, "amount")
pivot_table.setPivotTableStyleType(
    PivotTableStyleType.PIVOT_TABLE_STYLE_MEDIUM_10
)
# Group specific items into custom groups by item names
fruit = DiscreteGroupItem("fruit", ["grape", "cherry"])
vegetable = DiscreteGroupItem("vegetable", ["carrot", "potato"])
group_options = PivotFieldGroupOptions()
group_options.setDiscreteGroupItems([fruit, vegetable])
pivot_table.calculateData()
pivot_table.getRowFields().get(0).group(group_options)
wb.save("outputDiscreteGroupPivotField.xlsx")
jpype.shutdownJVM()
```

执行 `calculateData()` 后，数据透视表的行区域显示水果（葡萄 50、樱桃 80）和蔬菜（胡萝卜 60、马铃薯 70），总计为 260；列标签保留四个日期（2/5/2021、3/8/2022、4/10/2023、5/16/2024）。

## **按项目索引对数据透视字段项目进行分组**
当项目名称较长或已本地化时，可以使用 `DiscreteGroupItem` 的第二个构造函数按索引识别项目。索引表示项目在源数据中按出现顺序排列的、从零开始的位置，而非按字母顺序排列的位置。在上述示例数据中，葡萄对应项目 0，胡萝卜对应项目 1，马铃薯对应项目 2，樱桃对应项目 3，因此水果组对应 `{ 0, 3 }`，蔬菜组对应 `{ 1, 2 }`。结果与按名称分组的示例完全相同。

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import (
    Workbook,
    PivotFieldType,
    PivotTableStyleType,
)
Date = jpype.JClass("java.util.Date")
DiscreteGroupItem = jpype.JClass("com.aspose.cells.DiscreteGroupItem")
PivotFieldGroupOptions = jpype.JClass("com.aspose.cells.PivotFieldGroupOptions")
wb = Workbook()
sheet = wb.getWorksheets().get(0)
cells = sheet.getCells()
cells.get(0, 0).putValue("product")
cells.get(1, 0).putValue("grape")
cells.get(2, 0).putValue("carrot")
cells.get(3, 0).putValue("potato")
cells.get(4, 0).putValue("cherry")
date_style = wb.createStyle()
date_style.setCustom("m/d/yyyy")
cells.get(0, 1).putValue("date")
cells.get(1, 1).putValue(Date(2021 - 1900, 2 - 1, 5))
cells.get(2, 1).putValue(Date(2022 - 1900, 3 - 1, 8))
cells.get(3, 1).putValue(Date(2023 - 1900, 4 - 1, 10))
cells.get(4, 1).putValue(Date(2024 - 1900, 5 - 1, 16))
for r in range(1, 5):
    cells.get(r, 1).setStyle(date_style)
cells.get(0, 2).putValue("amount")
cells.get(1, 2).putValue(50.0)
cells.get(2, 2).putValue(60.0)
cells.get(3, 2).putValue(70.0)
cells.get(4, 2).putValue(80.0)
pivot_table = sheet.getPivotTables().add("=Sheet1!A1:C5", 11, 0)
pivot_table.addFieldToArea(PivotFieldType.ROW, "product")
pivot_table.addFieldToArea(PivotFieldType.COLUMN, "date")
pivot_table.addFieldToArea(PivotFieldType.DATA, "amount")
pivot_table.setPivotTableStyleType(
    PivotTableStyleType.PIVOT_TABLE_STYLE_MEDIUM_10
)
pivot_table.calculateData()
fruit = DiscreteGroupItem("fruit", [0, 3])
vegetable = DiscreteGroupItem("vegetable", [1, 2])
group_options = PivotFieldGroupOptions()
group_options.setDiscreteGroupItems([fruit, vegetable])
pivot_table.getRowFields().get(0).group(group_options)
pivot_table.calculateData()
wb.save("outputDiscreteGroupPivotFieldByIndex.xlsx")
jpype.shutdownJVM()
```

## **注意**

{{% alert color="primary" %}}
- 未分配给任何自定义组的项目不会丢失。它们会保留在数据透视表中，与自定义组处于同一层级，每个项目均作为独立的单项目条目保留。在上述示例中，仅定义水果组时，胡萝卜和马铃薯仍会作为独立条目保留在行区域中，与水果组并列。
- `PivotFieldGroupOptions.getNewPivotField()` 和 `setNewPivotField()` 方法控制离散分组的布局。`getNewPivotField()` 默认为 true，它会将分组字段作为新的外层字段添加到原始字段旁边，从而生成上述两级布局（`getRowFields()` 增至 2）。使用 `setNewPivotField(false)` 可改为使用分组字段替换原始字段；此时行区域仅显示一个层级，其中只包含组名及其汇总值，即水果 130（50 + 80）和蔬菜 130（60 + 70）。
- 在同一个 `getDiscreteGroupItems()` 集合中，可以混合使用 `DiscreteGroupItem` 基于名称和基于索引的构造函数。
{{% /alert %}}

## **相关文章**
- [在数据透视表中对数据透视字段进行分组](/cells/zh/python-java/group-pivot-fields-in-the-pivot-table/)
- [在数据透视表中添加行字段和列字段](/cells/zh/python-java/pivot-table-add-row-and-column-fields/)
- [按标签或值筛选数据透视表](/cells/zh/python-java/filter-by-label-or-value-of-pivot-table/)
- [将样式应用到数据透视表](/cells/zh/python-java/apply-style-to-pivot-table/)
- [刷新数据透视表](/cells/zh/python-java/refresh-pivot-table/)

{{< app/cells/assistant language="python" >}}