---
title: Hiding Overlaid Content with CrossHideRight while saving to HTML
type: docs
weight: 100
url: /net/hiding-overlaid-content-with-crosshideright-while-saving-to/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**

When you save your Excel file to HTML, you can specify different cross types for cell strings. By default, Aspose.Cells generates HTML as per Microsoft Excel, but when you change the cross type to **CrossHideRight**[https://reference.aspose.com/cells/net/aspose.cells/htmlcrosstype], it hides all the strings on the right side of the cell that are overlaid or overlapping with other cell strings.

## **Hiding Overlaid Content with CrossHideRight while saving to HTML**

The following sample code loads the [sample Excel file](64716894.xlsx) and saves it to [output HTML](64716893.zip) after setting the **HtmlSaveOptions.HtmlCrossStringType**[https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/htmlcrossstringtype] to **CrossHideRight**[https://reference.aspose.com/cells/net/aspose.cells/htmlcrosstype]. The screenshot explains how **CrossHideRight** affects the output HTML compared to the default output.

![todo:image_alt_text](hiding-overlaid-content-with-crosshideright-while-saving-to-html_1.png)

## **Sample Code**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "HTML-HidingOverlaidContentWithCrossHideRightWhileSavingToHtml.cs" >}}
{{< app/cells/assistant language="csharp" >}}
