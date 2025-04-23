---  
title: Hitta Typ av X och Y värden för punkter i diagramserie med Node.js via C++  
linktitle: Hitta typ av X och Y värden för punkter i diagramserier  
description: Lär dig hur du bestämmer typen av X och Y värden i diagramseriepunkter med Aspose.Cells for Node.js via C++. Denna guide förklarar typer av datavärden och hur du får tillgång till och arbetar med dem i dina diagram.  
keywords: Aspose.Cells för Node.js, diagram, X värden, Y värden, datatyper, åtkomst, arbete med, diagramserie.  
type: docs  
weight: 150  
url: /sv/nodejs-cpp/find-type-of-x-and-y-values-of-points-in-chart-series/  
---  

## **Möjliga användningsscenario**  
Ibland vill du veta typen av X- och Y-värden för diagrampunkter i en serie. Aspose.Cells for Node.js via C++ erbjuder egenskaperna `ChartPoint.XValueType` och `ChartPoint.YValueType` som kan användas för detta ändamål. Observera att du måste anropa `Chart.calculate()`-metoden innan du kan använda dessa egenskaper effektivt.  

## **Hitta typ av X- och Y-värden för punkter i diagramserier**  
Följande exempel kod laddar filen [exempel Excel](64716905.xlsx) och kommer åt den första diagrammet i den första arbetsboken. Den anropar sedan `Chart.calculate()`, avgör typen av X- och Y-värden för den första diagrampunkten och skriver ut dem i konsolen. Se nedan exempel på konsolutmatning för referens.  

## **Exempelkod**  
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const sourceDir = path.join(__dirname, "data");
// Load sample Excel file containing chart.
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "sampleFindTypeOfXandYValuesOfPointsInChartSeries.xlsx"));

// Access first worksheet.
const worksheet = workbook.getWorksheets().get(0);

// Access first chart.
const chart = worksheet.getCharts().get(0);

// Calculate chart data.
chart.calculate();

// Access first chart point in the first series.
const point = chart.getNSeries().get(0).getPoints().get(0);

// Print the types of X and Y values of chart point.
console.log("X Value Type: " + point.getXValueType());
console.log("Y Value Type: " + point.getYValueType());
```  

## **Konsoloutput**  

{{< highlight java >}}  
 X Value Type: IsString  

Y Value Type: IsNumeric  
{{< /highlight >}}  

