---
title : "Converting Worksheet to Different Image Formats" 
description : "" 
weight : 12019 
toc : false
type: docs
url: /cpp/developerguide/ld-sv-cvt/converting+worksheet+to+different+image+formats/
---

# Aspose.Cells for C++ : Converting Worksheet to Different Image Formats


Aspose.Cells allows you to export a worksheet from a workbook and convert it into different image formats. This article explains how to convert a worksheet to different image formats.

{{< panel title="Contents Summary" style="primary" >}}
*   1 [Converting Worksheet to Image](#converting-worksheet-to-image)
    *   1.1 [PNG Format](#png-format)
    *   1.2 [TIFF Format](#tiff-format)
*   2 [Converting Worksheet to SVG](#converting-worksheet-to-svg)
{{< /panel >}}
 

## Converting Worksheet to Image

Worksheets contain data that you want to analyze. For example, a worksheet can contain parameters, totals, percentages, exceptions, and calculations.

As a developer, you might need to present worksheets as images. For example, you might need to use an image of a worksheet in an application or web page. You might want to insert an image into a Microsoft Word document, a PDF file, a PowerPoint presentation or some other document type. Simply put, you want a worksheet rendered as an image so that you can use it somewhere else.

Aspose.Cells supports converting Excel worksheets to images. To use this feature, you need to import the [Aspose.Cells.Rendering](https://apireference.aspose.com/cpp/cells/namespace/aspose.cells.rendering/) namespace to your program or project. It has several valuable classes for rendering and printing, for example, [ISheetRender](https://apireference.aspose.com/cpp/cells/class/aspose.cells.rendering.i_sheet_render/), [IImageOrPrintOptions](https://apireference.aspose.com/cpp/cells/class/aspose.cells.rendering.i_image_or_print_options/) and others.

The [Aspose.Cells.Rendering.ISheetRender](https://apireference.aspose.com/cpp/cells/class/aspose.cells.rendering.i_sheet_render/) class represents a worksheet to render as images. It has an overloaded method, [ToImage](https://apireference.aspose.com/cpp/cells/class/aspose.cells.rendering.i_sheet_render/#ae508827a76d0c353ab0890024ec363c5), that can convert a worksheet to image file(s) with different attributes or options. Several image formats are supported, for example, BMP, PNG, GIF, JPG, JPEG, TIFF, EMF.

The following code snippet shows how to convert a worksheet in an Excel file to an image file.

### PNG Format

Please see the following sample code, its [sample Excel file](https://docs2.aspose.com/cells/cpp/attachments/66946350/67338402.xlsx), and the [output PNG Images](https://docs2.aspose.com/cells/cpp/attachments/66946350/67338401.zip).

### TIFF Format

Please see the following sample code, its [sample Excel file](https://docs2.aspose.com/cells/cpp/attachments/66946350/67338402.xlsx), and the [output TIFF Image](https://docs2.aspose.com/cells/cpp/attachments/66946350/67338419.zip).

## Converting Worksheet to SVG

SVG stands for Scalable Vector Graphics. SVG is a specification based on XML standards for two-dimensional vector graphics. It is an open standard that has been under development by the World Wide Web Consortium (W3C) since 1999.

Aspose.Cells for C++ has been able to convert worksheets to SVG image since version 18.5.0.

To use this feature, import the [Aspose.Cells.Rendering](https://apireference.aspose.com/cpp/cells/namespace/aspose.cells.rendering/) namespace to your program or project. It has several valuable classes for rendering and printing, for example, [ISheetRender](https://apireference.aspose.com/cpp/cells/class/aspose.cells.rendering.i_sheet_render/), [IImageOrPrintOptions](https://apireference.aspose.com/cpp/cells/class/aspose.cells.rendering.i_image_or_print_options/), and others.

The [Aspose.Cells.Rendering.IImageOrPrintOptions](https://apireference.aspose.com/cpp/cells/class/aspose.cells.rendering.i_image_or_print_options/) class specifies that the worksheet will be saved in SVG format. The following code snippet shows how to convert a worksheet in an Excel file to an SVG image file

Please see the following sample code, its [sample Excel file](https://docs2.aspose.com/cells/cpp/attachments/66946350/67338402.xlsx), and the [output SVG Images](https://docs2.aspose.com/cells/cpp/attachments/66946350/67338403.zip).

