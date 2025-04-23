---
title: Tre metodi per filtrare i dati del grafico
description: Impara come filtrare i grafici in Excel usando Aspose.Cells per Python via .NET. La nostra guida completa dimostrerà come applicare filtri ai grafici, personalizzare gli elementi del grafico, e usare strumenti di analisi dei dati per migliori insight e decisioni informate.
keywords: Aspose.Cells per Python via .NET, Filtrare Grafici in Excel, Analisi dei Dati, Decisioni, Visualizzazione.
type: docs
weight: 2210
url: /it/python-net/filtering-charts-in-excel/
---

{{% alert color="primary" %}}

## **1. Filtrare le serie per visualizzare un grafico**

### **Passaggi per filtrare le serie da un grafico in Excel**
In Excel, possiamo filtrare serie specifiche da un grafico, causando la non visualizzazione di tali serie filtrate nel grafico. Il grafico originale è mostrato nella **Figura 1**. Tuttavia, quando filtriamo **Testseries2** e **Testseries4**, il grafico apparirà come mostrato nella **Figura 2**.

In Aspose.Cells per Python via .NET, possiamo eseguire un'operazione simile. Per un file [di esempio](seriesFiltered.xlsx) come questo, se vogliamo filtrare **Testseries2** e **Testseries4**, possiamo eseguire il seguente codice. Inoltre, manterremo due liste: una ([n_series](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart/n_series/)) per memorizzare tutte le serie selezionate e un'altra ([filtered_n_series](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart/filtered_n_series/)) per memorizzare le serie filtrate.

Si **noti** che nel codice, quando impostiamo **chart.nSeries[0].is_filtered = TRUE;**, la prima serie in [n_series](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart/n_series/) verrà rimossa e inserita nella posizione appropriata all'interno di [filtered_n_series](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart/filtered_n_series/). Successivamente, la precedente **nSeries[1]** diventerà la nuova prima voce nella lista, e tutte le serie successive si sposteranno avanti di una posizione. Ciò significa che se poi eseguiamo **chart.nSeries[1].is_filtered = TRUE;**, stiamo effettivamente rimuovendo la terza serie originale. Questo può portare a confusione, quindi si consiglia di seguire l'operazione nel codice, che elimina le serie dal basso verso l'alto.

![todo:image_alt_text](Figure1.png)

![todo:image_alt_text](Figure2.png)

### **Codice di Esempio**
Il seguente codice di esempio carica il [file Excel di esempio](seriesFiltered.xlsx).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-seriesFiltered.py" >}}

## **2. Filtrare i dati e far cambiare il grafico**

Filtrare i tuoi dati è un ottimo modo per gestire i filtri del grafico con molti dati. Quando filtri i dati, il grafico cambierà. Un problema che dovremo affrontare è assicurarci che il grafico rimanga sullo schermo. Quando filtri, ottieni righe nascoste, e occasionalmente, il grafico sarà in quelle righe nascoste.

![todo:image_alt_text](Figure3.png)

### **Passaggi per utilizzare i filtri dei dati per modificare il grafico in Excel**

1. Fare clic all'interno del proprio intervallo di dati.
2. Fare clic sulla scheda **Dati**, e attivare i filtri cliccando su Filtri. La riga di intestazione avrà frecce a discesa.
3. Creare un grafico andando alla scheda **Inserisci** e selezionando un grafico a colonne.
4. Ora filtra i tuoi dati utilizzando le frecce a discesa nei dati. Non utilizzare i filtri del grafico.

### **Codice di Esempio**
Il seguente codice di esempio mostra la stessa funzionalità utilizzando Aspsoe.Cells.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-DataFilters.py" >}}

## **3. Filtra i dati utilizzando una Tabella e fai cambiare il grafico**

Utilizzare una Tabella è simile al Metodo 2, utilizzando un intervallo, ma hai vantaggi con le tabelle rispetto agli intervalli. Quando cambia il tuo intervallo in una Tabella e aggiungi dati, il grafico si aggiorna automaticamente. Con un intervallo, dovrai modificare la fonte dati.

### **Formatta come tabella in Excel**

Fare clic all'interno dei dati e utilizzare **CTRL + T** oppure utilizzare la scheda Home, **Formatta come Tabella**

![todo:image_alt_text](Figure4.png)

### **Codice di Esempio**
Il seguente codice di esempio carica il [file Excel di esempio](TableFilters.xlsx) mostra la stessa funzionalità utilizzando Aspsoe.Cells.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-TableFilters.py" >}}
