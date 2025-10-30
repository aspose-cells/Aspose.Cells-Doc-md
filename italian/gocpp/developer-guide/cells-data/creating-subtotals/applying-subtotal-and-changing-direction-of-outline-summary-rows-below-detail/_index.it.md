---
title: Applicare Subtotal e Cambiare Direzione delle Righe di Sommario dell Ombelico sotto dettaglio con Golang tramite C++
linktitle: Applicare il subtotale e cambiare direzione delle righe di riepilogo dell outline sotto il dettaglio
type: docs
weight: 100
url: /it/go-cpp/applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail/
description: Impara come applicare i subtotali e cambiare direzione delle righe di riepilogo outline sotto i dettagli usando l API Aspose.Cells for C++.
keywords: Applica subtotale, Aggiungi subtotale, cambia direzione del riepilogo dell outline. Righe sotto il Dettaglio, cambia direzione del riepilogo dell outline. Colonne a destra del Dettaglio, Crea subtotale e cambia direzione del riepilogo dell outline. Righe sotto il Dettaglio
---

{{% alert color="primary" %}}

Questo articolo spiegherà come applicare Subtotal ai dati e cambiare la direzione delle righe di riepilogo outline sotto i dettagli.

Puoi applicare Subtotal ai dati usando il metodo [**Worksheet.Cells.Subtotal()**](https://reference.aspose.com/cells/go-cpp/cells/subtotal_cellarea_int_consolidationfunction_int32array/). Esso accetta i seguenti parametri:

- **AreaCella** - L'intervallo su cui applicare il subtotale
- **RaggruppaPer** - Il campo su cui raggruppare, come un offset intero basato su zero
- **Funzione** - La funzione del subtotale
- **ListaTotale** - Un array di offset del campo basato su zero, indicando i campi a cui vengono aggiunti i subtotali
- **Replace** - Indica se sostituire i subtotali attuali
- **PageBreaks** - Indica se aggiungere interruzioni di pagina tra i gruppi
- **SummaryBelowData** - Indica se aggiungere il riepilogo sotto i dati.

Puoi anche controllare la direzione delle **righe di riepilogo sotto il dettaglio** dell'outline come mostrato nello screenshot seguente usando la proprietà `Worksheet.Outline.SummaryRowBelow`. Puoi aprire questa impostazione in Microsoft Excel tramite **Dati > Riquadro Outline > Impostazioni**.

![todo:image_alt_text](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_1.png)

{{% /alert %}}

## Immagini dei file di origine e di output

La seguente immagine mostra il file Excel di origine utilizzato nel codice di esempio sottostante che contiene alcuni dati nelle colonne A e B.

![todo:image_alt_text](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_2.png)

La seguente schermata mostra il file Excel generato dal codice di esempio. Come si può vedere, è stato applicato un subtotale al range A2:B11 e la direzione dell'outline è righe di riepilogo sotto i dettagli.

![todo:image_alt_text](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_3.png)

## Codice C++ per applicare Subtotal e modificare la direzione delle righe di riepilogo outline

Ecco il codice di esempio per ottenere l'output mostrato sopra.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ApplyingSubtotalAndChangingDirectionOfOutlineSummaryRowsBelowDetail.go" >}}
