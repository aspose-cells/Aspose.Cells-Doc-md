---
title: 将工作表转换为图像以及按页将工作表转换为图像
type: docs
weight: 80
url: /zh/python-net/converting-worksheet-to-image-and-worksheet-to-image-by-page/
---

{{% alert color="primary" %}}

本文档旨在为开发人员提供详细了解如何将工作表转换为图像文件以及将带有多个页面的工作表转换为每页一个图像文件。

有时，你可能需要将工作表作为图像显示，例如在应用程序或网页中使用。你可能需要将图像插入 Word 文档、PDF 文件、PowerPoint 演示文稿，或在其他场景中使用。简而言之，你希望将工作表渲染为图像。Aspose.Cells for Python via .NET 支持将 Excel 文件中的工作表转换为图像，并支持将工作簿转换为多张图片，每页一张。

您可以使用Office自动化来实现这一点，但Office自动化有它自己的缺点。有几个原因和问题涉及其中：例如安全性、稳定性、可伸缩性/速度、价格和功能。简而言之，有很多原因，但主要原因是微软自己强烈建议不要使用Office自动化。

{{% /alert %}}

## **使用 Aspose.Cells 将工作表转换为图像文件**

本文演示了如何在 Visual Studio 中创建控制台应用，使用 Aspose.Cells for Python via .NET API 将工作表转换为图像，以及在最少代码行数内将每个工作表转换为一张图像。

您需要将 [**aspose.cells.rendering**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering) 命名空间导入到您的程序/项目中。它具有几个有价值的类，如 [**SheetRender**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender)、[**ImageOrPrintOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions)、[**WorkbookRender**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/workbookrender) 等。[**SheetRender**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender) 类代表要为其渲染图像的工作表，并具有一个重载的 [**to_image**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender/to_image/#int-str) 方法，可以直接将工作表转换为具有任何属性或选项设置的图像文件。它可以返回一个 System.Drawing.Bitmap 对象，您可以将图像文件保存到磁盘/流中。支持多种图像格式，例如 BMP、PNG、GIF、JPG、JPEG、TIFF、EMF 等。

本文说明了如何将工作表转换为图像。此任务演示了如何使用 Aspose.Cells for Python via .NET 将模板工作簿中的工作表转换为图像文件。


### **将工作表转换为图像文件**

我在Microsoft Excel中创建了一个新工作簿，并在第一个工作表中添加了一些数据：**Testbook.xlsx**（1个工作表）。接下来，将模板文件的工作表Sheet1转换为名为SheetImage.jpg的图像文件。

以下是组件用来完成任务的代码。它将**Testbook.xlsx**中的Sheet1转换为图像文件，以说明这种转换有多么简便。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-ConvertWorksheettoImageFile-1.py" >}}

## **使用Aspose.Cells按页将工作表转换为图像文件**

此示例演示如何使用 Aspose.Cells for Python via .NET 将具有多页的模板工作簿中的每一页转换为一张图像。

### **按页将工作表转换为图像**

我在Microsoft Excel中创建了一个新工作簿，并在第一个工作表中添加了一些数据：**Testbook2.xlsx**（1个工作表）。

现在，将模板文件的工作表Sheet1转换为图像文件（每页一个文件）。由于我已经创建了执行复制任务的控制台应用程序，因此我将跳过创建控制台应用程序的步骤，直接转移到工作表转换步骤。

以下是组件用于完成任务的代码。它将Testbook2.xls中的Sheet1转换为每页一个图像文件。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-ConvertWorksheetToImageByPage-1.py" >}}

{{< app/cells/assistant language="python-net" >}}
