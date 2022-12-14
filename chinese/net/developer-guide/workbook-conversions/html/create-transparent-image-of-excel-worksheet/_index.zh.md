---
title: 创建 Excel 工作表的透明图像
type: docs
weight: 170
url: /zh/net/create-transparent-image-of-excel-worksheet/
---
{{% alert color="primary" %}}

有时，您需要将工作表的图像生成为透明图像。您想要对所有没有填充颜色的单元格应用透明度。 Aspose.Cells 提供了[**ImageOrPrintOptions.透明**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/transparent)属性将透明度应用于工作表图像。当这个属性是**错误的** 然后没有填充颜色的单元格用白色绘制，当它是**真的**没有填充颜色的单元格被绘制成透明的。

{{% /alert %}} 

在下面的工作表图像中，没有应用透明度。没有填充颜色的单元格被绘制成白色。

|**不透明的输出：单元格背景为白色**|
|:- |
|![待办事项：图片_替代_文本](create-transparent-image-of-excel-worksheet_1.png)|

同时，在下面的工作表图像中，应用了透明度。没有填充颜色的单元格是透明的。

|**启用透明度的输出**|
|:- |
|![待办事项：图片_替代_文本](create-transparent-image-of-excel-worksheet_2.png)|

以下示例代码从 Excel 工作表生成透明图像。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CreateTransparentImage-1.cs" >}}
