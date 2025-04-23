---
title: 在Excel转换为HTML时排除未使用的样式
type: docs
weight: 30
url: /zh/python-net/exclude-unused-styles-during-excel-to-html-conversion/
---

## **可能的使用场景**

Microsoft Excel文件可能包含许多未使用的样式。当将Excel文件导出为HTML格式时，这些未使用的样式也会被导出。这可能会增加HTML的大小。您可以通过将[**HtmlSaveOptions.exclude_unused_styles**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/exclude_unused_styles)属性的值设置为**true**来在将Excel文件转换为HTML时排除未使用的样式。以下屏幕截图显示了输出HTML中的一个未使用样式示例。

![todo:image_alt_text](exclude-unused-styles-during-excel-to-html-conversion_1.png)

## **在将 Excel 转换为 HTML 时排除未使用的样式**

以下示例代码创建一个工作簿，并创建了一个未使用的命名样式。由于将[**HtmlSaveOptions.exclude_unused_styles**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/exclude_unused_styles)设置为**true**，因此此未使用的命名样式将不会导出到[输出HTML](61767778.zip)。但如果将其设置为**false**，则此未使用样式将出现在输出HTML中，并且您可以在上述屏幕截图中查看HTML标记。

## **示例代码**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-ExcludeUnusedStylesInExcelToHTML.py" >}}
