---  
title: معالجة الوحدات التلقائية لمحور المخطط مثل Microsoft Excel باستخدام Node.js عبر C++  
linktitle: التعامل مع الوحدات التلقائية لمحور الرسم البياني مثل Microsoft Excel  
description: تعلم كيفية التعامل مع الوحدات التلقائية على محاور المخطط في Aspose.Cells for Node.js via C++. سيعرض دليلنا كيفية تكوين وتخصيص الوحدات التلقائية على محور المخطط، بما في ذلك عرض الترقيم العلمي وتعديل المقياس.  
keywords: Aspose.Cells for Node.js via C++، محاور المخططات، الوحدات التلقائية، Microsoft Excel، التكوين، التخصيص، الترقيم العلمي، القياس.  
type: docs  
weight: 120  
url: /ar/nodejs-cpp/handle-automatic-units-of-chart-axis-like-microsoft-excel/  
---  

## **سيناريوهات الاستخدام المحتملة**  
لم تكن الإصدارات الأولى من Aspose.Cells for Node.js via C++ قادرة على التعامل مع الوحدات التلقائية لمحور المخطط بشكل صحيح عند عرض المخطط كصورة أو PDF. الآن، يدعم Aspose.Cells for Node.js via C++ معالجة الوحدات التلقائية لمحور المخطط. لا يوجد تغيير في الكود. كل ما عليك هو تحويل مخططك إلى صورة أو PDF وسيقوم بعرض محور المخطط تمامًا كما يعرضه Microsoft Excel.  

## **التعامل مع الوحدات التلقائية لمحور الرسم البياني مثل Microsoft Excel**  
الشفرة النموذجية التالية تقوم بتحميل [ملف Excel النموذجي](61767755.xlsx) وتوليد [مخطط PDF الناتج](61767752.pdf). تُظهر الصورة المقتطعة الوحدات التلقائية لمحور المخطط داخل مستطيلات حمراء وتقارن أيضًا بين مخطط ملف Excel النموذجي ومخطط PDF الناتج. كلاهما مطابق تمامًا.  

![todo:image_alt_text](handle-automatic-units-of-chart-axis-like-microsoft-excel_1.png)  

## **الكود المثالي**  
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleHandleAutomaticUnitsOfChartAxisLikeMicrosoftExcel.xlsx");

// Load the sample Excel file
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access first chart
const chart = worksheet.getCharts().get(0);

// Render chart to pdf
chart.toPdf("outputHandleAutomaticUnitsOfChartAxisLikeMicrosoftExcel.pdf");
```  
