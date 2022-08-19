---
title: Add Pivot Connection
type: docs
weight: 30
url: /java/add-pivot-connection/
description: Learn how to add pivot connection with Aspose.Cells Java library.
keywords: Add pivot connection without office 2013, office 2016, office 2019 and office 365.
---

## **Possible Usage Scenarios**

If you want to associate slicer and pivot table in Excel, you need to right-click slicer and select "Report Connections..." item. In the option list, you can operate on the check box. Similarly, if you want to associate slicer and pivot table using Aspose.Cells Java API programmatically, please use the [**Slicer.addPivotConnection(PivotTable pivot)**](https://reference.aspose.com/cells/java/com.aspose.cells/slicer#addPivotConnection(com.aspose.cells.PivotTable)/) method. It will associate slicer and pivot table.

## **Associate Slicer and PivotTable**

The following sample code loads the [sample Excel file](add-pivot-connection.xlsx) that contains an existing slicer. It accesses the Slicer and then associates Slicer and PivotTable. Finally, it saves the workbook as [output Excel file](add-pivot-connection-out.xlsx). 


## **Sample Code**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Slicers-Adding-Pivot-Connection.java" >}}