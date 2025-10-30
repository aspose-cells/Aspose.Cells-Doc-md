---
title: Applicare il subtotale e cambiare direzione delle righe di riepilogo dell outline sotto il dettaglio
type: docs
weight: 100
url: /it/python-net/applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail/
description: Scopri come applicare il subtotale e cambiare la direzione delle righe di riepilogo dell outline sotto il dettaglio utilizzando Aspose.Cells per Python via .NET API.
keywords: Libreria Python Excel, Applica subtotale, Aggiungi subtotale, cambia direzione delle righe di riepilogo dell outline sotto il dettaglio, cambia direzione delle colonne di riepilogo dell outline a destra del dettaglio, Crea subtotale e cambia direzione delle righe di riepilogo dell outline sotto il dettaglio
---

{{% alert color="primary" %}}

Questo articolo spiegherà come applicare il subtotale ai dati e cambiare la direzione delle righe di riepilogo dell'outline sotto il dettaglio.

È possibile applicare il subtotale ai dati utilizzando il metodo [**Worksheet.cells.subtotal()**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/subtotal/#aspose.cells.CellArea-int-aspose.cells.ConsolidationFunction-list-bool-bool-bool). Richiede i seguenti parametri.

- **ca** - L'intervallo su cui applicare il subtotale
- **group_by** - Il campo su cui raggruppare, come un offset intero basato su zero
- **funzione** - La funzione di subtotale.
- **total_list** - Un array di offset di campi basato su zero, indicando i campi ai quali vengono aggiunti i subtotale.
- **replace** - Indica se sostituire i subtotale attuali
- **interruzioni_pagina** - Indica se aggiungere interruzioni di pagina tra i gruppi
- **riepilogo_sotto_dati** - Indica se aggiungere un riepilogo sotto i dati.

Inoltre, è possibile controllare la direzione delle **righe di riepilogo dell'outline sotto il dettaglio** come mostrato nella seguente immagine utilizzando la proprietà Worksheet.Outline.SummaryRowBelow. È possibile aprire questa impostazione in Microsoft Excel utilizzando **Dati > Riepilogo > Impostazioni**

![todo:image_alt_text](1.png)

{{% /alert %}}

## **Immagini dei file di origine e output**

La seguente immagine mostra il file Excel di origine utilizzato nel codice di esempio sottostante che contiene alcuni dati nelle colonne A e B.

![todo:image_alt_text](2.png)

La seguente schermata mostra il file Excel generato dal codice di esempio. Come si può vedere, è stato applicato un subtotale al range A2:B11 e la direzione dell'outline è righe di riepilogo sotto i dettagli.

![todo:image_alt_text](3.png)

## **Codice Python per applicare un subtotale e cambiare la direzione delle righe di riepilogo dell'outline**

Ecco il codice di esempio per ottenere l'output mostrato sopra.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-ApplyingSubtotalChangeSummaryDirection-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
