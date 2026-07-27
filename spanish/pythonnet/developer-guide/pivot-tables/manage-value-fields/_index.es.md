---
title: Administrar campos de valor de una tabla dinámica en Aspose.Cells para .NET
linktitle: Campos de valor
description: Aprenda a agregar campos base a la región de datos de una tabla dinámica, cambiar la función de resumen con PivotField.function y trazar el campo de valor en el eje de filas o columnas en Aspose.Cells for Python via .NET.
keywords: Aspose.Cells, Python via .NET, tabla dinámica, campo de valor, PivotField, PivotField.function, campo de datos, PivotTable.values_field, Sum, Average
type: docs
weight: 230
url: /es/python-net/pivot-table-manage-value-fields/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---


## Adding a Field to the Data Region

Adding a base field to the data (value) region is the first step in shaping how a pivot table aggregates your source data. Aspose.Cells exposes `PivotTable.add_field_to_area(PivotFieldType, str)`, an overload that accepts the constant `PivotFieldType.DATA` and the source-column name. Once a field is added to the data region, the API exposes it through the `PivotTable.data_fields` collection, in the order in which the fields were added. By default, a numeric source column is summarised with `ConsolidationFunction.SUM`, while a non-numeric column defaults to `Count`.

## Changing the Summary Function

{{% alert color="primary" %}}
Changing `function` only affects the aggregate, the source column does not change.
{{% /alert %}}

## Plotting Value Fields to Row or Column Axis

When a pivot table contains two or more data fields, Aspose.Cells exposes an additional virtual field called `PivotTable.values_field`. This virtual field represents the aggregate of every data field that lives in the data region. You can drag it into the Row or Column region as a base pivot field, which is useful for laying out multiple measures side by side.

{{% alert color="primary" %}}
`PivotTable.values_field` does not work if there is no or only one value field.
{{% /alert %}}

## Scenario 1 — Dragging a Base Field into the Value Region

This scenario shows how to put a single base field (`Amount`) into the data region of an existing pivot table. The shared pivot structure places `Category` and `Item` on the Row axis and `Year` on the Column axis. After the operation, `Amount` appears in the data region and is computed as the `Sum` of `Amount` by default.

```python
from aspose.cells.pivot import PivotFieldType

workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.name = "Data"

# Headers in A1:D1
worksheet.cells[0, 0].put_value("Category")
worksheet.cells[0, 1].put_value("Item")
worksheet.cells[0, 2].put_value("Year")
worksheet.cells[0, 3].put_value("Amount")

# Data rows A2:D9 using nested loops branching on j
for i in range(1, 9):
    for j in range(4):
        if j == 0:
            worksheet.cells[i, j].put_value("Fruit" if i <= 4 else "Vegetable")
        elif j == 1:
            if i == 1 or i == 2:
                worksheet.cells[i, j].put_value("Apple")
            elif i == 3 or i == 4:
                worksheet.cells[i, j].put_value("Banana")
            elif i == 5 or i == 6:
                worksheet.cells[i, j].put_value("Carrot")
            else:
                worksheet.cells[i, j].put_value("Daikon")
        elif j == 2:
            worksheet.cells[i, j].put_value(2020 + ((i - 1) % 2))
        elif j == 3:
            if i == 1:
                worksheet.cells[i, j].put_value(100)
            elif i == 2:
                worksheet.cells[i, j].put_value(150)
            elif i == 3:
                worksheet.cells[i, j].put_value(80)
            elif i == 4:
                worksheet.cells[i, j].put_value(90)
            elif i == 5:
                worksheet.cells[i, j].put_value(50)
            elif i == 6:
                worksheet.cells[i, j].put_value(60)
            elif i == 7:
                worksheet.cells[i, j].put_value(40)
            else:
                worksheet.cells[i, j].put_value(45)

# Add pivot table at F3 with name PivotTable1
pivot_index = worksheet.pivot_tables.add("A1:D9", "F3", "PivotTable1")
pivot_table = worksheet.pivot_tables[pivot_index]

# Pivot layout: Category and Item on Row, Year on Column, Amount as data field
pivot_table.add_field_to_area(PivotFieldType.ROW, "Category")
pivot_table.add_field_to_area(PivotFieldType.ROW, "Item")
pivot_table.add_field_to_area(PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")

pivot_table.calculate_data()
workbook.save("output_drag.xlsx")
```

## Scenario 2 — Changing the Summary Function

```python
import aspose.cells as ac

workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.name = "Data"

headers = ["Category", "Item", "Year", "Amount"]
for j in range(len(headers)):
    worksheet.cells[0, j].put_value(headers[j])

data = [
    ["Fruit",     "Apple",  2020, 100],
    ["Fruit",     "Apple",  2021, 150],
    ["Fruit",     "Banana", 2020,  80],
    ["Fruit",     "Banana", 2021,  90],
    ["Vegetable", "Carrot", 2020,  50],
    ["Vegetable", "Carrot", 2021,  60],
    ["Vegetable", "Daikon", 2020,  40],
    ["Vegetable", "Daikon", 2021,  45]
]

for i in range(len(data)):
    for j in range(len(data[i])):
        worksheet.cells[i + 1, j].put_value(data[i][j])

pivot_index = worksheet.pivot_tables.add("A1:D9", "F3", "PivotTable1")
pivot_table = worksheet.pivot_tables[pivot_index]

pivot_table.add_field_to_area(ac.PivotFieldType.ROW, "Category")
pivot_table.add_field_to_area(ac.PivotFieldType.ROW, "Item")
pivot_table.add_field_to_area(ac.PivotFieldType.COLUMN, "Year")

pivot_table.add_field_to_area(ac.PivotFieldType.DATA, "Amount")
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, "Amount")

count_field = pivot_table.data_fields[1]
count_field.function = ac.ConsolidationFunction.COUNT

pivot_table.calculate_data()

workbook.save("output_function.xlsx")
```

## Scenario 3 — Plotting Value Fields to Row or Column Axis

With two data fields in place, `PivotTable.values_field` becomes usable. This scenario drags that aggregate virtual field onto the Column region so that every measure in the data region appears as its own column block next to `Year`.

```python
import aspose.cells as ac

workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.name = "Data"

headers = ["Category", "Item", "Year", "Amount"]
for j in range(len(headers)):
    worksheet.cells[0, j].put_value(headers[j])

data = [
    ["Fruit",     "Apple",  2020, 100],
    ["Fruit",     "Apple",  2021, 150],
    ["Fruit",     "Banana", 2020,  80],
    ["Fruit",     "Banana", 2021,  90],
    ["Vegetable", "Carrot", 2020,  50],
    ["Vegetable", "Carrot", 2021,  60],
    ["Vegetable", "Daikon", 2020,  40],
    ["Vegetable", "Daikon", 2021,  45]
]

for i in range(len(data)):
    for j in range(len(data[i])):
        worksheet.cells[i + 1, j].put_value(data[i][j])

pivot_index = worksheet.pivot_tables.add("A1:D9", "F3", "PivotTable1")
pivot_table = worksheet.pivot_tables[pivot_index]

pivot_table.add_field_to_area(ac.PivotFieldType.ROW, "Category")
pivot_table.add_field_to_area(ac.PivotFieldType.ROW, "Item")
pivot_table.add_field_to_area(ac.PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, "Amount")
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, "Amount")
pivot_table.data_fields[1].function = ac.ConsolidationFunction.COUNT

# Plot the value fields onto the Column axis.
pivot_table.add_field_to_area(ac.PivotFieldType.COLUMN, pivot_table.values_field.name)

pivot_table.calculate_data()

workbook.save("output_plot.xlsx")
```

Together, these three scenarios cover every aspect of value-field manipulation in Aspose.Cells for Python via .NET, from a single data field with the default `Sum` to a multi-measure pivot in which the virtual `ValuesField` controls the layout on the Row or Column axis.

{{< app/cells/assistant language="python" >}}
