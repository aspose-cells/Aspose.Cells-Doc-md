---
title: Creazione di subtotali
type: docs
weight: 50
url: /it/java/creating-subtotals/
---
{{% alert color="primary" %}}

Puoi creare automaticamente subtotali per qualsiasi valore ripetuto in un foglio di calcolo. Aspose.Cells fornisce le funzionalità API che consentono di aggiungere subtotali ai fogli di calcolo in modo programmatico.

{{% /alert %}}

## **Utilizzando Microsoft Excel**

Per creare subtotali in Microsoft Excel:

1. Crea un semplice elenco di dati nel primo foglio di lavoro della cartella di lavoro (come mostrato nella figura seguente) e salva il file come Book1.xls.
1. Seleziona qualsiasi cella all'interno dell'elenco.
1.  Dal**Dati** menù, selezionare**Subtotali**.
 Viene visualizzata la finestra di dialogo Totali parziali. Definire quale funzione utilizzare e dove posizionare i subtotali.

   **Selezione di un intervallo di dati per aggiungere subtotali**

![cose da fare:immagine_alt_testo](creating-subtotals_1.png)

**La finestra di dialogo Subtotale** 

![cose da fare:immagine_alt_testo](creating-subtotals_2.png)

## **Utilizzando Aspose.Cells API**

 Aspose.Cells offre un corso,[**Cartella di lavoro**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) che rappresenta un file Excel Microsoft. Il[**Cartella di lavoro**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) la classe contiene un[**Raccolta di fogli di lavoro**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)che consente l'accesso a ciascun foglio di lavoro nel file Excel.

 Un foglio di lavoro è rappresentato da[**Foglio di lavoro**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)classe. La classe fornisce un'ampia gamma di proprietà e metodi per la gestione di un foglio di lavoro e altri oggetti. Ogni foglio di lavoro è composto da un[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) collezione. Per creare subtotali in un foglio di lavoro, utilizzare il[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)metodo del totale parziale della classe. Fornire valori appropriati per i parametri del metodo per ottenere il risultato desiderato.

L'esempio seguente mostra come creare subtotali nel primo foglio di lavoro del file modello (Book1.xls) utilizzando Aspose.Cells API.

Quando il codice viene eseguito, viene creato un foglio di lavoro con i subtotali.

**Applicazione di subtotali** 

![cose da fare:immagine_alt_testo](creating-subtotals_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-CreatingSubtotals-CreatingSubtotals.java" >}}
