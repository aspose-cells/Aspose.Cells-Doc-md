---
title: Export print area range to HTML
type: docs
weight: 60
url: /python-net/export-print-area-range-to/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**

This is a common scenario where we need to export only print area i.e. selected range of cells instead of the entire sheet to HTML. This feature is already available for PDF rendering, however, now you can perform this task for HTML as well. First set the print area in the page setup object of the worksheet. Later on, use [**HtmlSaveOptions.export_print_area_only**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/export_print_area_only) flag to export selected range only.

## Sample Code

Following sample code loads a workbook and then exports print area to the HTML. Sample file for testing this feature can be downloaded from the following link:

[sampleInlineCharts.xlsx](79527946.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-ExportPrintAreaToHtml-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
