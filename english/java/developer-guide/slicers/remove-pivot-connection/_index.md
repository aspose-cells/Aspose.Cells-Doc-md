---
title: Remove Pivot Connection
type: docs
weight: 30
url: /java/remove-pivot-connection/
description: Learn how to remove a pivot connection with the Aspose.Cells Java library.
keywords: Remove pivot connection without Office 2013, Office 2016, Office 2019, and Office 365.
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**

If you want to disassociate a slicer and a pivot table in Excel, you need to right‑click the slicer and select the "Report Connections…" item. In the options list, you can toggle the check box. Similarly, if you want to disassociate a slicer and a pivot table programmatically using the Aspose.Cells API, please use the [**Slicer.removePivotConnection(PivotTable pivot)**](https://reference.aspose.com/cells/java/com.aspose.cells/slicer#removePivotConnection-com.aspose.cells.PivotTable-) method. It will disassociate the slicer and the pivot table.

## **Removing Slicer**

The following sample code loads the [sample Excel file](remove-pivot-connection.xlsx) that contains an existing slicer. It accesses the slicers and then disassociates the slicer from the pivot table. Finally, it saves the workbook as the [output Excel file](remove-pivot-connection-out.xlsx). 


## **Sample Code**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Slicers-Removing-Pivot-Connection.java" >}}
{{< app/cells/assistant language="java" >}}
