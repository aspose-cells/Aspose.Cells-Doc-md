---
title: Get HTML5 String from Cell with Golang via C++
linktitle: Get HTML5 String from Cell
type: docs
weight: 90
url: /go-cpp/get-html5-string-from-cell/
description: Learn how to get HTML5 string from a cell using Aspose.Cells for C++ API.
keywords: Get HTML5 string from Cell, Obtain HTML5 string from Cell, Manage HTML5 string of Cell
---

## **Possible Usage Scenarios**

Aspose.Cells returns the HTML string of the cell using the [**GetHtmlString**](https://reference.aspose.com/cells/go-cpp/cell/gethtmlstring/) method which accepts a boolean parameter. If you pass **false** as a parameter, it will return Normal HTML but if you pass **true** as a parameter, it will return HTML5 string.

## **Get HTML5 String from Cell**

The following sample code creates a workbook object and adds some text in cell A1 of the first worksheet. It then gets the Normal HTML and HTML5 string from cell A1 using the [**GetHtmlString**](https://reference.aspose.com/cells/go-cpp/cell/gethtmlstring/) method and prints them on the console.

## **Sample Code**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-GO-CPP-GetHtml5StringFromCell.go" >}}
## **Console Output**

{{< highlight java >}}

 Normal:

<Font Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</Font>

Html5:

<div Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</div>

{{< /highlight >}}