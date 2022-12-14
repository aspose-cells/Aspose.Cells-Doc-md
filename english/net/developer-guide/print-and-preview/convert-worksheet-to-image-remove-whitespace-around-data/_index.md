---
title: Convert Worksheet to Image - Remove whitespace around data
type: docs
weight: 40
url: /net/convert-worksheet-to-image-remove-whitespace-around-data/
---

{{% alert color="primary" %}}

Sometimes, you need to present worksheet images in applications or web pages. For example, you might need to insert images into a Word document, a PDF file, a PowerPoint presentation, or some other document. Basically, you want to render a worksheet as an image so that it can be pasted into other applications. Aspose.Cells allows you to convert Microsoft Excel worksheets to images.

{{% /alert %}}

## **Remove Whitespace around Data**

The [**Aspose.Cells.Rendering.SheetRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender) API converts a worksheet to an image file with any specified attributes, for example, image format, paginated sheets, etc. Several image formats are supported, including BMP, GIF, JPG, TIFF, and EMF.

When you use the sheet-to-image feature, the output image has whitespace, that is, a border, around it by default. You can remove this by setting the top, bottom, left and right page setup margins for the source worksheet to 0 and specify [**Aspose.Cells.Rendering.ImageOrPrintOptions**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions) attributes accordingly.

The following code snippet removes the whitespace around the data in the output image.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RemoveWhitespaceAroundData-1.cs" >}}

