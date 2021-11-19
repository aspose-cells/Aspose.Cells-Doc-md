---
title: Convert Excel to HTML with tooltip
type: docs
weight: 200
url: /net/convert-excel-to-html-with-tooltip/
aliases: [/net/convert-excel-to-html/]
---

## **Convert Excel to HTML with tooltip**

There might be cases where the text is cut off in the generated HTML and you want to display the complete text as a tooltip on the hover event. Aspose.Cells supports this by providing **[HtmlSaveOptions.AddTooltipText](https://apireference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/addtooltiptext)** property. Setting the **[HtmlSaveOptions.AddTooltipText](https://apireference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/addtooltiptext)** property to **true** will add the complete text as a tooltip in the generated HTML.

The following image shows the tooltip in the generated HTML file.

![todo:image_alt_text](convert-excel-to-html-with-tooltip_1.jpg)

The following code sample loads the [source excel file](98107416.xlsx) and generates the [output HTML file](98107417.zip) with the tooltip.

Sample Code

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-ConvertExcelFileToHtmlWithTooltip-1.cs" >}}
