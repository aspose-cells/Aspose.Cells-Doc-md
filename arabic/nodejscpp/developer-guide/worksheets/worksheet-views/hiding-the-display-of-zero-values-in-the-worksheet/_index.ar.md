---
title: إخفاء عرض القيم الصفرية في ورقة العمل باستخدام Node.js عبر C++
linktitle: إخفاء عرض القيم الصفرية في ورقة العمل
type: docs
weight: 50
url: /ar/nodejs-cpp/hiding-the-display-of-zero-values-in-the-worksheet/
description: سيعرض لك هذا المقال رمزًا توضيحيًا يشرح كيفية إخفاء القيم الصفرية برمجياً في جدول بيانات Excel باستخدام مكتبة Node.js عبر C++.
keywords: إخفاء القيم الصفرية في ورقة عمل Excel باستخدام Node.js عبر C++
---

{{% alert color="primary" %}} 

في بعض الأحيان، تحتاج إلى إخفاء القيم الصفرية في جدول بيانات. قد يكون اختيار شخصي أو معيار تنسيق.

{{% /alert %}} 

لإخفاء القيم الصفرية في ورقة العمل في Microsoft Excel (على سبيل المثال Microsoft Excel 2003):

1. من قائمة **الأدوات**، حدد **الخيارات**، ثم حدد علامة تبويب **العرض**.
1. ألغِ تحديد خيار **قيم الصفر**.
1. انقر على **موافق**.

 يرجى مراجعة رمز المثال أدناه الذي يوضح إخفاء الأصفار باستخدام Aspose.Cells for Node.js via C++.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xlsx");
// Create a new Workbook object
const workbook = new AsposeCells.Workbook(filePath);

// Get First worksheet of the workbook
const sheet = workbook.getWorksheets().get(0);

// Hide the zero values in the sheet
sheet.setDisplayZeros(false);

// Save the workbook
workbook.save(path.join(dataDir, "outputfile.out.xlsx"));
```
