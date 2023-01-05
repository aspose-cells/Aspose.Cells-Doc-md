---
title: 指定如何在输出 PDF 和图像中交叉字符串
type: docs
weight: 20
url: /zh/python-java/specify-how-to-cross-string-in-output-pdf-and-image/
---
## **指定如何在输出 PDF 和图像中交叉字符串**
当单元格包含大于单元格宽度的文本或字符串时，如果下一列中的下一个单元格为 null 或为空，则字符串会溢出。当您将 Excel 文件保存到 PDF/Image 时，您可以通过使用[文本交叉类型](https://reference.aspose.com/cells/python/asposecells.api/TextCrossType)枚举。它具有以下值

- [TextCrossType.DEFAULT](https://reference.aspose.com/cells/python/asposecells.api/textcrosstype#DEFAULT): 显示类似 MS Excel，取决于下一个单元格。如果下一个单元格为空，则字符串将交叉或被截断。
- [文本交叉类型。交叉保持](https://reference.aspose.com/cells/python/asposecells.api/textcrosstype#CROSS_KEEP)显示类似于MS Excel exporting PDF/Image的字符串
- [TextCrossType.CROSS_OVERRIDE](https://reference.aspose.com/cells/python/asposecells.api/textcrosstype#CROSS_OVERRIDE)跨过其他单元格显示所有文本，并覆盖跨过单元格的文本
- [文本交叉类型.STRICT_在_细胞](https://reference.aspose.com/cells/python/asposecells.api/textcrosstype#STRICT_IN_CELL)：只显示单元格宽度内的字符串。

以下示例代码加载示例 Excel 文件并通过指定不同的 TextCrossType 将其保存为 PDF/Image 格式。示例 Excel 文件和输出文件可从以下链接下载：

[样例交叉类型.xlsx](sampleCrossType.xlsx)

[outputCrossType.pdf](outputCrossType.pdf)

[outputCrossType.png](outputCrossType.png)
## **示例代码**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Rendering-RenderUsingTextCrossType.py" >}}
