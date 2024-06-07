---
title: 将打印区域范围导出到HTML
type: docs
weight: 60
url: /zh/net/export-print-area-range-to/
---

## **可能的使用场景**

这是一个常见的情况，我们需要将只打印区域即选定的单元格范围而不是整个工作表导出到HTML。这个功能已经可以用于PDF渲染，现在您也可以为HTML执行此任务。首先在工作表的页面设置对象中设置打印区域。随后，使用[**HtmlSaveOptions.ExportPrintAreaOnly**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exportprintareaonly)标志仅导出选定范围。

## 示例代码

以下示例代码加载一个工作簿，然后将打印区域导出为 HTML。可从以下链接下载用于测试此功能的示例文件:

[sampleInlineCharts.xlsx](79527946.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-HTML-ExportPrintAreaToHtml-1.cs" >}}
