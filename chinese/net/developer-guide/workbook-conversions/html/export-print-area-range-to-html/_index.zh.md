---
title: 将打印区域范围导出到 HTML
type: docs
weight: 60
url: /zh/net/export-print-area-range-to/
---
## **可能的使用场景**

这是一种常见的情况，我们只需要将打印区域（即选定的单元格范围）而不是整个工作表导出到 HTML。此功能已可用于 PDF 呈现，但是，现在您也可以对 HTML 执行此任务。首先在工作表的页面设置对象中设置打印区域。稍后，使用[**HtmlSaveOptions.ExportPrintAreaOnly**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exportprintareaonly)仅导出选定范围的标志。

## 示例代码

以下示例代码加载工作簿，然后将打印区域导出到 HTML。可以从以下链接下载用于测试此功能的示例文件：

[示例内联图表.xlsx](79527946.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-HTML-ExportPrintAreaToHtml-1.cs" >}}
