---
title: Creazione di totali parziali
type: docs
weight: 800
url: /it/net/creating-subtotals/
description: Scopri come creare totali parziali per qualsiasi valore ripetuto in un foglio di calcolo utilizzando Aspose.Cells for .NET API.
keywords: Apply Subtotals, Set Subtotals, Add subtotals, Create Subtotals, How to add subtotals to a worksheet 
---
{{% alert color="primary" %}}

Puoi creare automaticamente totali parziali per qualsiasi valore ripetuto in un foglio di calcolo. Aspose.Cells fornisce funzionalità API che ti aiutano ad aggiungere totali parziali ai fogli di calcolo a livello di codice.

{{% /alert %}}

##  **Utilizzando Microsoft Excel**

Per aggiungere totali parziali in Microsoft Excel:

1. Crea un semplice elenco di dati nel primo foglio di lavoro della cartella di lavoro (come mostrato nella figura seguente) e salva il file come Book1.xls.
1. Seleziona qualsiasi cella all'interno dell'elenco.
1.  Dal**Dati** selezionare *Subtotali**. Verrà visualizzata la finestra di dialogo Totali parziali. Definire quale funzione utilizzare e dove posizionare i totali parziali.

##  **Utilizzando lo Aspose.Cells API**

 Aspose.Cells fornisce una lezione,[**Cartella di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , che rappresenta un file Excel Microsoft. IL[**Cartella di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook) la classe contiene a[**Fogli di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)raccolta che consente l'accesso a ciascun foglio di lavoro nel file Excel.

Un foglio di lavoro è rappresentato da[**Foglio di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) classe. La classe fornisce un'ampia gamma di proprietà e metodi per la gestione di fogli di lavoro e altri oggetti. Ogni foglio di lavoro è composto da a[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)collezione. Per aggiungere totali parziali a un foglio di lavoro, utilizzare il comando[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)classe'[**totale parziale**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/subtotal/index)metodo. Fornire valori di parametro al metodo per specificare come calcolare e posizionare il totale parziale.

Negli esempi seguenti, abbiamo aggiunto i totali parziali al primo foglio di lavoro del file modello (Book1.xls) utilizzando Aspose.Cells API. Quando il codice viene eseguito, viene creato un foglio di lavoro con i totali parziali.

I frammenti di codice che seguono mostrano come aggiungere totali parziali a un foglio di lavoro con Aspose.Cells for .NET.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-CreatingSubtotals-1.cs" >}}

##  **Argomenti avanzati**
- [Applicazione del totale parziale e modifica della direzione delle righe di riepilogo della struttura sotto i dettagli](/cells/it/net/applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail/)
