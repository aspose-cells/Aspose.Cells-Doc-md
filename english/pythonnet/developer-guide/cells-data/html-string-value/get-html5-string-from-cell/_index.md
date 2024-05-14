---
title: Get HTML5 string from Cell
type: docs
weight: 90
url: /python-net/get-html5-string-from-cell/
description: Learn how to Get HTML5 string from Cell through the Aspose.Cells for Python via .NET API.
keywords: Python Excel Libray, Python Get HTML5 string from Cell, Obtain HTML5 string from Cell using Python, Manage HTML5 string of Cell in Python.
---

## **Possible Usage Scenarios**

Aspose.Cells for Python via .NET returns the HTML string of the cell using the [**get_html_string(html5)**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_html_string/#bool) method which accepts a boolean parameter. If you pass **false** as a parameter, it will return Normal HTML but if you pass **true** as a parameter, it will return HTML5 string.

## **Get HTML5 string from Cell**

The following sample code creates a workbook object and adds some text in cell A1 of the first worksheet. It then gets the Normal HTML and HTML5 string from cell A1 using the [**get_html_string(html5)**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_html_string/#bool) method and prints them on the console.

## **Sample Code**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-HtmlStringValue-GetHTML5StringFromCell.py" >}}

## **Console Output**

{{< highlight java >}}

 Normal:

<Font Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</Font>

Html5:

<div Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</div>

{{< /highlight >}}
