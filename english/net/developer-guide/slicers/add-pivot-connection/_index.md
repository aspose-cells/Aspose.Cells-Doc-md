---
title: Add Pivot Connection
type: docs
weight: 30
url: /net/add-pivot-connection/
description: Learn how to add pivot connection with Aspose.Cells library.
keywords: Add pivot connection without Office 2013, Office 2016, Office 2019, and Office 365.
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**

If you want to associate a slicer and a pivot table in Excel, you need to right‑click the slicer and select the “Report Connections...” item. In the options list, you can check the boxes. Similarly, if you want to associate a slicer and a pivot table using the Aspose.Cells API programmatically, please use the [**Slicer.AddPivotConnection(PivotTable pivot)**](https://reference.aspose.com/cells/net/aspose.cells.slicers/slicer/addpivotconnection/) method. It will associate the slicer with the pivot table.

## **Associate Slicer and PivotTable**

The following sample code loads the [sample Excel file](add-pivot-connection.xlsx) that contains an existing slicer. It accesses the slicer and then associates the slicer with the pivot table. Finally, it saves the workbook as [output Excel file](add-pivot-connection-out.xlsx). 

## **Sample Code**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Slicers-Adding-Pivot-Connection.cs" >}}
{{< app/cells/assistant language="csharp" >}}
