---
title: Adatta tutte le colonne del foglio di lavoro su una singola pagina PDF
type: docs
weight: 70
url: /it/java/fit-all-worksheet-columns-on-single-pdf-page/
---
{{% alert color="primary" %}}

 A volte si desidera generare un file PDF che si adatti a tutte le colonne di un foglio di lavoro su una singola pagina. Il[**PdfSaveOptions.setAllColumnsInOnePagePerSheet**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#AllColumnsInOnePagePerSheet) property fornisce questa funzionalità in un modo molto facile da usare. Calcoli complessi come l'altezza e la larghezza della pagina PDF di output vengono gestiti internamente e si basano sui dati nel foglio di lavoro.

{{% /alert %}}

## **Adatta le colonne del foglio di lavoro a una singola pagina PDF**

[**PdfSaveOptions.setAllColumnsInOnePagePerSheet**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#AllColumnsInOnePagePerSheet)garantisce che tutte le colonne di un foglio di lavoro vengano visualizzate in una singola pagina PDF, sebbene le righe possano espandersi in più pagine a seconda dei dati nel foglio di lavoro.

{{% alert color="primary" %}}

Quando un determinato foglio di lavoro ha molte colonne, il file PDF sottoposto a rendering potrebbe mostrare i contenuti a dimensioni molto ridotte. È ancora leggibile se ingrandito in un'applicazione di visualizzazione come Acrobat Reader.

{{% /alert %}}

 Il codice di esempio seguente mostra come utilizzare il file[**PdfSaveOptions.setAllColumnsInOnePagePerSheet**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#AllColumnsInOnePagePerSheet)proprietà per eseguire il rendering di un foglio di lavoro di grandi dimensioni di 100 colonne.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-FitAllWorksheetColumns-FitAllWorksheetColumns.java" >}}

{{% alert color="primary" %}}

 Se il tuo foglio di calcolo contiene formule, è meglio chiamare[**Workbook.calculateFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula()) appena prima di eseguire il rendering del foglio di calcolo in formato PDF. In questo modo si assicurerà che i valori dipendenti dalla formula vengano ricalcolati e che i valori corretti vengano visualizzati nel PDF.

{{% /alert %}}
