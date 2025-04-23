---
title: طرق مختلفة لفتح الملفات باستخدام Node.js عبر C++
linktitle: طرق مختلفة لفتح الملفات
type: docs
weight: 10
url: /ar/nodejs-cpp/different-ways-to-open-files/
description: تشرح هذه المقالة كيف تفتح ملف إكسل باستخدام واجهة برمجة التطبيقات Aspose.Cells for Node.js via C++.
keywords: فتح ملف إكسل باستخدام Node.js بدون Excel، كيف أفتح ملف إكسل باستخدام Node.js.
---

{{% alert color="primary" %}}

مع Aspose.Cells، من السهل فتح الملفات، على سبيل المثال، لاسترداد البيانات، أو لاستخدام قالب مصمم لتسريع عملية التطوير.

{{% /alert %}}

## **كيفية فتح ملف إكسل عبر مسار**

يمكن للمطورين فتح ملف Microsoft Excel باستخدام مسار الملف على الكمبيوتر المحلي عن طريق تحديده في منشئ فئة [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook). ببساطة قم بتمرير المسار كسلسلة نصية. ستقوم Aspose.Cells تلقائيًا باكتشاف نوع تنسيق الملف.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");
// Opening through Path
// Creating a Workbook object and opening an Excel file using its file path
const workbook1 = new AsposeCells.Workbook(filePath);
console.log("Workbook opened using path successfully!");
```

## **كيفية فتح ملف إكسل عبر تيار**

كما أنها سهلة الفتح كتيار. للقيام بذلك، استخدم نسخة محملة زائد من المنشئ يأخذ كائن *Stream* الذي يحتوي على الملف.

```javascript
try {
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book2.xls");
// Opening through Stream
// Create a Stream object
const fstream = fs.createReadStream(filePath);

// Creating a Workbook object, open the file from a Stream object
// That contains the content of file and it should support seeking
const chunks = [];
fstream.on('data', (chunk) => {
chunks.push(chunk);
```

## **كيفية فتح ملف بالبيانات فقط**

لفتح ملف يحتوي فقط على البيانات، استخدم فئتي [**LoadOptions**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions) و [**LoadFilter**](https://reference.aspose.com/cells/nodejs-cpp/loadfilter) لضبط السمات والخيارات ذات الصلة بالفئة لملف القالب الذي سيتم تحميله.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Load only specific sheets with data and formulas
// Other objects, items etc. would be discarded

// Instantiate LoadOptions specified by the LoadFormat
const loadOptions = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Xlsx);

// Set LoadFilter property to load only data & cell formatting
loadOptions.setLoadFilter(new AsposeCells.LoadFilter(AsposeCells.LoadDataFilterOptions.CellData));

// Create a Workbook object and opening the file from its path
const workbook = new AsposeCells.Workbook(path.join(dataDir, "Book1.xlsx"), loadOptions);
console.log("File data imported successfully!");
```

## **كيفية تحميل الأوراق المرئية فقط**

أثناء تحميل [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)، أحيانًا قد تحتاج فقط إلى البيانات في أوراق العمل المرئية في المصنف. يسمح لك Aspose.Cells بتخطي البيانات في أوراق العمل غير المرئية أثناء تحميل المصنف. للقيام بذلك، أنشئ دالة مخصصة ترث من فئة [**LoadFilter**](https://reference.aspose.com/cells/nodejs-cpp/loadfilter) ومرر كائنها إلى خاصية [**LoadOptions.getLoadFilter()**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/#getLoadFilter--).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const sampleFile = "output.xlsx";
const samplePath = path.join(dataDir, sampleFile);

// Create a sample workbook
// and put some data in first cell of all 3 sheets
const createWorkbook = new AsposeCells.Workbook();
createWorkbook.getWorksheets().get("Sheet1").getCells().get("A1").putValue("Aspose");
createWorkbook.getWorksheets().add("Sheet2").getCells().get("A1").putValue("Aspose");
createWorkbook.getWorksheets().add("Sheet3").getCells().get("A1").putValue("Aspose");
createWorkbook.getWorksheets().get("Sheet3").setIsVisible(false);
createWorkbook.save(samplePath);

// Load the sample workbook
const loadOptions = new AsposeCells.LoadOptions();
loadOptions.setLoadFilter(new AsposeCells.LoadFilter()); // Corrected line by defining LoadFilter properly

const loadWorkbook = new AsposeCells.Workbook(samplePath, loadOptions);
console.log(`Sheet1: A1: ${loadWorkbook.getWorksheets().get("Sheet1").getCells().get("A1").getValue()}`);
console.log(`Sheet1: A2: ${loadWorkbook.getWorksheets().get("Sheet2").getCells().get("A1").getValue()}`);
console.log(`Sheet1: A3: ${loadWorkbook.getWorksheets().get("Sheet3").getCells().get("A1").getValue()}`);
```

إليك تنفيذ فئة *CustomLoad* المشار إليها في المقتطف أعلاه.

```javascript
const { Workbook, LoadDataFilterOptions } = require("aspose.cells.node");

class CustomLoad {
startSheet(sheet) {
if (sheet.isVisible()) {
// Load everything from visible worksheet
this.loadDataFilterOptions = LoadDataFilterOptions.All;
} else {
// Load nothing
this.loadDataFilterOptions = LoadDataFilterOptions.Structure;
}
}
}
```

{{% alert color="primary" %}}

سيتم إلقاء استثناء إذا حاولت فتح ملفات إكسل غير أصلية أو تنسيقات ملفات أخرى (على سبيل المثال PPT/PPTX، DOC/DOCX، وغيرها) باستخدام Aspose.Cells.

{{% /alert %}} 

{{% alert color="primary" %}}

هناك احتمالات عادلة أن يُلقى منشئ [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) خطأ *OutOfMemoryError* أثناء تحميل جداول بيانات كبيرة. تشير هذه الاستثناء إلى أن الذاكرة المتاحة غير كافية لتحميل الجدول بالكامل في الذاكرة؛ لذلك، يجب تحميل الجدول مع تمكين تفضيلات الذاكرة.

{{% /alert %}}

