---
title: Exporter un graphique en SVG avec attribut viewBox en utilisant Node.js via C++
linktitle: Exporter le graphique en SVG avec l attribut viewBox
type: docs
weight: 280
url: /fr/nodejs-cpp/export-chart-to-svg-with-viewbox-attribute/
description: Apprenez comment exporter un graphique au format SVG avec l attribut viewBox en utilisant Aspose.Cells for Node.js via C++.
---

{{% alert color="primary" %}}

Par défaut, lorsque le graphique est exporté au format SVG, l'attribut **viewBox** n'est pas inclus dans son XML. Cependant, Aspose.Cells fournit la propriété [**ImageOrPrintOptions.getSVGFitToViewPort()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getSVGFitToViewPort--) qui, lorsqu'elle est définie sur **true**, exporte le graphique en SVG avec l'attribut viewBox.

{{% /alert %}}

## Exporter le graphique en SVG avec l'attribut viewBox

Le code d'exemple suivant exporte le graphique au format SVG avec l'attribut viewBox.

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

Si vous ouvrez le SVG du graphique dans le bloc-notes, vous trouverez l'attribut **viewBox** similaire à ceci.

{{< highlight java >}}

 <svg xmlns="http://www.w3.org/2000/svg"

     xmlns:xlink="http://www.w3.org/1999/xlink"

     width="100%" height="100%"

     viewBox="0 0 480 288">

{{< /highlight >}}

{{% /alert %}}
{{< app/cells/assistant language="nodejs-cpp" >}}
