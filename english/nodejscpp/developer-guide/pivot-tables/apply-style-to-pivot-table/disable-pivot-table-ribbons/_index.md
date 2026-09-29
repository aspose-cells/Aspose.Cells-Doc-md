---
title: Disable Pivot Table Ribbons
type: docs
weight: 90
url: /nodejs-cpp/disable-pivot-table-ribbons/
description: How to disable Pivot Table Ribbons with Aspose.Cells for Node.js via C++.
keywords: Aspose.Cells for Node.js Excel, Excel Node.js library, Disable Pivot Table Ribbons Using Aspose.Cells for Node.js via C++ Excel Library.
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Pivot-table-based reports are useful but prone to error if target users do not have detailed knowledge of Excel to configure these reports. In these circumstances, organizations will want to restrict users from being able to change a pivot-table-based report. Common pivot table features such as adding additional filters, slicers, fields, or changing the order of items in the report are generally not recommended for all users. However, these users should also be able to refresh the report and use existing filters or slicers. Aspose.Cells for Node.js via C++ provides this ability to developers for restricting users from changing these reports while creating them. For this purpose, Excel offers a feature to disable the pivot table ribbon, and the same capability is provided by Aspose.Cells for Node.js via C++. In other words, developers can disable the ribbon that contains controls for modifying these reports.

{{% /alert %}}

## **How to Disable Pivot Table Ribbon Using Aspose.Cells for Node.js via C++**

The following code demonstrates this feature by accessing a pivot table from a sheet and then setting [**setEnableWizard**](https://reference.aspose.com/cells/nodejs-cpp/pivottable/#setEnableWizard-boolean-) to **false**. The sample pivot table file can be downloaded from this [link](pivot_table_test.xlsx).

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-DisablePivotTableRibbon.js" >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
