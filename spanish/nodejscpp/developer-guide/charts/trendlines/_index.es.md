---
title: Obtener el texto de la ecuación de la línea de tendencia del gráfico con Node.js a través de C++
description: Aprende cómo usar Aspose.Cells for Node.js via C++ para recuperar el texto de la ecuación de una línea de tendencia en un gráfico creado en Microsoft Excel. Nuestra guía demostrará cómo acceder y extraer la ecuación de una línea de tendencia para análisis o visualización adicional.
keywords: Aspose.Cells for Node.js via C++, Línea de tendencia del gráfico, Texto de la ecuación, Microsoft Excel, Análisis de datos, Visualización.
linktitle: Líneas de tendencia
type: docs
weight: 110
url: /es/nodejs-cpp/get-equation-text-of-chart-trendline/
---

{{% alert color="primary" %}}

Puedes recuperar el Texto de la ecuación de la línea de tendencia del gráfico usando Aspose.Cells for Node.js via C++. Aspose.Cells ofrece la propiedad [**DataLabels.getText()**](https://reference.aspose.com/cells/nodejs-cpp/datalabels/#getText--) que devuelve el Texto de la ecuación de la línea de tendencia del gráfico. Para usar esta propiedad, primero debes llamar al método [**Chart.calculate()**](https://reference.aspose.com/cells/nodejs-cpp/chart/#calculate--).

{{% /alert %}}

La siguiente captura muestra el gráfico con una línea de tendencia y su texto de ecuación en color rojo. Nosotros recuperaremos este texto usando la propiedad [**DataLabels.getText()**](https://reference.aspose.com/cells/nodejs-cpp/datalabels/#getText--) en el siguiente ejemplo de código.

![todo:image_alt_text](get-equation-text-of-chart-trendline_1.png)

## Código Node.js para obtener el texto de la ecuación de la línea de tendencia del gráfico

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Create workbook object from source Excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "source.xlsx"));

// Access the first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access the first chart inside the worksheet
const chart = worksheet.getCharts().get(0);

// Calculate the Chart first to get the Equation Text of Trendline
chart.calculate();

// Access the Trendline
const trendLine = chart.getNSeries().get(0).getTrendLines().get(0);

// Read the Equation Text of Trendline
console.log("Equation Text: " + trendLine.getDataLabels().getText());
```

Resultado generado por el código de ejemplo

Este es el resultado de consola del código de ejemplo anterior.

{{< highlight javascript >}}

Equation Text: y = 8.1333x + 5

{{< /highlight >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
