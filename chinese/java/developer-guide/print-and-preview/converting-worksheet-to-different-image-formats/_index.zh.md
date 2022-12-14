---
title: 将工作表转换为不同的图像格式
type: docs
weight: 30
url: /zh/java/converting-worksheet-to-different-image-formats/
---
{{% alert color="primary" %}}

Aspose.Cells 允许您从工作簿中导出工作表并将其转换为不同的格式。本文介绍如何将工作表转换为不同的格式。

{{% /alert %}}

## **将工作表转换为图像**

有时，保存工作表的图片很有用。图像可以在线共享，插入到其他文档中（例如，用 Microsoft Word 编写的报告，或 PowerPoint 演示文稿）。

Aspose.Cells 提供图片导出通过**[SheetRender](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender)**班级。此类表示将呈现为图像的工作表。这**[SheetRender](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender)**类提供了**[toImage()](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender#toImage(int,%20java.io.OutputStream))**将工作表转换为图像文件的方法。支持 BMP、PNG、JPEG、TIFF 和 EMF 格式。

{{% alert color="primary" %}}

Aspose.Cells for Java 也支持转换为TIFF格式。要将工作表转换为 TIFF 图像，请将 JAI 库添加到类路径中。

{{% /alert %}} {{% alert color="primary" %}}

目前工作表转图API不支持3D气泡图。

{{% /alert %}}

下面的代码显示了如何将 Microsoft Excel 文件中的工作表转换为 PNG 文件。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-WorksheetToImage-1.java" >}}

## **将工作表转换为 SVG**

 SVG代表**可缩放矢量图形**SVG 是一种基于 XML 标准的二维矢量图形规范。它是一个开放标准，自 1999 年以来一直由万维网联盟 (W3C) 开发。

自 v7.1.0 发布以来，**Aspose.Cells for Java**可以将工作表转换为 SVG 图像。

要使用此功能，您需要将 com.aspose.cells 命名空间导入您的程序或项目。它有几个有价值的渲染和打印类，例如，**[SheetRender](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender)**, **[ImageOrPrintOptions](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions)**, **[WorkbookRender](https://reference.aspose.com/cells/java/com.aspose.cells/workbookrender)**， 和别的。

这**[com.aspose.cells.ImageOrPrintOptions](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions)** class 指定工作表将以 SVG 格式保存。

这**[SheetRender](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender)**类接受的对象**[ImageOrPrintOptions](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions)**作为将保存格式设置为 SVG 格式的参数。

以下代码片段显示了如何将 Excel 文件中的工作表转换为 SVG 图像文件。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-ConvertingWorksheetToSVG-ConvertingWorksheetToSVG.java" >}}

### **在工作簿中呈现活动工作表**

转换工作簿中的活动工作表的一种简单方法是设置活动工作表索引，然后将工作簿另存为 SVG。它会将活动工作表呈现为 SVG。以下示例代码演示了此功能：

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-ConvertActiveWorksheetToSVG-1.java" >}}

## 相关文章

- [使用 viewBox 属性将图表导出为 SVG](/cells/zh/java/export-chart-to-svg-with-viewbox-attribute/)
- [将工作表或图表导出为具有所需宽度和高度的图像](/cells/zh/java/export-worksheet-or-chart-into-image-with-desired-width-and-height/)
- [按页将工作表转换为图像并将工作表转换为图像](/cells/zh/java/converting-worksheet-to-image-and-worksheet-to-image-by-page/)
