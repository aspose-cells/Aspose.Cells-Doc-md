---
title: 将工作表转换为不同的图像格式
type: docs
weight: 30
url: /zh/java/converting-worksheet-to-different-image-formats/
---

{{% alert color="primary" %}}

Aspose.Cells允许您从工作簿导出工作表并将其转换为不同的格式。本文解释了如何将工作表转换为不同的格式。

{{% /alert %}}

## **将工作表转换为图像**

有时保存工作表图片是很有用的。图片可以在线共享，插入到其他文档（例如用Microsoft Word编写的报告或PowerPoint演示文稿）。

Aspose.Cells通过[**SheetRender**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender)类提供图像导出功能。该类表示将呈现为图像的工作表。[**SheetRender**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender)类提供了将工作表转换为图像文件的[**toImage()**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender#toImage(int,%20java.io.OutputStream))方法。支持BMP、PNG、JPEG、TIFF和EMF格式。

{{% alert color="primary" %}}

Aspose.Cells for Java 还支持转换为 TIFF 格式。要将工作表转换为 TIFF 图像，需将 JAI 库添加到类路径中。

{{% /alert %}} {{% alert color="primary" %}}

目前，转换工作表到图像API不支持3D气泡图表。

{{% /alert %}}

下面的代码显示了如何将Microsoft Excel文件中的工作表转换为PNG文件。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-WorksheetToImage-1.java" >}}

## **将工作表转换为SVG**

SVG代表**可伸缩矢量图形**。SVG是基于XML标准的二维矢量图形规范。它是一个开放标准，自1999年由万维网联盟（W3C）开发。

自 v7.1.0 发布以来，**Aspose.Cells for Java** 可以将工作表转换为 SVG 图像。

要使用此功能，您需要在程序或项目中导入com.aspose.cells命名空间。它有一些有价值的类用于呈现和打印，例如[**SheetRender**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender)、[**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions)、[**WorkbookRender**](https://reference.aspose.com/cells/java/com.aspose.cells/workbookrender)等。

[**com.aspose.cells.ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions)类指定工作表将以SVG格式保存。

[**SheetRender**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender)类以[**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions)的对象作为参数，设置保存格式为SVG格式。

下面的代码片段显示了如何将Excel文件中的工作表转换为SVG图像文件。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-ConvertingWorksheetToSVG-ConvertingWorksheetToSVG.java" >}}

### **渲染工作簿中的活动工作表**

将工作簿中的活动工作表转换成SVG的简单方法是设置活动工作表索引，然后将工作簿保存为SVG。这将把活动工作表呈现为SVG。以下示例代码演示了这个特性：

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-ConvertActiveWorksheetToSVG-1.java" >}}

## 相关文章

- [使用viewBox属性将图表导出为SVG](/cells/zh/java/export-chart-to-svg-with-viewbox-attribute/)
- [使用所需的宽度和高度将工作表或图表导出为图像](/cells/zh/java/export-worksheet-or-chart-into-image-with-desired-width-and-height/)
- [将工作表转为图像以及按页面转为图像](/cells/zh/java/converting-worksheet-to-image-and-worksheet-to-image-by-page/)
