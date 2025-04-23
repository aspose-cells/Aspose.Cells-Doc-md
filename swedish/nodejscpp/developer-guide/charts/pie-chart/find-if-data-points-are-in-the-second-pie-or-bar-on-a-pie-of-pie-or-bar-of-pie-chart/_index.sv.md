---  
title: Hitta om datapunkter är i den andra cirkeln eller stapeln på en pie of pie eller bar of pie diagram med Node.js via C++  
linktitle: Ta reda på om datapunkterna finns i den andra pajen eller stapeln på ett paj eller stapeldiagram  
description: Lär dig att använda Aspose.Cells for Node.js via C++ för att hitta om datapunkter är i den andra cirkeln eller stapeln på ett pie of pie eller bar of pie diagram. Denna guide visar hur man identifierar och får åtkomst till sekundära cirklar eller staplar i ett sammansatt diagram för effektiv analys och manipulation av data.  
keywords: Aspose.Cells for Node.js via C++, Pie of Pie diagram, Bar of Pie diagram, Sekundär cirkel, Sekundär stapel, Dataanalys, Datarangling.  
type: docs  
weight: 180  
url: /sv/nodejs-cpp/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/  
---  

## **Möjliga användningsscenario**  
 Du kan avgöra om datapunkter i serie är i den andra cirkeln på *Pie of Pie*-diagram eller i bars av *Bar of Pie*-diagrammet med Aspose.Cells for Node.js via C++. Använd gärna egenskapen [ChartPoint.isInSecondaryPlot()](https://reference.aspose.com/cells/nodejs-cpp/chartpoint/#isInSecondaryPlot--) för att bestämma det.  

Hämta gärna [exempelfilen i Excel](5115193.xlsx) som används i följande exempel och se dess konsolutdata. Om du öppnar [exempelfilen i Excel](5115193.xlsx), kommer du att hitta alla datapunkter mindre än 10 som är inuti stapeln för *Bar of Pie*-diagrammet, som också visas av konsolutdata.  
## **Ta reda på om datapunkterna finns i den andra pajen eller stapeln på ett paj- eller stapeldiagram**  
 Följande exempel visar hur man avgör om datapunkter är i den andra cirkeln eller stapeln på ett *Pie of Pie* eller *Bar of Pie*-diagram.  

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
## **Konsoloutput**  
 Se den följande konsolutdata som genererats efter körning av ovanstående exempel med [exempelfilen i Excel](5115193.xlsx). Om [ChartPoint.isInSecondaryPlot()](https://reference.aspose.com/cells/nodejs-cpp/chartpoint/#isInSecondaryPlot--) är **falskt**, är datapunkten innanför cirkeln, annars är den innanför stapeln.  

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

