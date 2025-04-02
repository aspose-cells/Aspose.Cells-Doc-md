---  
title: Find if Data Points are in the Second Pie or Bar on a Pie of Pie or Bar of Pie Chart with Node.js via C++  
linktitle: Find if Data Points are in the Second Pie or Bar on a Pie of Pie or Bar of Pie Chart  
description: Learn how to use Aspose.Cells for Node.js via C++ to find if data points are in the second pie or bar on a pie of pie or bar of pie chart. This guide will demonstrate how to identify and access the secondary pie or bar on a composite chart, allowing you to analyze and manipulate the data effectively.  
keywords: Aspose.Cells for Node.js via C++, Pie of Pie Chart, Bar of Pie Chart, Secondary Pie, Secondary Bar, Data Analysis, Data Manipulation.  
type: docs  
weight: 180  
url: /nodejs-cpp/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/  
---  

## **Possible Usage Scenarios**  
You can find if data points of series are in the second pie on *Pie of Pie* chart or in the bar of *Bar of Pie* chart using Aspose.Cells for Node.js via C++. Please use the [ChartPoint.isInSecondaryPlot()](https://reference.aspose.com/cells/nodejs-cpp/chartpoint/#isInSecondaryPlot--) property to determine it.  

Please download the [sample excel file](5115193.xlsx) used in the following sample code and see its console output. If you open the [sample excel file](5115193.xlsx), you will find all the data points which are less than 10 are inside the bar of *Bar of Pie* chart as also shown by console output.  
## **Find if Data Points are in the Second Pie or Bar on a Pie of Pie or Bar of Pie Chart**  
The following sample code shows how to find if data points are in the second pie or bar on a *Pie of Pie* or *Bar of Pie* chart.  

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
## **Console Output**  
Please see the following console output generated after the execution of the above sample code with the [sample excel file](5115193.xlsx). If [ChartPoint.isInSecondaryPlot()](https://reference.aspose.com/cells/nodejs-cpp/chartpoint/#isInSecondaryPlot--) is **false**, the data point is inside the Pie or if it is **true**, then the data point is inside the Bar.  

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
  