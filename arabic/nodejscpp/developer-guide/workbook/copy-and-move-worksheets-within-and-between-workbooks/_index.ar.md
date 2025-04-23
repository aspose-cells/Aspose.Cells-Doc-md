---
title: نسخ ونقل أوراق العمل داخل ومابين دفاتر العمل باستخدام Node.js عبر C++
linktitle: نسخ ونقل أوراق العمل داخل وبين أوراق العمل
type: docs
weight: 80
url: /ar/nodejs-cpp/copy-and-move-worksheets-within-and-between-workbooks/
description: تعلّم كيفية نسخ ونقل أوراق العمل داخل ومابين دفاتر العمل باستخدام Aspose.Cells for Node.js via C++. إدارة بنية دفتر العمل بكفاءة.
---

{{% alert color="primary" %}}

أحيانًا، تحتاج إلى عدد من أوراق العمل مع تنسيقات وإدخال بيانات مشتركة. على سبيل المثال، إذا كنت تعمل مع الميزانيات الربعية، قد ترغب في إنشاء دفتر عمل يحتوي على أوراق تحتوي على نفس عناوين الأعمدة وعناوين الصفوف والصيغ. هناك طريقة للقيام بذلك: عن طريق إنشاء ورقة واحدة ثم نسخها ثلاث مرات.

يدعم Aspose.Cells for Node.js via C++ نسخ أو نقل أوراق العمل داخل أو بين دفاتر العمل. يتم نسخ أوراق العمل بما في ذلك البيانات والتنسيق والجداول والمصفوفات والرسوم البيانية والصور وغيرها من الكائنات بأعلى درجة من الدقة.

{{% /alert %}}

## **نسخ ونقل أوراق العمل**

### **نسخ ورقة عمل داخل دفتر عمل**

الخطوات الأولية هي نفسها لجميع الأمثلة.

1. أنشئ معينين بيانات في Microsoft Excel. لأغراض هذا المثال، قمنا بإنشاء معينين جديدين في Microsoft Excel وإدخال بعض البيانات إلى أوراق العمل.

- FirstWorkbook.xlsx (3 ورقات عمل).
- SecondWorkbook.xlsx (ورقة عمل واحدة).

1. قم بتنزيل وتثبيت Aspose.Cells:
   1. [تحميل Aspose.Cells for Node.js via C++](https://downloads.aspose.com/cells/nodejs-cpp).
   1. قم بتثبيته على كمبيوتر التطوير الخاص بك.
      جميع [مكونات Aspose](http://www.aspose.com/) ، عند التثبيت، تعمل في وضع التقييم. وضع التقييم ليس له حد زمني ولكنه يضيف علامات مائية فقط إلى المستندات المنتجة.
1. أنشئ مشروعًا:
   1.ابدأ بيئة تطويرك.
   1. أنشئ تطبيقًا جديدًا على الكونسول.
1. أضف مراجع:
   1. أضف مرجعًا إلى Aspose.Cells إلى المشروع.
      على سبيل المثال، أضف مرجع إلى ...\Program Files\Aspose\Aspose.Cells\Bin\NodeJs\Aspose.Cells.dll
1. نسخ ورقة العمل داخل دفتر العمل
   المثال الأول يقوم بنسخ الورقة الأولى (نسخ) داخل FirstWorkbook.xlsx.

عند تنفيذ الكود، يتم نسخ ورقة العمل التي تحمل اسم نسخ داخل FirstWorkbook.xlsx بإسم الورقة الأخيرة.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Open a file into the first book.
const excelWorkbook1 = new AsposeCells.Workbook(path.join(dataDir, "FirstWorkbook.xlsx"));

// Copy the first sheet of the first book within the workbook
excelWorkbook1.getWorksheets().get(2).copy(excelWorkbook1.getWorksheets().get("Copy"));

// Save the file.
excelWorkbook1.save(path.join(dataDir, "FirstWorkbookCopied_out.xlsx"));
```

### **نقل ورقة العمل داخل دفتر العمل**

يظهر الكود أدناه كيفية نقل ورقة العمل من موقع إلى آخر في دفتر العمل. عند تنفيذ الكود، يتم نقل ورقة العمل التي تسمى Move من المؤشر 1 إلى المؤشر 2 في FirstWorkbook.xlsx.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "FirstWorkbook.xlsx");
// Open a file into the first book.
const excelWorkbook2 = new AsposeCells.Workbook(filePath);

// Move the sheet
const worksheets = excelWorkbook2.getWorksheets();
const worksheet = worksheets.get(0);
worksheet.moveTo(1);

// Save the file.
excelWorkbook2.save(path.join(dataDir, "FirstWorkbookMoved_out.xlsx"));
```

### **نسخ ورقة العمل بين دفاتر العمل**

ينفذ الرمز نسخة من ورقة العمل المسماة Copy إلى ملف SecondWorkbook.xlsx باسم Sheet2.

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const excelWorkbook3 = new AsposeCells.Workbook();
const excelWorkbook4 = new AsposeCells.Workbook();

// Create source worksheet
excelWorkbook3.getWorksheets().add("Copy");

// Add new worksheet into second Workbook
excelWorkbook4.getWorksheets().add();

// Copy the first sheet of the first book into second book.
excelWorkbook4.getWorksheets().get(1).copy(excelWorkbook3.getWorksheets().get("Copy"));

// Save the file.
excelWorkbook4.save(path.join(dataDir, "CopyWorksheetsBetweenWorkbooks_out.xlsx"));
```

### **نقل ورقة العمل بين دفاتر العمل**

عند تنفيذ الكود، يتم نقل ورقة العمل المسماة Move من FirstWorkbook.xlsx إلى SecondWorkbook.xlsx بإسم Sheet3.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create new workbooks instead of opening existing files
const excelWorkbook5 = new AsposeCells.Workbook();
const excelWorkbook6 = new AsposeCells.Workbook();

// Add New Worksheet
excelWorkbook6.getWorksheets().add();

// Copy the sheet from first book into second book.
excelWorkbook6.getWorksheets().get(0).copy(excelWorkbook5.getWorksheets().get(0));

// Remove the copied worksheet from first workbook
excelWorkbook5.getWorksheets().removeAt(0);

// Save the file.
excelWorkbook5.save(path.join(dataDir, "FirstWorkbookWithMove_out.xlsx"));

// Save the file.
excelWorkbook6.save(path.join(dataDir, "SecondWorkbookWithMove_out.xlsx"));
```
