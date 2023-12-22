---
title: Ignora gli errori durante il rendering di Excel su PDF
type: docs
weight: 80
url: /it/python-net/ignore-errors-while-rendering-excel-to-pdf/
description: Scopri come ignorare gli errori durante il rendering di Excel in PDF con Aspose.Cells for Python via .NET API.
keywords: Python Ignore Errors while Rendering Excel to PDF, Ignore Errors while saving Excel to PDF using Python, Python Ignore Errors while converting Excel to PDF, Ignore Errors for Excel to PDF in python
---
##  **Possibili scenari di utilizzo**

 A volte, quando converti il tuo file Excel in PDF, si verificano errori o eccezioni e il processo di conversione termina. Puoi ignorare tutti questi errori durante il processo di conversione utilizzando il file[**PdfSaveOptions.ignore_error**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/ignore_error/)proprietà. In questo modo, il processo di conversione verrà completato senza problemi senza generare errori o eccezioni, ma potrebbe verificarsi la perdita di dati. Pertanto, utilizza questa proprietà solo se la perdita di dati non è critica per te.

##  **Ignora gli errori durante il rendering di Excel su PDF**

 Il codice seguente carica il file[file Excel di esempio](55541778.xlsx) ma il file Excel di esempio è errato e genera un errore durante[conversione a PDF](55541779.pdf) in 17.11 ma poiché stiamo utilizzando[**PdfSaveOptions.ignore_error**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/ignore_error/)proprietà, non genera un errore. Tuttavia, uno*forma arrotondata di freccia rossa*come mostrato in questo screenshot è andato perso.

![cose da fare:immagine_alt_testo](ignore-errors-while-rendering-excel-to-pdf_1.png)

##  **Codice d'esempio**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-IgnoreErrorsWhileRenderingExcelToPdf.py" >}}
