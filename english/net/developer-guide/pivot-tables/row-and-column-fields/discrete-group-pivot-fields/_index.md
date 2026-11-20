---
title: Discrete Grouping of Pivot Field Items
description: Learn how to group pivot field items into custom named groups such as fruit and vegetables using DiscreteGroupItem and PivotFieldGroupOptions.DiscreteGroupItems in Aspose.Cells for .NET.
linktitle: Discrete Grouping
keywords: Aspose.Cells, pivot table, discrete grouping, DiscreteGroupItem, PivotFieldGroupOptions, group pivot items, custom groups, PivotField.Group, C#, Excel pivot table
type: docs
weight: 90
url: /net/discrete-group-pivot-fields/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**
- Automatic grouping collects items by data type, such as dates into months and quarters or numbers into ranges. Discrete grouping solves the opposite problem, collecting specific, unrelated items into custom named groups, for example products into fruit and vegetables, stores into regions, or accounts into zones. Aspose.Cells provides discrete grouping through the `DiscreteGroupItem` class and the `PivotFieldGroupOptions.DiscreteGroupItems` property.
- A `DiscreteGroupItem` is a group name plus the items that belong to it. The items can be identified in two ways, by their names (`new DiscreteGroupItem("fruit", new string[] { "grape", "cherry" })`) or by their zero-based positions in the source data (`new DiscreteGroupItem("fruit", new int[] { 0, 3 })`). Both forms produce the same result.
- Discrete grouping is applied to a field in the row or column area of the pivot table by passing the options to `PivotField.Group(PivotFieldGroupOptions)`.

## **Group Pivot Field Items by Item Names**
The following example builds a small sales list (product, date and amount), creates a pivot table from it with `product` in the row area, `date` in the column area and `amount` in the data area, then defines two custom groups by item names, fruit (grape, cherry) and vegetables (carrot, potato). The result shows a two-level row layout, the group name as the outer level and the original items nested underneath, so trends can be read per custom group and per item.

```csharp
using Aspose.Cells;
using Aspose.Cells.Pivot;
Workbook wb = new Workbook();
Worksheet sheet = wb.Worksheets[0];
Cells cells = sheet.Cells;
cells[0, 0].Value = "product";
cells[1, 0].Value = "grape";
cells[2, 0].Value = "carrot";
cells[3, 0].Value = "potato";
cells[4, 0].Value = "cherry";
Style dateStyle = wb.CreateStyle();
dateStyle.Custom = "m/d/yyyy";
cells[0, 1].Value = "date";
cells[1, 1].Value = new DateTime(2021, 2, 5);
cells[2, 1].Value = new DateTime(2022, 3, 8);
cells[3, 1].Value = new DateTime(2023, 4, 10);
cells[4, 1].Value = new DateTime(2024, 5, 16);
for (int r = 1; r <= 4; r++) cells[r, 1].SetStyle(dateStyle);
cells[0, 2].Value = "amount";
cells[1, 2].Value = 50;
cells[2, 2].Value = 60;
cells[3, 2].Value = 70;
cells[4, 2].Value = 80;
// Add a pivot table with the destination cell A12 (row 11, column 0)
PivotTable pivotTable = sheet.PivotTables.Add("=Sheet1!A1:C5", 11, 0);
pivotTable.AddFieldToArea(PivotFieldType.Row, "product");
pivotTable.AddFieldToArea(PivotFieldType.Column, "date");
pivotTable.AddFieldToArea(PivotFieldType.Data, "amount");
pivotTable.PivotTableStyleType = PivotTableStyleType.PivotTableStyleMedium10;
// Group specific items into custom groups by item names
DiscreteGroupItem fruit = new DiscreteGroupItem("fruit", new string[] { "grape", "cherry" });
DiscreteGroupItem vegetable = new DiscreteGroupItem("vegetable", new string[] { "carrot", "potato" });
PivotFieldGroupOptions groupOptions = new PivotFieldGroupOptions();
groupOptions.DiscreteGroupItems = new DiscreteGroupItem[] { fruit, vegetable };
pivotTable.RowFields[0].Group(groupOptions);
pivotTable.CalculateData();
wb.Save("outputDiscreteGroupPivotField.xlsx");
```

After `CalculateData()` the row area of the pivot table shows fruit (grape 50, cherry 80) and vegetable (carrot 60, potato 70) with the grand total 260, and the column labels keep the four dates (2/5/2021, 3/8/2022, 4/10/2023, 5/16/2024).

## **Group Pivot Field Items by Item Indices**
When the item names are long or localized, the second constructor of `DiscreteGroupItem` identifies the items by index. The indices are zero-based positions of the items in the order they appear in the source data, not alphabetical order. In the sample data above grape is item 0, carrot is item 1, potato is item 2 and cherry is item 3, so fruit is `{ 0, 3 }` and vegetable is `{ 1, 2 }`. The result is identical to the name-based example.

```csharp
using Aspose.Cells;
using Aspose.Cells.Pivot;
Workbook wb = new Workbook();
Worksheet sheet = wb.Worksheets[0];
Cells cells = sheet.Cells;
cells[0, 0].Value = "product";
cells[1, 0].Value = "grape";
cells[2, 0].Value = "carrot";
cells[3, 0].Value = "potato";
cells[4, 0].Value = "cherry";
Style dateStyle = wb.CreateStyle();
dateStyle.Custom = "m/d/yyyy";
cells[0, 1].Value = "date";
cells[1, 1].Value = new DateTime(2021, 2, 5);
cells[2, 1].Value = new DateTime(2022, 3, 8);
cells[3, 1].Value = new DateTime(2023, 4, 10);
cells[4, 1].Value = new DateTime(2024, 5, 16);
for (int r = 1; r <= 4; r++) cells[r, 1].SetStyle(dateStyle);
cells[0, 2].Value = "amount";
cells[1, 2].Value = 50;
cells[2, 2].Value = 60;
cells[3, 2].Value = 70;
cells[4, 2].Value = 80;
// Add a pivot table with the destination cell A12 (row 11, column 0)
PivotTable pivotTable = sheet.PivotTables.Add("=Sheet1!A1:C5", 11, 0);
pivotTable.AddFieldToArea(PivotFieldType.Row, "product");
pivotTable.AddFieldToArea(PivotFieldType.Column, "date");
pivotTable.AddFieldToArea(PivotFieldType.Data, "amount");
pivotTable.PivotTableStyleType = PivotTableStyleType.PivotTableStyleMedium10;
// grape is item 0, carrot is item 1, potato is item 2, cherry is item 3
// (zero-based positions in the order the items appear in the source data)
DiscreteGroupItem fruit = new DiscreteGroupItem("fruit", new int[] { 0, 3 });
DiscreteGroupItem vegetable = new DiscreteGroupItem("vegetable", new int[] { 1, 2 });
PivotFieldGroupOptions groupOptions = new PivotFieldGroupOptions();
groupOptions.DiscreteGroupItems = new DiscreteGroupItem[] { fruit, vegetable };
pivotTable.RowFields[0].Group(groupOptions);
pivotTable.CalculateData();
wb.Save("outputDiscreteGroupPivotFieldByIndex.xlsx");
```

## **Note**

{{% alert color="primary" %}}
- Items that are not assigned to any custom group are not lost. They stay in the pivot table at the same level as the custom groups, each as its own single-item entry. In the example above, defining only the fruit group leaves carrot and potato in the row area as standalone entries next to the fruit group.
- The `PivotFieldGroupOptions.NewPivotField` property controls the layout of discrete grouping. It defaults to true, which adds the grouped field as a new outer field beside the original one, producing the two-level layout shown above (`RowFields` grows to 2). Set it to false to replace the original field instead, the row area then shows a single level containing only the group names with their aggregated values, fruit 130 (50 + 80) and vegetable 130 (60 + 70).
- The name-based and index-based constructors of `DiscreteGroupItem` can be mixed within the same `DiscreteGroupItems` array.
{{% /alert %}}

## **Related Articles**
- [Group Pivot Fields in the Pivot Table](/cells/net/group-pivot-fields-in-the-pivot-table/)
- [Add Row and Column Fields in Pivot Table](/cells/net/pivot-table-add-row-and-column-fields/)
- [Filtering Pivot Tables by Label or Value](/cells/net/filter-by-label-or-value-of-pivot-table/)
- [Apply Style to Pivot Table](/cells/net/apply-style-to-pivot-table/)
- [Refresh Pivot Table](/cells/net/refresh-pivot-table/)

{{< app/cells/assistant language="csharp" >}}