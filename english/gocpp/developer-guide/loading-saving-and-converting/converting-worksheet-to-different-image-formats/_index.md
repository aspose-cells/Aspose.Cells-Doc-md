---
title: Converting Worksheet to Different Image Formats
type: docs
weight: 90
url: /go-cpp/converting-worksheet-to-different-image-formats/
---

{{% alert color="primary" %}}

Aspose.Cells allows you to export a worksheet from a workbook and convert it into different image formats. This article explains how to convert a worksheet to different image formats.

{{% /alert %}}

## **Converting Worksheet to Image**

Worksheets contain data that you want to analyze. For example, a worksheet can contain parameters, totals, percentages, exceptions, and calculations.

As a developer, you might need to present worksheets as images. For example, you might need to use an image of a worksheet in an application or web page. You might want to insert an image into a Microsoft Word document, a PDF file, a PowerPoint presentation, or some other document type. Simply put, you want a worksheet rendered as an image so that you can use it somewhere else.

Aspose.Cells supports converting Excel worksheets to images. To use this feature, you need to import the [Aspose.Cells.Rendering](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/) namespace **into** your program or project. It has several valuable classes for rendering and printing, for example, [SheetRender](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/), [ImageOrPrintOptions](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/), and others.

The `Aspose.Cells.Rendering.ISheetRender` class represents a worksheet to render as images. It has an overloaded method, [ToImage](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/toimage/), that can convert a worksheet to image file(s) with different attributes or options. Several image formats are supported, for example, BMP, PNG, GIF, JPG, JPEG, TIFF, and EMF.

The following code snippet shows how to convert a worksheet in an Excel file to an image file.

### **convert Excel/spreadsheet to PNG with GoLang**

Please see the following sample code, its [sample Excel file](67338402.xlsx), and the [output PNG Images](67338401.zip).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ConvertWorksheetToImage_Png.go" >}}

### **convert Excel/spreadsheet to TIFF with GoLang**

Please see the following sample code, its [sample Excel file](67338402.xlsx), and the [output TIFF Image](67338419.zip).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ConvertWorksheetToImage_Tiff.go" >}}

## **convert Excel/spreadsheet to SVG with GoLang**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ConvertWorksheetToImage_Svg.go" >}}

SVG stands for Scalable Vector Graphics. SVG is a specification based on XML standards for two‑dimensional vector graphics. It is an open standard that has been under development by the World Wide Web Consortium (W3C) since 1999.

Aspose.Cells for Go via C++ has been able to convert worksheets to SVG images since version 24.12.0.

To use this feature, import the `Aspose.Cells.Rendering` namespace **into** your program or project. It has several valuable classes for rendering and printing, for example, `ISheetRender`, `IImageOrPrintOptions`, and others.

The `Aspose.Cells.Rendering.IImageOrPrintOptions` class specifies that the worksheet will be saved in SVG format. The following code snippet shows how to convert a worksheet in an Excel file to an SVG image file.

Please see the following sample code, its [sample Excel file](67338402.xlsx), and the [output SVG Images](67338403.zip).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ConvertWorksheetToImage_SVG.go" >}}