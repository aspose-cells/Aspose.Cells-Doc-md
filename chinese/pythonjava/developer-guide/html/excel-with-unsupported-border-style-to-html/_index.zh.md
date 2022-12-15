---
title: 具有不受支持的 HTML 边框样式的 Excel
type: docs
weight: 80
url: /zh/python-java/excel-with-unsupported-border-style-to/
---
## **具有不受支持的 HTML 边框样式的 Excel**
Microsoft Excel 支持 Web 浏览器不支持的某些类型的虚线边框。当使用 Aspose.Cells 将此类文件转换为 HTML 时，这些边框将被删除。但是，Aspose.Cells for Python via Java 支持显示类似的边框[HtmlSaveOptions.ExportSimilarBorderStyle](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#ExportSimilarBorderStyle)财产。您可以设置值[HtmlSaveOptions.ExportSimilarBorderStyle](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#ExportSimilarBorderStyle)财产给**真的**导出不受支持的边框。

下面的示例代码加载[示例 Excel 文件](sampleExportSimilarBorderStyle.xlsx)包含一些不受支持的边框，如以下屏幕截图所示。截图进一步说明了效果[HtmlSaveOptions.ExportSimilarBorderStyle](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#ExportSimilarBorderStyle)里面的财产[输出 HTML](outputExportSimilarBorderStyle.zip).

![待办事项：图像_替代_文本](Export-Similar-Border-Style.png)

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "HTML-ExportSimilarBorderStyle.py" >}}
