---
title: Convert Worksheet to Image - Remove Whitespace around Data with Golang via C++
linktitle: Convert Worksheet to Image - Remove Whitespace around Data
type: docs
weight: 40
url: /go-cpp/convert-worksheet-to-image-remove-whitespace-around-data/
description: Learn how to convert a worksheet to an image and remove whitespace around the data using Aspose.Cells for Go via C++.
---

{{% alert color="primary" %}}

Sometimes, you need to present worksheet images in applications or web pages. For example, you might need to insert images into a Word document, a PDF file, a PowerPoint presentation, or some other document. Basically, you want to render a worksheet as an image so that it can be pasted into other applications. Aspose.Cells allows you to convert Microsoft Excel worksheets to images.

{{% /alert %}}

## **Remove Whitespace around Data**

The [**SheetRender**](https://reference.aspose.com/cells/go-cpp/sheetrender/) API converts a worksheet to an image file with any specified attributes, for example, image format, paginated sheets, etc. Several image formats are supported, including BMP, GIF, JPG, TIFF, and EMF.

When you use the sheet‑to‑image feature, the output image has whitespace—that is, a border—around it by default. You can remove this by setting the top, bottom, left, and right page‑setup margins for the source worksheet to 0 and specifying the [**ImageOrPrintOptions**](https://reference.aspose.com/cells/go-cpp/imageorprintoptions/) attributes accordingly.

The following code snippet removes the whitespace around the data in the output image.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ConvertWorksheetToImageRemoveWhitespaceAroundData.go" >}}
{{< app/cells/assistant language="go" >}}
