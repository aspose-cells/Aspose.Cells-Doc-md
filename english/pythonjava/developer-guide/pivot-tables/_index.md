---
title: Pivot Tables
linktitle: Pivot Tables
description: Create and format pivot tables with Aspose.Cells for Python via Java.
url: /python-java/create-pivot-table/
type: docs
weight: 160
keywords: Create Pivot Table, Insert Pivot Table, Format Pivot Table.
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **What is a Pivot Table?**
A pivot table is an interactive summary report: it condenses a large block of raw, row-by-row data into a compact matrix without a single formula. You decide which columns become row labels, which become column labels and which are aggregated as values — the pivot table does the grouping and the math:
- **Summarize** — total sales per product, per region or per quarter instead of long formula chains.
- **Compare** — categories on the rows and periods on the columns turn a flat list into a cross report where trends are visible at a glance.
- **Drill down** — double-click any summary value to inspect the source rows behind it.
- **Refresh** — when the source data changes, one refresh recalculates the whole report.
Typical scenarios are sales dashboards, expense breakdowns and inventory analysis — any question of the form "how do these numbers break down by category and time?". Aspose.Cells for Python via Java builds the same pivot tables programmatically, so the workbooks your application generates can carry ready-made reports instead of raw data only.

### **Pivot Table Object Model**
Aspose.Cells provides a set of classes that are used to create and control pivot tables. The building blocks are:
- `PivotField` represents a field in a `PivotTable`.
- `PivotFieldCollection` represents a collection of all the `PivotField` objects in the `PivotTable`.
- `PivotTable` represents a PivotTable on a worksheet.
- `PivotTableCollection` represents a collection of all the `PivotTable` objects on a worksheet.

### **Creating a Simple Pivot Table Using Aspose.Cells**
Creating a pivot table is a three-step recipe: write the source data into worksheet cells, add the pivot table at a destination position, and place the pivot fields into the row, column and data areas.
1. Add data to a worksheet using the cell's `putValue` method. This data will be used as the pivot table's data source.
2. Add a pivot table to the worksheet by calling the `PivotTables` collection's `add` method: `add(sourceData, row, column)`. `sourceData` is the source range (for example, "A1:C8"); `row` and `column` are the 0-based coordinates of the destination cell at the pivot table's upper-left corner (cell E3 means row 2, column 4). The method returns the new `PivotTable` object directly.
3. Place the pivot fields with the `PivotTable` object's `addFieldToArea` method: a field name goes to the row area (`PivotFieldType.ROW`), the column area (`PivotFieldType.COLUMN`) or the data area (`PivotFieldType.DATA`).
4. Save the workbook — the pivot table is written into the saved file.
After executing the example code, a pivot table is added to the worksheet.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, PivotFieldType
# Create a new workbook and get the first worksheet
workbook = Workbook()
sheet = workbook.getWorksheets().get(0)
cells = sheet.getCells()
# Write the source data: sales per sport and quarter
cells.get("A1").putValue("Sport")
cells.get("B1").putValue("Quarter")
cells.get("C1").putValue("Sales")
cells.get("A2").putValue("Golf")
cells.get("B2").putValue("Qtr3")
cells.get("C2").putValue(1500)
cells.get("A3").putValue("Golf")
cells.get("B3").putValue("Qtr4")
cells.get("C3").putValue(2000)
cells.get("A4").putValue("Tennis")
cells.get("B4").putValue("Qtr3")
cells.get("C4").putValue(600)
cells.get("A5").putValue("Tennis")
cells.get("B5").putValue("Qtr4")
cells.get("C5").putValue(1500)
cells.get("A6").putValue("Tennis")
cells.get("B6").putValue("Qtr3")
cells.get("C6").putValue(4070)
cells.get("A7").putValue("Tennis")
cells.get("B7").putValue("Qtr4")
cells.get("C7").putValue(5000)
cells.get("A8").putValue("Golf")
cells.get("B8").putValue("Qtr3")
cells.get("C8").putValue(6430)
# Add a pivot table at destination cell E3, sourced from A1:C8
pivotTable = sheet.getPivotTables().add("A1:C8", 2, 4)
# Assign pivot fields: Sport to Rows, Quarter to Columns, Sales to Data
pivotTable.addFieldToArea(PivotFieldType.ROW, "Sport")
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Quarter")
pivotTable.addFieldToArea(PivotFieldType.DATA, "Sales")
# Save the workbook
workbook.save("pivotTable_test_out.xlsx")
```

{{% alert color="primary" %}}
When assigning a range of cells as the data source, the range must go from top left to bottom right. For example, "A1:C3" is valid but "C3:A1" is not.
{{% /alert %}}

## Related Articles
- [Add Filter Fields to a Pivot Table in Aspose.Cells for Python via Java](/cells/python-java/add-page-field-in-pivot-table/)
- [Apply Styles to Pivot Tables in Aspose.Cells for Python via Java](/cells/python-java/apply-style-to-pivot-table/)
- [Modify Page Field Layout in Pivot Table](/cells/python-java/change-page-field-layout/)
- [Filtering Pivot Tables by Label or Value](/cells/python-java/filter-by-label-or-value-of-pivot-table/)
- [Manage Pivot Table Value Fields in Aspose.Cells for Python via Java](/cells/python-java/manage-value-fields/)

{{< app/cells/assistant language="python" >}}