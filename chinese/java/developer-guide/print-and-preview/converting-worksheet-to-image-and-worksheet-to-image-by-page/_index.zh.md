---
title: 将工作表转换为图像和按页将工作表转换为图像
type: docs
weight: 210
url: /zh/java/converting-worksheet-to-image-and-worksheet-to-image-by-page/
---

{{% alert color="primary" %}}

本文档旨在为开发人员提供详细了解如何将工作表转换为图像文件和将多个页的工作表转换为单张图片文件的信息。

有时，您可能需要将工作表呈现为图像，例如在应用程序或网页中使用。您可能需要将图像插入到Word文档、PDF文件、PowerPoint演示文稿中，或者在其他一些场景中使用。简单地说，您想要将工作表呈现为图像。Aspose.Cells API支持将Microsoft Excel文件中的工作表转换为图像。Aspose.Cells还支持将工作簿转换为多个图像文件，每页一个。

{{% /alert %}}

## **使用Aspose.Cells将工作表转换为图像文件**

本文介绍了如何使用Aspose.Cells for Java API将工作表转换为图像。API提供了一些有价值的类，如[**SheetRender**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetRender)、[**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions)、[**WorkbookRender**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookRender)等。[**SheetRender**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetRender)类表示要为工作表呈现图像，并且有一个重载的[**toImage**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender#toImage(int,%20java.io.OutputStream)方法，可以直接将工作表转换为图像文件并设置任何属性或选项。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-ConvertWorksheettoImageFile-1.java" >}}

### **结果**

执行上述代码后，名为Sheet1的工作表将被转换为图像文件SheetImage.jpg。

**输出JPG**

![todo:image_alt_text](converting-worksheet-to-image-and-worksheet-to-image-by-page_1.png)

## **使用 Aspose.Cells 将工作表按页转换为图片文件**

本示例展示如何使用 Aspose.Cells 将模板工作簿中有多页的工作表转换为一个图片文件。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-ConvertWorksheetToImageByPage-1.java" >}}

### **结果**

执行上述代码后，名为Sheet1的工作表将被转换为两个图像文件（每页一个）Sheet 1 Page 1.Tiff和Sheet 1 Page 2.Tiff。

**生成的图像文件（Sheet 1 Page 1.Tiff）**

![todo:image_alt_text](converting-worksheet-to-image-and-worksheet-to-image-by-page_2.png)

**生成的图像文件（Sheet 1 Page 2.Tiff）**

![todo:image_alt_text](converting-worksheet-to-image-and-worksheet-to-image-by-page_3.png)

{{% alert color="primary" %}}

本文介绍了如何使用Aspose.Cells将工作表转换为图像文件，以及如何使用Aspose.Cells将具有多个页面的工作表转换为多个图像文件（每页一个）。Aspose.Cells比其他组件提供更灵活的选择，并提供出色的速度、效率和可靠性。结果显示，Aspose.Cells经过多年的研究、设计和精心调整。

{{% /alert %}}

## 相关文章

- [将工作表转换为不同的图像格式](/cells/zh/java/converting-worksheet-to-different-image-formats/)
- [使用所需宽度和高度将工作表或图表导出为图像](/cells/zh/java/export-worksheet-or-chart-into-image-with-desired-width-and-height/)
