---
title: 将工作表转换为不同的图像格式
type: docs
weight: 90
url: /zh/cpp/converting-worksheet-to-different-image-formats/
---

{{% alert color="primary" %}} 

Aspose.Cells 允许您从工作簿中导出工作表并将其转换为不同的图像格式。本文解释了如何将工作表转换为不同的图像格式。

{{% /alert %}} 
## **将工作表转换为图像**
工作表包含您想要分析的数据。例如，工作表可以包含参数、总计、百分比、异常和计算。

作为开发人员，您可能需要将工作表呈现为图像。例如，您可能需要在应用程序或网页中使用工作表的图像。您可能希望将图像插入到 Microsoft Word 文档、PDF 文件、PowerPoint 演示文稿或其他文档类型中。简而言之，您希望将工作表呈现为图像，以便在其他地方使用它。

Aspose.Cells支持将Excel工作表转换为图像。要使用此功能，您需要将`Aspose.Cells.Rendering`命名空间导入到您的程序或项目中。它具有几个有价值的类用于呈现和打印，例如`SheetRender`、`ImageOrPrintOptions`等。

`Aspose.Cells.Rendering.ISheetRender`类表示要呈现为图像的工作表。它有一个重载的方法`ToImage`，可以使用不同的属性或选项将工作表转换为图像文件。支持多种图像格式，例如BMP、PNG、GIF、JPG、JPEG、TIFF、EMF。

以下代码片段显示了如何将Excel文件中的工作表转换为图像文件。
### **PNG格式**
请参阅以下示例代码、其[示例Excel文件](67338402.xlsx)和[输出的PNG图像](67338401.zip)。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadingSavingAndConverting-ConvertingWorksheetToImage_PNG-new.cpp" >}}

### **TIFF格式**
请参阅以下示例代码、其[示例Excel文件](67338402.xlsx)和[输出的TIFF图像](67338419.zip)。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadingSavingAndConverting-ConvertingWorksheetToImage_TIFF-new.cpp" >}}

## **将工作表转换为SVG**
SVG代表可缩放矢量图形。SVG是基于XML标准的二维矢量图形规范。自1999年以来，它一直是由万维网联盟（W3C）开发的开放标准。

Aspose.Cells for C++自版本18.5.0以来就能够将工作表转换为SVG图像。

要使用此功能，请将`Aspose.Cells.Rendering`命名空间导入到您的程序或项目中。它具有几个有价值的类用于呈现和打印，例如`ISheetRender`、`IImageOrPrintOptions`等。

`Aspose.Cells.Rendering.IImageOrPrintOptions`类指定工作表将以SVG格式保存。以下代码片段显示了如何将Excel文件中的工作表转换为SVG图像文件。

请参阅以下示例代码、其[示例Excel文件](67338402.xlsx)和[输出的SVG图像](67338403.zip)。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadingSavingAndConverting-ConvertingWorksheetToImage_SVG-new.cpp" >}}
