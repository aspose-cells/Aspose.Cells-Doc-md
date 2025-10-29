---
title: 导出Excel文件为HTML时导出注释
type: docs
weight: 40
url: /zh/python-net/export-comments-while-saving-excel-file-to/
---

## **可能的使用场景**

保存Excel文件为HTML时，不会导出注释。不过，Aspose.Cells for Python via .NET 提供该功能，通过设置 [**HtmlSaveOptions.is_export_comments**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/is_export_comments) 属性，如果设为 **true**，HTML也会显示Excel中的注释。

## **在将 Excel 文件保存为 HTML 时导出批注**

下面的示例代码解释了 [**HtmlSaveOptions.is_export_comments**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/is_export_comments) 属性的用法。截图展示了当它设置为 **true** 时代码对 HTML 的影响。请下载[sample Excel file](50528260.xlsx)和[generated HTML](5052826.txt)以供参考。

![todo:image_alt_text](export-comments-while-saving-excel-file-to-html_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-ExportCommentsWhileSavingExcelFileToHtml.py" >}}
{{< app/cells/assistant language="python-net" >}}
