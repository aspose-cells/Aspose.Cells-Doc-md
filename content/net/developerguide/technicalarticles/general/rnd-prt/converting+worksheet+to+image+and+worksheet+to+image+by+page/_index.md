---
title : "Converting Worksheet to Image and Worksheet to Image by Page" 
description : "" 
weight : 20363 
toc : false
type: docs
url: /net/developerguide/technicalarticles/general/rnd-prt/converting+worksheet+to+image+and+worksheet+to+image+by+page/
---

# Aspose.Cells for .NET : Converting Worksheet to Image and Worksheet to Image by Page


This document is designed to provide the developers with a detailed understanding on how to convert a worksheet to an image file & worksheet with multiple pages to an image file per page.

Sometimes, you might need to present worksheets as images, for example to use them in applications or web pages. You might need to insert the images into a Word document, a PDF file, a PowerPoint presentation or use them in some other scenario. Simply, you want to render the worksheet as an image. Aspose.Cells supports converting worksheets in Microsoft Excel files to images. Also, Aspose.Cells supports converting a workbook to multiple image files, one per page.

You might use Office Automation to achieve this, but Office automation has its own drawbacks. There are several reasons and issues involved: for example security, stability, scalability/Speed, price, and features. In short, there are many reasons, but the main one is that Microsoft themselves strongly recommends against Office automation.

{{< panel title="Contents Summary" style="primary" >}}
*   1 [Using Aspose.Cells to Convert Worksheet to Image File](#using-aspose.cells-to-convert-worksheet-to-image-file)
    *   1.1 [Setup Project](#setup-project)
    *   1.2 [Convert Worksheet to Image File](#convert-worksheet-to-image-file)
*   2 [Using Aspose.Cells to Convert Worksheet to Image File by Page](#using-aspose.cells-to-convert-worksheet-to-image-file-by-page)
    *   2.1 [Convert Worksheet to Image by page](#convert-worksheet-to-image-by-page)
{{< /panel >}}
 

 

# Using Aspose.Cells to Convert Worksheet to Image File

This article shows how to create a console application in Visual Studio.Net, convert a worksheet to an image, and a worksheet into one image for each worksheet with a few and simplest lines of code using the Aspose.Cells API.

You need to import the `Aspose.Cells.Rendering` namespace to your program/project. It has several valuable classes, such as `SheetRender`, `ImageOrPrintOptions`, `WorkbookRender` and so on. The `Aspose.Cells.Rendering.SheetRender` class represents a worksheet to render images for the worksheet and has an overloaded `ToImage` method that can convert a worksheet to image files directly with any attributes or options set. It can return a `System.Drawing.Bitmap` object and you can save an image file to the disk/stream. Several image formats are supported, for example BMP, PNG, GIF, JPG, JPEG, TIFF, EMF and others.

This article explains how to:

*   Convert a worksheet to an image
*   Convert every page in a worksheet to an image

This task shows how to use Aspose.Cells to convert a worksheet from a template workbook to an image file.

## Setup Project

1.  First, [download Aspose.Cells for .NET](http://www.aspose.com/community/files/51/.net-components/aspose.cells-for-.net/default.aspx).
2.  Install it on your development computer. All [Aspose](http://www.aspose.com/) components, when installed, work in evaluation mode. The evaluation mode has no time limit and it only injects watermarks into produced documents. Now start Visual Studio.Net and create a new console application. This example uses a C# console application, but you can use VB.NET too. [Add reference](http://www.aspose.com/docs/display/cellsnet/Referencing+Aspose.Cells+from+a+.NET+Project) to `Aspose.Cells` into created project.

## Convert Worksheet to Image File

I created a new workbook in Microsoft Excel and added some data in the first worksheet: **Testbook.xlsx** (1 worksheet). Next, convert the template file’s worksheet Sheet1 to an image file called SheetImage.jpg.

Following is the code (written in C# and then in VB) used by the component to accomplish the task. It converts Sheet1 in **Testbook.xlsx** to an image file to explain how easy this conversion is.

# Using Aspose.Cells to Convert Worksheet to Image File by Page

This example shows how to use Aspose.Cells to convert a worksheet from a template workbook that has several pages to one image file per page.

## Convert Worksheet to Image by page

I created a new workbook in Microsoft Excel and added some data in the first worksheet: **Testbook2.xlsx** (1 worksheet).

Now, convert the template file's worksheet Sheet1 to image files (one file per page). As I already created the console application to perform the copy task, I will skip those console application creation steps and directly move to the worksheet conversion steps.

Following is the code (written first in C# and then in VB) used by the component to accomplish the task. It converts Sheet1 in Testbook2.xls to image files by page.

