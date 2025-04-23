---
title: 在Aspose.Cells中将工作表转换为图像
type: docs
weight: 20
url: /zh/net/converting-worksheet-to-image-in-aspose-cells/
---

本文档旨在为开发人员提供详细的了解如何将工作表转换为图像文件和如何将工作表的多页转换为每页一个图像文件。
有时候，您可能需要将工作表呈现为图像，例如在应用程序或网页中使用。您可能需要将图像插入到Word文档、**PDF**文件、PowerPoint演示文稿中，或在其他一些场景中使用。简单地说，您想将工作表呈现为图像。Aspose.Cells支持将Microsoft Excel文件中的工作表转换为图像。此外，**Aspose.Cells**还支持将工作簿转换为多个图像文件，每页一个。

您可以使用Office自动化来实现这一点，但Office自动化有它自己的缺点。有几个原因和问题涉及其中：例如安全性、稳定性、可伸缩性/速度、价格和功能。简而言之，有很多原因，但主要原因是微软自己强烈建议不要使用Office自动化。

本文展示了如何在Visual Studio.Net中创建控制台应用程序，将工作表转换为图像，并通过使用Aspose.Cells API的几行最简单的代码将工作表转换为每个工作表的一个图像。您需要将Aspose.Cells.Rendering命名空间导入到您的程序/项目中。它有几个有价值的类，例如SheetRender、ImageOrPrintOptions、WorkbookRender等。Aspose.Cells.Rendering.SheetRender类表示需要为工作表渲染图像，它有一个重载的**ToImage**方法，可以直接将工作表转换为图像文件，并使用您期望的属性或选项进行指定。它可以返回**System.Drawing.Bitmap**对象，您可以将图像文件保存到磁盘/流中。支持几种图像格式，例如.bmp、.png、.gif、.jpg、.jpeg、.tiff、.emf等。

{{< highlight csharp >}}

//Create a new Workbook object

//Open a template excel file

Workbook book = new Workbook("Sheet to Image.xls");

//Get the first worksheet.

Worksheet sheet = book.Worksheets[0];

//Define ImageOrPrintOptions

ImageOrPrintOptions imgOptions = new ImageOrPrintOptions();

//Specify the image type

imgOptions.ImageType = ImageType.Jpeg;

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
{{< app/cells/assistant language="csharp" >}}
