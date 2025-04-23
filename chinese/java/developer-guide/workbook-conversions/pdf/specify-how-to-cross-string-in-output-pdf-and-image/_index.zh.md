---
title: 指定输出PDF和图像中如何跨越字符串
type: docs
weight: 110
url: /zh/java/specify-how-to-cross-string-in-output-pdf-and-image/
---

## **可能的使用场景**

当单元格包含文本或字符串但宽度大于单元格宽度时，则如果下一列中的下一个单元格为空或为空，字符串会溢出。将Excel文件保存为PDF/图像时，可以通过指定交叉类型来控制此溢出。它具有以下值

- [**TextCrossType.DEFAULT**](https://reference.aspose.com/cells/java/com.aspose.cells/textcrosstype#DEFAULT)：像MS Excel一样显示，取决于下一个单元格。如果下一个单元格为空，字符串将跨越或被截断。

- [**TextCrossType. CROSS_KEEP**](https://reference.aspose.com/cells/java/com.aspose.cells/textcrosstype#CROSS-KEEP)：像MS Excel一样显示输出PDF/图像中的字符串

- [**TextCrossType.CROSS_OVERRIDE**](https://reference.aspose.com/cells/java/com.aspose.cells/textcrosstype#CROSS-OVERRIDE)：通过跨越其他单元格显示所有文本并覆盖跨越单元格的文本

- [**TextCrossType.STRICT_IN_CELL**](https://reference.aspose.com/cells/java/com.aspose.cells/textcrosstype#STRICT-IN-CELL)：仅显示单元格宽度内的字符串。

## **使用TextCrossType指定输出PDF/图像中如何跨越字符串**

以下示例代码加载示例Excel文件，并通过指定不同的[**TextCrossType**](https://reference.aspose.com/cells/java/com.aspose.cells/TextCrossType)将其保存为PDF/图像格式。可以从以下链接下载示例Excel文件和输出文件：

[sampleCrossType.xlsx](sampleCrossType.xlsx)

[outputCrossType.pdf](outputCrossType.pdf)

[outputCrossType.png](outputCrossType.png)

## **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Rendering-RenderUsingTextCrossType-1.java" >}}
{{< app/cells/assistant language="java" >}}
