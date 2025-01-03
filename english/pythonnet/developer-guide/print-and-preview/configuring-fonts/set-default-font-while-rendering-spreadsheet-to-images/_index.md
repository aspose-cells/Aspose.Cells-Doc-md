---
title: Set Default Font while rendering spreadsheet to images
type: docs
weight: 360
url: /python-net/set-default-font-while-rendering-spreadsheet-to-images/
---

{{% alert color="primary" %}}

Please use the [**ImageOrPrintOptions.default_font**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/default_font) property to set the default font while rendering spreadsheets to images. This property will only be effective when the default font of the workbook could not render your characters. The default font specified with [**ImageOrPrintOptions.default_font**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/default_font) property is used for all those cells which have invalid or non-existent fonts.

{{% /alert %}}

## Set Default Font while rendering spreadsheet to images

The following sample code creates a workbook, adds some text in cell A4 of the first worksheet, and sets its font to invalid or non-existent font. Then, it takes two images of the worksheet. The first image is taken by setting the [**ImageOrPrintOptions.default_font**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/default_font) property to *Courier New* and the second image is taken by setting the [**ImageOrPrintOptions.default_font**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/default_font) property to *Times New Roman*.

This is the output image after setting the [**ImageOrPrintOptions.default_font**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/default_font) property to *Courier New*.

![todo:image_alt_text](1.png)

This is the output image after setting the [**ImageOrPrintOptions.default_font**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/default_font) property to *Times New Roman*.

![todo:image_alt_text](2.png)

## Sample Code

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-SetDefaultFontWhileRenderingSpreadsheet-1.cs" >}}

