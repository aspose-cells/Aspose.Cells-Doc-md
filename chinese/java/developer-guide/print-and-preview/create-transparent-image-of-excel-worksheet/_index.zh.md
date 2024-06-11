---
title: Create Transparent Image of Excel Worksheet
type: docs
weight: 80
url: /zh/java/create-transparent-image-of-excel-worksheet/
---

{{% alert color="primary" %}}

有时，您需要将自己的工作表的图像生成为透明图像。您希望将透明度应用于所有空白填充颜色的单元格。Aspose.Cells提供了[**ImageOrPrintOptions.setTransparent()**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#Transparent)属性来应用透明度到工作表图像。当该属性为**false**时，没有填充颜色的单元格将以白色绘制，当该属性为**true**时，没有填充颜色的单元格将透明绘制。

{{% /alert %}}

In the following worksheet image, transparency has not been applied. The cells with no fill colors are drawn white.

**未应用透明度的工作表图像**

![todo:image_alt_text](create-transparent-image-of-excel-worksheet_1.png)

While, in the following worksheet image, transparency has been applied. The cells with no fill colors are transparent.

**应用透明度后的工作表图像**

![todo:image_alt_text](create-transparent-image-of-excel-worksheet_2.png)

您可以使用以下示例代码生成Excel工作表的透明图像。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-CreateTransparentImage-1.java" >}}
