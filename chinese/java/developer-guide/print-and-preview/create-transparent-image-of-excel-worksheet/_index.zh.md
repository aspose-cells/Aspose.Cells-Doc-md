---
title: 创建 Excel 工作表的透明图像
type: docs
weight: 80
url: /zh/java/create-transparent-image-of-excel-worksheet/
---
{{% alert color="primary" %}}

有时，您需要将工作表的图像生成为透明图像。您想要对所有没有填充颜色的单元格应用透明度。 Aspose.Cells 提供了[**ImageOrPrintOptions.setTransparent()**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#Transparent)将透明度应用于工作表图像的属性。当这个属性是**错误的** 然后没有填充颜色的单元格用白色绘制，当它是**真的**没有填充颜色的单元格被绘制成透明的。

{{% /alert %}}

在下面的工作表图像中，没有应用透明度。没有填充颜色的单元格被绘制成白色。

**未应用透明度的工作表图像**

![待办事项：图像_替代_文本](create-transparent-image-of-excel-worksheet_1.png)

同时，在下面的工作表图像中，应用了透明度。没有填充颜色的单元格是透明的。

**应用透明度后的工作表图像**

![待办事项：图像_替代_文本](create-transparent-image-of-excel-worksheet_2.png)

您可以使用以下示例代码生成 Excel 工作表的透明图像。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-CreateTransparentImage-1.java" >}}
