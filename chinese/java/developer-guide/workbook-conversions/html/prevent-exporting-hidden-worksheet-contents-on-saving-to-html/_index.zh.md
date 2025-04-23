---
title: 在保存为 HTML 时阻止导出隐藏的工作表内容
type: docs
weight: 90
url: /zh/java/prevent-exporting-hidden-worksheet-contents-on-saving-to/
---

{{% alert color="primary" %}}

您可以将 Excel 工作簿保存为 HTML。但是，如果工作簿包含隐藏的工作表，则 Aspose.Cells 默认情况下会将隐藏的工作表内容导出到 HTML 输出的 (_files) 目录中，该目录包含诸如工作表、图像、tabstrip.htm、stylesheet.css 等文件。有时，以这种方式导出隐藏的工作表内容是不合适的。例如，如果隐藏的工作表包含不应导出到 _files 目录的图像。

{{% /alert %}}

Aspose.Cells 提供了 [**HtmlSaveOptions.ExportHiddenWorksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExportHiddenWorksheet) 属性。默认情况下，[**ExportHiddenWorksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExportHiddenWorksheet) 属性设置为 **true**。如果将其设置为 **false**，则 Aspose.Cells 将不会导出隐藏的工作表内容。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-PreventExportingHiddenWorksheetContent-PreventExportingHiddenWorksheetContent.java" >}}

除了控制是否导出隐藏的工作表之外，您还可以配置导出工作簿到 HTML 的其他设置。以下文章演示了 Aspose.Cells 支持的其他导出工作簿到 HTML 的功能。

- [将 Excel 转换为带有标题的 HTML](/cells/zh/java/convert-excel-to-html-with-headings/)
- [在将 Excel 转换为 HTML 时排除未使用的样式](/cells/zh/java/exclude-unused-styles-during-excel-to-html-conversion/)
- [在将 Excel 文件保存为 HTML 时导出批注](/cells/zh/java/export-comments-while-saving-excel-file-to-html/)
- [在保存为 HTML 时隐藏重叠的内容与 CrossHideRight](/cells/zh/java/hiding-overlaid-content-with-crosshideright-while-saving-to-html/)
- [在Web浏览器不支持边框样式时导出相似的边框样式](/cells/zh/java/export-similar-border-style-when-border-style-is-not-supported-by-web-browsers/)
{{< app/cells/assistant language="java" >}}
