---
title: الحصول على ورقة العمل الخاصة بالمخطط باستخدام Node.js عبر C++
linktitle: الحصول على ورقة البيانات للشارت
description: تعلم كيفية استرجاع ورقة العمل المرتبطة بمخطط Excel باستخدام Aspose.Cells for Node.js via C++. الوصول إلى البيانات الأساسية للمخطط ومعالجتها بكفاءة.
keywords: Aspose.Cells لـ Node.js، مخططات Excel، أوراق العمل، معالجة البيانات، البيانات الأساسية، العمليات، Node.js عبر C++
type: docs
weight: 1000
url: /ar/nodejs-cpp/get-worksheet-of-the-chart/
---

{{% alert color="primary" %}}

في بعض الأحيان، قد ترغب في الوصول إلى ورقة عمل من مرجع شارت. توفر Aspose.Cells ال [**Chart.getWorksheet()**](https://reference.aspose.com/cells/nodejs-cpp/chart/#getWorksheet--) المعني الذي يعيد مرجع الورقة التي تحتوي على الشارت.

{{% /alert %}}

يعرض المثال التالي كيفية استخدام الخاصية [**Chart.getWorksheet()**](https://reference.aspose.com/cells/nodejs-cpp/chart/#getWorksheet--). يُطبع اسم ورقة العمل أولاً، ثم يتم الوصول إلى أول مخطط على الورقة. ثم يُطبع اسم ورقة العمل مرة أخرى، باستخدام الخاصية [**Chart.getWorksheet()**](https://reference.aspose.com/cells/nodejs-cpp/chart/#getWorksheet--).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sample.xlsx"));

// Access first worksheet of the workbook
const worksheet = workbook.getWorksheets().get(0);

// Print worksheet name
console.log("Sheet Name: " + worksheet.getName());

// Access the first chart inside this worksheet
const charts = worksheet.getCharts();
if (charts.getCount() > 0) {
const chart = charts.get(0);

// Access the chart's sheet and display its name again
console.log("Chart's Sheet Name: " + chart.getWorksheet().getName());
} else {
console.log("No charts available in the worksheet.");
}
```

أدناه نتيجة الإخراج على الشاشة التي يؤدي إليها الكود المثالي. كما يمكنك رؤية، فإنه يطبع اسم الورقة نفسه بكلتا المرتين.

{{< highlight javascript >}}

Sheet Name: Portfolio

Chart's Sheet Name: Portfolio

{{< /highlight >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
