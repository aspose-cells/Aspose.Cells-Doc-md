---
title: 在Excel转换为HTML时排除未使用的样式
type: docs
weight: 30
url: /zh/python-java/exclude-unused-styles-during-excel-to-html-conversion/
---

## **在将 Excel 转换为 HTML 时排除未使用的样式**
Microsoft Excel文件可能包含许多未使用的样式。将这些文件导出为HTML格式时，未使用的样式也会被导出。这会导致输出HTML文件大小的增加。Aspose.Cells for Python via Java支持在将Excel文件转换为HTML期间排除这些样式。为此，API提供了HtmlSaveOptions.ExcludeUnusedStyles属性。将HtmlSaveOptions.ExcludeUnusedStyles属性的值设置为True将会从输出HTML中排除所有未使用的样式。

以下截图显示了输出HTML文件中将被设置为True的HtmlSaveOptions.ExcludeUnusedStyles属性移除的未使用样式。

![todo:image_alt_text](HtmlSaveOptions-Exclude-Unused-Styles.png)

以下示例代码演示了在将Excel转为HTML期间移除未使用样式。

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "HTML-ExcludeUnusedStylesInExcelToHTML.py" >}}
