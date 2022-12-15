---
title: 将电子表格渲染为图像时设置默认字体
type: docs
weight: 840
url: /zh/java/set-default-font-while-rendering-spreadsheet-to-images/
---
{{% alert color="primary" %}} 

请使用[ImageOrPrintOptions.DefaultFont](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#DefaultFont)在将电子表格呈现为图像时设置默认字体的属性。此属性仅在工作簿的默认字体无法呈现您的字符时才有效。指定的默认字体[ImageOrPrintOptions.DefaultFont](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#DefaultFont)属性用于所有具有无效或不存在字体的单元格。

{{% /alert %}} 
## **将电子表格渲染为图像时设置默认字体**
以下示例代码创建一个工作簿，在第一个工作表的单元格 A4 中添加一些文本并将其字体设置为无效或不存在的字体。然后，它拍摄工作表的两张图像。第一张图片是通过设置[ImageOrPrintOptions.DefaultFont](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#DefaultFont)财产给*快递新*第二张图片是通过设置[ImageOrPrintOptions.DefaultFont](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#DefaultFont)财产给*英语字体格式一种*.

这是设置后的输出图像[ImageOrPrintOptions.DefaultFont](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#DefaultFont)财产给*快递新*.

![待办事项：图像_替代_文本](set-default-font-while-rendering-spreadsheet-to-images_1.png)

这是设置后的输出图像[ImageOrPrintOptions.DefaultFont](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#DefaultFont)财产给*英语字体格式一种*.

![待办事项：图像_替代_文本](set-default-font-while-rendering-spreadsheet-to-images_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-files-utility-SetDefaultFontWhileRenderingSpreadsheetToImages-.java" >}}
