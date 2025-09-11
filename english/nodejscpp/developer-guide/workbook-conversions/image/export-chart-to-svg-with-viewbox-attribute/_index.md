---
title: Export Chart to SVG with viewBox attribute using Node.js via C++
linktitle: Export Chart to SVG with viewBox attribute
type: docs
weight: 280
url: /nodejs-cpp/export-chart-to-svg-with-viewbox-attribute/
description: Learn how to export a chart to SVG format with the viewBox attribute using Aspose.Cells for Node.js via C++.
---

{{% alert color="primary" %}}

By default, when the chart is exported to SVG format, the **viewBox** attribute is not included in its XML. However, Aspose.Cells provides [**ImageOrPrintOptions.getSVGFitToViewPort()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getSVGFitToViewPort--) property which when set to **true** exports the chart to SVG with viewBox attribute.

{{% /alert %}}

## Export Chart to SVG with viewBox attribute

The following sample code exports the chart to SVG format with the viewBox attribute.

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

If you open the chart's SVG in notepad, you will find the **viewBox** attribute similar to this.

{{< highlight java >}}

 <svg xmlns="http://www.w3.org/2000/svg"

     xmlns:xlink="http://www.w3.org/1999/xlink"

     width="100%" height="100%"

     viewBox="0 0 480 288">

{{< /highlight >}}

{{% /alert %}}
{{< app/cells/assistant language="nodejs-cpp" >}}