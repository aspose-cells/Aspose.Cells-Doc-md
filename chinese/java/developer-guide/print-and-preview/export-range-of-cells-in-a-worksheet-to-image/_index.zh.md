---
title: 将工作表中的 Cells 范围导出到图像
type: docs
weight: 130
url: /zh/java/export-range-of-cells-in-a-worksheet-to-image/
---
{{% alert color="primary" %}}

您可以使用 Aspose.Cells 制作工作表的图像。但是，有时您只需要将工作表中的一系列单元格导出到图像。本文解释了如何实现这一点。

{{% /alert %}}

要拍摄某个范围的图像，请将打印区域设置为所需范围，然后将所有边距设置为 0。同时设置[**ImageOrPrintOptions.setOnePagePerSheet() 方法**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#OnePagePerSheet)到**真的**.

以下代码获取范围 E8:H10 的图像。下面是代码中使用的源工作簿的屏幕截图。您可以使用任何工作簿试用代码。

**输入文件**

![待办事项：图片_替代_文本](export-range-of-cells-in-a-worksheet-to-image_1.png)

执行代码仅创建 E8:H10 范围的图像。

**输出图像**

![待办事项：图片_替代_文本](export-range-of-cells-in-a-worksheet-to-image_2.jpg)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-ExportRangeofCells-1.java" >}}

您还可以找到这篇文章[将工作表转换为不同的图像格式](/cells/zh/java/converting-worksheet-to-different-image-formats/)有帮助。
