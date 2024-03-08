---
title: Image
type: docs
weight: 300
url: /zh/python-net/convert-excel-to-image/
description: 使用 Aspose.Cells for Python via .NET API 将图表转换为 Image。
keywords: Python Convert Chart to Image, Export Chart to Image in Python via NET, Python Save Chart to Image.
---
{{% alert color="primary" %}}

Aspose.Cells for Python via .NET 允许您从工作簿导出工作表并将其转换为不同的格式。本文介绍如何将工作表转换为不同的格式。

{{% /alert %}}

## 将工作簿转换为 TIFF

 Excel 文件可以包含多个工作表和多个页面。[工作簿渲染](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/workbookrender)允许您将 Excel 转换为多页的 TIFF。此外，您还可以控制 TIFF 的多个选项，例如[压缩](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/tiff_compression/), [颜色深度](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/tiff_color_depth/)， 解决（[水平分辨率](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/horizontal_resolution/), [垂直分辨率](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/vertical_resolution/)).

下面的代码片段展示了如何将Excel转换为多页的TIFF。这[源 Excel 文件](workbook-to-tiff-with-mulitiple-pages.xlsx)和[生成 TIFF 图像](workbook-to-tiff-with-mulitiple-pages.tiff)附上供您参考。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Workbook-To-Tiff-With-Mulitiple-Pages.py" >}}

##  **将工作表转换为 Image**

工作表包含您要分析的数据。例如，工作表可以包含参数、总计、百分比、例外和计算。

作为开发人员，您可能需要将工作表呈现为图像。例如，您可能需要在应用程序或网页中使用工作表的图像。您可能想要将图像插入 Microsoft Word 文档、PDF 文件、PowerPoint 演示文稿或某些其他文档类型。简而言之，您希望将工作表呈现为图像，以便可以在其他地方使用它。

Aspose.Cells for Python via .NET 支持将 Excel 工作表转换为图像。要使用此功能，您需要导入**[aspose.cells.rendering](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/)**您的程序或项目的名称空间。它有几个有价值的类用于渲染和打印，例如*[图纸渲染](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender/)**, *[图像或打印选项](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/)**, *[工作簿渲染](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/workbookrender/)**， 和别的。

这**[SheetRender](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender/)**类表示要呈现为图像的工作表。它有一个重载方法，*[印象](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender/to_image/#int-str)**，可以将工作表转换为具有不同属性或选项的图像文件。它返回一个 System.Drawing.Bitmap 对象，您可以将图像文件保存到磁盘或流中。支持多种图像格式，例如 BMP、PNG、GIF、JPG、JPEG、TIFF、EMF。

以下代码片段显示如何将 Excel 文件中的工作表转换为图像文件。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheet-ConvertWorksheetToImageByPage-1.py" >}}

{{% alert color="primary" %}}

目前，用于将工作表转换为图像的API不支持3D气泡图。

{{% /alert %}}

##  **将工作表转换为 SVG**

SVG 代表可缩放矢量图形。 SVG是基于XML标准的二维矢量图形规范。它是一个开放标准，自 1999 年以来一直由万维网联盟 (W3C) 开发。

Aspose.Cells for Python via .NET 自版本 7.1.0 以来已经能够将工作表转换为 SVG 图像。以下代码片段显示如何将 Excel 文件中的工作表转换为 SVG 图像文件。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheet-ConvertWorksheetToSVG-1.py" >}}

##  **高级主题**
- [将 Excel 图表转换为 Image](/cells/zh/python-net/convert-an-excel-chart-to-image/)
- [将图表转换为 SVG 格式的 Image](/cells/zh/python-net/converting-chart-to-image-in-svg-format/)
- [使用 viewBox 属性将图表导出到 SVG](/cells/zh/python-net/export-chart-to-svg-with-viewbox-attribute/)
