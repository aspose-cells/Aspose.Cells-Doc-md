---
title: Hiding Overlaid Content with CrossHideRight while saving to HTML
type: docs
weight: 100
url: /net/hiding-overlaid-content-with-crosshideright-while-saving-to/
---

## **Possible Usage Scenarios**

When you save your Excel file to HTML, you can specify different cross types for cell strings. By default, Aspose.Cells generates HTML as per Microsoft Excel but when you change the cross type to [**CrossHideRight**](https://reference.aspose.com/cells/net/aspose.cells/htmlcrosstype), then it hides all the strings at the right side of the cell which are overlaid or overlapping with cell string.

## **Hiding Overlaid Content with CrossHideRight while saving to Html**

The following sample code loads the [sample Excel file](64716894.xlsx) and saves it to [output HTML](64716893.zip) after setting the [**HtmlSaveOptions.HtmlCrossStringType**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/htmlcrossstringtype) as [**CrossHideRight**](https://reference.aspose.com/cells/net/aspose.cells/htmlcrosstype). The screenshot explains how [**CrossHideRight**](https://reference.aspose.com/cells/net/aspose.cells/htmlcrosstype) affects the output HTML from default output.

![todo:image_alt_text](hiding-overlaid-content-with-crosshideright-while-saving-to-html_1.png)

## **Sample Code**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "HTML-HidingOverlaidContentWithCrossHideRightWhileSavingToHtml.cs" >}}
