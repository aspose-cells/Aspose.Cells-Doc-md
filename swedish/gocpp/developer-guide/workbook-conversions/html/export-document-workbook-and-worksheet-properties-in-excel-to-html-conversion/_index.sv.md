---
title: Exportera dokumentarbok och kalkylbladsegenskaper i Excel till HTML konvertering med Golang via C++
linktitle: Exportera dokumentbok och kalkylbladsattribut i Excel till HTML omvandling
type: docs
weight: 50
url: /sv/go-cpp/export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion/
description: Lär dig hur du exporterar eller undviker att exportera dokument , arbetsboks och kalkylbladsattribut vid konvertering av Excel till HTML med Aspose.Cells for C++.
---

## **Möjliga användningsscenario**

När en Microsoft Excel-fil exporteras till HTML med Microsoft Excel eller Aspose.Cells, exporteras även olika typer av dokument-, arbetsboks- och kalkylbladsattribut, som visas i följande skärmbild. Du kan undvika att exportera dessa egenskaper genom att ställa in [**HtmlSaveOptions.GetExportDocumentProperties()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getexportdocumentproperties/), [**HtmlSaveOptions.GetExportWorkbookProperties()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getexportworkbookproperties/) och [**HtmlSaveOptions.GetExportWorksheetProperties()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getexportworksheetproperties/) till **false**. Standardvärdet är **true**. Följande skärmbild visar hur dessa egenskaper ser ut i exporterad HTML.

![todo:image_alt_text](export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion_1.png)

## **Exportera dokument-, arbetsboks- och kalkylbladsattribut i Excel till HTML-omvandling**

Följande exempel kod laddar [exempel-Excel-filen](61767776.xlsx) och konverterar den till HTML utan att exportera dokument-, arbetsboks- och kalkylbladsattribut i [utdata-HTML](61767779.zip).

## **Exempelkod**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ExportDocumentWorkbookAndWorksheetPropertiesInExcelToHtmlConversion.go" >}}
