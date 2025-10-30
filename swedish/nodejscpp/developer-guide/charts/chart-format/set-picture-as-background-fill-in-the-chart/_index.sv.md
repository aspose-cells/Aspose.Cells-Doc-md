---
title: Ställ in bild som bakgrundsfyllning i diagrammet med Node.js via C++
linktitle: Ange bild som bakgrundsfyllning i diagrammet
description: Lär dig hur du ställer in en bild som bakgrundsfyllning i ett diagram med Aspose.Cells for Node.js via C++. Vår guide visar hur du importerar och positionerar bilden, justerar storlek och färg, samt tillämpar formateringsalternativ för att förbättra diagrammets utseende.
keywords: Aspose.Cells for Node.js via C++, diagram, bakgrundsfyllning, bild, import, positionering, storlek, färg, formatering.
type: docs
weight: 30
url: /sv/nodejs-cpp/set-picture-as-background-fill-in-the-chart/
---

{{% alert color="primary" %}}

Aspose.Cells låter dig använda en gradient, textur, mönster eller bild som fyllEffekt för olika objekt, som diagrammets plotyta, diagramyta eller legendboxen. Denna dokument visar hur man lägger till en bild i bakgrunden på ett diagram.

{{% /alert %}}

För att uppnå detta tillhandahåller Aspose.Cells egenskapen [**Chart.getPlotArea()**](https://reference.aspose.com/cells/nodejs-cpp/chart/#getPlotArea--). Följande kodexempel demonstrerar användningen av egenskapen [**Chart.getPlotArea()**](https://reference.aspose.com/cells/nodejs-cpp/chart/#getPlotArea--) för att ställa in en bild som bakgrundsfyllning i diagrammet.

## Node.js kod för att ställa in bild som bakgrundsfyllning i diagrammet

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Get the first worksheet.
let sheet = workbook.getWorksheets().get(0);

// Set the name of worksheet
sheet.setName("Data");

// Get the cells collection in the sheet.
const cells = workbook.getWorksheets().get(0).getCells();

// Put some values into a cells of the Data sheet.
cells.get("A1").putValue("Region");
cells.get("A2").putValue("France");
cells.get("A3").putValue("Germany");
cells.get("A4").putValue("England");
cells.get("A5").putValue("Sweden");
cells.get("A6").putValue("Italy");
cells.get("A7").putValue("Spain");
cells.get("A8").putValue("Portugal");
cells.get("B1").putValue("Sale");
cells.get("B2").putValue(70000);
cells.get("B3").putValue(55000);
cells.get("B4").putValue(30000);
cells.get("B5").putValue(40000);
cells.get("B6").putValue(35000);
cells.get("B7").putValue(32000);
cells.get("B8").putValue(10000);

// Add a chart sheet.
let sheetIndex = workbook.getWorksheets().add(AsposeCells.SheetType.Chart);
sheet = workbook.getWorksheets().get(sheetIndex);

// Set the name of worksheet
sheet.setName("Chart");

// Create chart
let chartIndex = sheet.getCharts().add(AsposeCells.ChartType.Column, 1, 1, 25, 10);
const chart = sheet.getCharts().get(chartIndex);

// Set some properties of chart plot area.
// To set a picture as fill format and make the border invisible.
const fs = require("fs");
const data = fs.readFileSync(path.join(dataDir, "aspose.png"));
chart.getPlotArea().getArea().getFillFormat().setImageData(data);
chart.getPlotArea().getBorder().setIsVisible(false);

// Set properties of chart title
chart.getTitle().setText("Sales By Region");
chart.getTitle().getFont().setColor(AsposeCells.Color.Blue);
chart.getTitle().getFont().setIsBold(true);
chart.getTitle().getFont().setSize(12);

// Set properties of nseries
chart.getNSeries().add("Data!B2:B8", true);
chart.getNSeries().setCategoryData("Data!A2:A8");
chart.getNSeries().setIsColorVaried(true);

// Set the Legend.
const legend = chart.getLegend();
legend.setPosition(AsposeCells.LegendPositionType.Top);

// Save the excel file
workbook.save(path.join(dataDir, "column_chart_out.xls"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
