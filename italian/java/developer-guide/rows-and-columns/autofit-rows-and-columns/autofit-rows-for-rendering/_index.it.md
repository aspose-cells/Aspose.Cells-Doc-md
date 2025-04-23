---
title: AutoAdattamento righe per il rendering
type: docs
weight: 130
url: /it/java/autofit-rows-for-rendering/
---

In generale, quando si vuole visualizzare tutto il testo in una cella, è possibile adattare automaticamente la riga nella visualizzazione Normale con zoom al 100% in Microsoft Excel. Questo consente al testo di essere completamente visibile nella visualizzazione Normale, e anche quando si stampa o si salva il file in formato PDF, il testo verrà visualizzato correttamente.

Tuttavia, in alcuni casi, l'adattamento automatico della riga funziona bene nella visualizzazione Normale, ma quando si passa alla visualizzazione di stampa o si salva il file in formato PDF, il testo viene tagliato. Si prega di controllare il file sorgente [Book1.xlsx](Book1.xlsx) e gli screenshot.

![il testo viene tagliato nella visualizzazione di stampa](text_clipped_in_printview.png)

Se si desidera evitare il taglio del testo nel file PDF salvato, è possibile adattare automaticamente la riga con l'opzione [AutoFitterOptions.ForRendering](https://reference.aspose.com/cells/java/com.aspose.cells/autofitteroptions/#setForRendering-boolean-).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Docs-Autofit-AutofitRowsForRendering.java" >}}

Ora, il testo non è tagliato nel file PDF di output.

![il testo non è tagliato nel pdf salvato](text_not_clipped_in_saved_pdf.png)
{{< app/cells/assistant language="java" >}}
