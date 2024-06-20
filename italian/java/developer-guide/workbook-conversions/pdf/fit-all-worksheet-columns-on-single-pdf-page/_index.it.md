---
title: Adatta Tutte le Colonne del Foglio di Lavoro su una Singola Pagina PDF
type: docs
weight: 70
url: /it/java/fit-all-worksheet-columns-on-single-pdf-page/
---

{{% alert color="primary" %}}

A volte si desidera generare un file PDF che adatti tutte le colonne di un foglio di calcolo su una singola pagina. La proprietà [**PdfSaveOptions.setAllColumnsInOnePagePerSheet**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#AllColumnsInOnePagePerSheet) fornisce questa funzionalità in modo molto semplice da utilizzare. Calcoli complessi come l'altezza e la larghezza della pagina PDF di output sono gestiti internamente e si basano sui dati nel foglio di calcolo.

{{% /alert %}}

## **Adatta le Colonne del Foglio di Lavoro su una Singola Pagina PDF**

[**PdfSaveOptions.setAllColumnsInOnePagePerSheet**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#AllColumnsInOnePagePerSheet) garantisce che tutte le colonne di un foglio di calcolo siano rese in una singola pagina PDF, anche se le righe possono espandersi su più pagine a seconda dei dati nel foglio di calcolo.

{{% alert color="primary" %}}

Quando un dato foglio di calcolo ha molte colonne, il file PDF generato può mostrare i contenuti a una dimensione molto piccola. Eppure è comunque leggibile quando ingrandito in un'applicazione di visualizzazione come Acrobat Reader.

{{% /alert %}}

Il codice di esempio qui sotto mostra come utilizzare la proprietà [**PdfSaveOptions.setAllColumnsInOnePagePerSheet**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#AllColumnsInOnePagePerSheet) per rendere un ampio foglio di calcolo con 100 colonne.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-FitAllWorksheetColumns-FitAllWorksheetColumns.java" >}}

{{% alert color="primary" %}}

Se il foglio di calcolo contiene formule, è meglio chiamare il metodo [**Workbook.calculateFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula--) subito prima di rendere il foglio di calcolo in formato PDF. In questo modo si garantirà che i valori dipendenti dalle formule vengano ricalcolati e che i valori corretti siano resi nel PDF.

{{% /alert %}}
