---  
title: Lägga till anpassade etiketter till datapunkterna i diagramserien med Node.js via C++  
linktitle: Lägga till anpassade etiketter till datapunkter i diagramserien  
description: Lär dig hur du lägger till anpassade etiketter till datapunkter i serierna i ett diagram med hjälp av Aspose.Cells for Node.js via C++. Denna guide kommer att visa hur du modifierar etikettens utseende, position och formatering, samtidigt som du kopplar dem till din datakälla för exakt presentation.  
keywords: Aspose.Cells för Node.js, diagram, anpassade etiketter, datapunkter, serier, utseende, position, formatering, datakälla, presentation.  
type: docs  
weight: 100  
url: /sv/nodejs-cpp/adding-custom-labels-to-data-points-in-the-series-of-the-chart/  
---  

{{% alert color="primary" %}}  

Du kan lägga till anpassade etiketter till datapunkter i diagramserien. Aspose.Cells tillhandahåller [**DataLabels.getText()**](https://reference.aspose.com/cells/nodejs-cpp/datalabels/#getText--)-egenskapen för att lägga till dessa anpassade etiketter. Den här artikeln förklarar hur du använder denna egenskap för att lägga till anpassade etiketter till datapunkter i en diagramserie.

{{% /alert %}}  

Följande kod skapar **Scatter Diagram Kopplat Med Linjer Och Datapunkter** och lägger sedan till **Anpassade Etiketter** till **Datapunkterna** i **Serierna** av **Diagrammet**. Varje anpassad etikett visar **Seriens namn** och **Punktens namn**. Du kan använda all annan text istället för detta.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);
const sheet = workbook.getWorksheets().get(0);

// Put data
sheet.getCells().get(0, 0).putValue(1);
sheet.getCells().get(0, 1).putValue(2);
sheet.getCells().get(0, 2).putValue(3);

sheet.getCells().get(1, 0).putValue(4);
sheet.getCells().get(1, 1).putValue(5);
sheet.getCells().get(1, 2).putValue(6);

sheet.getCells().get(2, 0).putValue(7);
sheet.getCells().get(2, 1).putValue(8);
sheet.getCells().get(2, 2).putValue(9);

// Generate the chart
const chartIndex = sheet.getCharts().add(AsposeCells.ChartType.ScatterConnectedByLinesWithDataMarker, 5, 1, 24, 10);
const chart = sheet.getCharts().get(chartIndex);

chart.getTitle().setText("Test");
chart.getCategoryAxis().getTitle().setText("X-Axis");
chart.getValueAxis().getTitle().setText("Y-Axis");

chart.getNSeries().setCategoryData("A1:C1");

// Insert series
chart.getNSeries().add("A2:C2", false);

let series = chart.getNSeries().get(0);

let pointCount = series.getPoints().getCount();
for (let i = 0; i < pointCount; i++) {
const pointIndex = series.getPoints().get(i);
pointIndex.getDataLabels().setText("Series 1" + "\n" + "Point " + i);
}

// Insert series
chart.getNSeries().add("A3:C3", false);

series = chart.getNSeries().get(1);

pointCount = series.getPoints().getCount();
for (let i = 0; i < pointCount; i++) {
const pointIndex = series.getPoints().get(i);
pointIndex.getDataLabels().setText("Series 2" + "\n" + "Point " + i);
}

workbook.save(path.join(dataDir, "output_out.xlsx"), AsposeCells.SaveFormat.Xlsx);
```  

