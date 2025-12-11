---
title: Get Max Range In A Worksheet
type: docs
weight: 360
url: /net/get-max-range-in-a-worksheet/
description: This article describes how to get the max range, max data range, max display range of Excel files with Aspose.Cells for .Net library.
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}} 

When reading data from the worksheet, we need to know the maximum area.

When copying all data from a worksheet, we need to know the maximum area.

When exporting a specified area to HTML and PDF, we need to know the maximum area.

Aspose.Cells for .Net contains different ways to find max range in a worksheet. 

{{% /alert %}} 

## **Getting max range**
In Aspose.Cells, if the [**row**](https://reference.aspose.com/cells/net/aspose.cells/row) and [**column**](https://reference.aspose.com/cells/net/aspose.cells/column) objects are initialized, these rows and columns will be counted towards the maximum area, even if they are empty.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Get-Max-Range.cs" >}}

## **Getting max data range**
In most cases, we only need to obtain all the ranges containing all the data, even if the empty cells outside the range are formatted.  
The settings for shapes, tables, and pivot tables will be ignored.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Get-Max-Data-Range.cs" >}}

## **Getting max display range**
When we export all data from the worksheet to HTML, PDF, or images, we need to obtain an area containing all visible objects, including data, styles, graphics, tables, and pivot tables.  
The following code shows how to render the max display range to HTML:

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Get-Max-Display-Range.cs" >}}

Here is the [source Excel file](Book1.xlsx).
{{< app/cells/assistant language="csharp" >}}
