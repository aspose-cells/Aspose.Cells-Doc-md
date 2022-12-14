---
title: Exportera dokumentarbetsbok och kalkylbladsegenskaper i Excel till HTML-konvertering
type: docs
weight: 50
url: /sv/java/export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion/
---
## **Möjliga användningsscenarier**

När Microsoft Excel-fil exporteras till HTML med Microsoft Excel eller Aspose.Cells, exporterar den också olika typer av dokument-, arbetsbok- och kalkylbladsegenskaper som visas i följande skärmdump. Du kan undvika att exportera dessa egenskaper genom att ställa in[**HtmlSaveOptions.ExportDocumentProperties**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExportDocumentProperties), [**HtmlSaveOptions.ExportWorkbookProperties**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExportWorkbookProperties)och[**HtmlSaveOptions.ExportWorksheetProperties**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExportWorksheetProperties)som**falsk**. Standardvärdet för dessa egenskaper är**Sann**. Följande skärmdump visar hur dessa egenskaper ser ut i exporterad HTML.

![todo:image_alt_text](export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion_1.png)

## **Exportera dokument, arbetsbok och kalkylbladsegenskaper i Excel till HTML-konvertering**

Följande exempelkod laddar[exempel på Excel-fil](61767784.xlsx)och konverterar den till HTML och exporterar inte egenskaperna Dokument, Arbetsbok och Arbetsblad till[mata ut HTML](61767783.zip).

## **Exempelkod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "HTML-ExportDocumentWorkbookAndWorksheetPropertiesInHTML.java" >}}
