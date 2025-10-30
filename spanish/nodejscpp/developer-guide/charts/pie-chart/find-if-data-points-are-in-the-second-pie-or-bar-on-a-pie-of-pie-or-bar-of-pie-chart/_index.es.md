---  
title: Encontrar si los puntos de datos están en la segunda tarta o barra en un gráfico de Pie de Pie o Bar de Pie con Node.js mediante C++  
linktitle: Encuentre si los Puntos de Datos están en el Segundo Círculo o Barra en un Gráfico de Círculo de Círculos o Barra de Círculos  
description: Aprende cómo usar Aspose.Cells for Node.js via C++ para determinar si los puntos de datos están en la segunda tarta o barra en un gráfico de Pie de Pie o Bar de Pie. Esta guía demostrará cómo identificar y acceder a la tarta o barra secundaria en un gráfico compuesto, permitiéndote analizar y manipular los datos eficazmente.  
keywords: Aspose.Cells for Node.js via C++, Gráfico de Pie de Pie, Gráfico de Barra de Pie, Segunda Tarta, Segunda Barra, Análisis de Datos, Manipulación de Datos.  
type: docs  
weight: 180  
url: /es/nodejs-cpp/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/  
---  

## **Escenarios de uso posibles**  
Puedes determinar si los puntos de datos de la serie están en la segunda tarta en el gráfico *Pie of Pie* o en la barra en el gráfico *Bar of Pie* usando Aspose.Cells for Node.js via C++. Por favor, usa la propiedad [ChartPoint.isInSecondaryPlot()](https://reference.aspose.com/cells/nodejs-cpp/chartpoint/#isInSecondaryPlot--) para determinarlo.  

Por favor, descarga el [archivo Excel de ejemplo](5115193.xlsx) utilizado en el siguiente código de ejemplo y revisa su salida en la consola. Si abres el [archivo Excel de ejemplo](5115193.xlsx), encontrarás que todos los puntos de datos menores a 10 están dentro de la barra del gráfico *Bar of Pie* como también especifica la salida en consola.  
## **Encontrar si los Puntos de Datos están en el Segundo Pastel o Barra en un Gráfico de Pastel de Pastel o de Barra de Pastel**  
El siguiente código de ejemplo muestra cómo determinar si los puntos de datos están en la segunda tarta o barra en un gráfico *Pie of Pie* o *Bar of Pie*.  

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
## **Salida de la consola**  
Por favor, revisa la salida en consola generada después de ejecutar el código de ejemplo con el [archivo Excel de muestra](5115193.xlsx). Si [ChartPoint.isInSecondaryPlot()](https://reference.aspose.com/cells/nodejs-cpp/chartpoint/#isInSecondaryPlot--) es **falso**, el punto de datos está dentro de la Tarta, y si es **verdadero**, entonces el punto de datos está dentro de la Barra.  

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

{{< app/cells/assistant language="nodejs-cpp" >}}
