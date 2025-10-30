---
title: Crea tabelle pivot e grafici pivot con Golang tramite C++
linktitle: Creare Tabelle Pivot e Grafici Pivot
type: docs
weight: 20
url: /it/go-cpp/create-pivot-tables-and-pivot-charts/
description: Impara come creare tabelle pivot e grafici pivot in file Excel utilizzando Aspose.Cells con Golang tramite C++.
---

{{% alert color="primary" %}}

Una tabella pivot è un riepilogo interattivo dei record. Per esempio, puoi avere centinaia di voci di fatture in un elenco in un foglio di lavoro. Una tabella pivot può totalizzare le fatture per cliente, prodotto o data. Con Microsoft Excel, è possibile riorganizzare rapidamente le informazioni nella tabella pivot trascinando i pulsanti in una nuova posizione.

Un grafico pivot è una rappresentazione grafica interattiva dei dati in una tabella pivot. I grafici pivot sono stati introdotti in Excel 2000. Utilizzando un grafico pivot è ancora più facile capire i dati poiché la tabella pivot crea automaticamente subtotali e totali.

Aspose.Cells supporta [tabelle pivot](/cells/it/cpp/create-pivot-tables-and-pivot-charts/) e [grafici pivot](/cells/it/cpp/create-pivot-tables-and-pivot-charts/).

{{% /alert %}}

## **Aggiunta di tabelle pivot e grafici**

Aspose.Cells fornisce un insieme speciale di classi utilizzate per creare tabelle pivot. Queste classi vengono utilizzate per creare e impostare gli oggetti PivotTable, che fungono da blocchi di costruzione di base di un oggetto PivotTable:

- **PivotField**, un campo in un rapporto di tabella pivot.
- **PivotFields**, una collezione di tutti gli oggetti PivotField in una tabella pivot.
- **PivotTable**, un rapporto PivotTable su un foglio di lavoro.
- **PivotTables**, una collezione di tutti gli oggetti PivotTable sul foglio di lavoro.

### **Preparazione all'uso di Aspose.Cells**

1. Scarica e installa Aspose.Cells:
   1. [Scarica Aspose.Cells](https://downloads.aspose.com/cells/go-cpp/).
   1. Installalo sul tuo computer di sviluppo.
      Tutti i componenti [Aspose](http://www.aspose.com/), una volta installati, funzionano in modalità di valutazione. La modalità di valutazione non ha limiti di tempo e inserisce soltanto filigrane nei documenti prodotti. Per lavorare con il componente in modo completo, è necessario avere una licenza valida.
1. Crea un progetto:
   1. Avvia il tuo IDE C++ (ad esempio Visual Studio).
   1. Crea una nuova applicazione console.
1. Aggiungi riferimenti:
   Aggiungi un riferimento al componente Aspose.Cells nel tuo progetto, ad esempio, `...\Program Files\Aspose\Aspose.Cells\Bin\Net1.0\Aspose.Cells.dll`.

### **Aggiunta di una tabella pivot**

Per creare una tabella pivot utilizzando Aspose.Cells:

1. Aggiungi alcuni dati alle celle di un foglio di lavoro usando il metodo `PutValue` di un oggetto `Cell`. Puoi anche usare un file modello già compilato con dati. I dati verranno usati come origine dati della tabella pivot.
1. Aggiungi una tabella pivot al foglio di lavoro chiamando il metodo `Add` della collezione `PivotTables` (racchiuso nell'oggetto `Worksheet`).
1. Accedi al nuovo oggetto `PivotTable` dalla collezione `PivotTables` passando il suo indice. Usa uno qualsiasi degli oggetti tabella pivot racchiusi nell'oggetto `PivotTable` per gestire la tabella.

Di seguito sono riportati esempi di codice.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CreatePivotTablesAndPivotCharts.go" >}}
### **Aggiunta di un grafico pivot**

Per creare un PivotChart utilizzando Aspose.Cells:

1. Aggiungi un grafico.
1. Imposta il `PivotSource` del grafico per fare riferimento a una tabella pivot esistente nel foglio di calcolo.
1. Imposta altri attributi.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CreatePivotTablesAndPivotCharts-1.go" >}}
