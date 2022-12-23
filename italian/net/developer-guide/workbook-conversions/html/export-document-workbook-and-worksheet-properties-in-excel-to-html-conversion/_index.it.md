---
title: Esporta la cartella di lavoro del documento e le proprietà del foglio di lavoro in Excel alla conversione HTML
type: docs
weight: 50
url: /it/net/export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion/
---
## **Possibili scenari di utilizzo**

Quando il file Excel Microsoft viene esportato in HTML utilizzando Microsoft Excel o Aspose.Cells, esporta anche vari tipi di proprietà Documento, Cartella di lavoro e Foglio di lavoro come mostrato nello screenshot seguente. È possibile evitare di esportare queste proprietà impostando il file[**HtmlSaveOptions.ExportDocumentProperties**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exportdocumentproperties), [**HtmlSaveOptions.ExportWorkbookProperties**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exportworkbookproperties)e[**HtmlSaveOptions.ExportWorksheetProperties**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exportworksheetproperties) come**falso** . Il valore predefinito di queste proprietà è**VERO**. Lo screenshot seguente mostra l'aspetto di queste proprietà nel codice HTML esportato.

![cose da fare:immagine_alt_testo](export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion_1.png)

## **Esporta le proprietà di documenti, cartelle di lavoro e fogli di lavoro in Excel alla conversione HTML**

 Il codice di esempio seguente carica il file[esempio di file Excel](61767776.xlsx) e lo converte in HTML e non esporta le proprietà Documento, Cartella di lavoro e Foglio di lavoro in[uscita HTML](61767779.zip).

## **Codice d'esempio**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "HTML-ExportDocumentWorkbookAndWorksheetPropertiesInHTML.cs" >}}
