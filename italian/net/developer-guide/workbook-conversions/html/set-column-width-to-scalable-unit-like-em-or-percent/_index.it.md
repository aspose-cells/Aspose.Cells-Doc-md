---
title: Imposta la larghezza della colonna su un'unità scalabile come em o percentuale
type: docs
weight: 130
url: /it/net/set-column-width-to-scalable-unit-like-em-or-percent/
---
La generazione di un file HTML da un foglio di calcolo è molto comune. La dimensione delle colonne è definita in "pt" che funziona in molti casi. Tuttavia, può verificarsi un caso in cui questa dimensione fissa potrebbe non essere richiesta. Ad esempio, se la larghezza di un pannello contenitore è 600 px in cui viene visualizzata questa pagina HTML. In questo caso, potresti ottenere una barra di scorrimento orizzontale se la larghezza della tabella generata è maggiore. Era necessario che questa dimensione fissa fosse cambiata in un'unità scalabile come em o percent per ottenere una migliore presentazione. Il seguente codice di esempio può essere utilizzato dove[**HtmlSaveOptions.WidthScalable**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/widthscalable) è impostato per**VERO** per creare una larghezza scalabile.

Il file sorgente di esempio e i file di output possono essere scaricati dai seguenti collegamenti:

[sampleForScalableColumns.xlsx](73990150.xlsx)

[outsampleForScalableColumns.zip](73990151.zip)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-HTML-SetScalableColumnWidth-1.cs" >}}
