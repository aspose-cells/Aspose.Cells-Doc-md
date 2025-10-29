---
title: قراءة عنوان الرسم البياني من ملف ODS باستخدام Node.js عبر C++
linktitle: قراءة عنوان المخطط من ملف ODS
description: تعلم كيفية استخدام Aspose.Cells for Node.js via C++ لقراءة عنوان الرسم البياني من ملف جدول بيانات من المستند المفتوح (ODS). سيُظهر دليلنا كيفية استخراج والوصول إلى عنوان الرسم البياني لمزيد من التحليل أو العرض.
keywords: Aspose.Cells for Node.js via C++، قراءة عنوان الرسم البياني، ملف جدول بيانات المستند المفتوح، ملف ODS، استخراج الرسم البياني، تحليل البيانات.
type: docs
weight: 160
url: /ar/nodejs-cpp/read-chart-subtitle-from-ods-file/
---

## **قراءة عنوان الرسم البياني من ملف ODS**

يوفر Aspose.Cells إمكانية قراءة عناوين الرسوم البيانية في ملفات ODS باستخدام خاصية [**Chart.getSubTitle()**](https://reference.aspose.com/cells/nodejs-cpp/chart/#getSubTitle--). يحمّل الكود النموذجي التالي ملف ODSExample (89620481.ods) ويقرأ عنوان الرسم البياني باستخدام الخاصية [**Chart.getSubTitle()**](https://reference.aspose.com/cells/nodejs-cpp/chart/#getSubTitle--) ويطبع النتيجة في نافذة وحدة التحكم. يُرجى مراجعة مخرجات الكود أدناه للمرجعية.

## **الكود المثالي**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");
// Load excel file containing charts
const filePath = path.join(sourceDir, "SampleChart.ods");
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access first chart inside the worksheet
const chart = worksheet.getCharts().get(0);

console.log("Chart Subtitle: " + chart.getSubTitle().getText());
```

## **مخرجات الوحدة**

{{< highlight javascript >}}

Chart Subtitle: Sample Chart Subtitle

{{< /highlight >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
