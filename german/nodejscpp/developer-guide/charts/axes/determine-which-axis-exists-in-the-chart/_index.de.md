---  
title: Bestimmen, welche Achse im Diagramm vorhanden ist mit Node.js über C++  
linktitle: Bestimmen Sie, welche Achse im Diagramm vorhanden ist  
description: Erfahren Sie, wie Sie feststellen, welche Achse in einem mit Aspose.Cells for Node.js via C++ erstellten Diagramm vorhanden ist. Unser Leitfaden hilft Ihnen, die verschiedenen Achsen in einem Diagramm zu identifizieren und darauf zuzugreifen, einschließlich Kategorie , Wert und Sekundärachsen.  
keywords: Aspose.Cells für Node.js, Diagramm, Achse, Vorhandensein, Kategorie, Wert, Sekundär.  
type: docs  
weight: 140  
url: /de/nodejs-cpp/determine-which-axis-exists-in-the-chart/  
---  

{{% alert color="primary" %}}  
Manchmal muss der Nutzer wissen, ob eine bestimmte Achse im Diagramm vorhanden ist. Zum Beispiel, ob eine Sekundär-Wertachse im Diagramm vorhanden ist oder nicht. Einige Diagramme wie Kreis, Explodierter Kreis, Pfeil-Kreis, Kreisbalken, 3D-Kreis, 3D-Explodierter Kreis, Donut, Explodierter Donut usw. haben keine Achse.  

Aspose.Cells stellt die Methode [**Chart.hasAxis(axisType, isPrimary)**](https://reference.aspose.com/cells/nodejs-cpp/chart/#hasAxis-AxisType-boolean-) bereit, um festzustellen, ob das Diagramm eine bestimmte Achse hat oder nicht.  
{{% /alert %}}  

Das folgende Beispiel zeigt, wie [**Chart.hasAxis(axisType, isPrimary)**](https://reference.aspose.com/cells/nodejs-cpp/chart/#hasAxis-AxisType-boolean-) verwendet wird, um zu bestimmen, ob das Beispiel-Diagramm primäre und sekundäre Kategorie- und Wertachsen hat.  

## Node.js-Code zur Bestimmung, welche Achse im Diagramm vorhanden ist  

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

## Von dem Beispielcode generierte Konsolenausgabe  

Der Konsolenausdruck des Codes ist unten dargestellt und zeigt `true` für die Primäre Kategorie- und Wertachse sowie `false` für die Sekundäre Kategorie- und Wertachse.  

{{< highlight java >}}  
Has Primary Category Axis: True  
Has Secondary Category Axis: False  
Has Primary Value Axis: True  
Has Secondary Value Axis: False  
{{< /highlight >}}  
{{< app/cells/assistant language="nodejs-cpp" >}}
