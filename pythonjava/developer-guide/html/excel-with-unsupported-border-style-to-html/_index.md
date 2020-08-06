---
title: Excel with unsupported border style to HTML
type: docs
weight: 80
url: /pythonjava/excel-with-unsupported-border-style-to-html/
---

## **Excel with unsupported border style to HTML**
Microsoft Excel supports some type of dashed borders that are not supported by Web Browsers. When such files are converted to HTML using Aspose.Cells, those borders are removed. However, Aspose.Cells for Python via Java supports displaying similar borders with [HtmlSaveOptions.ExportSimilarBorderStyle](https://apireference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#ExportSimilarBorderStyle) property. You may set the value of [HtmlSaveOptions.ExportSimilarBorderStyle](https://apireference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#ExportSimilarBorderStyle) property to **True** to export unsupported borders.

The following sample code loads the [sample Excel file](https://docs.aspose.com/download/attachments/64454886/sampleExportSimilarBorderStyle.xlsx?version=1&modificationDate=1522151988853&api=v2) that contains some unsupported borders as shown in the following screenshot. The screenshot further illustrates the effect of [HtmlSaveOptions.ExportSimilarBorderStyle](https://apireference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#ExportSimilarBorderStyle) property inside the [output HTML](https://docs.aspose.com/download/attachments/64454886/outputExportSimilarBorderStyle.zip?version=1&modificationDate=1522151939950&api=v2).

![todo:image_alt_text](https://docs.aspose.com/download/attachments/64454886/Export-Similar-Border-Style.png?version=1&modificationDate=1522151881518&api=v2)

{{< gist "aspose-com-gists" "f3cac13617c487b51b47cc9ae1d7c008" "HTML-ExportSimilarBorderStyle.py" >}}
