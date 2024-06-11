---
title: 使用 ImageOrPrintOptions 将工作表和工作簿转换为图像
type: docs
weight: 220
url: /zh/java/render-the-worksheet-and-workbook-to-image-using-imageorprintoptions/
---

{{% alert color="primary" %}}

本文档旨在详细介绍将工作表或工作簿转换为图像文件并对图像和打印选项应用不同设置的方法，如分辨率、TIFF 压缩、图像格式和页面质量。

{{% /alert %}}

## **概述**

有时候，您可能需要将工作表呈现为图形表示。您可能需要将工作表图像嵌入到应用程序或网页中。您可能需要将图像插入到Word文档、PDF文件、PowerPoint演示文稿中，或者在某些其他情景中使用。简单来说，您希望将工作表呈现为图像，以便在别处使用。Aspose.Cells支持将Excel文件中的工作表转换为图像。此外，Aspose.Cells支持设置不同选项，如图像格式、分辨率（垂直和水平）、图像质量以及其他图像和打印选项。

该 API 提供了一些有价值的类，例如 [**SheetRender**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetRender)、[**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions)、[**WorkbookRender**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookRender) 等。

[**SheetRender**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetRender)类处理渲染工作表图像的任务，而[**WorkbookRender**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookRender)类则处理工作簿的渲染。上述两个类都有多个重载版本的*toImage*方法，可以直接将工作表或工作簿转换为指定属性或选项的图像文件。您可以将图像文件保存到磁盘/流中。支持多种图像格式，例如BMP，PNG，GIFF，JPEG，TIFF，EMF等。

### **将工作表转为图像**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-ConvertWorksheettoImage-1.java" >}}

## **转换选项**

可以保存特定页面到图像。下面的代码将工作簿中的第一个和第二个工作表转换为JPG图像。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-ConversionOptions-1.java" >}}

或者您可以循环遍历工作簿，并将其中的每个工作表渲染为单独的图像：

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-WorksheetToSeparateImage-1.java" >}}

## **将工作簿转为图像**

要将完整的工作簿渲染为图像格式，您可以采用上述方法，也可以简单地使用接受[**WorkbookRender**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookRender)类的实例以及[**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)对象的[**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions)对象。

您可以将整个工作簿保存到包含多帧或多页的单个TIFF图像中：

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-ConvertWorkbooktoImage-1.java" >}}

## 相关文章

- [将工作表转换为不同的图像格式](/cells/zh/java/converting-worksheet-to-different-image-formats/)
- [使用viewBox属性将图表导出为SVG](/cells/zh/java/export-chart-to-svg-with-viewbox-attribute/)
- [使用所需的宽度和高度将工作表或图表导出为图像](/cells/zh/java/export-worksheet-or-chart-into-image-with-desired-width-and-height/)
- [将工作表转为图像以及按页面转为图像](/cells/zh/java/converting-worksheet-to-image-and-worksheet-to-image-by-page/)
