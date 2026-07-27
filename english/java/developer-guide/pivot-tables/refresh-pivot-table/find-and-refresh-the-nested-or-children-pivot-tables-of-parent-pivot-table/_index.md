---
title: Find and Refresh the Nested or Child Pivot Tables of a Parent Pivot Table
type: docs
weight: 50
url: /java/find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**

Sometimes, one pivot table uses another pivot table as a data source, so it is called a child pivot table or nested pivot table. You can find the children pivot tables of a parent pivot table using the [**PivotTable.getChildren()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#getChildren--) method.

## **Find and Refresh the Nested or Child Pivot Tables of Parent Pivot Table**

The following sample code loads the [sample Excel file](61767766.xlsx) that contains three pivot tables. The bottom two pivot tables are the children of the above pivot table as shown in this screenshot. The code finds the children pivot tables using the [**PivotTable.getChildren()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#getChildren--) method and then refreshes them one by one.

![todo:image_alt_text](find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table_1.png)

## **Sample Code**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "PivotTables-FindAndRefreshNestedOrChildrenPivotTables.java" >}}
{{< app/cells/assistant language="java" >}}
