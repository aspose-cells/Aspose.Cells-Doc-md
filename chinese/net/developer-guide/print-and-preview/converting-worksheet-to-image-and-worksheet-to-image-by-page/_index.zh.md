---
title: 按页将工作表转换为图像并将工作表转换为图像
type: docs
weight: 80
url: /zh/net/converting-worksheet-to-image-and-worksheet-to-image-by-page/
---
{{% alert color="primary" %}}

本文档旨在让开发人员详细了解如何将工作表转换为图像文件以及将多页工作表转换为每页图像文件。

有时，您可能需要将工作表显示为图像，例如，以便在应用程序或网页中使用它们。您可能需要将图像插入到 Word 文档、PDF 文件、PowerPoint 演示文稿中，或者在其他一些场景中使用它们。简单地说，您想将工作表呈现为图像。 Aspose.Cells 支持将Microsoft Excel文件中的工作表转换为图片。此外，Aspose.Cells 支持将工作簿转换为多个图像文件，每页一个。

您可以使用 Office Automation 来实现这一点，但 Office Automation 有其自身的缺点。涉及多个原因和问题：例如安全性、稳定性、可扩展性/速度、价格和功能。简而言之，有很多原因，但最主要的是Microsoft 自己强烈建议不要使用Office 自动化。

{{% /alert %}}

## **使用 Aspose.Cells 将工作表转换为图像文件**

本文介绍如何使用 Aspose.Cells API 使用几行最简单的代码在 Visual Studio 中创建控制台应用程序，将工作表转换为图像，并将工作表转换为每个工作表的一张图像。

你需要导入[**Aspose.Cells.Rendering**](https://reference.aspose.com/cells/net/aspose.cells.rendering)命名空间到您的程序/项目。它有几个有价值的类，例如[**图纸渲染**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender), [**图像或打印选项**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions), [**工作簿渲染**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookrender)， 等等。这[**Aspose.Cells.Rendering.SheetRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender)类代表一个工作表，为工作表渲染图像，并有一个重载[**印象**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender/methods/toimage/index)可以将工作表直接转换为具有任何属性或选项集的图像文件的方法。它可以返回一个 System.Drawing.Bitmap 对象，您可以将图像文件保存到磁盘/流中。支持多种图像格式，例如 BMP、PNG、GIF、JPG、JPEG、TIFF、EMF 等。

本文介绍了如何：

- 将工作表转换为图像
- 将工作表中的每一页都转换为图像

此任务显示如何使用 Aspose.Cells 将工作表从模板工作簿转换为图像文件。

### **安装项目**

1. 第一的，[下载 Aspose.Cells for .NET](https://downloads.aspose.com/cells/net).
1. 在您的开发计算机上安装它。全部[Aspose](http://www.aspose.com/)组件在安装后以评估模式工作。评估模式没有时间限制，它只在生成的文档中注入水印。现在启动 Visual Studio.Net 并创建一个新的控制台应用程序。此示例使用 C# 控制台应用程序，但您也可以使用 VB.NET。将对 Aspose.Cells 的引用添加到创建的项目中。

### **将工作表转换为图像文件**

我在 Microsoft Excel 中创建了一个新工作簿，并在第一个工作表中添加了一些数据：**试卷.xlsx** （1 个工作表）。接下来，将模板文件的工作表 Sheet1 转换为名为 SheetImage.jpg 的图像文件。

以下是组件用于完成任务的代码。它将 Sheet1 转换为**试卷.xlsx**到一个图像文件来解释这种转换是多么容易。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ConvertingWorksheetToImage-ConvertWorksheettoImageFile-1.cs" >}}

## **使用 Aspose.Cells 将工作表按页转换为图像文件**

此示例说明如何使用 Aspose.Cells 将工作表从具有多页的模板工作簿转换为每页一个图像文件。

### **按页将工作表转换为图像**

我在 Microsoft Excel 中创建了一个新工作簿，并在第一个工作表中添加了一些数据：**Testbook2.xlsx** （1 个工作表）。

现在，将模板文件的工作表 Sheet1 转换为图像文件（每页一个文件）。由于我已经创建了控制台应用程序来执行复制任务，因此我将跳过这些控制台应用程序创建步骤，直接转到工作表转换步骤。

以下是组件用于完成任务的代码。它将 Testbook2.xls 中的 Sheet1 按页转换为图像文件。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ConvertingWorksheetToImage-ConvertWorksheetToImageByPage-1.cs" >}}

