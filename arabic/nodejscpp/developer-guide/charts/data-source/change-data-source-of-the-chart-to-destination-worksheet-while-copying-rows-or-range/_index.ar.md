---
title: تغيير مصدر بيانات المخطط إلى ورقة الوجهة أثناء نسخ الصفوف أو النطاق باستخدام Node.js عبر C++
linktitle: تغيير مصدر البيانات للرسم البياني إلى ورقة العمل الوجهة أثناء نسخ الصفوف أو النطاق
description: تعلم كيفية تغيير مصدر بيانات مخطط إلى ورقة وجهة أثناء نسخ الصفوف أو نطاق في Aspose.Cells for Node.js via C++. يوضح هذا الدليل كيفية تحديث نطاق بيانات المخطط وربطه بورقة العمل الوجهة.
keywords: Aspose.Cells for Node.js via C++، المخططات، مصدر البيانات، ورقة العمل الوجهة، الصفوف، النطاق، النسخ، التحديث، نطاق البيانات، الربط.
type: docs
weight: 440
url: /ar/nodejs-cpp/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/
---

## **سيناريوهات الاستخدام المحتملة**

عند نسخ الصفوف أو النطاق الذي يحتوي على مخططات إلى ورقة عمل جديدة، فإن مصدر بيانات المخطط لا يتغير. على سبيل المثال، إذا كان مصدر البيانات للمخطط هو `=Sheet1!$A$1:$B$4`، فبعد نسخ الصفوف أو النطاق إلى ورقة عمل جديدة، سيظل مصدر البيانات كما هو، أي `=Sheet1!$A$1:$B$4`. لا يزال يشير إلى ورقة العمل القديمة، أي Sheet1. وهذا هو السلوك أيضًا في Microsoft Excel. إذا كنت ترغب في أن يشير إلى ورقة العمل الجديدة، يرجى استخدام الخاصية [**CopyOptions.getReferToDestinationSheet()**](https://reference.aspose.com/cells/nodejs-cpp/copyoptions/#getReferToDestinationSheet--) وضبطها على **true** عند استدعاء الطريقة [**Cells.copyRows(Cells, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#copyRows-cells-number-number-number-). الآن، إذا كانت ورقة العمل الوجهة الخاصة بك هي DestSheet، فسيتم تغيير مصدر البيانات للمخطط من `=Sheet1!$A$1:$B$4` إلى `=DestSheet!$A$1:$B$4`.

## **تغيير مصدر البيانات للرسم البياني إلى ورقة العمل الوجهة أثناء نسخ الصفوف أو النطاق**

يوضح الكود النموذجي التالي استخدام الخاصية [**CopyOptions.getReferToDestinationSheet()**](https://reference.aspose.com/cells/nodejs-cpp/copyoptions/#getReferToDestinationSheet--) أثناء نسخ الصفوف أو النطاق الذي يحتوي على مخططات إلى ورقة عمل جديدة. يستخدم الكود ملف Excel النموذجي (5113699.xlsx) ويولد ملف Excel الناتج (5113697.xlsx).

![todo:image_alt_text](change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range_1.png)

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Load sample excel file
const wb = new AsposeCells.Workbook(filePath);

// Access the first sheet which contains chart
const source = wb.getWorksheets().get(0);

// Add another sheet named DestSheet
const destination = wb.getWorksheets().add("DestSheet");

// Set CopyOptions.ReferToDestinationSheet to true
const options = new AsposeCells.CopyOptions();
options.setReferToDestinationSheet(true);

// Copy all the rows of source worksheet to destination worksheet which includes chart as well
// The chart data source will now refer to DestSheet
destination.getCells().copyRows(source.getCells(), 0, 0, source.getCells().getMaxDisplayRange().getRowCount(), options);

// Save workbook in xlsx format
wb.save(path.join(dataDir, "output_out.xlsx"), AsposeCells.SaveFormat.Xlsx);
```
