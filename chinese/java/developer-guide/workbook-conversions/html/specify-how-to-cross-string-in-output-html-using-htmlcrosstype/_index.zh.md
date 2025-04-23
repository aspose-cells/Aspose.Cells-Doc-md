---
title: 使用HtmlCrossType指定输出HTML中如何交叉字符串
type: docs
weight: 140
url: /zh/java/specify-how-to-cross-string-in-output-html-using-htmlcrosstype/
---

## **可能的使用场景**

当单元格包含文本或字符串，但大于单元格的宽度时，如果下一列中的下一个单元格为空或为空，则字符串会溢出。当将Excel文件保存为HTML时，您可以通过使用[**HtmlCrossType**](https://reference.aspose.com/cells/java/com.aspose.cells/HtmlCrossType)枚举来控制这种溢出。它具有以下值

- [**HtmlCrossType.DEFAULT**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#DEFAULT)：显示类似于MS Excel，取决于下一个单元格。如果下一个单元格为空，则字符串将交叉或被截断。

- [**HtmlCrossType.MS_EXPORT**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#MS-EXPORT)：显示与MS Excel导出HTML相同的字符串。

- [**HtmlCrossType.CROSS**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#CROSS)：显示HTML交叉字符串，为创建大型HTML文件的性能要比设置值为[**DEFAULT**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#DEFAULT)或[**FIT_TO_CELL**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#FIT-TO-CELL)快十倍。

- [**HtmlCrossType.CROSS_HIDE_RIGHT**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#CROSS-HIDE-RIGHT)：显示HTML交叉字符串并在文本重叠时隐藏右侧的字符串。

- [**HtmlCrossType.FIT_TO_CELL**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#FIT-TO-CELL)：仅显示单元格宽度内的字符串。

## **使用HtmlCrossType指定输出HTML中如何交叉字符串**

以下示例代码加载了[示例Excel文件](51740747.xlsx)，并通过指定不同的[**HtmlCrossType**](https://reference.aspose.com/cells/java/com.aspose.cells/HtmlCrossType)将其保存为HTML格式。请下载使用该代码生成的[输出HTML](51740745.zip)文件。示例Excel文件包含边框为红色的图像，如本截图所示，显示了对输出HTML中[**HtmlCrossType**](https://reference.aspose.com/cells/java/com.aspose.cells/HtmlCrossType)值的影响。

![todo:image_alt_text](specify-how-to-cross-string-in-output-html-using-htmlcrosstype_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-SpecifyHtmlCrossTypeInOutputHTML.java" >}}
{{< app/cells/assistant language="java" >}}
