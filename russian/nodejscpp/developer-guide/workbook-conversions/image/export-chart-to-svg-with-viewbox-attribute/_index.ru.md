---
title: Экспортировать график в SVG с атрибутом viewBox с помощью Node.js через C++
linktitle: Экспорт диаграммы в SVG с атрибутом viewBox
type: docs
weight: 280
url: /ru/nodejs-cpp/export-chart-to-svg-with-viewbox-attribute/
description: Узнайте, как экспортировать график в формат SVG с атрибутом viewBox с помощью Aspose.Cells for Node.js via C++.
---

{{% alert color="primary" %}}

По умолчанию, когда диаграмма экспортируется в формат SVG, атрибут **viewBox** не включается в его XML. Однако Aspose.Cells предоставляет свойство [**ImageOrPrintOptions.getSVGFitToViewPort()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getSVGFitToViewPort--), которое, когда установлено в **истину**, экспортирует диаграмму в SVG с атрибутом viewBox.

{{% /alert %}}

## Экспорт диаграммы в SVG с атрибутом viewBox

В следующем образце кода диаграмма экспортируется в формат SVG с атрибутом viewBox.

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

Если вы откроете файл SVG диаграммы в блокноте, вы обнаружите атрибут **viewBox** аналогичный этому.

{{< highlight java >}}

 <svg xmlns="http://www.w3.org/2000/svg"

     xmlns:xlink="http://www.w3.org/1999/xlink"

     width="100%" height="100%"

     viewBox="0 0 480 288">

{{< /highlight >}}

{{% /alert %}}
