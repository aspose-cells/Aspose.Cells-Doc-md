---
title: 在 Excel 到 HTML 的转换过程中排除未使用的样式
type: docs
weight: 30
url: /zh/python-java/exclude-unused-styles-during-excel-to-html-conversion/
---
## **在 Excel 到 HTML 的转换过程中排除未使用的样式**
Microsoft Excel 文件可能包含许多未使用的样式。当这些文件被导出为 HTML 格式时，未使用的样式也会被导出。这会导致输出 HTML 的大小增加。 Aspose.Cells for Python via Java 支持在将Excel文件转换为HTML时排除这些样式。为此，API 提供了[HtmlSaveOptions.ExcludeUnusedStyles](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#ExcludeUnusedStyles)财产。设定值[HtmlSaveOptions.ExcludeUnusedStyles](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#ExcludeUnusedStyles)财产给**真的**将从输出 HTML 中排除所有未使用的样式。

以下屏幕截图显示了 HTML 文件中未使用的样式，这些样式将通过设置值来删除[HtmlSaveOptions.ExcludeUnusedStyles](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#ExcludeUnusedStyles)财产给**真的**.

![待办事项：图像_替代_文本](HtmlSaveOptions-Exclude-Unused-Styles.png)

以下示例代码演示了在 Excel 到 HTML 的转换过程中删除未使用的样式。

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "HTML-ExcludeUnusedStylesInExcelToHTML.py" >}}
