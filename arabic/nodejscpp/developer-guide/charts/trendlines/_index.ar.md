---
title: الحصول على نص معادلة خط الاتجاه في المخطط باستخدام Node.js عبر C++
description: تعلم كيفية استخدام Aspose.Cells for Node.js via C++ لاسترجاع نص المعادلة لخط الاتجاه في مخطط منشأ في Microsoft Excel. سيُظهر دليلنا كيف تصل وتستخلص معادلة خط الاتجاه لمزيد من التحليل أو العرض.
keywords: Aspose.Cells for Node.js via C++، خط الاتجاه في المخطط، نص المعادلة، Microsoft Excel، تحليل البيانات، العرض.
linktitle: خطوط الاتجاه
type: docs
weight: 110
url: /ar/nodejs-cpp/get-equation-text-of-chart-trendline/
---

{{% alert color="primary" %}}

يمكنك استرجاع نص المعادلة لخط الاتجاه في المخطط باستخدام Aspose.Cells for Node.js via C++. توفر Aspose.Cells الخاصية [**DataLabels.getText()**](https://reference.aspose.com/cells/nodejs-cpp/datalabels/#getText--) التي تعود بنص المعادلة لخط الاتجاه في المخطط. لاستخدام هذه الخاصية، يجب عليك أولاً استدعاء طريقة [**Chart.calculate()**](https://reference.aspose.com/cells/nodejs-cpp/chart/#calculate--).

{{% /alert %}}

يعرض لقطة الشاشة التالية المخطط مع خط اتجاه والنص المعادلة الخاص به مرئي باللون الأحمر. سنسترجع هذا النص باستخدام الخاصية [**DataLabels.getText()**](https://reference.aspose.com/cells/nodejs-cpp/datalabels/#getText--) في الكود التالي.

![todo:image_alt_text](get-equation-text-of-chart-trendline_1.png)

## كود Node.js للحصول على نص معادلة خط الاتجاه في المخطط

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Create workbook object from source Excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "source.xlsx"));

// Access the first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access the first chart inside the worksheet
const chart = worksheet.getCharts().get(0);

// Calculate the Chart first to get the Equation Text of Trendline
chart.calculate();

// Access the Trendline
const trendLine = chart.getNSeries().get(0).getTrendLines().get(0);

// Read the Equation Text of Trendline
console.log("Equation Text: " + trendLine.getDataLabels().getText());
```

## الإخراج الذي تم توليده بواسطة رمز العينة

هذا هو إنتاج الكونسول للكود العيني أعلاه.

{{< highlight javascript >}}

Equation Text: y = 8.1333x + 5

{{< /highlight >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
