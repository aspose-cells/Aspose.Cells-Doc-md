---
title: Ignora gli errori durante la conversione di Excel in PDF
type: docs
weight: 80
url: /it/net/ignore-errors-while-rendering-excel-to-pdf/
---

## **Possibili Scenari di Utilizzo**

A volte, durante la conversione del file Excel in PDF, si verificano errori o eccezioni e il processo di conversione termina. È possibile ignorare tutti questi errori durante il processo di conversione utilizzando la proprietà [**PdfSaveOptions.IgnoreError**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/ignoreerror). In questo modo, il processo di conversione si completerà senza problemi senza generare alcun errore o eccezione, ma potrebbe verificarsi una perdita di dati. Pertanto, si prega di utilizzare questa proprietà solo se la perdita di dati non è critica per te.

## **Ignora gli errori durante la conversione di Excel in PDF**

Il seguente codice carica il [file Excel di esempio](55541778.xlsx) ma il file Excel di esempio è errato e genera un errore durante la [conversione in PDF](55541779.pdf) in 17.11 ma poiché stiamo usando la proprietà [**PdfSaveOptions.IgnoreError**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/ignoreerror), non genera un errore. Tuttavia, viene persa una *forma a freccia rossa arrotondata* come mostrato in questa schermata.

![todo:image_alt_text](ignore-errors-while-rendering-excel-to-pdf_1.png)

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Rendering-IgnoreErrorsWhileRenderingExcelToPdf.cs" >}}
{{< app/cells/assistant language="csharp" >}}
