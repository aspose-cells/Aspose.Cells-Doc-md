---
title: Adatta automaticamente le righe per il rendering
type: docs
weight: 130
url: /it/java/autofit-rows-for-rendering/
---
In genere, quando si desidera visualizzare tutto il testo in una cella, è possibile adattare automaticamente la riga nella visualizzazione normale con uno zoom del 100% in Microsoft Excel. Ciò consente al testo di essere completamente visibile nella visualizzazione normale e anche quando si stampa o si salva il file come PDF, il testo verrà visualizzato correttamente.

 Tuttavia, in alcuni casi, la riga di adattamento automatico funziona correttamente nella visualizzazione normale, ma quando si passa alla visualizzazione stampa o si salva il file come PDF, il testo viene troncato. Si prega di controllare il file sorgente[Libro1.xlsx](Book1.xlsx) e screenshot.

![il testo viene ritagliato in printview](text_clipped_in_printview.png)

Se vuoi evitare che il testo venga tagliato nel file PDF salvato, puoi adattare automaticamente la riga con il comando[AutoFitterOptions.ForRendering](https://reference.aspose.com/cells/java/com.aspose.cells/autofitteroptions/#setForRendering-boolean-) opzione.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Docs-Autofit-AutofitRowsForRendering.java" >}}

Ora, il testo non viene troncato nel file di output PDF.

![il testo non viene ritagliato nel pdf salvato](text_not_clipped_in_saved_pdf.png)