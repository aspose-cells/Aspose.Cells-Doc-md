---
title: تصفية الكائنات أثناء تحميل دفتر العمل أو ورقة العمل باستخدام Node.js عبر C++
linktitle: تصفية الكائنات أثناء تحميل المصنف أو ورقة العمل
type: docs
weight: 330
url: /ar/nodejs-cpp/filter-objects-while-loading-workbook-or-worksheet/
description: تعلم كيفية تصفية البيانات أثناء تحميل دفاتر العمل أو أوراق العمل باستخدام Aspose.Cells for Node.js via C++.
---

## **سيناريوهات الاستخدام المحتملة**
يرجى استخدام الخاصية [LoadOptions.getLoadFilter()](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/#getLoadFilter--) أثناء تصفية البيانات من دفتر العمل. ولكن إذا كنت تريد تصفية البيانات من أوراق عمل فردية، فستحتاج إلى تجاوز طريقة [LoadFilter.startSheet(Worksheet)]((https://reference.aspose.com/cells/nodejs-cpp/loadfilter/#startSheet-worksheet-))، يرجى تقديم القيمة المناسبة من تعداد [LoadDataFilterOptions](https://reference.aspose.com/cells/nodejs-cpp/loaddatafilteroptions) عند إنشاء أو العمل مع [LoadFilter](https://reference.aspose.com/cells/nodejs-cpp/loadfilter).

تحتوي تعداد [LoadDataFilterOptions](https://reference.aspose.com/cells/nodejs-cpp/loaddatafilteroptions) على القيم التالية الممكنة.

- الكل
- إعدادات الكتاب
- خلية فارغة
- خلية مع تخطيط
- بيانات الخلية
- خطأ الخلية
- رقم الخليّة
- سلسلة الخليّة
- قيمة الخلية
- Chart
- تنسيق شرطي
- التحقق من البيانات
- الأسماء المعرفة
- خصائص المستند
- صيغة
- الروابط الفائقة
- منطقة مدمجة
- الجدول المحوري
- الإعدادات
- الشكل
- بيانات الورقة
- إعدادات الورقة
- البنية
- النمط
- الجدول
- VBA
- خريطة Xml

## **تصفية الكائنات أثناء تحميل دفتر العمل**
يوضح الكود المصدري التالي كيفية تصفية الرسوم البيانية من دفتر العمل. يرجى التحقق من [ملف الإكسل العيني](5115258.xlsx) المستخدم في هذا الكود و [ملف PDF الناتج](5115257.pdf) الذي تم إنشاؤه بواسطته. كما يمكنك رؤية في ملف PDF الناتج، تم تصفية جميع الرسوم البيانية من دفتر العمل.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Filter charts from the workbook.
const lOptions = new AsposeCells.LoadOptions();
lOptions.setLoadFilter(new AsposeCells.LoadFilter(AsposeCells.LoadDataFilterOptions.All & ~AsposeCells.LoadDataFilterOptions.Chart));

// Load the workbook with above filter.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sampleFilterCharts.xlsx"), lOptions);

// Save worksheet to a single PDF page.
const pOptions = new AsposeCells.PdfSaveOptions();
pOptions.setOnePagePerSheet(true);

// Save the workbook in PDF format.
workbook.save(path.join(dataDir, "sampleFilterCharts.pdf"), pOptions);
```

## **تصفية الكائنات أثناء تحميل ورقة العمل**
يقوم الكود المصدري التالي بتحميل [ملف الإكسل الأصلي](5115255.xlsx) ويقوم بتصفية البيانات التالية من ورقات العمل باستخدام تصفية مخصصة.

- يتم تصفية الرسوم البيانية من ورقة العمل التي تحمل اسم لا توجد فيها رسوم بيانية.
- يتم تصفية الأشكال من ورقة العمل التي تحمل اسم لا توجد فيها أشكال.
- يتم تصفية التنسيق الشرطي من ورقة العمل التي تحمل اسم لا توجد فيها تنسيق شرطي.

يقوم بتحميل ملف Excel المصدر (5115255.xlsx) بتصفية مخصصة، ثم يأخذ صور جميع ورقات العمل بشكل تتابع. إليك صور الإخراج للإشارة. كما يمكنك أن ترى، الصورة الأولى ليست تحتوي على رسوم بيانية، الصورة الثانية ليست تحتوي على أشكال، والصورة الثالثة ليست تحتوي على تنسيق شرطي.

- [NoCharts.png](5115254.png)
- [NoShapes.png](5115256.png)
- [NoConditionalFormatting.png](5115251.png)

```javascript
const AsposeCells = require("aspose.cells.node");

class CustomLoadFilter extends AsposeCells.LoadFilter {
startSheet(sheet) {
if (sheet.getName() === "NoCharts") {
// Load everything and filter charts
this.loadDataFilterOptions = AsposeCells.LoadDataFilterOptions.All & ~AsposeCells.LoadDataFilterOptions.Chart;
}

if (sheet.getName() === "NoShapes") {
// Load everything and filter shapes
this.loadDataFilterOptions = AsposeCells.LoadDataFilterOptions.All & ~AsposeCells.LoadDataFilterOptions.Drawing;
}

if (sheet.getName() === "NoConditionalFormatting") {
// Load everything and filter conditional formatting
this.loadDataFilterOptions = AsposeCells.LoadDataFilterOptions.All & ~AsposeCells.LoadDataFilterOptions.ConditionalFormatting;
}
}
}
```

هكذا تستخدم فئة CustomLoadFilter حسب أسماء ورقة العمل.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

async function run() {
// Source directory
const sourceDir = path.join(__dirname, "data");

// Output directory
const outputDir = path.join(__dirname, "output");

// Filter worksheets using CustomLoadFilter class
const loadOpts = new AsposeCells.LoadOptions();
loadOpts.setLoadFilter(new CustomLoadFilter());

// Load the workbook with filter defined in CustomLoadFilter class
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "sampleCustomFilteringPerWorksheet.xlsx"), loadOpts);

// Take the image of all worksheets one by one
for (let i = 0; i < workbook.getWorksheets().getCount(); i++) {
// Access worksheet at index i
const worksheet = workbook.getWorksheets().get(i);

// Create an instance of ImageOrPrintOptions
// Render entire worksheet to image
const imageOpts = new AsposeCells.ImageOrPrintOptions();
imageOpts.setOnePagePerSheet(true);
imageOpts.setImageType(AsposeCells.ImageType.Png);

// Convert worksheet to image
const render = new AsposeCells.SheetRender(worksheet, imageOpts);
render.toImage(0, path.join(outputDir, `outputCustomFilteringPerWorksheet_${worksheet.getName()}.png`));
}
}

run();
```
{{< app/cells/assistant language="nodejs-cpp" >}}
