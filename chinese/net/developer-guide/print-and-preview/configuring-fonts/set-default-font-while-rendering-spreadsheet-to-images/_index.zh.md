---
title: 在将电子表格呈现为图像时设置默认字体
type: docs
weight: 360
url: /zh/net/set-default-font-while-rendering-spreadsheet-to-images/
---

{{% alert color="primary" %}}

请使用[**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/defaultfont)属性将默认字体设置为渲染电子表格为图像时的默认字体。仅当工作簿的默认字体无法呈现您的字符时，才会使用[**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/defaultfont)属性指定的默认字体。指定的默认字体将用于所有缺少或不存在的字体的单元格。

{{% /alert %}}

## 渲染电子表格为图像时设置默认字体

下面的示例代码创建一个工作簿，在第一个工作表的A4单元格中添加一些文本，并将其字体设置为无效或不存在的字体。然后，它会获取工作表的两个图像。第一张图片是通过将[**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/defaultfont)属性设置为Courier New获取的，第二张图片是通过将[**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/defaultfont)属性设置为Times New Roman获取的。

将[**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/defaultfont)属性设置为Courier New后的输出图像。

![todo:image_alt_text](set-default-font-while-rendering-spreadsheet-to-images_1.png)

将[**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/defaultfont)属性设置为Times New Roman后的输出图像。

![todo:image_alt_text](set-default-font-while-rendering-spreadsheet-to-images_2.png)

## 示例代码

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-SetDefaultFontWhileRenderingSpreadsheet-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
