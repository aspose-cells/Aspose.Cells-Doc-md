---
title: 在保存为HTML时阻止导出隐藏的工作表内容
type: docs
weight: 210
url: /zh/net/prevent-exporting-hidden-worksheet-contents-on-saving-to/
---

{{% alert color="primary" %}}

您可以将Excel工作簿保存为HTML。但是，如果工作簿包含隐藏的工作表，Aspose.Cells默认会将隐藏的工作表内容导出到包含文件夹的HTML输出中的(_files)目录，这个目录包含工作表、图像、tabstrip.htm、stylesheet.css等文件。有时以这种方式导出隐藏工作表的内容并不合适。例如，如果隐藏的工作表包含不应导出到_files目录中的图像。

{{% /alert %}}

Aspose.Cells 提供了 [**HtmlSaveOptions.ExportHiddenWorksheet**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exporthiddenworksheet) 属性。默认情况下，它设置为 **true**，隐藏的工作表会导出到 HTML 中。如果将其设置为 **false**，Aspose.Cells 将不会导出隐藏的工作表内容。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-PreventExportingHiddenContent-PreventExportingHiddenContentWhileSavingAsHTML.cs" >}}

