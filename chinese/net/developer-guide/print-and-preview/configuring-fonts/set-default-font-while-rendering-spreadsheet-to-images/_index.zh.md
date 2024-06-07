---
title: 在将电子表格渲染为图像时设置默认字体
type: docs
weight: 360
url: /zh/net/set-default-font-while-rendering-spreadsheet-to-images/
---

{{% alert color="primary" %}}

请使用 [**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/defaultfont) 属性来设置在将电子表格渲染为图像时的默认字体。当工作簿的默认字体无法呈现您的字符时，此属性将发挥作用。使用 [**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/defaultfont) 属性指定的默认字体适用于那些具有无效或不存在字体的单元格。

{{% /alert %}}

## 在将电子表格渲染为图像时设置默认字体

以下示例代码创建一个工作簿，在第一个工作表的 A4 单元格中添加一些文本，并将其字体设置为无效或不存在的字体。然后，它通过将 [**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/defaultfont) 属性设置为 *Courier New* 来捕获工作表的两个图像。第一张图像是通过将 [**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/defaultfont) 属性设置为 *Courier New* 获取的，第二张图像是通过将 [**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/defaultfont) 属性设置为 *Times New Roman* 获取的。

在将 [**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/defaultfont) 属性设置为 *Courier New* 后的输出图像。

![todo:image_alt_text](set-default-font-while-rendering-spreadsheet-to-images_1.png)

在将 [**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/defaultfont) 属性设置为 *Times New Roman* 后的输出图像。

![todo:image_alt_text](set-default-font-while-rendering-spreadsheet-to-images_2.png)

## 示例代码

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-SetDefaultFontWhileRenderingSpreadsheet-1.cs" >}}
