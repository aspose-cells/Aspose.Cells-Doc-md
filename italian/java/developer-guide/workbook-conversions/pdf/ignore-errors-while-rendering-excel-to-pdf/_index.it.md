---
title: Ignora gli errori durante la conversione di Excel in PDF
type: docs
weight: 70
url: /it/java/ignore-errors-while-rendering-excel-to-pdf/
---

## **Possibili Scenari di Utilizzo**

A volte quando converti il tuo file Excel in PDF, si verificano errori o eccezioni e il processo di conversione si interrompe. Puoi ignorare tutti questi errori durante il processo di conversione usando la proprietà [**PdfSaveOptions.IgnoreError**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#IgnoreError). In questo modo, il processo di conversione sarà completato senza problemi e senza generare errori o eccezioni, ma potrebbe verificarsi la perdita di dati. Pertanto, si prega di utilizzare questa proprietà solo se la perdita di dati non è critica per te.

## **Ignora gli errori durante la conversione di Excel in PDF**

Il seguente codice carica il [file Excel di esempio](55541813.xlsx) ma il file Excel di esempio è errato e genera un errore durante la [conversione in PDF](55541814.pdf) in 17.11 ma poiché stiamo utilizzando la proprietà [**PdfSaveOptions.IgnoreError**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#IgnoreError), non genera un errore. Tuttavia, una forma simile ad una freccia rossa arrotondata come mostrato in questo screenshot viene persa.

![todo:image_alt_text](ignore-errors-while-rendering-excel-to-pdf_1.png)

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Rendering-IgnoreErrorsWhileRenderingExcelToPdf.java" >}}
