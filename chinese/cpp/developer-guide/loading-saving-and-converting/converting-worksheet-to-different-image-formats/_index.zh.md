---
title: 将工作表转换为不同的图像格式
type: docs
weight: 90
url: /zh/cpp/converting-worksheet-to-different-image-formats/
---
{{% alert color="primary" %}} 

Aspose.Cells 允许您从工作簿导出工作表并将其转换为不同的图像格式。本文介绍如何将工作表转换为不同的图像格式。

{{% /alert %}} 
##  **将工作表转换为图像**
工作表包含您要分析的数据。例如，工作表可以包含参数、总计、百分比、例外和计算。

作为开发人员，您可能需要将工作表呈现为图像。例如，您可能需要在应用程序或网页中使用工作表的图像。您可能想要将图像插入 Microsoft Word 文档、PDF 文件、PowerPoint 演示文稿或某些其他文档类型。简而言之，您希望将工作表呈现为图像，以便可以在其他地方使用它。

Aspose.Cells 支持将Excel工作表转换为图像。要使用此功能，您需要导入[Aspose.Cells.Rendering](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/)您的程序或项目的名称空间。它有几个有价值的类用于渲染和打印，例如，[图纸渲染](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/), [图像或打印选项](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/)和别的。

`Aspose.Cells.Rendering.ISheetRender` 类表示渲染为图像的工作表。它有一个重载方法，[印象](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/toimage/)，可以将工作表转换为具有不同属性或选项的图像文件。支持多种图像格式，例如BMP、PNG、GIF、JPG、JPEG、EMF。

以下代码片段显示如何将 Excel 文件中的工作表转换为图像文件。
###  **PNG 格式**
请看下面的示例代码，其[Excel 文件示例](67338402.xlsx)，以及[输出PNG图像](67338401.zip).

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadingSavingAndConverting-ConvertingWorksheetToImage_PNG-new.cpp" >}}
<!--
### **TIFF Format**
Please see the following sample code, its [sample Excel file](67338402.xlsx), and the [output TIFF Image](67338419.zip).

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadingSavingAndConverting-ConvertingWorksheetToImage_TIFF-new.cpp" >}}
-->
##  **将工作表转换为 SVG**
SVG 代表可缩放矢量图形。 SVG是基于XML标准的二维矢量图形规范。它是一个开放标准，自 1999 年以来一直由万维网联盟 (W3C) 开发。

Aspose.Cells for C++ 自版本 18.5.0 以来已能够将工作表转换为 SVG 图像。

要使用此功能，请将 `Aspose.Cells.Rendering` 命名空间导入到您的程序或项目中。它有几个有价值的用于渲染和打印的类，例如 `ISheetRender`、`IImageOrPrintOptions` 等。

`Aspose.Cells.Rendering.IImageOrPrintOptions` 类指定工作表将以 SVG 格式保存。以下代码片段显示如何将 Excel 文件中的工作表转换为 SVG 图像文件

请看下面的示例代码，其[Excel 文件示例](67338402.xlsx)，以及[输出SVG图像](67338403.zip).

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadingSavingAndConverting-ConvertingWorksheetToImage_SVG-new.cpp" >}}
