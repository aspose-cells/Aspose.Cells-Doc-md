---
title: Come aggiungere un grafico pivot utilizzando Aspose.Cells
linktitle: Grafico pivot
type: docs
weight: 100
url: /it/net/how-to-add-pivot-chart/
description: Come aggiungere un grafico pivot utilizzando Aspose.Cells.
keywords: PivotChart
---
##  Cos'è il grafico pivot

Un grafico pivot in Excel è una rappresentazione grafica dei dati creati da una tabella pivot. Consente agli utenti di visualizzare e analizzare i dati in modo dinamico riepilogando e visualizzando le informazioni sotto forma di grafico. I grafici pivot sono interattivi e possono essere facilmente modificati per mostrare diverse prospettive dei dati, rendendoli un potente strumento per l'analisi e la presentazione dei dati in Excel.

##  Come aggiungere un grafico pivot utilizzando Aspose.Cells

###  **Aggiunta di una tabella pivot**

Per creare una tabella pivot utilizzando Aspose.Cells:

1. Aggiungi alcuni dati alle celle di un foglio di lavoro utilizzando il metodo PutValue/setValue dell'oggetto Cell. Utilizzi anche un file modello già riempito di dati. I dati verranno utilizzati come origine dati della tabella pivot.
1. Aggiungere una tabella pivot al foglio di lavoro chiamando il metodo add della raccolta PivotTables (incapsulato nell'oggetto Worksheet).
1. Accedi al nuovo oggetto tabella pivot dalla raccolta PivotTables passandone l'indice. # Utilizzare uno qualsiasi degli oggetti tabella pivot incapsulati nell'oggetto Tabella pivot per gestire la tabella.

Di seguito sono riportati esempi di codice.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CreatePivotTablesPivotCharts-CreatePivotTable-1.cs" >}}

###  **Aggiunta di un grafico pivot**

Per creare un grafico pivot utilizzando Aspose.Cells:

1. Aggiungi un grafico.
1. Imposta l'origine pivot del grafico in modo che faccia riferimento a una tabella pivot esistente nel foglio di calcolo.
1. Imposta altri attributi.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CreatePivotTablesPivotCharts-CreatePivotChart-1.cs" >}}

