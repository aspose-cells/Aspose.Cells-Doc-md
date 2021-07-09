---
title: Render the Worksheet and Workbook to Image using ImageOrPrintOptions
type: docs
weight: 220
url: /java/render-the-worksheet-and-workbook-to-image-using-imageorprintoptions/
---

{{% alert color="primary" %}}

This document is designed to provide a detailed understanding of how to convert a worksheet or a workbook to an image file and apply different image and print options for the image, options like resolution, TIFF compression, image format, and page quality.

{{% /alert %}}

## **Overview**

Sometimes, you might require presenting your worksheets as a pictorial representation. You do need to present the worksheet images into your applications or web pages. You might need to insert the images into a Word document, a PDF file, a PowerPoint presentation, or use them in some other scenario. Simply you want a worksheet rendered as an image so that you can use it elsewhere. Aspose.Cells supports converting worksheets in Excel files to images. Also, Aspose.Cells supports setting different options like image format, resolution (both vertical and horizontal), image quality, and other image and print options.

The API provides several valuable classes, for example, [**SheetRender**](https://apireference.aspose.com/cells/java/com.aspose.cells/SheetRender), [**ImageOrPrintOptions**](https://apireference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions), [**WorkbookRender**](https://apireference.aspose.com/cells/java/com.aspose.cells/WorkbookRender), etc.

The [**SheetRender**](https://apireference.aspose.com/cells/java/com.aspose.cells/SheetRender) class handles the task of rendering images for the worksheet whereas the [**WorkbookRender**](https://apireference.aspose.com/cells/java/com.aspose.cells/WorkbookRender) does the same for a workbook. Both aforesaid classes have several overloaded versions of the *toImage* method that can directly convert a worksheet or a workbook to image file(s) specified with your desired attributes or options. You can save the image file to the disk/stream. There are several image formats supported, e.g BMP, PNG, GIFF, JPEG, TIFF, EMF, and so on.

### **Convert Worksheet to Image**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-ConvertWorksheettoImage-1.java" >}}

## **Conversion Options**

It is possible to save specific pages to image. The following code converts the first and second worksheets in a workbook to JPG images.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-ConversionOptions-1.java" >}}

Or you can cycle through the workbook and render each worksheet in it to a separate image:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-WorksheetToSeparateImage-1.java" >}}

## **Convert Workbook to Image:**

In order to render the complete workbook to image format, you may either use the above approach or simply use the [**WorkbookRender**](https://apireference.aspose.com/cells/java/com.aspose.cells/WorkbookRender) class that accepts an instance of [**Workbook**](https://apireference.aspose.com/cells/java/com.aspose.cells/Workbook) as well as the object of [**ImageOrPrintOptions**](https://apireference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions).

{{% alert color="primary" %}}

The [**WorkbookRender**](https://apireference.aspose.com/cells/java/com.aspose.cells/WorkbookRender) class can only save the workbook to the TIFF format.

{{% /alert %}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-ConvertWorkbooktoImage-1.java" >}}

## Related Articles

- [Converting Worksheet to Different Image Formats](/cells/java/converting-worksheet-to-different-image-formats/)
- [Export Chart to SVG with viewBox attribute](/cells/java/export-chart-to-svg-with-viewbox-attribute/)
- [Export Worksheet or Chart into Image with Desired Width and Height](/cells/java/export-worksheet-or-chart-into-image-with-desired-width-and-height/)
- [Converting Worksheet to Image and Worksheet to Image by Page](/cells/java/converting-worksheet-to-image-and-worksheet-to-image-by-page/)
