---
title: Insert Pivot Table
description: Create and format pivot tables with Aspose.Cells for Python via .NET.
linktitle: Pivot Tables
url: /python-net/create-pivot-table/
type: docs
weight: 160
keywords: Create Pivot Table, Insert Pivot Table, Format Pivot Table.
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **What is a Pivot Table?**
A pivot table is an interactive summary report: it condenses a large block of raw, row-by-row data into a compact matrix without a single formula. You decide which columns become row labels, which become column labels and which are aggregated as values — the pivot table does the grouping and the math:
- **Summarize** — total sales per product, per region or per quarter instead of long formula chains.
- **Compare** — categories on the rows and periods on the columns turn a flat list into a cross report where trends are visible at a glance.
- **Drill down** — double-click any summary value to inspect the source rows behind it.
- **Refresh** — when the source data changes, one refresh recalculates the whole report.
Typical scenarios are sales dashboards, expense breakdowns and inventory analysis — any question of the form "how do these numbers break down by category and time?". Aspose.Cells for Python via .NET builds the same pivot tables programmatically, so the workbooks your application generates can carry ready-made reports instead of raw data only.

### **Pivot Table Object Model**
Aspose.Cells for Python via .NET provides a special set of classes in the [**aspose.cells.pivot**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/) namespace that are used to create and control pivot tables. These classes are used to create and set [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/) objects, the building blocks of a pivot table. The objects are:
- [**PivotField**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfield/) represents a field in a [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/).
- [**PivotFieldCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfieldcollection) represents a collection of all the [**PivotField**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfield/) objects in the [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable).
- [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable) represents a PivotTable on a worksheet.
- [**PivotTableCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection) represents a collection of all the [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable) objects on a worksheet.

### **Creating a Simple Pivot Table Using Aspose.Cells**
Creating a pivot table is a three-step recipe: write the source data into worksheet cells, add the pivot table at a destination position, and place the pivot fields into the row, column and data areas.
1. Add data to a worksheet using the [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell) object's [**put_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/put_value/#str) method. This data will be used as the pivot table's data source.
2. Add a pivot table to the worksheet by calling the [**PivotTables**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection) collection's [**add**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection/add/#str-str-str) method: `add(source_data, row, column)`. `source_data` is the source range (for example, "A1:C8"); `row` and `column` are the 0-based coordinates of the destination cell at the pivot table's upper-left corner (cell E3 means row 2, column 4). The method returns the new [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable) object directly.
3. Place the pivot fields with the [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable) object's `add_field_to_area` method: a field name goes to the row area (`PivotFieldType.ROW`), the column area (`PivotFieldType.COLUMN`) or the data area (`PivotFieldType.DATA`).
4. Save the workbook — the pivot table is written into the saved file.
After executing the example code, a pivot table is added to the worksheet.

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType
# Create a new workbook and get the first worksheet
workbook = ac.Workbook()
sheet = workbook.worksheets[0]
# Write the source data: sales per sport and quarter
sheet.cells.get("A1").put_value("Sport")
sheet.cells.get("B1").put_value("Quarter")
sheet.cells.get("C1").put_value("Sales")
sheet.cells.get("A2").put_value("Golf")
sheet.cells.get("B2").put_value("Qtr3")
sheet.cells.get("C2").put_value(1500)
sheet.cells.get("A3").put_value("Golf")
sheet.cells.get("B3").put_value("Qtr4")
sheet.cells.get("C3").put_value(2000)
sheet.cells.get("A4").put_value("Tennis")
sheet.cells.get("B4").put_value("Qtr3")
sheet.cells.get("C4").put_value(600)
sheet.cells.get("A5").put_value("Tennis")
sheet.cells.get("B5").put_value("Qtr4")
sheet.cells.get("C5").put_value(1500)
sheet.cells.get("A6").put_value("Tennis")
sheet.cells.get("B6").put_value("Qtr3")
sheet.cells.get("C6").put_value(4070)
sheet.cells.get("A7").put_value("Tennis")
sheet.cells.get("B7").put_value("Qtr4")
sheet.cells.get("C7").put_value(5000)
sheet.cells.get("A8").put_value("Golf")
sheet.cells.get("B8").put_value("Qtr3")
sheet.cells.get("C8").put_value(6430)
# Add a pivot table at destination cell E3, sourced from A1:C8
pivot_table = sheet.pivot_tables.add("A1:C8", 2, 4)
# Assign pivot fields: Sport to Rows, Quarter to Columns, Sales to Data
pivot_table.add_field_to_area(PivotFieldType.ROW, "Sport")
pivot_table.add_field_to_area(PivotFieldType.COLUMN, "Quarter")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Sales")
# Save the workbook
workbook.save("pivotTable_test_out.xlsx")
```

{{% alert color="primary" %}}
When assigning a range of cells as the data source, the range must go from top left to bottom right. For example, "A1:C3" is valid but "C3:A1" is not.
{{% /alert %}}

## Related Articles
- [Add Filter Fields to a Pivot Table in Aspose.Cells for Python via .NET](/cells/python-net/add-page-field-in-pivot-table/)
- [Apply Styles to Pivot Tables in Aspose.Cells for Python via .NET](/cells/python-net/apply-style-to-pivot-table/)
- [Modify Page Field Layout in Pivot Table](/cells/python-net/change-page-field-layout/)
- [Filtering Pivot Tables by Label or Value](/cells/python-net/filter-by-label-or-value-of-pivot-table/)
- [Manage Pivot Table Value Fields in Aspose.Cells for Python via .NET](/cells/python-net/manage-value-fields/)

{{< app/cells/assistant language="python-net" >}}