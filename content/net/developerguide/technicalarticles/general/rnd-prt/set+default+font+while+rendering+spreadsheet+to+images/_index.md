---
title : "Set Default Font while rendering spreadsheet to images" 
description : "" 
weight : 20391 
toc : false
type: docs
url: /net/developerguide/technicalarticles/general/rnd-prt/set+default+font+while+rendering+spreadsheet+to+images/
---

# Aspose.Cells for .NET : Set Default Font while rendering spreadsheet to images


Please use the `ImageOrPrintOptions.DefaultFont` property to set the default font while rendering spreadsheet to images. This property will only be effective when the default font of workbook could not render your characters. The default font specified with `ImageOrPrintOptions.DefaultFont` property is used for all those cells which have invalid or non-existent fonts.

## Set Default Font while rendering spreadsheet to images

The following sample code creates a workbook, adds some text in cell A4 of first worksheet and sets its font to invalid or non-existent font. Then, it takes two images of the worksheet. The first image is taken by setting the `ImageOrPrintOptions.DefaultFont` property to `Courier New` and the second image is taken by setting the `ImageOrPrintOptions.DefaultFont` property to `Times New Roman`.

This is the output image after setting the `ImageOrPrintOptions.DefaultFont` property to `Courier New`.

![](https://docs2.aspose.com/cells/net/attachments/5024959/5115519.png)

This is the output image after setting the `ImageOrPrintOptions.DefaultFont` property to `Times New Roman`.

![](https://docs2.aspose.com/cells/net/attachments/5024959/5115515.png)

