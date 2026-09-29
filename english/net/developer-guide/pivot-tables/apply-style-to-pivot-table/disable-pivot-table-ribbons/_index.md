---
title: Disable Pivot Table Ribbons
type: docs
weight: 90
url: /net/disable-pivot-table-ribbons/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Pivot-table-based reports are useful but prone to error if target users do not have detailed knowledge of Excel to configure these reports. In these circumstances, organizations will want to restrict users from being able to change a pivot-table-based report. Common pivot table features, such as adding additional filters, slicers, fields, or changing the order of items in the report, are generally not recommended for all users. On the other hand, these users should also be able to refresh the report and use existing filters or slicers. Aspose.Cells has provided this ability to developers to restrict users from changing these reports while creating them. For this purpose, Excel provides a feature to disable the pivot table ribbon, and Aspose.Cells also provides this capability; developers can disable the ribbon that contains controls for modifying these reports.

{{% /alert %}}

## **Disable Pivot Table Ribbon using PivotTable.EnableWizard**

The following code demonstrates this feature by accessing a pivot table from a sheet and then setting [**EnableWizard**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/properties/enablewizard) to **false**. A sample pivot table file can be downloaded from this [link](pivot_table_test.xlsx).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "PivotTables-DisablePivotTableRibbon.cs" >}}
{{< app/cells/assistant language="csharp" >}}
