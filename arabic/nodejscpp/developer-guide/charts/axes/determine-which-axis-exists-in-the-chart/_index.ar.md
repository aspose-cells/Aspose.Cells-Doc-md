---  
title: تحديد أي محور موجود في المخطط باستخدام Node.js عبر C++  
linktitle: تحديد المحور الموجود في الرسم البياني  
description: تعلم كيفية تحديد أي المحاور موجود في مخطط أنشئ باستخدام Aspose.Cells for Node.js via C++. سيرشدك دليلنا إلى التعرف على المحاور المختلفة في مخطط، بما في ذلك المحاور الفئة، والقيمة، والثانوية.  
keywords: Aspose.Cells لـ Node.js، مخطط، محور، وجود، فئة، قيمة، ثانوي.  
type: docs  
weight: 140  
url: /ar/nodejs-cpp/determine-which-axis-exists-in-the-chart/  
---  

{{% alert color="primary" %}}  
أحيانًا، يحتاج المستخدم إلى معرفة ما إذا كان محور معين موجود في المخطط. على سبيل المثال، يريد أن يعرف ما إذا كان يوجد محور قيمة ثانوي داخل المخطط أم لا. بعض المخططات مثل الفطيرة، الفطيرة المنفجرة، فطيرة عادية، فطيرة شريط، فطيرة ثلاثية الأبعاد، فطيرة ثلاثية الأبعاد منفجرة، دائرة مملوءة، مملوءة منفوخة، وغيرها لا تحتوي على محور.  

توفر Aspose.Cells [**Chart.hasAxis(axisType, isPrimary)**](https://reference.aspose.com/cells/nodejs-cpp/chart/#hasAxis-AxisType-boolean-) لتحديد ما إذا كان لدى المخطط محور معين أم لا.  
{{% /alert %}}  

 يوضح الكود التالي استخدام [**Chart.hasAxis(axisType, isPrimary)**](https://reference.aspose.com/cells/nodejs-cpp/chart/#hasAxis-AxisType-boolean-) لتحديد ما إذا كان الرسم البياني التجريبي يحتوي على محور فئة وقيمة أساسي وثانوي.  

## كود Node.js لتحديد أي محور موجود في المخطط  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "source.xlsx");
// Create workbook object
const workbook = new AsposeCells.Workbook(filePath);

// Access the first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Check if there are any charts before accessing
const charts = worksheet.getCharts();
if (charts.getCount() === 0) {
console.log("No charts found in the worksheet.");
return;
}

// Access the chart
const chart = charts.get(0);

// Determine which axis exists in chart
let ret = chart.hasAxis(AsposeCells.AxisType.Category, true);
console.log("Has Primary Category Axis: " + ret);

ret = chart.hasAxis(AsposeCells.AxisType.Category, false);
console.log("Has Secondary Category Axis: " + ret);

ret = chart.hasAxis(AsposeCells.AxisType.Value, true);
console.log("Has Primary Value Axis: " + ret);

ret = chart.hasAxis(AsposeCells.AxisType.Value, false);
console.log("Has Secondary Value Axis: " + ret);
```  

## الناتج على واجهة الأوامر الناتجة عن الكود المثال  

يظهر مخرجات وحدة التحكم للكود أدناه، والتي تعرض true للمحور الرئيسي للفئة والقيمة و false للمحور الثانوي للفئة والقيمة.  

{{< highlight java >}}  
Has Primary Category Axis: True  
Has Secondary Category Axis: False  
Has Primary Value Axis: True  
Has Secondary Value Axis: False  
{{< /highlight >}}  
{{< app/cells/assistant language="nodejs-cpp" >}}
