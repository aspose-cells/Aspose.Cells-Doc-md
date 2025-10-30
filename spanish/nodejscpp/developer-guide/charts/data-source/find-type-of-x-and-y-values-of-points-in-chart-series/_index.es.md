---  
title: Encontrar el tipo de valores de X y Y de los puntos en la serie del gráfico con Node.js a través de C++  
linktitle: Encontrar el tipo de valores X e Y de los puntos en la serie del gráfico  
description: Aprende cómo determinar el tipo de valores X e Y en los puntos de la serie del gráfico usando Aspose.Cells for Node.js via C++. Esta guía explica los tipos de datos y cómo acceder y trabajar con ellos en tus gráficos.  
keywords: Aspose.Cells para Node.js, gráficos, valores X, valores Y, tipos de datos, acceso, trabajo con, serie del gráfico.  
type: docs  
weight: 150  
url: /es/nodejs-cpp/find-type-of-x-and-y-values-of-points-in-chart-series/  
---  

## **Escenarios de uso posibles**  
A veces quieres conocer el tipo de valores X e Y en los puntos de una serie del gráfico. Aspose.Cells for Node.js via C++ proporciona las propiedades `ChartPoint.XValueType` y `ChartPoint.YValueType` que pueden usarse para este propósito. Ten en cuenta que deberás llamar al método `Chart.calculate()` antes de poder usar estas propiedades de manera efectiva.  

## **Encontrar el tipo de valores X e Y de los puntos en la serie del gráfico**  
El siguiente código de ejemplo carga el [archivo de ejemplo en Excel](64716905.xlsx) y accede al primer gráfico dentro de la primera hoja. Luego llama al método `Chart.calculate()` y encuentra el tipo de valores X e Y del primer punto del gráfico, imprimiéndolos en la consola. Consulta la salida de la consola a continuación como referencia.  

## **Código de muestra**  
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

## **Salida de la consola**  

{{< highlight java >}}  
 X Value Type: IsString  

Y Value Type: IsNumeric  
{{< /highlight >}}  

{{< app/cells/assistant language="nodejs-cpp" >}}
