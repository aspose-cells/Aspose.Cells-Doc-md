---  
title: Ställ in datakälla för diagrammet med Node.js via C++  
description: Lär dig om de olika datakällor som stöds av Aspose.Cells for Node.js via C++. Vår guide kommer att gå igenom de olika typer av datakällor som finns och visa hur du ansluter och hämtar data från dem för att fylla dina arbetsblad.  
keywords: Aspose.Cells for Node.js via C++, diagram, dataformatering, etiketter, färger, typsnitt, utseende, användarvänlighet.  
linktitle: Datakälla  
type: docs  
weight: 10  
url: /sv/nodejs-cpp/data-formatting-in-charts/  
---  

I våra tidigare ämnen har vi redan gett många exempel för att visa hur du kan ställa in en datakälla för ditt diagram men i detta ämne ska vi ge mer detaljer om de typer av data som kan ställas in för ett diagram.

## **Ställa in Diagramdata**

Det finns två typer av data att hantera när man arbetar med diagram med hjälp av Aspose.Cells som följer:

- Diagramdata.
- Kategoridata.

### **Diagramdata**

Diagramdata är den data vi använder som datakälla för att skapa våra diagram. Vi kan lägga till ett cellområde (innehållande diagramdata) genom att anropa [**SeriesCollection**](https://reference.aspose.com/cells/nodejs-cpp/seriescollection)-objektets [**add(string, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/seriescollection/#add-string-boolean-)-metod.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Adding a new worksheet to the Excel object
const sheetIndex = workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(sheetIndex);

// Adding sample values to cells
worksheet.getCells().get("A1").putValue(50);
worksheet.getCells().get("A2").putValue(100);
worksheet.getCells().get("A3").putValue(170);
worksheet.getCells().get("A4").putValue(300);
worksheet.getCells().get("B1").putValue(160);
worksheet.getCells().get("B2").putValue(32);
worksheet.getCells().get("B3").putValue(50);
worksheet.getCells().get("B4").putValue(40);

// Adding sample values to cells as category data
worksheet.getCells().get("C1").putValue("Q1");
worksheet.getCells().get("C2").putValue("Q2");
worksheet.getCells().get("C3").putValue("Y1");
worksheet.getCells().get("C4").putValue("Y2");

// Adding a chart to the worksheet
const chartIndex = worksheet.getCharts().add(AsposeCells.ChartType.Column, 5, 0, 15, 5);

// Accessing the instance of the newly added chart
const chart = worksheet.getCharts().get(chartIndex);

// Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B4"
chart.getNSeries().add("A1:B4", true);

// Saving the Excel file
workbook.save(path.join(dataDir, "output.xls"));
```

### **Kategoridata**

Kategoridata används för märkningsetiketter på diagramdata och kan läggas till i [**SeriesCollection**](https://reference.aspose.com/cells/nodejs-cpp/seriescollection) med dess [**getCategoryData()**](https://reference.aspose.com/cells/nodejs-cpp/seriescollection/#getCategoryData--)-egenskap. Ett komplett exempel ges nedan för att visa användningen av diagram- och kategoridata. Efter att ha kört ovanstående kodexempel kommer ett kolumn diagram att läggas till i arbetsbladet som visas nedan.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Adding a new worksheet to the Excel object
const sheetIndex = workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(sheetIndex);

// Adding sample values to cells
worksheet.getCells().get("A1").putValue(10);
worksheet.getCells().get("A2").putValue(100);
worksheet.getCells().get("A3").putValue(170);
worksheet.getCells().get("A4").putValue(200);
worksheet.getCells().get("B1").putValue(120);
worksheet.getCells().get("B2").putValue(320);
worksheet.getCells().get("B3").putValue(50);
worksheet.getCells().get("B4").putValue(40);

// Adding sample values to cells as category data
worksheet.getCells().get("C1").putValue("Q1");
worksheet.getCells().get("C2").putValue("Q2");
worksheet.getCells().get("C3").putValue("Y1");
worksheet.getCells().get("C4").putValue("Y2");

// Adding a chart to the worksheet
const chartIndex = worksheet.getCharts().add(AsposeCells.ChartType.Column, 5, 0, 15, 5);

// Accessing the instance of the newly added chart
const chart = worksheet.getCharts().get(chartIndex);

// Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B4"
chart.getNSeries().add("A1:B4", true);

// Setting the data source for the category data of SeriesCollection
chart.getNSeries().setCategoryData("C1:C4");

// Saving the Excel file
workbook.save(path.join(dataDir, "output.xls"));
```

## **Fortsatta ämnen**  
- [Ändra datakällan för diagrammet till destinationskalkylbladet samtidigt som du kopierar rader eller område](/cells/sv/nodejs-cpp/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/)  
- [Skapa Dynamiska Diagram](/cells/sv/nodejs-cpp/create-dynamic-charts/)  
- [Enkel metod för diagraminställning med hjälp av Chart.SetChartDataRange-metoden](/cells/sv/nodejs-cpp/easy-way-for-chart-setup-using-chart-setchartdatarange-method/)  
- [Hitta typ av X- och Y-värden för punkter i diagramserier](/cells/sv/nodejs-cpp/find-type-of-x-and-y-values-of-points-in-chart-series/)  
