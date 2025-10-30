---
title: Adatta tutte le colonne del foglio di lavoro su una singola pagina PDF con Golang tramite C++
linktitle: Adatta Tutte le Colonne del Foglio di Lavoro su una Singola Pagina PDF
type: docs
weight: 160
url: /it/go-cpp/fit-all-worksheet-columns-on-single-pdf-page/
description: Genera un PDF che si adatta a tutte le colonne di un foglio di lavoro in una sola pagina usando Aspose.Cells con Golang tramite C++.
---

{{% alert color="primary" %}}

 A volte si desidera generare un file PDF che si adatti a tutte le colonne di un foglio di lavoro in una sola pagina. La proprietà [**PdfSaveOptions.PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)**](https://reference.aspose.com/cells/go-cpp/paginatedsaveoptions/~paginatedsaveoptions/) fornisce questa funzione in modo molto semplice. Calcoli complessi come altezza e larghezza del PDF di output sono gestiti internamente e sono basati sui dati del foglio di lavoro.

{{% /alert %}}

## **Adatta le Colonne del Foglio di Lavoro su una Singola Pagina PDF**

 [**PdfSaveOptions.PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)**](https://reference.aspose.com/cells/go-cpp/paginatedsaveoptions/~paginatedsaveoptions/) garantisce che tutte le colonne di un foglio siano rappresentate in un singolo PDF, anche se le righe possono espandersi su diverse pagine a seconda dei dati del foglio di lavoro.

 Il codice di esempio seguente mostra come usare la proprietà [**PdfSaveOptions.PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)**](https://reference.aspose.com/cells/go-cpp/paginatedsaveoptions/~paginatedsaveoptions/) per rappresentare un grande foglio di lavoro di 100 colonne.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FitAllWorksheetColumnsOnSinglePdfPage.go" >}}
{{% alert color="primary" %}}

Quando un dato foglio di lavoro ha molte colonne, il file PDF generato potrebbe mostrare il contenuto in dimensioni molto ridotte. È comunque leggibile se ingrandito in un'applicazione di visualizzazione come Acrobat Reader.

{{% /alert %}} {{% alert color="primary" %}}

Se il foglio di calcolo contiene formule, è meglio chiamare [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/go-cpp/workbook/calculateformula/) proprio prima di rendere il foglio di calcolo in formato PDF. In questo modo si garantisce il ricalcolo dei valori dipendenti dalle formule e la visualizzazione dei valori corretti nel PDF.

{{% /alert %}}
