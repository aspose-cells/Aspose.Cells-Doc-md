---
title: Ignora gli errori durante il rendering di Excel in PDF
type: docs
weight: 70
url: /it/java/ignore-errors-while-rendering-excel-to-pdf/
---
## **Possibili scenari di utilizzo**

A volte, quando converti il tuo file Excel in PDF, si verificano errori o eccezioni e il processo di conversione termina. È possibile ignorare tutti questi errori durante il processo di conversione utilizzando il file[**PdfSaveOptions.IgnoreError**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#IgnoreError)proprietà. In questo modo, il processo di conversione verrà completato senza intoppi senza generare errori o eccezioni, ma potrebbe verificarsi la perdita di dati. Pertanto, utilizza questa proprietà solo se la perdita di dati non è critica per te.

## **Ignora gli errori durante il rendering di Excel in PDF**

Il codice seguente carica il file[esempio di file Excel](55541813.xlsx)ma il file Excel di esempio è errato e genera un errore durante il file[conversione in PDF](55541814.pdf)in 17.11 ma dal momento che stiamo usando[**PdfSaveOptions.IgnoreError**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#IgnoreError)proprietà, non genera un errore. Tuttavia, una forma a forma di freccia rossa arrotondata come mostrato in questo screenshot è andata persa.

![cose da fare:immagine_alt_testo](ignore-errors-while-rendering-excel-to-pdf_1.png)

## **Codice di esempio**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Rendering-IgnoreErrorsWhileRenderingExcelToPdf.java" >}}
