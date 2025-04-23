---
title: تجميد الصف العلوي (الصفوف العليا) في ورقة إكسل باستخدام Node.js عبر C++
linktitle: تجميد الصفوف
type: docs
weight: 190
url: /ar/nodejs-cpp/how-to-freeze-rows-of-excel-worksheet
description: في هذا المقال، ستتعلم كيفية تجميد الصفوف العلوية من أوراق عمل إكسل برمجيًا باستخدام مكتبة Node.js وواجه برمجة تطبيقات C++.
keywords: تجميد الصفوف العلوية، تجميد الصف الأعلى في Node.js باستخدام C++.
---

## **مقدمة**

في هذا المقال، سنتعلم كيف نجمد الصف (الصفوف) العلوية. عندما يكون لديك كمية هائلة من البيانات تحت عنوان مشترك، لا يمكنك رؤية العنوان عند التمرير لأسفل في الورقة. يمكنك تجميد الصفوف العليا بحيث يمكنك رؤية الجزء المجمد حتى عند تمرير الباقي من البيانات. يمكنك بسهولة رؤية رؤوس الأعمدة في الصفوف العليا.

## **تجميد الصفوف في إكسل**

**![تجميد الصفوف العلوية في إكسل](Freeze-Rows.png)**

1. إذا أردت تجميد الصف العلوي، فابدأ بتحديد الصف تحت الصف الذي يحتاج إلى تجميده.
2. انقر على عرض > تجميد الأجزاء.
3. في القائمة المنسدلة، انقر على تجميد الصف العلوي.
4. إذا قمت بالتمرير لأسفل، سيكون الصف الأول دائماً في أعلى العرض.

**![صف مجمد](Frozen-Row.png)**

كما ترى، الصف الأول مجمد؛ يبقى الصف الأول دائمًا في أعلى العرض عند التمرير لأسفل.

تجميد الصفوف يتيح لك عرض بياناتك الكبيرة بدون الحاجة لمتابعة تسميات الصفوف.

## **تجميد الصفوف باستخدام Aspose.Cells for Node.js via C++**
من السهل تجميد الصف (الصفوف) باستخدام Aspose.Cells for Node.js via C++. 
يرجى استخدام طريقة [**Worksheet.freezePanes(number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#freezePanes-number-number-number-number-) لتجميد الصف (الصفوف) عند الصف المحدد.
1. إنشاء دفتر العمل لفتح الملف أو إنشاء ملف فارغ.
2. تجميد الصف الأول باستخدام طريقة Worksheet.freezePanes()
3. حفظ الملف.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Freeze.xlsx");

// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook(filePath);

// Freezing panes at the cell B2
workbook.getWorksheets().get(0).freezePanes("A2", 1, 0);

// Saving the file
workbook.save("frozen.xlsx");
```

[ملف Excel مصدري عينة مرفق](../Freeze.xlsx).
