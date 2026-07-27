---
title: Value Fields in Aspose.Cells for Node.js via C++
linktitle: Value Fields
description: Learn how to add base fields to the data region of a pivot table, change the summary function with PivotField.Function, and plot the value field onto the Row or Column axis in Aspose.Cells for Node.js via C++.
keywords: Aspose.Cells, Node.js, C++, pivot table, value field, PivotField, PivotField.Function, data field, PivotTable.ValuesField, Sum, Average
type: docs
weight: 230
url: /nodejs-cpp/manage-value-fields/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

Value fields are the heart of every pivot table, the numeric aggregates that summarise the source data. In Aspose.Cells for Node.js via C++, the data region of a pivot table is populated by adding base fields to it through `PivotTable.addFieldToArea`, and each field placed in that region can have its own summary function. When two or more data fields exist, Aspose.Cells exposes a special aggregate field, `PivotTable.ValuesField`, that can be plotted onto the Row or Column axis as a base field, giving you finer control over how value fields appear in the layout.

## Adding a Field to the Data Region

Adding a base field to the data (value) region is the first step in shaping how a pivot table aggregates your source data. Aspose.Cells exposes `PivotTable.addFieldToArea(PivotFieldType, string)`, an overload that accepts the constant `PivotFieldType.Data` and the source-column name. Once a field is added to the data region, the API exposes it through the `PivotTable.DataFields` collection, in the order in which the fields were added. By default, a numeric source column is summarised with `ConsolidationFunction.Sum`, while a non-numeric column defaults to `Count`.

## Changing the Summary Function

Every field placed in the data region is wrapped internally as a `PivotField` instance, and its `Function` property returns a value from the `ConsolidationFunction` enum. The same `Function` setter lets you switch between the available aggregates, including `Sum`, `Count`, `Average`, `Max`, `Min`, `Product`, `StdDev`, `StdDevp`, `Var`, and `Varp`.

{{% alert color="primary" %}}
Changing `Function` only affects the aggregate, the source column does not change.
{{% /alert %}}

You can therefore leave one data field as `Sum` while you add a second data field that targets the same source column but uses `Count` or `Average`, all in a single pivot.

## Plotting Value Fields to Row or Column Axis

When a pivot table contains two or more data fields, Aspose.Cells exposes an additional virtual field called `PivotTable.ValuesField`. This virtual field represents the aggregate of every data field that lives in the data region. You can drag it into the Row or Column region as a base pivot field, which is useful for laying out multiple measures side by side.

{{% alert color="primary" %}}
`PivotTable.ValuesField` does not work if there is no or only one value field.
{{% /alert %}}

The scenarios below walk through three end-to-end examples that demonstrate each capability described above against the same pivot structure.

## Scenario 1 — Dragging a Base Field into the Value Region

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

## Scenario 2 — Changing the Summary Function

This scenario starts from the same pivot structure as Scenario 1 but adds the `Amount` field to the data region twice. Both data fields reference the same source column, however the second field is overridden using the `PivotField.Function` setter so that it becomes `Count` instead of the default `Sum`.

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Data");

worksheet.getCells().get(0, 0).putValue("Category");
worksheet.getCells().get(0, 1).putValue("Item");
worksheet.getCells().get(0, 2).putValue("Year");
worksheet.getCells().get(0, 3).putValue("Amount");

for (let i = 1; i <= 8; i++)
{
    for (let j = 0; j <= 3; j++)
    {
        if (j == 0)
        {
            worksheet.getCells().get(i, j).putValue(i <= 5 ? "Fruit" : "Vegetable");
        }
        else if (j == 1)
        {
            let items = ["Apple", "Apple", "Banana", "Banana", "Carrot", "Carrot", "Daikon", "Daikon"];
            worksheet.getCells().get(i, j).putValue(items[i - 1]);
        }
        else if (j == 2)
        {
            let years = [2020, 2021, 2020, 2021, 2020, 2021, 2020, 2021];
            worksheet.getCells().get(i, j).putValue(years[i - 1]);
        }
        else
        {
            let amounts = [100, 150, 80, 90, 50, 60, 40, 45];
            worksheet.getCells().get(i, j).putValue(amounts[i - 1]);
        }
    }
}

let pivotIndex = worksheet.getPivotTables().add("A1:D9", "F3", "PivotTable1");
let pivotTable = worksheet.getPivotTables().get(pivotIndex);

pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Category");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Item");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");

pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

let countField = pivotTable.getDataFields().get(1);
countField.setFunction(AsposeCells.ConsolidationFunction.Count);

pivotTable.refreshData();
pivotTable.calculateData();

workbook.save("output_function.xlsx");
```

## Scenario 3 — Plotting Value Fields to Row or Column Axis

With two data fields in place, `PivotTable.ValuesField` becomes usable. This scenario drags that aggregate virtual field onto the Column region so that every measure in the data region appears as its own column block next to `Year`.

<!-- CODE_BLOCK:2:Build a complete end-to-end sample that starts with a require statement to load the Aspose.Cells Node.js module, then creates a Workbook instance, calls workbook.getWorksheets().get(0) to obtain the first worksheet, assigns worksheet.setName("Data"), and writes the same 4-column 9-row dataset (Category, Item, Year, Amount) using individual worksheet.getCells().get(i, j).putValue(...) calls for each cell, iterating row index i from 1 to 8 inclusive and column index j from 0 to 3 in nested loops, branching on j to pick the correct value, so A1:D1 contains the headers and A2:D9 contains the eight data rows. Add a pivot table by calling worksheet.getPivotTables().add("A1:D9", "F3", "PivotTable1"), place "Category" and "Item" on Row, place "Year" on Column, then call pivotTable.addFieldToArea(PivotFieldType.Data, "Amount") twice. Assign pivotTable.getDataFields().get(1).setFunction(ConsolidationFunction.Count) so the second data field becomes Count while the first remains Sum. Finally call pivotTable.addFieldToArea(PivotFieldType.Column, pivotTable.getValuesField().getName()) to plot the value fields onto the Column axis. Call pivotTable.refreshData() and pivotTable.calculateData() and save the workbook with workbook.save("output_plot.xlsx"). The final layout has Row region (Category, Item), Column region (Year + ValuesField), and Data region (Sum-of-Amount, Count-of-Amount). -->

Together, these three scenarios cover every aspect of value-field manipulation in Aspose.Cells for Node.js via C++, from a single data field with the default `Sum` to a multi-measure pivot in which the virtual `ValuesField` controls the layout on the Row or Column axis.

## Related Articles

- [Pivot Table Row and Column Fields in Aspose.Cells for Node.js via C++](/cells/nodejs-cpp/row-and-column-fields/)
- [Page Fields in Pivot Tables](/cells/nodejs-cpp/add-page-field-in-pivot-table/)
- [Refreshing Pivot Tables in Aspose.Cells for Node.js via C++](/cells/nodejs-cpp/refresh-pivot-table/)
- [Applying Styles to Pivot Tables](/cells/nodejs-cpp/apply-style-to-pivot-table/)

{{< app/cells/assistant language="javascript" >}}