---
title: Find and Refresh the Nested or Children Pivot Tables of Parent Pivot Table
type: docs
weight: 50
url: /java/find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table/
---

## **Possible Usage Scenarios**
Sometimes, one pivot table uses another pivot table as a data source, so it is called a child pivot table or nested pivot table. You can find the children pivot tables of a parent pivot table using the [PivotTable.getChildren()](https://apireference.aspose.com/java/cells/com.aspose.cells/pivottable#getChildren\(\)) method.
## **Find and Refresh the Nested or Children Pivot Tables of Parent Pivot Table**
The following sample code loads the [sample Excel file](attachments/61540750/61767766.xlsx) that contains three pivot tables. The bottom two pivot tables are the children of the above pivot table as shown in this screenshot. The code finds the children pivot table using the [PivotTable.getChildren()](https://apireference.aspose.com/java/cells/com.aspose.cells/pivottable#getChildren\(\)) method and then refreshes them one by one.

![todo:image_alt_text](find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table_1.png)
## **Sample Code**
{{< gist "aspose-com-gists" "439a68a5e4305388c50ca306ef238de5" "PivotTables-FindAndRefreshNestedOrChildrenPivotTables.java" >}}
