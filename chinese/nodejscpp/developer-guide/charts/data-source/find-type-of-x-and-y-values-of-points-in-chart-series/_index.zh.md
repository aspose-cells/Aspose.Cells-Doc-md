---  
title: 通过Node.js在C++中找到图表系列中点的X值和Y值的类型  
linktitle: 查找图表系列中点的X和Y值类型  
description: 学习如何在Aspose.Cells for Node.js via C++中确定图表系列点的X值和Y值的类型。本指南解释了数据值的类型以及如何访问和操作它们。  
keywords: Aspose.Cells for Node.js、图表、X值、Y值、数据类型、访问、操作、图表系列。  
type: docs  
weight: 150  
url: /zh/nodejs-cpp/find-type-of-x-and-y-values-of-points-in-chart-series/  
---  

## **可能的使用场景**  
有时你想知道系列中点的X值和Y值的类型。Aspose.Cells for Node.js via C++提供了`ChartPoint.XValueType`和`ChartPoint.YValueType`属性用以此用途。请注意，在有效使用这些属性之前，必须调用`Chart.calculate()`方法。  

## **查找图表系列中点的X和Y值类型**  
以下示例代码加载了[示例Excel文件](64716905.xlsx)，访问了第一个工作表中的第一个图表，然后调用`Chart.calculate()`方法，并找出第一个图表点的X值和Y值类型，并在控制台输出。请参考下面的控制台输出。  

## **示例代码**  
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

## **控制台输出**  

{{< highlight java >}}  
 X Value Type: IsString  

Y Value Type: IsNumeric  
{{< /highlight >}}  

