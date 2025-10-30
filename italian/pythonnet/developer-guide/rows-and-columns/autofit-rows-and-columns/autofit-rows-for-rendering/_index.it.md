---
title: AutoAdattamento righe per il rendering
type: docs
weight: 130
url: /it/python-net/autofit-rows-for-rendering/
description: Scopri come AutoFit righe per il rendering tramite l API Aspose.Cells per Python via .NET.
keywords: Libreria Excel Python, AutoFit righe per il rendering, Python regola automaticamente l altezza della riga quando si apre il file di Excel. 
---

In generale, quando si vuole visualizzare tutto il testo in una cella, è possibile adattare automaticamente la riga nella visualizzazione Normale con zoom al 100% in Microsoft Excel. Questo consente al testo di essere completamente visibile nella visualizzazione Normale, e anche quando si stampa o si salva il file in formato PDF, il testo verrà visualizzato correttamente.

Tuttavia, in alcuni casi, l'adattamento automatico della riga funziona bene nella visualizzazione Normale, ma quando si passa alla visualizzazione di stampa o si salva il file in formato PDF, il testo viene tagliato. Si prega di controllare il file sorgente [Book1.xlsx](Book1.xlsx) e gli screenshot.

![il testo viene tagliato nella visualizzazione di stampa](text_clipped_in_printview.png)

Se si desidera evitare il testo che viene tagliato nel file PDF salvato, è possibile adattare automaticamente la riga con l'opzione [AutoFitterOptions.for_rendering](https://reference.aspose.com/cells/python-net/aspose.cells/autofitteroptions/for_rendering/).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-AutofitRowsForRendering.py" >}}

Ora, il testo non è tagliato nel file PDF di output.

![il testo non è tagliato nel pdf salvato](text_not_clipped_in_saved_pdf.png)
{{< app/cells/assistant language="python-net" >}}
