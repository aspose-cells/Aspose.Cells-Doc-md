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

The [**Aspose.Cells.Rendering.SheetRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender) class represents a worksheet to render images for the worksheet, it has an overloaded [**ToImage**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender/methods/toimage/index) method that can directly convert a worksheet to image file(s) specified with your desired attributes or options. It can return System.Drawing.Bitmap object and you can Save an image file to the disk/stream. There are several image formats supported, e.g BMP, PNG, GIFF, JPEG, TIFF, EMF and so on.

## **Using Aspose.Cells to Convert Worksheet to Image using ImageOrPrint options.**

### **Creating a template workbook in Microsoft Excel**

I created a new workbook in MS Excel and added some data in the first worksheet. Now, I will convert the template file’s worksheet “Sheet1” to an image file “SheetImage.tiff” and will apply different image options like horizontal and vertical resolutions, TiffCompression etc.

### **Download and Install Aspose.Cells**

First, you need to [download](https://downloads.aspose.com/cells/net) Aspose.Cells for .Net. Install it on your development computer. All [Aspose](http://www.aspose.com/) components, when installed, work in evaluation mode. The evaluation mode has no time limit and it only injects watermarks into produced documents.

### **Create a Project**

Start Visual Studio. Net and create a new console application. This example will show a C# console application, but you can use VB.NET too.

### **Add References**

该项目将使用 Aspose.Cells。因此，您必须在项目中添加对 Aspose.Cells 组件的引用。例如，向….\Program Files\Aspose\Aspose.Cells for .NET\Bin\Net1.0\Aspose.Cells.dll 添加引用。

### **Convert Worksheet to an Image file**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UsingImageOrPrintOptions-WorksheetToAnImage-1.cs" >}}

## **转换选项**

可以保存特定页面到图像。下面的代码将工作簿中的第一个和第二个工作表转换为JPG图像。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UsingImageOrPrintOptions-SpecificPagesToImage-1.cs" >}}

## **Image conversion using WorkbookRender**

A TIFF image can contian more than one frames. You can save the whole workbook to a single TIFF image with multiply frames or pages:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UsingImageOrPrintOptions-UseWorkbookRenderForImageConversion-1.cs" >}}

