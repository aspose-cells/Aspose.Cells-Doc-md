---
title: تجنب صفحة فارغة في ملف PDF الناتج عندما لا يوجد شيء للطباعة باستخدام Node.js عبر C++
linktitle: تجنب الصفحة الفارغة في ملف PDF الناتج عندما لا يوجد شيء للطباعة
type: docs
weight: 30
url: /ar/nodejs-cpp/avoid-blank-page-in-output-pdf-when-there-is-nothing-to-print/
description: تعلم كيفية تجنب صفحات فارغة في ملف PDF الناتج عندما لا يوجد شيء للطباعة باستخدام Aspose.Cells for Node.js via C++.
---

## **سيناريوهات الاستخدام المحتملة**

 عند كون ملف إكسل فارغ ويقوم المستخدم بحفظه كملف PDF باستخدام Aspose.Cells for Node.js via C++، يتم عرض صفحة فارغة في ملف PDF الناتج. أحيانًا يكون هذا السلوك الافتراضي غير مرغوب فيه. توفر Aspose.Cells الخاصية [**PdfSaveOptions.getOutputBlankPageWhenNothingToPrint()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getOutputBlankPageWhenNothingToPrint--) لمعالجة هذه المشكلة. إذا قمت بضبطها على **false**، فسيحدث استثناء في حال عدم وجود شيء للطباعة في ملف PDF الناتج.

## **تجنب الصفحة الفارغة في ملف PDF الناتج عندما لا يوجد شيء للطباعة**

 ينشئ المثال التالي كودًا نموذجيًا لمصنف فارغ ثم يحفظه كملف PDF بعد ضبط الخاصية [**PdfSaveOptions.getOutputBlankPageWhenNothingToPrint()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getOutputBlankPageWhenNothingToPrint--) على **false**. بما أنه لا يوجد شيء للطباعة في ملف PDF الناتج، يحدث استثناء كما هو موضح أدناه.

## **الكود المثالي**

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

// Create empty workbook.
const wb = new AsposeCells.Workbook();

// Create Pdf save options.
const opts = new AsposeCells.PdfSaveOptions();

// Default value of OutputBlankPageWhenNothingToPrint is true.
// Setting false means - Do not output blank page when there is nothing to print.
opts.setOutputBlankPageWhenNothingToPrint(false);

// Save workbook to Pdf format, it will throw exception because workbook has nothing to print.
const ms = new Uint8Array();

try {
// Save to Pdf format. It will throw exception.
wb.save(ms, opts);
} catch (ex) {
console.error("Exception Message: " + ex.message + "\r\n");
}
```

## **استثناء**

{{< highlight javascript >}}

 exception was unhandled

  HResult=-2146232832

  Message=There is nothing to output/print.

  Source=Aspose.Cells

  StackTrace:

       at Aspose.Cells.Workbook.Save(String fileName, SaveOptions saveOptions)

{{< /highlight >}}
