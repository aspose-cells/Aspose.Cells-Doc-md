---
title: نسخ النطاقات من إكسل باستخدام Node.js عبر C++
linktitle: نسخ النطاقات
type: docs
weight: 105
url: /ar/nodejs-cpp/copy-ranges-of-Excel/
---

## **مقدمة**

في اكسل، يمكنك تحديد نطاق، ونسخ النطاق، ثم لصقه بخيارات محددة إلى نفس ورقة العمل، أوراق العمل الأخرى، أو ملفات أخرى.

## **نسخ النطاقات باستخدام Aspose.Cells for Node.js via C++**

يوفر Aspose.Cells for Node.js via C++ بعض طرق التحميل الزائد [Range.copy(Range, PasteOptions)](https://reference.aspose.com/cells/nodejs-cpp/range/#copy-range-pasteoptions-) لنسخ النطاق. و [Range.copyStyle(Range)](https://reference.aspose.com/cells/nodejs-cpp/range/#copyStyle-range-) لنقل نمط النسخة فقط؛ [Range.copyData(Range)](https://reference.aspose.com/cells/nodejs-cpp/range/#copyData-range-) لنقل قيمة النطاق فقط.

## **نسخ النطاق**

إنشاء نطاقين: النطاق المصدر، والنطاق الهدف، ثم نسخ النطاق المصدر إلى النطاق الهدف باستخدام طريقة `Range.copy`.

انظر الكود التالي:

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook();

// Get all the worksheets in the book.
let worksheets = workbook.getWorksheets();

// Get the first worksheet in the worksheets collection.
let worksheet = workbook.getWorksheets().get(0);

// Create a range of cells.
let sourceRange = worksheet.getCells().createRange("A1", "A2");

// Input some data with some formattings into A few cells in the range.
sourceRange.get(0, 0).setValue("Test");
sourceRange.get(1, 0).setValue(123);

// Create target range of cells.
let targetRange = worksheet.getCells().createRange("B1", "B2");

// Copy source range to target range in the same worksheet 
targetRange.copy(sourceRange);

// Create target range of cells.
workbook.getWorksheets().add();
worksheet = workbook.getWorksheets().get(1);

targetRange = worksheet.getCells().createRange("A1", "A2");
// Copy source range to target range in another worksheet 
targetRange.copy(sourceRange);

// Copy to another workbook
const anotherWorkbook = new AsposeCells.Workbook();

worksheet = workbook.getWorksheets().get(0);

targetRange = worksheet.getCells().createRange("A1", "A2");
// Copy source range to target range in another workbook 
targetRange.copy(sourceRange);
```

## **لصق النطاق مع الخيارات**

يدعم Aspose.Cells for Node.js via C++ لصق النطاق بأنواع محددة.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Get all the worksheets in the book.
const worksheets = workbook.getWorksheets();

// Get the first worksheet in the worksheets collection.
const worksheet = workbook.getWorksheets().get(0);

// Create a range of cells.
const sourceRange = worksheet.getCells().createRange("A1", "A2");

// Input some data with some formattings into
// A few cells in the range.
sourceRange.get(0, 0).setValue("Test");
sourceRange.get(1, 0).setValue(123);

// Create target range of cells.
const targetRange = worksheet.getCells().createRange("B1", "B2");

// Init paste options.
const options = new AsposeCells.PasteOptions();
// Set paste type.
options.setPasteType(AsposeCells.PasteType.ValuesAndFormats);
options.setSkipBlanks(true);
// Copy source range to target range
targetRange.copy(sourceRange, options);
```

## **نسخ بيانات النطاق فقط**

أيضًا، يمكنك نسخ البيانات باستخدام طريقة `Range.copyData` كما هو موضح في الكود التالي:

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Get all the worksheets in the book.
const worksheets = workbook.getWorksheets();

// Get the first worksheet in the worksheets collection.
const worksheet = worksheets.get(0);

// Create a range of cells.
const sourceRange = worksheet.getCells().createRange("A1", "A2");

// Input some data with some formattings into
// A few cells in the range.
sourceRange.get(0, 0).setValue("Test");
sourceRange.get(1, 0).setValue(123);

// Create target range of cells.
const targetRange = worksheet.getCells().createRange("B1", "B2");

// Copy the data of source range to target range
targetRange.copyData(sourceRange);
```

## **مواضيع متقدمة**
- [نسخ أطوال الصفوف من النطاق المصدر إلى النطاق الهدف](/cells/ar/nodejs-cpp/copy-row-heights-of-source-range-to-destination-range/)

