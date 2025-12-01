---
title: Image
type: docs
weight: 300
url: /net/convert-excel-to-image/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---


{{% alert color="primary" %}}

Aspose.Cells allows you to export a worksheet from the workbook and convert it into different formats. This article explains how to convert a worksheet to different formats.

{{% /alert %}}

## Converting Workbook to TIFF

An Excel file can contain multiple sheets with multiple pages. [**WorkbookRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookrender) allows you to convert Excel to TIFF with multiple pages. Also, you can control multiple options for TIFF, like [Compression](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/tiffcompression), [Color depth](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/tiffcolordepth), Resolution([Horizontal resolution](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/horizontalresolution), [Vertical resolution](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/verticalresolution)).

The following code snippet shows how to convert Excel to TIFF with multiple pages. The [source Excel file](workbook-to-tiff-with-mulitiple-pages.xlsx) and [generated TIFF image](workbook-to-tiff-with-mulitiple-pages.tiff) are attached for your reference.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Workbook-To-Tiff-With-Mulitiple-Pages.cs" >}}

## **Converting Worksheet to Image**

Worksheets contain data that you want to analyze. For example, a worksheet can contain parameters, totals, percentages, exceptions, and calculations.

As a developer, you might need to present worksheets as images. For example, you might need to use an image of a worksheet in an application or web page. You might want to insert an image into a Microsoft Word document, a PDF file, a PowerPoint presentation or some other document type. Simply put, you want a worksheet rendered as an image so that you can use it somewhere else.

Aspose.Cells supports converting Excel worksheets to images. To use this feature, you need to import the [**Aspose.Cells.Rendering**](https://reference.aspose.com/cells/net/aspose.cells.rendering) namespace to your program or project. It has several valuable classes for rendering and printing, for example [**SheetRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender), [**ImageOrPrintOptions**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions), [**WorkbookRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookrender), and others.

The [**SheetRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender) class represents a worksheet to render as images. It has an overloaded method, [**ToImage**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender/methods/toimage/index), that can convert a worksheet to image file(s) with different attributes or options. It returns a System.Drawing.Bitmap object and you can save an image file to disk or stream. Several image formats are supported, for example BMP, PNG, GIF, JPG, JPEG, TIFF, EMF.

The following code snippet shows how to convert a worksheet in an Excel file to an image file.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ConvertingWorksheetToImage-ConvertWorksheetToImageByPage-1.cs" >}}

{{% alert color="primary" %}}

At present, the API for converting worksheets to images does not support 3D bubble charts.

{{% /alert %}}

## **Converting Worksheet to SVG**

SVG stands for Scalable Vector Graphics. SVG is a specification based on XML standards for two-dimensional vector graphics. It is an open standard that has been under development by the World Wide Web Consortium (W3C) since 1999.

Aspose.Cells for .NET has been able to convert worksheets to SVG image since version 7.1.0. The following code snippet shows how to convert a worksheet in an Excel file to an SVG image file.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ConvertingWorksheetToImage-ConvertWorksheetToSVG-1.cs" >}}

## **Advance topics**
- [Convert an Excel Chart to Image](/cells/net/convert-an-excel-chart-to-image/)
- [Converting Chart to Image in SVG Format](/cells/net/converting-chart-to-image-in-svg-format/)
- [Export Chart to SVG with viewBox attribute](/cells/net/export-chart-to-svg-with-viewbox-attribute/)
- [Track Conversion Progress of Excel to TIFF](/cells/net/track-conversion-progress-of-excel-to-tiff/)
{{< app/cells/assistant language="csharp" >}}
