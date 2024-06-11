---
title: 不支持的边框样式的Excel转为HTML
type: docs
weight: 80
url: /zh/python-java/excel-with-unsupported-border-style-to/
---

## **不支持的边框样式的Excel转为HTML**
Microsoft Excel支持一些虚线边框类型，这些边框不受Web浏览器支持。当使用Aspose.Cells将此类文件转换为HTML时，这些边框将被移除。但是，Aspose.Cells for Python via Java支持使用HtmlSaveOptions.ExportSimilarBorderStyle属性显示类似的边框。您可以将HtmlSaveOptions.ExportSimilarBorderStyle属性的值设置为True以导出不支持的边框。

以下示例代码加载了包含一些不支持边框的示例Excel文件，并在下图中显示了HtmlSaveOptions.ExportSimilarBorderStyle属性在输出HTML中的效果。

![todo:image_alt_text](Export-Similar-Border-Style.png)

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "HTML-ExportSimilarBorderStyle.py" >}}
