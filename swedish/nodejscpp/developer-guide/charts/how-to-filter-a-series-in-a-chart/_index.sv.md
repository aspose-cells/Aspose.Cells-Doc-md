---
title: Tre metoder för att filtrera diagramdata med Node.js via C++
linktitle: Tre metoder för att filtrera Diagramdata
description: Lär dig hur man filtrerar diagram i Excel med Aspose.Cells for Node.js via C++. Vår omfattande guide visar hur man tillämpar filter på diagram, anpassar diagramelement och använder dataanalysverktyg för bättre insikter och informerade beslut.
keywords: Aspose.Cells for Node.js via C++, Filtrera diagram i Excel, Dataanalys, Beslutsfattande, Visualisering.
type: docs
weight: 2210
url: /sv/nodejs-cpp/filtering-charts-in-excel/
---


## **1. Filtrera bort serier för att rendera ett diagram**

### **Steg för att filtrera serier från ett diagram i Excel**
I Excel kan vi filtrera ut specifika serier från ett diagram, vilket gör att dessa filtrerade serier inte visas i diagrammet. Det ursprungliga diagrammet visas i **Figur 1**. Men när vi filtrerar ut **Testseriek2** och **Testseriek4**, kommer diagrammet att se ut som i **Figur 2**.

I Aspose.Cells for Node.js via C++ kan vi utföra en liknande operation. För en [provfil](seriesFiltered.xlsx) som denna, om vi vill filtrera ut **Testseriek2** och **Testseriek4**, kan vi köra följande kod. Dessutom kommer vi att behålla två listor: en ([Chart.getNSeries()](https://reference.aspose.com/cells/nodejs-cpp/chart/#getNSeries--)) för att lagra alla valda serier.

![todo:image_alt_text](Figure1.png)

![todo:image_alt_text](Figure2.png)

### **Exempelkod**
Följande kodexempel laddar den [exempelfil i Excel](seriesFiltered.xlsx).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "seriesFiltered.xlsx");
// Create an instance of existing Workbook
let workbook = new AsposeCells.Workbook(filePath);
// Get filtered series list
let nSeriesFiltered = workbook.getWorksheets().get(0).getCharts().get("Chart 1").getFilteredNSeries();
// Get selected series list
let nSeries = workbook.getWorksheets().get(0).getCharts().get("Chart 1").getNSeries();
// Should be 0
console.log("Filtered Series count: " + nSeriesFiltered.getCount());
// Should be 6
console.log("Visible Series count: " + nSeries.getCount());
// Process from the end to the beginning
nSeries.get(1).setIsFiltered(true);
nSeries.get(0).setIsFiltered(true);
// Should be 2
console.log("Filtered Series count: " + nSeriesFiltered.getCount());
// Should be 4
console.log("Visible Series count: " + nSeries.getCount());
workbook.save("seriesFiltered-out.xlsx");
workbook = new AsposeCells.Workbook("seriesFiltered-out.xlsx");
// Should be 2
console.log("Filtered Series count: " + nSeriesFiltered.getCount());
// Should be 4
console.log("Visible Series count: " + nSeries.getCount());
```

## **2. Filtrera datan och låt diagrammet ändras**

Att filtrera dina data är ett bra sätt att hantera diagramfilter med mycket data. När du filtrerar data, förändras diagrammet. En lösning vi måste ta itu med är att se till att diagrammet stannar på skärmen. När du filtrerar får du dolda rader, och ibland är diagrammet i dessa dolda rader.

![todo:image_alt_text](Figure3.png)

### **Steg för att använda Datafilter för att ändra diagrammet i Excel**

1. Klicka inom ditt datarange.
2. Klicka på fliken **Data**, och slå på filter genom att klicka på Filter. Din rubrikrad kommer att ha nedrullningspilar.
3. Skapa ett diagram genom att gå till fliken **Infoga** och välja en kolumnsdiagram.
4. Filtrera nu din data med hjälp av nedrullningspilarna i datan. Använd inte Diagramfilter.

### **Exempelkod**
Följande exempel kod visar samma funktion med Aspose.Cells.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Create an instance of Worksheet
const sheet = workbook.getWorksheets().get("Sheet1");
// Add data into details cells.
sheet.getCells().get(0, 0).putValue("Fruits Name");
sheet.getCells().get(0, 1).putValue("Fruits Price");
sheet.getCells().get(1, 0).putValue("Apples");
sheet.getCells().get(2, 0).putValue("Bananas");
sheet.getCells().get(3, 0).putValue("Grapes");
sheet.getCells().get(4, 0).putValue("Oranges");
sheet.getCells().get(1, 1).putValue(5);
sheet.getCells().get(2, 1).putValue(2);
sheet.getCells().get(3, 1).putValue(1);
sheet.getCells().get(4, 1).putValue(4);

// Add a chart to the worksheet
const chartIndex = sheet.getCharts().add(AsposeCells.ChartType.Column, 7, 7, 15, 15);
// Access the instance of the newly added chart
const chart = sheet.getCharts().get(chartIndex);
// Set data range
chart.setChartDataRange("A1:B5", true);
// Set AutoFilter range
sheet.getAutoFilter().setRange("A1:B5");
// Add filters for a filter column.
sheet.getAutoFilter().addFilter(0, "Bananas");
sheet.getAutoFilter().addFilter(0, "Oranges");
// Apply the filters
sheet.getAutoFilter().refresh();
chart.toImage("Autofilter.png");
workbook.save("Autofilter.xlsx");
```

## **3. Filtrera datan med ett tabell och låt diagrammet ändras**

Att använda en tabell är liknande som metod 2, som använder ett intervall, men du har fördelar med tabeller över intervall. När du ändrar ditt intervall till en tabell och lägger till data, uppdateras diagrammet automatiskt. Med ett intervall måste du ändra datakällan.

### **Formatera som tabell i Excel**

Klicka inuti din data och använd **CTRL + T** eller använd fliken Hem, **Formatera som tabell**

![todo:image_alt_text](Figure4.png)

### **Exempelkod**
Följande exempelkod laddar [provfilen](TableFilters.xlsx) som visar samma funktion med Aspose.Cells.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "TableFilters.xlsx");
// Create a workbook.
const workbook = new AsposeCells.Workbook(filePath);
// Access first worksheet
const sheet = workbook.getWorksheets().get(0);
// Access the instance of the newly added chart
const chartIndex = sheet.getCharts().add(AsposeCells.ChartType.Column, 7, 7, 15, 15);
const chart = sheet.getCharts().get(chartIndex);
// Set data range
chart.setChartDataRange("A1:B7", true);
// Convert the chart to image
chart.toImage("TableFilters.before.png");
// Add a new List Object to the worksheet
const listObject = sheet.getListObjects().get(sheet.getListObjects().add("A1", "B7", true));
// Add default style to the table
listObject.setTableStyleType(AsposeCells.TableStyleType.TableStyleMedium10);
// Show Total
listObject.setShowTotals(false);
// Add filters for a filter column.
listObject.getAutoFilter().addFilter(0, "James");
// Apply the filters
listObject.getAutoFilter().refresh();
// After adding new value the chart will change
listObject.putCellValue(7, 0, "Me");
listObject.putCellValue(7, 1, 1000);
// Check the changed images
chart.toImage("TableFilters.after.png");
// Saving the Excel file
workbook.save("TableFilter.out.xlsx");
```
