---  
title: Determinar qué Eje existe en el Gráfico con Node.js vía C++  
linktitle: Determinar qué eje existe en el gráfico  
description: Aprende cómo determinar qué eje existe en un gráfico creado con Aspose.Cells for Node.js via C++. Nuestra guía te ayudará a identificar y acceder a los diferentes ejes en un gráfico, incluyendo los ejes de categoría, valor y secundario.  
keywords: Aspose.Cells para Node.js, gráfico, eje, existencia, categoría, valor, secundario.  
type: docs  
weight: 140  
url: /es/nodejs-cpp/determine-which-axis-exists-in-the-chart/  
---  

{{% alert color="primary" %}}  
A veces, el usuario necesita saber si un eje en particular existe en el Gráfico. Por ejemplo, quieren saber si un Eje de Valor Secundario existe dentro del gráfico o no. Algunos gráficos como Pastel, Pastel Explotado, Pastel Pastel, Pastel Barra, Pastel 3D, Pastel 3D Explotado, Rosquilla, Rosquilla Explotada, etc., no tienen eje.  

Aspose.Cells proporciona [**Chart.hasAxis(axisType, isPrimary)**](https://reference.aspose.com/cells/nodejs-cpp/chart/#hasAxis-AxisType-boolean-) método para determinar si el gráfico tiene un eje específico o no.  
{{% /alert %}}  

El siguiente código de ejemplo demuestra el uso de [**Chart.hasAxis(axisType, isPrimary)**](https://reference.aspose.com/cells/nodejs-cpp/chart/#hasAxis-AxisType-boolean-) para determinar si el gráfico de muestra tiene Ejes de Categoría y Valor Principales y Secundarios.  

## Código de Node.js para determinar qué eje existe en el gráfico  

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

## Salida de consola generada por el código de ejemplo  

La salida de la consola del código se muestra a continuación, que muestra verdadero para el Eje de Categoría y Valor Principal y falso para el Eje de Categoría y Valor Secundario.  

{{< highlight java >}}  
Has Primary Category Axis: True  
Has Secondary Category Axis: False  
Has Primary Value Axis: True  
Has Secondary Value Axis: False  
{{< /highlight >}}  
{{< app/cells/assistant language="nodejs-cpp" >}}
