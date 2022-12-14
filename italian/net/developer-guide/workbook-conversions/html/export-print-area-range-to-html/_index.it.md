---
title: Esporta l'intervallo dell'area di stampa in HTML
type: docs
weight: 60
url: /it/net/export-print-area-range-to/
---
## **Possibili scenari di utilizzo**

 Questo è uno scenario comune in cui abbiamo bisogno di esportare solo l'area di stampa, cioè un intervallo selezionato di celle invece dell'intero foglio in HTML. Questa funzione è già disponibile per il rendering PDF, tuttavia ora puoi eseguire questa attività anche per HTML. Per prima cosa impostare l'area di stampa nell'oggetto di impostazione della pagina del foglio di lavoro. In seguito, usa[**HtmlSaveOptions.ExportPrintAreaOnly**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exportprintareaonly) flag per esportare solo l'intervallo selezionato.

## Codice di esempio

Il seguente codice di esempio carica una cartella di lavoro e quindi esporta l'area di stampa nell'HTML. Il file di esempio per testare questa funzione può essere scaricato dal seguente link:

[sampleInlineCharts.xlsx](79527946.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-HTML-ExportPrintAreaToHtml-1.cs" >}}
