---
title: Come aggiungere un PivotChart utilizzando Aspose.Cells
linktitle: Grafico pivot
type: docs
weight: 100
url: /it/net/how-to-add-pivot-chart/
description: Come aggiungere un PivotChart utilizzando Aspose.Cells.
keywords: PivotChart
---
## Cosa è un PivotChart

Un grafico pivot è una rappresentazione visiva dei dati in una tabella pivot. I grafici pivot offrono un modo per riassumere, analizzare, esplorare e presentare dati riassuntivi. Ecco alcune caratteristiche e aspetti chiave dei grafici pivot:

1. Rappresentazione Dinamica dei Dati: I grafici pivot si aggiornano automaticamente per riflettere le modifiche nella tabella pivot. Se aggiungi o rimuovi campi nella tabella pivot, il grafico pivot si aggiorna di conseguenza.

1. Interattivo: I grafici pivot sono interattivi, permettendo agli utenti di filtrare, ordinare e approfondire i dati. Questo rende facile esplorare diversi aspetti del set di dati.

1. Layout flessibile: gli utenti possono modificare il layout del grafico pivot trascinando e rilasciando i campi, offrendo flessibilità nella visualizzazione dei dati.

1. Tipi di grafico vari: i grafici pivot possono essere creati utilizzando vari tipi di grafico come grafici a barre, a linee, a torta e altri, a seconda della natura dei dati e delle intuizioni desiderate.

1. Sintesi: i grafici pivot riassumono grandi quantità di dati e possono mostrare totali, medie, conteggi o altre statistiche di sintesi.

1. Filtraggio: offrono capacità di filtraggio, consentendo di visualizzare solo i dati che soddisfano determinati criteri.

<br>
I grafici pivot sono comunemente usati nelle strategie di business intelligence e analisi dei dati per fornire un riassunto visivo chiaro e conciso di insiemi di dati complessi. Sono uno strumento potente per prendere decisioni basate sui dati.

## Come aggiungere un PivotChart utilizzando Aspose.Cells

### **Aggiunta di una tabella pivot**

Per creare una tabella pivot utilizzando Aspose.Cells:

1. Aggiungi alcuni dati a delle celle del foglio di lavoro utilizzando il metodo PutValue/setValue di un oggetto Cell. Puoi anche usare un file modello già compilato con dati. I dati verranno utilizzati come origine dati della tabella pivot.
1. Aggiungi una tabella pivot al foglio di lavoro chiamando il metodo add della collezione PivotTables (incapsulato nell'oggetto Worksheet).
1. Accedi al nuovo oggetto PivotTable dalla collezione PivotTables passando il suo indice. # Usa uno qualsiasi degli oggetti tabella pivot incapsulati nell'oggetto PivotTable per gestire la tabella.

Di seguito sono riportati esempi di codice.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CreatePivotTablesPivotCharts-CreatePivotTable-1.cs" >}}

### **Aggiunta di un grafico pivot**

Per creare un PivotChart utilizzando Aspose.Cells:

1. Aggiungi un grafico.
1. Imposta il PivotSource del grafico per fare riferimento a una tabella pivot esistente nel foglio di calcolo.
1. Imposta altri attributi.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CreatePivotTablesPivotCharts-CreatePivotChart-1.cs" >}}

{{< app/cells/assistant language="csharp" >}}
