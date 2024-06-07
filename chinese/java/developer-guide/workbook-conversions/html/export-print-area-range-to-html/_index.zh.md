---
title: 将打印区域范围导出到HTML
type: docs
weight: 60
url: /zh/java/export-print-area-range-to-html/
---

## 可能的使用场景

将选定的单元格范围而不是整个工作表导出为HTML是一个非常普遍的场景。这项功能在PDF渲染中已经可用，现在您也可以在HTML中执行此任务。首先，在工作表的页面设置对象中设置打印区域。然后使用[**HtmlSaveOptions.ExportPrintAreaOnly**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExportPrintAreaOnly)属性仅导出选定的范围。

## 导出打印区域范围到HTML的Java代码

以下示例代码加载一个工作簿，然后将打印区域导出到HTML。测试此功能的示例文件可以从以下链接下载：

[sampleInlineCharts.xlsx](79527960.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-HTML-ExportPrintAreaToHtml-1.java" >}}

