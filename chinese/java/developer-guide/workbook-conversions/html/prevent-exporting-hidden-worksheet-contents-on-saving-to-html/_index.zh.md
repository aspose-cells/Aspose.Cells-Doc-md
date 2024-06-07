---
title: 在保存为HTML时阻止导出隐藏的工作表内容
type: docs
weight: 90
url: /zh/java/prevent-exporting-hidden-worksheet-contents-on-saving-to/
---

{{% alert color="primary" %}}

您可以将Excel工作簿保存为HTML。但是，如果工作簿包含隐藏的工作表，Aspose.Cells默认会将隐藏的工作表内容导出到包含文件夹的HTML输出中的(_files)目录，这个目录包含工作表、图像、tabstrip.htm、stylesheet.css等文件。有时以这种方式导出隐藏工作表的内容并不合适。例如，如果隐藏的工作表包含不应导出到_files目录中的图像。

{{% /alert %}}

Aspose.Cells提供了[**HtmlSaveOptions.ExportHiddenWorksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExportHiddenWorksheet)属性。默认情况下，[**ExportHiddenWorksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExportHiddenWorksheet)属性设置为true。如果将其设置为false，则Aspose.Cells将不导出隐藏的工作表内容。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-PreventExportingHiddenWorksheetContent-PreventExportingHiddenWorksheetContent.java" >}}

除了控制是否导出隐藏的工作表外，您还可以配置另外一些设置以将工作簿导出为HTML。下面的文章演示了Aspose.Cells支持的导出工作簿到HTML的其他功能。

- [将 Excel 转换为带有标头的 HTML](/cells/zh/java/convert-excel-to-html-with-headings/)
- [在Excel转换为HTML期间排除未使用的样式](/cells/zh/java/exclude-unused-styles-during-excel-to-html-conversion/)
- [在将Excel文件保存为HTML时导出评论](/cells/zh/java/export-comments-while-saving-excel-file-to-html/)
- [在保存为HTML时使用CrossHideRight隐藏叠加内容](/cells/zh/java/hiding-overlaid-content-with-crosshideright-while-saving-to-html/)
- [在Web浏览器不支持边框样式时导出相同的边框样式](/cells/zh/java/export-similar-border-style-when-border-style-is-not-supported-by-web-browsers/)
