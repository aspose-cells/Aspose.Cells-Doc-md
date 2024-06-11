---
title: 指定输出PDF和图像中如何跨越字符串
type: docs
weight: 20
url: /zh/python-java/specify-how-to-cross-string-in-output-pdf-and-image/
---

## **指定如何在输出PDF和图像中跨越字符串**
当单元格中包含的文本或字符串的宽度大于单元格的宽度时，如果下一列中的单元格为空，则字符串会溢出。当您将Excel文件保存为PDF /图像时，您可以通过指定[TextCrossType](https://reference.aspose.com/cells/python/asposecells.api/TextCrossType)枚举来控制此溢出。它具有以下值。

- [TextCrossType.DEFAULT](https://reference.aspose.com/cells/python/asposecells.api/textcrosstype#DEFAULT)：显示为MS Excel，取决于下一个单元格。如果下一个单元格为空，字符串将会跨越或被截断。
- [TextCrossType. CROSS_KEEP](https://reference.aspose.com/cells/python/asposecells.api/textcrosstype#CROSS_KEEP)：显示与MS Excel类似的字符串，导出PDF /图像。
- [TextCrossType.CROSS_OVERRIDE](https://reference.aspose.com/cells/python/asposecells.api/textcrosstype#CROSS_OVERRIDE) ：显示所有文本，跨越其他单元格并覆盖交叉单元格的文本
- [TextCrossType.STRICT_IN_CELL](https://reference.aspose.com/cells/python/asposecells.api/textcrosstype#STRICT_IN_CELL) ：仅在单元格宽度内显示字符串。

以下样例代码加载样本Excel文件，并通过指定不同的TextCrossType将其保存为PDF/Image格式。可以从以下链接下载样本Excel文件和输出文件：

[sampleCrossType.xlsx](sampleCrossType.xlsx)

[outputCrossType.pdf](outputCrossType.pdf)

[outputCrossType.png](outputCrossType.png)
## **示例代码**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Rendering-RenderUsingTextCrossType.py" >}}
