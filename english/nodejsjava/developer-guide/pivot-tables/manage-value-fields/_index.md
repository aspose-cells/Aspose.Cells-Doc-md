---
title: Manage Pivot Table Value Fields in Aspose.Cells for .NET
linktitle: Value Fields
description: Learn how to add base fields to the data region of a pivot table, change the summary function with PivotField.Function, and plot the value field onto the Row or Column axis in Aspose.Cells for Node.js via Java.
keywords: Aspose.Cells, Node.js via Java, pivot table, value field, PivotField, PivotField.Function, data field, PivotTable.ValuesField, Sum, Average
type: docs
weight: 230
url: /nodejs-java/pivot-table-manage-value-fields/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---
Value fields are the heart of every pivot table — the numeric aggregates that summarise the source data. In Aspose.Cells, the data region of a pivot table is populated by adding base fields through `PivotTable.AddFieldToArea`, and each field placed in that region can have its own summary function. When two or more data fields exist, Aspose.Cells exposes a special aggregate field, `PivotTable.ValuesField`, that can be plotted onto the Row or Column axis as a base field, giving you finer control over how value fields appear in the layout.

## Adding a Field to the Data Region

Adding a base field to the data (value) region is the first step in shaping how a pivot table aggregates the source data. Aspose.Cells exposes `PivotTable.AddFieldToArea(PivotFieldType, string)`, an overload that accepts the constant `PivotFieldType.Data` and the source-column name. Once a field is added to the data region, the API exposes it through the `PivotTable.DataFields` collection, in the order in which the fields were added. By default, a numeric source column is summarised with `Sum`, while a non-numeric column defaults to `Count`.

```javascript
const AsposeCells = require("aspose.cells");

const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Data");

const headers = ["Category", "Item", "Year", "Amount"];
for (let j = 0; j < headers.length; j++) {
    worksheet.getCells().get(0, j).putValue(headers[j]);
}

const data = [
    ["Fruit",     "Apple",  2020, 100],
    ["Fruit",     "Apple",  2021, 150],
    ["Fruit",     "Banana", 2020,  80],
    ["Fruit",     "Banana", 2021,  90],
    ["Vegetable", "Carrot", 2020,  50],
    ["Vegetable", "Carrot", 2021,  60],
    ["Vegetable", "Daikon", 2020,  40],
    ["Vegetable", "Daikon", 2021,  45]
];
for (let i = 0; i < data.length; i++) {
    for (let j = 0; j < data[i].length; j++) {
        worksheet.getCells().get(i + 1, j).putValue(data[i][j]);
    }
}

const pivotIndex = worksheet.getPivotTables().add("A1:D9", "F3", "PivotTable1");
const pivotTable = worksheet.getPivotTables().get(pivotIndex);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Category");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Item");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

pivotTable.refreshData();
pivotTable.calculateData();
workbook.save("output_drag.xlsx");
```

## Changing the Summary Function

Every field placed in the data region is wrapped internally as a `PivotField` instance, and its `Function` property returns a value from the `ConsolidationFunction` enum. The same `Function` setter lets you switch between the available aggregates, including `Sum`, `Count`, `Average`, `Max`, `Min`, `Product`, `StdDev`, `StdDevp`, `Var`, and `Varp`.

{{% alert color="primary" %}}
Changing `Function` only affects the aggregate; the source column does not change. You can therefore leave one data field as `Sum` while a second data field targets the same source column but uses `Count` or `Average`, all in a single pivot.
{{% /alert %}}

```javascript
const AsposeCells = require("aspose.cells");

const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Data");

const headers = ["Category", "Item", "Year", "Amount"];
for (let j = 0; j < headers.length; j++) {
    worksheet.getCells().get(0, j).putValue(headers[j]);
}

const data = [
    ["Fruit",     "Apple",  2020, 100],
    ["Fruit",     "Apple",  2021, 150],
    ["Fruit",     "Banana", 2020,  80],
    ["Fruit",     "Banana", 2021,  90],
    ["Vegetable", "Carrot", 2020,  50],
    ["Vegetable", "Carrot", 2021,  60],
    ["Vegetable", "Daikon", 2020,  40],
    ["Vegetable", "Daikon", 2021,  45]
];
for (let i = 0; i < data.length; i++) {
    for (let j = 0; j < data[i].length; j++) {
        worksheet.getCells().get(i + 1, j).putValue(data[i][j]);
    }
}

const pivotIndex = worksheet.getPivotTables().add("A1:D9", "F3", "PivotTable1");
const pivotTable = worksheet.getPivotTables().get(pivotIndex);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Category");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Item");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.getDataFields().get(1).setFunction(AsposeCells.ConsolidationFunction.Count);

pivotTable.refreshData();
pivotTable.calculateData();
workbook.save("output_function.xlsx");
```

## Plotting Value Fields to Row or Column Axis

When a pivot table contains two or more data fields, Aspose.Cells exposes an additional virtual field called `PivotTable.ValuesField`. This virtual field represents the aggregate of every data field that lives in the data region. You can drag it into the Row or Column region as a base pivot field, which is useful for laying out multiple measures side by side.

{{% alert color="primary" %}}
`PivotTable.ValuesField` does not work if there is no or only one value field.
{{% /alert %}}

```javascript
const AsposeCells = require("aspose.cells");

const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Data");

const headers = ["Category", "Item", "Year", "Amount"];
for (let j = 0; j < headers.length; j++) {
    worksheet.getCells().get(0, j).putValue(headers[j]);
}

const data = [
    ["Fruit",     "Apple",  2020, 100],
    ["Fruit",     "Apple",  2021, 150],
    ["Fruit",     "Banana", 2020,  80],
    ["Fruit",     "Banana", 2021,  90],
    ["Vegetable", "Carrot", 2020,  50],
    ["Vegetable", "Carrot", 2021,  60],
    ["Vegetable", "Daikon", 2020,  40],
    ["Vegetable", "Daikon", 2021,  45]
];
for (let i = 0; i < data.length; i++) {
    for (let j = 0; j < data[i].length; j++) {
        worksheet.getCells().get(i + 1, j).putValue(data[i][j]);
    }
}

const pivotIndex = worksheet.getPivotTables().add("A1:D9", "F3", "PivotTable1");
const pivotTable = worksheet.getPivotTables().get(pivotIndex);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Category");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Item");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.getDataFields().get(1).setFunction(AsposeCells.ConsolidationFunction.Count);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, pivotTable.getValuesField().getName());

pivotTable.refreshData();
pivotTable.calculateData();
workbook.save("output_plot.xlsx");
```

## Related Articles

- [Add Pivot Table Row and Column Fields in Aspose.Cells for .NET](/cells/net/pivot-table-add-row-column-fields/)
- [Filter Fields in Pivot Tables](/cells/net/add-filter-field-in-pivot-table/)
- [Refreshing Pivot Tables in Aspose.Cells for .NET](/cells/net/refresh-pivot-table/)
- [Applying Styles to Pivot Tables](/cells/net/apply-style-to-pivot-table/)
{{< app/cells/assistant language="javascript" >}}
