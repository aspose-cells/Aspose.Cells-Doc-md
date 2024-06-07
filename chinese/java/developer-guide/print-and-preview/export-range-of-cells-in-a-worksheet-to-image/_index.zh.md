---
title: 将工作表中的一系列单元格导出为图像
type: docs
weight: 130
url: /zh/java/export-range-of-cells-in-a-worksheet-to-image/
---

{{% alert color="primary" %}}

您可以使用Aspose.Cells制作工作表的图像。但是，有时您需要仅将工作表中的一系列单元格导出为图像。本文介绍了如何实现这一点。

{{% /alert %}}

要拍摄范围的图像，请将打印区域设置为所需的范围，然后将所有边距设置为0。还需将[**ImageOrPrintOptions.setOnePagePerSheet()**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#OnePagePerSheet)设置为**true**。

以下代码将获取E8:H10范围的图像。下面是代码中使用的源工作簿的屏幕截图。您可以在任何工作簿中尝试此代码。

**输入文件**

![todo:image_alt_text](export-range-of-cells-in-a-worksheet-to-image_1.png)

执行代码会创建一个仅包含E8:H10范围的图像。

**输出图像**

![todo:image_alt_text](export-range-of-cells-in-a-worksheet-to-image_2.jpg)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-ExportRangeofCells-1.java" >}}

您还可以在文章[将工作表转换为不同的图像格式](/cells/zh/java/converting-worksheet-to-different-image-formats/)中找到有用的信息。
