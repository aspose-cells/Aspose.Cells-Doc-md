---
title: Applicazione del subtotale e modifica della direzione delle righe di riepilogo del contorno sotto il dettaglio
type: docs
weight: 100
url: /it/java/applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail/
---
{{% alert color="primary" %}}

Questo articolo spiegherà come applicare il subtotale ai dati e modificare la direzione delle righe di riepilogo struttura sotto il dettaglio.

 È possibile applicare Subtotale ai dati utilizzando[**Foglio di lavoro.Cells.subtotale()**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#subtotal(com.aspose.cells.CellArea,%20int,%20int,%20int[])) metodo. Richiede i seguenti parametri.

- **CellArea** L'intervallo su cui applicare il subtotale
- **Raggruppare per** - Il campo in base al quale eseguire il raggruppamento, come offset di un numero intero in base zero
- **Funzione** - La funzione del subtotale.
- **Elenco totale** - Un array di offset di campo in base zero, che indica i campi a cui vengono aggiunti i subtotali.
- **Sostituire** - Indica se sostituire i subtotali correnti
- **PageBak** - Indica se aggiungere un'interruzione di pagina tra i gruppi
- **SummaryBelowData** - Indica se aggiungere un riepilogo sotto i dati.

 Inoltre, puoi controllare la direzione di Outline**Righe di riepilogo sotto i dettagli** come mostrato nello screenshot seguente utilizzando[**Worksheet.getOutline().SummaryRowBelow**](https://reference.aspose.com/cells/java/com.aspose.cells/outline#SummaryRowBelow) proprietà. È possibile aprire questa impostazione in Microsoft Excel utilizzando**Dati > Struttura > Impostazioni**

![cose da fare:immagine_alt_testo](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_1.png)

{{% /alert %}}

## Esempio

### Screenshot che confrontano i file di origine e di output

Lo screenshot seguente mostra il file Excel di origine utilizzato nel codice di esempio sottostante che contiene alcuni dati nelle colonne A e B.

![cose da fare:immagine_alt_testo](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_2.png)

Lo screenshot seguente mostra il file Excel di output generato dal codice di esempio. Come puoi vedere, il subtotale è stato applicato all'intervallo**A2:B11** e la direzione del contorno è righe di riepilogo sotto il dettaglio.

![cose da fare:immagine_alt_testo](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_3.png)

### Java codice per applicare il subtotale e modificare la direzione delle righe di riepilogo del contorno sotto il dettaglio

Ecco il codice di esempio per ottenere l'output mostrato sopra.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-ApplyingSubtotal-1.java" >}}
