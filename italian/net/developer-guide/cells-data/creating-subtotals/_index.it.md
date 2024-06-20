---
title: Creazione dei subtotali
type: docs
weight: 800
url: /it/net/creating-subtotals/
description: Scopri come creare i subtotali per qualsiasi valore ripetuto in un foglio di calcolo utilizzando l API Aspose.Cells for .NET.
keywords: Applica subtotali, Imposta subtotali, Aggiungi subtotali, Crea subtotali, Come aggiungere subtotali a un foglio di lavoro 
---

{{% alert color="primary" %}}

Puoi creare automaticamente subtotale per qualsiasi valore ripetuto in un foglio di calcolo. Aspose.Cells fornisce funzionalità API che ti aiutano ad aggiungere subtotali ai fogli di calcolo in modo programmato.

{{% /alert %}}

## **Utilizzando Microsoft Excel**

Per aggiungere subtotali in Microsoft Excel:

1. Crea una semplice lista di dati nel primo foglio di lavoro del documento (come mostrato nella figura qui sotto) e salva il file come Book1.xls.
1. Seleziona una qualsiasi cella all'interno della tua lista.
1. Dal menu **Dati**, seleziona **Subtotali**. Verrà visualizzata la finestra di dialogo Subtotali. Definisci quale funzione utilizzare e dove inserire i subtotali.

## **Utilizzando l'API Aspose.Cells**

Aspose.Cells fornisce una classe, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), che rappresenta un file Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) contiene una raccolta [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) che consente l'accesso a ciascun foglio di lavoro nel file Excel.

Un foglio di lavoro è rappresentato dalla classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). La classe fornisce una vasta gamma di proprietà e metodi per la gestione dei fogli di lavoro e di altri oggetti. Ogni foglio di lavoro è composto da una raccolta di [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells). Per aggiungere subtotali a un foglio di lavoro, utilizza il metodo [**Subtotal**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/subtotal/index) della classe [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells). Fornisci valori di parametro al metodo per specificare come il totale parziale deve essere calcolato e posizionato.

Nei seguenti esempi, abbiamo aggiunto dei totali parziali al primo foglio di lavoro del file di modello (Book1.xls) utilizzando l'API di Aspose.Cells. Quando il codice viene eseguito, viene creato un foglio di lavoro con dei totali parziali.

I frammenti di codice che seguono mostrano come aggiungere dei totali parziali a un foglio di lavoro con Aspose.Cells for .NET.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-CreatingSubtotals-1.cs" >}}

## **Argomenti avanzati**
- [Applicazione Subtotale e Modifica della Direzione delle Righe di Riepilogo dell'Outline sotto i Dettagli](/cells/it/net/applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail/)
