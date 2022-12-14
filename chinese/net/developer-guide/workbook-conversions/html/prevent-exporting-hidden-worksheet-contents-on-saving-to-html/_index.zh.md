---
title: 防止在保存为 HTML 时导出隐藏的工作表内容
type: docs
weight: 210
url: /zh/net/prevent-exporting-hidden-worksheet-contents-on-saving-to/
---
{{% alert color="primary" %}}

您可以将 Excel 工作簿保存为 HTML。但是，如果工作簿包含隐藏的工作表，默认情况下 Aspose.Cells 会将隐藏的工作表内容导出到 HTML 输出 (_ files) 目录，其中包含工作表、图像、tabstrip.htm、stylesheet.css 等文件。有时，以这种方式导出隐藏工作表的内容并不合适。例如，如果隐藏工作表包含不应导出到_文件目录。

{{% /alert %}}

Aspose.Cells 提供了[**HtmlSaveOptions.ExportHiddenWorksheet**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exporthiddenworksheet)财产。默认情况下，它设置为**真的**和隐藏的工作表导出为 HTML。如果你设置它**错误的**Aspose.Cells 不会导出隐藏的工作表内容。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-PreventExportingHiddenContent-PreventExportingHiddenContentWhileSavingAsHTML.cs" >}}

