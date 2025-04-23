---
title: 将打印区域范围导出为HTML
type: docs
weight: 60
url: /zh/python-net/export-print-area-range-to/
---

## **可能的使用场景**

这是一个常见情况，我们需要将选定的单元格范围而不是整个工作表导出为 HTML。此功能已经可用于 PDF 渲染，现在您也可以对 HTML 进行此任务。首先在工作表的页面设置对象中设置打印区域。然后使用 [**HtmlSaveOptions.export_print_area_only**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/export_print_area_only) 标志仅导出选定的范围。

## 示例代码

下面的示例代码加载一个工作簿，然后将打印区域导出到 HTML。用于测试此功能的示例文件可以从以下链接下载：

[sampleInlineCharts.xlsx](79527946.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-ExportPrintAreaToHtml-1.py" >}}
