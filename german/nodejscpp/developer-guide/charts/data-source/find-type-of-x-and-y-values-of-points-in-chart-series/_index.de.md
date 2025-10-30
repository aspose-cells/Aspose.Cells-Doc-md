---  
title: Bestimmen des Typs von X und Y Werten von Punkten in Diagrammserien mit Node.js via C++  
linktitle: Suchen Sie nach dem Typ von X und Y Werten der Punkte in der Diagrammserie  
description: Lernen Sie, wie Sie den Typ der X und Y Werte in Diagrammserienpunkten mithilfe von Aspose.Cells for Node.js via C++ bestimmen. Dieser Leitfaden erklärt die Arten von Datenwerten und wie man sie in Ihren Diagrammen abruft und verarbeitet.  
keywords: Aspose.Cells für Node.js, Diagramme, X Werte, Y Werte, Datentypen, Zugriff, Arbeit mit, Diagrammserien.  
type: docs  
weight: 150  
url: /de/nodejs-cpp/find-type-of-x-and-y-values-of-points-in-chart-series/  
---  

## **Mögliche Verwendungsszenarien**  
Manchmal möchten Sie den Typ der X- und Y-Werte von Punkten in einer Serie kennen. Aspose.Cells for Node.js via C++ bietet die Eigenschaften `ChartPoint.XValueType` und `ChartPoint.YValueType`, die dafür verwendet werden können. Bitte beachten Sie, dass Sie die Methode `Chart.calculate()` aufrufen müssen, bevor Sie diese Eigenschaften effektiv nutzen können.  

## **Typen von X- und Y-Werten von Punkten in Diagrammserien herausfinden**  
Der folgende Beispielcode lädt die [Beispieldatei Excel](64716905.xlsx) und greift auf das erste Diagramm im ersten Arbeitsblatt zu. Anschließend ruft er die Methode `Chart.calculate()` auf und ermittelt den Typ der X- und Y-Werte des ersten Diagrammpunkts, den er in der Konsole ausgibt. Bitte sehen Sie sich die unten angezeigte Konsolenausgabe zur Referenz an.  

## **Beispielcode**  
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

## **Konsolenausgabe**  

{{< highlight java >}}  
 X Value Type: IsString  

Y Value Type: IsNumeric  
{{< /highlight >}}  

{{< app/cells/assistant language="nodejs-cpp" >}}
