---
title: تعبئة تلقائية لنطاق من ملف إكسل باستخدام Node.js عبر C++
linktitle: نطاق ملء تلقائي
type: docs
weight: 105
url: /ar/nodejs-cpp/autofill-ranges/
description: تعلم كيفية القيام بعملية التعبئة التلقائية في نطاق معين من ملف إكسل باستخدام Aspose.Cells for Node.js via C++.
---

## **أداء عملية ملء تلقائي في النطاق المحدد في اكسل**

في إكسل، اختر نطاقًا، حرك الماوس إلى أسفل يمين، واسحب "زائد" للتعبئة التلقائية للبيانات.

## **ملء تلقائي لنطاقات باستخدام Aspose.Cells for Node.js via C++**

يظهر المثال التالي كيفية إجراء عملية التعبئة التلقائية على نطاق، وها هو ملف النموذج الذي يمكن تنزيله لاختبار هذه الميزة:

[range_autofill.xlsx](range_autofill.xlsx)

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "range_autofill.xlsx");

// Create a Workbook
const workbook = new AsposeCells.Workbook(filePath);
// Get Cells
const cells = workbook.getWorksheets().get(0).getCells();
// Create Range
const src = cells.createRange("C3:C4");
const dest = cells.createRange("C5:C10");
// AutoFill
src.autoFill(dest, AsposeCells.AutoFillType.Series);
// Save the Workbook
workbook.save("range_autofill_result.xlsx");
```

