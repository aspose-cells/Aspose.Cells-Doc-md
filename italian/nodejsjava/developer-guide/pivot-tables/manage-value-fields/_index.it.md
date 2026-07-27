---
title: Gestire i campi valore di una tabella pivot in Aspose.Cells per .NET
linktitle: Campi valore
description: Learn how to add value fields to a pivot table in Aspose.Cells for Node.js via Java and plot them onto Row/Column axis.
keywords: Aspose.Cells, Node.js via Java, pivot table, value field, PivotField, PivotField.Function, data field, Sum, Average
type: docs
weight: 230
url: /it/nodejs-java/pivot-table-manage-value-fields/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---


Value fields are the heart of every pivot table, the numeric aggregates that summarise the source data. In Aspose.Cells for Node.js via Java, the data region of a pivot table is populated by adding base fields to it through `PivotTable.addFieldToArea`, and each field placed in that region can have its own summary function. When two or more data fields exist, Aspose.Cells exposes a special aggregate field, `PivotTable.getValuesField()`, that can be plotted onto the Row or Column axis as a base field, giving you finer control over how value fields appear in the layout.

## Adding a Field to the Data Region

Adding a base field to the data (value) region is the first step in shaping how a pivot table aggregates your source data. Aspose.Cells exposes `PivotTable.addFieldToArea(PivotFieldType, string)`, an overload that accepts the constant `PivotFieldType.DATA` and the source-column name. Once a field is added to the data region, the API exposes it through the `PivotTable.getDataFields()` collection, in the order in which the fields were added. By default, a numeric source column is summarised with `ConsolidationFunction.SUM`, while a non-numeric column defaults to `COUNT`.

## Changing the Summary Function

Every field placed in the data region is wrapped internally as a `PivotField` instance, and its `getFunction()` property returns a value from the `ConsolidationFunction` enum. The same `setFunction()` setter lets you switch between the available aggregates, including `SUM`, `COUNT`, `AVERAGE`, `MAX`, `MIN`, `PRODUCT`, `STD_DEV`, `STD_DEVP`, `VAR`, and `VARP`.

{{% alert color="primary" %}}
Changing `Function` only affects the aggregate, the source column does not change.
{{% /alert %}}

You can therefore leave one data field as `SUM` while you add a second data field that targets the same source column but uses `COUNT` or `AVERAGE`, all in a single pivot.

## Plotting Value Fields to Row or Column Axis

When a pivot table contains two or more data fields, Aspose.Cells exposes an additional virtual field called `PivotTable.getValuesField()`. This virtual field represents the aggregate of every data field that lives in the data region. You can drag it into the Row or Column region as a base pivot field, which is useful for laying out multiple measures side by side.

{{% alert color="primary" %}}
`PivotTable.getValuesField()` does not work if there is no or only one value field.
{{% /alert %}}

## **Dragging a Base Field into the Value Region**

This scenario shows how to put a single base field (`Amount`) into the data region of an existing pivot table. The shared pivot structure places `Category` and `Item` on the Row axis and `Year` on the Column axis. After the operation, `Amount` appears in the data region and is computed as the `Sum` of `Amount` by default.

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Data");

// Headers in A1:D1
worksheet.getCells().get(0, 0).putValue("Category");
worksheet.getCells().get(0, 1).putValue("Item");
worksheet.getCells().get(0, 2).putValue("Year");
worksheet.getCells().get(0, 3).putValue("Amount");

// Data rows A2:D9 using nested loops branching on j
for (let i = 1; i <= 8; i++) {
 for (let j = 0; j < 4; j++) {
 switch (j) {
 case 0:
 worksheet.getCells().get(i, j).putValue(i <= 4 ? "Fruit" : "Vegetable");
 break;
 case 1:
 if (i == 1 || i == 2) worksheet.getCells().get(i, j).putValue("Apple");
 else if (i == 3 || i == 4) worksheet.getCells().get(i, j).putValue("Banana");
 else if (i == 5 || i == 6) worksheet.getCells().get(i, j).putValue("Carrot");
 else worksheet.getCells().get(i, j).putValue("Daikon");
 break;
 case 2:
 worksheet.getCells().get(i, j).putValue(2020 + ((i - 1) % 2));
 break;
 case 3:
 if (i == 1) worksheet.getCells().get(i, j).putValue(100);
 else if (i == 2) worksheet.getCells().get(i, j).putValue(150);
 else if (i == 3) worksheet.getCells().get(i, j).putValue(80);
 else if (i == 4) worksheet.getCells().get(i, j).putValue(90);
 else if (i == 5) worksheet.getCells().get(i, j).putValue(50);
 else if (i == 6) worksheet.getCells().get(i, j).putValue(60);
 else if (i == 7) worksheet.getCells().get(i, j).putValue(40);
 else worksheet.getCells().get(i, j).putValue(45);
 break;
 }
 }
}

// Add pivot table at F3 with name PivotTable1
let pivotIndex = worksheet.getPivotTables().add("A1:D9", "F3", "PivotTable1");
let pivotTable = worksheet.getPivotTables().get(pivotIndex);

// Pivot layout: Category and Item on Row, Year on Column, Amount as data field
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Category");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Item");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

pivotTable.refreshData();
pivotTable.calculateData();
workbook.save("output_drag.xlsx");
```

## **Changing the Summary Function**

<!-- CODE_BLOCK:1:Build a complete end-to-end sample that imports the Aspose.Cells namespace, then creates a new Workbook instance, gets worksheets.get(0), assigns worksheet.setName("Data"), and writes the same 4-column 9-row dataset (Category, Item, Year, Amount) using individual cells.get(i, j).putValue(...) calls for each cell, iterating row index i from 1 to 8 inclusive and column index j from 0 to 3 in nested loops, branching on j to pick the correct value, so A1:D1 contains the headers and A2:D9 contains the eight data rows. Add a pivot table by calling worksheet.getPivotTables().add("A1:D9", "F3", "PivotTable1"), place "Category" and "Item" on Row, place "Year" on Column, then call pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount") twice so that pivotTable.getDataFields() contains two fields. Retrieve the second data field via pivotTable.getDataFields().get(1) and assign countField.setFunction(ConsolidationFunction.COUNT) to change its summary function from the default SUM to COUNT; the first data field remains Sum of Amount. Demonstrate that the setFunction setter can also be assigned ConsolidationFunction.AVERAGE, MAX, MIN, etc. Call pivotTable.refreshData() and pivotTable.calculateData() and save the workbook with workbook.save("output_function.xlsx"). -->

## **Plotting Value Fields to Row or Column Axis**

With two data fields in place, `PivotTable.getValuesField()` becomes usable. This scenario drags that aggregate virtual field onto the Column region so that every measure in the data region appears as its own column block next to `Year`.

<!-- CODE_BLOCK:2:Build a complete end-to-end sample that imports the Aspose.Cells namespace, then creates a new Workbook instance, gets worksheets.get(0), assigns worksheet.setName("Data"), and writes the same 4-column 9-row dataset (Category, Item, Year, Amount) using individual cells.get(i, j).putValue(...) calls for each cell, iterating row index i from 1 to 8 inclusive and column index j from 0 to 3 in nested loops, branching on j to pick the correct value, so A1:D1 contains the headers and A2:D9 contains the eight data rows. Add a pivot table by calling worksheet.getPivotTables().add("A1:D9", "F3", "PivotTable1"), place "Category" and "Item" on Row, place "Year" on Column, then call pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount") twice. Assign pivotTable.getDataFields().get(1).setFunction(ConsolidationFunction.COUNT) so the second data field becomes COUNT while the first remains SUM. Finally call pivotTable.addFieldToArea(PivotFieldType.COLUMN, pivotTable.getValuesField().getName()) to plot the value fields onto the Column axis. Call pivotTable.refreshData() and pivotTable.calculateData() and save the workbook with workbook.save("output_plot.xlsx"). The final layout has Row region (Category, Item), Column region (Year + ValuesField), and Data region (Sum-of-Amount, Count-of-Amount). -->

Together, these three scenarios cover every aspect of value-field manipulation in Aspose.Cells for Node.js via Java, from a single data field with the default `SUM` to a multi-measure pivot in which the virtual `ValuesField` controls the layout on the Row or Column axis.

## Related Articles

- [Pivot Table Row and Column Fields in Aspose.Cells for Node.js via Java](/cells/nodejs-java/row-and-column-fields/)
- [Page Fields in Pivot Tables](/cells/nodejs-java/add-page-field-in-pivot-table/)
- [Refreshing Pivot Tables in Aspose.Cells for Node.js via Java](/cells/nodejs-java/refresh-pivot-table/)
- [Applying Styles to Pivot Tables](/cells/nodejs-java/apply-style-to-pivot-table/)

{{< app/cells/assistant language="javascript" >}}