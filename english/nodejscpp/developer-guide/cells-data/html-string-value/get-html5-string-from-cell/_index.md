---
title: Get HTML5 string from Cell
type: docs
weight: 90
url: /nodejs-cpp/get-html5-string-from-cell/
description: Learn how to get HTML5 string from Cell through the Aspose.Cells for Node.js via C++ API.
keywords: Get HTML5 string from Cell Node.js via C++, Obtain HTML5 string from Cell Node.js via C++, Manage HTML5 string of Cell Node.js via C++
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**

Aspose.Cells returns the HTML string of the cell using the [**Cell.getHtmlString(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getHtmlString-boolean-) method which accepts a boolean parameter. If you pass **false** as a parameter, it will return Normal HTML but if you pass **true** as a parameter, it will return HTML5 string.

## **Get HTML5 string from Cell**

The following sample code creates a workbook object and adds some text in cell A1 of the first worksheet. It then gets the Normal HTML and HTML5 string from cell A1 using the [**Cell.getHtmlString(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getHtmlString-boolean-) method and prints them on the console.

## **Sample Code**

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-HtmlStringValue-GetHtml5String.js" >}}


## **Console Output**

{{< highlight javascript >}}

 Normal:

<Font Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</Font>

Html5:

<div Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</div>

{{< /highlight >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
