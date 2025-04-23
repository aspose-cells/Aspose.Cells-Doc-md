---
title: اكتشف ما إذا كان مشروع VBA محميًا باستخدام Node.js عبر C++
linktitle: اكتشاف ما إذا كان المشروع VBA محميًا
type: docs
weight: 20
url: /ar/nodejs-cpp/find-out-if-vba-project-is-protected/
---

## ** اكتشف ما إذا كان مشروع VBA محميًا في Node.js**

يمكنك معرفة ما إذا كان مشروع VBA (تطبيقات Visual Basic) لملف إكسل الخاص بك محميًا أم لا باستخدام Aspose.Cells property [**VbaProject.isProtected()**](https://reference.aspose.com/cells/nodejs-cpp/vbaproject/#isProtected--).

## **الكود المثالي**

يقوم الرمز العملي التالي بإنشاء دفتر عمل ثم يتحقق مما إذا كان مشروع VBA محميًا أم لا. ثم يقوم بحماية مشروع VBA ويعيد التحقق مما إذا كان محميًا أم لا. يرجى مراجعة الناتج في وحدة التحكم كمرجع. قبل الحماية، يعيد [**VbaProject.isProtected()**](https://reference.aspose.com/cells/nodejs-cpp/vbaproject/#isProtected--) القيمة **خطأ** ولكن بعد الحماية، يعيد القيمة **صحيح**.

```javascript
const AsposeCells = require("aspose.cells.node");

// Create a workbook.
const wb = new AsposeCells.Workbook();

// Access the VBA project of the workbook.
const vbaProj = wb.getVbaProject();

// Find out if VBA Project is Protected using isProtected method.
console.log("IsProtected - Before Protecting VBA Project: " + vbaProj.isProtected());

// Protect the VBA project.
vbaProj.protect(true, "11");

// Find out if VBA Project is Protected using isProtected method.
console.log("IsProtected - After Protecting VBA Project: " + vbaProj.isProtected());
```

## **مخرجات الوحدة**

هذا هو إخراج المجموعة الخرجية للرمز العيني أعلاه للمرجع.

{{< highlight java >}}

IsProtected - Before Protecting VBA Project: False

IsProtected - After Protecting VBA Project: True

{{< /highlight >}}
