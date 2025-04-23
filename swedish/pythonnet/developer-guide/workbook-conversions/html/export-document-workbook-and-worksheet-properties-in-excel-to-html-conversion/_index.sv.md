---
title: Exportera dokumentarbetsbok och arbetsbladsegenskaper i Excel till HTML omvandling
type: docs
weight: 50
url: /sv/python-net/export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion/
---

## **Möjliga användningsscenario**

När Microsoft Excel-filen exporteras till HTML med Microsoft Excel eller Aspose.Cells, exporteras också olika typer av Dokument-, Arbetsboks- och Arbetsbladsegenskaper enligt följande skärmbild. Du kan undvika att exportera dessa egenskaper genom att ange [**HtmlSaveOptions.export_document_properties**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/export_document_properties), [**HtmlSaveOptions.export_workbook_properties**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/export_workbook_properties) och [**HtmlSaveOptions.export_worksheet_properties**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/export_worksheet_properties) till **false**. Standardvärdet för dessa egenskaper är **true**. Den följande skärmbilden visar hur dessa egenskaper ser ut i den exporterade HTML.

![todo:image_alt_text](export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion_1.png)

## **Exportera dokument-, arbetsboks- och arbetsbladsegenskaper i Excel till HTML-omvandling**

Följande exempelkod laddar [exempel Excel-filen](61767776.xlsx) och konverterar den till HTML och exporterar inte Dokument-, Arbetsboks- och Arbetsbladsegenskaper i [utdata-HTML-filen](61767779.zip).

## **Exempelkod**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-ExportDocumentWorkbookAndWorksheetPropertiesInHTML.py" >}}
