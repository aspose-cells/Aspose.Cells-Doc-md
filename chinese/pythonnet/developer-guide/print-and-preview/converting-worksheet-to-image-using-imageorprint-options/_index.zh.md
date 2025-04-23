---
title: 使用ImageOrPrint Options将工作表转换为图像
type: docs
weight: 90
url: /zh/python-net/converting-worksheet-to-image-using-imageorprint-options/
---

{{% alert color="primary" %}}

本文旨在详细介绍如何将工作表转换为图像文件，并应用不同的图像和打印选项，如分辨率、TIFF压缩、图像格式和页面质量。

{{% /alert %}}

## **将工作表保存为图像-不同方法**

有时，你需要以图片形式展示工作表。你希望在应用或网页中插入图片，或者用于其他场景。你希望将工作表渲染为图片以便在其他地方使用。Aspose.Cells for Python via .NET 支持将 Excel 文件中的工作表转换为图片，还支持设置图片格式、分辨率（垂直和水平）、图片质量及其他图片和打印选项。

您可能尝试过Office Automation，但Office Automation有自己的缺点。其中涉及多种原因和问题：例如安全性、稳定性、可扩展性和速度、价格和功能。简而言之，有许多原因，最主要的原因是微软自己强烈建议不要从软件解决方案中使用Office Automation。

本文演示了如何在 Visual Studio .NET 中创建控制台应用，使用 Aspose.Cells for Python via .NET 通过不同的图片和打印选项，将工作表转换为图片，并用最少代码实现。

您需要将[**aspose.cells.rendering**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering)命名空间导入到您的程序/项目中。它具有几个有价值的类，例如[**SheetRender**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender)、[**ImageOrPrintOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions)、[**WorkbookRender**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/workbookrender)等。

类 [**SheetRender**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender) 表示一个工作表来呈现工作表的图像, 它具有重载的 [**to_image**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender/to_image/#int-str) 方法, 可以直接将工作表转换为指定属性或选项的图像文件。 它可以返回 System.Drawing.Bitmap 对象, 并且您可以将图像文件保存到磁盘/流中。 支持多种图像格式, 例如 BMP、PNG、GIFF、JPEG、TIFF、EMF 等。

## **使用 Aspose.Cells 通过 ImageOrPrint 选项将工作表转换为图像**

### **在Microsoft Excel中创建一个模板工作簿**

我在MS Excel中创建了一个新的工作簿，并在第一个工作表中添加了一些数据。现在，我将把模板文件的工作表“Sheet1”转换为图像文件“SheetImage.tiff”，并将应用不同的图像选项，如水平和垂直分辨率、TiffCompression等。

### **将工作表转换为图像文件**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-WorksheetToAnImage-1.py" >}}


## **使用 WorkbookRender 进行图片转换**

TIFF图像可以包含多个帧。您可以将整个工作簿保存为单个TIFF图像，带有多个帧或页面：

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-UseWorkbookRenderForImageConversion-1.py" >}}

