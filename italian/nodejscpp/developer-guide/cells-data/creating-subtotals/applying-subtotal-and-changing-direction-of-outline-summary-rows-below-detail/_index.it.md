---
title: Applicare il subtotale e cambiare direzione delle righe di riepilogo dell outline sotto il dettaglio
type: docs
weight: 100
url: /it/nodejs-cpp/applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail/
description: Scopri come applicare subtotali e cambiare la direzione delle righe di riepilogo del contorno utilizzando l API Aspose.Cells for Node.js via C++.
keywords: Applica subtotale, Aggiungi subtotale, cambia direzione del riepilogo dell outline. Righe sotto il Dettaglio, cambia direzione del riepilogo dell outline. Colonne a destra del Dettaglio, Crea subtotale e cambia direzione del riepilogo dell outline. Righe sotto il Dettaglio
---

{{% alert color="primary" %}}

Questo articolo spiegherà come applicare il subtotale ai dati e cambiare la direzione delle righe di riepilogo dell'outline sotto il dettaglio.

È possibile applicare il subtotale ai dati utilizzando il metodo [**Worksheet.getCells().subtotal()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#subtotal-cellarea-number-consolidationfunction-numberarray-boolean-boolean-boolean-). Richiede i seguenti parametri.

- **AreaCella** - L'intervallo su cui applicare il subtotale
- **RaggruppaPer** - Il campo su cui raggruppare, come un offset intero basato su zero
- **Funzione** - La funzione del subtotale
- **ListaTotale** - Un array di offset del campo basato su zero, indicando i campi a cui vengono aggiunti i subtotali
- **Sostituisci** - Indica se sostituire i subtotali attuali
- **InterruzioniPagina** - Indica se aggiungere un'interruzione di pagina tra i gruppi
- **RiepilogoSottoDati** - Indica se aggiungere il riepilogo sotto i dati

Inoltre, è possibile controllare la direzione delle **righe di riepilogo dell'outline sotto il dettaglio** come mostrato nella seguente immagine utilizzando la proprietà Worksheet.Outline.SummaryRowBelow. È possibile aprire questa impostazione in Microsoft Excel utilizzando **Dati > Riepilogo > Impostazioni**

![todo:image_alt_text](1.png)

{{% /alert %}}

## Immagini dei file di origine e di output

La seguente immagine mostra il file Excel di origine utilizzato nel codice di esempio sottostante che contiene alcuni dati nelle colonne A e B.

![todo:image_alt_text](2.png)

La seguente schermata mostra il file Excel generato dal codice di esempio. Come si può vedere, è stato applicato un subtotale al range A2:B11 e la direzione dell'outline è righe di riepilogo sotto i dettagli.

![todo:image_alt_text](3.png)

## Node.js per applicare subtotali e cambiare la direzione delle righe di riepilogo del contorno

Ecco il codice di esempio per ottenere l'output mostrato sopra.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-ApplyingSubtotalChangeSummaryDirection-1.js" >}}
