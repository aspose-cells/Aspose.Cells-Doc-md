---
title: كيفية طباعة ملف Excel لاستخدام صفحات عريضة وارتفاع كامل مع Node.js عبر C++
linktitle: كيفية طباعة إكسل كصفحات مناسبة للعرض بشكل واسع ومرتفعة
type: docs
weight: 200
url: /ar/nodejs-cpp/how-to-print-excel-as-fitted-pages-wide-and-tall/
description: توضح هذه المقالة رمزًا يشرح كيفية تعيين FitToPagesWide و FitToPagesTall باستخدام Aspose.Cells for Node.js via C++.
keywords: Node.js عبر C++ كيفية تعيين FitToPagesWide و FitToPagesTall، كيفية إضافة FitToPagesWide و FitToPagesTall في Node.js، كيفية تعيين FitToPagesWide و FitToPagesTall في Excel، كيفية مسح FitToPagesWide و FitToPagesTall في Excel، كيفية طباعة Excel كصفحات عريضة وارتفاع كامل، كيفية طباعة ورقة العمل كصفحة واحدة، كيفية طباعة جميع أعمدة ورقة العمل في صفحة واحدة.
---

## **مقدمة**

يتم استخدام إعدادات FitToPagesWide و FitToPagesTall في تطبيقات جداول البيانات (مثل مايكروسوفت إكسل) للتحكم في كيفية تكبير الجدول عند الطباعة. تساعد هذه الإعدادات على ضمان أن المخرجات المطبوعة تتوافق مع عدد معين من الصفحات، أفقياً وعمودياً. إليك شرح لكل إعداد:

1. FitToPagesWide: يحدد هذا الإعداد عدد الصفحات عرضه يجب أن تتناسب مع المخرجات المطبوعة. على سبيل المثال، ضبطه إلى 1 يعني أن المحتوى سيتم تكبيره ليتلاءم مع عرض صفحة واحدة بغض النظر عن عرض الجدول.
 2. FitToPagesTall: يحدد هذا الإعداد عدد الصفحات ارتفاعًا الذي يجب أن يتناسب معه الناتج المطبوع. على سبيل المثال، تعيين FitToPagesTall إلى 1 يعني أن المحتوى سيتم تكبيره ليتناسب مع ارتفاع صفحة واحدة، بغض النظر عن عدد الصفوف.

## **لماذا نستخدم FitToPagesWide و FitToPagesTall**
وفيما يلي بعض الأسباب لضبط هذا الإعداد:
1. التحكم في التنسيق المطبوع: من خلال تحديد عدد الصفحات عرضاً وارتفاعاً، يمكنك ضمان أن يكون المستند المطبوع سهل القراءة ومنظم بشكل جيد، دون تقسيم الأعمدة أو الصفوف بشكل غير مناسب عبر الصفحات.
 2. الاتساق: إذا كنت تطبع عدة أوراق أو تقارير، فإن استخدام هذه الإعدادات يساعد على الحفاظ على تنسيق موحد، مما يسهل مقارنة وتحليل المستندات المطبوعة.
 3. عرض تقديمي احترافي: يمكن أن يؤدي تكبير المحتوى وتكييفه بشكل صحيح لعدد معين من الصفحات إلى عرض تقديمي أكثر احترافية واحترافية لبياناتك.

## **كيفية طباعة الملف كصفحات مناسبة عريضة وطويلة في Excel**

لتعيين إعدادات FitToPagesWide و FitToPagesTall في Microsoft Excel، اتبع الخطوات التالية:

1. افتح مصنف Excel الخاص بك وانتقل إلى الورقة التي تريد طباعةها.
 2. انتقل إلى علامة التبويب تخطيط الصفحة على الشريط.
 3. في مجموعة إعداد الصفحة، انقر على السهم الصغير في الزاوية اليمنى السفلى لفتح مربع حوار إعداد الصفحة.
 4. في مربع حوار إعداد الصفحة، انتقل إلى علامة التبويب الصفحة.
 5. تحت مقياس، اختر خيار "تتناسب مع" ثم حدد عدد الصفحات عريضة ومرتفعة التي تريدها: أدخل عدد الصفحات العريضة في المربع الأول (تتناسب مع x صفحات عريضة). أدخل عدد الصفحات المرتفعة في المربع الثاني (تتناسب مع y صفحات عالية).
<br>
<img src="2.png" width=60% />

 6. انقر على موافق لتطبيق الإعدادات.

## ** كيفية طباعة ملف Excel كصفحات عريضة وارتفاع كامل باستخدام Aspose.Cells for Node.js via C++**

 لتعيين FitToPagesWide و FitToPagesTall في ورقة عمل محددة: أولاً، قم بتحميل [ملف العينة](input.xlsx)، ثم تحتاج إلى تعديل خصائص [**PageSetup.getFitToPagesTall()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getFitToPagesTall--) و [**PageSetup.getFitToPagesWide()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getFitToPagesWide--) من كائن [**PageSetup**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/) للورقة المطلوبة. إليك مثال في Node.js:

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "input.xlsx");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook(filePath);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Setting the number of pages to which the length of the worksheet will be spanned
worksheet.getPageSetup().setFitToPagesTall(1);

// Setting the number of pages to which the width of the worksheet will be spanned
worksheet.getPageSetup().setFitToPagesWide(1);

// Save the workbook
workbook.save("out_net.pdf");
```

نتيجة الإخراج:
<br>
<img src="1.png" width=60% />

## ** كيفية طباعة ورقة عمل كصفحة واحدة باستخدام Aspose.Cells for Node.js via C++**

لطباعة ورقة العمل كصفحة واحدة: أولاً، قم بتحميل [ملف العينة](sample.xlsx)، ثم تحتاج إلى تعيين خاصية [**PdfSaveOptions.getOnePagePerSheet()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getOnePagePerSheet--) من كائن [**PdfSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/). إليك مثال في Node.js:

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

const options = new AsposeCells.PdfSaveOptions();
options.setOnePagePerSheet(true);

// Save the workbook.
workbook.save("OnePagePerSheet.pdf", options);
```

نتيجة الإخراج:
<br>
<img src="3.png" width=60% />

## **كيفية طباعة جميع أعمدة ورقة العمل في صفحة واحدة باستخدام Aspose.Cells for Node.js via C++**

لطباعة جميع أعمدة ورقة العمل في صفحة واحدة: أولاً، قم بتحميل [ملف العينة](sample.xlsx)، ثم تحتاج إلى تعيين خاصية [**PdfSaveOptions.getAllColumnsInOnePagePerSheet()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getAllColumnsInOnePagePerSheet--) من كائن [**PdfSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/). إليك مثال في Node.js:

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

const options = new AsposeCells.PdfSaveOptions();
options.setAllColumnsInOnePagePerSheet(true);

// Save the workbook.
workbook.save("AllColumnsInOnePagePerSheet.pdf", options);
```

نتيجة الإخراج:
<br>
<img src="4.png" width=60% />
