---
title: 使用 ImageOrPrintOptions 将工作表和工作簿呈现为图像
type: docs
weight: 220
url: /zh/java/render-the-worksheet-and-workbook-to-image-using-imageorprintoptions/
---
{{% alert color="primary" %}}

本文档旨在详细介绍如何将工作表或工作簿转换为图像文件，并为图像应用不同的图像和打印选项，如分辨率、TIFF 压缩、图像格式和页面质量等选项。

{{% /alert %}}

## **概述**

有时，您可能需要将您的工作表呈现为图形表示。您确实需要将工作表图像显示到您的应用程序或网页中。您可能需要将图像插入到 Word 文档、PDF 文件、PowerPoint 演示文稿中，或者在其他一些场景中使用它们。您只需要将工作表呈现为图像，以便您可以在其他地方使用它。 Aspose.Cells 支持将Excel文件中的工作表转换为图片。此外，Aspose.Cells 支持设置不同的选项，如图像格式、分辨率（垂直和水平）、图像质量以及其他图像和打印选项。

API 提供了几个有价值的类，例如，[**图纸渲染**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetRender), [**图像或打印选项**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions), [**工作簿渲染**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookRender)， ETC。

这[**图纸渲染**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetRender)类处理为工作表渲染图像的任务，而[**工作簿渲染**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookRender)对工作簿做同样的事情。上述两个类都有几个重载版本*印象*可以将工作表或工作簿直接转换为使用所需属性或选项指定的图像文件的方法。您可以将图像文件保存到磁盘/流中。支持多种图像格式，例如 BMP、PNG、GIFF、JPEG、TIFF、EMF 等。

### **将工作表转换为图像**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-ConvertWorksheettoImage-1.java" >}}

## **转换选项**

可以将特定页面保存到图像中。以下代码将工作簿中的第一个和第二个工作表转换为 JPG 图像。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-ConversionOptions-1.java" >}}

或者您可以循环浏览工作簿并将其中的每个工作表呈现为单独的图像：

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-WorksheetToSeparateImage-1.java" >}}

## **将工作簿转换为图像：**

为了将完整的工作簿呈现为图像格式，您可以使用上述方法或简单地使用[**工作簿渲染**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookRender)接受实例的类[**工作簿**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)以及对象[**图像或打印选项**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions).

{{% alert color="primary" %}}

这[**工作簿渲染**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookRender)类只能将工作簿保存为TIFF格式。

{{% /alert %}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-ConvertWorkbooktoImage-1.java" >}}

## 相关文章

- [将工作表转换为不同的图像格式](/cells/zh/java/converting-worksheet-to-different-image-formats/)
- [使用 viewBox 属性将图表导出到 SVG](/cells/zh/java/export-chart-to-svg-with-viewbox-attribute/)
- [将工作表或图表导出为具有所需宽度和高度的图像](/cells/zh/java/export-worksheet-or-chart-into-image-with-desired-width-and-height/)
- [按页将工作表转换为图像并将工作表转换为图像](/cells/zh/java/converting-worksheet-to-image-and-worksheet-to-image-by-page/)
