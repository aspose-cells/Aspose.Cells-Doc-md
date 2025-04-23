---
title: Manipolare Posizione, Dimensione e Designer del Grafico con Node.js tramite C++
linktitle: Manipolare Posizione, Dimensione e Progettazione del Grafico
description: Impara come usare Aspose.Cells for Node.js via C++ per manipolare efficacemente la posizione, la dimensione e il designer del grafico in Microsoft Excel. La nostra guida mostrerà come regolare queste proprietà per migliorare layout e visualizzazione.
keywords: Aspose.Cells for Node.js via C++, Posizione, Dimensione, Designer del grafico, Microsoft Excel, Layout, Visualizzazione.
type: docs
weight: 45
url: /it/nodejs-cpp/manipulate-position-size-and-designer-chart/
---

## **Posizione e Dimensione del Grafico**
A volte, vuoi cambiare la posizione o la dimensione del nuovo o esistente grafico all’interno del foglio di lavoro. Aspose.Cells fornisce la proprietà [Chart.getChartObject()](https://reference.aspose.com/cells/nodejs-cpp/chart/#getChartObject--) per ottenere questo. Puoi usare le sue sotto-proprietà per ridimensionare il grafico con una nuova altezza e larghezza o riposizionarlo con nuove coordinate X e Y.

### **Controllo Posizione e Dimensione del Grafico**
Per modificare la posizione (coordinate X, Y) o la dimensione (altezza, larghezza) del grafico, utilizzare queste proprietà:

1. [Shape.getX()](https://reference.aspose.com/cells/nodejs-cpp/shape/#getX--)
1. [Shape.getY()](https://reference.aspose.com/cells/nodejs-cpp/shape/#getY--)
1. [Shape.getHeight()](https://reference.aspose.com/cells/nodejs-cpp/shape/#getHeight--)
1. [Shape.getWidth()](https://reference.aspose.com/cells/nodejs-cpp/shape/#getWidth--)

L’esempio seguente spiega l’uso delle API sopra; carica il workbook esistente che contiene un grafico nel suo primo foglio di lavoro. Poi ridimensiona e riposiziona il grafico usando Aspose.Cells.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "chart.xls");

// Loads the workbook which contains the chart
const workbook = new AsposeCells.Workbook(filePath);
const worksheet = workbook.getWorksheets().get(1);

// Load the chart from source worksheet
const chart = worksheet.getCharts().get(0);

// Resize the chart
chart.getChartObject().setWidth(400);
chart.getChartObject().setHeight(300);

// Reposition the chart
chart.getChartObject().setX(250);
chart.getChartObject().setY(150);

// Output the file
workbook.save(path.join(dataDir, "chart.out.xls"));
```

## **Manipolazione dei Grafici del Designer**
Ci sono momenti in cui è necessario manipolare o modificare grafici nei file di modello del designer. Aspose.Cells supporta pienamente la manipolazione dei contenuti e degli elementi del grafico del designer. I dati, i contenuti del grafico, l’immagine di sfondo e la formattazione possono essere preservati con precisione.

### **Manipolazione dei Grafici del Designer nei File di Modello**
Per manipolare i grafici del designer nei file modello, usa l’API relativa ai grafici. Ad esempio, puoi usare la proprietà Worksheet.charts per ottenere la collezione di grafici esistenti nel file del modello.

#### **Creazione di un Grafico**
L'esempio seguente mostra come creare un grafico a piramide. Manipoleremo successivamente questo grafico.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Adding a new worksheet to the Excel object
const sheetIndex = workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(sheetIndex);

// Adding sample values to cells
worksheet.getCells().get("A1").putValue(50);
worksheet.getCells().get("A2").putValue(100);
worksheet.getCells().get("A3").putValue(150);
worksheet.getCells().get("B1").putValue(4);
worksheet.getCells().get("B2").putValue(20);
worksheet.getCells().get("B3").putValue(50);

// Adding a chart to the worksheet
const chartIndex = worksheet.getCharts().add(AsposeCells.ChartType.Pyramid, 5, 0, 15, 5);

// Accessing the instance of the newly added chart
const chart = worksheet.getCharts().get(chartIndex);

// Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B3"
chart.getNSeries().add("A1:B3", true);

// Saving the Excel file
workbook.save(path.join(dataDir, "book1.out.xls"));
```

#### **Manipolazione del Grafico**
L'esempio seguente mostra come manipolare il grafico esistente. In questo esempio, modifichiamo il grafico creato in precedenza. Nell'output generato, si noti che l'etichetta di data di un punto dati è stata impostata su 'Regno Unito, 30K'.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "piechart.xls");

// Loads the existing file.
const workbook = new AsposeCells.Workbook(filePath);

// Get the designer chart in the second sheet.
const sheet = workbook.getWorksheets().get(1);
const chart = sheet.getCharts().get(0);

// Get the data labels in the data series of the third data point.
const dataLabels = chart.getNSeries().get(0).getPoints().get(2).getDataLabels();

// Change the text of the label.
dataLabels.setText("Unided Kingdom, 400K ");

// Save the excel file.
workbook.save(path.join(dataDir, "output.xls"));
```

#### **Manipolazione di un Grafico a Linee nel Modello del Designer**
In questo esempio, manipoleremo un grafico a linee. Aggiungeremo alcune serie di dati al grafico esistente e ne cambieremo i colori delle linee.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Open the existing file.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sample.xlsx"));

// Get the designer chart in the first worksheet.
const chart = workbook.getWorksheets().get(0).getCharts().get(0);

// Add the third data series to it.
chart.getNSeries().add("{60, 80, 10}", true);

// Add another data series (fourth) to it.
chart.getNSeries().add("{0.3, 0.7, 1.2}", true);

// Plot the fourth data series on the second axis.
chart.getNSeries().get(3).setPlotOnSecondAxis(true);

// Change the Border color of the second data series.
chart.getNSeries().get(1).getBorder().setColor(AsposeCells.Color.Green);

// Change the Border color of the third data series.
chart.getNSeries().get(2).getBorder().setColor(AsposeCells.Color.Red);

// Make the second value axis visible.
chart.getSecondValueAxis().setIsVisible(true);

// Save the excel file.
workbook.save(path.join(dataDir, "output.xls"));
```

