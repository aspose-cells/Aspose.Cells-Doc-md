---  
title: إيجاد نوع قيم X و Y للنقاط في سلسلة المخطط باستخدام Node.js عبر C++  
linktitle: البحث عن نوع قيم X وY لنقاط في سلسلة الرسم البياني  
description: تعلم كيفية تحديد نوع قيم X و Y في نقاط سلسلة المخطط باستخدام Aspose.Cells for Node.js via C++. يوضح دليلنا أنواع قيم البيانات وكيفية الوصول إليها والعمل بها في مخططاتك.  
keywords: Aspose.Cells لـ Node.js، رسم بياني، قيم X، قيم Y، أنواع البيانات، الوصول، العمل، سلسلة المخطط.  
type: docs  
weight: 150  
url: /ar/nodejs-cpp/find-type-of-x-and-y-values-of-points-in-chart-series/  
---  

## **سيناريوهات الاستخدام المحتملة**  
أحيانًا، تريد معرفة نوع قيم X و Y لنقاط المخطط في سلسلة. توفر Aspose.Cells for Node.js via C++ خاصيتي `ChartPoint.XValueType` و `ChartPoint.YValueType` للاستخدام لهذا الغرض. يرجى ملاحظة أنه يجب استدعاء طريقة `Chart.calculate()` قبل أن تتمكن من استخدام هذه الخصائص بفعالية.  

## **البحث عن نوع قيم X وY لنقاط في سلسلة الرسم البياني**  
الكود التجريبي التالي يحمل ملف Excel [العينة](64716905.xlsx) ويصل إلى المخطط الأول داخل الورقة الأولى. ثم يستدعي طريقة `Chart.calculate()` ويجد نوع قيم X و Y لنقطة المخطط الأولى ويطبعها في وحدة التحكم. يرجى مراجعة إخراج وحدة التحكم أدناه كمصدر مرجعي.  

## **الكود المثالي**  
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const sourceDir = path.join(__dirname, "data");
// Load sample Excel file containing chart.
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "sampleFindTypeOfXandYValuesOfPointsInChartSeries.xlsx"));

// Access first worksheet.
const worksheet = workbook.getWorksheets().get(0);

// Access first chart.
const chart = worksheet.getCharts().get(0);

// Calculate chart data.
chart.calculate();

// Access first chart point in the first series.
const point = chart.getNSeries().get(0).getPoints().get(0);

// Print the types of X and Y values of chart point.
console.log("X Value Type: " + point.getXValueType());
console.log("Y Value Type: " + point.getYValueType());
```  

## **مخرجات الوحدة**  

{{< highlight java >}}  
 X Value Type: IsString  

Y Value Type: IsNumeric  
{{< /highlight >}}  

