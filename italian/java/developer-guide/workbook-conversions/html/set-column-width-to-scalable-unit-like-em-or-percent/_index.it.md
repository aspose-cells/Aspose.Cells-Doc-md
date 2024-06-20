---
title: Imposta la larghezza della colonna su unità scalabili come em o percentuale
type: docs
weight: 130
url: /it/java/set-column-width-to-scalable-unit-like-em-or-percent/
---

Generare un file HTML da un foglio di calcolo è molto comune. Le dimensioni delle colonne sono definite in "pt" e funzionano in molti casi. Tuttavia, può verificarsi una situazione in cui questa dimensione fissa potrebbe non essere richiesta. Ad esempio, se la larghezza del pannello contenitore è di 600px dove viene visualizzata questa pagina HTML. In questo caso, potrebbe comparire una barra di scorrimento orizzontale se la larghezza della tabella generata è maggiore. Era necessario che questa dimensione fissa venisse convertita in un'unità scalabile come em o percentuale per ottenere una presentazione migliore. Il codice di esempio seguente può essere utilizzato dove [**HtmlSaveOptions.WidthScalable**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#WidthScalable) è impostato su **true** per creare una larghezza scalabile.

I file di origine e i file di output di esempio possono essere scaricati dai seguenti collegamenti:

[sampleForScalableColumns.xlsx](74776596.xlsx)

[outsampleForScalableColumns.zip](74776597.zip)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "HTML-SetScalableColumnWidth.java" >}}
