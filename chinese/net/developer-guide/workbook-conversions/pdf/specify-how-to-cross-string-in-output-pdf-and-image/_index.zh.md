---
title: 指定输出PDF和图像中如何跨越字符串
type: docs
weight: 120
url: /zh/net/specify-how-to-cross-string-in-output-pdf-and-image/
---

## **可能的使用场景**

当单元格包含文本或字符串但超过了单元格的宽度时，如果下一列中的单元格为null或空，则字符串会溢出。当将Excel文件保存为PDF/Image时，您可以通过指定交叉类型来控制此溢出，该枚举具有以下值

- **TextCrossType.Default**：像MS Excel一样显示文本，依赖于下一个单元格。如果下一个单元格为空，字符串将会跨越或被截断。

- **TextCrossType.CrossKeep**：像MS Excel导出PDF/Image一样显示字符串

- **TextCrossType.CrossOverride**：通过跨越其他单元格并覆盖已跨越单元格的文本来显示所有文本

- **TextCrossType.StrictInCell**：仅在单元格宽度内显示字符串。

## **使用TextCrossType指定输出PDF/Image中的字符串如何跨越**

下面的示例代码加载示例Excel文件，并通过指定不同的[**TextCrossType**](https://reference.aspose.com/cells/net/aspose.cells/textcrosstype)将其保存为PDF/Image格式。示例Excel文件和输出文件可从以下链接下载：

[sampleCrossType.xlsx](81920905.xlsx)

[outputCrossType.pdf](81920903.pdf)

[outputCrossType.png](81920904.png)

###示例代码

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Rendering-RenderUsingTextCrossType-1.cs" >}}
