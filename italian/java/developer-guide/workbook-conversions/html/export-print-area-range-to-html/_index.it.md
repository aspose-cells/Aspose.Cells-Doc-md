---
title: Esporta l'intervallo dell'area di stampa in HTML
type: docs
weight: 60
url: /it/java/export-print-area-range-to-html/
---
## Possibili scenari di utilizzo

Questo è uno scenario molto comune in cui abbiamo bisogno di esportare solo l'area di stampa, cioè un intervallo selezionato di celle invece dell'intero foglio in HTML. Questa funzione è già disponibile per il rendering PDF, tuttavia ora puoi eseguire questa attività anche per HTML. Innanzitutto, imposta l'area di stampa nell'oggetto di impostazione della pagina del foglio di lavoro. Uso successivo[**HtmlSaveOptions.ExportPrintAreaOnly**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExportPrintAreaOnly)proprietà per esportare solo l'intervallo selezionato.

## Java codice per esportare l'intervallo dell'area di stampa in HTML

Il seguente codice di esempio carica una cartella di lavoro e quindi esporta l'area di stampa nell'HTML. Il file di esempio per testare questa funzione può essere scaricato dal seguente link:

[sampleInlineCharts.xlsx](79527960.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-HTML-ExportPrintAreaToHtml-1.java" >}}

