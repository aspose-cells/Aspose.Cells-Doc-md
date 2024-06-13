---
title: 图像
type: docs
weight: 300
url: /zh/python-net/convert-excel-to-image/
description: 使用Aspose.Cells for Python via .NET API将图表转换为图像。
keywords: Python 将图表转换为图像，在Python via NET 中导出图表为图像，Python 保存图表为图像。
---


{{% alert color="primary" %}}

Aspose.Cells for Python via .NET允许您从工作簿中导出工作表并将其转换为不同格式。本文解释了如何将工作表转换为不同格式。

{{% /alert %}}

## 将工作簿转换为TIFF

Excel文件可以包含多个带有多个页面的工作表。[**WorkbookRender**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/workbookrender)允许您将Excel转换为具有多个页面的TIFF。您还可以控制TIFF的多个选项，如[压缩](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/tiff_compression/)，[颜色深度](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/tiff_color_depth/)，分辨率（[水平分辨率](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/horizontal_resolution/)，[垂直分辨率](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/vertical_resolution/)）。

以下代码片段显示了如何将Excel转换为具有多个页面的TIFF。[源Excel文件](workbook-to-tiff-with-mulitiple-pages.xlsx)和[生成的TIFF图像](workbook-to-tiff-with-mulitiple-pages.tiff)附在此供参考。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Workbook-To-Tiff-With-Mulitiple-Pages.py" >}}

## **将工作表转换为图像**

工作表包含您想要分析的数据。例如，工作表可以包含参数、总计、百分比、异常和计算。

作为开发人员，您可能需要将工作表呈现为图像。例如，您可能需要在应用程序或网页中使用工作表的图像。您可能希望将图像插入到 Microsoft Word 文档、PDF 文件、PowerPoint 演示文稿或其他文档类型中。简而言之，您希望将工作表呈现为图像，以便在其他地方使用它。

Aspose.Cells for Python via .NET支持将Excel工作表转换为图像。要使用此功能，您需要将[**aspose.cells.rendering**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/)命名空间导入到您的程序或项目中。它具有几个有价值的类用于渲染和打印，例如[**SheetRender**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender/)、[**ImageOrPrintOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/)、[**WorkbookRender**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/workbookrender/)等。

[**SheetRender**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender/) 类代表要渲染为图像的工作表。 它有一个重载方法，[**to_image**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender/to_image/#int-str)，可以将工作表转换为具有不同属性或选项的图像文件。 它返回一个 System.Drawing.Bitmap 对象，您可以将图像文件保存到磁盘或流中。 支持几种图像格式，例如 BMP、PNG、GIF、JPG、JPEG、TIFF、EMF。

以下代码片段显示了如何将Excel文件中的工作表转换为图像文件。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheet-ConvertWorksheetToImageByPage-1.py" >}}

{{% alert color="primary" %}}

目前，将工作表转换为图像的API不支持3D气泡图。

{{% /alert %}}

## **将工作表转换为SVG**

SVG代表可缩放矢量图形。SVG是基于XML标准的二维矢量图形规范。自1999年以来，它一直是由万维网联盟（W3C）开发的开放标准。

Aspose.Cells for Python via .NET自7.1.0版以来一直能够将工作表转换为SVG图像。以下代码片段显示了如何将Excel文件中的工作表转换为SVG图像文件。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheet-ConvertWorksheetToSVG-1.py" >}}

## **高级主题**
- [将Excel图表转换为图像](/cells/zh/python-net/convert-an-excel-chart-to-image/)
- [将图表转换为SVG格式图像](/cells/zh/python-net/converting-chart-to-image-in-svg-format/)
- [使用viewBox属性将图表导出为SVG](/cells/zh/python-net/export-chart-to-svg-with-viewbox-attribute/)
