---
title: 按页将工作表转换为图像并将工作表转换为图像
type: docs
weight: 210
url: /zh/java/converting-worksheet-to-image-and-worksheet-to-image-by-page/
---
{{% alert color="primary" %}}

本文档旨在让开发人员详细了解如何将工作表转换为图像文件以及将多页工作表转换为每页图像文件。

有时，您可能需要将工作表显示为图像，例如，以便在应用程序或网页中使用它们。您可能需要将图像插入到 Word 文档、PDF 文件、PowerPoint 演示文稿中，或者在其他一些场景中使用它们。简单地说，您想将工作表呈现为图像。 Aspose.Cells API 支持将 Microsoft Excel 文件中的工作表转换为图像。此外，Aspose.Cells 支持将工作簿转换为多个图像文件，每页一个。

{{% /alert %}}

## **使用 Aspose.Cells 将工作表转换为图像文件**

本文介绍如何使用 Aspose.Cells for Java API 将工作表转换为图像。 API提供了几个有价值的类，比如[**图纸渲染**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetRender), [**图像或打印选项**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions), [**工作簿渲染**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookRender)， 等等。这[**图纸渲染**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetRender)类代表一个工作表，为工作表渲染图像，并有一个重载[**印象**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender#toImage(int,%20java.io.OutputStream)方法，可以将工作表直接转换为具有任何属性或选项集的图像文件。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-ConvertWorksheettoImageFile-1.java" >}}

### **结果**

执行上述代码后，名为Sheet1的工作表被转换为图像文件SheetImage.jpg。

**输出 JPG**

![待办事项：图像_替代_文本](converting-worksheet-to-image-and-worksheet-to-image-by-page_1.png)

## **使用 Aspose.Cells 将工作表按页转换为图像文件**

此示例说明如何使用 Aspose.Cells 将工作表从具有多页的模板工作簿转换为每页一个图像文件。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-ConvertWorksheetToImageByPage-1.java" >}}

### **结果**

执行上述代码后，名为 Sheet1 的工作表被转换为两个图像文件（每页 1 个）Sheet 1 Page 1.Tiff 和 Sheet 1 Page 2.Tiff。

**生成的图像文件（Sheet 1 Page 1.Tiff）**

![待办事项：图像_替代_文本](converting-worksheet-to-image-and-worksheet-to-image-by-page_2.png)

**生成的图片文件（Sheet 1 Page 2.Tiff）**

![待办事项：图像_替代_文本](converting-worksheet-to-image-and-worksheet-to-image-by-page_3.png)

{{% alert color="primary" %}}

本文介绍如何使用 Aspose.Cells 将工作表转换为图像文件以及将多页工作表转换为多个图像文件（每页一个）。Aspose.Cells 提供比其他组件更大的灵活性，并提供出色的速度、效率和可靠性。结果表明，Aspose.Cells 得益于多年的研究、设计和精心调整。

{{% /alert %}}

## 相关文章

- [将工作表转换为不同的图像格式](/cells/zh/java/converting-worksheet-to-different-image-formats/)
- [将工作表或图表导出为具有所需宽度和高度的图像](/cells/zh/java/export-worksheet-or-chart-into-image-with-desired-width-and-height/)
