---
title: Insert Pivot Table
description: Create and format pivot tables of Excel spreadsheet files using Aspose.Cells for Node.js via Java.
linktitle: Pivot Tables
url: /nodejs-java/create-pivot-table/
type: docs
weight: 160
keywords: Create Pivot Table, Insert Pivot Table, Format Pivot Table, Aspose.Cells for Node.js via Java.
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Create Pivot Table**
It is possible to use Aspose.Cells to add pivot tables to spreadsheets programmatically.

### **Pivot Table Object Model**
Aspose.Cells provides a set of classes that are used to create and control pivot tables. The building blocks are:
- `PivotField` represents a field in a `PivotTable`.
- `PivotFieldCollection` represents a collection of all the `PivotField` objects in the `PivotTable`.
- `PivotTable` represents a PivotTable on a worksheet.
- `PivotTableCollection` represents a collection of all the `PivotTable` objects on a worksheet.

### **Creating a Simple Pivot Table Using Aspose.Cells**
1. Add data to a worksheet using the cell's `putValue` method. This data will be used as the pivot table's data source.
2. Add a pivot table to the worksheet by calling the `PivotTables` collection's `add` method, which is encapsulated in the worksheet object.
3. Access the new `PivotTable` object from the `PivotTables` collection by passing the PivotTable's index.
4. Use any of the `PivotTable` objects (explained above) to manage the pivot table.

After executing the example code, a pivot table is added to the worksheet.

```javascript
var dataDir = "./";

// Instantiating a Workbook object
var workbook = new AsposeCells.Workbook();

// Obtaining the reference of the newly added worksheet
var sheet = workbook.getWorksheets().get(0);

var cells = sheet.getCells();

// Setting the value to the cells
var cell = cells.get("A1");
cell.putValue("Sport");
cell = cells.get("B1");
cell.putValue("Quarter");
cell = cells.get("C1");
cell.putValue("Sales");

cell = cells.get("A2");
cell.putValue("Golf");
cell = cells.get("A3");
cell.putValue("Golf");
cell = cells.get("A4");
cell.putValue("Tennis");
cell = cells.get("A5");
cell.putValue("Tennis");
cell = cells.get("A6");
cell.putValue("Tennis");
cell = cells.get("A7");
cell.putValue("Tennis");
cell = cells.get("A8");
cell.putValue("Golf");

cell = cells.get("B2");
cell.putValue("Qtr3");
cell = cells.get("B3");
cell.putValue("Qtr4");
cell = cells.get("B4");
cell.putValue("Qtr3");
cell = cells.get("B5");
cell.putValue("Qtr4");
cell = cells.get("B6");
cell.putValue("Qtr3");
cell = cells.get("B7");
cell.putValue("Qtr4");
cell = cells.get("B8");
cell.putValue("Qtr3");

cell = cells.get("C2");
cell.putValue(1500);
cell = cells.get("C3");
cell.putValue(2000);
cell = cells.get("C4");
cell.putValue(600);
cell = cells.get("C5");
cell.putValue(1500);
cell = cells.get("C6");
cell.putValue(4070);
cell = cells.get("C7");
cell.putValue(5000);
cell = cells.get("C8");
cell.putValue(6430);

var pivotTables = sheet.getPivotTables();

// Adding a PivotTable to the worksheet
var index = pivotTables.add("=A1:C8", "E3", "PivotTable2");

// Accessing the instance of the newly added PivotTable
var pivotTable = pivotTables.get(index);

// Unshowing grand totals for rows.
pivotTable.setRowGrand(false);

// Draging the first field to the row area.
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Row, 0);

// Draging the second field to the column area.
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Column, 1);

// Draging the third field to the data area.
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Data, 2);

// Saving the Excel file
workbook.save(dataDir + "pivotTable_test_out.xls");
```

{{% alert color="primary" %}}
When assigning a range of cells as the data source, the range must go from top left to bottom right. For example, "A1:C3" is valid but "C3:A1" is not.
{{% /alert %}}

## Related Articles
- [Add Filter Fields to a Pivot Table in Aspose.Cells for Node.js via Java](/cells/nodejs-java/add-page-field-in-pivot-table/)
- [Apply Styles to Pivot Tables in Aspose.Cells for Node.js via Java](/cells/nodejs-java/apply-style-to-pivot-table/)
- [Modify Page Field Layout in Pivot Table](/cells/nodejs-java/change-page-field-layout/)
- [Filtering Pivot Tables by Label or Value](/cells/nodejs-java/filter-by-label-or-value-of-pivot-table/)
- [Manage Pivot Table Value Fields in Aspose.Cells for Node.js via Java](/cells/nodejs-java/manage-value-fields/)

{{< app/cells/assistant language="nodejs-java" >}}