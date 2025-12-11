---
title: Add Pivot Connection
type: docs
weight: 30
url: /java/add-pivot-connection/
description: Learn how to add a pivot connection with the Aspose.Cells Java library.
keywords: Add pivot connection without Office 2013, Office 2016, Office 2019, and Office 365.
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**

If you want to associate a slicer and a pivot table in Excel, you need to right‑click the slicer and select the “Report Connections...” item. In the options list, you can check or uncheck the boxes. Similarly, if you want to associate a slicer and a pivot table programmatically using the Aspose.Cells Java API, please use the **[Slicer.addPivotConnection(PivotTable pivot)](https://reference.aspose.com/cells/java/com.aspose.cells/slicer#addPivotConnection-com.aspose.cells.PivotTable-)** method. It will associate the slicer with the pivot table.

## **Associate Slicer and PivotTable**

The following sample code loads the [sample Excel file](add-pivot-connection.xlsx) that contains an existing slicer. It accesses the slicer and then associates the slicer with the pivot table. Finally, it saves the workbook as the [output Excel file](add-pivot-connection-out.xlsx). 

## **Sample Code**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Slicers-Adding-Pivot-Connection.java" >}}
{{< app/cells/assistant language="java" >}}
