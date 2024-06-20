---
title: Esportare le proprietà del documento, del foglio di lavoro e del foglio di calcolo in HTML
type: docs
weight: 50
url: /it/java/export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion/
---

## **Possibili Scenari di Utilizzo**

Quando il file Microsoft Excel viene esportato in HTML usando Microsoft Excel o Aspose.Cells, vengono esportati anche vari tipi di proprietà del documento, del foglio di lavoro e del foglio di calcolo come mostrato nella seguente schermata. È possibile evitare di esportare queste proprietà impostando il [**HtmlSaveOptions.ExportDocumentProperties**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExportDocumentProperties), [**HtmlSaveOptions.ExportWorkbookProperties**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExportWorkbookProperties) e [**HtmlSaveOptions.ExportWorksheetProperties**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExportWorksheetProperties) come **false**. Il valore predefinito di queste proprietà è **true**. La seguente schermata mostra come appaiono queste proprietà nell'HTML esportato.

![todo:image_alt_text](export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion_1.png)

## **Esportare le proprietà del documento, del foglio di lavoro e del foglio di calcolo in HTML**

Il seguente codice di esempio carica il [file Excel di esempio](61767784.xlsx) e lo converte in HTML senza esportare le proprietà del documento, del foglio di lavoro e del foglio di calcolo in [HTML di output](61767783.zip).

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "HTML-ExportDocumentWorkbookAndWorksheetPropertiesInHTML.java" >}}
