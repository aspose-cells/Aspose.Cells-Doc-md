---
title: 在 Aspose.Cells 中将工作表转换为图像
type: docs
weight: 20
url: /zh/net/converting-worksheet-to-image-in-aspose-cells/
---
本文档旨在让开发人员详细了解如何将工作表转换为图像文件以及将多页工作表转换为每页图像文件。
有时，您可能需要将工作表显示为图像，例如在应用程序或网页中使用它们。您可能需要将图像插入到 Word 文档中，**PDF**文件、PowerPoint 演示文稿或在其他一些场景中使用它们。简单地说，您想将工作表呈现为图像。 Aspose.Cells 支持将Microsoft Excel文件中的工作表转换为图片。还，**Aspose.Cells**支持将工作簿转换为多个图像文件，每页一个。

您可以使用 Office Automation 来实现这一点，但 Office Automation 有其自身的缺点。涉及多个原因和问题：例如安全性、稳定性、可扩展性/速度、价格和功能。简而言之，有很多原因，但最主要的是Microsoft 自己强烈建议不要使用Office 自动化。

本文介绍如何在 Visual Studio.Net 中创建控制台应用程序，将工作表转换为图像，并将工作表转换为一张图像，每个工作表使用 Aspose.Cells API 的几行最简单的代码。您需要导入 Aspose.Cells.Rendering命名空间到您的程序/项目。它有几个有价值的类，eg SheetRender, ImageOrPrintOptions, WorkbookRender etc.Aspose.Cells.Rendering.SheetRender 类代表一个工作表，为工作表渲染图像，它有一个重载**印象**可以将工作表直接转换为使用所需属性或选项指定的图像文件的方法。它可以返回**系统.绘图.位图**对象，您可以将图像文件保存到磁盘/流。支持多种图像格式，例如 .bmp、.png、.gif、.jpg、.jpeg、.tiff、.emf 等。

{{< highlight "csharp" >}}

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
- [比特桶](https://bitbucket.org/asposemarketplace/aspose-for-vsto/downloads/Worksheet%20to%20Image%20%28Aspose.Cells%29.zip)
