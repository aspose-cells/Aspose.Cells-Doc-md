---
title: Insert Pivot Table
description: Create and format pivot tables of Excel spreadsheet files.
linktitle: Pivot Tables
url: /net/create-pivot-table/
type: docs
weight: 160
keywords: Create Pivot Table, Insert Pivot Table, Format Pivot Table.
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **What is a Pivot Table?**
A pivot table is an interactive summary report: it condenses a large block of raw, row-by-row data into a compact matrix without a single formula. You decide which columns become row labels, which become column labels and which are aggregated as values — the pivot table does the grouping and the math:
- **Summarize** — total sales per product, per region or per quarter instead of long formula chains.
- **Compare** — categories on the rows and periods on the columns turn a flat list into a cross report where trends are visible at a glance.
- **Drill down** — double-click any summary value to inspect the source rows behind it.
- **Refresh** — when the source data changes, one refresh recalculates the whole report.
Typical scenarios are sales dashboards, expense breakdowns and inventory analysis — any question of the form "how do these numbers break down by category and time?". Aspose.Cells for .NET builds the same pivot tables programmatically, so the workbooks your application generates can carry ready-made reports instead of raw data only.

### **Pivot Table Object Model**
Aspose.Cells provides a special set of classes in the [**Aspose.Cells.Pivot**](https://reference.aspose.com/cells/net/aspose.cells.pivot) namespace that are used to create and control pivot tables. These classes are used to create and set [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable) objects, the building blocks of a pivot table. The objects are:
- [**PivotField**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfield) represents a field in a [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable).
- [**PivotFieldCollection**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfieldcollection) represents a collection of all the [**PivotField**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfield) objects in the [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable).
- [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable) represents a PivotTable on a worksheet.
- [**PivotTableCollection**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection) represents a collection of all the [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable) objects on a worksheet.

### **Creating a Simple Pivot Table Using Aspose.Cells**
Creating a pivot table is a three-step recipe: write the source data into worksheet cells, add the pivot table at a destination position, and place the pivot fields into the row, column and data areas.
1. Add data to a worksheet using the [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) object's [**PutValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index) method. This data will be used as the pivot table's data source.
2. Add a pivot table to the worksheet by calling the [**PivotTables**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection) collection's [**Add**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection/methods/add/index) method: `Add(sourceData, row, column)`. `sourceData` is the source range (for example, "A1:C8"); `row` and `column` are the 0-based coordinates of the destination cell at the pivot table's upper-left corner (cell E3 means row 2, column 4). The method returns the new [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable) object directly.
3. Place the pivot fields with the [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable) object's `AddFieldToArea` method: a field name goes to the row area (`PivotFieldType.Row`), the column area (`PivotFieldType.Column`) or the data area (`PivotFieldType.Data`).
4. Save the workbook — the pivot table is written into the saved file.
After executing the example code, a pivot table is added to the worksheet.

```csharp
using Aspose.Cells;
using Aspose.Cells.Pivot;
// Create a new workbook and get the first worksheet
Workbook workbook = new Workbook();
Worksheet sheet = workbook.Worksheets[0];
// Write the source data: sales per sport and quarter
sheet.Cells["A1"].PutValue("Sport");
sheet.Cells["B1"].PutValue("Quarter");
sheet.Cells["C1"].PutValue("Sales");
sheet.Cells["A2"].PutValue("Golf");
sheet.Cells["B2"].PutValue("Qtr3");
sheet.Cells["C2"].PutValue(1500);
sheet.Cells["A3"].PutValue("Golf");
sheet.Cells["B3"].PutValue("Qtr4");
sheet.Cells["C3"].PutValue(2000);
sheet.Cells["A4"].PutValue("Tennis");
sheet.Cells["B4"].PutValue("Qtr3");
sheet.Cells["C4"].PutValue(600);
sheet.Cells["A5"].PutValue("Tennis");
sheet.Cells["B5"].PutValue("Qtr4");
sheet.Cells["C5"].PutValue(1500);
sheet.Cells["A6"].PutValue("Tennis");
sheet.Cells["B6"].PutValue("Qtr3");
sheet.Cells["C6"].PutValue(4070);
sheet.Cells["A7"].PutValue("Tennis");
sheet.Cells["B7"].PutValue("Qtr4");
sheet.Cells["C7"].PutValue(5000);
sheet.Cells["A8"].PutValue("Golf");
sheet.Cells["B8"].PutValue("Qtr3");
sheet.Cells["C8"].PutValue(6430);
// Add a pivot table at destination cell E3, sourced from A1:C8
PivotTable pivotTable = sheet.PivotTables.Add("A1:C8", 2, 4);
// Assign pivot fields: Sport to Rows, Quarter to Columns, Sales to Data
pivotTable.AddFieldToArea(PivotFieldType.Row, "Sport");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Quarter");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Sales");
// Save the workbook
workbook.Save("pivotTable_test_out.xlsx");
```

{{% alert color="primary" %}}
When assigning a range of cells as the data source, the range must go from top left to bottom right. For example, "A1:C3" is valid but "C3:A1" is not.
{{% /alert %}}

## Related Articles
- [Add Filter Fields to a Pivot Table in Aspose.Cells for .NET](/cells/net/add-page-field-in-pivot-table/)
- [Apply Styles to Pivot Tables in Aspose.Cells for .NET](/cells/net/apply-style-to-pivot-table/)
- [Modify Page Field Layout in Pivot Table](/cells/net/change-page-field-layout/)
- [Filtering Pivot Tables by Label or Value](/cells/net/filter-by-label-or-value-of-pivot-table/)
- [Manage Pivot Table Value Fields in Aspose.Cells for .NET](/cells/net/manage-value-fields/)

{{< app/cells/assistant language="csharp" >}}