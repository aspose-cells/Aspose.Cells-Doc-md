---
title: Imposta la larghezza della colonna su unità scalabili come em o percentuale
type: docs
weight: 130
url: /it/python-net/set-column-width-to-scalable-unit-like-em-or-percent/
---

Generare un file HTML da un foglio di calcolo è molto comune. Le dimensioni delle colonne sono definite in "pt", che funziona in molti casi. Tuttavia, può esserci un caso in cui questa dimensione fissa non sia richiesta. Ad esempio, se la larghezza del pannello contenitore è 600px dove viene visualizzata questa pagina HTML. In questo caso, potresti ottenere una barra di scorrimento orizzontale se la larghezza della tabella generata è maggiore. Era necessario che questa dimensione fissa fosse cambiata in un'unità scalabile come em o percentuale per ottenere una migliore presentazione. Il codice di esempio seguente può essere utilizzato dove [**HtmlSaveOptions.width_scalable**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/width_scalable) è impostato su **true** per creare una larghezza scalabile.

I file di origine e i file di output di esempio possono essere scaricati dai seguenti collegamenti:

[sampleForScalableColumns.xlsx](73990150.xlsx)

[outsampleForScalableColumns.zip](73990151.zip)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-SetScalableColumnWidth-1.py" >}}
