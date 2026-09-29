---
title: Disable Pivot Table Ribbons
type: docs
weight: 90
url: /python-net/disable-pivot-table-ribbons/
description: How to disable Pivot Table Ribbons with Aspose.Cells for Python via .NET.
keywords: Aspose.Cells for Python Excel, Excel Python library, Disable Pivot Table Ribbons Using Aspose.Cells for Python Excel Library.
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Pivot-table-based reports are useful but prone to error if target users do not have detailed knowledge of Excel to configure these reports. In these circumstances, organizations will want to restrict users from being able to change a pivot-table-based report. Common pivot table features such as adding additional filters, slicers, fields, or changing the order of items in the report are generally not recommended for all users. However, these users should still be able to refresh the report and use existing filters or slicers. Aspose.Cells for Python via .NET has provided this ability to developers to restrict users from changing these reports while they are being created. For this purpose, Excel provides a feature to disable the Pivot Table ribbon, and the same capability is offered by Aspose.Cells for Python via .NET, i.e., developers can disable the ribbon that contains controls to modify these reports.

{{% /alert %}}

## **How to Disable Pivot Table Ribbon Using Aspose.Cells for Python Excel Library**

The following code demonstrates this feature by accessing a pivot table from a sheet and then setting [**enable_wizard**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/enable_wizard/) to **false**. The sample pivot table file can be downloaded from this [link](pivot_table_test.xlsx).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-DisablePivotTableRibbon.py" >}}
{{< app/cells/assistant language="python-net" >}}
