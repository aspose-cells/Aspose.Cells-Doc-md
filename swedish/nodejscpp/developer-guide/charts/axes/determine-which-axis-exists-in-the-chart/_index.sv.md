---  
title: Bestäm vilken axel som finns i diagrammet med Node.js via C++  
linktitle: Bestäm vilken axel som finns i diagrammet  
description: Lär dig hur du bestämmer vilken axel som finns i ett diagram som skapats med Aspose.Cells for Node.js via C++. Vår guide hjälper dig att identifiera och komma åt de olika axlarna i ett diagram, inklusive kategori , värde och sekundära axlar.  
keywords: Aspose.Cells för Node.js, diagram, axel, förekomst, kategori, värde, sekundär.  
type: docs  
weight: 140  
url: /sv/nodejs-cpp/determine-which-axis-exists-in-the-chart/  
---  

{{% alert color="primary" %}}  
Ibland behöver användaren veta om en viss axel finns i diagrammet. Till exempel vill de veta om en sekundär värdeaxel finns i diagrammet eller inte. Vissa diagram som Pie, PieExploded, PiePie, PieBar, Pie3D, Pie3DExploded, Doughnut, DoughnutExploded, etc. har inte någon axel.  

Aspose.Cells tillhandahåller [**Chart.hasAxis(axisType, isPrimary)**](https://reference.aspose.com/cells/nodejs-cpp/chart/#hasAxis-AxisType-boolean-) metod för att avgöra om diagrammet har en specifik axel eller inte.  
{{% /alert %}}  

 Följande kodexempel demonstrerar användningen av [**Chart.hasAxis(axisType, isPrimary)**](https://reference.aspose.com/cells/nodejs-cpp/chart/#hasAxis-AxisType-boolean-) för att avgöra om diagrammet har primär och sekundär kategori- och värdeaxel.  

## Node.js-kod för att avgöra vilken axel som finns i diagrammet  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "source.xlsx");
// Create workbook object
const workbook = new AsposeCells.Workbook(filePath);

// Access the first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Check if there are any charts before accessing
const charts = worksheet.getCharts();
if (charts.getCount() === 0) {
console.log("No charts found in the worksheet.");
return;
}

// Access the chart
const chart = charts.get(0);

// Determine which axis exists in chart
let ret = chart.hasAxis(AsposeCells.AxisType.Category, true);
console.log("Has Primary Category Axis: " + ret);

ret = chart.hasAxis(AsposeCells.AxisType.Category, false);
console.log("Has Secondary Category Axis: " + ret);

ret = chart.hasAxis(AsposeCells.AxisType.Value, true);
console.log("Has Primary Value Axis: " + ret);

ret = chart.hasAxis(AsposeCells.AxisType.Value, false);
console.log("Has Secondary Value Axis: " + ret);
```  

## Konsolutdata som genereras av exempelkoden  

Körresultatet av koden visas nedan, vilket visar sant för Primär Kategori- och Värdeaxel och falskt för Sekundär Kategori- och Värdeaxel.  

{{< highlight java >}}  
Has Primary Category Axis: True  
Has Secondary Category Axis: False  
Has Primary Value Axis: True  
Has Secondary Value Axis: False  
{{< /highlight >}}  
