---
title: 指定输出PDF和图像中如何跨越字符串
type: docs
weight: 20
url: /zh/python-java/specify-how-to-cross-string-in-output-pdf-and-image/
---

## **指定如何在输出PDF和图像中跨越字符串**
当单元格中的文本或字符串大于单元格的宽度时，如果下一列中的下一个单元格是null或空，则字符串会溢出。当将Excel文件保存为PDF/Image时，您可以通过使用TextCrossType枚举来指定交叉类型来控制此溢出。它具有以下值

- TextCrossType.DEFAULT：类似于MS Excel的显示，取决于下一个单元格。如果下一个单元格为null，则字符串将交叉或被截断。
- TextCrossType.CROSS_KEEP：与MS Excel导出PDF/Image类似显示字符串
- TextCrossType.CROSS_OVERRIDE：通过交叉其他单元格并覆盖所交叉单元格的文本显示所有文本
- TextCrossType.STRICT_IN_CELL：仅在单元格宽度内显示字符串

以下示例代码加载了示例Excel文件，并通过指定不同的TextCrossType将其保存为PDF/Image格式。可以从以下链接下载示例Excel文件和输出文件:

[sampleCrossType.xlsx](sampleCrossType.xlsx)

[outputCrossType.pdf](outputCrossType.pdf)

[outputCrossType.png](outputCrossType.png)
## **示例代码**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Rendering-RenderUsingTextCrossType.py" >}}
