---
title: Esportare le proprietà del documento, del foglio di lavoro e del foglio di calcolo in HTML
type: docs
weight: 50
url: /it/net/export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion/
---

## **Possibili Scenari di Utilizzo**

Quando il file di Microsoft Excel viene esportato in HTML utilizzando Microsoft Excel o Aspose.Cells, vengono esportati anche vari tipi di proprietà di Documento, Libro di lavoro e Foglio di lavoro come mostrato nella seguente schermata. Puoi evitare l'esportazione di queste proprietà impostando il [**HtmlSaveOptions.ExportDocumentProperties**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exportdocumentproperties), [**HtmlSaveOptions.ExportWorkbookProperties**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exportworkbookproperties) e [**HtmlSaveOptions.ExportWorksheetProperties**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exportworksheetproperties) su **false**. Il valore predefinito di queste proprietà è **true**. La seguente schermata mostra come appaiono queste proprietà nell'HTML esportato.

![todo:image_alt_text](export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion_1.png)

## **Esportare le proprietà del documento, del foglio di lavoro e del foglio di calcolo in HTML**

Il codice di esempio seguente carica il [file di esempio di Excel](61767776.xlsx) e lo converte in HTML senza esportare le proprietà di Documento, Libro di lavoro e Foglio di lavoro nell'[output HTML](61767779.zip).

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "HTML-ExportDocumentWorkbookAndWorksheetPropertiesInHTML.cs" >}}
