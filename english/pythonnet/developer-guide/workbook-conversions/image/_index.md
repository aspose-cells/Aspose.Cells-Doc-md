---
title: Image
type: docs
weight: 300
url: /python-net/convert-excel-to-image/
description: Convert Chart to Image using Aspose.Cells for Python via .NET API.
keywords: Python Convert Chart to Image, Export Chart to Image in Python via NET, Python Save Chart to Image.
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells for Python via .NET allows you to export a worksheet from the workbook and convert it into different formats. This article explains how to convert a worksheet to different formats.

{{% /alert %}}

## Converting Workbook to TIFF

An Excel file can contain multiple sheets with multiple pages. [**WorkbookRender**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/workbookrender) allows you to convert Excel to TIFF with multiple pages. You can also control various options for TIFF, such as [Compression](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/tiff_compression/), [Color depth](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/tiff_color_depth/), and Resolution ([Horizontal resolution](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/horizontal_resolution/), [Vertical resolution](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/vertical_resolution/)).

The following code snippet shows how to convert Excel to TIFF with multiple pages. The [source Excel file](workbook-to-tiff-with-multiple-pages.xlsx) and [generated TIFF image](workbook-to-tiff-with-multiple-pages.tiff) are attached for your reference.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Workbook-To-Tiff-With-Multiple-Pages.py" >}}

## **Converting Worksheet to Image**

Worksheets contain data that you want to analyze. For example, a worksheet can contain parameters, totals, percentages, exceptions, and calculations.

As a developer, you might need to present worksheets as images. For instance, you may want to use an image of a worksheet in an application or web page, insert it into a Microsoft Word document, a PDF file, a PowerPoint presentation, or another document type. Simply put, you need a worksheet rendered as an image so that you can use it elsewhere.

Aspose.Cells for Python via .NET supports converting Excel worksheets to images. To use this feature, import the [**aspose.cells.rendering**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/) namespace into your program or project. It provides several valuable classes for rendering and printing, such as [**SheetRender**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender/), [**ImageOrPrintOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/), [**WorkbookRender**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/workbookrender/), and others.

The [**SheetRender**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender/) class represents a worksheet to be rendered as images. It has an overloaded method, [**to_image**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender/to_image/#int-str), which can convert a worksheet to image file(s) with different attributes or options. It returns a `System.Drawing.Bitmap` object, and you can save the image file to disk or a stream. Several image formats are supported, for example BMP, PNG, GIF, JPG, JPEG, TIFF, and EMF.

The following code snippet shows how to convert a worksheet in an Excel file to an image file.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheet-ConvertWorksheetToImageByPage-1.py" >}}

{{% alert color="primary" %}}

At present, the API for converting worksheets to images does not support 3D bubble charts.

{{% /alert %}}

## **Converting Worksheet to SVG**

SVG stands for Scalable Vector Graphics. SVG is a specification based on XML standards for two‑dimensional vector graphics. It is an open standard that has been under development by the World Wide Web Consortium (W3C) since 1999.

Aspose.Cells for Python via .NET has been able to convert worksheets to SVG images since version 7.1.0. The following code snippet shows how to convert a worksheet in an Excel file to an SVG image file.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheet-ConvertWorksheetToSVG-1.py" >}}

## **Advanced topics**
- [Convert an Excel Chart to Image](/cells/python-net/convert-an-excel-chart-to-image/)
- [Converting Chart to Image in SVG Format](/cells/python-net/converting-chart-to-image-in-svg-format/)
- [Export Chart to SVG with viewBox attribute](/cells/python-net/export-chart-to-svg-with-viewbox-attribute/)

{{< app/cells/assistant language="python-net" >}}
