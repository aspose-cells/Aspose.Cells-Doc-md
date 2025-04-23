---
title: 在将电子表格呈现为图像时设置默认字体
type: docs
weight: 840
url: /zh/java/set-default-font-while-rendering-spreadsheet-to-images/
---

{{% alert color="primary" %}} 

请使用[ImageOrPrintOptions.DefaultFont](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#DefaultFont)属性将默认字体设置为在将电子表格呈现为图像时使用的字体。当工作簿的默认字体无法呈现您的字符时，此属性将生效。使用[ImageOrPrintOptions.DefaultFont](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#DefaultFont)属性指定的默认字体用于所有那些具有无效或不存在字体的单元格。

{{% /alert %}} 
## **在将电子表格呈现为图像时设置默认字体**
以下示例代码创建一个工作簿，在第一个工作表的单元格A4中添加一些文本，并将其字体设置为无效或不存在的字体。然后，它获取工作表的两个图像。第一个图像是通过将[ImageOrPrintOptions.DefaultFont](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#DefaultFont)属性设置为*Courier New*获得的，第二个图像是通过将[ImageOrPrintOptions.DefaultFont](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#DefaultFont)属性设置为*Times New Roman*获得的。

将[ImageOrPrintOptions.DefaultFont](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#DefaultFont)属性设置为*Courier New*后的输出图像。

![todo:image_alt_text](set-default-font-while-rendering-spreadsheet-to-images_1.png)

在将 [ImageOrPrintOptions.DefaultFont](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#DefaultFont) 属性设置为 *Times New Roman* 后，这是输出图像。

![todo:image_alt_text](set-default-font-while-rendering-spreadsheet-to-images_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-files-utility-SetDefaultFontWhileRenderingSpreadsheetToImages-.java" >}}
{{< app/cells/assistant language="java" >}}
