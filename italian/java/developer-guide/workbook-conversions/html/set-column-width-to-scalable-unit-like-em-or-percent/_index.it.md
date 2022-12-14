---
title: Imposta la larghezza della colonna su un'unità scalabile come em o percentuale
type: docs
weight: 130
url: /it/java/set-column-width-to-scalable-unit-like-em-or-percent/
---
La generazione di un file HTML da un foglio di calcolo è molto comune. La dimensione delle colonne è definita in "pt" che funziona in molti casi. Tuttavia, può verificarsi un caso in cui questa dimensione fissa potrebbe non essere richiesta. Ad esempio, se la larghezza del pannello contenitore è 600 px in cui viene visualizzata questa pagina HTML. In questo caso, potresti ottenere una barra di scorrimento orizzontale se la larghezza della tabella generata è maggiore. Era necessario che questa dimensione fissa fosse cambiata in un'unità scalabile come em o percent per ottenere una migliore presentazione. Il seguente codice di esempio può essere utilizzato dove[**HtmlSaveOptions.WidthScalable**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#WidthScalable) è impostato per**VERO** per creare una larghezza scalabile.

Il file sorgente di esempio e i file di output possono essere scaricati dai seguenti collegamenti:

[sampleForScalableColumns.xlsx](74776596.xlsx)

[outsampleForScalableColumns.zip](74776597.zip)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "HTML-SetScalableColumnWidth.java" >}}
