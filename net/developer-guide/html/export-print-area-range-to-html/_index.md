---
title: Export print area range to HTML
type: docs
weight: 60
url: /net/export-print-area-range-to/
---

## **Possible Usage Scenarios**

This is a common scenario where we need to export only print area i.e. selected range of cells instead of the entire sheet to HTML. This feature is already available for PDF rendering, however, now you can perform this task for HTML as well. First set the print area in the page setup object of the worksheet. Later on, use [**HtmlSaveOptions.ExportPrintAreaOnly**](https://apireference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exportprintareaonly) flag to export selected range only.

## Sample Code

Following sample code loads a workbook and then exports print area to the HTML. Sample file for testing this feature can be downloaded from the following link:

[sampleInlineCharts.xlsx](79527946.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-HTML-ExportPrintAreaToHtml-1.cs" >}}
