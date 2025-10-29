---
title: تلقائيًا ملء ارتفاع الصف عند تحميل الملف باستخدام Node.js عبر C++
linktitle: تكييف ارتفاع الصف تلقائياً عند تحميل الملف
type: docs
weight: 120
url: /ar/nodejs-cpp/autofit-row-height/
description: تعلم كيفية ملاءمة الصفوف التي لا يتم تخصيص ارتفاعها عند تحميل ملف باستخدام Aspose.Cells for Node.js via C++.
keywords: ملء تلقائي لارتفاع الصف عند تحميل ملف Node.js عبر C++، لضبط ارتفاع الصف تلقائيًا عند فتح ملف إكسل عبر Node.js باستخدام C++ 
---

## **سيناريوهات الاستخدام المحتملة**
يتطابق ارتفاع الصف تلقائيًا مع خط المحتوى، ولكن عندما لا يتطابق ارتفاع الصف المخزن مع ارتفاع المحتوى في الملف، سيقوم إكسل تلقائيًا بضبط ارتفاع الصف عند تحميل الملف، في حين أن Aspose.Cells for Node.js via C++ لن يقوم بضبطه تلقائيًا لتحسين الأداء. إذا كنت بحاجة إلى استخدام برنامج Aspose.Cells لمطابقة ارتفاعات الخط تلقائيًا عند تحميل الملفات، يمكنك تحقيق ذلك من خلال المعامل [setAutoFitterOptions(AutoFitterOptions)](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/#setAutoFitterOptions-autofitteroptions-) في الكود الخاص بك.

يرجى الرجوع إلى صورة البيانات التالية. نلاحظ أن ارتفاع الصف المخزن في السطر 11 هو 15، لكن إكسل قام بضبط ارتفاع الصف تلقائيًا عند تحميل الملف.
<br>
<img src="1.png" width=70% />

## **ضبط ارتفاع الصف باستخدام Aspose.Cells for Node.js via C++**
إذا حملت الملف مباشرة وقمت بحفظه كملف PDF، لن يتم عرض البيانات بالكامل في PDF لأن ارتفاع الخط المخزن هو فقط 15.
<br>
<img src="2.png" width=70% />
<br>
إذا قمت بضبط المعامل [setAutoFitterOptions(AutoFitterOptions)](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/#setAutoFitterOptions-autofitteroptions-) على true عند تحميل الملف، فسيقوم Aspose.Cells تلقائيًا بضبط ارتفاع الصف. يمكن لارتفاع الصف المعدل تلبية متطلبات عرض النص بشكل فعال.
<br>
<img src="3.png" width=70% />

## **رمز النموذج لـ Node.js**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);
workbook.save(path.join(dataDir, "out.pdf"));

const loadOptions = new AsposeCells.LoadOptions();
loadOptions.setAutoFitterOptions(new AsposeCells.AutoFitterOptions());
loadOptions.getAutoFitterOptions().setOnlyAuto(true);
const book = new AsposeCells.Workbook(filePath, loadOptions);
book.save(path.join(dataDir, "out2.pdf"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
