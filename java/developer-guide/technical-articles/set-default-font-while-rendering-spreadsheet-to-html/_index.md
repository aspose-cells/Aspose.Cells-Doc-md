---
title: Set Default Font while rendering spreadsheet to HTML
type: docs
weight: 830
url: /java/set-default-font-while-rendering-spreadsheet-to/
---

{{% alert color="primary" %}} 

Aspose.Cells allows you to set default font while rendering spreadsheet to HTML. Please use the [HtmlSaveOptions.DefaultFontName](https://apireference.aspose.com/java/cells/com.aspose.cells/htmlsaveoptions#DefaultFontName) for this purpose. This property is useful when there are some cells in a spreadsheet that have invalid or non-existing fonts. Then those cells will be rendered in a font specified with [HtmlSaveOptions.DefaultFontName](https://apireference.aspose.com/java/cells/com.aspose.cells/htmlsaveoptions#DefaultFontName) property.

{{% /alert %}} 
#### **Set Default Font while rendering spreadsheet to HTML**
The following sample code creates a workbook and adds some text in cell B4 of the first worksheet and sets its font to some unknown/non-existing font. Then it saves the workbook in HTML by setting different default font names like Courier New, Arial, Times New Roman, etc.

The screenshot shows the effect of setting different default font names via [HtmlSaveOptions.DefaultFontName](https://apireference.aspose.com/java/cells/com.aspose.cells/htmlsaveoptions#DefaultFontName) property.

![todo:image_alt_text](set-default-font-while-rendering-spreadsheet-to-html_1.png)

The code generates the [output HTML file with Courier New](attachments/5276008/5472568.htm), the [output HTML with Arial](attachments/5276008/5472567.htm) and the [output HTML file with Times New Roman](attachments/5276008/5472565.htm).

{{< gist "aspose-com-gists" "439a68a5e4305388c50ca306ef238de5" "Examples-src-main-java-com-aspose-cells-examples-files-utility-SetDefaultFontWhileRenderingSpreadsheetToHTML-.java" >}}
