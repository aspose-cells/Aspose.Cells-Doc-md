---
title: Converting Worksheet to Image using ImageOrPrint Options
type: docs
weight: 90
url: /net/converting-worksheet-to-image-using-imageorprint-options/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

This document is designed to provide a detailed understanding of how to convert a worksheet to an image file and apply different image and print options for the image, options like resolution, TIFF compression, image format and page quality.

{{% /alert %}}

## **Saving Worksheets to Images - Different Approaches**

Sometimes, you might require presenting your worksheets as a pictorial representation. You do need to present the worksheet images into your applications or web pages. You might need to insert the images into a Word document, a PDF file, a PowerPoint presentation, or use them in some other scenario. Simply you want a worksheet rendered as an image so that you can use it elsewhere. Aspose.Cells supports converting worksheets in Excel files to images. Also, Aspose.Cells supports setting different options like image format, resolution (both vertical and horizontal), image quality, and other image and print options.

You might try Office Automation but Office automation has its own drawbacks. There are several reasons and issues involved: for example, security, stability, scalability and speed, price, and features. In Short, there are many reasons, with the top one being that Microsoft themselves strongly recommends against Office automation from software solutions.

This article shows how to create a console application in Visual Studio .NET, perform the conversion of a worksheet to image using different image and print options with a few and simplest lines of code using Aspose.Cells API.

You need to import [**Aspose.Cells.Rendering**](https://reference.aspose.com/cells/net/aspose.cells.rendering) namespace to your program/project. It has several valuable classes, for example, [**SheetRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender), [**ImageOrPrintOptions**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions), [**WorkbookRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookrender) etc.

The [**Aspose.Cells.Rendering.SheetRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender) class represents a worksheet to render images for the worksheet, it has an overloaded [**ToImage**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender/methods/toimage/index) method that can directly convert a worksheet to image file(s) specified with your desired attributes or options. It can return System.Drawing.Bitmap object and you can Save an image file to the disk/stream. There are several image formats supported, e.g BMP, PNG, GIFF, JPEG, TIFF, EMF and so on.

## **Using Aspose.Cells to Convert Worksheet to Image using ImageOrPrint options.**

### **Creating a template workbook in Microsoft Excel**

I created a new workbook in MS Excel and added some data in the first worksheet. Now, I will convert the template file’s worksheet “Sheet1” to an image file “SheetImage.tiff” and will apply different image options like horizontal and vertical resolutions, TiffCompression etc.

### **Download and Install Aspose.Cells**

First, you need to [download](https://downloads.aspose.com/cells/net) Aspose.Cells for .Net. Install it on your development computer. All [Aspose](http://www.aspose.com/) components, when installed, work in evaluation mode. The evaluation mode has no time limit and it only injects watermarks into produced documents.

### **Create a Project**

Start Visual Studio. Net and create a new console application. This example will show a C# console application, but you can use VB.NET too.

### **Add References**

This project will use Aspose.Cells. So, you have to add reference to Aspose.Cells component in your project. For example, add a reference to ….\Program Files\Aspose\Aspose.Cells for .NET\Bin\Net1.0\Aspose.Cells.dll

### **Convert Worksheet to an Image file**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UsingImageOrPrintOptions-WorksheetToAnImage-1.cs" >}}

## **Conversion Options**

It is possible to save specific pages to image. The following code converts the first and second worksheets in a workbook to JPG images.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UsingImageOrPrintOptions-SpecificPagesToImage-1.cs" >}}

## **Image conversion using WorkbookRender**

A TIFF image can contian more than one frames. You can save the whole workbook to a single TIFF image with multiply frames or pages:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UsingImageOrPrintOptions-UseWorkbookRenderForImageConversion-1.cs" >}}

{{< app/cells/assistant language="csharp" >}}
