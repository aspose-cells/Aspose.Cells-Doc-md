---
title: 使用 Golang 通过 C++ 将 Excel 转换为图片
linktitle: 将Excel转换为图像
type: docs
weight: 300
url: /zh/go-cpp/convert-excel-to-image/
description: 学习如何使用Aspose.Cells for C++将Excel工作表转换为包括TIFF和SVG格式的图片。
---

{{% alert color="primary" %}}

Aspose.Cells允许您从工作簿导出工作表并将其转换为不同的格式。本文解释了如何将工作表转换为不同的格式。

{{% /alert %}}

## 将工作簿转换为TIFF

Excel文件可以包含多个工作表与多页内容。[**WorkbookRender**](https://reference.aspose.com/cells/go-cpp/workbookrender/)允许你将Excel转换为多页TIFF。同时，可以控制TIFF的多项选项，如[压缩](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/tiffcompression/)、[GetTiffColorDepth()](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/gettiffcolordepth/)、分辨率（[GetHorizontalResolution()](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/gethorizontalresolution/)、[GetVerticalResolution()](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getverticalresolution/)。

以下代码片段显示了如何将Excel转换为具有多个页面的TIFF。[源Excel文件](workbook-to-tiff-with-mulitiple-pages.xlsx)和[生成的TIFF图像](workbook-to-tiff-with-mulitiple-pages.tiff)附在此供参考。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-Image.go" >}}
## **将工作表转换为图像**

工作表包含您想要分析的数据。例如，工作表可以包含参数、总计、百分比、异常和计算。

作为开发人员，您可能需要将工作表呈现为图像。例如，您可能需要在应用程序或网页中使用工作表的图像。您可能希望将图像插入到 Microsoft Word 文档、PDF 文件、PowerPoint 演示文稿或其他文档类型中。简而言之，您希望将工作表呈现为图像，以便在其他地方使用它。

Aspose.Cells支持将Excel工作表转换为图片。要使用此功能，需要在程序或项目中导入[**Aspose.Cells.Rendering**](https://reference.aspose.com/cells/go-cpp/)命名空间。它包含多个用于渲染和打印的类，例如[**SheetRender**](https://reference.aspose.com/cells/go-cpp/sheetrender/)、[**ImageOrPrintOptions**](https://reference.aspose.com/cells/go-cpp/imageorprintoptions/)、[**WorkbookRender**](https://reference.aspose.com/cells/go-cpp/workbookrender/)等。

[**SheetRender**](https://reference.aspose.com/cells/go-cpp/sheetrender/)类代表待渲染为图像的工作表。它拥有重载方法[**ToImage**](https://reference.aspose.com/cells/go-cpp/sheetrender/toimage/)，可以将工作表转换为不同属性或选项的图像文件。它返回一个`System.Drawing.Bitmap`对象，可以将图像保存到磁盘或流中。支持多种图像格式，例如BMP、PNG、GIF、JPG、JPEG、TIFF、EMF。

以下代码片段显示了如何将Excel文件中的工作表转换为图像文件。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-Image-1.go" >}}
{{% alert color="primary" %}}

目前，将工作表转换为图像的API不支持3D气泡图。

{{% /alert %}}

## **将工作表转换为SVG**

SVG代表可缩放矢量图形。SVG是基于XML标准的二维矢量图形规范。自1999年以来，它一直是由万维网联盟（W3C）开发的开放标准。

自7.1.0版起，Aspose.Cells for C++已支持将工作表转换为SVG图像文件。以下代码演示了如何将Excel文件中的工作表转换为SVG图像文件。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-Image-2.go" >}}
## **高级主题**
- [将Excel图表转换为图像](/cells/zh/cpp/convert-an-excel-chart-to-image/)
- [将图表转换为SVG格式图像](/cells/zh/cpp/converting-chart-to-image-in-svg-format/)
- [使用viewBox属性将图表导出为SVG](/cells/zh/cpp/export-chart-to-svg-with-viewbox-attribute/)
- [跟踪Excel转换为TIFF的进度](/cells/zh/cpp/track-conversion-progress-of-excel-to-tiff/)
