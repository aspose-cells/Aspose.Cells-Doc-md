---
title: Applicare il subtotale e cambiare direzione delle righe di riepilogo dell outline sotto il dettaglio
type: docs
weight: 100
url: /it/java/applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail/
---

{{% alert color="primary" %}}

Questo articolo spiegherà come applicare il subtotale ai dati e cambiare la direzione delle righe di riepilogo dell'outline sotto il dettaglio.

È possibile applicare il subtotale ai dati utilizzando il metodo [**Worksheet.Cells.subtotal()**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#subtotal(com.aspose.cells.CellArea,%20int,%20int,%20int[])). Richiede i seguenti parametri.

- **AreaCella** - L'intervallo su cui applicare il subtotale
- **RaggruppaPer** - Il campo su cui raggruppare, come un offset intero basato su zero
- **Funzione** - La funzione del subtotale
- **ListaTotale** - Un array di offset del campo basato su zero, indicando i campi a cui vengono aggiunti i subtotali
- **Sostituisci** - Indica se sostituire i subtotali attuali
- **Interruzioni di pagina** - Indica se aggiungere un'interruzione di pagina tra i gruppi
- **RiepilogoSottoDati** - Indica se aggiungere il riepilogo sotto i dati

Inoltre, è possibile controllare la direzione delle righe di **Riepilogo degli elementi dettagliati sotto** come mostrato nella schermata seguente utilizzando la proprietà [**Worksheet.getOutline().SummaryRowBelow**](https://reference.aspose.com/cells/java/com.aspose.cells/outline#SummaryRowBelow). È possibile aprire questa impostazione in Microsoft Excel tramite **Dati > Riepilogo > Impostazioni**

![todo:image_alt_text](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_1.png)

{{% /alert %}}

## Esempio

### Schermate confrontative dei file di origine e di output

La seguente immagine mostra il file Excel di origine utilizzato nel codice di esempio sottostante che contiene alcuni dati nelle colonne A e B.

![todo:image_alt_text](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_2.png)

La seguente schermata mostra il file Excel di output generato dal codice di esempio. Come puoi vedere, il totale è stato applicato all'intervallo **A2:B11** e la direzione dell'outline è delle righe di riepilogo sotto i dettagli.

![todo:image_alt_text](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_3.png)

### Codice Java per applicare il totale e cambiare la direzione delle righe di riepilogo dell'outline sotto i dettagli

Ecco il codice di esempio per ottenere l'output mostrato sopra.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-ApplyingSubtotal-1.java" >}}
