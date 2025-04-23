---
title: Skapa cirkeldiagram med ledarlinjer med Node.js via C++
description: Lär dig hur du använder Aspose.Cells for Node.js via C++ för att skapa ett cirkeldiagram med ledarlinjer i Microsoft Excel. Vår guide visar hur du lägger till ledarlinjer som kopplar datapunkter till legenden och förbättrar överskådligheten av diagrammet.
keywords: Aspose.Cells for Node.js via C++, Cirkeldiagram, Ledarlinjer, Microsoft Excel, Data Visualisering, Diagramanpassning.
linktitle: Cirkeldiagram
type: docs
weight: 45
url: /sv/nodejs-cpp/creating-pie-chart-with-leader-lines/
---

{{% alert color="primary" %}}

Denna artikel förklarar hur man skapar ett cirkeldiagram med ledarlinjer från grunden med hjälp av Aspose.Cells for Node.js via C++ API. I Excel är 'Visa ledarlinjer'-alternativet aktiverat som standard, så när du skapar ett cirkeldiagram i Excel visas ledarlinjerna. Men när du skapar ett liknande diagram med Aspose.Cells API måste du explicit ställa in [**Series.getHasLeaderLines()**](https://reference.aspose.com/cells/nodejs-cpp/series/#getHasLeaderLines--)-egenskapen.

{{% /alert %}}

För att demonstrera användningen av Aspose.Cells for Node.js via C++ API för att skapa ett cirkeldiagram med ledarlinjer, skapar vi först ett nytt [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) och matar in några data som kommer att fungera som serien datakälla. När datan är på plats, lägger vi till en [**Chart**](https://reference.aspose.com/cells/nodejs-cpp/chart) av typen [**ChartType.Pie**](https://reference.aspose.com/cells/nodejs-cpp/charttype) till samlingen av diagram och ställer in dess olika aspekter för att få önskad diagramvy.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Access the first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Add two columns of data
worksheet.getCells().get("A1").putValue("Retail");
worksheet.getCells().get("A2").putValue("Services");
worksheet.getCells().get("A3").putValue("Info & Communication");
worksheet.getCells().get("A4").putValue("Transport Equip");
worksheet.getCells().get("A5").putValue("Construction");
worksheet.getCells().get("A6").putValue("Other Products");
worksheet.getCells().get("A7").putValue("Wholesale");
worksheet.getCells().get("A8").putValue("Land Transport");
worksheet.getCells().get("A9").putValue("Air Transport");
worksheet.getCells().get("A10").putValue("Electric Appliances");
worksheet.getCells().get("A11").putValue("Securities");
worksheet.getCells().get("A12").putValue("Textiles & Apparel");
worksheet.getCells().get("A13").putValue("Machinery");
worksheet.getCells().get("A14").putValue("Metal Products");
worksheet.getCells().get("A15").putValue("Cash");
worksheet.getCells().get("A16").putValue("Banks");

worksheet.getCells().get("B1").putValue(10.4);
worksheet.getCells().get("B2").putValue(5.2);
worksheet.getCells().get("B3").putValue(6.4);
worksheet.getCells().get("B4").putValue(10.4);
worksheet.getCells().get("B5").putValue(7.9);
worksheet.getCells().get("B6").putValue(4.1);
worksheet.getCells().get("B7").putValue(3.5);
worksheet.getCells().get("B8").putValue(5.7);
worksheet.getCells().get("B9").putValue(3);
worksheet.getCells().get("B10").putValue(14.7);
worksheet.getCells().get("B11").putValue(3.6);
worksheet.getCells().get("B12").putValue(2.8);
worksheet.getCells().get("B13").putValue(7.8);
worksheet.getCells().get("B14").putValue(2.4);
worksheet.getCells().get("B15").putValue(1.8);
worksheet.getCells().get("B16").putValue(10.1);

// Create a pie chart and add it to the collection of charts
const id = worksheet.getCharts().add(AsposeCells.ChartType.Pie, 3, 3, 23, 13);

// Access newly created Chart instance
const chart = worksheet.getCharts().get(id);

// Set series data range
chart.getNSeries().add("B1:B16", true);

// Set category data range
chart.getNSeries().setCategoryData("A1:A16");

// Turn off legend
chart.setShowLegend(false);

// Access data labels
const dataLabels = chart.getNSeries().get(0).getDataLabels();

// Turn on category names
dataLabels.setShowCategoryName(true);

// Turn on percentage format
dataLabels.setShowPercentage(true);

// Set position
dataLabels.setPosition(AsposeCells.LabelPositionType.OutsideEnd);

// Set separator
dataLabels.setSeparatorType(AsposeCells.DataLabelsSeparatorType.Comma);
```

Hittills har vi skapat ett cirkeldiagram och ställt in dess olika aspekter. Nu kommer vi att slå på ledarlänkarna för diagrammet. Observera, för att visa ledarlänkar måste vi flytta dataetiketterna lite.

Följande kodsnutt slår på ledarlänkarna, uppdaterar diagrammet och beräknar sedan dataetiketternas positioner för att flytta dem på lämpligt sätt.

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Access the first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Add two columns of data
worksheet.getCells().get("A1").putValue("Retail");
worksheet.getCells().get("A2").putValue("Services");
worksheet.getCells().get("A3").putValue("Info & Communication");
worksheet.getCells().get("A4").putValue("Transport Equip");
worksheet.getCells().get("A5").putValue("Construction");
worksheet.getCells().get("A6").putValue("Other Products");
worksheet.getCells().get("A7").putValue("Wholesale");
worksheet.getCells().get("A8").putValue("Land Transport");
worksheet.getCells().get("A9").putValue("Air Transport");
worksheet.getCells().get("A10").putValue("Electric Appliances");
worksheet.getCells().get("A11").putValue("Securities");
worksheet.getCells().get("A12").putValue("Textiles & Apparel");
worksheet.getCells().get("A13").putValue("Machinery");
worksheet.getCells().get("A14").putValue("Metal Products");
worksheet.getCells().get("A15").putValue("Cash");
worksheet.getCells().get("A16").putValue("Banks");

worksheet.getCells().get("B1").putValue(10.4);
worksheet.getCells().get("B2").putValue(5.2);
worksheet.getCells().get("B3").putValue(6.4);
worksheet.getCells().get("B4").putValue(10.4);
worksheet.getCells().get("B5").putValue(7.9);
worksheet.getCells().get("B6").putValue(4.1);
worksheet.getCells().get("B7").putValue(3.5);
worksheet.getCells().get("B8").putValue(5.7);
worksheet.getCells().get("B9").putValue(3);
worksheet.getCells().get("B10").putValue(14.7);
worksheet.getCells().get("B11").putValue(3.6);
worksheet.getCells().get("B12").putValue(2.8);
worksheet.getCells().get("B13").putValue(7.8);
worksheet.getCells().get("B14").putValue(2.4);
worksheet.getCells().get("B15").putValue(1.8);
worksheet.getCells().get("B16").putValue(10.1);

// Create a pie chart and add it to the collection of charts
const id = worksheet.getCharts().add(AsposeCells.ChartType.Pie, 3, 3, 23, 13);

// Access newly created Chart instance
const chart = worksheet.getCharts().get(id);

// Set series data range
chart.getNSeries().add("B1:B16", true);

// Set category data range
chart.getNSeries().setCategoryData("A1:A16");

// Turn off legend
chart.setShowLegend(false);

// Access data labels
const dataLabels = chart.getNSeries().get(0).getDataLabels();

// Turn on category names
dataLabels.setShowCategoryName(true);

// Turn on percentage format
dataLabels.setShowPercentage(true);

// Set position
dataLabels.setPosition(AsposeCells.LabelPositionType.OutsideEnd);

// Set separator
dataLabels.setSeparatorType(AsposeCells.DataLabelsSeparatorType.Comma);

// Turn on leader lines
chart.getNSeries().get(0).setHasLeaderLines(true);

// Calculate chart
chart.calculate();

// You need to move DataLabels a little leftward or rightward depending on their position to show leader lines
const DELTA = 100;
for (let i = 0; i < chart.getNSeries().get(0).getPoints().getCount(); i++) {
let X = chart.getNSeries().get(0).getPoints().get(i).getDataLabels().getX();
// If it is greater than 2000, then move the X position a little right otherwise move the X position a little left
if (X > 2000)
chart.getNSeries().get(0).getPoints().get(i).getDataLabels().setX(X + DELTA);
else
chart.getNSeries().get(0).getPoints().get(i).getDataLabels().setX(X - DELTA);
}
```

Slutligen sparar följande kod diagrammet i bildformat och arbetsboken i XLSX-format.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

// Create an instance of Workbook in XLSX format
const workbook = new AsposeCells.Workbook(AsposeCells.FileFormatType.Xlsx);

// Access the first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Add two columns of data
worksheet.getCells().get("A1").putValue("Retail");
worksheet.getCells().get("A2").putValue("Services");
worksheet.getCells().get("A3").putValue("Info & Communication");
worksheet.getCells().get("A4").putValue("Transport Equip");
worksheet.getCells().get("A5").putValue("Construction");
worksheet.getCells().get("A6").putValue("Other Products");
worksheet.getCells().get("A7").putValue("Wholesale");
worksheet.getCells().get("A8").putValue("Land Transport");
worksheet.getCells().get("A9").putValue("Air Transport");
worksheet.getCells().get("A10").putValue("Electric Appliances");
worksheet.getCells().get("A11").putValue("Securities");
worksheet.getCells().get("A12").putValue("Textiles & Apparel");
worksheet.getCells().get("A13").putValue("Machinery");
worksheet.getCells().get("A14").putValue("Metal Products");
worksheet.getCells().get("A15").putValue("Cash");
worksheet.getCells().get("A16").putValue("Banks");

worksheet.getCells().get("B1").putValue(10.4);
worksheet.getCells().get("B2").putValue(5.2);
worksheet.getCells().get("B3").putValue(6.4);
worksheet.getCells().get("B4").putValue(10.4);
worksheet.getCells().get("B5").putValue(7.9);
worksheet.getCells().get("B6").putValue(4.1);
worksheet.getCells().get("B7").putValue(3.5);
worksheet.getCells().get("B8").putValue(5.7);
worksheet.getCells().get("B9").putValue(3);
worksheet.getCells().get("B10").putValue(14.7);
worksheet.getCells().get("B11").putValue(3.6);
worksheet.getCells().get("B12").putValue(2.8);
worksheet.getCells().get("B13").putValue(7.8);
worksheet.getCells().get("B14").putValue(2.4);
worksheet.getCells().get("B15").putValue(1.8);
worksheet.getCells().get("B16").putValue(10.1);

// Create a pie chart and add it to the collection of charts
const id = worksheet.getCharts().add(AsposeCells.ChartType.Pie, 3, 3, 23, 13);

// Access newly created Chart instance
const chart = worksheet.getCharts().get(id);

// Set series data range
chart.getNSeries().add("B1:B16", true);

// Set category data range
chart.getNSeries().setCategoryData("A1:A16");

// Turn off legend
chart.setShowLegend(false);

// Access data labels
const dataLabels = chart.getNSeries().get(0).getDataLabels();

// Turn on category names
dataLabels.setShowCategoryName(true);

// Turn on percentage format
dataLabels.setShowPercentage(true);

// Set position
dataLabels.setPosition(AsposeCells.LabelPositionType.OutsideEnd);

// Set separator
dataLabels.setSeparatorType(AsposeCells.DataLabelsSeparatorType.Comma);

// In order to save the chart image, create an instance of ImageOrPrintOptions
const anOption = new AsposeCells.ImageOrPrintOptions();

// Set image format
anOption.setImageType(AsposeCells.ImageType.Png);

// Set resolution
anOption.setHorizontalResolution(200);
anOption.setVerticalResolution(200);

// Render chart to image
chart.toImage(path.join(dataDir, "output_out.png"), anOption);

// Save the workbook to see chart inside the Excel
workbook.save(path.join(dataDir, "output_out.xlsx"));
```

|**Resulterande Cirkeldiagram**|
| :- |
|![todo:image_alt_text](creating-pie-chart-with-leader-lines_1.png)|

## **Fortsatta ämnen**
- [Anpassade färgval för skiv- eller sektorfärger i cirkeldiagram](/cells/sv/nodejs-cpp/custom-slice-or-sector-colors-in-pie-chart/)
- [Ta reda på om datapunkterna finns i den andra pajen eller stapeln på ett paj- eller stapeldiagram](/cells/sv/nodejs-cpp/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/)

## Relaterade artiklar

- [Skapa diagram](/cells/sv/nodejs-cpp/creating-charts/)
- [Anpassa diagram](/cells/sv/nodejs-cpp/customizing-charts/)
- [Dataformatering i diagram](/cells/sv/nodejs-cpp/data-formatting-in-charts/)
- [Ställa in diagramens utseende](/cells/sv/nodejs-cpp/setting-chart-appearance/)

