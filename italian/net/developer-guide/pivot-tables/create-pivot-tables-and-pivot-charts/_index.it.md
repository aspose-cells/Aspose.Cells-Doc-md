---
title: Crea tabelle pivot e grafici pivot
type: docs
weight: 20
url: /it/net/create-pivot-tables-and-pivot-charts/
---
{{% alert color="primary" %}}

Una tabella pivot è un riepilogo interattivo dei record. Ad esempio, potresti avere centinaia di voci di fattura in un elenco in un foglio di lavoro. Una tabella pivot può sommare le fatture per cliente, prodotto o data. Con Microsoft Excel è possibile riorganizzare rapidamente le informazioni nella tabella pivot trascinando i pulsanti in una nuova posizione.

Un grafico pivot è una rappresentazione grafica interattiva dei dati in una tabella pivot. I grafici pivot sono stati introdotti in Excel 2000. L'utilizzo di un grafico pivot rende ancora più semplice la comprensione dei dati poiché la tabella pivot crea automaticamente subtotali e totali.

 Aspose.Cells supporti[tabelle pivot](/cells/it/net/create-pivot-tables-and-pivot-charts/) e[grafici pivot](/cells/it/net/create-pivot-tables-and-pivot-charts/).

{{% /alert %}}

## **Aggiunta di tabelle pivot e grafici**

Aspose.Cells fornisce un insieme speciale di classi utilizzate per creare tabelle pivot. Queste classi vengono utilizzate per creare e impostare oggetti PivotTable, che fungono da elementi costitutivi di base di un oggetto PivotTable:

- PivotField, un campo in un rapporto tabella pivot.
- PivotFields, una raccolta di tutti gli oggetti PivotField in una tabella pivot.
- Tabella pivot, un rapporto di tabella pivot su un foglio di lavoro.
- Tabelle pivot, una raccolta di tutti gli oggetti tabella pivot nel foglio di lavoro.

### **Preparazione all'uso Aspose.Cells**

1. Scarica e installa Aspose.Cells:
   1. [Scarica Aspose.Cells](https://downloads.aspose.com/cells/net).
 1. Installalo sul tuo computer di sviluppo.
 Tutto[Aspose](http://www.aspose.com/) i componenti, una volta installati, funzionano in modalità di valutazione. La modalità di valutazione non ha limiti di tempo e si limita a inserire filigrane nei documenti prodotti. Per lavorare con il componente nella sua piena capacità è necessario disporre di una licenza valida.
1. Crea un progetto:
 1. Avviare Visual Studio.Net.
 1. Creare una nuova applicazione console.
1. Aggiungi riferimenti:
 Aggiungere un riferimento al componente Aspose.Cells nel progetto, ad esempio ...\Program Files\Aspose\Aspose.Cells\Bin\Net1.0\Aspose.Cells.dll

### **Aggiunta di una tabella pivot**

Per creare una tabella pivot utilizzando Aspose.Cells:

1. Aggiungere alcuni dati alle celle di un foglio di lavoro utilizzando il metodo PutValue/setValue di un oggetto Cell. Si utilizza anche un file modello già riempito di dati. I dati verranno utilizzati come origine dati della tabella pivot.
1. Aggiungi una tabella pivot al foglio di lavoro chiamando il metodo add della raccolta di tabelle pivot (incapsulato nell'oggetto Worksheet).
1. Accedi al nuovo oggetto PivotTable dalla raccolta PivotTables passandone l'indice. # Utilizzare uno qualsiasi degli oggetti tabella pivot incapsulati nell'oggetto PivotTable per gestire la tabella.

Esempi di codice sono riportati di seguito.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CreatePivotTablesPivotCharts-CreatePivotTable-1.cs" >}}

### **Aggiunta di un grafico pivot**

Per creare un grafico pivot utilizzando Aspose.Cells:

1. Aggiungi un grafico.
1. Impostare PivotSource del grafico in modo che faccia riferimento a una tabella pivot esistente nel foglio di calcolo.
1. Imposta altri attributi.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CreatePivotTablesPivotCharts-CreatePivotChart-1.cs" >}}

