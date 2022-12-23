---
title: 在 Excel 到 HTML 转换期间排除未使用的样式
type: docs
weight: 30
url: /zh/java/exclude-unused-styles-during-excel-to-html-conversion/
---
## **可能的使用场景**

Microsoft Excel 文件可能包含许多未使用的样式。当您将 Excel 文件导出为 HTML 格式时，这些未使用的样式也会被导出。这会增加 HTML 的大小。您可以在将 Excel 文件转换为 HTML 期间使用[**HtmlSaveOptions.ExcludeUnusedStyles**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExcludeUnusedStyles)财产。当你设置它**真的**，所有未使用的样式都从输出 HTML 中排除。以下屏幕截图显示了输出 HTML 中未使用的样式示例。

![待办事项：图片_替代_文本](exclude-unused-styles-during-excel-to-html-conversion_1.png)

## **在 Excel 到 HTML 转换期间排除未使用的样式**

下面的示例代码创建一个工作簿，还创建一个未使用的命名样式。自从[**HtmlSaveOptions.ExcludeUnusedStyles**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExcludeUnusedStyles)被设置为**真的**所以这个未使用的命名样式将不会导出到[输出 HTML](61767781.zip).但是如果你设置它**错误的**，然后这个未使用的样式将出现在输出 HTML 中，然后您可以在 HTML 标记中看到它，如上面的屏幕截图所示。

## **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "HTML-ExcludeUnusedStylesInExcelToHTML.java" >}}
