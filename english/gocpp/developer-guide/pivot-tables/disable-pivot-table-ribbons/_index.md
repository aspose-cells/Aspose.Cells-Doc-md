---
title: Disable Pivot Table Ribbons with Golang via C++
linktitle: Disable Pivot Table Ribbons
type: docs
weight: 90
url: /go-cpp/disable-pivot-table-ribbons/
description: Learn how to disable pivot table ribbons in Excel files using Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Pivot table-based reports are useful but prone to error if target users do not have detailed knowledge of Excel to configure these reports. In these circumstances, organizations will want to restrict users from being able to change a pivot table-based report. Common pivot table features like adding additional filters, slicers, fields, or changing the order of certain things in the report are mostly not recommended for every user. On the other hand, these users shall also be able to refresh the report and use existing filters or slicers. Aspose.Cells has provided this ability to developers for restricting users from changing these reports while creating them. For this purpose, Excel provides a feature to disable the pivot table ribbon, and the same is provided by Aspose.Cells. Developers can disable the ribbon which contains controls to modify these reports.

{{% /alert %}}

## **Disable Pivot Table Ribbon using PivotTable.EnableWizard**

The following code demonstrates this feature by accessing a pivot table from a sheet and then setting [**GetEnableWizard()**](https://reference.aspose.com/cells/go-cpp/pivottable/getenablewizard/) to **false**. A sample pivot table file can be downloaded from this [link](pivot_table_test.xlsx).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-GO-CPP-DisablePivotTableRibbons.go" >}}