---
title: إزالة الصفوف المكررة في ورقة العمل باستخدام Node.js عبر C++
linktitle: إزالة الصفوف المكررة في ورقة العمل
type: docs
weight: 370
url: /ar/nodejs-cpp/remove-duplicate-rows-in-a-worksheet/
description: تعلم كيفية إزالة الصفوف المكررة في ورقة العمل باستخدام Aspose.Cells for Node.js via C++ واختيار أعمدة محددة لفحص التكرار.
---

{{% alert color="primary" %}}

إزالة الصفوف المكررة هي واحدة من الميزات المفيدة في Microsoft Excel. تتيح للمستخدمين إزالة الصفوف المكررة في ورقة العمل، ويمكنك اختيار الأعمدة التي يجب فحصها للتكرار.

 يوفر Aspose.Cells for Node.js via C++ طريقة `Cells.removeDuplicates()` لهذا الغرض. يمكنك أيضًا تعيين `startRow`، `startColumn`، `endRow`، و `endColumn` لتحديد نطاق الأعمدة المراد فحصها للتكرار.

فيما يلي الملفات العينية التي يمكن تنزيلها لاختبار هذه الميزة:

[removeduplicates.xlsx](removeduplicates.xlsx)

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "removeduplicates.xlsx");

// Create workbook
const book = new AsposeCells.Workbook(filePath);

// Remove Duplicate
book.getWorksheets().get(0).getCells().removeDuplicates(0, 0, 5, 3);

// Save result
book.save("removeduplicates-result.xlsx");
```
