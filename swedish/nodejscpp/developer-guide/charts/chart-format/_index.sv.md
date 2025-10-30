---
title: Ställa in diagramutseende med Node.js via C++
description: Lär dig hur du konfigurerar utseendet på diagram i Aspose.Cells for Node.js via C++. Vår guide visar hur du ändrar diagramlayout, färger, teckensnitt och effekter för att uppnå önskad visuellt stil och förbättra dina kalkylblad.
keywords: Aspose.Cells for Node.js via C++, diagram, diagramutseende, layouter, färger, teckensnitt, effekter, kalkylblad.
linktitle: Diagramformat
type: docs
weight: 20
url: /sv/nodejs-cpp/setting-chart-appearance/
---

## **Ställa in diagramens utseende**
I Hur man skapar ett diagram gav vi en kort introduktion till typerna av diagram och diagramobjekt som erbjuds av Aspose.Cells, och beskrev hur man skapar ett. Den här artikeln diskuterar hur man anpassar diagrammens utseende genom att ställa in deras egenskaper:

- Inställning av diagramområdet.
- Inställning av diagramlinjer.
- Tillämpa teman.
- Ställa in titlar på diagram och axlar.
- Arbeta med rutnät.

### **Inställning av diagramområde**
Det finns olika typer av områden i ett diagram och Aspose.Cells ger flexibilitet att modifiera utseendet på varje område. Utvecklare kan tillämpa olika formateringsinställningar på ett område genom att ändra dess förgrundsfärg, bakgrundsfärg och fyllning osv.

I det givna exemplet har vi tillämpat olika formateringsinställningar på olika typer av områden i ett diagram. Dessa områden inkluderar:

- Plotområde
- Diagramområde
- Serieområdesamling
- Område för en enskild punkt i en serieområdesamling

Följande kodsnuttdemonstrerar hur man ställer in diagramområdet.

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
chart.getPlotArea().getArea().setForegroundColor(new AsposeCells.Color(0, 0, 255));

// Setting the foreground color of the chart area
chart.getChartArea().getArea().setForegroundColor(new AsposeCells.Color(255, 255, 0));

// Setting the foreground color of the 1st SeriesCollection area
chart.getNSeries().get(0).getArea().setForegroundColor(new AsposeCells.Color(255, 0, 0));

// Setting the foreground color of the area of the 1st SeriesCollection point
chart.getNSeries().get(0).getPoints().get(0).getArea().setForegroundColor(new AsposeCells.Color(0, 255, 255));

// Filling the area of the 2nd SeriesCollection with a gradient
chart.getNSeries().get(1).getArea().getFillFormat().setOneColorGradient(new AsposeCells.Color(0, 255, 0), 1, AsposeCells.GradientStyleType.Horizontal, 1);

// Saving the Excel file
workbook.save(path.join(dataDir, "book1.out.xls"));
```

### **Inställning av diagramlinjer**
Utvecklare kan även tillämpa olika typer av stilar på linjer eller datapunktmarkörer för [SeriesCollection](https://reference.aspose.com/cells/nodejs-cpp/seriescollection/). Följande kodsnutt visar hur man ställer in diagramlinjer med Aspose.Cells API.

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

// Applying a dotted line style on the lines of a SeriesCollection
chart.getNSeries().get(0).getBorder().setStyle(AsposeCells.LineType.Dot);

// Applying a triangular marker style on the data markers of a SeriesCollection
chart.getNSeries().get(0).getMarker().setMarkerStyle(AsposeCells.ChartMarkerType.Triangle);

// Setting the weight of all lines in a SeriesCollection to medium
chart.getNSeries().get(1).getBorder().setWeight(AsposeCells.WeightType.MediumLine);

// Saving the Excel file
workbook.save(path.join(dataDir, "book1.out.xls"));
```

### **Tillämpning av Microsoft Excel 2007/2010 teman på diagram**
Utvecklare kan tillämpa olika Microsoft Excel-teman/färger på [SeriesCollection](https://reference.aspose.com/cells/nodejs-cpp/seriescollection/) eller andra diagramobjekt som visas nedan i exemplet.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample_chart.xlsx");

// Loads the workbook containing the chart
const workbook = new AsposeCells.Workbook(filePath);

// Get the first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Get the first chart in the sheet
const chart = worksheet.getCharts().get(0);

// Specify the FillFormat's type to Solid Fill of the first series
chart.getNSeries().get(0).getArea().getFillFormat().setFillType(AsposeCells.FillType.Solid);

// Get the CellsColor of SolidFill
const cc = chart.getNSeries().get(0).getArea().getFillFormat().getSolidFill().getCellsColor();

// Create a theme in Accent style
cc.setThemeColor(new AsposeCells.ThemeColor(AsposeCells.ThemeColorType.Accent6, 0.6));

// Apply the theme to the series
chart.getNSeries().get(0).getArea().getFillFormat().getSolidFill().setCellsColor(cc);

// Save the Excel file
workbook.save(path.join(dataDir, "output.out.xlsx"));
```

### **Inställning av diagram- eller axeltitlar**
Du kan använda Microsoft Excel för att ställa in diagramtitlar och axlar i en WYSIWYG-miljö. Aspose.Cells tillåter också utvecklare att sätta diagramtitlar och axlar vid körning. Alla diagram och deras axlar innehåller en [Title](https://reference.aspose.com/cells/nodejs-cpp/title/) egenskap som kan användas för att ange deras titlar som visas nedan i ett exempel.

Följande kodexempel visar hur du kan ställa in titlar på diagram och axlar.

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

### **Arbeta med stora rutnätlinjer**
Det är möjligt att anpassa utseendet på stora rutnätlinjer. Dölj eller visa rutnätlinjer, eller definiera deras färg och andra inställningar. Nedan visar vi hur man döljer rutnätlinjer och hur man ändrar deras färg.

#### **Dölja stora rutnät**
Utvecklare kan kontrollera synligheten för större rutnätlinjer genom att ställa in egenskapen [isVisible()](https://reference.aspose.com/cells/nodejs-cpp/line/#isVisible--) för objektet [Line](https://reference.aspose.com/cells/nodejs-cpp/line/) till **true** eller **false**.

Följande kodsnutt visar hur man döljer större rutnätlinjer. Efter att ha döljt de större rutnätlinjerna, kommer ett kolumndiagram att läggas till kalkylbladet utan rutnätlinjer.

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

// Hiding the major gridlines of Category Axis
chart.getCategoryAxis().getMajorGridLines().setIsVisible(false);

// Hiding the major gridlines of Value Axis
chart.getValueAxis().getMajorGridLines().setIsVisible(false);

// Saving the Excel file
workbook.save(path.join(dataDir, "book1.out.xls"));
```

#### **Ändra inställningar för stora rutnät**
Utvecklare kan inte bara kontrollera synligheten för stora rutnät utan också andra egenskaper inklusive dess färg osv.

Följande kodsnutt visar hur man ändrar färgen på de större rutnätlinjerna. Efter att ha ställt in färgen på de större rutnätlinjerna kommer ett kolumndiagram att läggas till kalkylbladet med modifierade rutnätlinjer.

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

// Setting the color of Category Axis' major gridlines to silver
chart.getCategoryAxis().getMajorGridLines().setColor(AsposeCells.Color.Silver);

// Setting the color of Value Axis' major gridlines to red
chart.getValueAxis().getMajorGridLines().setColor(AsposeCells.Color.Red);

// Saving the Excel file
workbook.save(path.join(dataDir, "book1.out.xls"));
```

## **Fortsatta ämnen**
- [Ställ in värdenas formatkod för diagramserier](/cells/sv/nodejs-cpp/set-the-values-format-code-of-chart-series/)
- [Ange bild som bakgrundsfyllning i diagrammet.](/cells/sv/nodejs-cpp/set-picture-as-background-fill-in-the-chart/)


{{< app/cells/assistant language="nodejs-cpp" >}}
