---
title: Tre metodi per filtrare i dati del grafico
description: Scopri come filtrare i grafici in Excel utilizzando Aspose.Cells for .NET. La nostra guida completa dimostrerà come applicare filtri ai grafici, personalizzare gli elementi del grafico e utilizzare strumenti di analisi dei dati per ottenere informazioni migliori e prendere decisioni informate.
keywords: Aspose.Cells for .NET, Filtering Charts in Excel, Data Analysis, Decision Making, Visualization.
type: docs
weight: 2210
url: /it/net/filtering-charts-in-excel/
---
{{% alert color="primary" %}}

##  **1. Filtrare le serie per visualizzare un grafico**

###  **Passaggi per filtrare le serie da un grafico in Excel**
 In Excel, possiamo filtrare serie specifiche da un grafico, facendo sì che le serie filtrate non vengano visualizzate nel grafico. Il grafico originale è mostrato in**Figura 1**. Tuttavia, quando filtriamo **Testseries2** e *Testseries4**, il grafico apparirà come mostrato nella *Figura 2**.

 Allo Aspose.Cells possiamo eseguire un'operazione simile. Per un[campione](seriesFiltered.xlsx) file come questo, se vogliamo filtrarlo**Serie di test2** e *Testseries4**, possiamo eseguire il seguente codice. Inoltre, manterremo due elenchi: uno ([Serie N](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/nseries/)) elenco per memorizzare tutte le serie selezionate e un altro ([NSeries filtrato](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/filteredSeries/)) per memorizzare la serie filtrata.

Per favore**Nota** quello nel codice, quando impostiamo**chart.NSeries[0].IsFiltered = true;**, la prima serie in [NSeries](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/nseries/) verrà rimossa e inserito nella posizione appropriata all'interno di [FilteredNSeries](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/filteredSeries/). Successivamente, la precedente **NSeries[1]** diventerà il nuovo primo elemento dell'elenco e tutte le serie successive si sposteranno in avanti di una posizione. Ciò significa che se poi eseguiamo *chart.NSeries[1].IsFiltered = true;**, stiamo effettivamente rimuovendo la terza serie originale. Questo a volte può creare confusione, quindi consigliamo di seguire l'operazione nel codice, che cancella le serie dalla fine all'inizio.

![cose da fare:immagine_alt_testo](Figure1.png)

![cose da fare:immagine_alt_testo](Figure2.png)

###  **Codice d'esempio**
 Il codice di esempio seguente carica il file[file Excel di esempio](seriesFiltered.xlsx).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "seriesFiltered.cs" >}}

##  **2. Filtra i dati e lascia che il grafico cambi**

Filtrare i dati è un ottimo modo per gestire i filtri dei grafici con molti dati. Quando filtri i dati, il grafico cambierà. Un problema che dovremo affrontare è garantire che il grafico rimanga sullo schermo. Quando filtri, ottieni righe nascoste e, occasionalmente, il grafico si troverà in quelle righe nascoste.

![cose da fare:immagine_alt_testo](Figure3.png)

###  **Passaggi per utilizzare i filtri dati per modificare il grafico in Excel**

1. Fai clic all'interno dell'intervallo di dati.
 2. Fare clic su**Dati** scheda e attiva Filtri facendo clic su Filtri. La riga di intestazione avrà frecce a discesa.
 3. Crea un grafico andando a**Inserire** scheda e selezionando un grafico a colonne.
4. Ora filtra i tuoi dati utilizzando le frecce a discesa nei dati. Non utilizzare i filtri del grafico.

###  **Codice d'esempio**
Il seguente codice di esempio mostra la stessa funzionalità utilizzando Aspsoe.Cells.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "DataFilters.cs" >}}

##  **3. Filtra i dati utilizzando una tabella e lascia che il grafico cambi**

L'utilizzo di una tabella è simile al Metodo 2, che prevede l'utilizzo di un intervallo, ma con le tabelle rispetto agli intervalli si presentano vantaggi. Quando modifichi l'intervallo in una tabella e aggiungi dati, il grafico si aggiorna automaticamente. Con un intervallo, dovrai modificare l'origine dati.

###  **Formato come tabella in Excel**

 Fai clic all'interno dei tuoi dati e utilizza**CTRL+T** oppure utilizza la scheda Home,**Formato come tabella**

![cose da fare:immagine_alt_testo](Figure4.png)

###  **Codice d'esempio**
 Il codice di esempio seguente carica il file[file Excel di esempio](TableFilters.xlsx) mostra la stessa funzione utilizzando Aspsoe.Cells.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "TableFilters.cs" >}}