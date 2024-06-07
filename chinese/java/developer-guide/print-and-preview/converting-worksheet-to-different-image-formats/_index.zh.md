---
title: 将工作表转换为不同的图像格式
type: docs
weight: 30
url: /zh/java/converting-worksheet-to-different-image-formats/
---

{{% alert color="primary" %}}

Aspose.Cells允许您从工作簿中导出工作表并将其转换为不同格式。本文介绍了如何将工作表转换为不同格式。

{{% /alert %}}

## **将工作表转换为图像**

有时保存工作表的图片是很有用的。图片可以在线共享，插入到其他文档中（例如在Microsoft Word中编写的报告或演示文稿中）。Aspose.Cells通过**[SheetRender](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender)**类提供图像导出。该类代表将渲染为图像的工作表。**[SheetRender](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender)**类提供**[toImage()](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender#toImage(int,%20java.io.OutputStream))**方法，用于将工作表转换为图像文件。支持BMP、PNG、JPEG、TIFF和EMF格式。

Aspose.Cells通过**[SheetRender](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender)**类提供图像导出。此类表示将呈现为图像的工作表。**[SheetRender](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender)**类提供**[toImage()](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender#toImage(int,%20java.io.OutputStream))**方法，用于将工作表转换为图像文件。支持BMP、PNG、JPEG、TIFF和EMF格式。

{{% alert color="primary" %}}

Aspose.Cells for Java还支持将工作表转换为TIFF格式。要将工作表转换为TIFF图像，请将JAI库添加到类路径。

{{% /alert %}} {{% alert color="primary" %}}

目前，将工作表转换为图像API不支持3D气泡图。

{{% /alert %}}

下面的代码显示如何将Microsoft Excel文件中的工作表转换为PNG文件。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-WorksheetToImage-1.java" >}}

## **将工作表转换为SVG**

SVG代表**可缩放矢量图形**。SVG是基于XML标准的二维矢量图形规范。它是一个开放标准，自1999年以来由万维网联盟（W3C）开发。

自v7.1.0发布以来，**Aspose.Cells for Java**可以将工作表转换为SVG图像。

要使用此功能，您需要将com.aspose.cells命名空间导入到您的程序或项目中。它有几个有价值的类用于渲染和打印，例如**[SheetRender](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender)**，**[ImageOrPrintOptions](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions)**，**[WorkbookRender](https://reference.aspose.com/cells/java/com.aspose.cells/workbookrender)**等。

**[com.aspose.cells.ImageOrPrintOptions](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions)**类指定将工作表以SVG格式保存。

**[SheetRender](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender)**类将**[ImageOrPrintOptions](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions)**的对象作为参数，设置保存格式为SVG格式。

以下代码片段显示如何将Excel文件中的工作表转换为SVG图像文件。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-ConvertingWorksheetToSVG-ConvertingWorksheetToSVG.java" >}}

### **渲染工作簿中的活动工作表**

在工作簿中将活动工作表转换为图像的简单方法是设置活动工作表索引，然后将工作簿保存为SVG。它将活动工作表渲染为SVG。以下示例代码演示了此功能：

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-ConvertActiveWorksheetToSVG-1.java" >}}

## 相关文章

- [使用viewBox属性将图表导出为SVG](/cells/zh/java/export-chart-to-svg-with-viewbox-attribute/)
- [使用所需宽度和高度将工作表或图表导出为图像](/cells/zh/java/export-worksheet-or-chart-into-image-with-desired-width-and-height/)
- [将工作表转换为图像和按页转换工作表为图像](/cells/zh/java/converting-worksheet-to-image-and-worksheet-to-image-by-page/)
