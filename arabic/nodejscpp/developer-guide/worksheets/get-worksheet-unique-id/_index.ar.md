---
title: الحصول على معرف فريد للورقة باستخدام Node.js عبر C++
linktitle: الحصول على معرّف الورقة العمل فريد
type: docs
weight: 190
url: /ar/nodejs-cpp/get-worksheet-unique-id/
description: توضح هذه المقالة كيفية الحصول على المعرف الفريد لورقة عمل إكسل باستخدام مكتبة Node.js و API C++ برمجياً.
keywords: معرف فريد لورقة إكسل باستخدام Node.js عبر C++، معرف فريد لورقة باستخدام Node.js عبر C++
---

## **الحصول على معرف فريد لورقة العمل**

يوفر Aspose.Cells for Node.js via C++ القدرة على الحصول على المعرف الفريد لورقة العمل باستخدام الخاصية [**Worksheet.getUniqueId()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getUniqueId--). يوضح مقطع الكود التالي استخدام الخاصية [**Worksheet.getUniqueId()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getUniqueId--) لطباعة المعرف الفريد لورقة العمل. يستخدم هذا المقطع الملف [الملف النموذجي لإكسل](105480213.xlsx).

### كود المصدر

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const sourceDir = path.join(__dirname, "data");

// Load source Excel file
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "Book1.xlsx"));

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Print Unique Id
console.log("Unique Id: " + worksheet.getUniqueId());
```
