---
title: 导出Excel文件为HTML时导出注释
type: docs
weight: 60
url: /zh/python-java/export-comments-while-saving-excel-file-to/
---

## **在将 Excel 文件保存为 HTML 时导出批注**
将Excel转为HTML时不会导出批注。Aspose.Cells for Python via Java提供了在将Excel转为HTML期间导出批注的功能。要实现此功能，API提供了HtmlSaveOptions.IsExportComments属性。将HtmlSaveOptions.IsExportComments属性的值设置为True将会在输出HTML中导出批注。

以下截图显示了样本代码片段生成的输出HTML文件。

![todo:image_alt_text](Export-Comments-while-Saving-Excel-file-to-Html.png)

以下示例代码演示了在将Excel转为HTML期间导出批注。

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "HTML-ExportCommentsWhileSavingExcelFileToHtml.py" >}}
