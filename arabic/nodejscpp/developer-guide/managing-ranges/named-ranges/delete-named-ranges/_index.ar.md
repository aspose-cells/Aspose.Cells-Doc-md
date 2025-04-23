---
title: حذف النطاقات المعرفة باستخدام Node.js عبر C++
linktitle: حذف المدى المسمى
type: docs
weight: 90
url: /ar/nodejs-cpp/Delete-named-ranges/
description: يمكنك تعلم كيفية إزالة الأسماء المعرفة أو النطاقات المعرفة من ملفات Excel أو OpenOffice باستخدام Aspose.Cells for Node.js via C++.
---

## **مقدمة**
إذا كان هناك الكثير من الأسماء المحددة أو النطاقات المسماة في ملفات Excel، يجب علينا مسح بعضها لأنها لم يتم الرجوع إليها مرة أخرى.

## **إزالة النطاق المسمى في MS Excel**

لإزالة نطاق مسمى من Excel، يمكنك اتباع هذه الخطوات:
1. افتح Microsoft Excel وافتح المصنف الذي يحتوي على النطاق المسمى.
2. انتقل إلى علامة "الصيغ" في شريط أدوات Excel.
3. انقر على زر "مدير الأسماء" في مجموعة "الأسماء المحددة". سيفتح ذلك صندوق حوار مدير الأسماء.
4. في صندوق حوار مدير الأسماء، حدد النطاق المسمى الذي تريد إزالته.
5. انقر على الزر "حذف". قم بتأكيد الحذف عندما يُطلب.
6. انقر على الزر "إغلاق" لإغلاق صندوق حوار مدير الأسماء.
7. احفظ المصنف للحفاظ على التغييرات.

## **حذف النطاق المعرف باستخدام Aspose.Cells for Node.js via C++**
باستخدام Aspose.Cells for Node.js via C++، يمكنك إزالة النطاقات المعرفة أو الأسماء المحددة بواسطة [نص](https://reference.aspose.com/cells/nodejs-cpp/namecollection/#remove-string-) أو [فهرس](https://reference.aspose.com/cells/nodejs-cpp/namecollection/#removeAt-number-) في القائمة.

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook(filePath);

// Get all the worksheets in the book.
const worksheets = workbook.getWorksheets();

// Deleted a named range by text.
worksheets.getNames().remove("NamedRange");

// Deleted a defined name by index. Ensure to check the count before removal.
if (worksheets.getNames().getCount() > 0) {
worksheets.getNames().removeAt(0);
}

// Save the workbook to retain the changes.
workbook.save("Book2.xlsx");
```

ملاحظة: إذا تم الإشارة إلى الاسم المعرف بواسطة الصيغ، لا يمكن إزالته. يمكننا فقط إزالة صيغة الاسم المعرف.

## **إزالة بعض النطاقات المسماة**
عندما نقوم بإزالة اسم محدد، يجب علينا التحقق مما إذا كانت تتم الرجوع إليه في جميع الصيغ في الملف.
لتحسين أداء إزالة النطاقات المعرفة، يمكننا إزالتها معًا.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook(filePath);

// Get all the worksheets in the book.
const worksheets = workbook.getWorksheets();

// Deleted some defined names.
worksheets.getNames().remove(["NamedRange1", "NamedRange2"]);

// Save the workbook to retain the changes.
workbook.save("Book2.xlsx");
```

## **إزالة الأسماء المحددة المكررة**
تصاب بعض ملفات Excel بالضرر بسبب تكرار الأسماء المعرفة. لذلك، يمكننا إزالة الأسماء المكررة لإصلاح الملف.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");
// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook(filePath);

// Get all the worksheets in the book.
const worksheets = workbook.getWorksheets();

// Deleted some defined names.
worksheets.getNames().removeDuplicateNames();

// Save the workbook to retain the changes.
workbook.save("Book2.xlsx");
```



