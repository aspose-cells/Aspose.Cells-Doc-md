---
title: Find and Refresh the Nested or Children Pivot Tables of Parent Pivot Table
type: docs
weight: 60
url: /python-net/find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table/
description: How to find and refresh the nested or children Pivot Tables of parent Pivot Table with Aspose.Cells for Python via .NET.
keywords: Aspose.Cells for Python Excel, Excel Python library, Find and Refresh the Nested or Children Pivot Tables of Parent Pivot Table Using Aspose.Cells for Python Excel Library.
---

## **Possible Usage Scenarios**

Sometimes, one pivot table uses another pivot table as a data source, so it is called a child pivot table or nested pivot table. You can find the children pivot tables of a parent pivot table using the [**PivotTable.get_children()**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/get_children/#) method.

## **How to Find and Refresh the Nested or Children Pivot Tables of Parent Pivot Table**

The following sample code loads the [sample Excel file](61767747.xlsx) that contains three pivot tables. The bottom two pivot tables are the children of the above pivot table as shown in this screenshot. The code finds the children pivot table using the [**PivotTable.get_children()**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/get_children/#) method and then refreshes them one by one.

![todo:image_alt_text](find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table_1.png)

## **Sample Code**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-FindAndRefreshNestedOrChildrenPivotTables.py" >}}
