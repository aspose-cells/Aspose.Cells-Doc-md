---
title: Export print area range to HTML
type: docs
weight: 60
url: /python-net/export-print-area-range-to/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**

This is a common scenario where we need to export only the print area, i.e., a selected range of cells, instead of the entire sheet to HTML. This feature is already available for PDF rendering; however, you can now perform the same task for HTML as well. First, set the print area in the page‑setup object of the worksheet. Later, use the [**HtmlSaveOptions.export_print_area_only**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/export_print_area_only) flag to export the selected range only.

## Sample Code

The following sample code loads a workbook and then exports the print area to HTML. A sample file for testing this feature can be downloaded from the link below:

[sampleInlineCharts.xlsx](79527946.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-ExportPrintAreaToHtml-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
