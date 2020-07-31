---
title : "Set Default Font while rendering spreadsheet to HTML" 
description : "" 
weight : 12550 
toc : false
type: docs
url: /java/developerguide/technicalarticles/set+default+font+while+rendering+spreadsheet+to+html/
---

# Aspose.Cells for Java : Set Default Font while rendering spreadsheet to HTML


Aspose.Cells allows you to set default font while rendering spreadsheet to HTML. Please use the [HtmlSaveOptions.DefaultFontName](https://apireference.aspose.com/java/cells/com.aspose.cells/htmlsaveoptions#DefaultFontName) for this purpose. This property is useful when there are some cells in a spreadsheet that have invalid or non-existing fonts. Then those cells will be rendered in a font specified with [HtmlSaveOptions.DefaultFontName](https://apireference.aspose.com/java/cells/com.aspose.cells/htmlsaveoptions#DefaultFontName) property.

#### Set Default Font while rendering spreadsheet to HTML

The following sample code creates a workbook and adds some text in cell B4 of the first worksheet and sets its font to some unknown/non-existing font. Then it saves the workbook in HTML by setting different default font names like Courier New, Arial, Times New Roman, etc.

The screenshot shows the effect of setting different default font names via [HtmlSaveOptions.DefaultFontName](https://apireference.aspose.com/java/cells/com.aspose.cells/htmlsaveoptions#DefaultFontName) property.

![](https://docs2.aspose.com/cells/java/attachments/5276008/5472566.png)

The code generates the [output HTML file with Courier New](https://docs2.aspose.com/cells/java/attachments/5276008/5472568.htm), the [output HTML with Arial](https://docs2.aspose.com/cells/java/attachments/5276008/5472567.htm) and the [output HTML file with Times New Roman](https://docs2.aspose.com/cells/java/attachments/5276008/5472565.htm).


