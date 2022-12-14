---
title: 将打印区域范围导出到 HTML
type: docs
weight: 60
url: /zh/java/export-print-area-range-to-html/
---
## 可能的使用场景

这是一个非常常见的场景，我们只需要将打印区域（即选定的单元格范围）而不是整个工作表导出到 HTML。此功能已可用于 PDF 呈现，但是，现在您也可以对 HTML 执行此任务。首先，在工作表的页面设置对象中设置打印区域。以后使用[**HtmlSaveOptions.ExportPrintAreaOnly**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExportPrintAreaOnly)仅导出选定范围的属性。

## Java 将打印区域范围导出到 HTML 的代码

以下示例代码加载工作簿，然后将打印区域导出到 HTML。可以从以下链接下载用于测试此功能的示例文件：

[示例内联图表.xlsx](79527960.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-HTML-ExportPrintAreaToHtml-1.java" >}}

