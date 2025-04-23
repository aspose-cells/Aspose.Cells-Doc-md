---
title: تعيين رمز تنسيق القيم لسلسلة المخطط باستخدام Node.js عبر C++
description: تعلم كيفية تعيين رمز تنسيق القيم لسلسلة المخطط في Aspose.Cells for Node.js via C++. ستساعدك هذه الدليل على فهم كيفية تنسيق بيانات سلسلة المخطط الخاصة بك باستخدام رمز التنسيق المناسب، مما يتيح لك تقديم بياناتك بدقة واحترافية.
keywords: Aspose.Cells لـ Node.js، سلسلة المخطط، رمز تنسيق القيم، التنسيق، عرض البيانات، الدقة، الاحترافية.
linktitle: تنسيق الأرقام
type: docs
weight: 100
url: /ar/nodejs-cpp/set-the-values-format-code-of-chart-series/
---

## **سيناريوهات الاستخدام المحتملة**
يمكنك تعيين رمز تنسيق القيم لسلسلة المخطط باستخدام الخاصية [Series.getValuesFormatCode()](https://reference.aspose.com/cells/nodejs-cpp/series/#getValuesFormatCode--) . هذه الخاصية ليست مفيدة فقط للسلسلة المستندة إلى النطاق داخل ورقة العمل ولكنها تعمل أيضًا بشكل جيد للسلسلة التي تم إنشاؤها بمصفوفة من القيم.

## **تعيين رمز تنسيق القيم لسلاسل الرسم البياني**
الكود النموذجي التالي يضيف سلسلة في مخطط فارغ لم يكن لديه سلسلة من قبل. يضيف السلسلة باستخدام مصفوفة القيم. بمجرد إضافة السلسلة، يتم تنسيقها باستخدام رمز $#,##0 باستخدام الخاصية [Series.getValuesFormatCode()](https://reference.aspose.com/cells/nodejs-cpp/series/#getValuesFormatCode--) وتحول الرقم 10000 إلى $10,000. تظهر الصورة الملتقطة تأثير الرمز على ملف إكسل النموذجي (51740712.xlsx) وملف الإكسل الناتج (51740713.xlsx) بعد التنفيذ.

![todo:image_alt_text](set-the-values-format-code-of-chart-series_1.png)

## **الكود المثالي**
```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "51740712.xlsx");

// Load the source Excel file 
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access first chart
const chart = worksheet.getCharts().get(0);

// Add series using an array of values
chart.getNSeries().add("{10000, 20000, 30000, 40000}", true);

// Access the series and set its values format code
const series = chart.getNSeries().get(0);
series.setValuesFormatCode("$#,##0");

// Save the output Excel file
workbook.save(path.join(dataDir, "51740713.xlsx"));
```
