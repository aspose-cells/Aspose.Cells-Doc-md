---
title: Gestisci i titoli dei grafici di Excel con Node.js via C++
description: Impara come usare Aspose.Cells for Node.js via C++ per aggiungere e formattare i titoli di grafici e assi in Microsoft Excel. La nostra guida dimostrerà come impostare diversi tipi di titoli, regolare il loro aspetto e modificare i titoli degli assi per una migliore rappresentazione e chiarezza dei dati.
keywords: Aspose.Cells for Node.js via C++, Titoli del grafico, Titoli degli assi, Microsoft Excel, Rappresentazione dei dati, Aspetto.
linktitle: Titoli
type: docs
weight: 50
url: /it/nodejs-cpp/chart-and-axis-titles/
---

{{% alert color="primary" %}}

Nei grafici di Excel, ci sono 2 tipi di titoli:
1. Titolo del Grafico 
1. Titoli degli Assi

{{% /alert %}}

## **Opzioni del Titolo**
Aspose.Cells for Node.js via C++ consente anche di gestire i titoli del grafico in fase di esecuzione. Con l’oggetto [Title](https://reference.aspose.com/cells/nodejs-cpp/title/), puoi cambiare testo, font e formato di riempimento per i titoli.

|![todo:image_alt_text](chart_title.png)|

## **Impostare i Titoli dei Grafici o degli Assi**
Puoi usare Microsoft Excel per impostare i titoli di un grafico e dei suoi assi in un ambiente WYSIWYG. Aspose.Cells for Node.js via C++ consente anche agli sviluppatori di impostare i titoli di un grafico e dei suoi assi in fase di esecuzione. Tutti i grafici e i loro assi contengono una proprietà [Title](https://reference.aspose.com/cells/nodejs-cpp/title/) che può essere usata per impostare i loro titoli come mostrato nell’esempio seguente.

Il seguente frammento di codice dimostra come impostare i titoli ai grafici e agli assi.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Adding a new worksheet to the Workbook object
const sheetIndex = workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(sheetIndex);

// Adding sample values to cells
worksheet.getCells().get("A1").putValue(50);
worksheet.getCells().get("A2").putValue(100);
worksheet.getCells().get("A3").putValue(150);
worksheet.getCells().get("B1").putValue(60);
worksheet.getCells().get("B2").putValue(32);
worksheet.getCells().get("B3").putValue(50);

// Adding a chart to the worksheet
const chartIndex = worksheet.getCharts().add(AsposeCells.ChartType.Column, 5, 0, 15, 5);

// Accessing the instance of the newly added chart
const chart = worksheet.getCharts().get(chartIndex);

// Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B3"
chart.getNSeries().add("A1:B3", true);

// Setting the foreground color of the plot area
chart.getPlotArea().getArea().setForegroundColor(AsposeCells.Color.Blue);

// Setting the foreground color of the chart area
chart.getChartArea().getArea().setForegroundColor(AsposeCells.Color.Yellow);

// Setting the foreground color of the 1st SeriesCollection area
chart.getNSeries().get(0).getArea().setForegroundColor(AsposeCells.Color.Red);

// Setting the foreground color of the area of the 1st SeriesCollection point
chart.getNSeries().get(0).getPoints().get(0).getArea().setForegroundColor(AsposeCells.Color.Cyan);

// Filling the area of the 2nd SeriesCollection with a gradient
chart.getNSeries().get(1).getArea().getFillFormat().setOneColorGradient(AsposeCells.Color.Lime, 1, AsposeCells.GradientStyleType.Horizontal, 1);

// Setting the title of a chart
chart.getTitle().setText("Title");

// Setting the font color of the chart title to blue
chart.getTitle().getFont().setColor(AsposeCells.Color.Blue);

// Setting the title of category axis of the chart
chart.getCategoryAxis().getTitle().setText("Category");

// Setting the title of value axis of the chart
chart.getValueAxis().getTitle().setText("Value");

// Saving the Excel file
workbook.save(path.join(dataDir, "book1.out.xls"));
```

## **Argomenti avanzati**
- [Leggi il sottotitolo del grafico dal file ODS](/cells/it/nodejs-cpp/read-chart-subtitle-from-ods-file/)
