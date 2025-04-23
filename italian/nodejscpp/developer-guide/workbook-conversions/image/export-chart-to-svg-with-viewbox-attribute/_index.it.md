---
title: Esporta grafico in SVG con attributo viewBox usando Node.js tramite C++
linktitle: Esporta il grafico in SVG con attributo viewBox
type: docs
weight: 280
url: /it/nodejs-cpp/export-chart-to-svg-with-viewbox-attribute/
description: Impara come esportare un grafico in formato SVG con attributo viewBox utilizzando Aspose.Cells for Node.js via C++.
---

{{% alert color="primary" %}}

Per impostazione predefinita, quando il grafico viene esportato nel formato SVG, l'attributo **viewBox** non è incluso nel suo XML. Tuttavia, Aspose.Cells fornisce [**ImageOrPrintOptions.getSVGFitToViewPort()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getSVGFitToViewPort--) proprietà che, quando impostata su **true**, esporta il grafico in SVG con l'attributo viewBox.

{{% /alert %}}

## Esportare il grafico in SVG con attributo viewBox

Il seguente codice di esempio esporta il grafico nel formato SVG con l'attributo viewBox.

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

Se apri l'SVG del grafico in notepad, troverai l'attributo **viewBox** simile a questo.

{{< highlight java >}}

 <svg xmlns="http://www.w3.org/2000/svg"

     xmlns:xlink="http://www.w3.org/1999/xlink"

     width="100%" height="100%"

     viewBox="0 0 480 288">

{{< /highlight >}}

{{% /alert %}}
