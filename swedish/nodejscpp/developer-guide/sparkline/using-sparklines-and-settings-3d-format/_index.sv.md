---
title: Använd sparklines och inställningar för 3D format med Node.js via C++
linktitle: Använda sparklines och inställningar 3D format
type: docs
weight: 40
url: /sv/nodejs-cpp/using-sparklines-and-settings-3d-format/
description: Lär dig hur du använder sparklines och tillämpar 3D formatering i Excel filer med Aspose.Cells for Node.js via C++. 
---

## **Användning av sparklines**
Microsoft Excel 2010 kan analysera information på fler sätt än någonsin tidigare. Det låter användarna spåra och markera viktiga datatrender med nya verktyg för dataanalys och visualisering. Sparklines är minidiagram som du kan placera i celler så att du kan se data och diagram på samma tabell. När sparklines används på rätt sätt blir dataanalys snabbare och mer fokuserad. De ger också en enkel vy av information och undviker överfyllda arbetsblad med många upptagna diagram.

Aspose.Cells for Node.js via C++ tillhandahåller ett API för att manipulera sparklines i kalkylblad.
### **Sparklines i Microsoft Excel**
För att infoga sparklines i Microsoft Excel 2010:

1. Välj cellerna där du vill att sparklines ska visas. För att göra dem enkla att visa, välj celler bredvid datan.
1. Klicka på **Infoga** på menyn och välj sedan **kolumn** i **Sparklines** gruppen.
1. Välj eller ange cellområdet på arbetsbladet som innehåller källdata. Graferna kommer att visas.

Sparklines hjälper dig att se trender, till exempel vinst- eller förlustrekord för en softbolliga. Sparklines kan till och med summera hela säsongen för varje lag i ligan.
### **Sparklines med Aspose.Cells for Node.js via C++**
Utvecklare kan skapa, ta bort eller läsa sparklines (i mallfilen) med hjälp av API:et som tillhandahålls av Aspose.Cells for Node.js via C++. Klasserna som hanterar sparklines finns i [SparklineGroupCollection](https://reference.aspose.com/cells/nodejs-cpp/sparklinegroupcollection/)-modulen, så du måste inkludera denna modul innan du använder dessa funktioner.

Genom att lägga till anpassad grafik för ett givet dataområde har utvecklare friheten att lägga till olika typer av små diagram i utvalda cellområden.

Exemplet nedan demonstrerar funktionen Sparklines. Exemplet visar hur man:

1. Öppna en enkel mallfil.
1. Läs sparklinesinformation för ett arbetsblad.
1. Lägg till nya gnistrande linjer för ett givet datintervall till ett cellområde.
1. Spara Excel-filen på disk.


```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiate a Workbook
// Open a template file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "Book1.xlsx"));
// Get the first worksheet
const sheet = workbook.getWorksheets().get(0);

// Use the following lines if you need to read the Sparklines
// Read the Sparklines from the template file (if it has)
const sparklinesCount = sheet.getSparklineGroups().getCount();

for (let i = 0; i < sparklinesCount; i++)
{
const group = sheet.getSparklineGroups().get(i);
// Display the Sparklines group information e.g type, number of sparklines items
console.log(`sparkline group: type:${group.getType()}, sparkline items count:${group.getSparklines().getCount()}`);
const sparklineCount = sparklineGroup.getSparklines().getCount();
for (let j = 0; j < sparklineCount; j++) 
{
const sparkline = sparklineGroup.getSparklines().get(j);
// Display the individual Sparkines and the data ranges
console.log(`sparkline: row:${sparkline.getRow()}, col:${sparkline.getColumn()}, dataRange:${sparkline.getDataRange()}`);
}
}


// Add Sparklines
// Define the CellArea D2:D10
const ca = AsposeCells.CellArea.createCellArea(1, 4, 7, 4);
// Add new Sparklines for a data range to a cell area
const idx = sheet.getSparklineGroups().add(AsposeCells.SparklineType.Column, "Sheet1!B2:D8", false, ca);
const group = sheet.getSparklineGroups().get(idx);
// Create CellsColor
const clr = workbook.createCellsColor();
clr.setColor(AsposeCells.Color.Orange);
group.setSeriesColor(clr);

// Save the excel file
workbook.save(path.join(dataDir, "Book1.out.xlsx"));
```
## **Inställning 3D-format**
Du kan behöva 3D-diagramstilar för att få jobbresultaten för ditt scenario. Aspose.Cells for Node.js via C++ tillhandahåller det relevanta API:et för att tillämpa Microsoft Excel 2007 3D-formatering.

Ett komplett exempel ges nedan för att visa hur man skapar ett diagram och tillämpar Microsoft Excel 2007 3D-formatering. Efter att ha exekverat exempelkoden kommer ett stapeldiagram (med 3D-effekter) att läggas till på arbetsbladet.


```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "3d_format.out.xlsx");

// Instantiate a new Workbook
const book = new AsposeCells.Workbook();

// Add a Data Worksheet
const dataSheet = book.getWorksheets().add("DataSheet");

// Add Chart Worksheet
const sheet = book.getWorksheets().add("MyChart");

// Put some values into the cells in the data worksheet
dataSheet.getCells().get("B1").putValue(1);
dataSheet.getCells().get("B2").putValue(2);
dataSheet.getCells().get("B3").putValue(3);
dataSheet.getCells().get("A1").putValue("A");
dataSheet.getCells().get("A2").putValue("B");
dataSheet.getCells().get("A3").putValue("C");

// Define the Chart Collection
const charts = sheet.getCharts();
// Add a Column chart to the Chart Worksheet
const chartSheetIdx = charts.add(AsposeCells.ChartType.Column, 5, 0, 25, 15);

// Get the newly added Chart
const chart = book.getWorksheets().get(2).getCharts().get(0);

// Set the background/foreground color for PlotArea/ChartArea
chart.getPlotArea().getArea().setBackgroundColor(AsposeCells.Color.White);
chart.getChartArea().getArea().setBackgroundColor(AsposeCells.Color.White);
chart.getPlotArea().getArea().setForegroundColor(AsposeCells.Color.White);
chart.getChartArea().getArea().setForegroundColor(AsposeCells.Color.White);

// Hide the Legend
chart.setShowLegend(false);

// Add Data Series for the Chart
chart.getNSeries().add("DataSheet!B1:B3", true);
// Specify the Category Data
chart.getNSeries().setCategoryData("DataSheet!A1:A3");

// Get the Data Series
const ser = chart.getNSeries().get(0);

// Apply the 3-D formatting
const spPr = ser.getShapeProperties();
const fmt3d = spPr.getFormat3D();

// Specify Bevel with its height/width
const bevel = fmt3d.getTopBevel();
bevel.setType(AsposeCells.BevelPresetType.Circle);
bevel.setHeight(2);
bevel.setWidth(5);

// Specify Surface material type
fmt3d.setSurfaceMaterialType(AsposeCells.PresetMaterialType.WarmMatte);

// Specify surface lighting type
fmt3d.setSurfaceLightingType(AsposeCells.LightRigType.ThreePoint);

// Specify lighting angle
fmt3d.setLightingAngle(20);

// Specify Series background/foreground and line color
ser.getArea().setBackgroundColor(AsposeCells.Color.Maroon);
ser.getArea().setForegroundColor(AsposeCells.Color.Maroon);
ser.getBorder().setColor(AsposeCells.Color.Maroon);

// Save the Excel file
book.save(filePath);
```
