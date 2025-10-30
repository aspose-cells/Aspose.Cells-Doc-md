---
title: Node.js aracılığıyla C++ kullanarak viewBox özelliği ile SVG ye Grafik İhracı
linktitle: viewBox özniteliği ile SVG ye Grafik Dışa Aktarma
type: docs
weight: 280
url: /tr/nodejs-cpp/export-chart-to-svg-with-viewbox-attribute/
description: Aspose.Cells for Node.js via C++ kullanarak viewBox özelliği ile grafiği SVG formatına aktarımını öğrenin.
---

{{% alert color="primary" %}}

Varsayılan olarak, grafik SVG biçimine dışa aktarıldığında, **viewBox** özniteliği içinde yer almaz. Ancak, Aspose.Cells, **true** olarak ayarlandığında grafiği viewBox özniteliği ile SVG'ye dışa aktarır.

{{% /alert %}}

## viewBox Özniteliği ile SVG'ye Grafik Dışa Aktarma

Aşağıdaki örnek kod, grafiği viewBox özniteliği ile SVG biçiminde dışa aktarır.

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

Grafiğin SVG'sini not defterinde açarsanız, benzer bir **viewBox** özniteliği bulacaksınız.

{{< highlight java >}}

 <svg xmlns="http://www.w3.org/2000/svg"

     xmlns:xlink="http://www.w3.org/1999/xlink"

     width="100%" height="100%"

     viewBox="0 0 480 288">

{{< /highlight >}}

{{% /alert %}}
{{< app/cells/assistant language="nodejs-cpp" >}}
