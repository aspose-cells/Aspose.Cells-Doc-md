---  
title: Prüfen, ob Datenpunkte in der zweiten Scheibe oder im Balken eines Pie of Pie oder Bar of Pie Diagramms mit Node.js via C++ sind  
linktitle: Feststellen, ob Datenauswahl in der zweiten Torte oder Balken in einem Tortendiagramm oder Balkendiagramm aufgeführt ist  
description: Lernen Sie, wie Sie mit Aspose.Cells for Node.js via C++ feststellen, ob Datenpunkte in der zweiten Scheibe oder im Balken eines Pie of Pie oder Bar of Pie Diagramms liegen. Dieser Leitfaden zeigt, wie man den sekundären Kreis oder Balken auf einem zusammengesetzten Diagramm identifiziert und darauf zugreift, um die Daten effektiv zu analysieren und zu manipulieren.  
keywords: Aspose.Cells for Node.js via C++, Pie of Pie Chart, Bar of Pie Chart, Sekundärer Kreis, Sekundärer Balken, Datenanalyse, Datenmanipulation.  
type: docs  
weight: 180  
url: /de/nodejs-cpp/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/  
---  

## **Mögliche Verwendungsszenarien**  
Sie können feststellen, ob die Datenpunkte einer Serie in der zweiten Scheibe eines *Pie of Pie*-Diagramms oder im Balken eines *Bar of Pie*-Diagramms mit Aspose.Cells for Node.js via C++ liegen. Bitte verwenden Sie die Eigenschaft [ChartPoint.isInSecondaryPlot()](https://reference.aspose.com/cells/nodejs-cpp/chartpoint/#isInSecondaryPlot--) , um dies zu bestimmen.  

Bitte laden Sie die [Beispieldatei Excel](5115193.xlsx) herunter, die im folgenden Beispielcode verwendet wird, und sehen Sie sich die Konsolenausgabe an. Wenn Sie die [Beispieldatei Excel](5115193.xlsx) öffnen, finden Sie alle Datenpunkte, die kleiner als 10 sind, innerhalb des Balkens des *Bar of Pie*-Diagramms, wie auch die Konsolenausgabe zeigt.  
## **Herausfinden, ob Datenpunkte in der zweiten Torte oder Balken in einem Tortendiagramm der Torten oder Balken sind**  
Das folgende Beispiel zeigt, wie man feststellt, ob Datenpunkte in der zweiten Scheibe oder im Balken eines *Pie of Pie*- oder *Bar of Pie*-Diagramms liegen.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Load source excel file containing Bar of Pie chart
const workbook = new AsposeCells.Workbook(path.join(dataDir, "PieBars.xlsx"));

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access first chart which is Bar of Pie chart and calculate it
const chart = worksheet.getCharts().get(0);
chart.calculate();

// Access the chart series
const series = chart.getNSeries().get(0);

/* 
* Print the data points of the chart series and 
* check its IsInSecondaryPlot property to determine 
* if data point is inside the bar or pie 
*/
for (let i = 0; i < series.getPoints().getCount(); i++) {
// Access chart point
const chartPoint = series.getPoints().get(i);

// Skip null values
if (chartPoint.get_YValue() === null) continue;

/* 
* Print the chart point value and see if it is inside bar or pie.
* If the IsInSecondaryPlot is true, then the data point is inside bar 
* otherwise it is inside the pie. 
*/
console.log("Value: " + chartPoint.get_YValue());
console.log("IsInSecondaryPlot: " + chartPoint.isInSecondaryPlot());
console.log();
}
```  
## **Konsolenausgabe**  
Bitte sehen Sie die folgende Konsolenausgabe nach Ausführung des obigen Beispielcodes mit der [Beispieldatei Excel](5115193.xlsx). Wenn [ChartPoint.isInSecondaryPlot()](https://reference.aspose.com/cells/nodejs-cpp/chartpoint/#isInSecondaryPlot--) **falsch** ist, befindet sich der Datenpunkt im Kreis, andernfalls im Balken.  

{{< highlight javascript >}}  
 Value: 15  
IsInSecondaryPlot: false  

Value: 9  
IsInSecondaryPlot: true  

Value: 2  
IsInSecondaryPlot: true  

Value: 40  
IsInSecondaryPlot: false  

Value: 5  
IsInSecondaryPlot: true  

Value: 4  
IsInSecondaryPlot: true  

Value: 25  
IsInSecondaryPlot: false  
{{< /highlight >}}  

