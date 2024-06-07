---
title: 使用ImageOrPrintOptions将工作表和工作簿渲染为图像
type: docs
weight: 220
url: /zh/java/render-the-worksheet-and-workbook-to-image-using-imageorprintoptions/
---

{{% alert color="primary" %}}

本文旨在提供如何将工作表或工作簿转换为图像文件并应用不同的图像和打印选项的详细理解，如分辨率、TIFF压缩、图像格式和页面质量等选项。

{{% /alert %}}

## **概览**

有时您可能需要将工作表呈现为图像。您需要将工作表图像嵌入到应用程序或网页中。您可能需要将图像插入到 Word 文档、PDF 文件、PowerPoint 演示文稿中，或在其他某些情景中使用它们。简单地说，您希望将工作表呈现为图像，以便在其他地方使用。Aspose.Cells 支持将 Excel 文件中的工作表转换为图片。此外，Aspose.Cells 还支持设置不同的选项，如图像格式、分辨率（垂直和水平）、图像质量和其他图像和打印选项。

API提供了几个有价值的类，例如[**SheetRender**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetRender)，[**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions)，[**WorkbookRender**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookRender)等。

[**SheetRender**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetRender)类处理工作表的图像呈现任务，而[**WorkbookRender**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookRender)类处理工作簿的图像呈现任务。上述两个类都具有多个*toImage*方法的重载版本，可以直接将工作表或工作簿转换为带有所需属性或选项的图像文件。您可以将图像文件保存到磁盘/流中。支持多种图像格式，如BMP、PNG、GIFF、JPEG、TIFF、EMF等。

### **将工作表转换为图像**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-ConvertWorksheettoImage-1.java" >}}

## **转换选项**

可以将特定页面保存为图像。以下代码将一个工作簿中的第一个和第二个工作表转换为 JPG 图像。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-ConversionOptions-1.java" >}}

或者您可以遍历工作簿，并将其中的每个工作表呈现为单独的图像：

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-WorksheetToSeparateImage-1.java" >}}

## **将工作簿转换为图像：**

为了将完整的工作簿呈现为图像格式，您可以使用上述方法或简单地使用[**WorkbookRender**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookRender)类，该类接受[**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)类的实例以及[**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions)类的对象。

您可以将整个工作簿保存为带有多个帧或页面的单个TIFF图像：

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-ConvertWorkbooktoImage-1.java" >}}

## 相关文章

- [将工作表转换为不同的图像格式](/cells/zh/java/converting-worksheet-to-different-image-formats/)
- [使用viewBox属性将图表导出为SVG](/cells/zh/java/export-chart-to-svg-with-viewbox-attribute/)
- [使用所需宽度和高度将工作表或图表导出为图像](/cells/zh/java/export-worksheet-or-chart-into-image-with-desired-width-and-height/)
- [将工作表转换为图像和按页转换工作表为图像](/cells/zh/java/converting-worksheet-to-image-and-worksheet-to-image-by-page/)
