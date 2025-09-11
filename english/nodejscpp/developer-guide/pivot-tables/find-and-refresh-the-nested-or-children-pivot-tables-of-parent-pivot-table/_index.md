---
title: Find and Refresh the Nested or Children Pivot Tables of Parent Pivot Table
type: docs
weight: 60
url: /nodejs-cpp/find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table/
description: How to find and refresh the nested or children Pivot Tables of parent Pivot Table with Aspose.Cells for Node.js via C++.
keywords: Aspose.Cells for Node.js Excel, Excel Node.js library, Find and Refresh the Nested or Children Pivot Tables of Parent Pivot Table Using Aspose.Cells for Node.js Excel Library.
---

## **Possible Usage Scenarios**

Sometimes, one pivot table uses another pivot table as a data source, so it is called a child pivot table or nested pivot table. You can find the children pivot tables of a parent pivot table using the [**PivotTable.getChildren()**](https://reference.aspose.com/cells/nodejs-cpp/pivottable/#getChildren--) method.

## **How to Find and Refresh the Nested or Children Pivot Tables of Parent Pivot Table**

The following sample code loads the [sample Excel file](61767747.xlsx) that contains three pivot tables. The bottom two pivot tables are the children of the above pivot table as shown in this screenshot. The code finds the children pivot table using the [**PivotTable.getChildren()**](https://reference.aspose.com/cells/nodejs-cpp/pivottable/#getChildren--) method and then refreshes them one by one.

![todo:image_alt_text](find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table_1.png)

## **Sample Code**

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-FindAndRefreshNestedOrChildrenPivotTables.js" >}}
{{< app/cells/assistant language="nodejs-cpp" >}}