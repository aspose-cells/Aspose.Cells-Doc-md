---
title: Leer subtítulo del gráfico desde un archivo ODS usando Node.js a través de C++
linktitle: Leer subtítulo de gráfico de archivo ODS
description: Aprende cómo usar Aspose.Cells for Node.js via C++ para leer el subtítulo del gráfico desde un archivo de hoja de cálculo OpenDocument (ODS). Nuestra guía demostrará cómo extraer y acceder al subtítulo de un gráfico para análisis o visualización adicionales.
keywords: Aspose.Cells for Node.js via C++, leer subtítulo del gráfico, hoja de cálculo OpenDocument, archivo ODS, extracción de gráficos, análisis de datos.
type: docs
weight: 160
url: /es/nodejs-cpp/read-chart-subtitle-from-ods-file/
---

## **Leer subtítulo del gráfico desde un archivo ODS**

Aspose.Cells te permite leer subtítulos de gráficos en archivos ODS usando la propiedad [**Chart.getSubTitle()**](https://reference.aspose.com/cells/nodejs-cpp/chart/#getSubTitle--). El siguiente código de ejemplo carga el [archivo ODS de muestra](89620481.ods) y lee el subtítulo del gráfico usando la propiedad [**Chart.getSubTitle()**](https://reference.aspose.com/cells/nodejs-cpp/chart/#getSubTitle--) y lo imprime en la ventana de consola. Consulta la salida de la consola del código abajo para referencia.

## **Código de muestra**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");
// Load excel file containing charts
const filePath = path.join(sourceDir, "SampleChart.ods");
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access first chart inside the worksheet
const chart = worksheet.getCharts().get(0);

console.log("Chart Subtitle: " + chart.getSubTitle().getText());
```

## **Salida de la consola**

{{< highlight javascript >}}

Chart Subtitle: Sample Chart Subtitle

{{< /highlight >}}
