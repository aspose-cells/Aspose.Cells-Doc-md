---
title: Exportera dokumentarbetsbok och kalkylbladsegenskaper i Excel till HTML-konvertering
type: docs
weight: 50
url: /sv/net/export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion/
---
## **Möjliga användningsscenarier**

När Microsoft Excel-fil exporteras till HTML med Microsoft Excel eller Aspose.Cells, exporterar den också olika typer av dokument-, arbetsbok- och kalkylbladsegenskaper som visas i följande skärmdump. Du kan undvika att exportera dessa egenskaper genom att ställa in[**HtmlSaveOptions.ExportDocumentProperties**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exportdocumentproperties), [**HtmlSaveOptions.ExportWorkbookProperties**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exportworkbookproperties)och[**HtmlSaveOptions.ExportWorksheetProperties**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exportworksheetproperties) som**falsk** . Standardvärdet för dessa egenskaper är**Sann**. Följande skärmdump visar hur dessa egenskaper ser ut i exporterad HTML.

![todo:image_alt_text](export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion_1.png)

## **Exportera dokument, arbetsbok och kalkylbladsegenskaper i Excel till HTML-konvertering**

 Följande exempelkod laddar[exempel på Excel-fil](61767776.xlsx) och konverterar den till HTML och exporterar inte egenskaperna Dokument, Arbetsbok och Arbetsblad till[mata ut HTML](61767779.zip).

## **Exempelkod**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "HTML-ExportDocumentWorkbookAndWorksheetPropertiesInHTML.cs" >}}
