---
title: Create Transparent Image of Excel Worksheet
type: docs
weight: 170
url: /zh/python-net/create-transparent-image-of-excel-worksheet/
---

{{% alert color="primary" %}}

有时，你需要生成具有透明背景的工作表图像。你想对没有填充颜色的所有单元格应用透明度。Aspose.Cells for Python via .NET 提供 [**ImageOrPrintOptions.transparent**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/transparent) 属性来应用工作表图像的透明度。当此属性为 **false** 时，无填充色的单元格将用白色绘制；当为 **true** 时，无填充色的单元格将是透明的。

{{% /alert %}} 

在下面的工作表图片中，没有应用透明度。没有填充颜色的单元格绘制成了白色。

|**没有透明度的输出：单元格背景为白色**|
| :- |
|![todo:image_alt_text](create-transparent-image-of-excel-worksheet_1.png)|

而在下面的工作表图片中，应用了透明度。没有填充颜色的单元格是透明的。

|**启用透明度输出**|
| :- |
|![todo:image_alt_text](create-transparent-image-of-excel-worksheet_2.png)|

下面的示例代码从 Excel 工作表生成一个透明的图像。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-CreateTransparentImage-1.py" >}}

