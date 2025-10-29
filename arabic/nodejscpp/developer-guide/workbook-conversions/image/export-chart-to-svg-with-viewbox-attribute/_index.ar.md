---
title: تصدير مخطط إلى SVG مع سمة viewBox باستخدام Node.js عبر C++
linktitle: تصدير الرسم البياني إلى SVG مع خاصية viewBox
type: docs
weight: 280
url: /ar/nodejs-cpp/export-chart-to-svg-with-viewbox-attribute/
description: تعلم كيفية تصدير مخطط إلى صيغة SVG مع سمة viewBox باستخدام Aspose.Cells for Node.js via C++.
---

{{% alert color="primary" %}}

بشكل افتراضي، عند تصدير الرسم البياني إلى تنسيق SVG، لا يتم تضمين سمة **viewBox** في XML الخاص به. ومع ذلك، يوفر Aspose.Cells خاصية [**ImageOrPrintOptions.getSVGFitToViewPort()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getSVGFitToViewPort--) التي عند تعيينها على **true** يقوم بتصدير الرسم البياني إلى SVG مع سمة viewBox.

{{% /alert %}}

## تصدير الرسم البياني إلى SVG بسمة viewBox

الرمز العينة التالي يقوم بتصدير الرسم البياني إلى تنسيق SVG مع سمة viewBox.

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

إذا فتحت ملف SVG الخاص بالرسم البياني في المفكرة، فستجد سمة viewBox مماثلة لهذه.

{{< highlight java >}}

 <svg xmlns="http://www.w3.org/2000/svg"

     xmlns:xlink="http://www.w3.org/1999/xlink"

     width="100%" height="100%"

     viewBox="0 0 480 288">

{{< /highlight >}}

{{% /alert %}}
{{< app/cells/assistant language="nodejs-cpp" >}}
