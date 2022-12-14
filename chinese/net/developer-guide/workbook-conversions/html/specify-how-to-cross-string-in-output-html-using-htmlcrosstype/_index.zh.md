---
title: 使用 HtmlCrossType 指定如何在输出 HTML 中交叉字符串
type: docs
weight: 140
url: /zh/net/specify-how-to-cross-string-in-output-html-using-htmlcrosstype/
---
## **可能的使用场景**

当单元格包含文本或字符串但大于单元格的宽度时，如果下一列中的下一个单元格为 null 或为空，则字符串会溢出。当您将 Excel 文件保存为 HTML 时，您可以通过使用[**Html 交叉类型**](https://reference.aspose.com/cells/net/aspose.cells/htmlcrosstype)枚举。它具有以下值

- **HtmlCrossType.Default**: 显示类似 MS Excel，取决于下一个单元格。如果下一个单元格为空，则字符串将交叉或被截断。

- **HtmlCrossType.MSExport**: 像MS Excel 导出HTML 一样显示字符串。

- **HtmlCrossType.交叉**：显示 HTML 交叉字符串，创建大型 HTML 文件的性能比设置为 Default 或 FitToCell 快十倍以上。

- **HtmlCrossType.FitToCell**：只显示单元格宽度内的字符串。

## **使用 HtmlCrossType 指定如何在输出 HTML 中交叉字符串**

下面的示例代码加载[示例 Excel 文件](51740732.xlsx)并通过指定不同的方式将其保存为 HTML 格式[**Html 交叉类型**](https://reference.aspose.com/cells/net/aspose.cells/htmlcrosstype).请下载[输出 HTML](51740734.zip)使用此代码生成。示例 Excel 文件包含带有红色边框的图像，如显示效果的屏幕截图所示[**Html 交叉类型**](https://reference.aspose.com/cells/net/aspose.cells/htmlcrosstype)输出 HTML 上的值。

![待办事项：图片_替代_文本](specify-how-to-cross-string-in-output-html-using-htmlcrosstype_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-SpecifyHtmlCrossTypeInOutputHTML.cs" >}}
