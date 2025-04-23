---
title: Deshabilitar ajuste de texto para las etiquetas de datos del gráfico con Node.js a través de C++
description: Aprende a desactivar el ajuste de texto para las etiquetas de datos en gráficos usando Aspose.Cells for Node.js via C++. Nuestra guía te mostrará cómo evitar que las etiquetas largas se superpongan y ofrecerás visualizaciones de gráficos más legibles y claras.
keywords: Aspose.Cells for Node.js via C++, creación de gráficos, etiquetas de datos, ajuste de texto, superposición, legibilidad, visualizaciones.
type: docs
weight: 70
url: /es/nodejs-cpp/disable-text-wrapping-for-data-labels-of-the-chart/
---

{{% alert color="primary" %}}

Microsoft Excel 2013 permite a los usuarios ajustar o desajustar el texto dentro de las etiquetas de datos del gráfico. De forma predeterminada, el texto dentro de las etiquetas de datos del gráfico está en estado desajustado.

Aspose.Cells proporciona una propiedad [**DataLabels.isTextWrapped()**](https://reference.aspose.com/cells/nodejs-cpp/datalabels/#isTextWrapped--) que puedes establecer en true o false para habilitar o deshabilitar el ajuste de texto de las etiquetas de datos respectivamente.

{{% /alert %}}

El siguiente ejemplo de código muestra cómo deshabilitar el ajuste de texto para las etiquetas de datos del gráfico.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample_wrap_label.xlsx");
// Load the sample Excel file inside the workbook object
const workbook = new AsposeCells.Workbook(filePath);

// Access the first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access the first chart inside the worksheet
const chart = worksheet.getCharts().get(0);

// Disable the Text Wrapping of Data Labels in all Series
chart.getNSeries().get(0).getDataLabels().setIsTextWrapped(false);
chart.getNSeries().get(1).getDataLabels().setIsTextWrapped(false);
chart.getNSeries().get(2).getDataLabels().setIsTextWrapped(false);

// Save the workbook
workbook.save(path.join(dataDir, "Output_out.xlsx"));
```
