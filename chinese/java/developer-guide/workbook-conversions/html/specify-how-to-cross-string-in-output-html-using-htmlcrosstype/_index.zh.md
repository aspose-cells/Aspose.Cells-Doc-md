---
title: 指定如何在输出 HTML 中跨越字符串使用 HtmlCrossType
type: docs
weight: 140
url: /zh/java/specify-how-to-cross-string-in-output-html-using-htmlcrosstype/
---

## **可能的使用场景**

当单元格包含文本或字符串，但其大小超过单元格的宽度时，如果下一列中的单元格为 null 或为空，则字符串将溢出。将 Excel 文件保存为 HTML 时，您可以通过使用 [**HtmlCrossType**](https://reference.aspose.com/cells/java/com.aspose.cells/HtmlCrossType) 枚举指定交叉类型来控制此溢出。它有以下值

- [**HtmlCrossType.DEFAULT**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#DEFAULT): 类似于 MS Excel 的显示方式，取决于下一个单元格。如果下一个单元格为 null，则字符串会溢出或被截断。

- [**HtmlCrossType.MS_EXPORT**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#MS_EXPORT): 类似于 MS Excel 导出 HTML 的显示字符串。

- [**HtmlCrossType.CROSS**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#CROSS): 显示 HTML 交叉字符串，创建大型 HTML 文件的性能将比将值设置为 [**DEFAULT**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#DEFAULT) 或 [**FIT_TO_CELL**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#FIT_TO_CELL) 快十倍以上。

- [**HtmlCrossType.CROSS_HIDE_RIGHT**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#CROSS_HIDE_RIGHT): 显示 HTML 交叉字符串，并在文本重叠时隐藏右侧的字符串。

- [**HtmlCrossType.FIT_TO_CELL**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#FIT_TO_CELL): 仅在单元格宽度内显示字符串。

## **指定如何在输出 HTML 中跨越字符串使用 HtmlCrossType**

以下示例代码通过指定不同的 [**HtmlCrossType**](https://reference.aspose.com/cells/java/com.aspose.cells/HtmlCrossType)，加载了 [示例 Excel 文件](51740747.xlsx) 并将其保存为 HTML 格式。请下载使用此代码生成的 [输出 HTML](51740745.zip) 文件。示例 Excel 文件中包含边框为红色的图像。

![todo:image_alt_text](specify-how-to-cross-string-in-output-html-using-htmlcrosstype_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-SpecifyHtmlCrossTypeInOutputHTML.java" >}}
