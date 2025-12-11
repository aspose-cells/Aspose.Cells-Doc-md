---
title: Set Default Font while Rendering a Spreadsheet to Images
type: docs
weight: 360
url: /python-net/set-default-font-while-rendering-spreadsheet-to-images/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Please use the [**ImageOrPrintOptions.default_font**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/default_font) property to set the default font while rendering spreadsheets to images. This property will only be effective when the workbook's default font cannot render your characters. The default font specified with [**ImageOrPrintOptions.default_font**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/default_font) property is used for all cells that have invalid or non‑existent fonts.

{{% /alert %}}

## Set Default Font while Rendering a Spreadsheet to Images

The following sample code creates a workbook, adds some text in cell A4 of the first worksheet, and sets its font to an invalid or non‑existent font. Then, it generates two images of the worksheet. The first image is created by setting the [**ImageOrPrintOptions.default_font**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/default_font) property to *Courier New*, and the second image is created by setting the same property to *Times New Roman*.

This is the output image after setting the [**ImageOrPrintOptions.default_font**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/default_font) property to *Courier New*.

![todo:image_alt_text](1.png)

This is the output image after setting the [**ImageOrPrintOptions.default_font**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/default_font) property to *Times New Roman*.

![todo:image_alt_text](2.png)

## Sample Code

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-SetDefaultFontWhileRenderingSpreadsheet-1.cs" >}}

{{< app/cells/assistant language="python-net" >}}
