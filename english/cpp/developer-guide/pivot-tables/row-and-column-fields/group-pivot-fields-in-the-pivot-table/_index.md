---
title: Group Pivot Fields in the Pivot Table
description: Learn how to group row and column pivot fields in a pivot table into date periods such as months and quarters and numeric ranges using PivotField.Group and PivotFieldGroupOptions in Aspose.Cells for C++.
linktitle: Group Pivot Fields
keywords: Aspose.Cells, pivot table, group pivot field, PivotField.Group, PivotFieldGroupOptions, date grouping, number grouping, months, quarters, numeric range, C++
type: docs
weight: 80
url: /cpp/group-pivot-fields-in-the-pivot-table/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**
- Grouping pivot fields is useful when a row or column field of a pivot table contains many distinct items, such as a date field with hundreds of dates or a numeric field with many scattered values. Grouping collapses these items into meaningful sections: dates into months, quarters and years, and numbers into ranges such as 0-1, 2-3, 4-5. This makes a large pivot table compact and easier to analyze. Aspose.Cells provides this capability through the `PivotField.Group()` method (automatic grouping by data type) and `PivotField.Group(PivotFieldGroupOptions)` (custom grouping options).
- Date grouping rolls the individual dates up into larger periods, such as days, months, quarters and years, and builds a time hierarchy (for example Years, Quarters, Months). Trends over time become visible at a glance, and each period level becomes its own pivot field in the row or column area of the pivot table.
- Grouping is available only for fields placed in the ROW or COLUMN area of a pivot table. A data (value) field cannot be grouped directly. To group such a field you must first add it to the row or column area of the pivot table.

## **Group Pivot Fields Automatically**
The parameterless `PivotField.Group()` overload inspects the data type of the field and groups it automatically. A field that contains only dates (and blanks) is grouped by months. A field that contains only numbers (and blanks) is grouped into numeric ranges using an automatic interval.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    Workbook wb(u"sampleGroupPivotFieldsInPivotTable.xlsx");
    Worksheet ws = wb.GetWorksheets().Get(1);
    PivotTable pt = ws.GetPivotTables().Get(0);
    PivotField field = pt.GetRowFields().Get(0);
    field.Group();
    pt.CalculateData();
    wb.Save(u"outputAutoGroupPivotField.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Group Pivot Fields with Custom Options**
The `PivotFieldGroupOptions` class provides custom grouping configuration. For date fields, set `StartDate`, `EndDate`, and `GroupTypes`. For numeric fields, set `StartNumber`, `EndNumber`, and `Interval`. The `NewPivotField` property controls whether grouping creates new pivot fields alongside the original (see the Note section at the end of this article).

### **Group a Date Field by Months and Quarters**
The following example groups the date row field of the sample pivot table by months and quarters between a start and end date. The code loads the [sample Excel file](sampleGroupPivotFieldsInPivotTable.xlsx), performs the grouping, calculates the pivot table data, and saves the grouped result. The screenshot shows the effect: the date row field is now grouped by quarters and months.
Note that the order of the values in `options.GroupTypes` is ignored. No matter in which order the group types are listed, the grouped fields are always displayed from the largest period to the smallest: years, quarters, months, days, hours, minutes, seconds. In this example the months are listed before the quarters in `options.GroupTypes`, yet the quarters are displayed as the outer level and the months as the inner level.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    // Load the sample workbook
    Workbook wb(u"sampleGroupPivotFieldsInPivotTable.xlsx");
    // Access the second worksheet and its pivot table
    Worksheet ws = wb.GetWorksheets().Get(1);
    PivotTable pt = ws.GetPivotTables().Get(0);
    // Group the first row field (a date field) by months and quarters
    PivotFieldGroupOptions options;
    Date startDate{2008, 1, 1, 0, 0, 0, 0};
    Date endDate{2008, 9, 5, 0, 0, 0, 0};
    options.SetStartDate(startDate);
    options.SetEndDate(endDate);
    // Set group types: Months and Quarters
    Vector<PivotGroupByType> groupTypes{ PivotGroupByType::Months, PivotGroupByType::Quarters };
    options.SetGroupTypes(groupTypes);
    // Apply grouping to the first row field
    PivotField rowField = pt.GetRowFields().Get(0);
    rowField.Group(options);
    // Calculate the pivot table data and save the output file
    pt.CalculateData();
    wb.Save(u"outputGroupPivotFieldsInPivotTable.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

![Pivot table grouped by months and quarters](group-pivot-fields-in-the-pivot-table_1.png)

### **Group a Numeric Field into Ranges**
`FieldTwo` of the sample pivot table is initially a data (value) field. Because only row or column fields can be grouped, the code first calls `PivotTable.AddFieldToArea(PivotFieldType.Row, "FieldTwo")` to move `FieldTwo` to the row area, refreshes the pivot, then groups the numeric field into the ranges 0-1, 2-3 and 4-5 using `StartNumber = 0`, `EndNumber = 5` and `Interval = 2`.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    Workbook wb(u"sampleGroupPivotFieldsInPivotTable.xlsx");
    Worksheet ws = wb.GetWorksheets().Get(1);
    PivotTable pt = ws.GetPivotTables().Get(0);
    pt.AddFieldToArea(PivotFieldType::Row, U16String("FieldTwo"));
    pt.CalculateData();
    PivotFieldGroupOptions options;
    options.SetStartNumber(0);
    options.SetEndNumber(5);
    options.SetInterval(2);
    pt.GetRowFields().Get(1).Group(options);
    pt.CalculateData();
    wb.Save(u"outputNumberGroupPivotField.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Note**

{{% alert color="primary" %}}
- The `PivotField.GroupBy()` method overloads are deprecated and removed from the API surface. `PivotField.Group()` and `PivotField.Group(PivotFieldGroupOptions)` are the replacements.
- In Microsoft Excel, grouping a numeric field REPLACES the original pivot field with the grouped ranges, while grouping a date field creates NEW pivot fields (one per group level, for example Quarters and Months) beside the original field. Starting with Aspose.Cells 26.10, the `PivotField.Group()` methods follow the same behavior as Excel. The `PivotFieldGroupOptions.NewPivotField` property exists for compatibility with older versions: it defaults to false for numeric grouping and true for date-time grouping; set it to false if you want date grouping to replace the original pivot field instead of creating new pivot fields.
- The `PivotFieldGroupOptions.Interval` property takes effect only for numeric grouping and for date grouping by days (for example, grouping dates into 7-day periods); it is ignored when dates are grouped by months, quarters or years.
{{% /alert %}}

## **Related Articles**
- [Add Row and Column Fields in Pivot Table](/cells/cpp/pivot-table-add-row-and-column-fields/)
- [Filtering Pivot Tables by Label or Value](/cells/cpp/filter-by-label-or-value-of-pivot-table/)
- [Add Page Field in Pivot Table](/cells/cpp/add-page-field-in-pivot-table/)
- [Apply Style to Pivot Table](/cells/cpp/apply-style-to-pivot-table/)
- [Refresh Pivot Table](/cells/cpp/refresh-pivot-table/)

{{< app/cells/assistant language="cpp" >}}