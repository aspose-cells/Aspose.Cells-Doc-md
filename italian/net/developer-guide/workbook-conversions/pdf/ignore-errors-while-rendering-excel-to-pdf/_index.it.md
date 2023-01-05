---
title: Ignora gli errori durante il rendering di Excel a PDF
type: docs
weight: 80
url: /it/net/ignore-errors-while-rendering-excel-to-pdf/
---
## **Possibili scenari di utilizzo**

 A volte, quando si converte il file Excel in PDF, si verificano errori o eccezioni e il processo di conversione termina. È possibile ignorare tutti questi errori durante il processo di conversione utilizzando il file[**PdfSaveOptions.IgnoreError**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/ignoreerror)proprietà. In questo modo, il processo di conversione verrà completato senza intoppi senza generare errori o eccezioni, ma potrebbe verificarsi la perdita di dati. Pertanto, utilizza questa proprietà solo se la perdita di dati non è critica per te.

## **Ignora gli errori durante il rendering di Excel a PDF**

 Il codice seguente carica il file[esempio di file Excel](55541778.xlsx) ma il file Excel di esempio è errato e genera un errore durante[conversione a PDF](55541779.pdf) in 17.11 ma dal momento che stiamo usando[**PdfSaveOptions.IgnoreError**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/ignoreerror)proprietà, non genera un errore. Tuttavia, uno*a forma di freccia rossa arrotondata*come mostrato in questo screenshot è perso.

![cose da fare:immagine_alt_testo](ignore-errors-while-rendering-excel-to-pdf_1.png)

## **Codice d'esempio**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Rendering-IgnoreErrorsWhileRenderingExcelToPdf.cs" >}}
