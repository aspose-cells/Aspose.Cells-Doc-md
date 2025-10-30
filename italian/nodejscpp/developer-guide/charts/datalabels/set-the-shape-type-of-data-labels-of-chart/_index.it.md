---
title: Imposta il tipo di forma delle Etichette dati del grafico con Node.js via C++
linktitle: Imposta il tipo di forma dell etichetta dati del grafico
description: Impara come impostare il tipo di forma delle etichette dei dati nei grafici utilizzando Aspose.Cells for Node.js via C++. Questa guida spiegherà i diversi tipi di forma disponibili e ti mostrerà come scegliere la forma appropriata per le tue etichette dei dati per migliorare la presentazione e l usabilità.
keywords: Aspose.Cells for Node.js via C++, creazione di grafici, etichette dati, tipi di forma, presentazione, usabilità.
type: docs
weight: 110
url: /it/nodejs-cpp/set-the-shape-type-of-data-labels-of-chart/
---

## **Possibili Scenari di Utilizzo**
Puoi cambiare il tipo di forma delle etichette dei dati del grafico usando la proprietà `DataLabels.shapeType`. Essa accetta il valore dell'enumerazione `DataLabelShapeType` e modifica di conseguenza il tipo di forma delle etichette dei dati. Alcuni dei suoi valori sono

{{< highlight javascript >}}
 DataLabelShapeType.BentLineCallout
DataLabelShapeType.DownArrowCallout
DataLabelShapeType.Ellipse
DataLabelShapeType.LineCallout
DataLabelShapeType.Rect
etc.
{{< /highlight >}}

## **Imposta il tipo di forma delle etichette dati del grafico**
Il seguente esempio di codice cambia il tipo di forma delle etichette dei dati del grafico in `DataLabelShapeType.WedgeEllipseCallout`. Consulta il [file Excel di esempio](60489778.xlsx) utilizzato in questo codice e il [file Excel di output](60489779.xlsx) generato. Lo screenshot mostra l'effetto del codice sul file Excel di esempio.

![todo:image_alt_text](set-the-shape-type-of-data-labels-of-chart_1.png)
## **Codice di Esempio**
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleSetShapeTypeOfDataLabelsOfChart.xlsx");

// Load source Excel file
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access first chart
const chart = worksheet.getCharts().get(0);

// Access first series
const series = chart.getNSeries().get(0);

// Set the shape type of data labels i.e. Speech Bubble Oval
series.getDataLabels().setShapeType(AsposeCells.DataLabelShapeType.WedgeEllipseCallout);

// Save the output Excel file
workbook.save(path.join(dataDir, "outputSetShapeTypeOfDataLabelsOfChart.xlsx"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
