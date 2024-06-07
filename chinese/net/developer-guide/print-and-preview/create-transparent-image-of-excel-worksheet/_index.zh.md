---
title: 创建Excel工作表的透明图像
type: docs
weight: 170
url: /zh/net/create-transparent-image-of-excel-worksheet/
---

{{% alert color="primary" %}}

有时，您需要将工作表的图像生成为透明图像。您希望将透明度应用于所有没有填充颜色的单元格。Aspose.Cells提供[**ImageOrPrintOptions.Transparent**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/transparent)属性来将透明度应用于工作表图像。当此属性为**false**时，没有填充颜色的单元格将以白色绘制，当为**true**时，没有填充颜色的单元格将被绘制为透明。

{{% /alert %}} 

在以下工作表图像中，未应用透明度。没有填充颜色的单元格为白色。

|**没有透明度的输出：单元格背景为白色**|
| :- |
|![todo:image_alt_text](create-transparent-image-of-excel-worksheet_1.png)|

而在以下工作表图像中，已应用透明度。没有填充颜色的单元格为透明。

|**启用透明度的输出**|
| :- |
|![todo:image_alt_text](create-transparent-image-of-excel-worksheet_2.png)|

以下示例代码从Excel工作表生成透明图像。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CreateTransparentImage-1.cs" >}}
