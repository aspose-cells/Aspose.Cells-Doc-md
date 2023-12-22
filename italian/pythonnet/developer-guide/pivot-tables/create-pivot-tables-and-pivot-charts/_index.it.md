---
title: Crea tabelle pivot e grafici pivot
type: docs
weight: 20
url: /it/python-net/create-pivot-tables-and-pivot-charts/
description: Come aggiungere tabelle pivot e grafici pivot con Aspose.Cells for Python via .NET.
keywords: Add Pivot Tables and Pivot Charts.
---
{{% alert color="primary" %}}

Una tabella pivot è un riepilogo interattivo di record. Ad esempio, potresti avere centinaia di voci di fattura in un elenco in un foglio di lavoro. Una tabella pivot può totalizzare le fatture per cliente, prodotto o data. Con Microsoft Excel è possibile riorganizzare rapidamente le informazioni nella tabella pivot trascinando i pulsanti in una nuova posizione.

Un grafico pivot è una rappresentazione grafica interattiva dei dati in una tabella pivot. I grafici pivot sono stati introdotti in Excel 2000. L'uso di un grafico pivot rende ancora più semplice la comprensione dei dati poiché la tabella pivot crea automaticamente totali parziali e totali.

 Aspose.Cells for Python via .NET supporti[tabelle pivot](/cells/it/python-net/create-pivot-tables-and-pivot-charts/) E[grafici pivot](/cells/it/python-net/create-pivot-tables-and-pivot-charts/).

{{% /alert %}}

##  **Aggiunta di tabelle e grafici pivot**

Aspose.Cells for Python via .NET fornisce un set speciale di classi utilizzate per creare tabelle pivot. Queste classi vengono utilizzate per creare e impostare oggetti tabella pivot, che fungono da elementi costitutivi di base di un oggetto tabella pivot:

- PivotField, un campo in un rapporto tabella pivot.
- PivotFields, una raccolta di tutti gli oggetti PivotField in una tabella pivot.
- Tabella pivot, un rapporto di tabella pivot su un foglio di lavoro.
- Tabelle pivot, una raccolta di tutti gli oggetti tabella pivot nel foglio di lavoro.

###  **Preparazione all'uso Aspose.Cells for Python via .NET**
1.  Installa Aspose.Cells for Python via .NET da[pipi](https://pypi.org/project/aspose-cells-python/)utilizzare il comando come: $ pip install aspose-cells-python.
1. Puoi anche seguire le istruzioni passo passo su come installare "Aspose.Cells for Python via .NET" nel tuo ambiente di sviluppo.


###  **Aggiunta di una tabella pivot**

Per creare una tabella pivot utilizzando Aspose.Cells for Python via .NET:

1. Aggiungi alcuni dati alle celle di un foglio di lavoro utilizzando il metodo put_value dell'oggetto Cell. Utilizzi anche un file modello già riempito di dati. I dati verranno utilizzati come origine dati della tabella pivot.
1. Aggiungere una tabella pivot al foglio di lavoro chiamando il metodo add della raccolta PivotTables (incapsulato nell'oggetto Worksheet).
1. Accedi al nuovo oggetto tabella pivot dalla raccolta PivotTables passandone l'indice. # Utilizzare uno qualsiasi degli oggetti tabella pivot incapsulati nell'oggetto Tabella pivot per gestire la tabella.

Di seguito sono riportati esempi di codice.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-CreatePivotTablesPivotCharts-CreatePivotTable-1.py" >}}

###  **Aggiunta di un grafico pivot**

Per creare un grafico pivot utilizzando Aspose.Cells for Python via .NET:

1. Aggiungi un grafico.
1. Imposta l'origine pivot del grafico in modo che faccia riferimento a una tabella pivot esistente nel foglio di calcolo.
1. Imposta altri attributi.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-CreatePivotTablesPivotCharts-CreatePivotChart-1.py" >}}

