---
title: Get HTML5 string from Cell
type: docs
weight: 90
url: /net/get-html5-string-from-cell/
---

## **Possible Usage Scenarios**

Aspose.Cells returns the HTML string of the cell using the [**GetHtmlString**](https://apireference.aspose.com/cells/net/aspose.cells/cell/methods/gethtmlstring) method which accepts a boolean parameter. If you pass **false** as a parameter, it will return Normal HTML but if you pass **true** as a parameter, it will return HTML5 string.

## **Get HTML5 string from Cell**

The following sample code creates a workbook object and adds some text in cell A1 of the first worksheet. It then gets the Normal HTML and HTML5 string from cell A1 using the [**GetHtmlString**](https://apireference.aspose.com/cells/net/aspose.cells/cell/methods/gethtmlstring) method and prints them on the console.

## **Sample Code**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "HTML-GetHTML5StringFromCell.cs" >}}

## **Console Output**

{{< highlight java >}}

 Normal:

<Font Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</Font>

Html5:

<div Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</div>

{{< /highlight >}}
