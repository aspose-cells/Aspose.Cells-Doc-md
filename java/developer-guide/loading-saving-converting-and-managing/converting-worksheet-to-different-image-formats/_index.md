---
title: Converting Worksheet to Different Image Formats
type: docs
weight: 30
url: /java/converting-worksheet-to-different-image-formats/
---

{{% alert color="primary" %}}

Aspose.Cells allows you to export a worksheet from the workbook and convert it into different formats. This article explains how to convert a worksheet to different formats.

{{% /alert %}}

## **Converting Worksheet to Image**

Sometimes, it is useful to save a picture of a worksheet. Images can be shared online, inserted into other documents (reports written in Microsoft Word, for example, or PowerPoint presentations).

Aspose.Cells provides image export through the **[SheetRender](https://apireference.aspose.com/cells/java/com.aspose.cells/sheetrender)** class. This class represents the worksheet that will be rendered to an image. The **[SheetRender](https://apireference.aspose.com/cells/java/com.aspose.cells/sheetrender)** class provides the **[toImage()](https://apireference.aspose.com/cells/java/com.aspose.cells/sheetrender#toImage(int,%20java.io.OutputStream))** method for converting a worksheet to an image file. BMP, PNG, JPEG, TIFF, and EMF formats are supported.

{{% alert color="primary" %}}

Aspose.Cells for Java also supports conversion to TIFF format. To convert a worksheet to a TIFF image, add the JAI library to your classpath.

{{% /alert %}} {{% alert color="primary" %}}

At present, the converting worksheet to image API does not support 3D-bubble charts.

{{% /alert %}}

The code below shows how to convert a worksheet in a Microsoft Excel file to a PNG file.

{{< gist "aspose-com-gists" "439a68a5e4305388c50ca306ef238de5" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-WorksheetToImage-1.java" >}}

## **Converting Worksheet to SVG**

SVG stands for **Scalable Vector Graphics**. SVG is a specification based on XML standards for two-dimensional vector graphics. It is an open standard that has been under development by the World Wide Web Consortium (W3C) since 1999.

Since the release of v7.1.0, **Aspose.Cells for Java** can convert worksheets into SVG images.

To use this feature, you need to import the com.aspose.cells namespace to your program or project. It has several valuable classes for rendering and printing, for example, **[SheetRender](https://apireference.aspose.com/cells/java/com.aspose.cells/sheetrender)**, **[ImageOrPrintOptions](https://apireference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions)**, **[WorkbookRender](https://apireference.aspose.com/cells/java/com.aspose.cells/workbookrender)**, and others.

The **[com.aspose.cells.ImageOrPrintOptions](https://apireference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions)** class specifies that the worksheet will be saved in SVG format.

The **[SheetRender](https://apireference.aspose.com/cells/java/com.aspose.cells/sheetrender)** class takes the object of **[ImageOrPrintOptions](https://apireference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions)** as a parameter that sets the save format to SVG format.

The following code snippet shows how to convert a worksheet in an Excel file to an SVG image file.

{{< gist "aspose-com-gists" "439a68a5e4305388c50ca306ef238de5" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-ConvertingWorksheetToSVG-ConvertingWorksheetToSVG.java" >}}

### **Render active worksheet in a workbook**

A simple way to convert active worksheet in a workbook is to set the active sheet index and then save the workbook as SVG. It will render the active sheet to SVG. Following sample code demonstrates this feature:

{{< gist "aspose-com-gists" "439a68a5e4305388c50ca306ef238de5" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-ConvertActiveWorksheetToSVG-1.java" >}}

## Related Articles

- [Export Chart to SVG with viewBox attribute](/cells/java/export-chart-to-svg-with-viewbox-attribute/)
- [Export Worksheet or Chart into Image with Desired Width and Height](/cells/java/export-worksheet-or-chart-into-image-with-desired-width-and-height/)
- [Converting Worksheet to Image and Worksheet to Image by Page](/cells/java/converting-worksheet-to-image-and-worksheet-to-image-by-page/)
