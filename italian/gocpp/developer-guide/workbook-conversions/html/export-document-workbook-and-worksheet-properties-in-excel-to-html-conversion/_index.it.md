---
title: Esporta le proprietà del documento, il workbook e il foglio di lavoro durante la conversione da Excel a HTML con Golang via C++
linktitle: Esporta le proprietà del documento, del workbook e del foglio di lavoro nella conversione Excel in HTML
type: docs
weight: 50
url: /it/go-cpp/export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion/
description: Impara come esportare o evitare di esportare le proprietà del Documento, Workbook e Foglio di lavoro durante la conversione di file Excel in HTML usando Aspose.Cells for C++.
---

## **Possibili Scenari di Utilizzo**

Quando un file Microsoft Excel viene esportato in HTML usando Microsoft Excel o Aspose.Cells, vengono esportate anche varie tipologie di proprietà del Documento, del Workbook e del Foglio di lavoro, come mostrato nella schermata successiva. È possibile evitare di esportare queste proprietà impostando [**HtmlSaveOptions.GetExportDocumentProperties()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getexportdocumentproperties/), [**HtmlSaveOptions.GetExportWorkbookProperties()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getexportworkbookproperties/) e [**HtmlSaveOptions.GetExportWorksheetProperties()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getexportworksheetproperties/) su **false**. Il valore predefinito di queste proprietà è **true**. La schermata seguente mostra come appaiono in HTML esportato.

![todo:image_alt_text](export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion_1.png)

## **Esporta proprietà del Documento, del Workbook e del Foglio di lavoro nella conversione Excel in HTML**

Il codice di esempio di seguito carica il [file Excel di esempio](61767776.xlsx) e lo converte in HTML senza esportare le proprietà di Documento, Cartella di Lavoro e Foglio di Lavoro nell'[output HTML](61767779.zip).

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ExportDocumentWorkbookAndWorksheetPropertiesInExcelToHtmlConversion.go" >}}
