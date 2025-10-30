---
title: Ottieni il foglio di lavoro del grafico con Node.js tramite C++
linktitle: Ottieni il foglio di lavoro del grafico
description: Impara come recuperare il foglio di lavoro associato a un grafico Excel usando Aspose.Cells for Node.js via C++. Accedi e manipola i dati sottostanti del grafico in modo efficiente.
keywords: Aspose.Cells per Node.js, grafici Excel, fogli di lavoro, manipolazione dati, dati sottostanti, operazioni, Node.js tramite C++
type: docs
weight: 1000
url: /it/nodejs-cpp/get-worksheet-of-the-chart/
---

{{% alert color="primary" %}}

A volte, potresti voler accedere a un foglio di lavoro da un riferimento di un grafico. Aspose.Cells fornisce la proprietà [**Chart.getWorksheet()**](https://reference.aspose.com/cells/nodejs-cpp/chart/#getWorksheet--) che restituisce il riferimento del foglio di lavoro che contiene il grafico.

{{% /alert %}}

Il seguente esempio mostra come usare la proprietà [**Chart.getWorksheet()**](https://reference.aspose.com/cells/nodejs-cpp/chart/#getWorksheet--). Il codice prima stampa il nome del foglio di lavoro, poi accede al primo grafico nel foglio di lavoro. Quindi stampa di nuovo il nome del foglio di lavoro, usando la proprietà [**Chart.getWorksheet()**](https://reference.aspose.com/cells/nodejs-cpp/chart/#getWorksheet--).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sample.xlsx"));

// Access first worksheet of the workbook
const worksheet = workbook.getWorksheets().get(0);

// Print worksheet name
console.log("Sheet Name: " + worksheet.getName());

// Access the first chart inside this worksheet
const charts = worksheet.getCharts();
if (charts.getCount() > 0) {
const chart = charts.get(0);

// Access the chart's sheet and display its name again
console.log("Chart's Sheet Name: " + chart.getWorksheet().getName());
} else {
console.log("No charts available in the worksheet.");
}
```

Di seguito viene riportato l'output della console che il codice di esempio produce. Come puoi vedere, stampa lo stesso nome del foglio di lavoro entrambe le volte.

{{< highlight javascript >}}

Sheet Name: Portfolio

Chart's Sheet Name: Portfolio

{{< /highlight >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
