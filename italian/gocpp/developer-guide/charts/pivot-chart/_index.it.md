---
title: Come aggiungere un PivotChart con Golang tramite C++
linktitle: Grafico pivot
type: docs
weight: 100
url: /it/go-cpp/how-to-add-pivot-chart/
description: Come aggiungere un PivotChart usando Aspose.Cells con Golang tramite C++.
keywords: PivotChart
---

## Cosa è un PivotChart

Un grafico pivot è una rappresentazione visiva dei dati in una tabella pivot. I grafici pivot offrono un modo per riassumere, analizzare, esplorare e presentare dati riassuntivi. Ecco alcune caratteristiche e aspetti chiave dei grafici pivot:

1. **Rappresentazione Dinamica dei Dati**: I grafici pivot si aggiornano automaticamente per riflettere le modifiche nella tabella pivot. Se aggiungi o rimuovi campi nella tabella pivot, il grafico pivot si aggiorna di conseguenza.

1. **Interattivo**: I grafici pivot sono interattivi, permettendo agli utenti di filtrare, ordinare e approfondire i dati. Questo rende facile esplorare diversi aspetti del set di dati.

1. **Layout Flessibile**: Gli utenti possono cambiare il layout del grafico pivot trascinando e rilasciando i campi, offrendo flessibilità su come i dati sono visualizzati.

1. **Tipi di Grafico Vari**: I grafici pivot possono essere creati usando vari tipi di grafico come barre, linee, torte e altro, a seconda della natura dei dati e degli insight desiderati.

1. **Riepilogo**: I grafici pivot riassumono grandi quantità di dati e possono mostrare totali, medie, conteggi o altre statistiche riepilogative.

1. **Filtraggio**: Offrono capacità di filtro, permettendo di visualizzare solo i dati che soddisfano determinati criteri.

<br>
I grafici pivot sono comunemente usati nelle strategie di business intelligence e analisi dei dati per fornire un riassunto visivo chiaro e conciso di insiemi di dati complessi. Sono uno strumento potente per prendere decisioni basate sui dati.

## Come aggiungere un PivotChart utilizzando Aspose.Cells

### **Aggiunta di una tabella pivot**

Per creare una tabella pivot utilizzando Aspose.Cells:

1. Aggiungi alcuni dati a celle del foglio di lavoro utilizzando il metodo `PutValue` o `SetValue` di un oggetto `Cell`. Puoi anche usare un file modello già compilato con dati. I dati saranno usati come fonte della tabella pivot.
1. Aggiungi una tabella pivot al foglio di lavoro chiamando il metodo `Add` della collezione `PivotTables` (racchiuso nell'oggetto `Worksheet`).
1. Accedi al nuovo oggetto `PivotTable` dalla collezione `PivotTables` passando il suo indice. Usa uno qualsiasi degli oggetti tabella pivot racchiusi nell'oggetto `PivotTable` per gestire la tabella.

Di seguito sono riportati esempi di codice.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-PivotChart.go" >}}
### **Aggiunta di un grafico pivot**

Per creare un PivotChart utilizzando Aspose.Cells:

1. Aggiungi un grafico.
1. Imposta il `PivotSource` del grafico per fare riferimento a una tabella pivot esistente nel foglio di calcolo.
1. Imposta altri attributi.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-PivotChart-1.go" >}}
