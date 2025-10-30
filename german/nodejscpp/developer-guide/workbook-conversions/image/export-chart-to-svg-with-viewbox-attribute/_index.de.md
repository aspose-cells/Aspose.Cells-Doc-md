---
title: Exportieren Sie Diagramm nach SVG mit viewBox Attribut unter Verwendung von Node.js via C++
linktitle: Diagramm als SVG mit viewBox Attribut exportieren
type: docs
weight: 280
url: /de/nodejs-cpp/export-chart-to-svg-with-viewbox-attribute/
description: Lernen Sie, wie Sie ein Diagramm mit dem viewBox Attribut im SVG Format mithilfe von Aspose.Cells for Node.js via C++ exportieren.
---

{{% alert color="primary" %}}

Standardmäßig ist das **viewBox**-Attribut beim Export des Diagramms ins SVG-Format nicht in seinem XML enthalten. Allerdings bietet Aspose.Cells [**ImageOrPrintOptions.getSVGFitToViewPort()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getSVGFitToViewPort--) Eigenschaft, die beim Einstellen auf **true** das Diagramm ins SVG mit viewBox-Attribut exportiert.

{{% /alert %}}

## Diagramm als SVG mit viewBox-Attribut Exportieren

Der folgende Beispielcode exportiert das Diagramm im SVG-Format mit dem viewBox-Attribut.

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

Wenn Sie das SVG des Diagramms in Notepad öffnen, finden Sie das **viewBox**-Attribut ähnlich wie dieses.

{{< highlight java >}}

 <svg xmlns="http://www.w3.org/2000/svg"

     xmlns:xlink="http://www.w3.org/1999/xlink"

     width="100%" height="100%"

     viewBox="0 0 480 288">

{{< /highlight >}}

{{% /alert %}}
{{< app/cells/assistant language="nodejs-cpp" >}}
