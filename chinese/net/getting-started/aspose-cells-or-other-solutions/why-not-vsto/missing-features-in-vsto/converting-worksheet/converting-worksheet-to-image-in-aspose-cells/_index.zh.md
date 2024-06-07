---
title: 将工作表转换为图像在Aspose.Cells中
type: docs
weight: 20
url: /zh/net/converting-worksheet-to-image-in-aspose-cells/
---

本文旨在为开发人员提供详细了解如何将工作表转换为图像文件和具有多个页面的工作表转换为图像文件。
有时，您可能需要将工作表呈现为图像，例如在应用程序或网页中使用它们。您可能需要将图像插入到Word文档、**PDF**文件、PowerPoint演示文稿中或在其他一些场景中使用它们。简单地说，您希望将工作表呈现为图像。Aspose.Cells支持将Microsoft Excel文件中的工作表转换为图像。另外，**Aspose.Cells**支持将工作簿转换为多个图像文件，每个页面一个。

您可以使用Office Automation来实现这一点，但是Office Automation有其自身的缺点。涉及多种原因和问题，例如安全性、稳定性、可伸缩性/速度、价格和功能。简而言之，有很多原因，但主要原因是微软本身强烈建议避免使用Office Automation。

本文介绍了如何在Visual Studio.Net中创建一个控制台应用程序，使用Aspose.Cells API的几行简单代码将工作表转换为图像，并将每个工作表转换为一个图像。

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
## **下载示例代码**
- [Github](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Cells1.0/Worksheet.to.Image.Aspose.Cells.zip)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-vsto/downloads/Worksheet%20to%20Image%20%28Aspose.Cells%29.zip)
