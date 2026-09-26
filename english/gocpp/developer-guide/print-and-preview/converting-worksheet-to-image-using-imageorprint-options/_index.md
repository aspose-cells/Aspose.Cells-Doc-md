---
title: Converting Worksheet to Image using ImageOrPrint Options with Golang via C++
linktitle: Converting Worksheet to Image
type: docs
weight: 90
url: /go-cpp/converting-worksheet-to-image-using-imageorprint-options/
description: Learn how to convert a worksheet to an image file and apply different image and print options using Aspose.Cells with Golang via C++.
---

{{% alert color="primary" %}}

This document is designed to provide a detailed understanding of how to convert a worksheet to an image file and apply different image and print options for the image, such as resolution, TIFF compression, image format, and page quality.

{{% /alert %}}

## **Saving Worksheets to Images - Different Approaches**

Sometimes, you might require presenting your worksheets as a pictorial representation. You may need to present the worksheet images in your applications or web pages, insert them into a Word document, a PDF file, a PowerPoint presentation, or use them in some other scenario. Simply put, you want a worksheet rendered as an image so that you can use it elsewhere. Aspose.Cells supports converting worksheets in Excel files to images. Additionally, Aspose.Cells supports setting different options like image format, resolution (both vertical and horizontal), image quality, and other image and print options.

You might consider Office Automation, but it has its own drawbacks. There are several reasons and issues involved, such as security, stability, scalability, speed, price, and features. In short, there are many reasons, with the top one being that Microsoft itself strongly recommends against Office automation from software solutions.

This article shows how to create a console application in Visual Studio, perform the conversion of a worksheet to an image using a few simple lines of code with different image and print options using Aspose.Cells API.

You need to include the [**Aspose.Cells.Rendering**](https://reference.aspose.com/cells/go-cpp/aspose.cells.rendering/) namespace in your program/project. It has several valuable classes, for example, [**SheetRender**](https://reference.aspose.com/cells/go-cpp/sheetrender/), [**ImageOrPrintOptions**](https://reference.aspose.com/cells/go-cpp/imageorprintoptions/), [**WorkbookRender**](https://reference.aspose.com/cells/go-cpp/workbookrender/), etc.

The [**Aspose.Cells.Rendering.SheetRender**](https://reference.aspose.com/cells/go-cpp/sheetrender/) class represents a worksheet to render images for the worksheet. It has an overloaded [**ToImage**](https://reference.aspose.com/cells/go-cpp/sheetrender/toimage_int_string/) method that can directly convert a worksheet to image file(s) specified with your desired attributes or options. It can return a bitmap object, and you can save an image file to the disk/stream. Several image formats are supported, such as BMP, PNG, GIF, JPEG, TIFF, EMF, and so on.

## **Using Aspose.Cells to Convert Worksheet to Image using ImageOrPrint Options**

### **Creating a Template Workbook in Microsoft Excel**

I created a new workbook in MS Excel and added some data in the first worksheet. Now, I will convert the template file’s worksheet “Sheet1” to an image file “SheetImage.tiff” and will apply different image options like horizontal and vertical resolutions, TIFF compression, etc.

### **Download and Install Aspose.Cells**

First, you need to [download](https://downloads.aspose.com/cells/go-cpp/) Aspose.Cells for Go via C++. Install it on your development computer. All [Aspose](http://www.aspose.com/) components, when installed, work in evaluation mode. The evaluation mode has no time limit and only injects watermarks into produced documents.

### **Create a Project**

Start Visual Studio and create a new console application. This example will show a C++ console application.

### **Add References**

This project will use Aspose.Cells. So, you have to add a reference to the Aspose.Cells component in your project. For example, add a reference to `...\Program Files\Aspose\Aspose.Cells for Go via C++\Bin\Aspose.Cells.lib`.

### **Convert Worksheet to an Image File**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ConvertingWorksheetToImageUsingImageorprintOptions.go" >}}

## **Conversion Options**

It is possible to save specific pages to an image. The following code converts the first and second worksheets in a workbook to JPG images.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ConvertingWorksheetToImageUsingImageorprintOptions-1.go" >}}

## **Image Conversion using WorkbookRender**

A TIFF image can contain more than one frame. You can save the whole workbook to a single TIFF image with multiple frames or pages:

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ConvertingWorksheetToImageUsingImageorprintOptions-2.go" >}}
{{< app/cells/assistant language="go" >}}
