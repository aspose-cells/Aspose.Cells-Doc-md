---
title: Get HTML5 string from Cell
type: docs
weight: 90
url: /java/get-html5-string-from-cell/
---

## **Possible Usage Scenarios**

Aspose.Cells returns the HTML string of the cell using the [**getHtmlString(boolean html5)**](https://apireference.aspose.com/cells/java/com.aspose.cells/cell#HtmlString) method. If you pass **false** as a parameter, it will return you Normal HTML but if you pass **true** as a parameter, it will return HTML5 string.

## **Get HTML5 string from Cell**

The following sample code creates a workbook object and adds some text in cell A1 of the first worksheet. It then gets the Normal HTML and HTML5 string from cell A1 using the [**getHtmlString(boolean html5)**](https://apireference.aspose.com/cells/java/com.aspose.cells/cell#HtmlString) method and prints them on the console.

## **Sample Code**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "HTML-GetHTML5StringFromCell.java" >}}

## **Console Output**

{{< highlight java >}}

Normal:

<Font Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</Font>

Html5:

<div Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</div>

{{< /highlight >}}
