---
title: Exportdiagram till SVG med viewBox attribuet med Node.js via C++
linktitle: Exportera diagram till SVG med viewBox attribut
type: docs
weight: 280
url: /sv/nodejs-cpp/export-chart-to-svg-with-viewbox-attribute/
description: Lär dig hur du exporterar ett diagram till SVG format med viewBox attributet med Aspose.Cells for Node.js via C++.
---

{{% alert color="primary" %}}

Som standard, när diagrammet exporteras till SVG-format, ingår inte attributet **viewBox** i dess XML. Men Aspose.Cells tillhandahåller [**ImageOrPrintOptions.getSVGFitToViewPort()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getSVGFitToViewPort--)-egenskapen som när den är inställd på **true** exporterar diagrammet till SVG med viewBox-attributen.

{{% /alert %}}

## Exportera diagram till SVG med viewBox-attribut

Följande kodexempel exporterar diagrammet till SVG-format med viewBox-attributet.

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

Om du öppnar diagrammets SVG i anteckningar kommer du att hitta **viewBox** -attributet som liknar detta.

{{< highlight java >}}

 <svg xmlns="http://www.w3.org/2000/svg"

     xmlns:xlink="http://www.w3.org/1999/xlink"

     width="100%" height="100%"

     viewBox="0 0 480 288">

{{< /highlight >}}

{{% /alert %}}
