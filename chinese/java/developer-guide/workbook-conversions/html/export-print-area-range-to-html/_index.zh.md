---
title: 将打印区域范围导出为HTML
type: docs
weight: 60
url: /zh/java/export-print-area-range-to-html/
---

## 可能的使用场景

这是一个非常常见的场景，我们需要将仅打印区域即所选单元格的范围导出为HTML，而不是整个工作表。这个功能已经在PDF渲染中可用，现在也可以在HTML中执行此任务。首先在工作表的页面设置对象中设置打印区域。然后仅使用 [**HtmlSaveOptions.ExportPrintAreaOnly**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExportPrintAreaOnly) 属性来仅导出所选范围。

## 导出打印区域范围至HTML的Java代码

以下示例代码加载一个工作簿，然后将打印范围导出至HTML。您可以从以下链接下载用于测试此功能的示例文件:

[sampleInlineCharts.xlsx](79527960.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-HTML-ExportPrintAreaToHtml-1.java" >}}

{{< app/cells/assistant language="java" >}}
