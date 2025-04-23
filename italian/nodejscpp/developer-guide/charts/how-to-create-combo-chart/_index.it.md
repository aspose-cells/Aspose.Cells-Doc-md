---
title: Come creare un grafico combinato con Node.js tramite C++
linktitle: Come creare un grafico Combo
description: Impara come creare un grafico combinato usando Aspose.Cells for Node.js via C++. La nostra guida completa dimostrerà come combinare diversi tipi di grafici in un unico grafico combinato per una presentazione dei dati più efficace.
keywords: Aspose.Cells for Node.js via C++, Grafico combinato, Combinare tipi di grafico, Presentazione dei dati, Visualizzazione efficace.
type: docs
weight: 73
url: /it/nodejs-cpp/create-combo-chart/
---

## **Possibili Scenari di Utilizzo**
I grafici Combo in Excel ti permettono di usufruire di questa opzione poiché puoi facilmente combinare due o più tipi di grafico per rendere i tuoi dati comprensibili. I grafici Combo sono utili quando i tuoi dati contengono molteplici tipologie di valori, inclusi prezzo e volume. Inoltre, i grafici Combo sono fattibili quando i numeri dei tuoi dati cambiano ampiamente da serie a serie.
Prendendo il seguente set di dati come esempio, possiamo osservare che questi dati sono piuttosto simili ai dati citati in [**VHCL**](https://docs.aspose.com/cells/nodejs-cpp/create-volume-high-low-close-stock-chart/). Se vogliamo visualizzare series0, che corrisponde a "Ricavo totale," come un grafico a Linee, come dovremmo procedere?

![todo:image_alt_text](sample.png)
## **Grafico Combo**
Dopo aver eseguito il codice qui sotto, vedrai il Grafico Combo come mostrato di seguito.

![todo:image_alt_text](result.png)
## **Codice di Esempio**
Il codice di esempio seguente carica il [file Excel di esempio] (combo.xlsx) e genera il [file Excel di output] (out.xlsx).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "combo.xlsx");

// Create the workbook
const workbook = new AsposeCells.Workbook(filePath);
// Access the first worksheet
const worksheet = workbook.getWorksheets().get(0);
// Add a stock volume (VHLC)
const pieIdx = worksheet.getCharts().add(AsposeCells.ChartType.StockVolumeHighLowClose, 15, 0, 34, 12);
// Retrieve the Chart object
const chart = worksheet.getCharts().get(pieIdx);
// Set the legend can be showed
chart.setShowLegend(true);
// Set the chart title name 
chart.getTitle().setText("Combo Chart");
// Set the Legend at the bottom of the chart area
chart.getLegend().setPosition(AsposeCells.LegendPositionType.Bottom);
// Set data range
chart.setChartDataRange("A1:E12", true);
// Set category data 
chart.getNSeries().get(0).setXValues("A2:A12");  // Corrected method

// Set the Series[1] Series[2] and Series[3] to different Marker Style
for (let j = 0; j < chart.getNSeries().getCount(); j++) {
switch (j) {
case 1:
chart.getNSeries().get(j).getMarker().setMarkerStyle(AsposeCells.ChartMarkerType.Circle);
chart.getNSeries().get(j).getMarker().setMarkerSize(15);
chart.getNSeries().get(j).getMarker().getArea().setFormatting(AsposeCells.FormattingType.Custom);
chart.getNSeries().get(j).getMarker().getArea().setForegroundColor(AsposeCells.Color.Pink);
chart.getNSeries().get(j).getBorder().setIsVisible(false);
break;
case 2:
chart.getNSeries().get(j).getMarker().setMarkerStyle(AsposeCells.ChartMarkerType.Dash);
chart.getNSeries().get(j).getMarker().setMarkerSize(15);
chart.getNSeries().get(j).getMarker().getArea().setFormatting(AsposeCells.FormattingType.Custom);
chart.getNSeries().get(j).getMarker().getArea().setForegroundColor(AsposeCells.Color.Orange);
chart.getNSeries().get(j).getBorder().setIsVisible(false);
break;
case 3:
chart.getNSeries().get(j).getMarker().setMarkerStyle(AsposeCells.ChartMarkerType.Square);
chart.getNSeries().get(j).getMarker().setMarkerSize(15);
chart.getNSeries().get(j).getMarker().getArea().setFormatting(AsposeCells.FormattingType.Custom);
chart.getNSeries().get(j).getMarker().getArea().setForegroundColor(AsposeCells.Color.LightBlue);
chart.getNSeries().get(j).getBorder().setIsVisible(false);
break;
}
}
// Set the chart type for Series[0] 
chart.getNSeries().get(0).setType(AsposeCells.ChartType.Line);
// Set style for the border of first series
chart.getNSeries().get(0).getBorder().setStyle(AsposeCells.LineType.Solid);
// Set Color for the first series
chart.getNSeries().get(0).getBorder().setColor(AsposeCells.Color.DarkBlue);
// Fill the PlotArea area with nothing 
chart.getPlotArea().getArea().setFormatting(AsposeCells.FormattingType.None);
// Save the Excel file
workbook.save("out.xlsx");
```
