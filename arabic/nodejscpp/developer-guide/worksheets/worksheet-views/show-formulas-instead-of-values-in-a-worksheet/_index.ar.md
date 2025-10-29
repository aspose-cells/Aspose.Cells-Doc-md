---
title: عرض الصيغ بدلاً من القيم في ورقة عمل باستخدام Node.js عبر C++
linktitle: عرض الصيغ بدلاً من القيم في ورقة العمل
type: docs
weight: 20
url: /ar/nodejs-cpp/show-formulas-instead-of-values-in-a-worksheet/
description: توفر هذه المقالة رمز نموذجياً لاستخدام واجهة برمجة التطبيقات Node.js عبر C++ لعرض الصيغ بدلاً من القيم في ورقة عمل أو جدول بيانات إكسل برمجياً.
---

{{% alert color="primary" %}}

من الممكن عرض الصيغ بدلاً من القيم المحسوبة في Microsoft Excel باستخدام خيار **إظهار الصيغ** من شريط **الصيغ**. عندما يتم عرض الصيغ، يعرض Microsoft Excel الصيغ في ورقة العمل. يمكنك تحقيق الشيء ذاته باستخدام Aspose.Cells for Node.js via C++.

{{% /alert %}}

توفر Aspose.Cells خاصية اختيار التحقق من الأخطاء. تدير فئة {0} أنواع مختلفة من فحوصات الأخطاء، على سبيل المثال، الأرقام المخزنة كنص، أخطاء حساب الصيغ، وأخطاء التحقق من الصحة. استخدم تعداد {1} لضبط نوع التحقق من الأخطاء المطلوب.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "source.xlsx");

// Load the source workbook
const workbook = new AsposeCells.Workbook(filePath);

// Access the first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Show formulas of the worksheet
worksheet.setShowFormulas(true);

// Save the workbook
workbook.save(path.join(dataDir, ".out.xlsx"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
