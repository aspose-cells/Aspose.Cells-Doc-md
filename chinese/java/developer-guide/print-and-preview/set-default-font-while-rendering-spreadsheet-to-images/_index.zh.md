---
title: 在将电子表格渲染为图像时设置默认字体
type: docs
weight: 840
url: /zh/java/set-default-font-while-rendering-spreadsheet-to-images/
---

{{% alert color="primary" %}} 

请使用[ImageOrPrintOptions.DefaultFont](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#DefaultFont)属性设置渲染电子表格为图像时的默认字体。当工作簿的默认字体无法呈现您的字符时，此属性将有效。使用[ImageOrPrintOptions.DefaultFont](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#DefaultFont)属性指定的默认字体用于那些具有无效或不存在字体的单元格。

{{% /alert %}} 
## **在将电子表格渲染为图像时设置默认字体**
以下示例代码创建一个工作簿，在第一个工作表的A4单元格中添加一些文本并将其字体设置为无效或不存在字体。然后，它会对工作表进行两次图像处理。第一张图像是通过将[ImageOrPrintOptions.DefaultFont](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#DefaultFont)属性设置为*Courier New*来获取的，第二张图像是通过将[ImageOrPrintOptions.DefaultFont](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#DefaultFont)属性设置为*Times New Roman*来获取的。

将[ImageOrPrintOptions.DefaultFont](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#DefaultFont)属性设置为*Courier New*后的输出图像。

![todo:image_alt_text](set-default-font-while-rendering-spreadsheet-to-images_1.png)

将[ImageOrPrintOptions.DefaultFont](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#DefaultFont)属性设置为*Times New Roman*后的输出图像。

![todo:image_alt_text](set-default-font-while-rendering-spreadsheet-to-images_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-files-utility-SetDefaultFontWhileRenderingSpreadsheetToImages-.java" >}}
