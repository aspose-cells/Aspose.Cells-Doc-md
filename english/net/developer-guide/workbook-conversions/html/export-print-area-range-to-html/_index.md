---
title: Export print area range to HTML
type: docs
weight: 60
url: /net/export-print-area-range-to/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**

This is a common scenario where we need to export only the print area, i.e., a selected range of cells, instead of the entire sheet to HTML. This feature is already available for PDF rendering; however, you can now perform this task for HTML as well. First, set the print area in the page‑setup object of the worksheet. Later, use the [**HtmlSaveOptions.ExportPrintAreaOnly**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exportprintareaonly) flag to export only the selected range.

## Sample Code

Following sample code loads a workbook and then exports the print area to HTML. Sample file for testing this feature can be downloaded from the following link:

[sampleInlineCharts.xlsx](79527946.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-HTML-ExportPrintAreaToHtml-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
