---
title: Exportera dokumentarbetsbok och arbetsbladsegenskaper i Excel till HTML omvandling
type: docs
weight: 50
url: /sv/java/export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion/
---

## **Möjliga användningsscenario**

När Microsoft Excel-fil exporteras till HTML med hjälp av Microsoft Excel eller Aspose.Cells, exporteras också olika typer av dokument-, arbetsboks- och arbetsbladsegenskaper enligt följande skärmbild. Du kan undvika att exportera dessa egenskaper genom att ställa in [**HtmlSaveOptions.ExportDocumentProperties**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExportDocumentProperties), [**HtmlSaveOptions.ExportWorkbookProperties**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExportWorkbookProperties) och [**HtmlSaveOptions.ExportWorksheetProperties**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExportWorksheetProperties) som **falska**. Standardvärdet för dessa egenskaper är **sant**. Följande skärmbild visar hur dessa egenskaper ser ut i den exporterade HTML-filen.

![todo:image_alt_text](export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion_1.png)

## **Exportera dokument-, arbetsboks- och arbetsbladsegenskaper i Excel till HTML-omvandling**

Följande provkod laddar [provexelfilen](61767784.xlsx) och konverterar den till HTML och exporterar inte dokument-, arbetsboks- och arbetsbladsegenskaper i [utdata-HTML](61767783.zip).

## **Exempelkod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "HTML-ExportDocumentWorkbookAndWorksheetPropertiesInHTML.java" >}}
{{< app/cells/assistant language="java" >}}
