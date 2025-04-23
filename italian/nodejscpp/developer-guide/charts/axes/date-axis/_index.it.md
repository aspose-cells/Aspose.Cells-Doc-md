---
title: Asse delle date con Node.js tramite C++
description: Impara come gestire l asse delle date in Aspose.Cells for Node.js via C++. La nostra guida ti aiuterà a capire come lavorare con vari formati di data, scale temporali e frequenze delle etichette dei tick.
keywords: Aspose.Cells per Node.js, asse dell asse, gestione, formati di data, scale temporali, frequenza delle etichette degli tick.
type: docs
weight: 200
url: /it/nodejs-cpp/date-axis/
---

## **Possibili Scenari di Utilizzo**
Quando crei un grafico dai dati di un foglio di lavoro che utilizzano date, e le date sono rappresentate lungo l'asse orizzontale (categoria) nel grafico, Aspose.Cells for Node.js via C++ cambia automaticamente l'asse delle categorie in un asse di data (scale temporali).
Un asse data visualizza le date in ordine cronologico a intervalli o unità di base specifici, come il numero di giorni, mesi o anni, anche se le date sul foglio di lavoro non sono in ordine sequenziale o nelle stesse unità di base.
Per impostazione predefinita, Aspose.Cells determina le unità di base per l'asse delle date in base alla minima differenza tra due date nei dati del foglio di lavoro. Ad esempio, se hai dati sui prezzi delle azioni dove la differenza più piccola tra le date è di sette giorni, Excel imposta l'unità di base in giorni, ma puoi modificarla in mesi o anni se desideri vedere l'andamento delle azioni su un periodo più lungo.

## **Gestire l'Asse Data come Microsoft Excel**
Vedi il seguente esempio di codice che crea un nuovo file Excel e inserisce i valori del grafico nel primo foglio di lavoro. 
Poi aggiungiamo un grafico e impostiamo il tipo del [**Axis**](https://reference.aspose.com/cells/nodejs-cpp/axis/) 
a [**Axis.getCategoryType()**](https://reference.aspose.com/cells/nodejs-cpp/axis/#getCategoryType--) e quindi impostiamo le unità di base su Giorni.

![todo:image_alt_text](excel.png)

## **Codice di Esempio**
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);
// Get the first worksheet
const worksheet = workbook.getWorksheets().get(0);
// Add the sample values to cells
worksheet.getCells().get("A1").putValue("Date");
// 14 means datetime format
const style = worksheet.getCells().getStyle();
style.setNumber(14);
// Put values to cells for creating chart
worksheet.getCells().get("A2").setStyle(style);
worksheet.getCells().get("A2").putValue(new Date(Date.UTC(2022, 5, 26)));
worksheet.getCells().get("A3").setStyle(style);
worksheet.getCells().get("A3").putValue(new Date(Date.UTC(2022, 4, 22)));
worksheet.getCells().get("A4").setStyle(style);
worksheet.getCells().get("A4").putValue(new Date(Date.UTC(2022, 7, 3)));
worksheet.getCells().get("B1").putValue("Price");
worksheet.getCells().get("B2").putValue(40);
worksheet.getCells().get("B3").putValue(50);
worksheet.getCells().get("B4").putValue(60);
// Add a chart to the worksheet
const chartIndex = worksheet.getCharts().add(AsposeCells.ChartType.Column, 9, 6, 21, 13);
// Access the instance of the newly added chart
const chart = worksheet.getCharts().get(chartIndex);
// Add SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B4"
chart.setChartDataRange("A1:B4", true);         
// Set the Axis type to Date time
chart.getCategoryAxis().setCategoryType(AsposeCells.CategoryType.TimeScale);
// Set the base unit for CategoryAxis to days
chart.getCategoryAxis().setBaseUnitScale(AsposeCells.TimeUnit.Days);
// Set the direction for the axis text to be vertical
chart.getCategoryAxis().getTickLabels().setDirectionType(AsposeCells.ChartTextDirectionType.Vertical);
// Fill the PlotArea area with nothing 
chart.getPlotArea().getArea().getFillFormat().setFillType(AsposeCells.FillType.None);
// Set max value of Y axis.
chart.getValueAxis().setMaxValue(70);
// Set major unit.
chart.getValueAxis().setMajorUnit(10);
// Save the file
workbook.save("DateAxis.xlsx");
```
