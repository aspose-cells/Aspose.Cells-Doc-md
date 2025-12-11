---
title: Converting Worksheet to Image and Worksheet to Image by Page
type: docs
weight: 80
url: /net/converting-worksheet-to-image-and-worksheet-to-image-by-page/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

This document is designed to provide developers with a detailed understanding of how to convert a worksheet to an image file **and** a worksheet with multiple pages to an image file per page.

Sometimes, you might need to present worksheets as images, for example, to use them in applications or web pages. You might need to insert the images into a Word document, a PDF file, a PowerPoint presentation, or use them in some other scenario. Simply, you want to render the worksheet as an image. Aspose.Cells supports converting worksheets in Microsoft Excel files to images. Also, Aspose.Cells supports converting a workbook to multiple image files, one per page.

You might use Office Automation to achieve this, but Office automation has its own drawbacks. There are several reasons and issues involved: for example, security, stability, scalability/speed, cost, and features. In short, there are many reasons, but the main one is that Microsoft itself strongly recommends against Office automation.

{{% /alert %}}

## **Using Aspose.Cells to Convert Worksheet to Image File**

This article shows how to create a console application in Visual Studio, convert a worksheet to an image, and convert a worksheet into one image per page with a few simple lines of code using the Aspose.Cells API.

You need to import the [**Aspose.Cells.Rendering**](https://reference.aspose.com/cells/net/aspose.cells.rendering) namespace to your program/project. It has several valuable classes, such as [**SheetRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender), [**ImageOrPrintOptions**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions), [**WorkbookRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookrender), and so on. The [**Aspose.Cells.Rendering.SheetRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender) class represents a worksheet to render images for the worksheet and has an overloaded [**ToImage**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender/methods/toimage/index) method that can convert a worksheet to image files directly with any attributes or options set. It can return a System.Drawing.Bitmap object and you can save an image file to the disk/stream. Several image formats are supported, for example, BMP, PNG, GIF, JPG, JPEG, TIFF, EMF, and others.

This article explains how to:

- Convert a worksheet to an image
- Convert every page in a worksheet to an image

This task shows how to use Aspose.Cells to convert a worksheet from a template workbook to an image file.

### **Setup Project**

1. First, [download Aspose.Cells for .NET](https://downloads.aspose.com/cells/net).  
2. Install it on your development computer. All [Aspose](http://www.aspose.com/) components, when installed, work in evaluation mode. The evaluation mode has no time limit and it only injects watermarks into produced documents. Now start Visual Studio .NET and create a new console application. This example uses a C# console application, but you can use VB.NET too. Add a reference to Aspose.Cells in the created project.

### **Convert Worksheet to Image File**

I created a new workbook in Microsoft Excel and added some data in the first worksheet: **Testbook.xlsx** (1 worksheet). Next, convert the template file’s worksheet Sheet1 to an image file called SheetImage.jpg.

Following is the code used by the component to accomplish the task. It converts Sheet1 in **Testbook.xlsx** to an image file to illustrate how easy this conversion is.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ConvertingWorksheetToImage-ConvertWorksheettoImageFile-1.cs" >}}

## **Using Aspose.Cells to Convert Worksheet to Image File by Page**

This example shows how to use Aspose.Cells to convert a worksheet from a template workbook that has several pages to one image file per page.

### **Convert Worksheet to Image by Page**

I created a new workbook in Microsoft Excel and added some data in the first worksheet: **Testbook2.xlsx** (1 worksheet).

Now, convert the template file's worksheet Sheet1 to image files (one file per page). As I already created the console application to perform the copy task, I will skip those console application creation steps and directly move to the worksheet conversion steps.

Following is the code used by the component to accomplish the task. It converts Sheet1 in **Testbook2.xlsx** to image files by page.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ConvertingWorksheetToImage-ConvertWorksheetToImageByPage-1.cs" >}}

{{< app/cells/assistant language="csharp" >}}
