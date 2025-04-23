---
title: 在保存为 HTML 时阻止导出隐藏的工作表内容
type: docs
weight: 210
url: /zh/python-net/prevent-exporting-hidden-worksheet-contents-on-saving-to/
---

{{% alert color="primary" %}}

您可以将 Excel 工作簿保存为 HTML。但是，如果工作簿包含隐藏的工作表，则 Aspose.Cells 默认情况下会将隐藏的工作表内容导出到 HTML 输出的 (_files) 目录中，该目录包含诸如工作表、图像、tabstrip.htm、stylesheet.css 等文件。有时，以这种方式导出隐藏的工作表内容是不合适的。例如，如果隐藏的工作表包含不应导出到 _files 目录的图像。

{{% /alert %}}

Aspose.Cells提供[**HtmlSaveOptions.export_hidden_worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/export_hidden_worksheet) 属性。默认情况下，它设置为**true**并且将隐藏的工作表导出为HTML。如果将其设置为**false**，Aspose.Cells将不会导出隐藏的工作表内容。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-PreventExportingHiddenContentWhileSavingAsHTML.py" >}}

