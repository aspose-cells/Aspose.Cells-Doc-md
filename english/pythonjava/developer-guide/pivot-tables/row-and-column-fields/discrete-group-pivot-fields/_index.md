---
title: Discrete Grouping of Pivot Field Items
description: Learn how to group pivot field items into custom named groups such as fruit and vegetables using DiscreteGroupItem and PivotFieldGroupOptions.getDiscreteGroupItems in Aspose.Cells for Python via Java.
linktitle: Discrete Grouping
keywords: Aspose.Cells, pivot table, discrete grouping, DiscreteGroupItem, PivotFieldGroupOptions, group pivot items, custom groups, PivotField.group, Python via Java, Excel pivot table
type: docs
weight: 90
url: /python-java/discrete-group-pivot-fields/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**
- Automatic grouping collects items by data type, such as dates into months and quarters or numbers into ranges. Discrete grouping solves the opposite problem, collecting specific, unrelated items into custom named groups, for example products into fruit and vegetables, stores into regions, or accounts into zones. Aspose.Cells provides discrete grouping through the `DiscreteGroupItem` class and the `PivotFieldGroupOptions.getDiscreteGroupItems()` method.
- A `DiscreteGroupItem` is a group name plus the items that belong to it. The items can be identified in two ways, by their names (`DiscreteGroupItem("fruit", ["grape", "cherry"])`) or by their zero-based positions in the source data (`DiscreteGroupItem("fruit", [0, 3])`). Both forms produce the same result.
- Discrete grouping is applied to a field in the row or column area of the pivot table by passing the options to `PivotField.group(PivotFieldGroupOptions)`.

## **Group Pivot Field Items by Item Names**
The following example builds a small sales list (product, date and amount), creates a pivot table from it with `product` in the row area, `date` in the column area and `amount` in the data area, then defines two custom groups by item names, fruit (grape, cherry) and vegetables (carrot, potato). The result shows a two-level row layout, the group name as the outer level and the original items nested underneath, so trends can be read per custom group and per item.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import (
    Workbook,
    Worksheet,
    Cells,
    Range,
    SaveFormat,
    DiscreteGroupItem,
    PivotFieldGroupOptions,
    PivotFieldType,
    PivotTableStyleType,
)
GregorianCalendar = jpype.JPackage("java.util").GregorianCalendar
def create_date(year, month, day):
    calendar = GregorianCalendar(year, month - 1, day)
    return calendar.getTime()
wb = Workbook()
sheet = wb.getWorksheets().get(0)
cells = sheet.getCells()
cells.get(0, 0).putValue("product")
cells.get(1, 0).putValue("grape")
cells.get(2, 0).putValue("carrot")
cells.get(3, 0).putValue("potato")
cells.get(4, 0).putValue("cherry")
date_style = wb.createStyle()
date_style.setCustom("m/d/yyyy")
cells.get(0, 1).putValue("date")
cells.get(1, 1).putValue(create_date(2021, 2, 5))
cells.get(2, 1).putValue(create_date(2022, 3, 8))
cells.get(3, 1).putValue(create_date(2023, 4, 10))
cells.get(4, 1).putValue(create_date(2024, 5, 16))
for r in range(1, 5):
    cells.get(r, 1).setStyle(date_style)
cells.get(0, 2).putValue("amount")
cells.get(1, 2).putValue(50.0)
cells.get(2, 2).putValue(60.0)
cells.get(3, 2).putValue(70.0)
cells.get(4, 2).putValue(80.0)
# Add a pivot table with the destination cell A12 (row 11, column 0)
pivot_table = sheet.getPivotTables().add("=Sheet1!A1:C5", 11, 0)
pivot_table.addFieldToArea(PivotFieldType.ROW, "product")
pivot_table.addFieldToArea(PivotFieldType.COLUMN, "date")
pivot_table.addFieldToArea(PivotFieldType.DATA, "amount")
pivot_table.setPivotTableStyleType(
    PivotTableStyleType.PIVOT_TABLE_STYLE_MEDIUM_10
)
# Group specific items into custom groups by item names
fruit = DiscreteGroupItem("fruit", ["grape", "cherry"])
vegetable = DiscreteGroupItem("vegetable", ["carrot", "potato"])
group_options = PivotFieldGroupOptions()
group_options.setDiscreteGroupItems([fruit, vegetable])
pivot_table.calculateData()
pivot_table.getRowFields().get(0).group(group_options)
wb.save("outputDiscreteGroupPivotField.xlsx")
jpype.shutdownJVM()
```

After `calculateData()` the row area of the pivot table shows fruit (grape 50, cherry 80) and vegetable (carrot 60, potato 70) with the grand total 260, and the column labels keep the four dates (2/5/2021, 3/8/2022, 4/10/2023, 5/16/2024).

## **Group Pivot Field Items by Item Indices**
When the item names are long or localized, the second constructor of `DiscreteGroupItem` identifies the items by index. The indices are zero-based positions of the items in the order they appear in the source data, not alphabetical order. In the sample data above grape is item 0, carrot is item 1, potato is item 2 and cherry is item 3, so fruit is `{ 0, 3 }` and vegetable is `{ 1, 2 }`. The result is identical to the name-based example.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import (
    Workbook,
    PivotFieldType,
    PivotTableStyleType,
)
Date = jpype.JClass("java.util.Date")
DiscreteGroupItem = jpype.JClass("com.aspose.cells.DiscreteGroupItem")
PivotFieldGroupOptions = jpype.JClass("com.aspose.cells.PivotFieldGroupOptions")
wb = Workbook()
sheet = wb.getWorksheets().get(0)
cells = sheet.getCells()
cells.get(0, 0).putValue("product")
cells.get(1, 0).putValue("grape")
cells.get(2, 0).putValue("carrot")
cells.get(3, 0).putValue("potato")
cells.get(4, 0).putValue("cherry")
date_style = wb.createStyle()
date_style.setCustom("m/d/yyyy")
cells.get(0, 1).putValue("date")
cells.get(1, 1).putValue(Date(2021 - 1900, 2 - 1, 5))
cells.get(2, 1).putValue(Date(2022 - 1900, 3 - 1, 8))
cells.get(3, 1).putValue(Date(2023 - 1900, 4 - 1, 10))
cells.get(4, 1).putValue(Date(2024 - 1900, 5 - 1, 16))
for r in range(1, 5):
    cells.get(r, 1).setStyle(date_style)
cells.get(0, 2).putValue("amount")
cells.get(1, 2).putValue(50.0)
cells.get(2, 2).putValue(60.0)
cells.get(3, 2).putValue(70.0)
cells.get(4, 2).putValue(80.0)
pivot_table = sheet.getPivotTables().add("=Sheet1!A1:C5", 11, 0)
pivot_table.addFieldToArea(PivotFieldType.ROW, "product")
pivot_table.addFieldToArea(PivotFieldType.COLUMN, "date")
pivot_table.addFieldToArea(PivotFieldType.DATA, "amount")
pivot_table.setPivotTableStyleType(
    PivotTableStyleType.PIVOT_TABLE_STYLE_MEDIUM_10
)
pivot_table.calculateData()
fruit = DiscreteGroupItem("fruit", [0, 3])
vegetable = DiscreteGroupItem("vegetable", [1, 2])
group_options = PivotFieldGroupOptions()
group_options.setDiscreteGroupItems([fruit, vegetable])
pivot_table.getRowFields().get(0).group(group_options)
pivot_table.calculateData()
wb.save("outputDiscreteGroupPivotFieldByIndex.xlsx")
jpype.shutdownJVM()
```

## **Note**

{{% alert color="primary" %}}
- Items that are not assigned to any custom group are not lost. They stay in the pivot table at the same level as the custom groups, each as its own single-item entry. In the example above, defining only the fruit group leaves carrot and potato in the row area as standalone entries next to the fruit group.
- The `PivotFieldGroupOptions.getNewPivotField()` and `setNewPivotField()` methods control the layout of discrete grouping. `getNewPivotField()` defaults to true, which adds the grouped field as a new outer field beside the original one, producing the two-level layout shown above (`getRowFields()` grows to 2). Use `setNewPivotField(false)` to replace the original field instead; the row area then shows a single level containing only the group names with their aggregated values, fruit 130 (50 + 80) and vegetable 130 (60 + 70).
- The name-based and index-based constructors of `DiscreteGroupItem` can be mixed within the same `getDiscreteGroupItems()` collection.
{{% /alert %}}

## **Related Articles**
- [Group Pivot Fields in the Pivot Table](/cells/python-java/group-pivot-fields-in-the-pivot-table/)
- [Add Row and Column Fields in Pivot Table](/cells/python-java/pivot-table-add-row-and-column-fields/)
- [Filtering Pivot Tables by Label or Value](/cells/python-java/filter-by-label-or-value-of-pivot-table/)
- [Apply Style to Pivot Table](/cells/python-java/apply-style-to-pivot-table/)
- [Refresh Pivot Table](/cells/python-java/refresh-pivot-table/)

{{< app/cells/assistant language="python" >}}