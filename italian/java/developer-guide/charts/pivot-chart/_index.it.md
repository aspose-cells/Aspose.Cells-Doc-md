---
title: Come aggiungere un PivotChart utilizzando Aspose.Cells
linktitle: Grafico pivot
type: docs
weight: 100
url: /it/java/how-to-add-pivot-chart/
description: Come aggiungere un PivotChart utilizzando Aspose.Cells.
keywords: PivotChart
---
## Cosa è un PivotChart
Un grafico pivot è una rappresentazione visuale dei dati in una tabella pivot. I grafici pivot forniscono un modo per riassumere, analizzare, esplorare e presentare i dati di sintesi. Ecco alcune caratteristiche chiave e aspetti dei grafici pivot:

1. Rappresentazione dinamica dei dati: I grafici pivot si aggiornano automaticamente per riflettere le modifiche nella tabella pivot. Se aggiungi o rimuovi campi nella tabella pivot, anche il grafico pivot viene aggiornato di conseguenza.

1. Interattivo: I grafici pivot sono interattivi, consentono agli utenti di filtrare, ordinare e approfondire nei dati. Ciò facilita l'esplorazione di diversi aspetti dell'insieme di dati.

1. Layout flessibile: Gli utenti possono cambiare il layout del grafico pivot trascinando e rilasciando campi, offrendo così flessibilità nella visualizzazione dei dati.

1. Diversi tipi di grafico: I grafici pivot possono essere creati utilizzando vari tipi di grafico come grafici a barre, grafici a linee, grafici a torta e altro ancora, a seconda della natura dei dati e delle informazioni che si desidera ottenere.

1. Sintesi: I grafici pivot riassumono grandi quantitativi di dati e possono mostrare totali, medie, conteggi o altre statistiche di sintesi.

1. Filtraggio: Forniscono funzionalità di filtraggio, consentendo di visualizzare solo i dati che soddisfano determinati criteri.

<br>
I grafici pivot sono comunemente utilizzati nell'intelligence aziendale e nell'analisi dei dati per fornire un riepilogo visivo chiaro e conciso di complessi set di dati. Sono uno strumento potente per prendere decisioni basate sui dati.

## Come aggiungere un PivotChart utilizzando Aspose.Cells
### **Creazione di una tabella pivot**

Per creare una tabella pivot utilizzando Aspose.Cells:

1. Aggiungi alcuni dati a delle celle del foglio di lavoro utilizzando il metodo PutValue/setValue di un oggetto Cell. Puoi anche usare un file modello già compilato con dati. I dati verranno utilizzati come origine dati della tabella pivot.
1. Aggiungi una tabella pivot al foglio di lavoro chiamando il metodo add della collezione PivotTables (incapsulato nell'oggetto Worksheet).
1. Accedi al nuovo oggetto PivotTable dalla raccolta PivotTables passando il suo indice.
1. Utilizza uno qualsiasi degli oggetti tabella pivot incapsulati nell'oggetto PivotTable per gestire la tabella.

Di seguito è riportato un esempio di codice. L'esecuzione del codice genera un nuovo file: pivotTable_test.xls.

**Dati di input** 

![todo:image_alt_text](create-pivot-tables-and-pivot-charts_1.png)

**La tabella pivot di output**

![todo:image_alt_text](create-pivot-tables-and-pivot-charts_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CreatePivotTable-CreatePivotTable.java" >}}

### **Creare un grafico pivot basato sulla tabella pivot**

Per creare un grafico pivot utilizzando Aspose.Cells:

1. Aggiungi un grafico.
1. Imposta il PivotSource del grafico per fare riferimento a una tabella pivot esistente nel foglio di calcolo.
1. Imposta altri attributi.

Di seguito è riportato il codice utilizzato dal componente per completare il compito. L'esecuzione del codice genera un nuovo file: pivotChart_test.xls.

**Il foglio del grafico pivot**

![todo:image_alt_text](create-pivot-tables-and-pivot-charts_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CreatePivotChartbasedonPivotTable-CreatePivotChartbasedonPivotTable.java" >}}

{{% alert color="primary" %}}

Questo articolo mostra come creare tabelle pivot e grafici pivot utilizzando Aspose.Cells. Speriamo che ti aiuti a utilizzare queste funzionalità nei tuoi scenari.

Aspose.Cells ha beneficiato di anni di ricerca, progettazione e sintonizzazione attenta.

Accogliamo con favore le tue domande, commenti e suggerimenti su [Aspose.Cells Forum](https://forum.aspose.com/c/cells/9). Garantiamo una risposta tempestiva.

{{% /alert %}}
