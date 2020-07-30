---
title : "Get HTML5 string from Cell" 
description : "" 
weight : 12093 
toc : false
type: docs
url: /java/developerguide/html/get+html5+string+from+cell/
---

# Aspose.Cells for Java : Get HTML5 string from Cell


{{< panel title="Contents Summary" style="primary" >}}
*   1 [Possible Usage Scenarios](#possible-usage-scenarios)
*   2 [Get HTML5 string from Cell](#get-html5-string-from-cell)
*   3 [Sample Code](#sample-code)
*   4 [Console Output](#console-output)
{{< /panel >}}
 

## Possible Usage Scenarios

Aspose.Cells returns the HTML string of the cell using the [getHtmlString(boolean html5)](https://apireference.aspose.com/java/cells/com.aspose.cells/cell#HtmlString) method. If you pass **false **as a parameter, it will return you Normal HTML but if you pass **true **as a parameter, it will return HTML5 string.

## Get HTML5 string from Cell

The following sample code creates a workbook object and adds some text in cell A1 of the first worksheet. It then gets the Normal HTML and HTML5 string from cell A1 using the [getHtmlString(boolean html5)](https://apireference.aspose.com/java/cells/com.aspose.cells/cell#HtmlString) method and prints them on the console.

## Sample Code

## Console Output

{{< code lang="cs" >}}
Normal:
<Font Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</Font>

Html5:
<div Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</div>
{{< /code >}}

