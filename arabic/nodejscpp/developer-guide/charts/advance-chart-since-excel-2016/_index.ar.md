---  
title: قراءة وتعديل مخططات Excel 2016 باستخدام Node.js عبر ++C  
linktitle: قراءة وتلاعب رسومات Excel 2016  
description: تعلم كيفية قراءة وتعديل مخططات Excel 2016 باستخدام Aspose.Cells for Node.js via C++. ستظهر لك هذه الدليل كيفية الوصول وتعديل خصائص المخطط المختلفة.  
keywords: Aspose.Cells لـ Node.js، مخططات Excel 2016، قراءة، تعديل، وسوم البيانات، ألوان السلاسل، التخطيط، المخططات الهرمية، المخططات الدائرية.  
type: docs  
weight: 48  
url: /ar/nodejs-cpp/read-and-manipulate-excel-2016-charts/  
---  

## **سيناريوهات الاستخدام المحتملة**  
أصبحت Aspose.Cells الآن تدعم قراءة وتلاعب الرسومات Microsoft Excel 2016 التي لم تكن موجودة في Microsoft Excel 2013 أو الإصدارات السابقة.  
## **قراءة وتلاعب شكل بيانات Excel 2016**  
يعرض الكود النموذجي التالي تحميل ملف Excel المصدر ([source excel file](22774101.xlsx)) الذي يحتوي على مخططات Excel 2016 في أول ورقة عمل. يقوم بقراءة جميع المخططات واحدًا تلو الآخر ويغير عنوانه وفقًا لنوع المخطط. تظهر لقطة الشاشة التالية الملف المصدر قبل تنفيذ الكود. كما ترى، عنوان المخطط هو نفسه لجميع المخططات.

![todo:image_alt_text](read-and-manipulate-excel-2016-charts_1.png)

تظهر اللقطة الشاشية التالية [ملف Excel الناتج](22774104.xlsx) بعد تنفيذ الكود. كما تلاحظ، تم تغيير عنوان الرسم حسب نوعه.

![todo:image_alt_text](read-and-manipulate-excel-2016-charts_2.png)  
## **الكود المثالي**  
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "excel2016Charts.xlsx");

// Load source excel file containing excel 2016 charts
const workbook = new AsposeCells.Workbook(filePath);

// Access the first worksheet which contains the charts
const sheet = workbook.getWorksheets().get(0);

// Access all charts one by one and read their types
for (let i = 0; i < sheet.getCharts().getCount(); i++) {
// Access the chart
const ch = sheet.getCharts().get(i);

// Print chart type
console.log(ch.getType());

// Change the title of the charts as per their types
ch.getTitle().setText("Chart Type is " + ch.getType().toString());
}

// Save the workbook
workbook.save(path.join(dataDir, "out_excel2016Charts.xlsx"));
```  
## **مخرجات الوحدة**  
إليك إخراج وحدة التحكم للشيفرة النموذجية أعلاه عند تنفيذها مع [ملف Excel المصدر المقدم](22774101.xlsx).

{{< highlight javascript >}}  

 Waterfall  

Treemap  

Sunburst  

Histogram  

BoxWhisker  

{{< /highlight >}}  

## **مواضيع متقدمة**  
- [إنشاء رسم بياني Waterfall](/cells/ar/nodejs-cpp/creating-waterfall-chart/)  
- [إنشاء رسم بياني TreeMap](/cells/ar/nodejs-cpp/creating-treemap-chart/)  
- [إنشاء رسم بياني Sunburst](/cells/ar/nodejs-cpp/creating-sunburst-chart/)  

