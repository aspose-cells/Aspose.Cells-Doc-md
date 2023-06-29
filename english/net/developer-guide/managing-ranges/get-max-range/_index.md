---
title: Get Max Range In A Worksheet
type: docs
weight: 360
url: /net/get-max-range-in-a-worksheet/
description: This article describes how to get the max range , max data range, max display range of Excel files with Aspose.Cells for .Net library.
---

{{% alert color="primary" %}} 

When reading data from the worksheet, we need to know the maximum area.

When copying all data from a worksheet, we need to know the maximum area.

When exporting a specified area to html and pdf, we need to know the maximum area.

Aspose.Cells for .Net contains different ways to find max range in a worksheet. 


{{% /alert %}} 



## **Getting max range**
In Aspose.Cells ,if the [**row**](https://reference.aspose.com/cells/net/aspose.cells/row) and [**column**](https://reference.aspose.com/cells/net/aspose.cells/column) objects are initialized, these rows and columns will be counted to the maximum area, even if there is no data in empty rows or columns.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Get-Max-Range.cs" >}}

## **Getting max data range**
In most cases, we only need to obtain all the ranges containing all the data, even if the empty cells outside the range are formatted.
And the settings about shapes, tables and pivottables will be ignored.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Get-Max-Data-Range.cs" >}}

## **Getting max display range**
When we export all data from the worksheet to HTML, PDF, or images, we need to obtain an area containing all visible objects, including data, styles, graphics, tables, and pivot tables.
The following codes show how to render the max diplay range to html:

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Get-Max-Display-Range.cs" >}}

Here is [source excel file](Book1.xlsx).
