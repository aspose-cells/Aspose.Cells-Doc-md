---
title: Remove Pivot Connection with Golang via C++
linktitle: Remove Pivot Connection
type: docs
weight: 30
url: /go-cpp/remove-pivot-connection/
description: Learn how to remove pivot connection with Aspose.Cells library using C++.
keywords: Remove pivot connection without office 2013, office 2016, office 2019 and office 365.
---

## **Possible Usage Scenarios**

If you want to disassociate the slicer and pivot table in Excel, you need to right‑click the slicer and select the **"Report Connections..."** item. In the options list, you can toggle the check box. Similarly, if you want to disassociate the slicer and pivot table using the Aspose.Cells API programmatically, please use the [**Slicer.RemovePivotConnection(PivotTable pivot)**](https://reference.aspose.com/cells/go-cpp/slicer/removepivotconnection/) method. It will disassociate the slicer and pivot table.

## **Disassociate slicer and pivot table**

The following sample code loads the [sample Excel file](remove-pivot-connection.xlsx) that contains an existing slicer. It accesses the slicers and then disassociates the slicer from the pivot table. Finally, it saves the workbook as the [output Excel file](remove-pivot-connection-out.xlsx).

## **Sample Code**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-RemovePivotConnection.go" >}}