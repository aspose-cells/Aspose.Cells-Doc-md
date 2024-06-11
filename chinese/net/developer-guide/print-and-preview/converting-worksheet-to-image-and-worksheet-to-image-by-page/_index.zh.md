---
title: 将工作表转换为图像以及按页将工作表转换为图像
type: docs
weight: 80
url: /zh/net/converting-worksheet-to-image-and-worksheet-to-image-by-page/
---

{{% alert color="primary" %}}

本文档旨在为开发人员提供详细了解如何将工作表转换为图像文件以及将带有多个页面的工作表转换为每页一个图像文件。

有时，您可能需要将工作表呈现为图像，例如在应用程序或网页中使用。您可能需要将图像插入 Word 文档、PDF 文件、PowerPoint 演示文稿中，或者在其他一些场景中使用它们。简单来说，您希望将工作表呈现为图像。Aspose.Cells 支持将 Microsoft Excel 文件中的工作表转换为图像。Aspose.Cells 还支持将工作簿转换为多个图像文件，每页一个。

您可以使用Office自动化来实现这一点，但Office自动化有它自己的缺点。有几个原因和问题涉及其中：例如安全性、稳定性、可伸缩性/速度、价格和功能。简而言之，有很多原因，但主要原因是微软自己强烈建议不要使用Office自动化。

{{% /alert %}}

## **使用 Aspose.Cells 将工作表转换为图像文件**

本文介绍了如何在 Visual Studio 中创建控制台应用程序，使用 Aspose.Cells API 将工作表转换为图像，并将每个工作表转换为单个图像的几行最简代码。

您需要将 [**Aspose.Cells.Rendering**](https://reference.aspose.com/cells/net/aspose.cells.rendering) 命名空间导入到您的程序/项目中。它具有几个有价值的类，如 [**SheetRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender)、[**ImageOrPrintOptions**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions)、[**WorkbookRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookrender) 等。[**Aspose.Cells.Rendering.SheetRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender) 类代表要为其渲染图像的工作表，并具有一个重载的 [**ToImage**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender/methods/toimage/index) 方法，可以直接将工作表转换为具有任何属性或选项设置的图像文件。它可以返回一个 System.Drawing.Bitmap 对象，您可以将图像文件保存到磁盘/流中。支持多种图像格式，例如 BMP、PNG、GIF、JPG、JPEG、TIFF、EMF 等。

本文解释了如何：

- 将工作表转换为图像
- 将工作表中的每个页面转换为图像

此任务显示如何使用Aspose.Cells将模板工作簿中的工作表转换为图像文件。

### **设置项目**

1. 首先，[下载 Aspose.Cells for .NET](https://downloads.aspose.com/cells/net)。
1. 在开发计算机上安装它。 当安装了所有Aspose组件时，它们都以评估模式运行。 评估模式没有时间限制，只会在生成的文档中添加水印。现在启动Visual Studio.Net并创建一个新的控制台应用程序。此示例使用C#控制台应用程序，但您也可以使用VB.NET。将Aspose.Cells的引用添加到创建的项目中。

### **将工作表转换为图像文件**

我在Microsoft Excel中创建了一个新工作簿，并在第一个工作表中添加了一些数据：**Testbook.xlsx**（1个工作表）。接下来，将模板文件的工作表Sheet1转换为名为SheetImage.jpg的图像文件。

以下是组件用来完成任务的代码。它将**Testbook.xlsx**中的Sheet1转换为图像文件，以说明这种转换有多么简便。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ConvertingWorksheetToImage-ConvertWorksheettoImageFile-1.cs" >}}

## **使用Aspose.Cells按页将工作表转换为图像文件**

此示例演示如何使用Aspose.Cells将模板工作簿中具有多个页面的工作表转换为每页一个图像文件。

### **按页将工作表转换为图像**

我在Microsoft Excel中创建了一个新工作簿，并在第一个工作表中添加了一些数据：**Testbook2.xlsx**（1个工作表）。

现在，将模板文件的工作表Sheet1转换为图像文件（每页一个文件）。由于我已经创建了执行复制任务的控制台应用程序，因此我将跳过创建控制台应用程序的步骤，直接转移到工作表转换步骤。

以下是组件用于完成任务的代码。它将Testbook2.xls中的Sheet1转换为每页一个图像文件。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ConvertingWorksheetToImage-ConvertWorksheetToImageByPage-1.cs" >}}

