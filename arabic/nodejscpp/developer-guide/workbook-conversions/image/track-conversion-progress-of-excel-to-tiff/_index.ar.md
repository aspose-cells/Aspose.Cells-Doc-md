---
title: تتبع تقدم التحويل من Excel إلى TIFF باستخدام Node.js عبر C++
linktitle: تتبع تقدم التحويل من إكسيل إلى TIFF
type: docs
weight: 190
url: /ar/nodejs-cpp/track-conversion-progress-of-excel-to-tiff/
description: تعلم كيفية تتبع تقدم تحويل ملفات Excel إلى TIFF باستخدام Aspose.Cells for Node.js via C++. عزز تجربة المستخدم أثناء عملية التحويل.
---

## **سيناريوهات الاستخدام المحتملة**

أحيانًا قد يستغرق تحويل ملفات Excel الكبيرة بعض الوقت. خلال هذا الوقت، قد ترغب في عرض تقدم تحويل المستند بدلاً من شاشة تحميل فقط لتعزيز قابلية استخدام تطبيقك. يدعم Aspose.Cells for Node.js via C++ تتبع عملية تحويل المستند من خلال توفير واجهة {0}. توفر الواجهة {1} {2} و {3} التي يمكنك تنفيذها في فئتك المخصصة. يمكنك أيضًا التحكم في الصفحات التي يتم عرضها كما هو موضح في الفئة {TestPageSavingCallback} المخصصة.

## **تتبع تقدّم تحويل Excel إلى TIFF**

الكود التالي يقوم بتحميل ملف Excel المصدر (95584311.xlsx) ويطبع تقدم التحويل في وحدة التحكم باستخدام الفئة المخصصة {TestPageSavingCallback} التي تنفذ الواجهة {0}. الملف الناتج مرتبط للرجوع إليه.

[Output File](95584312.tiff)

## **الكود المثالي**

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// Source directory
const sourceDir = path.join(__dirname, "data");

// Output directory
const outputDir = path.join(__dirname, "output");

const filePath = path.join(sourceDir, "sampleUseWorkbookRenderForImageConversion.xlsx");
const workbook = new AsposeCells.Workbook(filePath);
const opts = new AsposeCells.ImageOrPrintOptions();

// Define TestTiffPageSavingCallback
class TestTiffPageSavingCallback {
// Implement required methods for the callback here
}

opts.setPageSavingCallback(new TestTiffPageSavingCallback());
opts.setImageType(AsposeCells.ImageType.Tiff);

const wr = new AsposeCells.WorkbookRender(workbook, opts);
wr.toImage(path.join(outputDir, "DocumentConversionProgressForTiff_out.tiff"));
```

الكود التالي هو للفئة المخصصة {TestTiffPageSavingCallback}.

```javascript
const AsposeCells = require("aspose.cells.node");

class TestTiffPageSavingCallback {
pageStartSaving(args) {
console.log(`Start saving page index ${args.pageIndex} of pages ${args.pageCount}`);

// Don't output pages before page index 2.
if (args.pageIndex < 2) {
args.setIsToOutput(false);
}
}

pageEndSaving(args) {
console.log(`End saving page index ${args.pageIndex} of pages ${args.pageCount}`);

// Don't output pages after page index 8.
if (args.pageIndex >= 8) {
args.setHasMorePages(false);
}
}
}
```

## **مخرجات الوحدة**

{{< highlight java >}}

Start saving page index 0 of pages 10</br>
End saving page index 0 of pages 10</br>
Start saving page index 1 of pages 10</br>
End saving page index 1 of pages 10</br>
Start saving page index 2 of pages 10</br>
End saving page index 2 of pages 10</br>
Start saving page index 3 of pages 10</br>
End saving page index 3 of pages 10</br>
Start saving page index 4 of pages 10</br>
End saving page index 4 of pages 10</br>
Start saving page index 5 of pages 10</br>
End saving page index 5 of pages 10</br>
Start saving page index 6 of pages 10</br>
End saving page index 6 of pages 10</br>
Start saving page index 7 of pages 10</br>
End saving page index 7 of pages 10</br>
Start saving page index 8 of pages 10</br>
End saving page index 8 of pages 10</br>

{{< /highlight >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
