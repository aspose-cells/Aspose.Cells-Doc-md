---
title: Find and Refresh the Nested or Children Pivot Tables of Parent Pivot Table with Golang via C++
linktitle: Find and Refresh Nested or Children Pivot Tables
type: docs
weight: 60
url: /go-cpp/find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table/
description: Learn how to find and refresh nested or children pivot tables of a parent pivot table using Aspose.Cells for C++.
---

## **Possible Usage Scenarios**

Sometimes, one pivot table uses another pivot table as a data source, so it is called a child pivot table or nested pivot table. You can find the children pivot tables of a parent pivot table using the [**PivotTable::GetChildren()**](https://reference.aspose.com/cells/go-cpp/pivottable/getchildren/) method.

## **Find and Refresh the Nested or Children Pivot Tables of Parent Pivot Table**

The following sample code loads the [sample Excel file](61767747.xlsx) that contains three pivot tables. The bottom two pivot tables are the children of the above pivot table as shown in this screenshot. The code finds the children pivot table using the [**PivotTable::GetChildren()**](https://reference.aspose.com/cells/go-cpp/pivottable/getchildren/) method and then refreshes them one by one.

![todo:image_alt_text](find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table_1.png)

## **Sample Code**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FindAndRefreshTheNestedOrChildrenPivotTablesOfParentPivotTable.go" >}}