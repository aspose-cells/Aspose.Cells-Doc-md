---
title: 将不受支持的边框样式的Excel转换为HTML
type: docs
weight: 80
url: /zh/python-java/excel-with-unsupported-border-style-to/
---

## **将不受支持的边框样式的Excel转换为HTML**
Microsoft Excel支持一些Web浏览器不支持的虚线边框类型。当使用Aspose.Cells将这些文件转换为HTML时，这些边框会被移除。然而，Aspose.Cells for Python via Java支持使用[HtmlSaveOptions.ExportSimilarBorderStyle](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#ExportSimilarBorderStyle)属性显示类似的边框。您可以将[HtmlSaveOptions.ExportSimilarBorderStyle](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#ExportSimilarBorderStyle)属性的值设置为**True**，以导出不受支持的边框。

以下示例代码加载包含一些不受支持边框的[sample Excel文件](sampleExportSimilarBorderStyle.xlsx)，如下截图所示。截图进一步说明了[HtmlSaveOptions.ExportSimilarBorderStyle](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#ExportSimilarBorderStyle)属性对[输出的HTML](outputExportSimilarBorderStyle.zip)内的影响。

![todo:image_alt_text](Export-Similar-Border-Style.png)

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "HTML-ExportSimilarBorderStyle.py" >}}
