---  
title: Hantera Axes i Excel diagram med Node.js via C++  
description: Lär dig hur man konfigurerar diagramaxlar i Aspose.Cells for Node.js via C++. Vår guide visar hur man justerar primära och sekundära axlar, sätter deras intervall och modifierar deras egenskaper för att förbättra dina diagram.  
keywords: Aspose.Cells for Node.js via C++, diagramaxlar, konfiguration, primära axlar, sekundära axlar, intervall, egenskaper.  
linktitle: Axlar  
type: docs  
weight: 50  
url: /sv/nodejs-cpp/chart-axes/  
---  

{{% alert color="primary" %}}  

I Excel-diagram finns det 3 typer av axlar:  
1. Horisontell (Kategori) Axel : X-Axel  
2. Vertikal (Värde) Axel : Y-axel  
3. Djup (Serie) Axel : Z-axel  

{{% /alert %}}  

## **Axelealternativ**  
Aspose.Cells for Node.js via C++ tillåter dig också att hantera diagramaxlar vid körning. Med [Axis](https://reference.aspose.com/cells/nodejs-cpp/axis/) objekt kan du ändra alla alternativ för Axis som görs i Excel.  

|![todo:image_alt_text](chart_axes.png)|  

## **Hantera X- och Y-axlar**  
I Excel-diagram är horisontella och vertikala axlar de två mest populära att använda.  

Följande kodsnutt visar hur man ställer in alternativen för X- och Y-axlar.  

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "chart_axes.xlsx");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Adding a new worksheet to the Workbook object
const sheetIndex = workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(sheetIndex);

// Adding sample values to cells
worksheet.getCells().get("A1").putValue("Series1");
worksheet.getCells().get("A2").putValue(50);
worksheet.getCells().get("A3").putValue(100);
worksheet.getCells().get("A4").putValue(150);
worksheet.getCells().get("B1").putValue("Series2");
worksheet.getCells().get("B2").putValue(60);
worksheet.getCells().get("B3").putValue(32);
worksheet.getCells().get("B4").putValue(50);

// Adding a chart to the worksheet
const chartIndex = worksheet.getCharts().add(AsposeCells.ChartType.Column, 5, 0, 15, 5);

// Accessing the instance of the newly added chart
const chart = worksheet.getCharts().get(chartIndex);
// Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B4"
chart.setChartDataRange("A1:B4", true);

// Hiding X axis
chart.getCategoryAxis().setIsVisible(false);

// Setting max value of Y axis
chart.getValueAxis().setMaxValue(200);
// Setting major unit
chart.getValueAxis().setMajorUnit(50);

// Save the file
workbook.save(filePath);
```  

## **Fortsatta ämnen**  
- [Ändra riktning för ticketiketter](/cells/sv/nodejs-cpp/change-tick-label-direction/)  
- [Bestäm vilken axel som finns i diagrammet](/cells/sv/nodejs-cpp/determine-which-axis-exists-in-the-chart/)  
- [Hantera automatiska enheter för diagramaxeln som Microsoft Excel](/cells/sv/nodejs-cpp/handle-automatic-units-of-chart-axis-like-microsoft-excel/)  
- [Läs av axeletiketter efter att ha beräknat diagrammet](/cells/sv/nodejs-cpp/read-axis-labels-after-calculating-the-chart/)  
- [Hur man ställer in kategoriaxel i Excel-diagram](/cells/sv/nodejs-cpp/how-to-set-category-axis/)  

{{< app/cells/assistant language="nodejs-cpp" >}}
