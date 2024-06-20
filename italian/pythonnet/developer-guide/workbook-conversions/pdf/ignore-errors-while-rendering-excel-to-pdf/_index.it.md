---
title: Ignora gli errori durante la conversione di Excel in PDF
type: docs
weight: 80
url: /it/python-net/ignore-errors-while-rendering-excel-to-pdf/
description: Scopri come ignorare gli errori durante la rappresentazione di Excel in PDF con Aspose.Cells per Python via .NET API.
keywords: Ignora gli errori durante la rappresentazione di Excel in PDF, ignora gli errori durante il salvataggio di Excel in PDF usando Python, ignora gli errori durante la conversione di Excel in PDF, ignora gli errori per Excel in PDF in Python
---

## **Possibili Scenari di Utilizzo**

A volte, durante la conversione del file Excel in PDF, si verificano errori o eccezioni e il processo di conversione termina. È possibile ignorare tutti questi errori durante il processo di conversione utilizzando la proprietà [**PdfSaveOptions.ignore_error**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/ignore_error/). In questo modo, il processo di conversione si completerà senza problemi senza generare alcun errore o eccezione, ma potrebbe verificarsi una perdita di dati. Pertanto, si prega di utilizzare questa proprietà solo se la perdita di dati non è critica per te.

## **Ignora gli errori durante la conversione di Excel in PDF**

Il seguente codice carica il [file Excel di esempio](55541778.xlsx) ma il file Excel di esempio è errato e genera un errore durante la [conversione in PDF](55541779.pdf) in 17.11 ma poiché stiamo usando la proprietà [**PdfSaveOptions.ignore_error**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/ignore_error/), non genera un errore. Tuttavia, viene persa una *forma a freccia rossa arrotondata* come mostrato in questa schermata.

![todo:image_alt_text](ignore-errors-while-rendering-excel-to-pdf_1.png)

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-IgnoreErrorsWhileRenderingExcelToPdf.py" >}}
