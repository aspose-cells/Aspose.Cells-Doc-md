---
title: Exportar Gráfico a SVG con atributo viewBox usando Node.js a través de C++
linktitle: Exportar gráfico a SVG con el atributo viewBox
type: docs
weight: 280
url: /es/nodejs-cpp/export-chart-to-svg-with-viewbox-attribute/
description: Aprende cómo exportar un gráfico a formato SVG con el atributo viewBox usando Aspose.Cells for Node.js via C++.
---

{{% alert color="primary" %}}

De forma predeterminada, cuando el gráfico se exporta al formato SVG, el atributo **viewBox** no se incluye en su XML. Sin embargo, Aspose.Cells proporciona la propiedad [**ImageOrPrintOptions.getSVGFitToViewPort()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getSVGFitToViewPort--) que, cuando se establece en **true**, exporta el gráfico a SVG con el atributo viewBox.

{{% /alert %}}

## Exportar gráfico a SVG con el atributo viewBox

El siguiente código de ejemplo exporta el gráfico al formato SVG con el atributo viewBox.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create workbook object from source file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "SampleChartBook.xlsx"));

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access first chart inside the worksheet
const chart = worksheet.getCharts().get(0);

// Set image or print options with SVGFitToViewPort true
const opts = new AsposeCells.ImageOrPrintOptions();
opts.setImageType(AsposeCells.ImageType.Svg);
opts.setSVGFitToViewPort(true);

// Save the chart to svg format
chart.toImage(path.join(dataDir, "Image_out.svg"), opts);
```

{{% alert color="primary" %}}

Si abres el SVG del gráfico en el bloc de notas, encontrarás el atributo **viewBox** similar a este:

{{< highlight java >}}

 <svg xmlns="http://www.w3.org/2000/svg"

     xmlns:xlink="http://www.w3.org/1999/xlink"

     width="100%" height="100%"

     viewBox="0 0 480 288">

{{< /highlight >}}

{{% /alert %}}
