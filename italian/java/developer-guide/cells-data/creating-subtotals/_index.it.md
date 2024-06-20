---
title: Creazione dei subtotali
type: docs
weight: 50
url: /it/java/creating-subtotals/
---

{{% alert color="primary" %}}

Puoi creare automaticamente i subtotali per qualsiasi valore ripetuto in un foglio di calcolo. Aspose.Cells fornisce funzionalità API che ti aiutano ad aggiungere i subtotali ai fogli di calcolo in modo programmato.

{{% /alert %}}

## **Utilizzando Microsoft Excel**

Per creare i subtotali in Microsoft Excel:

1. Crea una semplice lista di dati nel primo foglio di lavoro del documento (come mostrato nella figura qui sotto) e salva il file come Book1.xls.
1. Seleziona una qualsiasi cella all'interno della tua lista.
1. Dal menu **Dati**, seleziona **Subtotali**.
   Viene visualizzata la finestra di dialogo Subtotali. Definisci quale funzione utilizzare e dove posizionare i subtotali.

   **Selezione di un intervallo di dati per aggiungere i subtotali**

![todo:image_alt_text](creating-subtotals_1.png)

**La finestra di dialogo Subtotale** 

![todo:image_alt_text](creating-subtotals_2.png)

## **Utilizzando l'API di Aspose.Cells**

Aspose.Cells fornisce una classe, [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) che rappresenta un file Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) contiene un [**WorksheetCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) che consente l'accesso a ciascun foglio di lavoro nel file Excel.

Un foglio di lavoro è rappresentato dalla classe [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet). La classe fornisce una vasta gamma di proprietà e metodi per gestire un foglio di lavoro e altri oggetti. Ogni foglio di lavoro è composto da una raccolta di [**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/Cells). Per creare i subtotali in un foglio di lavoro, utilizza il metodo di subtotali della classe [**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/Cells). Fornisci valori appropriati per i parametri del metodo per ottenere il risultato desiderato.

L'esempio qui sotto mostra come creare i subtotali nel primo foglio di lavoro del file di modello (Book1.xls) utilizzando l'API di Aspose.Cells.

Quando il codice viene eseguito, viene creato un foglio di lavoro con i subtotali.

**Applicare i subtotali** 

![todo:image_alt_text](creating-subtotals_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-CreatingSubtotals-CreatingSubtotals.java" >}}
