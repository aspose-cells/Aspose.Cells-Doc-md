---
title: 将工作表转换为图像和按页将工作表转换为图像
type: docs
weight: 80
url: /zh/net/converting-worksheet-to-image-and-worksheet-to-image-by-page/
---

{{% alert color="primary" %}}

本文档旨在为开发人员提供详细了解如何将工作表转换为图像文件和将多个页的工作表转换为单张图片文件的信息。

有时，您可能需要将工作表呈现为图像，例如在应用程序或网页中使用。您可能需要将这些图像插入到Word文档、PDF文件、PowerPoint演示文稿中或在其他场景中使用。简而言之，您希望将工作表呈现为图像。Aspose.Cells支持将Microsoft Excel文件中的工作表转换为图像。此外，Aspose.Cells还支持将工作簿转换为多个图像文件，每页一个。

您可以使用Office Automation来实现这一点，但是Office Automation有其自身的缺点。涉及多种原因和问题，例如安全性、稳定性、可伸缩性/速度、价格和功能。简而言之，有很多原因，但主要原因是微软本身强烈建议避免使用Office Automation。

{{% /alert %}}

## **使用Aspose.Cells将工作表转换为图像文件**

本文介绍了如何在Visual Studio中创建控制台应用程序，使用Aspose.Cells API的少量和最简单的代码将工作表转换为图像，并将每个工作表转换为一个图像。

您需要将[**Aspose.Cells.Rendering**](https://reference.aspose.com/cells/net/aspose.cells.rendering)命名空间导入到您的程序/项目中。它具有多个有价值的类，例如[**SheetRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender)、[**ImageOrPrintOptions**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions)、[**WorkbookRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookrender)等。[**Aspose.Cells.Rendering.SheetRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender)类代表用于为工作表渲染图像的工作表，并有一个重载的[**ToImage**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender/methods/toimage/index)方法，该方法可以直接将工作表转换为图像文件并设置任何属性或选项。它可以返回一个System.Drawing.Bitmap对象，您可以将图像文件保存到磁盘/流中。支持多种图像格式，例如BMP、PNG、GIF、JPG、JPEG、TIFF、EMF等。

本文解释了如何：

- 将工作表转换为图像
- 将工作表的每个页面转换为图像

此任务展示了如何使用Aspose.Cells将来自模板工作簿的工作表转换为图像文件。

### **设置项目**

1.首先，[下载Aspose.Cells for .NET](https://downloads.aspose.com/cells/net)。
1. 在开发计算机上安装它。所有的 [Aspose](http://www.aspose.com/) 元件，在安装时都是以评估模式运行的。评估模式没有时间限制，只会在生成的文档中插入水印。现在启动 Visual Studio.Net 并创建一个新的控制台应用程序。本示例使用了 C# 控制台应用程序，但您也可以使用 VB.NET。将Aspose.Cells添加到创建的项目的引用中。

### **将工作表转换为图片文件**

我在 Microsoft Excel 中创建了一个新工作簿，并在第一个工作表中添加了一些数据：**Testbook.xlsx**（1 个工作表）。接下来，将模板文件的工作表Sheet1转换为名为SheetImage.jpg的图片文件。

以下是组件用来完成该任务的代码。它将**Testbook.xlsx**中的Sheet1转换为图片文件，以说明这种转换有多简单。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ConvertingWorksheetToImage-ConvertWorksheettoImageFile-1.cs" >}}

## **使用 Aspose.Cells 将工作表按页转换为图片文件**

本示例展示如何使用 Aspose.Cells 将模板工作簿中有多页的工作表转换为一个图片文件。

### **按页将工作表转换为图片**

我在 Microsoft Excel 中创建了一个新工作簿，并在第一个工作表中添加了一些数据：**Testbook2.xlsx**（1 个工作表）。

现在，将模板文件的工作表Sheet1转换为图片文件（每页一个文件）。由于我已经创建了执行复制任务的控制台应用程序，所以我将跳过这些控制台应用程序创建步骤，直接转到工作表转换步骤。

以下是组件用来完成该任务的代码。它将 Testbook2.xls 中的Sheet1转换为按页的图片文件。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ConvertingWorksheetToImage-ConvertWorksheetToImageByPage-1.cs" >}}

