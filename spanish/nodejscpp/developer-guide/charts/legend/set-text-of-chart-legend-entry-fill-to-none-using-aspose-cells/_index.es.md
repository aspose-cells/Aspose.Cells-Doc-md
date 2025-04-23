---
title: Configura el texto de la entrada de la leyenda del gráfico para que no tenga relleno usando Aspose.Cells for Node.js via C++
linktitle: Establecer el texto de relleno de entrada de leyenda del gráfico a ninguno usando Aspose.Cells
description: Aprende cómo usar Aspose.Cells for Node.js via C++ para configurar el texto de una entrada de la leyenda del gráfico a ningún relleno. Esta guía demostrará cómo modificar el color de relleno de las entradas de leyenda en gráficos de Microsoft Excel para mejor visualización y personalización.
keywords: Aspose.Cells for Node.js via C++, Relleno de entrada de leyenda del gráfico, Microsoft Excel, Visualización, Personalización.
type: docs
weight: 320
url: /es/nodejs-cpp/set-text-of-chart-legend-entry-fill-to-none-using-aspose-cells/
---

{{% alert color="primary" %}}

Si deseas configurar el texto del relleno de la entrada de la leyenda del gráfico a ninguno para que no se muestre dentro de la leyenda del gráfico, establece [**LegendEntry.isTextNoFill()**](https://reference.aspose.com/cells/nodejs-cpp/legendentry/#isTextNoFill--) en **true**.

{{% /alert %}}

El siguiente código de muestra establece el texto del relleno de la segunda entrada de leyenda del gráfico en ninguno. Descargue el [archivo de Excel de muestra](5115219.xlsx) utilizado en este código y el [archivo de Excel de salida](5115217.xlsx) generado por él para su referencia.

La siguiente captura de pantalla resalta el efecto de este código en el archivo de Excel de muestra (5115219.xlsx).

![todo:image_alt_text](set-text-of-chart-legend-entry-fill-to-none-using-aspose-cells_1.png)

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Open the template file.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "Sample.xlsx"));

// Access the first worksheet
const sheet = workbook.getWorksheets().get(0);

// Access the first chart inside the sheet
const chart = sheet.getCharts().get(0);

// Set text of second legend entry fill to none
chart.getLegend().getLegendEntries().get(1).setIsTextNoFill(true);

// Save the workbook in xlsx format
workbook.save(path.join(dataDir, "ChartLegendEntry_out.xlsx"), AsposeCells.SaveFormat.Xlsx);
```
