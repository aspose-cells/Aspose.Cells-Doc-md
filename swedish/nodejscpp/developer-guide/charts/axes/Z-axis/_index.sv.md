---
title: Z axel med Node.js via C++
description: Lär dig hur du arbetar med Z axeln i Aspose.Cells for Node.js via C++. Vår guide hjälper dig att förstå hur du konfigurerar och anpassar Z axeln, inklusive dess skala och etiketter, för att förbättra diagrammen.
keywords: Aspose.Cells for Node.js via C++, Z axel, diagramkonstruktion, konfiguration, anpassning, skala, etiketter.
type: docs
weight: 210
url: /sv/nodejs-cpp/z-axis/
---

## **Möjliga användningsscenario**
För vissa 3D-diagram, såsom 3D-kolumn, 3D-kon eller 3D-pyramid som har en djup- (serier) axel, även känd som Z-axeln, kan du ändra den. Du kan ange intervallen mellan märkestickor, axelrubriker och andra operationer.

## **Hantera primär och sekundär axel som i Microsoft Excel**
Se följande exempel som skapar en ny Excel-fil och placerar värden av diagrammet i det första arket. Sedan lägger vi till ett diagram och ställer in diagramtypen till Column3D, då kan du även se Z-axeln, också kallad Djupaxeln. 

![todo:image_alt_text](excel.png)

## **Exempelkod**
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);
// Get the first worksheet
const worksheet = workbook.getWorksheets().get(0);
// Put values to cells for creating chart
worksheet.getCells().get("A1").putValue("A");
worksheet.getCells().get("B1").putValue("B");
worksheet.getCells().get("C1").putValue("C");
worksheet.getCells().get("A2").putValue(2);
worksheet.getCells().get("A3").putValue(1);
worksheet.getCells().get("B2").putValue(2);
worksheet.getCells().get("B3").putValue(3);
worksheet.getCells().get("C2").putValue(2);
worksheet.getCells().get("C3").putValue(3);
// Add a chart to the worksheet
const chartIndex = worksheet.getCharts().add(AsposeCells.ChartType.Column3D, 9, 6, 25, 16);
// Access the instance of the newly added chart
const chart = worksheet.getCharts().get(chartIndex);
// Calculate the chart
chart.calculate();
// Add SeriesCollection (chart data source) to the chart ranging from "A2" cell to "C3"
chart.setChartDataRange("A2:C3", true);
// Hide the CategoryAxis axis
chart.getCategoryAxis().setIsVisible(false);
// Hide the ValueAxis axis
chart.getValueAxis().setIsVisible(false);
// Save the file
workbook.save("ZAxis.xlsx");
```
{{< app/cells/assistant language="nodejs-cpp" >}}
