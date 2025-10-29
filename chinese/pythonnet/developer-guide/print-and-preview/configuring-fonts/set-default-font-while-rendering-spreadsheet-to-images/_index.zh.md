---
title: 在将电子表格呈现为图像时设置默认字体
type: docs
weight: 360
url: /zh/python-net/set-default-font-while-rendering-spreadsheet-to-images/
---

{{% alert color="primary" %}}

请使用[**ImageOrPrintOptions.default_font**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/default_font)属性将默认字体设置为渲染电子表格为图像时的默认字体。仅当工作簿的默认字体无法呈现您的字符时，才会使用[**ImageOrPrintOptions.default_font**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/default_font)属性指定的默认字体。指定的默认字体将用于所有缺少或不存在的字体的单元格。

{{% /alert %}}

## 渲染电子表格为图像时设置默认字体

下面的示例代码创建一个工作簿，在第一个工作表的A4单元格中添加一些文本，并将其字体设置为无效或不存在的字体。然后，它会获取工作表的两个图像。第一张图片是通过将[**ImageOrPrintOptions.default_font**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/default_font)属性设置为Courier New获取的，第二张图片是通过将[**ImageOrPrintOptions.default_font**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/default_font)属性设置为Times New Roman获取的。

将[**ImageOrPrintOptions.default_font**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/default_font)属性设置为Courier New后的输出图像。

![todo:image_alt_text](1.png)

将[**ImageOrPrintOptions.default_font**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/default_font)属性设置为Times New Roman后的输出图像。

![todo:image_alt_text](2.png)

## 示例代码

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-SetDefaultFontWhileRenderingSpreadsheet-1.cs" >}}

{{< app/cells/assistant language="python-net" >}}
