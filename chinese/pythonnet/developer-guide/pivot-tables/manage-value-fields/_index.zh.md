---
title: 在 Aspose.Cells for Python via .NET 中管理数据透视表值字段
linktitle: 值字段
description: 学习如何向数据透视表的值区域添加基础字段，使用 PivotField.function 更改汇总函数，以及将值字段绘制到行或列轴，适用于 Aspose.Cells for Python via .NET。
keywords: Aspose.Cells, Python via .NET, 数据透视表, 值字段, PivotField, PivotField.function, 数据字段, PivotTable.values_field, 求和, 平均值
type: docs
weight: 230
url: /zh/python-net/manage-value-fields/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## 将字段添加到数据区域
将基础字段添加到数据（值）区域是定义数据透视表如何汇总源数据的第一步。Aspose.Cells 提供 `PivotTable.AddFieldToArea(PivotFieldType, string)` 重载，接受常量 `PivotFieldType.DATA` 和源列名称。字段一旦添加到数据区域，API 会通过 `PivotTable.DataFields` 集合公开该字段，顺序与添加时相同。默认情况下，数值类型的源列使用 `Sum` 进行汇总，而非数值列默认使用 `Count`。

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.name = "Data"
headers = ["Category", "Item", "Year", "Amount"]
for j, h in enumerate(headers):
    worksheet.cells.get(0, j).put_value(h)
data = [
    ["Fruit",     "Apple",  2020, 100],
    ["Fruit",     "Apple",  2021, 150],
    ["Fruit",     "Banana", 2020,  80],
    ["Fruit",     "Banana", 2021,  90],
    ["Vegetable", "Carrot", 2020,  50],
    ["Vegetable", "Carrot", 2021,  60],
    ["Vegetable", "Daikon", 2020,  40],
    ["Vegetable", "Daikon", 2021,  45],
]
for i, row in enumerate(data):
    for j, val in enumerate(row):
        worksheet.cells.get(i + 1, j).put_value(val)
pivot_table = worksheet.pivot_tables.add("A1:D9", 2, 5)
pivot_table.add_field_to_area(PivotFieldType.ROW, "Category")
pivot_table.add_field_to_area(PivotFieldType.ROW, "Item")
pivot_table.add_field_to_area(PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")
pivot_table.calculate_data()
workbook.save("output_drag.xlsx")
```

## 更改汇总函数
当字段位于数据区域后，Aspose.Cells 通过 `PivotTable.DataFields` 上的 `PivotField` 对象公开它。每个 `PivotField` 都具有可写的 `Function` 属性，类型为 `ConsolidationFunction`，用于控制对该字段底层数值的聚合方式。`ConsolidationFunction` 是一个枚举，成员包括 `Sum`、`Count`、`Average`、`Max`、`Min`、`Product`、`StdDev`、`StdDevp`、`Var` 和 `Varp`——前六个覆盖了大多数实际使用场景，后四个是用于方差分析的统计聚合。

{{% alert color="primary" %}}
更改 `Function` 只会影响聚合方式；源列以及数据透视表的行/列结构不会被修改。要为已有的数据字段切换聚合方式，请设置 `pivotTable.DataFields[i].Function = ConsolidationFunction.<X>;`，然后调用 `pivotTable.calculate_data()` 重新呈现数据透视表。
{{% /alert %}}

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType
from aspose.cells import ConsolidationFunction
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.name = "Data"
headers = ["Category", "Item", "Year", "Amount"]
for j, h in enumerate(headers):
    worksheet.cells.get(0, j).put_value(h)
data = [
    ["Fruit",     "Apple",  2020, 100],
    ["Fruit",     "Apple",  2021, 150],
    ["Fruit",     "Banana", 2020,  80],
    ["Fruit",     "Banana", 2021,  90],
    ["Vegetable", "Carrot", 2020,  50],
    ["Vegetable", "Carrot", 2021,  60],
    ["Vegetable", "Daikon", 2020,  40],
    ["Vegetable", "Daikon", 2021,  45],
]
for i, row in enumerate(data):
    for j, val in enumerate(row):
        worksheet.cells.get(i + 1, j).put_value(val)
pivot_table = worksheet.pivot_tables.add("A1:D9", 2, 5)
pivot_table.add_field_to_area(PivotFieldType.ROW, "Category")
pivot_table.add_field_to_area(PivotFieldType.ROW, "Item")
pivot_table.add_field_to_area(PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")
pivot_table.data_fields[1].function = ConsolidationFunction.COUNT
pivot_table.calculate_data()
workbook.save("output_function.xlsx")
```

## 将值字段绘制到行或列轴
当数据透视表包含两个或以上的数据字段时，Aspose.Cells 会公开一个名为 `PivotTable.ValuesField` 的额外虚拟字段。该虚拟字段表示位于数据区域的所有数据字段的聚合结果。您可以将其拖动到行或列区域作为基础数据透视字段，这在并排布局多个度量值时非常有用。

{{% alert color="primary" %}}
`PivotTable.ValuesField` 在没有值字段或仅有一个值字段时不可用。
{{% /alert %}}

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType
from aspose.cells import ConsolidationFunction
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.name = "Data"
headers = ["Category", "Item", "Year", "Amount"]
for j, h in enumerate(headers):
    worksheet.cells.get(0, j).put_value(h)
data = [
    ["Fruit",     "Apple",  2020, 100],
    ["Fruit",     "Apple",  2021, 150],
    ["Fruit",     "Banana", 2020,  80],
    ["Fruit",     "Banana", 2021,  90],
    ["Vegetable", "Carrot", 2020,  50],
    ["Vegetable", "Carrot", 2021,  60],
    ["Vegetable", "Daikon", 2020,  40],
    ["Vegetable", "Daikon", 2021,  45],
]
for i, row in enumerate(data):
    for j, val in enumerate(row):
        worksheet.cells.get(i + 1, j).put_value(val)
pivot_table = worksheet.pivot_tables.add("A1:D9", 2, 5)
pivot_table.add_field_to_area(PivotFieldType.ROW, "Category")
pivot_table.add_field_to_area(PivotFieldType.ROW, "Item")
pivot_table.add_field_to_area(PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")
pivot_table.data_fields[1].function = ConsolidationFunction.COUNT
pivot_table.add_field_to_area(PivotFieldType.COLUMN, pivot_table.values_field)
pivot_table.calculate_data()
workbook.save("output_plot.xlsx")
```

{{< app/cells/assistant language="python-net" >}}