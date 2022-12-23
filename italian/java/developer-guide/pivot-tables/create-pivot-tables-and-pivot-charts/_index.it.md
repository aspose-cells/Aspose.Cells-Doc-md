---
title: Crea tabelle pivot e grafici pivot
type: docs
weight: 10
url: /it/java/create-pivot-tables-and-pivot-charts/
description: Crea tabelle pivot e grafici pivot con Aspose.Cells for Java API.
keywords: excel create pivot table java, excel create pivot chart java, excel create pivot table and pivot chart java, create excel pivot table java, create excel pivot chart java, create excel pivot table and pivot chart java, java create excel pivot table and pivot chart, how to create excel pivot table and pivot chart java
---
{{% alert color="primary" %}}

Una tabella pivot è un riepilogo interattivo dei record. Ad esempio, potresti avere centinaia di voci di fattura in un elenco in un foglio di lavoro. Una tabella pivot può sommare le fatture per cliente, prodotto o data. Con Microsoft Excel è possibile riorganizzare rapidamente le informazioni nella tabella pivot trascinando i pulsanti in una nuova posizione.

Un grafico pivot è una rappresentazione grafica interattiva dei dati in una tabella pivot. I grafici pivot sono stati introdotti in Excel 2000. L'utilizzo di un grafico pivot rende ancora più semplice la comprensione dei dati poiché la tabella pivot crea automaticamente subtotali e totali.

 Aspose.Cells supporti[tabelle pivot](/cells/it/java/create-pivot-tables-and-pivot-charts/#creating-a-pivot-table) e[grafici pivot](/cells/it/java/create-pivot-tables-and-pivot-charts/#creating-a-pivot-chart-based-on-the-pivot-table).

{{% /alert %}}

## **Aggiunta di tabelle pivot e grafici**

Aspose.Cells fornisce un insieme speciale di classi utilizzate per creare tabelle pivot. Queste classi vengono utilizzate per creare e impostare oggetti PivotTable, che fungono da elementi costitutivi di base di un oggetto PivotTable:

- PivotField, un campo in un rapporto tabella pivot.
- PivotFields, una raccolta di tutti gli oggetti PivotField in una tabella pivot.
- Tabella pivot, un rapporto di tabella pivot su un foglio di lavoro.
- Tabelle pivot, una raccolta di tutti gli oggetti tabella pivot nel foglio di lavoro.

### **Preparazione all'uso Aspose.Cells**

1. Scarica e installa Aspose.Cells.Zip:
   1. [Scarica Aspose.Cells for Java](https://downloads.aspose.com/cells/java).
 1. Decomprimilo sul tuo computer di sviluppo.
 Tutti[Aspose](http://www.aspose.com/) i componenti, una volta installati, funzionano in modalità di valutazione. La modalità di valutazione non ha limiti di tempo e si limita a inserire filigrane nei documenti prodotti.
1. Crea un progetto
 1. È possibile creare un progetto utilizzando un editor Java, ad esempio Eclipse, o creare un semplice programma utilizzando un blocco note.
1. Aggiungi percorso di classe:
 Per impostare un percorso di classe utilizzando Eclipse:
1. Estrarre Aspose.Cells.jar e dom4j_1.6.1.jar da Aspose.Cells.zip.
 1. Imposta il classpath del progetto in Eclipse:
1. Selezionare il progetto in Eclipse e quindi fare clic sui menu Project-Properties.
 1. Selezionare "Java Build Path" nella parte sinistra della finestra popup, quindi selezionare la scheda "Librerie", fare clic su "Aggiungi JAR" o "Aggiungi JAR esterni" per selezionare Aspose.Cells.jar e dom4j_1.6.1.jar e aggiungerli nei percorsi di costruzione.
 1. Scrivere un'applicazione per richiamare le API dei componenti di Aspose.
 Oppure puoi impostarlo in fase di esecuzione al prompt di dos in Windows.

{{< highlight "java" >}}

 javac \-classpath %classpath%;e:\Aspose.Cells.jar; ClassName .javajava \-classpath %classpath%;e:\Aspose.Cells.jar; ClassName 

{{< /highlight >}}

### **Creazione di una tabella pivot**

Per creare una tabella pivot utilizzando Aspose.Cells:

1. Aggiungere alcuni dati alle celle di un foglio di lavoro utilizzando il metodo PutValue/setValue di un oggetto Cell. Si utilizza anche un file modello già riempito di dati. I dati verranno utilizzati come origine dati della tabella pivot.
1. Aggiungi una tabella pivot al foglio di lavoro chiamando il metodo add della raccolta di tabelle pivot (incapsulato nell'oggetto Worksheet).
1. Accedi al nuovo oggetto PivotTable dalla raccolta PivotTables passandone l'indice.
1. Utilizzare uno qualsiasi degli oggetti tabella pivot incapsulati nell'oggetto tabella pivot per gestire la tabella.

Di seguito viene fornito un esempio di codice. L'esecuzione del codice genera un nuovo file: pivotTable_test.xls.

**Dati in ingresso** 

![cose da fare:immagine_alt_testo](create-pivot-tables-and-pivot-charts_1.png)

**La tabella pivot di output**

![cose da fare:immagine_alt_testo](create-pivot-tables-and-pivot-charts_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CreatePivotTable-CreatePivotTable.java" >}}

### **Creazione di un grafico pivot basato sulla tabella pivot**

Per creare un grafico pivot utilizzando Aspose.Cells:

1. Aggiungi un grafico.
1. Impostare PivotSource del grafico in modo che faccia riferimento a una tabella pivot esistente nel foglio di calcolo.
1. Imposta altri attributi.

Di seguito è riportato il codice utilizzato dal componente per eseguire l'attività. L'esecuzione del codice genera un nuovo file: pivotChart_test.xls.

**Il foglio del grafico pivot**

![cose da fare:immagine_alt_testo](create-pivot-tables-and-pivot-charts_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CreatePivotChartbasedonPivotTable-CreatePivotChartbasedonPivotTable.java" >}}

{{% alert color="primary" %}}

Questo articolo mostra come creare tabelle pivot e grafici pivot utilizzando Aspose.Cells. Si spera che ti aiuti a utilizzare queste funzionalità nei tuoi scenari.

Aspose.Cells ha beneficiato di anni di ricerca, progettazione e attenta messa a punto.

 Accogliamo con favore le vostre domande, commenti e suggerimenti a[Aspose.Cells Foro](https://forum.aspose.com/c/cells/9). Garantiamo una pronta risposta.

{{% /alert %}}

## articoli Correlati

- [Ordinamento personalizzato nella tabella pivot](/cells/it/java/custom-sorting-in-pivot-table/)
- [Formattazione della tabella pivot](/cells/it/java/formatting-pivot-table/)
- [Aggiorna e calcola la tabella pivot con elementi calcolati](/cells/it/java/refresh-and-calculate-pivot-table-having-calculated-items/)
- [Disattiva i nastri della tabella pivot](/cells/it/java/disable-pivot-table-ribbons/)

