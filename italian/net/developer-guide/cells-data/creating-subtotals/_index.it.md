---
title: Creazione di subtotali
type: docs
weight: 800
url: /it/net/creating-subtotals/
---
{{% alert color="primary" %}}

Puoi creare automaticamente subtotali per qualsiasi valore ripetuto in un foglio di calcolo. Aspose.Cells fornisce API funzionalità che consentono di aggiungere subtotali ai fogli di calcolo in modo programmatico.

{{% /alert %}}

## **Utilizzando Microsoft Excel**

Per aggiungere subtotali in Microsoft Excel:

1. Crea un semplice elenco di dati nel primo foglio di lavoro della cartella di lavoro (come mostrato nella figura seguente) e salva il file come Book1.xls.
1. Seleziona qualsiasi cella all'interno dell'elenco.
1.  Dal**Dati** menù, selezionare**Subtotali**. Verrà visualizzata la finestra di dialogo Subtotali. Definire quale funzione utilizzare e dove posizionare i subtotali.

## **Utilizzando il Aspose.Cells API**

 Aspose.Cells offre un corso,[**Cartella di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , che rappresenta un file Excel Microsoft. Il[**Cartella di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook) la classe contiene un[**Fogli di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)raccolta che consente l'accesso a ciascun foglio di lavoro nel file Excel.

 Un foglio di lavoro è rappresentato da[**Foglio di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) classe. La classe fornisce un'ampia gamma di proprietà e metodi per la gestione di fogli di lavoro e altri oggetti. Ogni foglio di lavoro è composto da un[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) collezione. Per aggiungere totali parziali a un foglio di lavoro, utilizzare il[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) classe'[**totale parziale**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/subtotal/index)metodo. Fornire i valori dei parametri al metodo per specificare come deve essere calcolato e posizionato il subtotale.

Negli esempi seguenti, abbiamo aggiunto subtotali al primo foglio di lavoro del file modello (Book1.xls) utilizzando Aspose.Cells API. Quando il codice viene eseguito, viene creato un foglio di lavoro con subtotali.

I frammenti di codice che seguono mostrano come aggiungere subtotali a un foglio di lavoro con Aspose.Cells for .NET.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-CreatingSubtotals-1.cs" >}}

## **Argomenti avanzati**
- [Applicazione del subtotale e modifica della direzione delle righe di riepilogo del contorno sotto il dettaglio](/cells/it/net/applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail/)
