---
title: Converting Worksheet to Image in Aspose.Cells
type: docs
weight: 20
url: /net/converting-worksheet-to-image-in-aspose-cells/
---

This document is designed to provide the developers with a detailed understanding on how to convert a worksheet to an image file & worksheet with multiple pages to an image file per page.
Sometimes, you might need to present worksheets as images, for example to use them in applications or web pages. You might need to insert the images into a Word document, a **PDF** file, a PowerPoint presentation or use them in some other scenario. Simply, you want to render the worksheet as an image. Aspose.Cells supports converting worksheets in Microsoft Excel files to images. Also, **Aspose.Cells** supports converting a workbook to multiple image files, one per page.

You might use Office Automation to achieve this, but Office automation has its own drawbacks. There are several reasons and issues involved: for example security, stability, scalability/Speed, price, and features. In short, there are many reasons, but the main one is that Microsoft themselves strongly recommends against Office automation.

This article shows how to create a console application in Visual Studio.Net, convert a worksheet to an image, and a worksheet into one image for each worksheet with a few and simplest lines of code using Aspose.Cells API.You need to import Aspose.Cells.Rendering namespace to your program/project. It has several valuable classes, e.g SheetRender, ImageOrPrintOptions, WorkbookRender etc.Aspose.Cells.Rendering.SheetRender class represents a worksheet to render images for the worksheet, it has an overloaded **ToImage** method that can directly convert a worksheet to image file(s) specified with your desired attributes or options. It can return **System.Drawing.Bitmap** object and you can Save an image file to the disk/stream. There are several image formats supported, e.g .bmp, .png, .gif, .jpg, .jpeg, .tiff, .emf etc.

{{< highlight csharp >}}

 //Create a new Workbook object

//Open a template excel file

Workbook book = new Workbook("Sheet to Image.xls");

//Get the first worksheet.

Worksheet sheet = book.Worksheets[0];

//Define ImageOrPrintOptions

ImageOrPrintOptions imgOptions = new ImageOrPrintOptions();

//Specify the image format

imgOptions.ImageFormat = System.Drawing.Imaging.ImageFormat.Jpeg;

//Render the sheet with respect to specified image/print options

SheetRender sr = new SheetRender(sheet, imgOptions);

//Render the image for the sheet

Bitmap bitmap = sr.ToImage(0);

//Save the image file

bitmap.Save("SheetImage.jpg");

{{< /highlight >}}
## **Download Sample Code**
- [Github](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Cells1.0/Worksheet.to.Image.Aspose.Cells.zip)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-vsto/downloads/Worksheet%20to%20Image%20%28Aspose.Cells%29.zip)
