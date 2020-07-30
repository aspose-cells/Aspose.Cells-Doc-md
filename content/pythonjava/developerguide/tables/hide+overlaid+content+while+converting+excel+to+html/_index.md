---
title : "Hide Overlaid Content while converting Excel to HTML" 
description : "" 
weight : 12040 
toc : false
type: docs
url: /pythonjava/developerguide/tables/hide+overlaid+content+while+converting+excel+to+html/
---

# Aspose.Cells for Python via Java : Hide Overlaid Content while converting Excel to HTML


{{< panel title="Contents Summary" style="primary" >}}
*   1 [Hide Overlaid Content while converting Excel to HTML](#hide-overlaid-content-while-converting-excel-to-html)
*   2 [Sample Code](#sample-code)
{{< /panel >}}
 

 

## Hide Overlaid Content while converting Excel to HTML

When you save your Excel file to HTML, you can specify different cross types for cell strings. By default, Aspose.Cells generates HTML as per Microsoft Excel but when you change the [HtmlSaveOptions.HtmlCrossStringType](https://apireference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#HtmlCrossStringType) to [CROSS\_HIDE\_RIGHT](https://apireference.aspose.com/cells/python/asposecells.api/htmlcrosstype#CROSS_HIDE_RIGHT) then it hides all the strings at the right side of the cell which are overlaid or overlapping with cell string.

The following sample code loads the [sample Excel file](https://docs.aspose.com/download/attachments/64456354/sampleHidingOverlaidContentWithCrossHideRight.xlsx?version=1&modificationDate=1525009682893&api=v2) and saves it to [output HTML](https://docs.aspose.com/download/attachments/64456354/HTML-outputHidingOverlaidContentWithCrossHideRight.zip?version=1&modificationDate=1525009682893&api=v2) after setting the [HtmlSaveOptions.HtmlCrossStringType](https://apireference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#HtmlCrossStringType) as [CROSS\_HIDE\_RIGHT](https://apireference.aspose.com/cells/python/asposecells.api/htmlcrosstype#CROSS_HIDE_RIGHT). The screenshot explains how [CROSS\_HIDE\_RIGHT](https://apireference.aspose.com/cells/python/asposecells.api/htmlcrosstype#CROSS_HIDE_RIGHT) affects the output HTML from the default output.

![](https://docs.aspose.com/download/attachments/64456354/Hiding-Overlaid-Content-With-CrossHideRight.png?version=1&modificationDate=1525009682893&api=v2)

## Sample Code

