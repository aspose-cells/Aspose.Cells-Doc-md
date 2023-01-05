---
title: 防止在保存到 HTML 时导出隐藏的工作表内容
type: docs
weight: 90
url: /zh/java/prevent-exporting-hidden-worksheet-contents-on-saving-to/
---
{{% alert color="primary" %}}

您可以将 Excel 工作簿保存到 HTML。但是，如果工作簿包含隐藏工作表，则 Aspose.Cells 默认将隐藏工作表内容导出到 HTML 输出（_ files) 目录，其中包含工作表、图像、tabstrip.htm、stylesheet.css 等文件。有时，以这种方式导出隐藏工作表的内容并不合适。例如，如果隐藏工作表包含不应导出到_文件目录。

{{% /alert %}}

Aspose.Cells 提供了[**HtmlSaveOptions.ExportHiddenWorksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExportHiddenWorksheet)财产。默认情况下，[**导出隐藏工作表**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExportHiddenWorksheet)属性设置为**真的**.如果你将它设置为**错误的**那么 Aspose.Cells 将不会导出隐藏的工作表内容。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-PreventExportingHiddenWorksheetContent-PreventExportingHiddenWorksheetContent.java" >}}

除了控制是否导出隐藏工作表外，您还可以配置导出工作簿到HTML的额外设置。以下文章将演示Aspose.Cells支持的导出工作簿到HTML的其他功能。

- [将 Excel 转换为带标题的 HTML](/cells/zh/java/convert-excel-to-html-with-headings/)
- [在 Excel 到 HTML 转换期间排除未使用的样式](/cells/zh/java/exclude-unused-styles-during-excel-to-html-conversion/)
- [将 Excel 文件保存到 HTML 时导出注释](/cells/zh/java/export-comments-while-saving-excel-file-to-html/)
- [在保存到 HTML 时使用 CrossHideRight 隐藏覆盖内容](/cells/zh/java/hiding-overlaid-content-with-crosshideright-while-saving-to-html/)
- [当 Web 浏览器不支持边框样式时导出类似的边框样式](/cells/zh/java/export-similar-border-style-when-border-style-is-not-supported-by-web-browsers/)
