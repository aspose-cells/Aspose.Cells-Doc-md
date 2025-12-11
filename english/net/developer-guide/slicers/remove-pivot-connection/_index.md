---
title: Remove Pivot Connection
type: docs
weight: 30
url: /net/remove-pivot-connection/
description: Learn how to remove a pivot connection with the Aspose.Cells library.
keywords: Remove pivot connection without Office 2013, Office 2016, Office 2019, and Office 365.
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**

If you want to disassociate a slicer and a pivot table in Excel, you need to right‑click the slicer and select the **“Report Connections…”** item. In the options list, you can toggle the check box. Similarly, if you want to disassociate a slicer and a pivot table using the Aspose.Cells API programmatically, please use the [**Slicer.RemovePivotConnection(PivotTable pivot)**](https://reference.aspose.com/cells/net/aspose.cells.slicers/slicer/removepivotconnection/) method. It will disassociate the slicer from the pivot table.

## **Disassociate a slicer and a pivot table**

The following sample code loads the [sample Excel file](remove-pivot-connection.xlsx) that contains an existing slicer. It accesses the slicers and then disassociates the slicer from the pivot table. Finally, it saves the workbook as the [output Excel file](remove-pivot-connection-out.xlsx). 

## **Sample Code**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Slicers-Removing-Pivot-Connection.cs" >}}
{{< app/cells/assistant language="csharp" >}}
