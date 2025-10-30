---  
title: Leer etiquetas del eje después de calcular el gráfico con Node.js a través de C++  
linktitle: Leer etiquetas del eje después de calcular el gráfico  
description: Aprende cómo leer las etiquetas del eje en Aspose.Cells for Node.js via C++ después de calcular el gráfico. Nuestra guía te mostrará cómo acceder y recuperar las etiquetas del eje, incluido su formato y posición.  
keywords: Aspose.Cells para Node.js, gráficos, etiquetas del eje, cálculo, lectura, acceso, recuperación, formato, posición, Node.js a través de C++  
type: docs  
weight: 90  
url: /es/nodejs-cpp/read-axis-labels-after-calculating-the-chart/  
---  

## **Escenarios de uso posibles**

Puedes leer las etiquetas del eje de tu gráfico después de calcular sus valores usando el método [**Chart.calculate()**](https://reference.aspose.com/cells/nodejs-cpp/chart/#calculate--). Por favor, usa el método [**Axis.getAxisTexts()**](https://reference.aspose.com/cells/nodejs-cpp/axis/#getAxisTexts--) para este propósito que devolverá la lista de etiquetas del eje.

## **Leer etiquetas del eje después de calcular el gráfico**

Consulte el siguiente código de ejemplo que carga el [archivo de Excel de muestra](ReadAxisLabels.xlsx) y lee las etiquetas del eje de categoría del gráfico en la primera hoja de cálculo. Luego imprime los valores de las etiquetas del eje en la consola. Consulte la salida de la consola del código de ejemplo a continuación como referencia.

## **Código de muestra**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "ReadAxisLabels_new.xlsx");

// Load the Excel file containing chart
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access the chart
const chart = worksheet.getCharts().get(0);

// Calculate the chart
chart.calculate();

// Read axis labels of category axis
const lstLabels = chart.getCategoryAxis().getAxisTexts();

// Print axis labels on console
console.log("Category Axis Labels: ");
console.log("---------------------");

// Iterate axis labels and print them one by one
for (let i = 0; i < lstLabels.length; i++) {
console.log(lstLabels[i]);
}
```

## **Salida de la consola**

{{< highlight javascript >}}  
 Category Axis Labels:  

\---------------------  

Iran  

China  

USA  

Brazil  

England  
{{< /highlight >}}  

{{< app/cells/assistant language="nodejs-cpp" >}}
