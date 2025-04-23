---
title: Adatta Tutte le Colonne del Foglio di Lavoro su una Singola Pagina PDF
type: docs
weight: 160
url: /it/net/fit-all-worksheet-columns-on-single-pdf-page/
---

{{% alert color="primary" %}}

A volte si desidera generare un file PDF che adatti tutte le colonne di un foglio di lavoro in una sola pagina. La proprietà [**PdfSaveOptions.AllColumnsInOnePagePerSheet**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/allcolumnsinonepagepersheet) fornisce questa funzionalità in modo molto semplice da utilizzare. Calcoli complessi come l'altezza e la larghezza dell'output PDF sono gestiti internamente e si basano sui dati presenti nel foglio di lavoro.

{{% /alert %}}

## **Adatta le Colonne del Foglio di Lavoro su una Singola Pagina PDF**

[**PdfSaveOptions.AllColumnsInOnePagePerSheet**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/allcolumnsinonepagepersheet) garantisce che tutte le colonne in un foglio di lavoro siano rese in un'unica pagina PDF, anche se le righe possono espandersi su più pagine a seconda dei dati presenti nel foglio di lavoro.

Il codice di esempio qui sotto mostra come utilizzare la proprietà [**PdfSaveOptions.AllColumnsInOnePagePerSheet**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/allcolumnsinonepagepersheet) per rendere un ampio foglio di lavoro con 100 colonne.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FitAllWorksheetColumns-1.cs" >}}

{{% alert color="primary" %}}

Quando un dato foglio di lavoro ha molte colonne, il file PDF generato potrebbe mostrare il contenuto in dimensioni molto ridotte. È comunque leggibile se ingrandito in un'applicazione di visualizzazione come Acrobat Reader.

{{% /alert %}} {{% alert color="primary" %}}

Se il foglio di calcolo contiene formule, è meglio chiamare [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula) proprio prima di rendere il foglio di calcolo in formato PDF. In questo modo si garantisce il ricalcolo dei valori dipendenti dalle formule e la visualizzazione dei valori corretti nel PDF.

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
