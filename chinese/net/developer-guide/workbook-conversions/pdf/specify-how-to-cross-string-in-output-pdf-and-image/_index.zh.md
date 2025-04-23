---
title: 指定输出PDF和图像中如何跨越字符串
type: docs
weight: 120
url: /zh/net/specify-how-to-cross-string-in-output-pdf-and-image/
---

## **可能的使用场景**

当单元格包含文本或字符串但大于单元格宽度时，如果下一列的单元格为空，则字符串会溢出。当您将Excel文件保存为PDF / 图像时，您可以通过使用[**TextCrossType**](https://reference.aspose.com/cells/net/aspose.cells/textcrosstype)枚举指定交叉类型来控制此溢出。它具有以下值

- **TextCrossType.Default**: 显示与MS Excel类似的文本，具体取决于下一个单元格。 如果下一个单元格为空，则字符串将交叉或被截断。

- **TextCrossType.CrossKeep**: 显示与MS Excel导出PDF/Image类似的字符串。

- **TextCrossType.CrossOverride**: 显示所有文本，通过跨越其他单元格，并覆盖经过交叉处理的单元格上的文本

- **TextCrossType.StrictInCell**: 仅在单元格宽度内显示字符串。

## **使用TextCrossType指定输出PDF/图像中如何跨越字符串**

以下示例代码加载示例Excel文件，并通过指定不同的[**TextCrossType**](https://reference.aspose.com/cells/net/aspose.cells/textcrosstype)将其保存为PDF/图像格式。可以从以下链接下载示例Excel文件和输出文件：

[sampleCrossType.xlsx](81920905.xlsx)

[outputCrossType.pdf](81920903.pdf)

[outputCrossType.png](81920904.png)

### 示例代码

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Rendering-RenderUsingTextCrossType-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
