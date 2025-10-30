---
title: Etiqueta de datos personalizada con texto enriquecido en el gráfico con Node.js a través de C++
description: Aprende a agregar etiquetas de datos personalizadas con texto enriquecido a los puntos del gráfico en Aspose.Cells for Node.js via C++. Nuestra guía mostrará cómo formatear las etiquetas con diferentes fuentes, colores y opciones de alineación para mejorar la apariencia y legibilidad de tus gráficos.
keywords: Aspose.Cells for Node.js via C++, creación de gráficos, texto enriquecido, etiquetas de datos personalizadas, fuentes, colores, alineación, apariencia, legibilidad.
type: docs
weight: 10
url: /es/nodejs-cpp/rich-text-custom-data-label-of-chart-point/
---

{{% alert color="primary" %}}

Puedes usar Aspose.Cells para crear etiquetas de datos personalizadas con texto enriquecido para puntos del gráfico. Aspose.Cells proporciona el método [**ChartTextFrame.characters(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/charttextframe/#characters-number-number-) para devolver el objeto [**FontSetting**](https://reference.aspose.com/cells/nodejs-cpp/fontsetting) que puede usarse para establecer las propiedades de fuente del texto, como el color, negrita, etc.

{{% /alert %}}

## Etiqueta de Datos Personalizada con Texto Enriquecido del Punto del Gráfico

El siguiente código accede al primer punto de la primera serie, establece su texto y luego configura la fuente de los primeros 10 caracteres estableciendo su color a rojo y su negrita en **true**.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Create a workbook from source Excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sample_custom_datalabel.xlsx"));

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access the first chart inside the sheet
const chart = worksheet.getCharts().get(0);

// Access the data label of first series first point
const dlbls = chart.getNSeries().get(0).getPoints().get(0).getDataLabels();

// Set data label text
dlbls.setText("Rich Text Label");

// Set the font setting of the first 10 characters
const fntSetting = dlbls.characters(0, 10);
fntSetting.getFont().setColor(AsposeCells.Color.Red);
fntSetting.getFont().setIsBold(true);

// Save the workbook
workbook.save(path.join(dataDir, "output_out.xlsx"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
