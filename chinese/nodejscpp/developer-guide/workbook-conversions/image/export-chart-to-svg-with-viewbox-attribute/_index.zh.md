---
title: 使用 C++ 通过 Node.js 导出带有 viewBox 属性的 SVG 图表
linktitle: 导出带有viewBox属性的SVG图表
type: docs
weight: 280
url: /zh/nodejs-cpp/export-chart-to-svg-with-viewbox-attribute/
description: 学习如何使用 Aspose.Cells for Node.js via C++ 导出带有 viewBox 属性的 SVG 格式图表。
---

{{% alert color="primary" %}}

默认情况下，将图表导出为SVG格式时，其XML中不包括**viewBox**属性。但是，Aspose.Cells提供了[**ImageOrPrintOptions.getSVGFitToViewPort()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getSVGFitToViewPort--)属性，将其设置为**true**时会导出具有viewBox属性的SVG图表。

{{% /alert %}}

## 导出带有viewBox属性的SVG图表

以下示例代码将图表导出为带有viewBox属性的SVG格式。

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

如果在记事本中打开图表的SVG文件，将会找到类似于这样的**viewBox**属性。

{{< highlight java >}}

 <svg xmlns="http://www.w3.org/2000/svg"

     xmlns:xlink="http://www.w3.org/1999/xlink"

     width="100%" height="100%"

     viewBox="0 0 480 288">

{{< /highlight >}}

{{% /alert %}}
{{< app/cells/assistant language="nodejs-cpp" >}}
