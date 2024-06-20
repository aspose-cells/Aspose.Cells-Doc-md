---
title: Creare Tabelle Pivot e Grafici Pivot
type: docs
weight: 20
url: /it/python-net/create-pivot-tables-and-pivot-charts/
description: Come aggiungere Tabelle Pivot e Grafici Pivot con Aspose.Cells per Python via .NET.
keywords: Aspose.Cells per Python Excel, Libreria Excel Python, Aggiungi Tabelle Pivot e Grafici Pivot Utilizzando Aspose.Cells per Python Libreria Excel.
---

{{% alert color="primary" %}}

Una tabella pivot è un riassunto interattivo di record. Ad esempio, potresti avere centinaia di voci di fattura in un elenco in un foglio di lavoro. Una tabella pivot può totalizzare le fatture per cliente, prodotto o data. Con Microsoft Excel è possibile ridisporre rapidamente le informazioni nella tabella pivot trascinando i pulsanti in una nuova posizione.

Un grafico pivot è una rappresentazione grafica interattiva dei dati in una tabella pivot. I grafici pivot sono stati introdotti in Excel 2000. Utilizzando un grafico pivot è ancora più facile capire i dati poiché la tabella pivot crea automaticamente subtotali e totali.

Aspose.Cells per Python via .NET supporta [tabelle pivot](/cells/it/python-net/create-pivot-tables-and-pivot-charts/) e [grafici pivot](/cells/it/python-net/create-pivot-tables-and-pivot-charts/).

{{% /alert %}}

## **Aggiungi Tabelle Pivot e Grafici Utilizzando Aspose.Cells per Python Libreria Excel**

Aspose.Cells per Python via .NET fornisce un insieme speciale di classi utilizzate per creare tabelle pivot. Queste classi vengono utilizzate per creare e impostare oggetti PivotTable, che agiscono come blocchi di base dell'oggetto PivotTable:

- PivotField, un campo in un rapporto di tabella pivot.
- PivotFields, una raccolta di tutti gli oggetti PivotField in una tabella pivot.
- PivotTable, un rapporto di tabella pivot su un foglio di lavoro.
- PivotTables, una raccolta di tutti gli oggetti PivotTable sul foglio di lavoro.

### **Prepararsi a utilizzare Aspose.Cells per Python via .NET**
1. Installa Aspose.Cells per Python via .NET da [pypi](https://pypi.org/project/aspose-cells-python/), utilizza il comando come: $ pip install aspose-cells-python.
1. Puoi anche seguire le istruzioni passo-passo su come installare “Aspose.Cells per Python via .NET” nel tuo ambiente di sviluppo.


### **Come Aggiungere una Tabella Pivot Utilizzando la Libreria Excel di Aspose.Cells per Python**

Per creare una tabella pivot utilizzando Aspose.Cells per Python via .NET:

1. Aggiungi alcuni dati alle celle di un foglio di lavoro utilizzando il metodo put_value di un oggetto Cell. Puoi anche utilizzare un file modello già compilato con dati. I dati verranno utilizzati come origine dati della tabella pivot.
1. Aggiungi una tabella pivot al foglio di lavoro chiamando il metodo add della collezione PivotTables (incapsulato nell'oggetto Worksheet).
1. Accedi al nuovo oggetto PivotTable dalla collezione PivotTables passando il suo indice. # Usa uno qualsiasi degli oggetti tabella pivot incapsulati nell'oggetto PivotTable per gestire la tabella.

Di seguito sono riportati esempi di codice.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-CreatePivotTablesPivotCharts-CreatePivotTable-1.py" >}}

### **Come Aggiungere un Grafico Pivot Utilizzando la Libreria Excel di Aspose.Cells per Python**

Per creare un PivotChart utilizzando Aspose.Cells per Python via .NET:

1. Aggiungi un grafico.
1. Imposta il PivotSource del grafico per fare riferimento a una tabella pivot esistente nel foglio di calcolo.
1. Imposta altri attributi.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-CreatePivotTablesPivotCharts-CreatePivotChart-1.py" >}}

