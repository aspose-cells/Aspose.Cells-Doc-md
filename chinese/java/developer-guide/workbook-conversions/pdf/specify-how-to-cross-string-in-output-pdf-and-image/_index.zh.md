---
title: 指定如何在输出 PDF 和图像中交叉字符串
type: docs
weight: 110
url: /zh/java/specify-how-to-cross-string-in-output-pdf-and-image/
---
## **可能的使用场景**

当单元格包含文本或字符串但大于单元格的宽度时，如果下一列中的下一个单元格为 null 或为空，则字符串会溢出。当您将 Excel 文件保存为 PDF/Image 时，您可以通过使用[**文本交叉类型**](https://reference.aspose.com/cells/java/com.aspose.cells/TextCrossType)枚举。它具有以下值

- [**TextCrossType.DEFAULT**](https://reference.aspose.com/cells/java/com.aspose.cells/textcrosstype#DEFAULT): 显示类似 MS Excel，取决于下一个单元格。如果下一个单元格为空，则字符串将交叉或被截断。

- [**文本交叉类型。交叉保持**](https://reference.aspose.com/cells/java/com.aspose.cells/textcrosstype#CROSS_KEEP)显示字符串，如 MS Excel 导出 PDF/图像

- [**TextCrossType.CROSS_OVERRIDE**](https://reference.aspose.com/cells/java/com.aspose.cells/textcrosstype#CROSS_OVERRIDE): 通过交叉其他单元格显示所有文本并覆盖交叉单元格的文本

- [**TextCrossType.STRICT_IN_CELL**](https://reference.aspose.com/cells/java/com.aspose.cells/textcrosstype#STRICT_IN_CELL)：只显示单元格宽度内的字符串。

## **使用 TextCrossType 指定如何在输出 PDF/图像中交叉字符串**

以下示例代码加载示例 Excel 文件并通过指定不同的格式将其保存为 PDF/图像格式[**文本交叉类型**](https://reference.aspose.com/cells/java/com.aspose.cells/TextCrossType).示例 Excel 文件和输出文件可从以下链接下载：

[样例交叉类型.xlsx](sampleCrossType.xlsx)

[outputCrossType.pdf](outputCrossType.pdf)

[outputCrossType.png](outputCrossType.png)

## **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Rendering-RenderUsingTextCrossType-1.java" >}}
