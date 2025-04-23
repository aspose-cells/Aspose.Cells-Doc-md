---
title: 使用ImageOrPrint Options将工作表转换为图像
type: docs
weight: 90
url: /zh/net/converting-worksheet-to-image-using-imageorprint-options/
---

{{% alert color="primary" %}}

本文旨在详细介绍如何将工作表转换为图像文件，并应用不同的图像和打印选项，如分辨率、TIFF压缩、图像格式和页面质量。

{{% /alert %}}

## **将工作表保存为图像-不同方法**

有时候，您可能需要将工作表呈现为图形表示。您可能需要将工作表图像嵌入到应用程序或网页中。您可能需要将图像插入到Word文档、PDF文件、PowerPoint演示文稿中，或者在某些其他情景中使用。简单来说，您希望将工作表呈现为图像，以便在别处使用。Aspose.Cells支持将Excel文件中的工作表转换为图像。此外，Aspose.Cells支持设置不同选项，如图像格式、分辨率（垂直和水平）、图像质量以及其他图像和打印选项。

您可能尝试过Office Automation，但Office Automation有自己的缺点。其中涉及多种原因和问题：例如安全性、稳定性、可扩展性和速度、价格和功能。简而言之，有许多原因，最主要的原因是微软自己强烈建议不要从软件解决方案中使用Office Automation。

本文介绍了如何在Visual Studio .NET中创建控制台应用程序，使用Aspose.Cells API以及几行简单的代码执行工作表转换为图像的转换，并使用不同的图像和打印选项。

您需要将[**Aspose.Cells.Rendering**](https://reference.aspose.com/cells/net/aspose.cells.rendering)命名空间导入到您的程序/项目中。它具有几个有价值的类，例如[**SheetRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender)、[**ImageOrPrintOptions**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions)、[**WorkbookRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookrender)等。

类 [**Aspose.Cells.Rendering.SheetRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender) 表示一个工作表来呈现工作表的图像, 它具有重载的 [**ToImage**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender/methods/toimage/index) 方法, 可以直接将工作表转换为指定属性或选项的图像文件。 它可以返回 System.Drawing.Bitmap 对象, 并且您可以将图像文件保存到磁盘/流中。 支持多种图像格式, 例如 BMP、PNG、GIFF、JPEG、TIFF、EMF 等。

## **使用Aspose.Cells将工作表转换为图像，使用图像或打印选项。**

### **在Microsoft Excel中创建一个模板工作簿**

我在MS Excel中创建了一个新的工作簿，并在第一个工作表中添加了一些数据。现在，我将把模板文件的工作表“Sheet1”转换为图像文件“SheetImage.tiff”，并将应用不同的图像选项，如水平和垂直分辨率、TiffCompression等。

### **下载并安装Aspose.Cells**

首先，您需要[下载](https://downloads.aspose.com/cells/net) Aspose.Cells for .Net。将其安装到开发计算机上。所有[Aspose](http://www.aspose.com/)组件，在安装后工作在评估模式中。评估模式没有时间限制，只会向生成的文档中注入水印。

### **创建一个项目**

启动Visual Studio .Net并创建一个新的控制台应用程序。本示例将展示一个C#控制台应用程序，但您也可以使用VB.NET。

### **添加引用**

该项目将使用 Aspose.Cells。因此，您必须在项目中添加对 Aspose.Cells 组件的引用。例如，向….\Program Files\Aspose\Aspose.Cells for .NET\Bin\Net1.0\Aspose.Cells.dll 添加引用。

### **将工作表转换为图像文件**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UsingImageOrPrintOptions-WorksheetToAnImage-1.cs" >}}

## **转换选项**

可以保存特定页面到图像。下面的代码将工作簿中的第一个和第二个工作表转换为JPG图像。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UsingImageOrPrintOptions-SpecificPagesToImage-1.cs" >}}

## **使用 WorkbookRender 进行图片转换**

TIFF图像可以包含多个帧。您可以将整个工作簿保存为单个TIFF图像，带有多个帧或页面：

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UsingImageOrPrintOptions-UseWorkbookRenderForImageConversion-1.cs" >}}

{{< app/cells/assistant language="csharp" >}}
