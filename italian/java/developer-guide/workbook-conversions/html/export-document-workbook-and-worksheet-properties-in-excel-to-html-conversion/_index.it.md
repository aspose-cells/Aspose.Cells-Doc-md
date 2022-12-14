---
title: Esporta la cartella di lavoro del documento e le proprietà del foglio di lavoro nella conversione da Excel a HTML
type: docs
weight: 50
url: /it/java/export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion/
---
## **Possibili scenari di utilizzo**

Quando il file Excel Microsoft viene esportato in HTML utilizzando Microsoft Excel o Aspose.Cells, esporta anche vari tipi di proprietà Documento, Cartella di lavoro e Foglio di lavoro come mostrato nello screenshot seguente. È possibile evitare di esportare queste proprietà impostando il file[**HtmlSaveOptions.ExportDocumentProperties**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExportDocumentProperties), [**HtmlSaveOptions.ExportWorkbookProperties**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExportWorkbookProperties)e[**HtmlSaveOptions.ExportWorksheetProperties**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExportWorksheetProperties)come**falso**. Il valore predefinito di queste proprietà è**VERO**. Lo screenshot seguente mostra l'aspetto di queste proprietà nell'HTML esportato.

![cose da fare:immagine_alt_testo](export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion_1.png)

## **Esporta le proprietà di documenti, cartelle di lavoro e fogli di lavoro nella conversione da Excel a HTML**

Il codice di esempio seguente carica il file[esempio di file Excel](61767784.xlsx)e lo converte in HTML e non esporta le proprietà Documento, Cartella di lavoro e Foglio di lavoro in[output HTML](61767783.zip).

## **Codice di esempio**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "HTML-ExportDocumentWorkbookAndWorksheetPropertiesInHTML.java" >}}
