---
title: 用 Golang 通过 C++ 将打印区域范围导出为 HTML
linktitle: 导出打印区域范围到HTML
type: docs
weight: 60
url: /zh/go-cpp/export-print-area-range-to/
description: 学习如何使用编号Aspose.Cells for C++将打印区域范围导出到HTML。
---

## **可能的使用场景**

这是一个常见场景，我们只需导出打印区域，即所选范围的单元格，而非整个工作表到HTML中。此功能已在PDF渲染中实现，现在也可以用于HTML。首先，在工作表的页面设置对象中设置打印区域。之后，使用[**HtmlSaveOptions.GetExportPrintAreaOnly()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getexportprintareaonly/)标志只导出选中的范围。

## **示例代码**

以下示例代码加载工作簿，然后导出其打印区域到HTML。测试此功能的示例文件可以从以下链接下载：

[sampleInlineCharts.xlsx](79527946.xlsx)

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ExportPrintAreaRangeToHtml.go" >}}
