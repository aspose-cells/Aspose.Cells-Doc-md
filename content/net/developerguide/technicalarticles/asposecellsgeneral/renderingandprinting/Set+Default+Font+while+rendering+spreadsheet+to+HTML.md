+++
title = "Set Default Font while rendering spreadsheet to HTML" 
description = "" 
weight = 20392 
+++

Aspose.Cells for .NET : Set Default Font while rendering spreadsheet to HTML  

# Aspose.Cells for .NET : Set Default Font while rendering spreadsheet to HTML


Aspose.Cells allows you to set default font while rendering spreadsheet to HTML. Please use the `HtmlSaveOptions.DefaultFontName` for this purpose. This property is useful when there are some cells in spreadsheet that has invalid or non-existing fonts. Then those cells will be rendered in a font specified with `HtmlSaveOptions.DefaultFontName` property.

## Set Default Font while rendering spreadsheet to HTML

The following sample code creates a workbook and adds some text in cell B4 of first worksheet and sets its font to some unknown/non-existing font. Then it saves the workbook in HTML by setting different default font names like Courier New, Arial, Times New Roman etc.

The screenshot shows the effect of setting different default font names via `HtmlSaveOptions.DefaultFontName` property.

![](https://docs2.aspose.com/cells/net/attachments/5024958/5115507.png)

The code generates the [output HTML file with Courier New](https://docs2.aspose.com/cells/net/attachments/5024958/5115516.htm), the [output HTML with Arial](https://docs2.aspose.com/cells/net/attachments/5024958/5115518.htm) and the [output HTML file with Times New Roman](https://docs2.aspose.com/cells/net/attachments/5024958/5115517.htm).

## Attachments:

![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [effect-of-setting-different-default-fonts.png](https://docs2.aspose.com/cells/net/attachments/5024958/5115507.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [sample.xlsx](https://docs2.aspose.com/cells/net/attachments/5024958/5115506.xlsx) (application/unknown)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [out\_courier\_new.htm](https://docs2.aspose.com/cells/net/attachments/5024958/5115516.htm) (text/html)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [out\_times\_new\_roman.htm](https://docs2.aspose.com/cells/net/attachments/5024958/5115517.htm) (text/html)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [out\_arial.htm](https://docs2.aspose.com/cells/net/attachments/5024958/5115518.htm) (text/html)  

