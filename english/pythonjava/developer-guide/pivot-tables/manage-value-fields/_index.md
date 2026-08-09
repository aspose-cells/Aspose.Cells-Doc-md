---
title: Manage Pivot Table Value Fields in Aspose.Cells for Python via Java
linktitle: Value Fields
description: Learn how to add base fields to the data region of a pivot table, change the summary function with PivotField.Function, and plot the value field onto the Row or Column axis in Aspose.Cells for Python via Java.
keywords: Aspose.Cells, Python via Java, pivot table, value field, PivotField, PivotField.Function, data field, PivotTable.ValuesField, Sum, Average
type: docs
weight: 230
url: /python-java/manage-value-fields/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---


## Adding a Field to the Data Region

Adding a base field to the data (value) region is the first step in shaping how a pivot table aggregates the source data. Aspose.Cells exposes `PivotTable.AddFieldToArea(PivotFieldType, string)`, an overload that accepts the constant `PivotFieldType.Data` and the source-column name. Once a field is added to the data region, the API exposes it through the `PivotTable.DataFields` collection, in the order in which the fields were added. By default, a numeric source column is summarised with `Sum`, while a non-numeric column defaults to `Count`.

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

## Changing the Summary Function

Each `PivotField` returned by `PivotTable.DataFields` exposes a writable `Function` property of type `ConsolidationFunction`, the aggregate applied to that field's underlying values. `ConsolidationFunction` is an enum with members `Sum`, `Count`, `Average`, `Max`, `Min`, `Product`, `StdDev`, `StdDevp`, `Var`, and `Varp` — the first six cover the vast majority of real-world use cases, while the last four are statistical aggregates useful for variance analysis.

{{% alert color="primary" %}}
Changing `Function` only affects the aggregate; the source column and the pivot's row/column structure are not modified. To switch the aggregate for an existing data field, set `pivotTable.DataFields[i].Function = ConsolidationFunction.<X>;` and then call `pivotTable.CalculateData()` to re-render the pivot.
{{% /alert %}}



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

## Plotting Value Fields to Row or Column Axis

When a pivot table contains two or more data fields, Aspose.Cells exposes an additional virtual field called `PivotTable.ValuesField`. This virtual field represents the aggregate of every data field that lives in the data region. You can drag it into the Row or Column region as a base pivot field, which is useful for laying out multiple measures side by side.

{{% alert color="primary" %}}
`PivotTable.ValuesField` does not work if there is no or only one value field.
{{% /alert %}}

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

{{< app/cells/assistant language="python" >}}
