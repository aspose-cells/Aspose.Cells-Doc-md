---
title: Ignora Errori durante il Rendering di Excel in PDF con Golang tramite C++
linktitle: Ignora gli errori durante la conversione di Excel in PDF
type: docs
weight: 80
url: /it/go-cpp/ignore-errors-while-rendering-excel-to-pdf/
description: Impara come ignorare gli errori durante la conversione di Excel in PDF utilizzando Aspose.Cells for C++.
---

## **Possibili Scenari di Utilizzo**

 A volte, quando converti il tuo file Excel in PDF, si verificano errori o eccezioni e il processo di conversione termina. Puoi ignorare tutti questi errori durante il processo di conversione usando la proprietà [**PdfSaveOptions.PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)**](https://reference.aspose.com/cells/go-cpp/paginatedsaveoptions/~paginatedsaveoptions/). In questo modo, il processo di conversione si completerà senza lanciare errori o eccezioni, ma potrebbe verificarsi una perdita di dati. Usa questa proprietà solo se la perdita di dati non è critica per te.

## **Ignora gli errori durante la conversione di Excel in PDF**

 Il codice seguente carica il [file Excel di esempio](55541778.xlsx) ma il file Excel di esempio contiene errori e si verifica un errore durante la [conversione in PDF](55541779.pdf) in 17.11, ma poiché stiamo usando la proprietà [**PdfSaveOptions.PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)**](https://reference.aspose.com/cells/go-cpp/paginatedsaveoptions/~paginatedsaveoptions/), non viene generato errore. Tuttavia, una *forma a freccia rossa arrotondata* come mostrato in questo screenshot viene persa.

![todo:image_alt_text](ignore-errors-while-rendering-excel-to-pdf_1.png)

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-IgnoreErrorsWhileRenderingExcelToPdf.go" >}}
