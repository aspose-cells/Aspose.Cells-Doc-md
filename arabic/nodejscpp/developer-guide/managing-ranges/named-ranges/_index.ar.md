---
title: إنشاء مصنف ونطاقات أسماء ذات نطاق ورقة عمل باستخدام Node.js عبر C++
linktitle: النطاق المسمى
type: docs
weight: 40
url: /ar/nodejs-cpp/create-workbook-and-worksheet-scoped-named-ranges/
description: تعلم كيفية إنشاء مصنف ونطاقات أسماء ذات نطاق ورقة عمل باستخدام Aspose.Cells for Node.js via C++. 
---

{{% alert color="primary" %}} 

يسمح Microsoft Excel للمستخدمين بتحديد مجالات مسماة بنطاقين مختلفين: نطاق العمل (المعروف أيضا باسم نطاق عالمي) ونطاق الورقة العمل.

- يمكن الوصول إلى مجالات مسماة ذات نطاق العمل من أي ورقة عمل ضمن هذا المصنف ببساطة عن طريق استخدام اسمها.
- تتم الوصول إلى مجالات المسميات ذات نطاق ورقة العمل باستخدام مرجع لورقة العمل المعينة التي تم إنشاء المسمى فيها.

يوفر Aspose.Cells for Node.js via C++ نفس وظيفة Microsoft Excel لإضافة نطاقات مسماة بموجب المصنف وورقة العمل. عند إنشاء نطاق مسمى بموجب ورقة عمل، يجب استخدام إشارة ورقة العمل في النطاق المسمي لتحديده كنطاق مسمى بموجب ورقة عمل.

{{% /alert %}} 
## **إضافة نطاق مسمى بنطاق سجل العمل**


```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create a new Workbook object
const workbook = new AsposeCells.Workbook();

// Get first worksheet of the workbook
const sheet = workbook.getWorksheets().get(0);

// Get worksheet's cells collection
const cells = sheet.getCells();

// Create a range of Cells from Cell A1 to C10
const workbookScope = cells.createRange("A1", "C10");

// Assign the name to workbook scope named range
workbookScope.setName("workbookScope");

// Save the workbook
workbook.save(path.join(dataDir, "WorkbookScope.out.xlsx"));
```
## **إضافة نطاق مسمى بنطاق ورق العمل**


```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create a new Workbook object
const workbook = new AsposeCells.Workbook();

// Get first worksheet of the workbook
const sheet = workbook.getWorksheets().get(0);

// Get worksheet's cells collection
const cells = sheet.getCells();
// Create a range of Cells
const localRange = cells.createRange("A1", "C10");

// Assign name to range with sheet reference
localRange.setName("Sheet1!local");

// Save the workbook
workbook.save(path.join(dataDir, "output.out.xls"));
```

## **مواضيع متقدمة**
- [إنشاء الوصول ونسخ نطاقات مسماة](/cells/ar/nodejs-cpp/create-access-and-copy-named-ranges/)
- [تنسيق وتعديل نطاقات مسماة](/cells/ar/nodejs-cpp/format-and-modify-named-ranges/)
- [الحصول على نطاق مع روابط خارجية](/cells/ar/nodejs-cpp/get-range-with-external-links/)
- [تنفيذ نطاقات غير متتابعة](/cells/ar/nodejs-cpp/implementing-non-sequential-ranges/)


{{< app/cells/assistant language="nodejs-cpp" >}}
