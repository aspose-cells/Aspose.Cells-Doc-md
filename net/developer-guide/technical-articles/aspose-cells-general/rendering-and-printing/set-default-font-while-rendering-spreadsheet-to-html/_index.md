---
title: Set Default Font while rendering spreadsheet to HTML
type: docs
weight: 370
url: /net/set-default-font-while-rendering-spreadsheet-to-html/
---

{{% alert color="primary" %}} 

Aspose.Cells allows you to set default font while rendering spreadsheet to HTML. Please use the [HtmlSaveOptions.DefaultFontName](https://apireference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/defaultfontname) for this purpose. This property is useful when there are some cells in a spreadsheet that have invalid or non-existing fonts. Then those cells will be rendered in a font specified with the [HtmlSaveOptions.DefaultFontName](https://apireference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/defaultfontname) property.

{{% /alert %}} 
## **Set Default Font while rendering spreadsheet to HTML**
The following sample code creates a workbook and adds some text in cell B4 of the first worksheet and sets its font to some unknown/non-existing font. Then it saves the workbook in HTML by setting different default font names like Courier New, Arial, Times New Roman, etc.

The screenshot shows the effect of setting different default font names via [HtmlSaveOptions.DefaultFontName](https://apireference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/defaultfontname) property.

![todo:image_alt_text](set-default-font-while-rendering-spreadsheet-to-html_1.png)

The code generates the [output HTML file with Courier New](attachments/5024958/5115516.htm), the [output HTML with Arial](attachments/5024958/5115518.htm), and the [output HTML file with Times New Roman](attachments/5024958/5115517.htm).



{{< gist "aspose-com-gists" "24a8eac23c3325e20dababecf735a43b" "Examples-CSharp-Articles-RenderingAndPrinting-SetDefaultFontWhileRendering-1.cs" >}}