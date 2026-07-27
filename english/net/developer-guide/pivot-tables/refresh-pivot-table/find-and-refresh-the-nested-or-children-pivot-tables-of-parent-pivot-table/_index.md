---
title: Find and Refresh the Nested or Child Pivot Tables of a Parent Pivot Table
type: docs
weight: 60
url: /net/find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**

Sometimes, one pivot table uses another pivot table as a data source, so it is called a child pivot table or nested pivot table. You can find the child pivot tables of a parent pivot table using the [**PivotTable.GetChildren()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/methods/getchildren) method.

## **Find and Refresh the Nested or Child Pivot Tables of a Parent Pivot Table**

The following sample code loads the [sample Excel file](61767747.xlsx) that contains three pivot tables. The bottom two pivot tables are the children of the above pivot table as shown in this screenshot. The code finds the child pivot tables using the [**PivotTable.GetChildren()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/methods/getchildren) method and then refreshes them one by one.

![todo:image_alt_text](find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table_1.png)

## **Sample Code**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "PivotTables-FindAndRefreshNestedOrChildrenPivotTables.cs" >}}
{{< app/cells/assistant language="csharp" >}}
