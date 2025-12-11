---
title: Add Pivot Connection with Golang via C++
linktitle: Add Pivot Connection
type: docs
weight: 30
url: /go-cpp/add-pivot-connection/
description: Learn how to add a pivot connection with the Aspose.Cells library using C++.
keywords: Add pivot connection without Office 2013, Office 2016, Office 2019, and Office 365.
---

## **Possible Usage Scenarios**

If you want to associate a slicer and a pivot table in Excel, you need to right‑click the slicer and select the **“Report Connections...”** item. In the options list, you can check the boxes. Similarly, if you want to associate a slicer and a pivot table using the Aspose.Cells API programmatically, please use the [**Slicer.AddPivotConnection(PivotTable pivot)**](https://reference.aspose.com/cells/go-cpp/slicer/addpivotconnection/) method. It will associate the slicer with the pivot table.

## **Associate Slicer and PivotTable**

The following sample code loads the [sample Excel file](add-pivot-connection.xlsx) that contains an existing slicer. It accesses the slicer and then associates the slicer with the pivot table. Finally, it saves the workbook as the [output Excel file](add-pivot-connection-out.xlsx). 

## **Sample Code**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AddPivotConnection.go" >}}