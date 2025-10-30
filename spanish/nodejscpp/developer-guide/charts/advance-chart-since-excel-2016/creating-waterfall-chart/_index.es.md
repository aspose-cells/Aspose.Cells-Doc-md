---
title: Cómo crear un gráfico de cascada con Node.js vía C++
linktitle: Cómo crear un gráfico de cascada
type: docs
weight: 160
url: /es/nodejs-cpp/creating-waterfall-chart/
description: Crear gráficos de cascada en Excel con Node.js y Aspose.Cells for Node.js via C++.
keywords: crear gráfico de cascada en Excel Node.js vía C++, creando gráfico de cascada en Excel Node.js vía C++, cómo crear gráfico de cascada en Excel Node.js vía C++
---

{{% alert color="primary" %}}

Un gráfico de cascada es un tipo especial de gráfico que normalmente se utiliza para demostrar cómo la posición inicial aumenta o disminuye. Microsoft Excel tiene muchos tipos de gráficos predefinidos, incluyendo columna, línea, pastel, barra, radar, etc., pero el gráfico de cascada va más allá de los gráficos básicos y puede crearse usando los tipos de gráficos existentes con poca o mucha personalización.

{{% /alert %}} 

Las API de Aspose.Cells permiten crear un gráfico de cascada con la ayuda del gráfico de líneas. La API también permite personalizar la apariencia del gráfico para darle forma de cascada configurando las propiedades [**Series.getUpBars()**](https://reference.aspose.com/cells/nodejs-cpp/series/#getUpBars--) y [**Series.getDownBars()**](https://reference.aspose.com/cells/nodejs-cpp/series/#getDownBars--).

El fragmento de código proporcionado a continuación demuestra el uso de Aspose.Cells for Node.js via C++ para crear un gráfico de cascada desde cero.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Create an instance of Workbook
const workbook = new AsposeCells.Workbook();

// Retrieve the first Worksheet in Workbook
const worksheet = workbook.getWorksheets().get(0);

// Retrieve the Cells of the first Worksheet
const cells = worksheet.getCells();

// Input some data which chart will use as source
cells.get("A1").putValue("Previous Year");
cells.get("A2").putValue("January");
cells.get("A3").putValue("March");
cells.get("A4").putValue("August");
cells.get("A5").putValue("October");
cells.get("A6").putValue("Current Year");

cells.get("B1").putValue(8.5);
cells.get("B2").putValue(1.5);
cells.get("B3").putValue(7.5);
cells.get("B4").putValue(7.5);
cells.get("B5").putValue(8.5);
cells.get("B6").putValue(3.5);

cells.get("C1").putValue(1.5);
cells.get("C2").putValue(4.5);
cells.get("C3").putValue(3.5);
cells.get("C4").putValue(9.5);
cells.get("C5").putValue(7.5);
cells.get("C6").putValue(9.5);

// Add a Chart of type Waterfall in same worksheet as of data
const idx = worksheet.getCharts().add(AsposeCells.ChartType.Waterfall, 4, 4, 25, 13);

// Retrieve the Chart object
const chart = worksheet.getCharts().get(idx);

// Add Series
chart.getNSeries().add("$B$1:$C$6", true);

// Add Category Data
chart.getNSeries().setCategoryData("$A$1:$A$6");

// Series has Up Down Bars
chart.getNSeries().get(0).setHasUpDownBars(true);

// Set the colors of Up and Down Bars
chart.getNSeries().get(0).getUpBars().getArea().setForegroundColor(AsposeCells.Color.Green);
chart.getNSeries().get(0).getDownBars().getArea().setForegroundColor(AsposeCells.Color.Red);

// Make both Series Lines invisible
chart.getNSeries().get(0).getBorder().setIsVisible(false);
chart.getNSeries().get(1).getBorder().setIsVisible(false);

// Set the Plot Area Formatting Automatic
chart.getPlotArea().getArea().setFormatting(AsposeCells.FormattingType.Automatic);

// Delete the Legend
chart.getLegend().getLegendEntries().get(0).setIsDeleted(true);
chart.getLegend().getLegendEntries().get(1).setIsDeleted(true);

// Save the workbook
workbook.save(path.join(dataDir, "output_out.xlsx"));
```

## Artículos relacionados

- [Creando gráficos](/cells/es/nodejs-cpp/creating-charts/)
- [Personalizar gráficos](/cells/es/nodejs-cpp/customizing-charts/)
{{< app/cells/assistant language="nodejs-cpp" >}}
