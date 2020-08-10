---
title: Hiding Overlaid Content with CrossHideRight while saving to Html
type: docs
weight: 100
url: /net/hiding-overlaid-content-with-crosshideright-while-saving-to/
---

## **Possible Usage Scenarios**
When you save your Excel file to HTML, you can specify different cross types for cell strings. By default, Aspose.Cells generates HTML as per Microsoft Excel but when you change the cross type to [CrossHideRight](https://apireference.aspose.com/net/cells/aspose.cells/htmlcrosstype), then it hides all the strings at the right side of the cell which are overlaid or overlapping with cell string.
## **Hiding Overlaid Content with CrossHideRight while saving to Html**
The following sample code loads the [sample Excel file](attachments/64456179/64716894.xlsx) and saves it to [output HTML](attachments/64456179/64716893.zip) after setting the [HtmlSaveOptions.HtmlCrossStringType](https://apireference.aspose.com/net/cells/aspose.cells/htmlsaveoptions/properties/htmlcrossstringtype) as [CrossHideRight](https://apireference.aspose.com/net/cells/aspose.cells/htmlcrosstype). The screenshot explains how [CrossHideRight](https://apireference.aspose.com/net/cells/aspose.cells/htmlcrosstype) affects the output HTML from default output.

![todo:image_alt_text](hiding-overlaid-content-with-crosshideright-while-saving-to-html_1.png)
## **Sample Code**
{{< gist "aspose-com-gists" "24a8eac23c3325e20dababecf735a43b" "HTML-HidingOverlaidContentWithCrossHideRightWhileSavingToHtml.cs" >}}
