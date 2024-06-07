---
title: 在Excel转HTML期间排除未使用样式
type: docs
weight: 30
url: /zh/python-java/exclude-unused-styles-during-excel-to-html-conversion/
---

## **在Excel转换为HTML期间排除未使用的样式**
Microsoft Excel文件可能包含许多未使用的样式。将这些文件导出为HTML格式时，也会导出未使用的样式。这会导致输出HTML的文件大小增加。Aspose.Cells for Python通过Java支持在将Excel文件转换为HTML时不包括这些样式。为此，API提供了[HtmlSaveOptions.ExcludeUnusedStyles](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#ExcludeUnusedStyles)属性。将[HtmlSaveOptions.ExcludeUnusedStyles](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#ExcludeUnusedStyles)属性的值设置为**True**将从输出的HTML中排除所有未使用的样式。

以下截图显示了输出的HTML文件中即将删除的未使用样式。

![todo:image_alt_text](HtmlSaveOptions-Exclude-Unused-Styles.png)

以下示例代码演示了在将Excel转换为HTML过程中删除未使用样式。

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "HTML-ExcludeUnusedStylesInExcelToHTML.py" >}}
