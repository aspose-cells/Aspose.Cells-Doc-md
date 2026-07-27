---
title: Aspose.Cells for Python via Java 中的值字段
linktitle: Aspose.Cells for Python via Java 中的值字段
description: 了解如何向数据透视表的数据区域添加基础字段，使用 PivotField.Function 更改汇总函数，以及将值字段绘制到 Aspose.Cells for Python via Java 中的行或列轴。
keywords: Aspose.Cells, Python via Java, 数据透视表, 值字段, PivotField, PivotField.Function, 数据字段, PivotTable.ValuesField, Sum, Average
type: docs
weight: 230
url: /zh/python-java/manage-value-fields/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## 向数据区域添加字段
将基础字段添加到数据（值）区域是塑造数据透视表如何聚合源数据的第一步。Aspose.Cells 公开 `PivotTable.addFieldToArea(PivotFieldType, string)`，这是一个接受常量 `PivotFieldType.DATA` 和源列名称的重载。一旦字段被添加到数据区域，API 会通过 `PivotTable.DataFields` 集合按字段添加顺序公开它们。默认情况下，数值型源列使用 `ConsolidationFunction.SUM` 进行汇总，而非数值列默认为 `COUNT`。
## 更改汇总函数
放置在数据区域中的每个字段在内部都会被包装为 `PivotField` 实例，其 `Function` 属性返回 `ConsolidationFunction` 枚举中的一个值。同一个 `Function` setter 可用于在可用的聚合之间切换，包括 `SUM`、`COUNT`、`AVERAGE`、`MAX`、`MIN`、`PRODUCT`、`STDDEV`、`STDDEVP`、`VAR` 和 `VARP`。
{{% alert color="primary" %}}
更改 `Function` 仅影响聚合，源列不会更改。
{{% /alert %}}
因此，您可以让一个数据字段保持为 `SUM`，同时添加另一个针对同一源列但使用 `COUNT` 或 `AVERAGE` 的数据字段，所有这些都可以在同一个透视表中完成。
## 将值字段绘制到行或列轴
当数据透视表包含两个或更多数据字段时，Aspose.Cells 会公开一个名为 `PivotTable.ValuesField` 的额外虚拟字段。该虚拟字段表示数据区域中每个数据字段的聚合。您可以将其作为基础透视字段拖动到行或列区域，这对于并排排列多个度量值非常有用。
{{% alert color="primary" %}}
`PivotTable.ValuesField` 在没有或仅有一个值字段时不起作用。
{{% /alert %}}
下面的场景演练了三个端到端示例，针对相同的数据透视结构演示上述每个功能。
## 场景 1 — 将基础字段拖动到值区域
此场景演示如何将单个基础字段（`Amount`）放入现有数据透视表的数据区域。共享的数据透视结构将 `Category` 和 `Item` 放在行轴上，将 `Year` 放在列轴上。操作完成后，`Amount` 将出现在数据区域中，并默认按 `Sum` 计算 `Amount`。
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

pivot_index = worksheet.pivot_tables.add("A1:D9", "F3", "PivotTable1")
pivot_table = worksheet.pivot_tables[pivot_index]
pivot_table.add_field_to_area(PivotFieldType.ROW, "Category")
pivot_table.add_field_to_area(PivotFieldType.ROW, "Item")
pivot_table.add_field_to_area(PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")

pivot_table.calculate_data()
workbook.save("output_drag.xlsx")
```
## 场景 2 — 更改汇总函数
此场景从与场景 1 相同的数据透视结构开始，但将 `Amount` 字段添加到数据区域两次。两个数据字段都引用同一个源列，但第二个字段通过 `PivotField.Function` setter 被覆盖，使其变为 `Count` 而不是默认的 `Sum`。
```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType, ConsolidationFunction

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

pivot_index = worksheet.pivot_tables.add("A1:D9", "F3", "PivotTable1")
pivot_table = worksheet.pivot_tables[pivot_index]
pivot_table.add_field_to_area(PivotFieldType.ROW, "Category")
pivot_table.add_field_to_area(PivotFieldType.ROW, "Item")
pivot_table.add_field_to_area(PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")
pivot_table.data_fields[1].function = ConsolidationFunction.COUNT

pivot_table.calculate_data()
workbook.save("output_function.xlsx")
```
## 场景 3 — 将值字段绘制到行或列轴
在存在两个数据字段的情况下，`PivotTable.ValuesField` 变为可用。此场景将该聚合虚拟字段拖到列区域，以便数据区域中的每个度量值都显示为 `Year` 旁边独立的列块。
```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType, ConsolidationFunction

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

pivot_index = worksheet.pivot_tables.add("A1:D9", "F3", "PivotTable1")
pivot_table = worksheet.pivot_tables[pivot_index]
pivot_table.add_field_to_area(PivotFieldType.ROW, "Category")
pivot_table.add_field_to_area(PivotFieldType.ROW, "Item")
pivot_table.add_field_to_area(PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")
pivot_table.data_fields[1].function = ConsolidationFunction.COUNT
pivot_table.add_field_to_area(PivotFieldType.COLUMN, pivot_table.values_field.name)

pivot_table.calculate_data()
workbook.save("output_plot.xlsx")
```
综上所述，这三个场景涵盖了 Aspose.Cells for Python via Java 中值字段操作的方方面面，从具有默认 `Sum` 的单个数据字段，到虚拟 `ValuesField` 控制行或列轴布局的多度量透视表。

{{< app/cells/assistant language="python" >}}
