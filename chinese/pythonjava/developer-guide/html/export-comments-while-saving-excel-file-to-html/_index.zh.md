---
title: 在将Excel文件保存为HTML时导出评论
type: docs
weight: 60
url: /zh/python-java/export-comments-while-saving-excel-file-to/
---

## **在将Excel文件保存为HTML时导出评论**
在将Excel转换为HTML时，评论不会被导出。Aspose.Cells for Python via Java提供了在将Excel转换为HTML期间导出评论的功能。要实现这一点，API提供了[HtmlSaveOptions.IsExportComments](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#IsExportComments)属性。将[HtmlSaveOptions.IsExportComments](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#IsExportComments)属性的值设置为**True**将在输出的HTML中导出评论。

以下截图显示了样本代码片段生成的输出HTML文件。

![todo:image_alt_text](Export-Comments-while-Saving-Excel-file-to-Html.png)

以下示例代码演示了在将Excel转换为HTML过程中导出评论。

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "HTML-ExportCommentsWhileSavingExcelFileToHtml.py" >}}
