---
title: Excel with unsupported border style to HTML
type: docs
weight: 80
url: /python-java/excel-with-unsupported-border-style-to/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Excel with unsupported border style to HTML**
Microsoft Excel supports some type of dashed borders that are not supported by Web Browsers. When such files are converted to HTML using Aspose.Cells, those borders are removed. However, Aspose.Cells for Python via Java supports displaying similar borders with [HtmlSaveOptions.ExportSimilarBorderStyle](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#ExportSimilarBorderStyle) property. You may set the value of [HtmlSaveOptions.ExportSimilarBorderStyle](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#ExportSimilarBorderStyle) property to **True** to export unsupported borders.

The following sample code loads the [sample Excel file](sampleExportSimilarBorderStyle.xlsx) that contains some unsupported borders as shown in the following screenshot. The screenshot further illustrates the effect of [HtmlSaveOptions.ExportSimilarBorderStyle](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#ExportSimilarBorderStyle) property inside the [output HTML](outputExportSimilarBorderStyle.zip).

![todo:image_alt_text](Export-Similar-Border-Style.png)

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "HTML-ExportSimilarBorderStyle.py" >}}
