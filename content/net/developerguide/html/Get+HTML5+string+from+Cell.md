+++
title = "Get HTML5 string from Cell" 
description = "" 
weight = 12109 
+++

Aspose.Cells for .NET : Get HTML5 string from Cell  

# Aspose.Cells for .NET : Get HTML5 string from Cell


{{< panel title="Contents Summary" style="primary" >}}
*   1 [Possible Usage Scenarios](#GetHTML5stringfromCell-PossibleUsageScenarios)
*   2 [Get HTML5 string from Cell](#GetHTML5stringfromCell-GetHTML5stringfromCell)
*   3 [Sample Code](#GetHTML5stringfromCell-SampleCode)
*   4 [Console Output](#GetHTML5stringfromCell-ConsoleOutput)
{{< /panel >}}
 

## Possible Usage Scenarios

Aspose.Cells returns the HTML string of the cell using the [GetHtmlString](https://apireference.aspose.com/net/cells/aspose.cells/cell/methods/gethtmlstring) method which accepts a boolean parameter. If you pass **false** as a parameter, it will return Normal HTML but if you pass **true** as a parameter, it will return HTML5 string.

## Get HTML5 string from Cell

The following sample code creates a workbook object and adds some text in cell A1 of the first worksheet. It then gets the Normal HTML and HTML5 string from cell A1 using the [GetHtmlString](https://apireference.aspose.com/net/cells/aspose.cells/cell/methods/gethtmlstring) method and prints them on the console.

## Sample Code

## Console Output

{{< code lang="cs" >}}
Normal:
<Font Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</Font>

Html5:
<div Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</div>
{{< /code >}}

