---  
title: Converting Worksheet to Image and Worksheet to Image by Page with Golang via C++  
linktitle: Converting Worksheet to Image and Worksheet to Image by Page  
type: docs  
weight: 80  
url: /go-cpp/converting-worksheet-to-image-and-worksheet-to-image-by-page/  
description: Learn how to convert a worksheet to an image file and a worksheet with multiple pages to an image file per page using Aspose.Cells with Golang via C++.  
---  

{{% alert color="primary" %}}

This document is designed to provide developers with a detailed understanding of how to convert a worksheet to an image file and a worksheet with multiple pages to an image file per page.

Sometimes, you might need to present worksheets as images, for example, to use them in applications or web pages. You might need to insert the images into a Word document, a PDF file, a PowerPoint presentation, or use them in some other scenario. **Simply put, you want to render the worksheet as an image.** Aspose.Cells supports converting worksheets in Microsoft Excel files to images. Also, Aspose.Cells supports converting a workbook to multiple image files, one per page.

You might use Office Automation to achieve this, but Office automation has its own drawbacks. There are several reasons and issues involved: for example, security, stability, scalability/speed, price, and features. In short, there are many reasons, but the main one is that Microsoft themselves strongly recommends against Office automation.

{{% /alert %}}

## **Using Aspose.Cells to Convert Worksheet to Image File**

This article shows how to create a console application in Visual Studio, convert a worksheet to an image, and convert a worksheet into a separate image for each page with a few simple lines of code using the Aspose.Cells API.

You need to include the [**Aspose.Cells.Rendering**](https://reference.aspose.com/cells/go-cpp/aspose.cells.rendering/) namespace in your program/project. It has several valuable classes, such as [**SheetRender**](https://reference.aspose.com/cells/go-cpp/sheetrender/), [**ImageOrPrintOptions**](https://reference.aspose.com/cells/go-cpp/imageorprintoptions/), [**WorkbookRender**](https://reference.aspose.com/cells/go-cpp/workbookrender/), and so on. The [**Aspose.Cells.Rendering.SheetRender**](https://reference.aspose.com/cells/go-cpp/sheetrender/) class represents a worksheet for rendering images and has an overloaded [**ToImage**](https://reference.aspose.com/cells/go-cpp/sheetrender/toimage_int_string/) method that can convert a worksheet to image files directly with any attributes or options set. It can return a `System.Drawing.Bitmap` object, and you can save an image file to the disk/stream. Several image formats are supported, for example, BMP, PNG, GIF, JPG, JPEG, TIFF, EMF, and others.

This article explains how to:

- Convert a worksheet to an image
- Convert every page in a worksheet to an image

The task shows how to use Aspose.Cells to convert a worksheet from a template workbook to an image file.

### **Setup Project**

1. First, [download Aspose.Cells for Go via C++](https://downloads.aspose.com/cells/go-cpp/).  
2. Install it on your development computer. All [Aspose](http://www.aspose.com/) components, when installed, work in evaluation mode. The evaluation mode has no time limit and it only injects watermarks into produced documents. Now start Visual Studio and create a new console application. This example uses a C++ console application. Add a reference to Aspose.Cells in the created project.

### **Convert Worksheet to Image File**

I created a new workbook in Microsoft Excel and added some data in the first worksheet: **Testbook.xlsx** (1 worksheet). Next, convert the template file’s worksheet Sheet1 to an image file called SheetImage.jpg.

Following is the code used by the component to accomplish the task. It converts Sheet1 in **Testbook.xlsx** to an image file to demonstrate how easy this conversion is.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ConvertingWorksheetToImageAndWorksheetToImageByPage.go" >}}

## **Using Aspose.Cells to Convert Worksheet to Image File by Page**

This example shows how to use Aspose.Cells to convert a worksheet from a template workbook that has several pages to one image file per page.

### **Convert Worksheet to Image by Page**

I created a new workbook in Microsoft Excel and added some data in the first worksheet: **Testbook2.xlsx** (1 worksheet).

Now, convert the template file's worksheet Sheet1 to image files (one file per page). As I already created the console application to perform the copy task, I will skip those console application creation steps and directly move to the worksheet conversion steps.

Following is the code used by the component to accomplish the task. It converts Sheet1 in **Testbook2.xlsx** to image files by page.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ConvertingWorksheetToImageAndWorksheetToImageByPage-1.go" >}}
{{< app/cells/assistant language="go" >}}
