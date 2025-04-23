---  
title: العثور على ما إذا كانت نقاط البيانات موجودة في المخطط الدائري الثاني أو الشريط على مخطط دائري من دائري باستخدام Node.js عبر C++  
linktitle: العثور على ما إذا كانت نقاط البيانات في الرسم البياني الدائري الثاني أو الرسم البياني الشريطي الثاني  
description: تعلم كيفية استخدام Aspose.Cells for Node.js via C++ للعثور على ما إذا كانت نقاط البيانات موجودة في الدائري الثاني أو الشريط على مخطط دائري من دائري. سيُوضح دليلنا كيفية تحديد والوصول إلى الدائري الثانوي أو الشريط على مخطط مركب، مما يتيح لك تحليل البيانات وتعديلها بشكل فعال.  
keywords: Aspose.Cells for Node.js via C++، مخطط دائري من دائري، مخطط شريطي من دائري، دائري ثانوي، شريط ثانوي، تحليل بيانات، معالجة بيانات.  
type: docs  
weight: 180  
url: /ar/nodejs-cpp/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/  
---  

## **سيناريوهات الاستخدام المحتملة**  
 يمكنك العثور على ما إذا كانت نقاط البيانات في السلسلة ضمن الدائري الثاني على مخطط *الدائري من دائري* أو في الشريط على مخطط *شريطي من دائري* باستخدام Aspose.Cells for Node.js via C++. يرجى استخدام خاصية [ChartPoint.isInSecondaryPlot()](https://reference.aspose.com/cells/nodejs-cpp/chartpoint/#isInSecondaryPlot--) لتحديد ذلك.  

 يرجى تحميل [ملف Excel النموذجي](5115193.xlsx) المستخدم في كود المثال التالي ومراجعة ناتج وحدة التحكم الخاصة به. إذا قمت بفتح [ملف Excel النموذجي](5115193.xlsx)، ستجد أن جميع نقاط البيانات التي أقل من 10 تقع داخل الشريط على مخطط *الشريط من دائري* كما يظهر أيضًا في الناتج الخاص بوحدة التحكم.  
## **العثور على ما إذا كانت نقاط البيانات في الفقاعة الثانية أو العمود على مخطط 'بي of بي' أو 'عمود من بي'**  
 يظهر الكود المثال التالي كيفية تحديد ما إذا كانت نقاط البيانات في الدائري الثاني أو الشريط على مخطط *الدائري من دائري* أو *شريطي من دائري*.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Load source excel file containing Bar of Pie chart
const workbook = new AsposeCells.Workbook(path.join(dataDir, "PieBars.xlsx"));

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access first chart which is Bar of Pie chart and calculate it
const chart = worksheet.getCharts().get(0);
chart.calculate();

// Access the chart series
const series = chart.getNSeries().get(0);

/* 
* Print the data points of the chart series and 
* check its IsInSecondaryPlot property to determine 
* if data point is inside the bar or pie 
*/
for (let i = 0; i < series.getPoints().getCount(); i++) {
// Access chart point
const chartPoint = series.getPoints().get(i);

// Skip null values
if (chartPoint.get_YValue() === null) continue;

/* 
* Print the chart point value and see if it is inside bar or pie.
* If the IsInSecondaryPlot is true, then the data point is inside bar 
* otherwise it is inside the pie. 
*/
console.log("Value: " + chartPoint.get_YValue());
console.log("IsInSecondaryPlot: " + chartPoint.isInSecondaryPlot());
console.log();
}
```  
## **مخرجات الوحدة**  
 يرجى رؤية ناتج وحدة التحكم التالي الناتج عن تنفيذ الكود المثال أعلاه مع [ملف Excel النموذجي](5115193.xlsx). إذا كانت [ChartPoint.isInSecondaryPlot()](https://reference.aspose.com/cells/nodejs-cpp/chartpoint/#isInSecondaryPlot--) **خاطئة**، فإن نقطة البيانات تقع داخل الدائري وإذا كانت **صحيحة**، فإن نقطة البيانات تقع داخل الشريط.  

{{< highlight javascript >}}  
 Value: 15  
IsInSecondaryPlot: false  

Value: 9  
IsInSecondaryPlot: true  

Value: 2  
IsInSecondaryPlot: true  

Value: 40  
IsInSecondaryPlot: false  

Value: 5  
IsInSecondaryPlot: true  

Value: 4  
IsInSecondaryPlot: true  

Value: 25  
IsInSecondaryPlot: false  
{{< /highlight >}}  

