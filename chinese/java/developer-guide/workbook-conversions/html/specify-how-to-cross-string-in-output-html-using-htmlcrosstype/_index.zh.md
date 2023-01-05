---
title: 使用 HtmlCrossType 指定如何在输出 HTML 中交叉字符串
type: docs
weight: 140
url: /zh/java/specify-how-to-cross-string-in-output-html-using-htmlcrosstype/
---
## **可能的使用场景**

当单元格包含文本或字符串但大于单元格的宽度时，如果下一列中的下一个单元格为 null 或为空，则字符串会溢出。当您将 Excel 文件保存到 HTML 时，您可以通过使用[**Html 交叉类型**](https://reference.aspose.com/cells/java/com.aspose.cells/HtmlCrossType)枚举。它具有以下值

- [**HtmlCrossType.DEFAULT**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#DEFAULT): 显示像 MS Excel 取决于下一个单元格。如果下一个单元格为空，则字符串将交叉或被截断。

- [**HtmlCrossType.MS_EXPORT**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#MS_EXPORT): 显示字符串，如 MS Excel 导出 HTML。

- [**HtmlCrossType.CROSS**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#CROSS) : 显示 HTML cross string，创建 HTML 大文件的性能比设置为快十倍以上[**默认**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#DEFAULT)要么[**FIT_TO_CELL**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#FIT_TO_CELL).

- [**HtmlCrossType.CROSS_HIDE_RIGHT**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#CROSS_HIDE_RIGHT): 显示HTML 交叉字符串，当文本重叠时隐藏右边的字符串。

- [**HtmlCrossType.FIT_TO_CELL**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#FIT_TO_CELL)：只显示单元格宽度内的字符串。

## **使用 HtmlCrossType 指定如何在输出 HTML 中交叉字符串**

下面的示例代码加载[示例 Excel 文件](51740747.xlsx)并通过指定不同的方式将其保存为 HTML 格式[**Html 交叉类型**](https://reference.aspose.com/cells/java/com.aspose.cells/HtmlCrossType).请下载[输出 HTML](51740745.zip)使用此代码生成的文件。示例 Excel 文件包含带有红色边框的图像，如显示效果的屏幕截图所示[**Html 交叉类型**](https://reference.aspose.com/cells/java/com.aspose.cells/HtmlCrossType)输出值 HTML。

![待办事项：图片_替代_文本](specify-how-to-cross-string-in-output-html-using-htmlcrosstype_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-SpecifyHtmlCrossTypeInOutputHTML.java" >}}
