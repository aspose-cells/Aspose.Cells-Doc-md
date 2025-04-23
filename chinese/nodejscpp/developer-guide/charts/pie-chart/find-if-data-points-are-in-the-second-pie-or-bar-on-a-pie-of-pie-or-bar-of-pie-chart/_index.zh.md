---  
title: 使用Node.js通过C++在饼图或饼状图中的第二个饼或柱子中查找数据点  
linktitle: 查找数据点是否在饼图的第二个饼图或柱状图的柱状图上  
description: 学习如何使用Aspose.Cells for Node.js via C++查找数据点是否在饼图或饼状图的第二个饼或柱子中。本指南将演示如何识别和访问复合图表中的次级饼或柱，以便有效分析和操作数据。  
keywords: Aspose.Cells for Node.js via C++，饼图中的饼，柱状图中的柱，次级饼，次级柱，数据分析，数据操作。  
type: docs  
weight: 180  
url: /zh/nodejs-cpp/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/  
---  

## **可能的使用场景**  
你可以使用Aspose.Cells for Node.js via C++找到系列数据点是否在*饼的饼*图的第二个饼中或在*饼的柱*图的柱中。请使用[ChartPoint.isInSecondaryPlot()](https://reference.aspose.com/cells/nodejs-cpp/chartpoint/#isInSecondaryPlot--)属性来判断。  

请下载[示例Excel文件](5115193.xlsx)，并查看其控制台输出。若打开该文件，你会发现所有值小于10的数据点都在*饼的柱*图的柱内，如控制台输出所示。  
## **查找数据点是否在饼图的第二个饼图或柱状图的柱状图上**  
以下示例代码展示了如何判断数据点是否在*饼的饼*或*饼的柱*图中的第二个饼或柱子。  

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
## **控制台输出**  
请参阅在执行上述示例代码后，用[示例Excel文件](5115193.xlsx)生成的控制台输出。如果[ChartPoint.isInSecondaryPlot()](https://reference.aspose.com/cells/nodejs-cpp/chartpoint/#isInSecondaryPlot--)返回**false**，表示数据点在饼内；若为**true**，则在柱内。  

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

