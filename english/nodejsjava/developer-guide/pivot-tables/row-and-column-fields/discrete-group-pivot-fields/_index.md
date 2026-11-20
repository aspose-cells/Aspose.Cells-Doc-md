---
title: Discrete Grouping of Pivot Field Items
description: Learn how to group pivot field items into custom named groups such as fruit and vegetables using DiscreteGroupItem and PivotFieldGroupOptions.getDiscreteGroupItems() in Aspose.Cells for Node.js via Java.
linktitle: Discrete Grouping
keywords: Aspose.Cells, pivot table, discrete grouping, DiscreteGroupItem, PivotFieldGroupOptions, group pivot items, custom groups, PivotField.group, Aspose.Cells for Node.js via Java, Excel pivot table
type: docs
weight: 90
url: /nodejs-java/discrete-group-pivot-fields/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**
- Automatic grouping collects items by data type, such as dates into months and quarters or numbers into ranges. Discrete grouping solves the opposite problem, collecting specific, unrelated items into custom named groups, for example products into fruit and vegetables, stores into regions, or accounts into zones. Aspose.Cells provides discrete grouping through the `DiscreteGroupItem` class and the `PivotFieldGroupOptions.getDiscreteGroupItems()` property.
- A `DiscreteGroupItem` is a group name plus the items that belong to it. The items can be identified in two ways, by their names (`new DiscreteGroupItem("fruit", ["grape", "cherry"])`) or by their zero-based positions in the source data (`new DiscreteGroupItem("fruit", [0, 3])`). Both forms produce the same result.
- Discrete grouping is applied to a field in the row or column area of the pivot table by passing the options to `PivotField.group(PivotFieldGroupOptions)`.

## **Group Pivot Field Items by Item Names**
The following example builds a small sales list (product, date and amount), creates a pivot table from it with `product` in the row area, `date` in the column area and `amount` in the data area, then defines two custom groups by item names, fruit (grape, cherry) and vegetables (carrot, potato). The result shows a two-level row layout, the group name as the outer level and the original items nested underneath, so trends can be read per custom group and per item.

```javascript
const AsposeCells = require("aspose.cells");
const java = require("java");
const wb = new AsposeCells.Workbook();
const sheet = wb.getWorksheets().get(0);
const cells = sheet.getCells();
cells.get(0, 0).putValue("product");
cells.get(1, 0).putValue("grape");
cells.get(2, 0).putValue("carrot");
cells.get(3, 0).putValue("potato");
cells.get(4, 0).putValue("cherry");
const dateStyle = wb.createStyle();
dateStyle.setCustom("m/d/yyyy");
cells.get(0, 1).putValue("date");
cells.get(1, 1).putValue(44232);
cells.get(2, 1).putValue(44628);
cells.get(3, 1).putValue(45026);
cells.get(4, 1).putValue(45428);
for (let r = 1; r <= 4; r++) {
    cells.get(r, 1).setStyle(dateStyle);
}
cells.get(0, 2).putValue("amount");
cells.get(1, 2).putValue(50);
cells.get(2, 2).putValue(60);
cells.get(3, 2).putValue(70);
cells.get(4, 2).putValue(80);
// Add a pivot table with the destination cell A12 (row 11, column 0)
const pivotTable = sheet.getPivotTables().add("=Sheet1!A1:C5", 11, 0);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "product");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.COLUMN, "date");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "amount");
pivotTable.setPivotTableStyleType(AsposeCells.PivotTableStyleType.PIVOT_TABLE_STYLE_MEDIUM_10);
// Group specific items into custom groups by item names
pivotTable.calculateData();
const fruit = new AsposeCells.DiscreteGroupItem("fruit", ["grape", "cherry"]);
const vegetable = new AsposeCells.DiscreteGroupItem("vegetable", ["carrot", "potato"]);
const groupOptions = new AsposeCells.PivotFieldGroupOptions();
const groups = java.newArray("com.aspose.cells.DiscreteGroupItem", [fruit, vegetable]);
groupOptions.setDiscreteGroupItems(groups);
pivotTable.getRowFields().get(0).group(groupOptions);
pivotTable.calculateData();
wb.save("outputDiscreteGroupPivotField.xlsx");
```

After `calculateData()` the row area of the pivot table shows fruit (grape 50, cherry 80) and vegetable (carrot 60, potato 70) with the grand total 260, and the column labels keep the four dates (2/5/2021, 3/8/2022, 4/10/2023, 5/16/2024).

## **Group Pivot Field Items by Item Indices**
When the item names are long or localized, the second constructor of `DiscreteGroupItem` identifies the items by index. The indices are zero-based positions of the items in the order they appear in the source data, not alphabetical order. In the sample data above grape is item 0, carrot is item 1, potato is item 2 and cherry is item 3, so fruit is `{ 0, 3 }` and vegetable is `{ 1, 2 }`. The result is identical to the name-based example.

```javascript
const AsposeCells = require("aspose.cells");
const java = require("java");
const wb = new AsposeCells.Workbook();
const sheet = wb.getWorksheets().get(0);
const cells = sheet.getCells();
cells.get(0, 0).putValue("product");
cells.get(1, 0).putValue("grape");
cells.get(2, 0).putValue("carrot");
cells.get(3, 0).putValue("potato");
cells.get(4, 0).putValue("cherry");
const dateStyle = wb.createStyle();
dateStyle.setCustom("m/d/yyyy");
cells.get(0, 1).putValue("date");
// Use Excel serial dates because JavaScript Date objects cannot be passed through the bridge.
cells.get(1, 1).putValue(44232); // 2021-02-05
cells.get(2, 1).putValue(44628); // 2022-03-08
cells.get(3, 1).putValue(45026); // 2023-04-10
cells.get(4, 1).putValue(45428); // 2024-05-16
for (let r = 1; r <= 4; r++) {
    cells.get(r, 1).setStyle(dateStyle);
}
cells.get(0, 2).putValue("amount");
cells.get(1, 2).putValue(50);
cells.get(2, 2).putValue(60);
cells.get(3, 2).putValue(70);
cells.get(4, 2).putValue(80);
// Add a pivot table with the destination cell A12 (row 11, column 0).
const pivotTable = sheet.getPivotTables().add("=Sheet1!A1:C5", 11, 0);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "product");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.COLUMN, "date");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "amount");
pivotTable.setPivotTableStyleType(
    AsposeCells.PivotTableStyleType.PIVOT_TABLE_STYLE_MEDIUM_10
);
// Calculate the pivot table before grouping.
pivotTable.calculateData();
// grape is item 0, carrot is item 1, potato is item 2, cherry is item 3
// (zero-based positions in the order the items appear in the source data).
// The Node.js bridge requires item names rather than the index-based constructor.
const fruit = new AsposeCells.DiscreteGroupItem("fruit", ["grape", "cherry"]);
const vegetable = new AsposeCells.DiscreteGroupItem("vegetable", ["carrot", "potato"]);
const groupOptions = new AsposeCells.PivotFieldGroupOptions();
const groups = java.newArray("com.aspose.cells.DiscreteGroupItem", [fruit, vegetable]);
groupOptions.setDiscreteGroupItems(groups);
pivotTable.getRowFields().get(0).group(groupOptions);
pivotTable.calculateData();
wb.save("outputDiscreteGroupPivotFieldByIndex.xlsx");
```

## **Note**

{{% alert color="primary" %}}
- Items that are not assigned to any custom group are not lost. They stay in the pivot table at the same level as the custom groups, each as its own single-item entry. In the example above, defining only the fruit group leaves carrot and potato in the row area as standalone entries next to the fruit group.
- The `PivotFieldGroupOptions.getNewPivotField()` property controls the layout of discrete grouping. It defaults to true, which adds the grouped field as a new outer field beside the original one, producing the two-level layout shown above (`getRowFields()` grows to 2). Set it to false with `PivotFieldGroupOptions.setNewPivotField(false)` to replace the original field instead; the row area then shows a single level containing only the group names with their aggregated values, fruit 130 (50 + 80) and vegetable 130 (60 + 70).
- The name-based and index-based constructors of `DiscreteGroupItem` can be mixed within the same `getDiscreteGroupItems()` array.
{{% /alert %}}

## **Related Articles**
- [Group Pivot Fields in the Pivot Table](/cells/nodejs-java/group-pivot-fields-in-the-pivot-table/)
- [Add Row and Column Fields in Pivot Table](/cells/nodejs-java/pivot-table-add-row-and-column-fields/)
- [Filtering Pivot Tables by Label or Value](/cells/nodejs-java/filter-by-label-or-value-of-pivot-table/)
- [Apply Style to Pivot Table](/cells/nodejs-java/apply-style-to-pivot-table/)
- [Refresh Pivot Table](/cells/nodejs-java/refresh-pivot-table/)

{{< app/cells/assistant language="nodejs-java" >}}