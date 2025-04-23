---
title: Creare Tabelle Pivot e Grafici Pivot
type: docs
weight: 20
url: /it/nodejs-cpp/create-pivot-tables-and-pivot-charts/
description: Come aggiungere tabelle pivot e grafici pivot con Aspose.Cells for Node.js via C++.
keywords: Aspose.Cells for Node.js via C++ Excel, libreria Excel Node.js, aggiungi tabelle pivot e grafici pivot usando la libreria Excel Aspose.Cells for Node.js via C++.
---

{{% alert color="primary" %}}

Una tabella pivot è un riassunto interattivo di record. Ad esempio, potresti avere centinaia di voci di fattura in un elenco in un foglio di lavoro. Una tabella pivot può totalizzare le fatture per cliente, prodotto o data. Con Microsoft Excel è possibile ridisporre rapidamente le informazioni nella tabella pivot trascinando i pulsanti in una nuova posizione.

Un grafico pivot è una rappresentazione grafica interattiva dei dati in una tabella pivot. I grafici pivot sono stati introdotti in Excel 2000. Utilizzando un grafico pivot è ancora più facile capire i dati poiché la tabella pivot crea automaticamente subtotali e totali.

Aspose.Cells for Node.js via C++ supporta [tabelle pivot](/cells/it/nodejs-cpp/create-pivot-tables-and-pivot-charts/) e [grafici pivot](/cells/it/nodejs-cpp/create-pivot-tables-and-pivot-charts/).

{{% /alert %}}

## **Aggiungi tabelle pivot e grafici usando Aspose.Cells for Node.js via C++**

Aspose.Cells for Node.js via C++ fornisce un insieme speciale di classi usate per creare tabelle pivot. Queste classi sono utilizzate per creare e impostare oggetti PivotTable, che fungono da blocchi di costruzione di base per un oggetto PivotTable:

- PivotField, un campo in un rapporto di tabella pivot.
- PivotFields, una raccolta di tutti gli oggetti PivotField in una tabella pivot.
- PivotTable, un rapporto di tabella pivot su un foglio di lavoro.
- PivotTables, una raccolta di tutti gli oggetti PivotTable sul foglio di lavoro.

### **Prepararsi a usare Aspose.Cells for Node.js via C++**
1. Installa Aspose.Cells for Node.js via C++ da NPM, usa il comando: $ npm install aspose.cells.node.
1. Puoi anche seguire le istruzioni passo passo su come installare “Aspose.Cells for Node.js via C++” nel tuo ambiente di sviluppo.


### **Come aggiungere una tabella pivot usando Aspose.Cells for Node.js via C++**

Per creare una tabella pivot usando Aspose.Cells for Node.js via C++:

1. Aggiungi alcuni dati alle celle di un foglio di lavoro utilizzando il metodo put_value di un oggetto Cell. Puoi anche utilizzare un file modello già compilato con dati. I dati verranno utilizzati come origine dati della tabella pivot.
1. Aggiungi una tabella pivot al foglio di lavoro chiamando il metodo add della collezione PivotTables (incapsulato nell'oggetto Worksheet).
1. Accedi al nuovo oggetto PivotTable dalla collezione PivotTables passando il suo indice. # Usa uno qualsiasi degli oggetti tabella pivot incapsulati nell'oggetto PivotTable per gestire la tabella.

Di seguito sono riportati esempi di codice.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-CreatePivotTablesPivotCharts-CreatePivotTable-1.js" >}}

### **Come aggiungere un grafico pivot usando la libreria Aspose.Cells for Node.js via C++**

Per creare un PivotChart usando Aspose.Cells for Node.js via C++:

1. Aggiungi un grafico.
1. Imposta il PivotSource del grafico per fare riferimento a una tabella pivot esistente nel foglio di calcolo.
1. Imposta altri attributi.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-CreatePivotTablesPivotCharts-CreatePivotChart-1.js" >}}

