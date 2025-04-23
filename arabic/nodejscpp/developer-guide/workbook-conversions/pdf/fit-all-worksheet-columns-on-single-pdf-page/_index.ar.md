---
title: ملائمة جميع أعمدة ورقة العمل على صفحة PDF واحدة باستخدام Node.js عبر C++
linktitle: ملائمة جميع أعمدة الصفحة العملية على صفحة PDF واحدة
type: docs
weight: 160
url: /ar/nodejs-cpp/fit-all-worksheet-columns-on-single-pdf-page/
---

{{% alert color="primary" %}}

أحيانًا تحتاج إلى إنشاء ملف PDF يلائم جميع أعمدة صفحة العملية على صفحة واحدة. توفر الخاصية [**PdfSaveOptions.getAllColumnsInOnePagePerSheet()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getAllColumnsInOnePagePerSheet--) هذه الميزة بطريقة سهلة الاستخدام جدًا. يتم التعامل مع الحسابات المعقدة مثل ارتفاع وعرض PDF الناتج داخليًا ويستند إلى البيانات في صفحة العملية.

{{% /alert %}}

## **ملائمة أعمدة صفحة العملية على صفحة PDF واحدة**

[**PdfSaveOptions.getAllColumnsInOnePagePerSheet()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getAllColumnsInOnePagePerSheet--) يضمن أن يتم عرض جميع أعمدة ورقة العمل على صفحة PDF واحدة، على الرغم من أن الصفوف قد تتوسع إلى عدة صفحات اعتمادًا على البيانات في ورقة العمل.

الكود النموذجي أدناه يوضح كيفية استخدام [**PdfSaveOptions.getAllColumnsInOnePagePerSheet()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getAllColumnsInOnePagePerSheet--) لعرض صفحة عمل كبيرة تحتوي على 100 عمود.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Create and initialize an instance of Workbook
const workbook = new AsposeCells.Workbook(path.join(dataDir, "TestBook.xlsx"));
// Create and initialize an instance of PdfSaveOptions
const saveOptions = new AsposeCells.PdfSaveOptions();
// Set AllColumnsInOnePagePerSheet to true
saveOptions.setAllColumnsInOnePagePerSheet(true);
// Save Workbook to PDF format by passing the object of PdfSaveOptions
const outputFilePath = path.join(dataDir, "output.out.pdf");
workbook.save(outputFilePath, saveOptions);
```

{{% alert color="primary" %}}

عندما يحتوي ورق العمل المعطى على العديد من الأعمدة، قد يظهر ملف PDF المقرن بحجم صغير جدًا. لا يزال قابلاً للقراءة عند تكبيره في تطبيق العرض مثل Acrobat Reader.

{{% /alert %}} {{% alert color="primary" %}}

إذا كانت جداول البيانات الخاصة بك تحتوي على صيغ، من الأفضل استدعاء [**Workbook.calculateFormula()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#calculateFormula--) قبل تحويل جدول البيانات إلى تنسيق PDF. وذلك سيضمن إعادة حساب قيم الصيغ الخاصة وتقديم القيم الصحيحة في الملف الناتج PDF.

{{% /alert %}}
