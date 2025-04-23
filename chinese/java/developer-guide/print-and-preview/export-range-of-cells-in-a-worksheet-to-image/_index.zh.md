---
title: 导出工作表中的单元格范围为图像
type: docs
weight: 130
url: /zh/java/export-range-of-cells-in-a-worksheet-to-image/
---

{{% alert color="primary" %}}

您可以使用 Aspose.Cells 制作工作表的图像。但是，有时您只需将工作表中的一定范围的单元格导出为图像。本文解释了如何实现这一点。

{{% /alert %}}

要获取范围的图像，请将打印区域设置为所需的范围，然后将所有页面边距设置为0。还应设置[**ImageOrPrintOptions.setOnePagePerSheet()**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#OnePagePerSheet)为**true**。

以下代码获取了范围E8:H10的图像。下面是代码中使用的源工作簿的屏幕截图。您可以尝试任何工作簿中的代码。

输入文件

![todo:image_alt_text](export-range-of-cells-in-a-worksheet-to-image_1.png)

执行此代码会创建只包含范围E8:H10的图像。

**输出图像**

![todo:image_alt_text](export-range-of-cells-in-a-worksheet-to-image_2.jpg)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-ExportRangeofCells-1.java" >}}

您可能还会发现文章[将工作表转换为不同的图像格式](/cells/zh/java/converting-worksheet-to-different-image-formats/)有用。
{{< app/cells/assistant language="java" >}}
