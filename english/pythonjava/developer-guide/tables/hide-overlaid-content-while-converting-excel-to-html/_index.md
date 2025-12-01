---
title: Hide Overlaid Content while converting Excel to HTML
type: docs
weight: 40
url: /python-java/hide-overlaid-content-while-converting-excel-to/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Hide Overlaid Content while converting Excel to HTML**
When you save your Excel file to HTML, you can specify different cross types for cell strings. By default, Aspose.Cells generates HTML as per Microsoft Excel but when you change the [HtmlSaveOptions.HtmlCrossStringType](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#HtmlCrossStringType) to [CROSS_HIDE_RIGHT](https://reference.aspose.com/cells/python/asposecells.api/htmlcrosstype#CROSS_HIDE_RIGHT) then it hides all the strings at the right side of the cell which are overlaid or overlapping with cell string.

The following sample code loads the [sample Excel file](sampleHidingOverlaidContentWithCrossHideRight.xlsx) and saves it to [output HTML](HTML-outputHidingOverlaidContentWithCrossHideRight.zip) after setting the [HtmlSaveOptions.HtmlCrossStringType](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#HtmlCrossStringType) as [CROSS_HIDE_RIGHT](https://reference.aspose.com/cells/python/asposecells.api/htmlcrosstype#CROSS_HIDE_RIGHT). The screenshot explains how [CROSS_HIDE_RIGHT](https://reference.aspose.com/cells/python/asposecells.api/htmlcrosstype#CROSS_HIDE_RIGHT) affects the output HTML from the default output.

![todo:image_alt_text](Hiding-Overlaid-Content-With-CrossHideRight.png)
## **Sample Code**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "HTML-HidingOverlaidContentWithCrossHideRightWhileSavingToHtml.py" >}}
