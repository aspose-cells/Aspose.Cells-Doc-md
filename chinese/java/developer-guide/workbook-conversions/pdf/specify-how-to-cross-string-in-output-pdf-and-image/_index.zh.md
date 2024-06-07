---
title: 指定输出PDF和图像中如何跨越字符串
type: docs
weight: 110
url: /zh/java/specify-how-to-cross-string-in-output-pdf-and-image/
---

## **可能的使用场景**

当单元格包含文本或字符串，但宽度大于单元格宽度时，如果下一列中的单元格为空，则字符串会溢出。在将Excel文件保存为PDF/Image时，您可以通过指定交叉类型使用 [**TextCrossType**](https://reference.aspose.com/cells/java/com.aspose.cells/TextCrossType) 枚举来控制此溢出。它具有以下值

- [**TextCrossType.DEFAULT**](https://reference.aspose.com/cells/java/com.aspose.cells/textcrosstype#DEFAULT)：显示类似于MS Excel，取决于下一个单元格。如果下一个单元格为空，字符串将跨越或被截断。

- [**TextCrossType. CROSS_KEEP**](https://reference.aspose.com/cells/java/com.aspose.cells/textcrosstype#CROSS_KEEP)：类似于MS Excel导出PDF/Image的显示字符串

- [**TextCrossType.CROSS_OVERRIDE**](https://reference.aspose.com/cells/java/com.aspose.cells/textcrosstype#CROSS_OVERRIDE)：通过穿越其他单元格显示所有文本并覆盖穿越单元格的文本

- [**TextCrossType.STRICT_IN_CELL**](https://reference.aspose.com/cells/java/com.aspose.cells/textcrosstype#STRICT_IN_CELL)：仅在单元格宽度内显示字符串。

## **使用TextCrossType指定输出PDF/Image中的字符串如何跨越**

下面的示例代码加载示例Excel文件，并通过指定不同的[**TextCrossType**](https://reference.aspose.com/cells/java/com.aspose.cells/TextCrossType)将其保存为PDF/Image格式。示例Excel文件和输出文件可从以下链接下载：

[sampleCrossType.xlsx](sampleCrossType.xlsx)

[outputCrossType.pdf](outputCrossType.pdf)

[outputCrossType.png](outputCrossType.png)

## **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Rendering-RenderUsingTextCrossType-1.java" >}}
