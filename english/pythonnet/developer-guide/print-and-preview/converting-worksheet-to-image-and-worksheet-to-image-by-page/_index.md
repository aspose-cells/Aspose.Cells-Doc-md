---
title: Converting Worksheet to Image and Worksheet to Image by Page
type: docs
weight: 80
url: /python-net/converting-worksheet-to-image-and-worksheet-to-image-by-page/
---

{{% alert color="primary" %}}

This document is designed to provide the developers with a detailed understanding of how to convert a worksheet to an image file & worksheet with multiple pages to an image file per page.

Sometimes, you might need to present worksheets as images, for example, to use them in applications or web pages. You might need to insert the images into a Word document, a PDF file, a PowerPoint presentation, or use them in some other scenario. Simply, you want to render the worksheet as an image. Aspose.Cells for Python via .NET supports converting worksheets in Microsoft Excel files to images. Also, Aspose.Cells for Python via .NET supports converting a workbook to multiple image files, one per page.

You might use Office Automation to achieve this, but Office automation has its own drawbacks. There are several reasons and issues involved: for example security, stability, scalability/Speed, price, and features. In short, there are many reasons, but the main one is that Microsoft themselves strongly recommends against Office automation.

{{% /alert %}}

## **Using Aspose.Cells to Convert Worksheet to Image File**

This article shows how to create a console application in Visual Studio, convert a worksheet to an image, and convert a worksheet into one image for each worksheet with a few and simplest lines of code using the Aspose.Cells for Python via .NET API.

You need to import the [**aspose.cells.rendering**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering) namespace to your program/project. It has several valuable classes, such as [**SheetRender**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender), [**ImageOrPrintOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions), [**WorkbookRender**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/workbookrender), and so on. The [**SheetRender**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender) class represents a worksheet to render images for the worksheet and has an overloaded [**to_image**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender/to_image/#int-str) method that can convert a worksheet to image files directly with any attributes or options set. It can return a System.Drawing.Bitmap object and you can save an image file to the disk/stream. Several image formats are supported, for example, BMP, PNG, GIF, JPG, JPEG, TIFF, EMF, and others.

This article explains how to convert a worksheet to an image. This task shows how to use Aspose.Cells for Python via .NET to convert a worksheet from a template workbook to an image file.


### **Convert Worksheet to Image File**

I created a new workbook in Microsoft Excel and added some data in the first worksheet: **Testbook.xlsx** (1 worksheet). Next, convert the template file’s worksheet Sheet1 to an image file called SheetImage.jpg.

Following is the code used by the component to accomplish the task. It converts Sheet1 in **Testbook.xlsx** to an image file to explain how easy this conversion is.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-ConvertWorksheettoImageFile-1.py" >}}

## **Using Aspose.Cells to Convert Worksheet to Image File by Page**

This example shows how to use Aspose.Cells for Python via .NET to convert a worksheet from a template workbook that has several pages to one image file per page.

### **Convert Worksheet to Image by page**

I created a new workbook in Microsoft Excel and added some data in the first worksheet: **Testbook2.xlsx** (1 worksheet).

Now, convert the template file's worksheet Sheet1 to image files (one file per page). As I already created the console application to perform the copy task, I will skip those console application creation steps and directly move to the worksheet conversion steps.

Following is the code used by the component to accomplish the task. It converts Sheet1 in Testbook2.xls to image files by page.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-ConvertWorksheetToImageByPage-1.py" >}}

