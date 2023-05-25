---
title: 使用 ImageOrPrint 选项将工作表转换为图像
type: docs
weight: 90
url: /zh/net/converting-worksheet-to-image-using-imageorprint-options/
---
{{% alert color="primary" %}}

本文档旨在详细介绍如何将工作表转换为图像文件，并为图像应用不同的图像和打印选项，如分辨率、TIFF 压缩、图像格式和页面质量等选项。

{{% /alert %}}

##  **将工作表保存为图像 - 不同的方法**

有时，您可能需要将您的工作表呈现为图形表示。您确实需要将工作表图像显示到您的应用程序或网页中。您可能需要将图像插入到 Word 文档、PDF 文件、PowerPoint 演示文稿中，或者在其他一些场景中使用它们。您只需要将工作表呈现为图像，以便您可以在其他地方使用它。 Aspose.Cells 支持将Excel文件中的工作表转换为图片。此外，Aspose.Cells 支持设置不同的选项，如图像格式、分辨率（垂直和水平）、图像质量以及其他图像和打印选项。

您可以尝试 Office Automation，但 Office Automation 有其自身的缺点。涉及的原因和问题有几个：例如，安全性、稳定性、可扩展性和速度、价格和功能。简而言之，有很多原因，其中最重要的一个是 Microsoft 自己强烈建议不要通过软件解决方案实现 Office 自动化。

本文介绍如何在 Visual Studio .NET 中创建控制台应用程序，使用不同的图像和打印选项将工作表转换为图像，使用 Aspose.Cells API 使用几行最简单的代码。

你需要导入[**Aspose.Cells.Rendering**](https://reference.aspose.com/cells/net/aspose.cells.rendering)命名空间到您的程序/项目。它有几个有价值的类，例如，[**图纸渲染**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender), [**图像或打印选项**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions), [**工作簿渲染**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookrender)ETC。

这[**Aspose.Cells.Rendering.SheetRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender)类代表一个工作表，为工作表渲染图像，它有一个重载[**印象**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender/methods/toimage/index)可以将工作表直接转换为使用所需属性或选项指定的图像文件的方法。它可以返回 System.Drawing.Bitmap 对象，您可以将图像文件保存到磁盘/流。支持多种图片格式，例如BMP、PNG、GIFF、JPEG、TIFF、EMF等。

##  **使用 Aspose.Cells 使用 ImageOrPrint 选项将工作表转换为图像。**

###  **在 Microsoft Excel 中创建模板工作簿**

我在 MS Excel 中创建了一个新工作簿，并在第一个工作表中添加了一些数据。现在，我会将模板文件的工作表“Sheet1”转换为图像文件“SheetImage.tiff”，并将应用不同的图像选项，如水平和垂直分辨率、TiffCompression 等。

###  **下载并安装 Aspose.Cells**

首先，你需要[下载](https://downloads.aspose.com/cells/net).Net 的 Aspose.Cells。在您的开发计算机上安装它。全部[Aspose](http://www.aspose.com/)组件在安装后以评估模式工作。评估模式没有时间限制，它只在生成的文档中注入水印。

###  **创建项目**

启动视觉工作室。 Net 并创建一个新的控制台应用程序。此示例将显示 C# 控制台应用程序，但您也可以使用 VB.NET。

###  **添加引用**

该项目将使用 Aspose.Cells。因此，您必须在项目中添加对 Aspose.Cells 组件的引用。例如，添加对 ....\Program Files\Aspose\Aspose.Cells for .NET\Bin\Net1.0\Aspose.Cells.dll 的引用

###  **将工作表转换为图像文件**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UsingImageOrPrintOptions-WorksheetToAnImage-1.cs" >}}

##  **转换选项**

可以将特定页面保存为图像。以下代码将工作簿中的第一个和第二个工作表转换为 JPG 图像。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UsingImageOrPrintOptions-SpecificPagesToImage-1.cs" >}}

##  **使用 WorkbookRender 进行图像转换**

一张 TIFF 图像可以包含多个帧。您可以将整个工作簿保存为具有多帧或多页的单个 TIFF 图像：

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UsingImageOrPrintOptions-UseWorkbookRenderForImageConversion-1.cs" >}}

