---
title: Discrete Grouping of Pivot Field Items
description: Learn how to group pivot field items into custom named groups such as fruit and vegetables using DiscreteGroupItem and PivotFieldGroupOptions.DiscreteGroupItems in Aspose.Cells for C++.
linktitle: Discrete Grouping
keywords: Aspose.Cells for C++, pivot table, discrete grouping, DiscreteGroupItem, PivotFieldGroupOptions, group pivot items, custom groups, PivotField.Group, C++, Excel pivot table
type: docs
weight: 90
url: /cpp/discrete-group-pivot-fields/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**
- Automatic grouping collects items by data type, such as dates into months and quarters or numbers into ranges. Discrete grouping solves the opposite problem, collecting specific, unrelated items into custom named groups, for example products into fruit and vegetables, stores into regions, or accounts into zones. Aspose.Cells provides discrete grouping through the `DiscreteGroupItem` class and the `PivotFieldGroupOptions.DiscreteGroupItems` property.
- A `DiscreteGroupItem` is a group name plus the items that belong to it. The items can be identified in two ways, by their names (`DiscreteGroupItem("fruit", { "grape", "cherry" })`) or by their zero-based positions in the source data (`DiscreteGroupItem("fruit", { 0, 3 })`). Both forms produce the same result.
- Discrete grouping is applied to a field in the row or column area of the pivot table by passing the options to `PivotField.Group(PivotFieldGroupOptions)`.

## **Group Pivot Field Items by Item Names**
The following example builds a small sales list (product, date and amount), creates a pivot table from it with `product` in the row area, `date` in the column area and `amount` in the data area, then defines two custom groups by item names, fruit (grape, cherry) and vegetables (carrot, potato). The result shows a two-level row layout, the group name as the outer level and the original items nested underneath, so trends can be read per custom group and per item.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    Workbook wb;
    Worksheet sheet = wb.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();
    cells.Get(0, 0).PutValue(u"product");
    cells.Get(1, 0).PutValue(u"grape");
    cells.Get(2, 0).PutValue(u"carrot");
    cells.Get(3, 0).PutValue(u"potato");
    cells.Get(4, 0).PutValue(u"cherry");
    Style dateStyle = wb.CreateStyle();
    dateStyle.SetCustom(u"m/d/yyyy");
    cells.Get(0, 1).PutValue(u"date");
    cells.Get(1, 1).PutValue(Date{2021, 2, 5, 0, 0, 0, 0});
    cells.Get(2, 1).PutValue(Date{2022, 3, 8, 0, 0, 0, 0});
    cells.Get(3, 1).PutValue(Date{2023, 4, 10, 0, 0, 0, 0});
    cells.Get(4, 1).PutValue(Date{2024, 5, 16, 0, 0, 0, 0});
    for (int r = 1; r <= 4; ++r) {
        cells.Get(r, 1).SetStyle(dateStyle);
    }
    cells.Get(0, 2).PutValue(u"amount");
    cells.Get(1, 2).PutValue(50);
    cells.Get(2, 2).PutValue(60);
    cells.Get(3, 2).PutValue(70);
    cells.Get(4, 2).PutValue(80);
    PivotTable pivotTable = sheet.GetPivotTables().Add(u"=Sheet1!A1:C5", 11, 0);
    pivotTable.AddFieldToArea(PivotFieldType::Row, U16String(u"product"));
    pivotTable.AddFieldToArea(PivotFieldType::Column, U16String(u"date"));
    pivotTable.AddFieldToArea(PivotFieldType::Data, U16String(u"amount"));
    pivotTable.SetPivotTableStyleType(PivotTableStyleType::PivotTableStyleMedium10);
    DiscreteGroupItem fruit(u"fruit", Vector<U16String>{u"grape", u"cherry"});
    DiscreteGroupItem vegetable(u"vegetable", Vector<U16String>{u"carrot", u"potato"});
    PivotFieldGroupOptions groupOptions;
    groupOptions.SetDiscreteGroupItems(Vector<DiscreteGroupItem>{fruit, vegetable});
    pivotTable.GetRowFields().Get(0).Group(groupOptions);
    pivotTable.CalculateData();
    wb.Save(u"outputDiscreteGroupPivotField.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

After `CalculateData()` the row area of the pivot table shows fruit (grape 50, cherry 80) and vegetable (carrot 60, potato 70) with the grand total 260, and the column labels keep the four dates (2/5/2021, 3/8/2022, 4/10/2023, 5/16/2024).

## **Group Pivot Field Items by Item Indices**
When the item names are long or localized, the second constructor of `DiscreteGroupItem` identifies the items by index. The indices are zero-based positions of the items in the order they appear in the source data, not alphabetical order. In the sample data above grape is item 0, carrot is item 1, potato is item 2 and cherry is item 3, so fruit is `{ 0, 3 }` and vegetable is `{ 1, 2 }`. The result is identical to the name-based example.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    Workbook wb;
    Worksheet sheet = wb.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();
    cells.Get(0, 0).PutValue(u"product");
    cells.Get(1, 0).PutValue(u"grape");
    cells.Get(2, 0).PutValue(u"carrot");
    cells.Get(3, 0).PutValue(u"potato");
    cells.Get(4, 0).PutValue(u"cherry");
    Style dateStyle = wb.CreateStyle();
    dateStyle.SetCustom(u"m/d/yyyy");
    cells.Get(0, 1).PutValue(u"date");
    Date firstDate{2021, 2, 5, 0, 0, 0, 0};
    Date secondDate{2022, 3, 8, 0, 0, 0, 0};
    Date thirdDate{2023, 4, 10, 0, 0, 0, 0};
    Date fourthDate{2024, 5, 16, 0, 0, 0, 0};
    cells.Get(1, 1).PutValue(firstDate);
    cells.Get(2, 1).PutValue(secondDate);
    cells.Get(3, 1).PutValue(thirdDate);
    cells.Get(4, 1).PutValue(fourthDate);
    for (int r = 1; r <= 4; ++r) {
        cells.Get(r, 1).SetStyle(dateStyle);
    }
    cells.Get(0, 2).PutValue(u"amount");
    cells.Get(1, 2).PutValue(50);
    cells.Get(2, 2).PutValue(60);
    cells.Get(3, 2).PutValue(70);
    cells.Get(4, 2).PutValue(80);
    PivotTable pivotTable = sheet.GetPivotTables().Add(u"=Sheet1!A1:C5", 11, 0);
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"product");
    pivotTable.AddFieldToArea(PivotFieldType::Column, u"date");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"amount");
    pivotTable.SetPivotTableStyleType(PivotTableStyleType::PivotTableStyleMedium10);
    DiscreteGroupItem fruit(u"fruit", Vector<int32_t>{0, 3});
    DiscreteGroupItem vegetable(u"vegetable", Vector<int32_t>{1, 2});
    PivotFieldGroupOptions groupOptions;
    groupOptions.SetDiscreteGroupItems(Vector<DiscreteGroupItem>{fruit, vegetable});
    pivotTable.GetRowFields().Get(0).Group(groupOptions);
    pivotTable.CalculateData();
    wb.Save(u"outputDiscreteGroupPivotFieldByIndex.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Note**

{{% alert color="primary" %}}
- Items that are not assigned to any custom group are not lost. They stay in the pivot table at the same level as the custom groups, each as its own single-item entry. In the example above, defining only the fruit group leaves carrot and potato in the row area as standalone entries next to the fruit group.
- The `PivotFieldGroupOptions.NewPivotField` property controls the layout of discrete grouping. It defaults to true, which adds the grouped field as a new outer field beside the original one, producing the two-level layout shown above (`RowFields` grows to 2). Set it to false to replace the original field instead, the row area then shows a single level containing only the group names with their aggregated values, fruit 130 (50 + 80) and vegetable 130 (60 + 70).
- The name-based and index-based constructors of `DiscreteGroupItem` can be mixed within the same `DiscreteGroupItems` collection.
{{% /alert %}}

## **Related Articles**
- [Group Pivot Fields in the Pivot Table](/cells/cpp/group-pivot-fields-in-the-pivot-table/)
- [Add Row and Column Fields in Pivot Table](/cells/cpp/pivot-table-add-row-and-column-fields/)
- [Filtering Pivot Tables by Label or Value](/cells/cpp/filter-by-label-or-value-of-pivot-table/)
- [Apply Style to Pivot Table](/cells/cpp/apply-style-to-pivot-table/)
- [Refresh Pivot Table](/cells/cpp/refresh-pivot-table/)

{{< app/cells/assistant language="cpp" >}}