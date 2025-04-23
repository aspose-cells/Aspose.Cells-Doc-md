---
title: قفل أو فك قفل الأشكال باستخدام Node.js عبر C++
linktitle: قفل أو فتح الشكل
type: docs
weight: 200
url: /ar/nodejs-cpp/lock-or-unlock-shapes/
description: يعرض هذا المقال رمز يوضح كيفية قفل أو فتح قفل الأشكال لحمايتها باستخدام مكتبة Aspose.Cells لـ Node.js عبر C++.
keywords: قفل أو فك قفل الأشكال باستخدام Node.js عبر C++، كيفية قفل أو فتح قفل الأشكال باستخدام Node.js عبر C++، قفل أو فك قفل الأشكال لحمايتها في Node.js عبر C++.
---

## **سيناريوهات الاستخدام المحتملة**

أحيانًا، تحتاج إلى حماية جميع الأشكال في بعض الأوراق لمنع تدميرها من قبل مواقف غير مرغوب فيها. في هذه الحالة، تحتاج إلى قفل جميع الأشكال في الورقة المحددة. 

يمكن أن يكون قفل الأشكال في جدول بيانات أو مستند مفيدًا لأسباب عدة:
1. منع التغييرات العرضية: يضمن قفل الأشكال عدم تحريكها أو تغيير حجمها أو حذفها عن طريق المستخدمين عن غير قصد. هذا مهم بشكل خاص في المستندات المعقدة حيث قد تُستخدم الأشكال للملاحظات التوضيحية، أو الرسوم التوضيحية، أو كجزء من تصميم المستند.
1. الحفاظ على التخطيط والتصميم: غالبًا ما تلعب الأشكال دورًا حيويًا في تنظيم المستند والتصميم البصري. يضمن قفلها الحفاظ على المظهر المقصود، مما يضمن بقاء المستند احترافيًا وجذابًا بصريًا.
1. سلامة البيانات: في جداول البيانات، يمكن استخدام الأشكال لإبراز نقاط بيانات مهمة، أو إضافة ملاحظات، أو تقديم تفسيرات بصرية. يضمن قفل هذه الأشكال بقاء المعلومات السياقية التي تقدمها دقيقة وسليمة.
1. الاتساق في المستندات المشتركة: عند التعاون على المستندات، قد يكون لدى المستخدمين المختلفين مستويات متنوعة من الخبرة. يساعد قفل الأشكال على الحفاظ على الاتساق عبر المستند عن طريق منع التعديلات غير المقصودة.
1. الأمان: في المستندات الحساسة، يمكن أن يكون قفل الأشكال جزءًا من استراتيجية أوسع لحماية المعلومات. على سبيل المثال، في التقارير المالية أو المستندات القانونية، يمكن استخدام الأشكال المقفلة لحماية الملاحظات أو النقاط المميزة التي توفر سياقًا هامًا.

أحيانًا، تحتاج إلى القدرة على تعديل أشكال معينة في أوراق عمل معينة محمية، وفي هذه الحالة، تحتاج إلى إلغاء قفل هذه الأشكال. ستوضح هذه المقالة بالتفصيل كيف يمكن قفل وفتح الأشكال المحددة.

## **كيفية قفل الأشكال لحمايتها في إكسيل**

إليك كيفية قفل الخلايا في Microsoft Excel:

1. افتح ملف إكسل الخاص بك: افتح ملف إكسل الذي يحتوي على الأشكال التي تريد قفلها.

1. اختيار الشكل: انقر على الشكل الذي تريد قفله. يمكنك أيضًا اختيار عدة أشكال بالضغط مع الاستمرار على مفتاح Ctrl والنقر على كل شكل.

1. فتح لوحة تنسيق الشكل: انقر بزر الماوس الأيمن على الشكل (الأشكال) المختار واختر "الحجم والخصائص." بدلاً من ذلك، يمكنك الذهاب إلى علامة التبويب "التنسيق" على الشريط، وفي مجموعة "الحجم"، انقر على أيقونة الحوار (السهم الصغير) لفتح لوحة "تنسيق الشكل".
1. قفل الشكل: في لوحة "تنسيق الشكل"، انتقل إلى علامة التبويب "الحجم والخصائص" (الرمز يبدو كمربع بأسهم). تحت قسم "الخصائص"، ضع علامة في مربع "مقفول".
<br>
<img src="1.png" width=60% />
1. حماية ورقة العمل: انتقل إلى علامة التبويب "مراجعة" على الشريط. انقر على "حماية الورقة". ضع كلمة مرور (اختياري) واختر الأذونات التي ترغب في السماح بها (مثل اختيار الخلايا المقفلة، تنسيق الخلايا، وهلم جرا). انقر "موافق".
<br>
<img src="2.png" width=60% />

## **كيفية قفل جميع الأشكال في ورقة عمل محددة**

لحماية جميع الأشكال في ورقة عمل محددة، استخدم وظيفة `worksheet.protect(ProtectionType.Objects)`، كما هو موضح في الكود النموذجي التالي.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

const text = "This is a test";
const worksheet = workbook.getWorksheets().get(0);

let shape = worksheet.getShapes().addTextBox(1, 0, 1, 0, 30, 100);
shape.setText(text);

shape = worksheet.getShapes().addRectangle(5, 0, 1, 0, 30, 100);
shape.setText(text);

shape = worksheet.getShapes().addButton(9, 0, 1, 0, 30, 100);
shape.setText(text);

shape = worksheet.getShapes().addOval(13, 0, 1, 0, 50, 100);
shape.setText(text);

// Protect all shapes in a specified worksheet 
shape.getWorksheet().protect(AsposeCells.ProtectionType.Objects); // Protects the entire worksheet.
// or shape.getWorksheet().protect(AsposeCells.ProtectionType.All); // Protects all shapes in the specified worksheet.
// or worksheet.protect(AsposeCells.ProtectionType.Objects); // Protects the entire worksheet.
// or worksheet.protect(AsposeCells.ProtectionType.All); // Protects all shapes in the specified worksheet.

workbook.save("Locked.xlsx", AsposeCells.SaveFormat.Xlsx);
```

## **كيفية إلغاء قفل الأشكال المحددة في ورقة عمل محمية**

لفتح قفل شكل معين في ورقة عمل محمية، استخدم `shape.isLocked`، كما هو موضح في الكود النموذجي التالي.

ملحوظة: `shape.isLocked` ذو معنى فقط عندما تكون ورقة العمل محمية.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Locked.xlsx");

// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Get protected worksheet
const worksheet = workbook.getWorksheets().get(0);

// Get the specified shape to be unlocked
const shape = worksheet.getShapes().get("TextBox 1");

// Unlock the specified shape
if (!worksheet.getProtection().getAllowEditingObject() && shape.isLocked()) {
shape.setIsLocked(false);
}

workbook.save("UnLocked.xlsx", AsposeCells.SaveFormat.Xlsx);
```

