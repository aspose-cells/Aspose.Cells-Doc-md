---
title: Disable Pivot Table Ribbons
type: docs
weight: 90
url: /python-net/disable-pivot-table-ribbons/
description: How to disable Pivot Table Ribbons with Aspose.Cells for Python via .NET.
keywords: Disable Pivot Table Ribbons.
---

{{% alert color="primary" %}}

Pivot table based reports are useful but prone to error if target users do not have detailed knowledge of Excel to configure these reports. In these circumstances, organizations will want to restrict users from being able to change a pivot table based report. Common pivot table features like adding additional filters, slicers, fields, or changing the order of certain things in the report are mostly not recommended for every user. On the other hand, these users shall also be able to refresh the report and use existing filters or slicers. Aspose.Cells for Python via .NET has provided this ability to developers for restricting users from changing these reports while creating these reports. For this purpose, Excel provides a feature to disable the pivot table ribbon and the same is provided by Aspose.Cells for Python via .NET i.e. developer can disable the ribbon which contains controls to modify these reports.

{{% /alert %}}

## **Disable Pivot Table Ribbon using PivotTable.EnableWizard**

Following code demonstrates this feature by accessing a pivot table from a sheet and then setting [**enable_wizard**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/enable_wizard/) to **false**. Sample pivot table file can be downloaded from this [link](pivot_table_test.xlsx).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-DisablePivotTableRibbon.py" >}}
