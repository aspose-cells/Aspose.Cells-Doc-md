---
title: Export Comments while Saving Excel file to HTML
type: docs
weight: 40
url: /python-net/export-comments-while-saving-excel-file-to/
---

## **Possible Usage Scenarios**

When you save your Excel file into HTML, comments are not exported. However, Aspose.Cells for Python via .NET provides this feature using the [**HtmlSaveOptions.is_export_comments**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/is_export_comments) property. If you set it **true**, then HTML will also display comments present in your Excel file.

## **Export Comments while Saving Excel file to HTML**

The following sample code explains the usage of [**HtmlSaveOptions.is_export_comments**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/is_export_comments) property. The screenshot shows the effect of the code on the HTML when it is set to **true**. Please download the [sample Excel file](50528260.xlsx) and the [generated HTML](5052826.txt) for a reference.

![todo:image_alt_text](export-comments-while-saving-excel-file-to-html_1.png)

## **Sample Code**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-ExportCommentsWhileSavingExcelFileToHtml.py" >}}
{{< app/cells/assistant language="python-net" >}}