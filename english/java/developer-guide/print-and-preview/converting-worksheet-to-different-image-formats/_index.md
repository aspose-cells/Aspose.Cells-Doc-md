---
title: Converting Worksheet to Different Image Formats
type: docs
weight: 30
url: /java/converting-worksheet-to-different-image-formats/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells allows you to export a worksheet from the workbook and convert it into different formats. This article explains how to convert a worksheet to different formats.

{{% /alert %}}

## **Converting Worksheet to Image**

Sometimes, it is useful to save a picture of a worksheet. Images can be shared online, inserted into other documents (reports written in Microsoft Word, for example, or PowerPoint presentations).

Aspose.Cells provides image export through the [**SheetRender**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender) class. This class represents the worksheet that will be rendered to an image. The [**SheetRender**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender) class provides the [**toImage()**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender#toImage-int-java.io.OutputStream-) method for converting a worksheet to an image file. BMP, PNG, JPEG, TIFF, and EMF formats are supported.

{{% alert color="primary" %}}

Aspose.Cells for Java also supports conversion to TIFF format. To convert a worksheet to a TIFF image, add the JAI library to your classpath.

{{% /alert %}} {{% alert color="primary" %}}

At present, the worksheet-to-image conversion API does not support 3D-bubble charts.

{{% /alert %}}

The code below shows how to convert a worksheet in a Microsoft Excel file to a PNG file.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-WorksheetToImage-1.java" >}}

## **Converting Worksheet to SVG**

SVG stands for **Scalable Vector Graphics**. SVG is a specification based on XML standards for two-dimensional vector graphics. It is an open standard that has been under development by the World Wide Web Consortium (W3C) since 1999.

Since the release of v7.1.0, **Aspose.Cells for Java** can convert worksheets into SVG images.

To use this feature, you need to import the com.aspose.cells namespace to your program or project. It has several valuable classes for rendering and printing, for example, [**SheetRender**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender), [**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions), [**WorkbookRender**](https://reference.aspose.com/cells/java/com.aspose.cells/workbookrender), and others.

The [**com.aspose.cells.ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions) class specifies that the worksheet will be saved in SVG format.

The [**SheetRender**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender) class takes an [**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions) object as a parameter, which sets the save format to SVG.

The following code snippet shows how to convert a worksheet in an Excel file to an SVG image file.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-ConvertingWorksheetToSVG-ConvertingWorksheetToSVG.java" >}}

### **Render active worksheet in a workbook**

A simple way to convert the active worksheet in a workbook is to set the active sheet index and then save the workbook as SVG. It will render the active sheet to SVG. Following sample code demonstrates this feature:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-ConvertActiveWorksheetToSVG-1.java" >}}

## Related Articles

- [Export Chart to SVG with viewBox attribute](/cells/java/export-chart-to-svg-with-viewbox-attribute/)
- [Export Worksheet or Chart into Image with Desired Width and Height](/cells/java/export-worksheet-or-chart-into-image-with-desired-width-and-height/)
- [Converting Worksheet to Image and Worksheet to Image by Page](/cells/java/converting-worksheet-to-image-and-worksheet-to-image-by-page/)
{{< app/cells/assistant language="java" >}}
