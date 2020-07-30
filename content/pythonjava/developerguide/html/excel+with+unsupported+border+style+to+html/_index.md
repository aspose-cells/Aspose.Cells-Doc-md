---
title : "Excel with unsupported border style to HTML" 
description : "" 
weight : 12036 
toc : false
type: docs
url: /pythonjava/developerguide/html/excel+with+unsupported+border+style+to+html/
---

# Aspose.Cells for Python via Java : Excel with unsupported border style to HTML


{{< panel title="Contents Summary" style="primary" >}}
*   1 [Excel with unsupported border style to HTML](#excel-with-unsupported-border-style-to-html)
{{< /panel >}}
 

 

## Excel with unsupported border style to HTML

Microsoft Excel supports some type of dashed borders that are not supported by Web Browsers. When such files are converted to HTML using Aspose.Cells, those borders are removed. However, Aspose.Cells for Python via Java supports displaying similar borders with [HtmlSaveOptions.ExportSimilarBorderStyle](https://apireference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#ExportSimilarBorderStyle) property. You may set the value of [HtmlSaveOptions.ExportSimilarBorderStyle](https://apireference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#ExportSimilarBorderStyle) property to **True** to export unsupported borders.

The following sample code loads the [sample Excel file](https://docs.aspose.com/download/attachments/64454886/sampleExportSimilarBorderStyle.xlsx?version=1&modificationDate=1522151988853&api=v2) that contains some unsupported borders as shown in the following screenshot. The screenshot further illustrates the effect of [HtmlSaveOptions.ExportSimilarBorderStyle](https://apireference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#ExportSimilarBorderStyle) property inside the [output HTML](https://docs.aspose.com/download/attachments/64454886/outputExportSimilarBorderStyle.zip?version=1&modificationDate=1522151939950&api=v2).

![](https://docs.aspose.com/download/attachments/64454886/Export-Similar-Border-Style.png?version=1&modificationDate=1522151881518&api=v2)

