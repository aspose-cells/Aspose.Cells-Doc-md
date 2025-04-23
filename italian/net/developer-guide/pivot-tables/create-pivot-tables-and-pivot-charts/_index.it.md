---
title: Creare Tabelle Pivot e Grafici Pivot
type: docs
weight: 20
url: /it/net/create-pivot-tables-and-pivot-charts/
---

{{% alert color="primary" %}}

Una tabella pivot è un riassunto interattivo di record. Ad esempio, potresti avere centinaia di voci di fattura in un elenco in un foglio di lavoro. Una tabella pivot può totalizzare le fatture per cliente, prodotto o data. Con Microsoft Excel è possibile ridisporre rapidamente le informazioni nella tabella pivot trascinando i pulsanti in una nuova posizione.

Un grafico pivot è una rappresentazione grafica interattiva dei dati in una tabella pivot. I grafici pivot sono stati introdotti in Excel 2000. Utilizzando un grafico pivot è ancora più facile capire i dati poiché la tabella pivot crea automaticamente subtotali e totali.

Aspose.Cells supporta le [tabelle pivot](/cells/it/net/create-pivot-tables-and-pivot-charts/) e i [grafici pivot](/cells/it/net/create-pivot-tables-and-pivot-charts/).

{{% /alert %}}

## **Aggiunta di tabelle pivot e grafici**

Aspose.Cells fornisce un insieme speciale di classi utilizzate per creare tabelle pivot. Queste classi vengono utilizzate per creare e impostare gli oggetti PivotTable, che fungono da blocchi di costruzione di base di un oggetto PivotTable:

- PivotField, un campo in un rapporto di tabella pivot.
- PivotFields, una raccolta di tutti gli oggetti PivotField in una tabella pivot.
- PivotTable, un rapporto di tabella pivot su un foglio di lavoro.
- PivotTables, una raccolta di tutti gli oggetti PivotTable sul foglio di lavoro.

### **Preparazione all'uso di Aspose.Cells**

1. Scarica e installa Aspose.Cells:
   1. [Scarica Aspose.Cells](https://downloads.aspose.com/cells/net).
   1. Installalo sul tuo computer di sviluppo.
      Tutti i componenti [Aspose](http://www.aspose.com/), una volta installati, funzionano in modalità di valutazione. La modalità di valutazione non ha limiti di tempo e inserisce solo watermark nei documenti prodotti. Per utilizzare il componente a piena capacità, è necessario disporre di una licenza valida.
1. Crea un progetto:
   1. Avviare Visual Studio.Net.
   1. Crea una nuova applicazione console.
1. Aggiungi riferimenti:
   Aggiungi un riferimento al componente Aspose.Cells nel tuo progetto, ad esempio ...\Program Files\Aspose\Aspose.Cells\Bin\Net1.0\Aspose.Cells.dll

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
