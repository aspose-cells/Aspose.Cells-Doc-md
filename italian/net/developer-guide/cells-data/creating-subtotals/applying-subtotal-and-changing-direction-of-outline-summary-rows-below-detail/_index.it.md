---
title: Applicazione del totale parziale e modifica della direzione delle righe di riepilogo della struttura sotto i dettagli
type: docs
weight: 100
url: /it/net/applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail/
description: Scopri come applicare il totale parziale e modificare la direzione del riepilogo dello schema Righe sotto i dettagli utilizzando Aspose.Cells for .NET API.
keywords: Apply subtotal, Add subtotal, change direction of outline summary Rows below Detail, change direction of outline summary Columns to right of Detail, Create subtotal and change direction of outline summary Rows below Detail
---
{{% alert color="primary" %}}

Questo articolo spiegherà come applicare il totale parziale ai dati e modificare la direzione delle righe di riepilogo della struttura sotto i dettagli.

 È possibile applicare il totale parziale ai dati utilizzando[**Foglio di lavoro.Cells.Subtotale()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/subtotal/index) metodo. Richiede i seguenti parametri.

- **CellArea** - L'intervallo su cui applicare il totale parziale
- **Raggruppa per** - Il campo in base al quale raggruppare, come offset intero in base zero
- **Funzione** - La funzione subtotale.
- **Elenco totale** Una matrice di offset dei campi in base zero, che indica i campi a cui vengono aggiunti i totali parziali.
- **Sostituire** - Indica se sostituire i totali parziali correnti
- **Interruzioni di pagina** - Indica se aggiungere interruzioni di pagina tra i gruppi
- **Riepilogo sottoDati** - Indica se aggiungere un riepilogo sotto i dati.

 Inoltre, puoi controllare la direzione di Outline**Righe di riepilogo sotto i dettagli** come mostrato nello screenshot seguente utilizzando la proprietà Worksheet.Outline.SummaryRowBelow. È possibile aprire questa impostazione in Microsoft Excel utilizzando**Dati > Struttura > Impostazioni**

![cose da fare:immagine_alt_testo](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_1.png)

{{% /alert %}}

##  Immagini dei file di origine e di output

Lo screenshot seguente mostra il file Excel di origine utilizzato nel codice di esempio riportato di seguito che contiene alcuni dati nelle colonne A e B.

![cose da fare:immagine_alt_testo](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_2.png)

Lo screenshot seguente mostra il file Excel di output generato dal codice di esempio. Come puoi vedere, il totale parziale è stato applicato all'intervallo A2:B11 e la direzione del contorno è rappresentata dalle righe di riepilogo sotto i dettagli.

![cose da fare:immagine_alt_testo](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_3.png)

## Codice C# per applicare il totale parziale e modificare la direzione delle righe di riepilogo del contorno

Ecco il codice di esempio per ottenere l'output come mostrato sopra.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-StylingAndDataFormatting-ApplyingSubtotalChangeSummaryDirection-1.cs" >}}
