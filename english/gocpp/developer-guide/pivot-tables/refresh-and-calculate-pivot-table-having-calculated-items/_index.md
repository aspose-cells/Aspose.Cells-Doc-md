---
title: Refresh and Calculate Pivot Table having Calculated Items with Golang via C++
linktitle: Refresh and Calculate Pivot Table having Calculated Items
type: docs
weight: 40
url: /go-cpp/refresh-and-calculate-pivot-table-having-calculated-items/
description: Refresh and calculate pivot table with calculated items using Aspose.Cells with Golang via C++.
---

{{% alert color="primary" %}}

Aspose.Cells now supports refreshing and calculating pivot table having calculated items. Please use the [**PivotTable.RefreshData()**](https://reference.aspose.com/cells/go-cpp/pivottable/refreshdata/) and [**PivotTable.CalculateData()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/calculatedata/) as usual to perform this function.

{{% /alert %}}

## **Refresh and Calculate Pivot Table having Calculated Items**

The following sample code loads the [source excel file](5115238.xlsx) which contains a pivot table having three calculated items such as "add", "div", "div2". We first change the value of cell D2 to 20 and then refresh and calculate the pivot table using Aspose.Cells APIs and save the workbook in PDF format. The results in the [output PDF](5115229.pdf) show that Aspose.Cells refreshed and calculated the pivot table having calculated items successfully. You can verify it using Microsoft Excel by manually putting the value 20 in cell D2 and then refreshing the pivot table via Alt+F5 shortcut key or clicking the pivot table Refresh button.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-RefreshAndCalculatePivotTableHavingCalculatedItems.go" >}}