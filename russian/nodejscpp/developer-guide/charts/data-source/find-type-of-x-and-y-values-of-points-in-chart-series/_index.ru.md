---  
title: Найти тип X и Y значений точек в серии диаграммы с помощью Node.js через C++  
linktitle: Найдите тип значений X и Y точек в серии графика  
description: Узнайте, как определить тип X и Y значений в точках серии диаграммы, используя Aspose.Cells for Node.js via C++. Наше руководство объясняет типы данных и как получить доступ к ним и работать с ними в ваших диаграммах.  
keywords: Aspose.Cells для Node.js, построение диаграмм, X значения, Y значения, типы данных, доступ, работа, серия диаграмм.  
type: docs  
weight: 150  
url: /ru/nodejs-cpp/find-type-of-x-and-y-values-of-points-in-chart-series/  
---  

## **Возможные сценарии использования**  
Иногда вы хотите узнать тип X и Y значений точек диаграммы в серии. Aspose.Cells for Node.js via C++ предоставляет свойства `ChartPoint.XValueType` и `ChartPoint.YValueType`, которые можно использовать для этой цели. Обратите внимание, что перед использованием этих свойств необходимо вызвать метод `Chart.calculate()`.  

## **Найдите тип значений X и Y точек в серии графика**  
Следующий пример кода загружает [пробный файл Excel](64716905.xlsx) и получает доступ к первой диаграмме внутри первого листа. Затем он вызывает метод `Chart.calculate()` и определяет типы X и Y значений первой точки диаграммы, выводя их в консоль. См. вывод в консоли ниже для справки.  

## **Образец кода**  
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

## **Вывод в консоль**  

{{< highlight java >}}  
 X Value Type: IsString  

Y Value Type: IsNumeric  
{{< /highlight >}}  

