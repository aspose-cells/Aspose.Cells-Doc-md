---
title: Come aggiungere un grafico pivot utilizzando Aspose.Cells
linktitle: Grafico pivot
type: docs
weight: 100
url: /it/java/how-to-add-pivot-chart/
description: Come aggiungere un grafico pivot utilizzando Aspose.Cells.
keywords: PivotChart
---
##  Cos'è il grafico pivot

Un grafico pivot in Excel è una rappresentazione grafica dei dati creati da una tabella pivot. Consente agli utenti di visualizzare e analizzare i dati in modo dinamico riepilogando e visualizzando le informazioni sotto forma di grafico. I grafici pivot sono interattivi e possono essere facilmente modificati per mostrare diverse prospettive dei dati, rendendoli un potente strumento per l'analisi e la presentazione dei dati in Excel.

##  Come aggiungere un grafico pivot utilizzando Aspose.Cells
###  **Creazione di una tabella pivot**

Per creare una tabella pivot utilizzando Aspose.Cells:

1. Aggiungi alcuni dati alle celle di un foglio di lavoro utilizzando il metodo PutValue/setValue dell'oggetto Cell. Utilizzi anche un file modello già riempito di dati. I dati verranno utilizzati come origine dati della tabella pivot.
1. Aggiungere una tabella pivot al foglio di lavoro chiamando il metodo add della raccolta PivotTables (incapsulato nell'oggetto Worksheet).
1. Accedi al nuovo oggetto tabella pivot dalla raccolta PivotTables passandone l'indice.
1. Utilizzare uno qualsiasi degli oggetti tabella pivot incapsulati nell'oggetto Tabella pivot per gestire la tabella.

Di seguito è riportato un esempio di codice. L'esecuzione del codice genera un nuovo file: pivotTable_test.xls.

**Dati in ingresso** 

![cose da fare:immagine_alt_testo](create-pivot-tables-and-pivot-charts_1.png)

**La tabella pivot di output**

![cose da fare:immagine_alt_testo](create-pivot-tables-and-pivot-charts_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CreatePivotTable-CreatePivotTable.java" >}}

###  **Creazione di un grafico pivot basato sulla tabella pivot**

Per creare un grafico pivot utilizzando Aspose.Cells:

1. Aggiungi un grafico.
1. Imposta l'origine pivot del grafico in modo che faccia riferimento a una tabella pivot esistente nel foglio di calcolo.
1. Imposta altri attributi.

Di seguito è riportato il codice utilizzato dal componente per eseguire l'attività. L'esecuzione del codice genera un nuovo file: pivotChart_test.xls.

**Il foglio del grafico pivot**

![cose da fare:immagine_alt_testo](create-pivot-tables-and-pivot-charts_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CreatePivotChartbasedonPivotTable-CreatePivotChartbasedonPivotTable.java" >}}

{{% alert color="primary" %}}

Questo articolo mostra come creare tabelle pivot e grafici pivot utilizzando Aspose.Cells. Si spera che ti aiuti a utilizzare queste funzionalità nei tuoi scenari.

Aspose.Cells ha beneficiato di anni di ricerca, progettazione e attenta messa a punto.

 Accogliamo con favore le vostre domande, commenti e suggerimenti su[Aspose.Cells Foro](https://forum.aspose.com/c/cells/9). Garantiamo una pronta risposta.

{{% /alert %}}
