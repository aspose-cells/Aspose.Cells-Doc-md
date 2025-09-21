---
title: Export Print Area Range to HTML with Golang via C++
linktitle: Export Print Area Range to HTML
type: docs
weight: 60
url: /go-cpp/export-print-area-range-to/
description: Learn how to export the print area range to HTML using Aspose.Cells for C++.
---

## **Possible Usage Scenarios**

This is a common scenario where we need to export only the print area, i.e., a selected range of cells, instead of the entire sheet to HTML. This feature is already available for PDF rendering; however, now you can perform this task for HTML as well. First, set the print area in the page setup object of the worksheet. Later, use the [**HtmlSaveOptions.GetExportPrintAreaOnly()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getexportprintareaonly/) flag to export the selected range only.

## **Sample Code**

The following sample code loads a workbook and then exports the print area to HTML. The sample file for testing this feature can be downloaded from the following link:

[sampleInlineCharts.xlsx](79527946.xlsx)

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ExportPrintAreaRangeToHtml.go" >}}