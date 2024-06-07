---
title: 创建Excel工作表的透明图像
type: docs
weight: 80
url: /zh/java/create-transparent-image-of-excel-worksheet/
---

{{% alert color="primary" %}}

有时，您需要将工作表生成为透明图像。您希望将透明度应用于所有未填充颜色的单元格。Aspose.Cells提供了[**ImageOrPrintOptions.setTransparent()**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#Transparent)属性来应用透明度到工作表图像。当该属性为**false**时，没有填充颜色的单元格将以白色填充，而当其为**true**时，没有填充颜色的单元格将为透明。

{{% /alert %}}

在以下工作表图像中，未应用透明度。没有填充颜色的单元格为白色。

**未应用透明度的工作表图像**

![todo:image_alt_text](create-transparent-image-of-excel-worksheet_1.png)

而在以下工作表图像中，已应用透明度。没有填充颜色的单元格为透明。

**应用透明度后的工作表图像**

![todo:image_alt_text](create-transparent-image-of-excel-worksheet_2.png)

您可以使用以下示例代码生成Excel工作表的透明图像。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-CreateTransparentImage-1.java" >}}
