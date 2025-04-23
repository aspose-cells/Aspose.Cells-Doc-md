---
title: Ottieni il testo dell’equazione della Trendline del grafico con Node.js tramite C++
description: Scopri come utilizzare Aspose.Cells for Node.js via C++ per recuperare il testo dell’equazione di una trendline in un grafico creato in Microsoft Excel. La nostra guida dimostrerà come accedere ed estrarre l’equazione di una trendline per ulteriori analisi o visualizzazione.
keywords: Aspose.Cells for Node.js via C++, Trendline del grafico, Testo dell’equazione, Microsoft Excel, Analisi dei dati, Visualizzazione.
linktitle: Retta di Tendenza
type: docs
weight: 110
url: /it/nodejs-cpp/get-equation-text-of-chart-trendline/
---

{{% alert color="primary" %}}

Puoi recuperare il testo dell’equazione della Trendline del grafico utilizzando Aspose.Cells for Node.js via C++. Aspose.Cells fornisce la proprietà [**DataLabels.getText()**](https://reference.aspose.com/cells/nodejs-cpp/datalabels/#getText--) che restituisce il testo dell’equazione della trendline del grafico. Per utilizzare questa proprietà, devi prima chiamare il metodo [**Chart.calculate()**](https://reference.aspose.com/cells/nodejs-cpp/chart/#calculate--).

{{% /alert %}}

Lo screenshot seguente mostra il grafico con una Trendline e il suo testo dell’equazione mostrato in rosso. Recupereremo questo testo usando la proprietà [**DataLabels.getText()**](https://reference.aspose.com/cells/nodejs-cpp/datalabels/#getText--) nel seguente esempio di codice.

![todo:image_alt_text](get-equation-text-of-chart-trendline_1.png)

## Codice Node.js per ottenere il testo dell'equazione della trendline del grafico

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Create workbook object from source Excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "source.xlsx"));

// Access the first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access the first chart inside the worksheet
const chart = worksheet.getCharts().get(0);

// Calculate the Chart first to get the Equation Text of Trendline
chart.calculate();

// Access the Trendline
const trendLine = chart.getNSeries().get(0).getTrendLines().get(0);

// Read the Equation Text of Trendline
console.log("Equation Text: " + trendLine.getDataLabels().getText());
```

## Output generato dal codice di esempio

Questo è l'output console del codice di esempio precedente.

{{< highlight javascript >}}

Equation Text: y = 8.1333x + 5

{{< /highlight >}}
