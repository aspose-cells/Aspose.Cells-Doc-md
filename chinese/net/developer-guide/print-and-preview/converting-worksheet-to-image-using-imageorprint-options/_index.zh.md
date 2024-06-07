---
title: 使用 ImageOrPrint 选项将工作表转换为图片
type: docs
weight: 90
url: /zh/net/converting-worksheet-to-image-using-imageorprint-options/
---

{{% alert color="primary" %}}

本文旨在详细介绍如何将工作表转换为图片文件，并应用不同的图像和打印选项，如分辨率、TIFF 压缩、图像格式和页面质量等。

{{% /alert %}}

## **将工作表保存为图片 - 不同的方法**

有时您可能需要将工作表呈现为图像。您需要将工作表图像嵌入到应用程序或网页中。您可能需要将图像插入到 Word 文档、PDF 文件、PowerPoint 演示文稿中，或在其他某些情景中使用它们。简单地说，您希望将工作表呈现为图像，以便在其他地方使用。Aspose.Cells 支持将 Excel 文件中的工作表转换为图片。此外，Aspose.Cells 还支持设置不同的选项，如图像格式、分辨率（垂直和水平）、图像质量和其他图像和打印选项。

您可能尝试使用 Office 自动化，但 Office 自动化也有其缺点。涉及到许多原因和问题：例如，安全性、稳定性、可扩展性、速度、价格和功能。简而言之，有许多原因，其中最重要的一个原因是微软强烈建议不要使用 Office 自动化来作为软件解决方案。

本文展示了如何在 Visual Studio .NET 中创建控制台应用程序，使用 Aspose.Cells API 以简单的几行代码执行将工作表转换为图像，并使用不同的图像和打印选项。

您需要将 [**Aspose.Cells.Rendering**](https://reference.aspose.com/cells/net/aspose.cells.rendering) 命名空间导入到您的程序/项目中。它包含一些有价值的类，例如 [**SheetRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender)、[**ImageOrPrintOptions**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions)、[**WorkbookRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookrender) 等。

该 [**Aspose.Cells.Rendering.SheetRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender) 类表示要为工作表呈现的图像，它具有一个重载的 [**ToImage**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender/methods/toimage/index) 方法，可以直接将工作表转换为指定的图像文件并指定所需的属性或选项。它可以返回 System.Drawing.Bitmap 对象，您可以将图像文件保存到磁盘/流中。支持多种图像格式，如 BMP、PNG、GIFF、JPEG、TIFF、EMF 等。

## **使用 Aspose.Cells 使用 ImageOrPrint 选项将工作表转换为图像。**

### **在 Microsoft Excel 中创建一个模板工作簿**

我在 MS Excel 中创建一个新工作簿，并在第一个工作表中添加了一些数据。现在，我将转换模板文件的工作表“Sheet1”为图像文件“SheetImage.tiff”，并将应用不同的图像选项，如水平和垂直分辨率、Tiff 压缩等。

### **下载并安装 Aspose.Cells**

首先，您需要 [下载](https://downloads.aspose.com/cells/net) Aspose.Cells for .Net。将其安装在开发计算机上。所有的 [Aspose](http://www.aspose.com/) 元件，在安装时都是以评估模式运行的。评估模式没有时间限制，只会在生成的文档中插入水印。

### **创建一个项目**

启动 Visual Studio. Net 并创建一个新的控制台应用程序。本示例将展示一个 C# 控制台应用程序，但您也可以使用 VB.NET。

### **添加引用**

此项目将使用 Aspose.Cells。因此，您必须在您的项目中添加对 Aspose.Cells 元件的引用。例如，在 ….\Program Files\Aspose\Aspose.Cells for .NET\Bin\Net1.0\Aspose.Cells.dll 中添加引用。

### **将工作表转换为图像文件**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UsingImageOrPrintOptions-WorksheetToAnImage-1.cs" >}}

## **转换选项**

可以将特定页面保存为图像。以下代码将一个工作簿中的第一个和第二个工作表转换为 JPG 图像。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UsingImageOrPrintOptions-SpecificPagesToImage-1.cs" >}}

## **使用WorkbookRender进行图像转换**

TIFF图像可包含多个帧。您可以将整个工作簿保存为单个具有多帧或页的TIFF图像:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UsingImageOrPrintOptions-UseWorkbookRenderForImageConversion-1.cs" >}}

