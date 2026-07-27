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


## Adding a Field to the Data Region

Adding a base field to the data (value) region is the first step in shaping how a pivot table aggregates your source data. Aspose.Cells exposes `PivotTable.addFieldToArea(PivotFieldType, string)`, an overload that accepts the constant `PivotFieldType.DATA` and the source-column name. Once a field is added to the data region, the API exposes it through the `PivotTable.getDataFields()` collection, in the order in which the fields were added. By default, a numeric source column is summarised with `ConsolidationFunction.SUM`, while a non-numeric column defaults to `COUNT`.

## Changing the Summary Function

{{% alert color="primary" %}}
Changing `Function` only affects the aggregate, the source column does not change.
{{% /alert %}}

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

pivotTable.calculateData();
workbook.save("output_drag.xlsx");
```

## **Changing the Summary Function**

## **Plotting Value Fields to Row or Column Axis**

With two data fields in place, `PivotTable.getValuesField()` becomes usable. This scenario drags that aggregate virtual field onto the Column region so that every measure in the data region appears as its own column block next to `Year`.

Together, these three scenarios cover every aspect of value-field manipulation in Aspose.Cells for Node.js via Java, from a single data field with the default `SUM` to a multi-measure pivot in which the virtual `ValuesField` controls the layout on the Row or Column axis.

{{< app/cells/assistant language="javascript" >}}
