---  
title: إضافة تسميات مخصصة لنقاط البيانات في سلسلة المخطط باستخدام Node.js عبر C++  
linktitle: إضافة تسميات مخصصة إلى نقاط البيانات في سلسلة الرسم البياني  
description: تعلم كيفية إضافة تسميات مخصصة لنقاط البيانات في سلسلة مخطط باستخدام Aspose.Cells for Node.js via C++. سيُظهر دليلنا كيفية تعديل مظهر التسميات، والموقع، والتنسيق، مع ربطها بمصدر البيانات الخاص بك لتمثيل دقيق.  
keywords: Aspose.Cells لـ Node.js، رسم بياني، تسميات مخصصة، نقاط البيانات، سلسلة، المظهر، الموقع، التنسيق، مصدر البيانات، التمثيل.  
type: docs  
weight: 100  
url: /ar/nodejs-cpp/adding-custom-labels-to-data-points-in-the-series-of-the-chart/  
---  

{{% alert color="primary" %}}  

يمكنك إضافة تسميات مخصصة لنقاط البيانات في سلسلة الرسم البياني. يوفر Aspose.Cells [**DataLabels.getText()**](https://reference.aspose.com/cells/nodejs-cpp/datalabels/#getText--) خاصية لإضافة هذه التسميات المخصصة. سيشرح هذا المقال كيفية استخدام هذه الخاصية لإضافة تسميات مخصصة لنقاط البيانات في سلسلة الرسم البياني.

{{% /alert %}}  

يستعرض الكود التالي إنشاء **مخطط نقطي متصل بواسطة خطوط مع علامات البيانات** ثم يضيف **تسميات مخصصة** إلى **نقاط البيانات** في **السلسلة** من **المخطط**. يعرض كل تسمية مخصصة **اسم السلسلة** و **اسم النقطة**. يمكنك استخدام أي نص آخر بدلاً من ذلك.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);
const sheet = workbook.getWorksheets().get(0);

// Put data
sheet.getCells().get(0, 0).putValue(1);
sheet.getCells().get(0, 1).putValue(2);
sheet.getCells().get(0, 2).putValue(3);

sheet.getCells().get(1, 0).putValue(4);
sheet.getCells().get(1, 1).putValue(5);
sheet.getCells().get(1, 2).putValue(6);

sheet.getCells().get(2, 0).putValue(7);
sheet.getCells().get(2, 1).putValue(8);
sheet.getCells().get(2, 2).putValue(9);

// Generate the chart
const chartIndex = sheet.getCharts().add(AsposeCells.ChartType.ScatterConnectedByLinesWithDataMarker, 5, 1, 24, 10);
const chart = sheet.getCharts().get(chartIndex);

chart.getTitle().setText("Test");
chart.getCategoryAxis().getTitle().setText("X-Axis");
chart.getValueAxis().getTitle().setText("Y-Axis");

chart.getNSeries().setCategoryData("A1:C1");

// Insert series
chart.getNSeries().add("A2:C2", false);

let series = chart.getNSeries().get(0);

let pointCount = series.getPoints().getCount();
for (let i = 0; i < pointCount; i++) {
const pointIndex = series.getPoints().get(i);
pointIndex.getDataLabels().setText("Series 1" + "\n" + "Point " + i);
}

// Insert series
chart.getNSeries().add("A3:C3", false);

series = chart.getNSeries().get(1);

pointCount = series.getPoints().getCount();
for (let i = 0; i < pointCount; i++) {
const pointIndex = series.getPoints().get(i);
pointIndex.getDataLabels().setText("Series 2" + "\n" + "Point " + i);
}

workbook.save(path.join(dataDir, "output_out.xlsx"), AsposeCells.SaveFormat.Xlsx);
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
