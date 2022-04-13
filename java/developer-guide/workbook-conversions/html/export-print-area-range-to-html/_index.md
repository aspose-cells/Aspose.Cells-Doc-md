---
title: Export print area range to HTML
type: docs
weight: 60
url: /java/export-print-area-range-to-html/
aliases:
    - /java/export-print-area-range-to/
---

## Possible Usage Scenarios

This is a very common scenario that we need to export only print area i.e. selected range of cells instead of the entire sheet to HTML. This feature is already available for PDF rendering, however, now you can perform this task for HTML as well. First, set the print area in the page setup object of the worksheet. Later use [**HtmlSaveOptions.ExportPrintAreaOnly**](https://apireference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExportPrintAreaOnly) property to export selected range only.

## Java code to export print area range to HTML

Following sample code loads a workbook and then exports print area to the HTML. The sample file for testing this feature can be downloaded from the following link:

[sampleInlineCharts.xlsx](79527960.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-HTML-ExportPrintAreaToHtml-1.java" >}}
