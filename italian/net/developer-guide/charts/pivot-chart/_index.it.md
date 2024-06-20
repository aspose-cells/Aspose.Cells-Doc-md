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

Un PivotChart in Excel è una rappresentazione grafica dei dati creata da una tabella pivot. Consente agli utenti di visualizzare e analizzare dinamicamente i dati riassumendo e visualizzando le informazioni in forma di grafico. I PivotCharts sono interattivi e possono essere facilmente modificati per mostrare diverse prospettive dei dati, rendendoli uno strumento potente per l'analisi e la presentazione dei dati in Excel.

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

