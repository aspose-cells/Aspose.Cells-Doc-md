---
title: Skapa och hantera diagram med Node.js via C++
linktitle: Diagram
description: Lär dig att använda Aspose.Cells för Node.js för att skapa diagram i Microsoft Excel. Vår guide visar olika diagramtyper och hur man anpassar deras utseende och formatering.
keywords: Aspose.Cells för Node.js, Diagramskapande, Microsoft Excel, Diagramtyper, Anpassning, Utseende, Formatering.
type: docs
weight: 130
url: /sv/nodejs-cpp/creating-charts/
---

{{% alert color="primary" %}}

Det är möjligt att lägga till en mängd olika diagram i kalkylblad med Aspose.Cells. Aspose.Cells tillhandahåller många flexibla diagramobjekt. Det här ämnet diskuterar Aspose.Cells diagramobjekt.

{{% /alert %}}

## **Skapa diagram**

### **Enkelt skapa ett diagram**
Det är enkelt att skapa ett diagram med Aspose.Cells med följande exempelkod:
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Obtaining the reference of the first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Adding sample values to cells
worksheet.getCells().get("A2").putValue("Category1");
worksheet.getCells().get("A3").putValue("Category2");
worksheet.getCells().get("A4").putValue("Category3");

worksheet.getCells().get("B1").putValue("Column1");
worksheet.getCells().get("B2").putValue(4);
worksheet.getCells().get("B3").putValue(20);
worksheet.getCells().get("B4").putValue(50);
worksheet.getCells().get("C1").putValue("Column2");
worksheet.getCells().get("C2").putValue(50);
worksheet.getCells().get("C3").putValue(100);
worksheet.getCells().get("C4").putValue(150);

// Adding a chart to the worksheet
const chartIndex = worksheet.getCharts().add(AsposeCells.ChartType.Column, 5, 0, 15, 5);

// Accessing the instance of the newly added chart
const chart = worksheet.getCharts().get(chartIndex);

// Setting chart data source as the range "A1:C4"
chart.setChartDataRange("A1:C4", true);

// Saving the Excel file
workbook.save(path.join(dataDir, "output.xls"));
```

### **Saker att veta för att skapa ett diagram**

Innan du skapar diagram är det viktigt att förstå några grundläggande koncept som är till hjälp när du skapar diagram med Aspose.Cells.

#### **Diagramobjekt**

Diagramobjekten listas nedan:

- Serie, en enda dataserie i ett diagram.
- Axeln, ett diagramaxel.
- Diagram, ett enskilt Excel-diagram.
- Diagramområde, diagramområdet i arbetsbladet.
- ChartDataTable, en diagramdatatabell.
- ChartFrame, objektet ram i ett diagram.
- ChartPoint, enstaka punkt i en serie i ett diagram.
- ChartPointCollection, en samling som innehåller alla punkter i en serie.
- Charts, en samling av diagramobjekt.
- DataLabels, en samling av alla DataLabel-objekt för den angivna serien.
- FillFormat, fyllnadsformat för en form.
- Floor, golvet i ett 3D-diagram.
- Legend, diagrammets legend.
- Line, diagramlinjen.
- SeriesCollection, en samling av serieobjekt.
- TickLabels, de tickmarkeringsetiketter som är associerade med tickmarkeringar på en diagramaxel.
- Title, diagram- eller axeltiteln.
- Trendline, en trendlinje i ett diagram.
- TrendlineCollection, en samling av alla Trendline-objekt för den angivna dataserien.
- Walls, väggarna i ett 3D-diagram.

#### **Användning av diagramobjekt**

Som nämnts ovan är alla diagramobjekt instanser av sina respektive klasser och tillhandahåller specifika egenskaper och metoder för att utföra specifika uppgifter. Använd diagramobjekt för att skapa diagram.

Lägg till vilken typ av diagram som helst i ett kalkylblad med hjälp av [**getCharts()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCharts--)-samlingen. Varje objekt i [**getCharts()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCharts--)-samlingen representerar ett [**Chart**](https://reference.aspose.com/cells/nodejs-cpp/chart/)-objekt. Ett [**Chart**](https://reference.aspose.com/cells/nodejs-cpp/chart/)-objekt kapslar in alla andra diagramobjekt som krävs för att anpassa diagrammets utseende. Nästa avsnitt visar hur man använder några grundläggande diagramobjekt för att skapa ett enkelt diagram.

### **Skapa diagram med Aspose.Cells**

**Steg:**

1. Lägg till data i kalkylbladsceller med [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell/)-objektets [**putValue(string)**](https://reference.aspose.com/cells/nodejs-cpp/cell/#putValue-string-)-metod.
   Detta kommer att användas som datakälla för diagrammet.
1. Lägg till ett diagram i kalkylbladet genom att anropa [**ChartCollection**](https://reference.aspose.com/cells/nodejs-cpp/chartcollection)-samlingens [**add**](https://reference.aspose.com/cells/nodejs-cpp/chartcollection/#add-charttype-number-number-number-number-)-metod, kapslad i [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/)-objektet.
1. Ange typ av diagram med [**ChartType**](https://reference.aspose.com/cells/nodejs-cpp/charttype/)-uppräknaren.
   Till exempel, använder exemplet nedan värdet [**ChartType.Pyramid**](https://reference.aspose.com/cells/nodejs-cpp/charttype) som diagramtyp.
1. Åtkomst till det nya [**Chart**](https://reference.aspose.com/cells/nodejs-cpp/chart/)-objektet från [**Charts**](https://reference.aspose.com/cells/nodejs-cpp/chartcollection)-samlingen genom att ange dess index.
1. Använd något av diagramobjekten kapslade i [**Chart**](https://reference.aspose.com/cells/nodejs-cpp/chart/)-objektet för att hantera diagrammet.
   Exemplet nedan använder [**SeriesCollection**](https://reference.aspose.com/cells/nodejs-cpp/seriescollection/)-diagramobjektet för att ange diagrammets datakälla.

När du lägger till datakälla till diagrammet kan datakällan vara ett cellområde (som "A1:C3"), eller en sekvens av icke sammanhängande celler (som "A1, A3, A5"), eller en sekvens av värden (som "1,2,3").

Dessa allmänna steg gör det möjligt för dig att skapa vilken typ av diagram som helst. Använd olika diagramobjekt för att skapa olika diagram.

Det är möjligt att skapa många olika typer av diagram med Aspose.Cells. Alla standarddiagram som stöds av Aspose.Cells är fördefinierade i en uppräkning som heter [**ChartType**](https://reference.aspose.com/cells/nodejs-cpp/charttype/).

Fördefinierade diagramtyper är:

|**Diagramtyper**|**Beskrivning**|
| :- | :- |
|Column|Representerar diagram över klustringsskikt|
|ColumnStacked|Representerar det staplade kolumnl-diagrammet|
|Column100PercentStacked|Representerar 100% staplat kolumnl-diagram|
|Column3DClustered|Representerar 3D-staplade kolumnl-diagram|
|Column3DStacked|Representerar 3D-staplade kolumnl-diagram|
|Column3D100PercentStacked|Representerar 3D 100% staplat kolumnl-diagram|
|Column3D|Representerar 3D-kolumnl-diagram|
|Bar|Representerar det staplade stapeldiagrammet|
|BarStacked|Representerar det staplade stapeldiagrammet|
|Bar100PercentStacked|Representerar 100% staplat stapeldiagram|
|Bar3DClustered|Representerar 3D-staplade stapeldiagram|
|Bar3DStacked|Representerar 3D-staplade stapeldiagram|
|Bar3D100PercentStacked|Representerar 3D 100% staplat stapeldiagram|
|Line|Representerar linjediagram|
|LineStacked|Representerar staplat linjediagram|
|Line100PercentStacked|Representerar 100% staplat linjediagram|
|LineWithDataMarkers|Representerar linjediagram med datamarkörer|
|LineStackedWithDataMarkers|Representerar staplat linjediagram med datamarkörer|
|Line100PercentStackedWithDataMarkers|Representerar 100% staplat linjediagram med datamarkörer|
|Line3D|Representerar 3D linjediagram|
|Pie|Representerar cirkeldiagram|
|Pie3D|Representerar 3D cirkeldiagram|
|PiePie|Representerar kaka av kaka-diagram|
|PieExploded|Representerar Exploderad Cirkeldiagram|
|Pie3DExploded|Representerar 3D Exploderad Cirkeldiagram|
|PieBar|Representerar stapel av cirkeldiagram|
|Scatter|Representerar spridningsdiagram|
|ScatterConnectedByCurvesWithDataMarker|Representerar spridningsdiagram anslutna med kurvor, med datamarkörer|
|ScatterConnectedByCurvesWithoutDataMarker|Representerar spridningsdiagram anslutna med kurvor, utan datamarkörer|
|ScatterConnectedByLinesWithDataMarker|Representerar spridningsdiagram anslutna med linjer, med datamarkörer|
|ScatterConnectedByLinesWithoutDataMarker|Representerar spridningsdiagram anslutna med linjer, utan datamarkörer|
|Area|Representerar områdesdiagrammet|
|AreaStacked|Representerar staplade områdesdiagrammet|
|Area100PercentStacked|Representerar 100% staplade områdesdiagrammet|
|Area3D|Representerar 3D områdesdiagrammet|
|Area3DStacked|Representerar 3D staplade områdesdiagrammet|
|Area3D100PercentStacked|Representerar 3D 100% staplade områdesdiagrammet|
|Doughnut|Representerar doughnut diagrammet|
|DoughnutExploded|Representerar Exploderat doughnut diagram|
|Radar|Representerar radardiagram|
|RadarWithDataMarkers|Representerar Radar-diagram med datamarkörer|
|RadarFilled|Representerar fyllt radardiagram|
|Surface3D|Representerar 3D ytdiagram|
|SurfaceWireframe3D|Representerar Wireframe 3D-yt-diagram|
|SurfaceContour|Representerar konturdiagram|
|SurfaceContourWireframe|Representerar wireframe konturdiagram|
|Bubble|Representerar boll diagrammet|
|Bubble3D|Representerar 3D boll diagrammet|
|Cylinder|Representerar cylinderdiagram|
|CylinderStacked|Representerar staplade cylinderdiagram|
|Cylinder100PercentStacked|Representerar 100% staplade cylinderdiagram|
|CylindericalBar|Representerar Cylindrisk stapeldiagram|
|CylindericalBarStacked|Representerar Stapeldiagram med cylindriska staplar|
|CylindericalBar100PercentStacked|Representerar 100% stapeldiagram med cylindriska staplar|
|CylindericalColumn3D|Representerar 3D cylindrisk stapeldiagram|
|Cone|Representerar Konediagram|
|ConeStacked|Representerar Staplad Konediagram|
|Cone100PercentStacked|Representerar 100% Staplad Konediagram|
|ConicalBar|Representerar Konisk Stapeldiagram|
|ConicalBarStacked|Representerar Staplad Konisk stapeldiagram|
|ConicalBar100PercentStacked|Representerar 100% Staplad Konisk Stapeldiagram|
|ConicalColumn3D|Representerar 3D Konisk Kolumn Diagram|
|Pyramid|Representerar Pyramid Diagram|
|PyramidStacked|Representerar Staplad Pyramiddiagram|
|Pyramid100PercentStacked|Representerar 100% Staplad Pyramiddiagram|
|PyramidBar|Representerar Pyramid stapeldiagram|
|PyramidBarStacked|Representerar Staplad Pyramid Stapeldiagram|
|PyramidBar100PercentStacked|Representerar 100% Staplad Pyramid Stapeldiagram|
|PyramidColumn3D|Representerar 3D Pyramid Kolumn Diagram|
{{% alert color="primary" %}}

När du tilldelar en cellintervall som datakälla kan du bara ställa in intervallet från övre vänstra till nedre högra. Till exempel är "A1:C3" giltigt medan "C3:A1" är ogiltigt.

{{% /alert %}}

#### **Pyramiddiagram**

När exempelkoden körs läggs ett pyramiddiagram till kalkylarket.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
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
workbook.save(path.join(dataDir, "output.xls"));
```

#### **Linjediagram**

I exemplet ovan, genom att ändra [**ChartType**](https://reference.aspose.com/cells/nodejs-cpp/charttype/) till *Line* skapas ett linjediagram. Den kompletta källan finns nedan. När koden körs läggs ett linjediagram till i kalkylbladet.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

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
const chartIndex = worksheet.getCharts().add(AsposeCells.ChartType.Line, 5, 0, 15, 5);

// Accessing the instance of the newly added chart
const chart = worksheet.getCharts().get(chartIndex);

// Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B3"
chart.getNSeries().add("A1:B3", true);

// Saving the Excel file
workbook.save(path.join(dataDir, "output.xls"));
```

#### **Bubbel-diagram**

För att skapa ett bubbeldiagram måste [**ChartType**](https://reference.aspose.com/cells/nodejs-cpp/charttype/) ställas in på [**ChartType.Bubble**](https://reference.aspose.com/cells/nodejs-cpp/charttype) och några extra egenskaper som BubbleSizes, Values & XValues måste ställas in därefter. När följande kod körs läggs ett bubbeldiagram till kalkylbladet.

#### **Linje med Datum Markör Diagram**

För att skapa ett linjediagram med datapunkter måste [**ChartType**](https://reference.aspose.com/cells/nodejs-cpp/charttype/) ställas in på *ChartType.LineWithDataMarkers* och några extra egenskaper såsom bakgrundsområde, Series Markers, Values & XValues måste konfigureras därefter. När följande kod körs läggs ett sådant linjediagram till kalkylbladet.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Instantiate a workbook
const workbook = new AsposeCells.Workbook();

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Set columns title 
worksheet.getCells().get(0, 0).putValue("X");
worksheet.getCells().get(0, 1).putValue("Y");

// Random data shall be used for generating the chart
// Create random data and save in the cells
for (let i = 1; i < 21; i++) {
worksheet.getCells().get(i, 0).putValue(i);
worksheet.getCells().get(i, 1).putValue(0.8);
}

for (let i = 21; i < 41; i++) {
worksheet.getCells().get(i, 0).putValue(i - 20);
worksheet.getCells().get(i, 1).putValue(0.9);
}
// Add a chart to the worksheet
const idx = worksheet.getCharts().add(AsposeCells.ChartType.LineWithDataMarkers, 1, 3, 20, 20);

// Access the newly created chart
const chart = worksheet.getCharts().get(idx);

// Set chart style
chart.setStyle(3);

// Set autoscaling value to true
chart.setAutoScaling(true);

// Set foreground color white
chart.getPlotArea().getArea().setForegroundColor(AsposeCells.Color.White);

// Set Properties of chart title
chart.getTitle().setText("Sample Chart");

// Set chart type
chart.setType(AsposeCells.ChartType.LineWithDataMarkers);

// Set Properties of categoryaxis title
chart.getCategoryAxis().getTitle().setText("Units");

//Set Properties of nseries
const s2_idx = chart.getNSeries().add("A2:A2", true);
const s3_idx = chart.getNSeries().add("A22:A22", true);

// Set IsColorVaried to true for varied points color
chart.getNSeries().setIsColorVaried(true);

// Set properties of background area and series markers
chart.getNSeries().get(s2_idx).getArea().setFormatting(AsposeCells.FormattingType.Custom);
chart.getNSeries().get(s2_idx).getMarker().getArea().setForegroundColor(AsposeCells.Color.Yellow);
chart.getNSeries().get(s2_idx).getMarker().getBorder().setIsVisible(false);

// Set X and Y values of series chart
chart.getNSeries().get(s2_idx).setXValues("A2:A21");
chart.getNSeries().get(s2_idx).setValues("B2:B21");

// Set properties of background area and series markers
chart.getNSeries().get(s3_idx).getArea().setFormatting(AsposeCells.FormattingType.Custom);
chart.getNSeries().get(s3_idx).getMarker().getArea().setForegroundColor(AsposeCells.Color.Green);
chart.getNSeries().get(s3_idx).getMarker().getBorder().setIsVisible(false);

// Set X and Y values of series chart
chart.getNSeries().get(s3_idx).setXValues("A22:A41");
chart.getNSeries().get(s3_idx).setValues("B22:B41");

// Save the workbook
workbook.save(path.join(dataDir, "LineWithDataMarkerChart.xlsx"), AsposeCells.SaveFormat.Xlsx);
```

## **Fortsatta ämnen**
- [Läs och hantera Excel 2016-diagram](/cells/sv/nodejs-cpp/read-and-manipulate-excel-2016-charts/)
- [Hantera axlarna för Excel-diagram](/cells/sv/nodejs-cpp/chart-axes/)
- [Ställa in diagramens utseende](/cells/sv/nodejs-cpp/setting-chart-appearance/)
- [Diagramtyper](/cells/sv/nodejs-cpp/chart-types/)
- [Anpassa diagram](/cells/sv/nodejs-cpp/customizing-charts/)
- [Ställ in datamängd för diagrammet](/cells/sv/nodejs-cpp/data-formatting-in-charts/)
- [Hantera Dataetiketter för Excel-diagram](/cells/sv/nodejs-cpp/insert-datalabels-to-chart/)
- [Hämta kalkylarket för diagrammet](/cells/sv/nodejs-cpp/get-worksheet-of-the-chart/)
- [Hantera legenden för Excel-diagram](/cells/sv/nodejs-cpp/chart-legend/)
- [Manipulera Position Size och Designer-diagram](/cells/sv/nodejs-cpp/manipulate-position-size-and-designer-chart/)
- [Skapa cirkeldiagram med ledarlinjer](/cells/sv/nodejs-cpp/creating-pie-chart-with-leader-lines/)
- [Former i diagram](/cells/sv/nodejs-cpp/controls-in-charts/)
- [Hantera titlar för Excel-diagram](/cells/sv/nodejs-cpp/chart-and-axis-titles/)
- [Diagramrendering](/cells/sv/nodejs-cpp/chart-rendering/)
- [Få ekvationstext av diagramtrendlinje](/cells/sv/nodejs-cpp/get-equation-text-of-chart-trendline/)
{{< app/cells/assistant language="nodejs-cpp" >}}
