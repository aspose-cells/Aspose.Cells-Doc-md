---
title: Remove Pivot Connection
type: docs
weight: 30
url: /java/remove-pivot-connection/
description: Learn how to remove pivot connection with Aspose.Cells Java library.
keywords: Remove pivot connection without office 2013, office 2016, office 2019 and office 365.
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**

If you want to disassociate slicer and pivot table in Excel, you need to right-click slicer and select "Report Connections..." item. In the option list, you can operate on the check box. Similarly, if you want to disassociate slicer and pivot table using Aspose.Cells API programmatically, please use the [**Slicer.removePivotConnection(PivotTable pivot)**](https://reference.aspose.com/cells/java/com.aspose.cells/slicer#removePivotConnection-com.aspose.cells.PivotTable-) method. It will disassociate slicer and pivot table.

## **Removing Slicer**

The following sample code loads the [sample Excel file](remove-pivot-connection.xlsx) that contains an existing slicer. It accesses the slicers and then disassociates slicer and pivot table. Finally, it saves the workbook as [output Excel file](remove-pivot-connection-out.xlsx). 


## **Sample Code**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Slicers-Removing-Pivot-Connection.java" >}}
{{< app/cells/assistant language="java" >}}
