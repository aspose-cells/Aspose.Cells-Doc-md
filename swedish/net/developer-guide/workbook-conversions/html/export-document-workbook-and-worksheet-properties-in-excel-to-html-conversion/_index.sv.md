---
title: Exportera dokumentarbetsbok och arbetsbladsegenskaper i Excel till HTML omvandling
type: docs
weight: 50
url: /sv/net/export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion/
---

## **Möjliga användningsscenario**

När Microsoft Excel-filen exporteras till HTML med Microsoft Excel eller Aspose.Cells, exporteras också olika typer av Dokument-, Arbetsboks- och Arbetsbladsegenskaper enligt följande skärmbild. Du kan undvika att exportera dessa egenskaper genom att ange [**HtmlSaveOptions.ExportDocumentProperties**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exportdocumentproperties), [**HtmlSaveOptions.ExportWorkbookProperties**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exportworkbookproperties) och [**HtmlSaveOptions.ExportWorksheetProperties**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exportworksheetproperties) till **false**. Standardvärdet för dessa egenskaper är **true**. Den följande skärmbilden visar hur dessa egenskaper ser ut i den exporterade HTML.

![todo:image_alt_text](export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion_1.png)

## **Exportera dokument-, arbetsboks- och arbetsbladsegenskaper i Excel till HTML-omvandling**

Följande exempelkod laddar [exempel Excel-filen](61767776.xlsx) och konverterar den till HTML och exporterar inte Dokument-, Arbetsboks- och Arbetsbladsegenskaper i [utdata-HTML-filen](61767779.zip).

## **Exempelkod**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "HTML-ExportDocumentWorkbookAndWorksheetPropertiesInHTML.cs" >}}
