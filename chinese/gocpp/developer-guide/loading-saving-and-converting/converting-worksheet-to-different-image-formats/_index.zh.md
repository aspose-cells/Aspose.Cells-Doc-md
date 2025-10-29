---
title: 将工作表转换为不同的图像格式
type: docs
weight: 90
url: /zh/go-cpp/converting-worksheet-to-different-image-formats/
---

{{% alert color="primary" %}}

Aspose.Cells 允许您从工作簿中导出工作表并将其转换为不同的图像格式。本文解释了如何将工作表转换为不同的图像格式。

{{% /alert %}}

## **将工作表转换为图像**

工作表包含您想要分析的数据。例如，工作表可以包含参数、总计、百分比、异常和计算。

作为开发人员，可能需要将工作表作为图片展示。例如，在应用程序或网页中使用工作表的图片，或将图片插入微软Word文档、PDF文件、PowerPoint演示文稿或其他文档类型中。简单来说，您希望将工作表渲染为图片，以便在其他地方使用。

Aspose.Cells支持将Excel工作表转换为图片。要使用此功能，需导入【Aspose.Cells.Rendering】命名空间。它包含多个有用的类，例如【SheetRender】、【ImageOrPrintOptions】等，用于渲染和打印。

【Aspose.Cells.Rendering.ISheetRender】类表示需要渲染为图片的工作表，具有重载方法【ToImage】（https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/toimage/），可以将工作表转换为多种格式的图片文件（如BMP、PNG、GIF、JPG、JPEG、TIFF、EMF）。

以下代码片段显示了如何将Excel文件中的工作表转换为图像文件。

### ** 使用GoLang将Excel/电子表格转换为PNG**

请参阅以下示例代码、其[示例Excel文件](67338402.xlsx)和[输出的PNG图像](67338401.zip)。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ConvertWorksheetToImage_Png.go" >}}

### ** 使用GoLang将Excel/电子表格转换为TIFF**

请参阅以下示例代码、其[示例Excel文件](67338402.xlsx)和[输出的TIFF图像](67338419.zip)。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ConvertWorksheetToImage_Tiff.go" >}}

## ** 使用GoLang将Excel/电子表格转换为SVG**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ConvertWorksheetToImage_Svg.go" >}}

SVG代表可缩放矢量图形。SVG是基于XML标准的二维矢量图形规范。自1999年以来，它一直是由万维网联盟（W3C）开发的开放标准。

自版本24.12.0起，Aspose.Cells for Go via C++已能将工作表转换为SVG图片。

要使用此功能，请将`Aspose.Cells.Rendering`命名空间导入到您的程序或项目中。它具有几个有价值的类用于呈现和打印，例如`ISheetRender`、`IImageOrPrintOptions`等。

`Aspose.Cells.Rendering.IImageOrPrintOptions`类指定工作表将以SVG格式保存。以下代码片段显示了如何将Excel文件中的工作表转换为SVG图像文件。

请参阅以下示例代码、其[示例Excel文件](67338402.xlsx)和[输出的SVG图像](67338403.zip)。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ConvertWorksheetToImage_SVG.go" >}}
