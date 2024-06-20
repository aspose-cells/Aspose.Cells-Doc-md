---
title: Tre metodi per filtrare i dati del grafico
description: Scopri come filtrare i grafici in Excel usando Aspose.Cells for .NET. La nostra guida completa mostrerà come applicare filtri ai grafici, personalizzare gli elementi del grafico e utilizzare strumenti di analisi dei dati per ottenere migliori approfondimenti e decisioni informate.
keywords: Aspose.Cells for .NET, Filtraggio dei grafici in Excel, Analisi dei dati, Decision Making, Visualizzazione.
type: docs
weight: 2210
url: /it/net/filtering-charts-in-excel/
---

{{% alert color="primary" %}}

## **1. Filtrare le serie per visualizzare un grafico**

### **Passaggi per filtrare le serie da un grafico in Excel**
In Excel, possiamo filtrare serie specifiche da un grafico, causando la non visualizzazione di tali serie filtrate nel grafico. Il grafico originale è mostrato nella **Figura 1**. Tuttavia, quando filtriamo **Testseries2** e **Testseries4**, il grafico apparirà come mostrato nella **Figura 2**.

In Aspose.Cells, possiamo eseguire un'operazione simile. Per un [esempio](seriesFiltered.xlsx) di file come questo, se vogliamo filtrare **Testseries2** e **Testseries4**, possiamo eseguire il seguente codice. Inoltre, manterremo due liste: una ([NSeries](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/nseries/)) lista per memorizzare tutte le serie selezionate e un'altra ([FilteredNSeries](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/filteredSeries/)) per memorizzare le serie filtrate.

Si prega di **notare** che nel codice, quando impostiamo **chart.NSeries[0].IsFiltered = true;**, la prima serie in [NSeries](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/nseries/) verrà rimossa e posizionata nella posizione appropriata all'interno di [FilteredNSeries](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/filteredSeries/). Successivamente, il precedente **NSeries[1]** diventerà il nuovo primo elemento nella lista, e tutte le serie successive si sposteranno in avanti di una posizione. Questo significa che se eseguiamo poi **chart.NSeries[1].IsFiltered = true;**, stiamo effettivamente rimuovendo la serie originale terza. Questo può a volte portare a confusione, quindi raccomandiamo di seguire l'operazione nel codice, che elimina le serie dalla fine all'inizio.

![todo:image_alt_text](Figure1.png)

![todo:image_alt_text](Figure2.png)

### **Codice di Esempio**
Il seguente codice di esempio carica il [file Excel di esempio](seriesFiltered.xlsx).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "seriesFiltered.cs" >}}

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

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "DataFilters.cs" >}}

## **3. Filtra i dati utilizzando una Tabella e fai cambiare il grafico**

Utilizzare una Tabella è simile al Metodo 2, utilizzando un intervallo, ma hai vantaggi con le tabelle rispetto agli intervalli. Quando cambia il tuo intervallo in una Tabella e aggiungi dati, il grafico si aggiorna automaticamente. Con un intervallo, dovrai modificare la fonte dati.

### **Formatta come tabella in Excel**

Fare clic all'interno dei dati e utilizzare **CTRL + T** oppure utilizzare la scheda Home, **Formatta come Tabella**

![todo:image_alt_text](Figure4.png)

### **Codice di Esempio**
Il seguente codice di esempio carica il [file Excel di esempio](TableFilters.xlsx) mostra la stessa funzionalità utilizzando Aspsoe.Cells.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "TableFilters.cs" >}}
