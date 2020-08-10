---
title: Hide Overlaid Content while converting Excel to HTML
type: docs
weight: 40
url: /pythonjava/hide-overlaid-content-while-converting-excel-to/
---

## **Hide Overlaid Content while converting Excel to HTML**
When you save your Excel file to HTML, you can specify different cross types for cell strings. By default, Aspose.Cells generates HTML as per Microsoft Excel but when you change the [HtmlSaveOptions.HtmlCrossStringType](https://apireference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#HtmlCrossStringType) to [CROSS_HIDE_RIGHT](https://apireference.aspose.com/cells/python/asposecells.api/htmlcrosstype#CROSS_HIDE_RIGHT) then it hides all the strings at the right side of the cell which are overlaid or overlapping with cell string.

The following sample code loads the [sample Excel file](https://docs.aspose.com/download/attachments/64456354/sampleHidingOverlaidContentWithCrossHideRight.xlsx?version=1&modificationDate=1525009682893&api=v2) and saves it to [output HTML](https://docs.aspose.com/download/attachments/64456354/HTML-outputHidingOverlaidContentWithCrossHideRight.zip?version=1&modificationDate=1525009682893&api=v2) after setting the [HtmlSaveOptions.HtmlCrossStringType](https://apireference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#HtmlCrossStringType) as [CROSS_HIDE_RIGHT](https://apireference.aspose.com/cells/python/asposecells.api/htmlcrosstype#CROSS_HIDE_RIGHT). The screenshot explains how [CROSS_HIDE_RIGHT](https://apireference.aspose.com/cells/python/asposecells.api/htmlcrosstype#CROSS_HIDE_RIGHT) affects the output HTML from the default output.

![todo:image_alt_text](https://docs.aspose.com/download/attachments/64456354/Hiding-Overlaid-Content-With-CrossHideRight.png?version=1&modificationDate=1525009682893&api=v2)
## **Sample Code**
{{< gist "aspose-com-gists" "f3cac13617c487b51b47cc9ae1d7c008" "HTML-HidingOverlaidContentWithCrossHideRightWhileSavingToHtml.py" >}}
