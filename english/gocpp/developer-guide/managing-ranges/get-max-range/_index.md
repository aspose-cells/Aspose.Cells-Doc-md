---
title: Get Max Range In A Worksheet with Golang via C++
linktitle: Get Max Range In A Worksheet
type: docs
weight: 360
url: /go-cpp/get-max-range-in-a-worksheet/
description: This article describes how to get the max range, max data range, max display range of Excel files with Aspose.Cells for C++ library.
---

{{% alert color="primary" %}} 

When reading data from the worksheet, we need to know the maximum area.

When copying all data from a worksheet, we need to know the maximum area.

When exporting a specified area to HTML and PDF, we need to know the maximum area.

Aspose.Cells for C++ contains different ways to find the max range in a worksheet. 

{{% /alert %}} 

## **Getting max range**
In Aspose.Cells, if the [**Row**](https://reference.aspose.com/cells/go-cpp/row/) and [**Column**](https://reference.aspose.com/cells/cpp/aspose.cells/column/) objects are initialized, these rows and columns will be counted to the maximum area, even if there is no data in empty rows or columns.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-GO-CPP-GetMaxRange.go" >}}
## **Getting max data range**
In most cases, we only need to obtain all the ranges containing all the data, even if the empty cells outside the range are formatted.
And the settings about shapes, tables, and pivot tables will be ignored.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-GO-CPP-GetMaxRange-1.go" >}}
## **Getting max display range**
When we export all data from the worksheet to HTML, PDF, or images, we need to obtain an area containing all visible objects, including data, styles, graphics, tables, and pivot tables.
The following codes show how to render the max display range to HTML:

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-GO-CPP-GetMaxRange-2.go" >}}
Here is [source excel file](Book1.xlsx).