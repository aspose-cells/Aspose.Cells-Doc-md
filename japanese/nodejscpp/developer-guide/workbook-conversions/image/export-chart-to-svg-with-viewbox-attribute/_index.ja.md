---
title: Node.jsとC++を使用してviewBox属性付きのSVGへチャートをエクスポート
linktitle: viewBox属性を使用してチャートをSVG形式にエクスポート
type: docs
weight: 280
url: /ja/nodejs-cpp/export-chart-to-svg-with-viewbox-attribute/
description: Aspose.Cells for Node.js via C++を使用してviewBox属性付きのSVG形式にチャートをエクスポートする方法を学びます。
---

{{% alert color="primary" %}}

デフォルトでは、チャートをSVG形式にエクスポートするとき、そのXMLには**viewBox**属性が含まれません。しかし、Aspose.Cellsは、**true**に設定された場合に**viewBox**属性でチャートをSVG形式でエクスポートする[**ImageOrPrintOptions.getSVGFitToViewPort()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getSVGFitToViewPort--)プロパティを提供します。

{{% /alert %}}

## viewBox属性を含むSVG形式でチャートをエクスポート

次のコードサンプルは、viewBox属性を含むSVG形式でチャートをエクスポートします。

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

チャートのSVGをNotepadで開くと、次のような**viewBox**属性が見つかります。

{{< highlight java >}}

 <svg xmlns="http://www.w3.org/2000/svg"

     xmlns:xlink="http://www.w3.org/1999/xlink"

     width="100%" height="100%"

     viewBox="0 0 480 288">

{{< /highlight >}}

{{% /alert %}}
