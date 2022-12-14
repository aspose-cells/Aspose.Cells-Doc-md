---
title: Adatta tutte le colonne del foglio di lavoro su una singola pagina PDF
type: docs
weight: 160
url: /it/net/fit-all-worksheet-columns-on-single-pdf-page/
---
{{% alert color="primary" %}}

 volte si desidera generare un file PDF che si adatti a tutte le colonne di un foglio di lavoro su una pagina. Il[**PdfSaveOptions.AllColumnsInOnePagePerSheet**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/allcolumnsinonepagepersheet) property fornisce questa funzionalità in un modo molto facile da usare. Calcoli complessi come l'altezza e la larghezza del PDF di output vengono gestiti internamente e si basano sui dati nel foglio di lavoro.

{{% /alert %}}

## **Adatta le colonne del foglio di lavoro a una singola pagina PDF**

[**PdfSaveOptions.AllColumnsInOnePagePerSheet**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/allcolumnsinonepagepersheet)garantisce che tutte le colonne in un foglio di lavoro vengano visualizzate in una singola pagina PDF, sebbene le righe possano espandersi in più pagine a seconda dei dati nel foglio di lavoro.

Il codice di esempio riportato di seguito mostra come utilizzare[**PdfSaveOptions.AllColumnsInOnePagePerSheet**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/allcolumnsinonepagepersheet)proprietà per eseguire il rendering di un foglio di lavoro di grandi dimensioni di 100 colonne.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FitAllWorksheetColumns-1.cs" >}}

{{% alert color="primary" %}}

Quando un determinato foglio di lavoro ha molte colonne, il file PDF sottoposto a rendering potrebbe mostrare il contenuto in dimensioni molto ridotte. È ancora leggibile se ingrandito in un'applicazione di visualizzazione come Acrobat Reader.

{{% /alert %}} {{% alert color="primary" %}}

 Se il tuo foglio di calcolo contiene formule, è meglio chiamare[**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula) appena prima di eseguire il rendering del foglio di calcolo in formato PDF. In questo modo si assicurerà che i valori dipendenti dalla formula vengano ricalcolati e che i valori corretti vengano visualizzati nel PDF.

{{% /alert %}}
