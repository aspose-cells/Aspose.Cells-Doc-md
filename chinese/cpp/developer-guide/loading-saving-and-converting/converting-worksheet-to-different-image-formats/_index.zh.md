---
title: 将工作表转换为不同的图像格式
type: docs
weight: 90
url: /zh/cpp/converting-worksheet-to-different-image-formats/
---
{{% alert color="primary" %}} 

Aspose.Cells 允许您从工作簿导出工作表并将其转换为不同的图像格式。本文介绍如何将工作表转换为不同的图像格式。

{{% /alert %}} 
## **将工作表转换为图像**
工作表包含您要分析的数据。例如，工作表可以包含参数、总计、百分比、异常和计算。

作为开发人员，您可能需要将工作表显示为图像。例如，您可能需要在应用程序或网页中使用工作表的图像。您可能希望将图像插入 Microsoft Word 文档、PDF 文件、PowerPoint 演示文稿或其他文档类型。简而言之，您希望将工作表呈现为图像，以便您可以在其他地方使用它。

Aspose.Cells 支持将Excel工作表转换为图片。要使用此功能，您需要导入[Aspose.Cells.Rendering](https://reference.aspose.com/cells/cpp/namespace/aspose.cells.rendering)命名空间到您的程序或项目。它有几个有价值的渲染和打印类，例如，[表单渲染](https://reference.aspose.com/cells/cpp/class/aspose.cells.rendering.i_sheet_render), [IImageOrPrint选项](https://reference.aspose.com/cells/cpp/class/aspose.cells.rendering.i_image_or_print_options)和别的。

`Aspose.Cells.Rendering.ISheetRender` 类表示要呈现为图像的工作表。它有一个重载方法，[印象](https://reference.aspose.com/cells/cpp/class/aspose.cells.rendering.i_sheet_render#ae508827a76d0c353ab0890024ec363c5)，可以将工作表转换为具有不同属性或选项的图像文件。支持多种图像格式，例如 BMP、PNG、GIF、JPG、JPEG、TIFF、EMF。

以下代码片段显示了如何将 Excel 文件中的工作表转换为图像文件。
### **PNG格式**
请看下面的示例代码，其[示例 Excel 文件](67338402.xlsx) 和[输出PNG图像](67338401.zip).

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadingSavingAndConverting-ConvertingWorksheetToImage_PNG.cpp" >}}
### **TIFF 格式**
请看下面的示例代码，其[示例 Excel 文件](67338402.xlsx) 和[输出 TIFF 图像](67338419.zip).

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadingSavingAndConverting-ConvertingWorksheetToImage_TIFF.cpp" >}}
## **将工作表转换为 SVG**
SVG 代表可缩放矢量图形。 SVG 是一种基于 XML 标准的二维矢量图形规范。它是一个开放标准，自 1999 年以来一直由万维网联盟 (W3C) 开发。

Aspose.Cells for C++ 从版本 18.5.0 开始可以将工作表转换为 SVG 图像。

要使用此功能，请将 `Aspose.Cells.Rendering` 命名空间导入您的程序或项目。它有几个用于渲染和打印的有价值的类，例如 `ISheetRender`、`IImageOrPrintOptions` 等。

`Aspose.Cells.Rendering.IImageOrPrintOptions` 类指定工作表将以 SVG 格式保存。以下代码片段显示了如何将 Excel 文件中的工作表转换为 SVG 图像文件

请看下面的示例代码，其[示例 Excel 文件](67338402.xlsx) 和[输出 SVG 图像](67338403.zip).

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadingSavingAndConverting-ConvertingWorksheetToImage_SVG.cpp" >}}
