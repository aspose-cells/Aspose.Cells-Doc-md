---
title: Creare Tabelle Pivot e Grafici Pivot
type: docs
weight: 10
url: /it/java/create-pivot-tables-and-pivot-charts/
description: Crea tabelle pivot e grafici pivot con Aspose.Cells for Java API.
keywords: excel crea tabella pivot java, excel crea grafico pivot java, excel crea tabella pivot e grafico pivot java, crea tabella pivot excel java, crea grafico pivot excel java, crea tabella pivot excel e grafico pivot java, java crea tabella pivot excel e grafico pivot, come creare tabella pivot excel e grafico pivot java
---

{{% alert color="primary" %}}

Una tabella pivot è un riassunto interattivo di record. Ad esempio, potresti avere centinaia di voci di fattura in un elenco in un foglio di lavoro. Una tabella pivot può totalizzare le fatture per cliente, prodotto o data. Con Microsoft Excel è possibile ridisporre rapidamente le informazioni nella tabella pivot trascinando i pulsanti in una nuova posizione.

Un grafico pivot è una rappresentazione grafica interattiva dei dati in una tabella pivot. I grafici pivot sono stati introdotti in Excel 2000. Utilizzando un grafico pivot è ancora più facile capire i dati poiché la tabella pivot crea automaticamente subtotali e totali.

Aspose.Cells supporta [tabelle pivot](/cells/it/java/create-pivot-tables-and-pivot-charts/#creating-a-pivot-table) e [grafici pivot](/cells/it/java/create-pivot-tables-and-pivot-charts/#creating-a-pivot-chart-based-on-the-pivot-table).

{{% /alert %}}

## **Aggiunta di tabelle pivot e grafici**

Aspose.Cells fornisce un insieme speciale di classi utilizzate per creare tabelle pivot. Queste classi vengono utilizzate per creare e impostare gli oggetti PivotTable, che fungono da blocchi di costruzione di base di un oggetto PivotTable:

- PivotField, un campo in un rapporto di tabella pivot.
- PivotFields, una raccolta di tutti gli oggetti PivotField in una tabella pivot.
- PivotTable, un rapporto di tabella pivot su un foglio di lavoro.
- PivotTables, una raccolta di tutti gli oggetti PivotTable sul foglio di lavoro.

### **Preparazione all'uso di Aspose.Cells**

1. Scarica e installa Aspose.Cells.Zip:
   1. [Scarica Aspose.Cells for Java](https://downloads.aspose.com/cells/java).
   1. Estrarlo sul tuo computer di sviluppo.
      Tutti i componenti [Aspose](http://www.aspose.com/), una volta installati, funzionano in modalità di valutazione. La modalità di valutazione non ha limiti di tempo e inserisce solo filigrane nei documenti prodotti.
1. Crea un progetto
   1. È possibile creare un progetto utilizzando un Editor Java come Eclipse o creare un semplice programma utilizzando il Blocco note.
1. Aggiungi percorso della classe:
   Per impostare un percorso di classe utilizzando Eclipse:
   1. Estrai Aspose.Cells.jar e dom4j_1.6.1.jar da Aspose.Cells.zip.
   1. Imposta il percorso di classe del progetto in Eclipse:
   1. Seleziona il tuo progetto in Eclipse e poi fai clic sui menu Project-Properties.
   1. Seleziona "Percorso di compilazione Java" sul lato sinistro della finestra popup, poi seleziona la scheda "Librerie", clicca su "Aggiungi JAR" o "Aggiungi JAR Esterno" per selezionare Aspose.Cells.jar e dom4j_1.6.1.jar e aggiungerli ai percorsi di compilazione.
   1. Scrivi un'applicazione per invocare le API dei componenti di Aspose.
      Oppure puoi impostarlo in fase di esecuzione al prompt dei comandi di Windows.

{{< highlight java >}}

 javac \-classpath %classpath%;e:\Aspose.Cells.jar; ClassName .javajava \-classpath %classpath%;e:\Aspose.Cells.jar; ClassName 

{{< /highlight >}}

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

## Articoli correlati

- [Ordinamento personalizzato in tabella pivot](/cells/it/java/custom-sorting-in-pivot-table/)
- [Formattazione tabella pivot](/cells/it/java/formatting-pivot-table/)
- [Aggiornare e calcolare la tabella pivot con elementi calcolati](/cells/it/java/refresh-and-calculate-pivot-table-having-calculated-items/)
- [Disabilita i riquadri delle tabelle pivot](/cells/it/java/disable-pivot-table-ribbons/)

