---
title: Group Pivot Fields in the Pivot Table
description: Learn how to group row and column pivot fields in a pivot table into date periods such as months and quarters and numeric ranges using PivotField.Group and PivotFieldGroupOptions in Aspose.Cells for Python via .NET.
linktitle: Group Pivot Fields
keywords: Aspose.Cells, pivot table, group pivot field, PivotField.Group, PivotFieldGroupOptions, date grouping, number grouping, months, quarters, numeric range, Python via .NET
type: docs
weight: 80
url: /python-net/group-pivot-fields-in-the-pivot-table/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**
- Grouping pivot fields is useful when a row or column field of a pivot table contains many distinct items, such as a date field with hundreds of dates or a numeric field with many scattered values. Grouping collapses these items into meaningful sections: dates into months, quarters and years, and numbers into ranges such as 0-1, 2-3, 4-5. This makes a large pivot table compact and easier to analyze. Aspose.Cells for Python via .NET provides this capability through the `pivot_field.group()` method (automatic grouping by data type) and `pivot_field.group(pivot_field_group_options)` (custom grouping options).
- Date grouping rolls the individual dates up into larger periods, such as days, months, quarters and years, and builds a time hierarchy (for example Years, Quarters, Months). Trends over time become visible at a glance, and each period level becomes its own pivot field in the row or column area of the pivot table.
- Grouping is available only for fields placed in the ROW or COLUMN area of a pivot table. A data (value) field cannot be grouped directly. To group such a field you must first add it to the row or column area of the pivot table.

## **Group Pivot Fields Automatically**
The parameterless `pivot_field.group()` overload inspects the data type of the field and groups it automatically. A field that contains only dates (and blanks) is grouped by months. A field that contains only numbers (and blanks) is grouped into numeric ranges using an automatic interval.

```python
import aspose.cells as ac
# Load the sample workbook
wb = ac.Workbook("sampleGroupPivotFieldsInPivotTable.xlsx")
# Access the second worksheet and its pivot table
pt = wb.worksheets[1].pivot_tables[0]
# Group the first row field automatically.
# The field contains dates, so it is grouped by months.
field = pt.row_fields[0]
field.group()
# Calculate the pivot table data and save the output file
pt.calculate_data()
wb.save("outputAutoGroupPivotField.xlsx")
```

## **Group Pivot Fields with Custom Options**
The `PivotFieldGroupOptions` class provides custom grouping configuration. For date fields, set `start_date`, `end_date`, and `group_types`. For numeric fields, set `start_number`, `end_number`, and `interval`. The `new_pivot_field` property controls whether grouping creates new pivot fields alongside the original (see the Note section at the end of this article).

### **Group a Date Field by Months and Quarters**
The following example groups the date row field of the sample pivot table by months and quarters between a start and end date. The code loads the [sample Excel file](sampleGroupPivotFieldsInPivotTable.xlsx), performs the grouping, calculates the pivot table data, and saves the grouped result. The screenshot shows the effect: the date row field is now grouped by quarters and months.
Note that the order of the values in `options.group_types` is ignored. No matter in which order the group types are listed, the grouped fields are always displayed from the largest period to the smallest: years, quarters, months, days, hours, minutes, seconds. In this example the months are listed before the quarters in `options.group_types`, yet the quarters are displayed as the outer level and the months as the inner level.

```python
import aspose.cells as ac
from datetime import datetime
from aspose.cells.pivot import PivotGroupByType
from aspose.cells.pivot import PivotFieldGroupOptions
# Load the sample workbook
wb = ac.Workbook("sampleGroupPivotFieldsInPivotTable.xlsx")
# Access the second worksheet and its pivot table
pt = wb.worksheets[1].pivot_tables[0]
# Group the first row field (a date field) by months and quarters
options = PivotFieldGroupOptions()
options.start_date = datetime(2008, 1, 1)
options.end_date = datetime(2008, 9, 5)
options.group_types = [PivotGroupByType.MONTHS, PivotGroupByType.QUARTERS]
pt.row_fields[0].group(options)
# Calculate the pivot table data and save the output file
pt.calculate_data()
wb.save("outputGroupPivotFieldsInPivotTable.xlsx")
```

![Pivot table grouped by months and quarters](group-pivot-fields-in-the-pivot-table_1.png)

### **Group a Numeric Field into Ranges**
`FieldTwo` of the sample pivot table is initially a data (value) field. Because only row or column fields can be grouped, the code first calls `pivot_table.add_field_to_area(PivotFieldType.ROW, "FieldTwo")` to move `FieldTwo` to the row area, refreshes the pivot, then groups the numeric field into the ranges 0-1, 2-3 and 4-5 using `start_number=0`, `end_number=5` and `interval=2`.

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType
from aspose.cells.pivot import PivotFieldGroupOptions
# Load the sample workbook
wb = ac.Workbook("sampleGroupPivotFieldsInPivotTable.xlsx")
# Access the second worksheet and its pivot table
pt = wb.worksheets[1].pivot_tables[0]
# FieldTwo is a data field: move it to the row area first,
# because only row/column fields can be grouped
pt.add_field_to_area(PivotFieldType.ROW, "FieldTwo")
pt.calculate_data()
# Group the numeric field into the ranges 0-1, 2-3, 4-5
options = PivotFieldGroupOptions()
options.start_number = 0.0
options.end_number = 5.0
options.interval = 2.0
pt.row_fields[1].group(options)
# Calculate the pivot table data and save the output file
pt.calculate_data()
wb.save("outputNumberGroupPivotField.xlsx")
```

## **Note**

{{% alert color="primary" %}}
- The `pivot_field.group_by()` method overloads are deprecated and removed from the API surface. `pivot_field.group()` and `pivot_field.group(pivot_field_group_options)` are the replacements.
- In Microsoft Excel, grouping a numeric field REPLACES the original pivot field with the grouped ranges, while grouping a date field creates NEW pivot fields (one per group level, for example Quarters and Months) beside the original field. Starting with Aspose.Cells 26.10, the `pivot_field.group()` methods follow the same behavior as Excel. The `PivotFieldGroupOptions.new_pivot_field` property exists for compatibility with older versions: it defaults to false for numeric grouping and true for date-time grouping; set it to false if you want date grouping to replace the original pivot field instead of creating new pivot fields.
- The `PivotFieldGroupOptions.interval` property takes effect only for numeric grouping and for date grouping by days (for example, grouping dates into 7-day periods); it is ignored when dates are grouped by months, quarters or years.
{{% /alert %}}

## **Related Articles**
- [Add Row and Column Fields in Pivot Table](/cells/python-net/pivot-table-add-row-and-column-fields/)
- [Filtering Pivot Tables by Label or Value](/cells/python-net/filter-by-label-or-value-of-pivot-table/)
- [Add Page Field in Pivot Table](/cells/python-net/add-page-field-in-pivot-table/)
- [Apply Style to Pivot Table](/cells/python-net/apply-style-to-pivot-table/)
- [Refresh Pivot Table](/cells/python-net/refresh-pivot-table/)

{{< app/cells/assistant language="python-net" >}}