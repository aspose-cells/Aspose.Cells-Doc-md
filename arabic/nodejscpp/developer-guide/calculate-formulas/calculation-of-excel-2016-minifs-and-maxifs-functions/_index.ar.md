---
title: حساب دالتي MINIFS و MAXIFS في Excel 2016 باستخدام Node.js عبر C++
description: تقدم هذه المقالة شرحًا لكيفية استخدام مكتبة Aspose.Cells لحساب دالتي MINIFS و MAXIFS في Excel 2016 باستخدام Node.js عبر C++. قم بتحميل ملف Excel موجود أو إنشائه، ثم استخدم طرق Aspose.Cells لحساب هذه الدوال وحفظ النتائج على القرص.
keywords: Aspose.Cells، Excel، 2016، دالة MINIFS، دالة MAXIFS، الحساب، Node.js عبر C++
type: docs
weight: 300
url: /ar/nodejs-cpp/calculation-of-excel-2016-minifs-and-maxifs-functions/
---

## **سيناريوهات الاستخدام المحتملة**
يدعم Excel 2016 من Microsoft دوال MINIFS و MAXIFS. هذه الدوال غير مدعومة في Excel 2013 أو الإصدارات الأقدم. كما يدعم Aspose.Cells for Node.js via C++ حساب هذه الدوال. يوضح لقطة الشاشة التالية استخدام هذه الدوال. يرجى قراءة التعليقات الحمراء داخل لقطة الشاشة لمعرفة كيفية عمل هذه الدوال.

![todo:image_alt_text](calculation-of-excel-2016-minifs-and-maxifs-functions_1.png)

## **حساب وظائف MINIFS و MAXIFS في Excel 2016**
يحمّل الكود النموذجي التالي ملف Excel النموذجي ويستدعي طريقة Workbook.calculateFormula() لإجراء حساب الصيغة عبر Aspose.Cells for Node.js via C++، ثم يحفظ النتائج في PDF الناتج.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const sourceFilePath = path.join(dataDir, "sampleMINIFSAndMAXIFS.xlsx");

// Load your source workbook containing MINIFS and MAXIFS functions
const workbook = new AsposeCells.Workbook(sourceFilePath);

// Perform Aspose.Cells formula calculation
workbook.calculateFormula();

// Save the calculations result in pdf format
const options = new AsposeCells.PdfSaveOptions();
options.setOnePagePerSheet(true);
const outputFilePath = path.join(dataDir, "outputMINIFSAndMAXIFS.pdf");
workbook.save(outputFilePath, options);
```
