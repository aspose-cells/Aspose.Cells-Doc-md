---
title : "Export print area range to HTML" 
description : "" 
weight : 12106 
toc : false
type: docs
url: /net/developerguide/html/export+print+area+range+to+html/
---

# Aspose.Cells for .NET : Export print area range to HTML


{{< panel title="Contents Summary" style="primary" >}}
*   1 [Possible Usage Scenarios](#possible-usage-scenarios)
{{< /panel >}}
 

## Possible Usage Scenarios

This is a common scenario where we need to export only print area i.e. selected range of cells instead of the entire sheet to HTML. This feature is already available for PDF rendering, however, now you can perform this task for HTML as well. First set the print area in the page setup object of the worksheet. Later on, use [HtmlSaveOptions.ExportPrintAreaOnly](https://apireference.aspose.com/net/cells/aspose.cells/htmlsaveoptions/properties/exportprintareaonly) flag to export selected range only.

Sample Code

Following sample code loads a workbook and then exports print area to the HTML. Sample file for testing this feature can be downloaded from the following link:

[sampleInlineCharts.xlsx](https://docs2.aspose.com/cells/net/attachments/79331352/79527946.xlsx)

