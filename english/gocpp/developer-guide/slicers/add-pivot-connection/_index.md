---
title: Add Pivot Connection with Golang via C++
linktitle: Add Pivot Connection
type: docs
weight: 30
url: /go-cpp/add-pivot-connection/
description: Learn how to add pivot connection with Aspose.Cells library using C++.
keywords: Add pivot connection without office 2013, office 2016, office 2019 and office 365.
---

## **Possible Usage Scenarios**

If you want to associate slicer and pivot table in Excel, you need to right-click slicer and select "Report Connections..." item. In the option list, you can operate on the check box. Similarly, if you want to associate slicer and pivot table using Aspose.Cells API programmatically, please use the [**Slicer.AddPivotConnection(PivotTable pivot)**](https://reference.aspose.com/cells/go-cpp/slicer/addpivotconnection/) method. It will associate slicer and pivot table.

## **Associate Slicer and PivotTable**

The following sample code loads the [sample Excel file](add-pivot-connection.xlsx) that contains an existing slicer. It accesses the Slicer and then associates Slicer and PivotTable. Finally, it saves the workbook as [output Excel file](add-pivot-connection-out.xlsx). 

## **Sample Code**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AddPivotConnection.go" >}}