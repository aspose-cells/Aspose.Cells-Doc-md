---
title: تنفيذ نظام التاريخ 1904 باستخدام Node.js عبر C++
description: Aspose.Cells هي مكتبة Node.js للعمل مع ملفات جداول البيانات. تدعم تنفيذ نظام التاريخ 1904، مما يسمح للمستخدمين بحساب وتنسيق البيانات استنادًا إلى نظام التاريخ 1 يناير 1904. تصف هذه المقالة كيفية تنفيذ نظام التاريخ 1904 باستخدام مكتبة Aspose.Cells.
keywords: Aspose.Cells، نظام التاريخ 1904، جدول البيانات، الحساب، التنسيق، Node.js عبر C++
type: docs
weight: 7000
url: /ar/nodejs-cpp/implement-1904-date-system/
---

{{% alert color="primary" %}} 

يدعم Microsoft Excel نظامي التاريخ: نظام التاريخ 1900 (نظام التاريخ الافتراضي في Excel لنظام Windows) ونظام التاريخ 1904. يُستخدم نظام التاريخ 1904 عادةً لتوفير التوافق مع ملفات Excel لنظام Mac وهو النظام الافتراضي إذا كنت تستخدم Excel لنظام Mac. يمكنك ضبط نظام التاريخ 1904 لملفات Excel باستخدام Aspose.Cells for Node.js via C++. 

{{% /alert %}} 

لتنفيذ نظام التاريخ 1904 في Microsoft Excel (على سبيل المثال، Microsoft Excel 2003):

1. من القائمة **الأدوات**, حدد **الخيارات**, وحدد **الحساب**.
1. حدد خيار **نظام تاريخ 1904**.
1. انقر على **موافق**.

|**اختيار نظام تاريخ 1904 في Microsoft Excel**|
| :- |
|![todo:image_alt_text](implement-1904-date-system_1.png)|

انظر إلى الرمز البريدي العيني التالي حول كيفية تحقيق ذلك باستخدام واجهات برمجة التطبيقات Aspose.Cells.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xlsx");
// Initialize a new Workbook
// Open an excel file
const workbook = new AsposeCells.Workbook(filePath);

// Implement 1904 date system
workbook.getSettings().setDate1904(true);

// Save the excel file
workbook.save(path.join(dataDir, "Mybook.out.xlsx"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
