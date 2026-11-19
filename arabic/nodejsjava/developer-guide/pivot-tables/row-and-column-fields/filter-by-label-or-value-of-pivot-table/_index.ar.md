---
title: تصفية الجداول المحورية حسب التسمية أو القيمة
description: يدعم Aspose.Cells for Node.js via Java إمكانيات تصفية شاملة للجداول المحورية. توضح هذه المقالة كيفية تصفية بيانات الجدول المحوري باستخدام مرشحات التسميات ومرشحات التاريخ ومرشحات القيم ومرشحات أعلى 10 وعن طريق إخفاء أو إظهار العناصر المحورية.
linktitle: تصفية الجداول المحورية حسب التسمية أو القيمة
url: /ar/nodejs-java/filter-by-label-or-value-of-pivot-table/
keywords: Aspose.Cells, مكتبة Node.js via Java, جدول بيانات, جدول محوري, مرشح, مرشح التسمية, مرشح القيمة, مرشح التاريخ, مرشح أعلى 10, عنصر محوري, إخفاء العنصر المحوري
type: docs
weight: 10
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
يوفر Aspose.Cells خمس استراتيجيات عملية لتصفية البيانات المعروضة في الجدول المحوري. يمكنك تطبيق مرشحات التسميات على حقول الصفوف أو الأعمدة المستندة إلى النصوص، واستخدام مرشحات التاريخ عندما يحتوي الحقل على خلايا تاريخ ووقت فقط أو خلايا فارغة، وتطبيق مرشحات القيم مقابل الأرقام المجمعة، واستخدام مرشحات أعلى 10 للترتيب حسب حقل قيمة، أو إخفاء وإظهار العناصر المحورية الفردية يدويًا باستخدام خاصية `IsHidden`. تتعرض كل استراتيجية من خلال واجهات برمجية مخصصة على فئتي `PivotField` و `PivotItem`.
{{% /alert %}}

## **المقدمة**
تعد الجداول المحورية أدوات تحليلية قوية، لكن الملخصات الخام غالبًا ما تحتوي على معلومات أكثر بكثير مما تحتاج إلى تقديمه. التصفية هي الآلية الأساسية لتضييق نطاق الجدول المحوري وصولًا إلى الصفوف أو الأعمدة أو القيم المهمة لتقرير معين. يعكس Aspose.Cells for Node.js via Java إمكانيات التصفية المتوفرة في Microsoft Excel، ويعرضها برمجيًا بحيث يمكن أتمتة إنشاء التقارير بالكامل.
تتناول هذه المقالة استراتيجيات التصفية التالية:
1. **مرشح التسمية** — يصفي عناصر حقل الصف أو العمود استنادًا إلى تسمياتها النصية.
2. **مرشح التاريخ** — يصفي حقول الصفوف أو الأعمدة التي تحتوي على قيم تاريخ ووقت فقط (أو خلايا فارغة).
3. **مرشح القيمة** — يصفي العناصر بناءً على القيم المجمعة لحقل بيانات.
4. **مرشح أعلى 10** — يعرض فقط أعلى أو أدنى عدد N من العناصر مرتبة حسب حقل قيمة.
5. **إخفاء / إظهار العناصر المحورية** — يتحكم يدويًا في رؤية كل عنصر فردي في حقل.
تستخدم كل طريقة دالة مختلفة على فئة `PivotField` أو خاصية على فئة `PivotItem`. بعد تطبيق أي مرشح، يجب استدعاء `getPivotCache().refresh()` على الجدول المحوري بحيث تعكس البيانات المخزنة مؤقتًا والقيم المحسوبة حالة المرشح الجديدة.

## **مرشح التسمية**
يتيح لك مرشح التسمية تصفية عناصر حقل الصف أو العمود بمقارنة تسمياتها النصية بنمط معين. يكون ذلك مفيدًا عندما تريد عرض المنتجات التي تبدأ أسماؤها بحرف معين فقط، أو تحتوي على كلمة محددة، أو تطابق معيارًا آخر قائمًا على التسمية.
يعرض Aspose.Cells تصفية التسميات من خلال دالة `PivotField.filterByLabel(PivotFilterType, string)`. يتضمن تعداد `PivotFilterType` قيمًا مثل `CaptionBeginsWith` و `CaptionContains` و `CaptionEndsWith` و `CaptionDoesNotContain` و `CaptionIsNotBlank` و `CaptionIsBlank` وغيرها. توفر الوسيطة الثانية سلسلة التسمية المستخدمة للمقارنة.
يقوم المثال التالي بتحميل مصنف يحتوي على جدول محوري موجود، ويطبق مرشح تسمية بحيث تظل العناصر التي تبدأ تسمياتها ببادئة محددة مرئية فقط، ثم يقوم بتحديث الجدول المحوري وحفظ النتيجة.

```javascript
const AsposeCells = require("aspose.cells");
let fileName = "sample.xlsx";
let prefix = "B";
// Load the existing workbook containing a pivot table
let workbook = new AsposeCells.Workbook(fileName);
// Access the worksheet by index (first worksheet)
let worksheet = workbook.getWorksheets().get(0);
// Access the pivot table by index
let pivotTable = worksheet.getPivotTables().get(0);
// Retrieve the first row PivotField
let rowField = pivotTable.getRowFields().get(0);
// Apply the label filter — show only row items whose labels begin with the supplied prefix
rowField.filterByLabel(AsposeCells.PivotFilterType.CAPTION_BEGINS_WITH, prefix, "");
// Refresh and recalculate the pivot table data so the filter takes effect
pivotTable.getPivotCache().refresh();
// Save the workbook back to disk
workbook.save(fileName);
```

## **مرشح التاريخ**
تتيح لك مرشحات التاريخ تضييق نطاق الجدول المحوري بناءً على معايير قائمة على التاريخ مثل اليوم أو الأسبوع الماضي أو هذا الشهر أو الربع القادم أو نطاق تاريخ محدد. وهي مرشحات متخصصة تعمل فقط ضد الحقول التي تخزن معلومات التاريخ والوقت.

{{% alert color="primary" %}}
لا يعمل مرشح التاريخ إلا عندما تحتوي منطقة الصف أو العمود على خلايا تاريخ ووقت فقط أو قيم فارغة. إذا كان الحقل الأساسي يحتوي على أنواع بيانات أخرى مثل الأرقام أو النصوص، فلن ينتج مرشح التاريخ النتيجة المتوقعة. تأكد من تنسيق الحقل كتاريخ ومن أن جميع القيم هي نسخ `DateTime` صالحة أو خلايا فارغة قبل تطبيق هذا المرشح.
يعرض Aspose.Cells تصفية التاريخ من خلال دالة `PivotField.filterByDate(PivotFilterType, params DateTime[] values)`. يحتوي تعداد `PivotFilterType` على قيم تاريخ مخصصة مثل `Today` و `Yesterday` و `LastWeek` و `ThisWeek` و `NextWeek` و `LastMonth` و `ThisMonth` و `NextMonth` و `LastQuarter` و `ThisQuarter` و `NextQuarter` و `LastYear` و `ThisYear` و `NextYear` و `Between`. بناءً على نوع المرشح المختار، يمكنك تمرير قيمة أو قيمتي `DateTime` (بالنسبة لـ `Between`، تمرر تاريخ البدء وتاريخ الانتهاء).
يقوم المثال التالي بتحميل مصنف يحتوي على جدول محوري توجد منطقة الصف فيه على حقل تاريخ، ويطبق مرشح تاريخ يقيد العناصر المرئية إلى نطاق تاريخ معين، ثم يقوم بتحديث الجدول المحوري وحفظ المصنف.
{{% /alert %}}

```javascript
const AsposeCells = require("aspose.cells");
const fs = require("fs");
let inputPath = "sample.xlsx";
let outputPath = "output_filtered.xlsx";
if (!fs.existsSync(inputPath))
{
    throw new Error("Source workbook not found. Path: " + inputPath);
}
// Load the existing workbook that contains the pivot table
var workbook = new AsposeCells.Workbook(inputPath);
// Access the worksheet that holds the pivot table (by index)
var worksheet = workbook.getWorksheets().get(0);
// Access the pivot table by index
var pivotTable = worksheet.getPivotTables().get(0);
// Retrieve the date PivotField from the row area
// (Date filter only works when the row/column area contains only date-time cells or blanks)
let dateField = pivotTable.getRowFields().get(0);
// Define the date criterion for the Between filter
let startDate = new Date(2020, 0, 1);
let endDate = new Date(2020, 11, 31);
// Apply the date filter on the pivot field
dateField.filterByDate(AsposeCells.PivotFilterType.DATE_BETWEEN, startDate, endDate);
// Refresh and recalculate the pivot table so the filter takes effect
pivotTable.getPivotCache().refresh();
// Persist the workbook
workbook.save(outputPath);
```

## **مرشح القيمة**
تعمل مرشحات القيم على القيم المجمعة التي يحسبها الجدول المحوري في منطقة البيانات الخاصة به. وبدلاً من مطابقة تسميات النص، فإنها تقارن الإجماليات الرقمية بحد معين. تتضمن حالات الاستخدام النموذجية عرض المنتجات التي يتجاوز مجموع مبيعاتها مبلغًا مستهدفًا فقط أو المناطق التي يقع عدد معاملاتها ضمن نطاق معين فقط.
يعرض Aspose.Cells تصفية القيم من خلال دالة `PivotField.filterByValue(PivotField valueField, PivotFilterType filterType, params object[] values)`. تستخدم وسيطة `filterType` قيمًا مثل `ValueGreaterThan` و `ValueLessThan` و `ValueBetween` و `ValueEqual` و `ValueNotEqual` و `ValueGreaterThanOrEqual` و `ValueLessThanOrEqual`. تحدد وسيطة `valueField` حقل البيانات الذي يجب تقييمه، وتوفر الوسيطة (الوسيطات) النهائية قيمة (قيم) الحد.
يقوم المثال التالي بتحميل مصنف يحتوي على جدول محوري، ويطبق مرشح قيمة يحتفظ فقط بالعناصر التي تتجاوز مبيعاتها المجمعة حدًا رقميًا، ثم يقوم بتحديث الجدول المحوري وحفظ المصنف.

```javascript
const AsposeCells = require("aspose.cells");
var workbook = new AsposeCells.Workbook("sample.xlsx");
var worksheet = workbook.getWorksheets().get(0);
var pivotTable = worksheet.getPivotTables().get(0);
var rowField = pivotTable.getRowFields().get(0);
var dataField = pivotTable.getDataFields().get(0);
// Find the data field index manually since PivotFieldCollection doesn't have IndexOf
var dataFieldIndex = -1;
for (var i = 0; i < pivotTable.getDataFields().getCount(); i++)
{
    if (pivotTable.getDataFields().get(i) == dataField)
    {
        dataFieldIndex = i;
        break;
    }
}
if (dataFieldIndex >= 0)
{
    rowField.filterByValue(dataFieldIndex, AsposeCells.PivotFilterType.VALUE_GREATER_THAN, 5000, Number.MAX_VALUE);
}
pivotTable.getPivotCache().refresh();
workbook.save("output.xlsx");
```

## **مرشح أعلى 10**
مرشح أعلى 10 هو شكل متخصص من مرشح القيمة يحتفظ فقط بأعلى أو أدنى عدد N من العناصر بناءً على حقل قيمة مختار. يُستخدم بشكل شائع لتقارير الترتيب مثل "أفضل 10 منتجات حسب الإيرادات" أو "أسفل 5 مناطق حسب عدد المبيعات".

{{% alert color="primary" %}}
لا يكون مرشح أعلى 10 فعالًا إلا عندما يحتوي الجدول المحوري على حقل قيمة محوري واحد أو أكثر في منطقة البيانات. بدون وجود حقل قيمة واحد على الأقل، لا يوجد مقياس مجمع لترتيب العناصر مقابله، ولا يمكن تطبيق المرشح.
تكشف Aspose.Cells عن تصفية أفضل 10 من خلال الطريقة `PivotField.filterTop10(valueFieldIndex, filterType, isTop, itemCount)`. المعلمة `valueFieldIndex` هي فهرس حقل البيانات الذي تُرتَّب العناصر حسب قيمه المجمعة، وتحدد `filterType` وحدة `itemCount` (`PivotFilterType.COUNT` تحتفظ بعدد ثابت من العناصر، و`PivotFilterType.PERCENT` تحتفظ بنسبة مئوية من العناصر بحيث تكون `itemCount` هي النسبة المئوية نفسها)، وتشير `isTop` إلى ما إذا كان سيتم الاحتفاظ بأعلى العناصر (true) أم أدناها (false)، وتحدد `itemCount` عدد العناصر أو النسبة المئوية المطلوب الاحتفاظ بها.
يقوم المثال التالي بتحميل مصنف يحتوي على جدول محوري يوجد به حقل قيمة، ويطبق مرشح أعلى 10 للاحتفاظ فقط بأعلى 10 عناصر من حيث مجموع المبيعات، ثم يقوم بتحديث الجدول المحوري وحفظ المصنف.
{{% /alert %}}

```javascript
const AsposeCells = require("aspose.cells");
let inputPath = "input.xlsx";
let outputPath = "output.xlsx";
let workbook = new AsposeCells.Workbook(inputPath);
// Access the worksheet that holds the pivot table (index 0)
let worksheet = workbook.getWorksheets().get(0);
// Access the pivot table by index
let pivotTable = worksheet.getPivotTables().get(0);
// Confirm there is at least one value PivotField in the data area
if (pivotTable.getDataFields().getCount() == 0)
{
    throw new Error("Pivot table has no value (data) PivotField.");
}
let valueField = pivotTable.getDataFields().get(0);
// Retrieve the target row PivotField (the field we want to apply Top 10 on)
let rowField = pivotTable.getRowFields().get(0);
// The first (and only) data field is at index 0; Top 10 ranks by it.
let valueFieldIndex = 0;
// Apply the Top 10 filter on the row field:
//   - itemCount   = 10
//   - filterType  = PivotFilterType.SUM
//   - isTop       = true (top N; false would mean bottom N)
//   - valueFieldIndex = the index of the data field used to rank items
rowField.filterTop10(valueFieldIndex, AsposeCells.PivotFilterType.COUNT, true, 10);
// Refresh the pivot table data and recalculate it so the filter takes effect
pivotTable.getPivotCache().refresh();
// Save the workbook
workbook.save(outputPath);
```

## **التصفية عن طريق إخفاء أو إظهار العناصر المحورية**
بالإضافة إلى واجهات برمجة APIs المنظمة للفلترة، يتيح لك Aspose.Cells التحكم في رؤية كل عنصر محوري فردي مباشرة. من خلال التكرار عبر مجموعة `PivotItems` الخاصة بـ `PivotField` وتبديل خاصية `IsHidden`، يمكنك قمع عناصر محددة بشكل انتقائي دون تطبيق مرشح قائم على الصيغة. يؤدي تعيين `IsHidden = true` إلى إخفاء العنصر من الجدول المحوري؛ بينما يؤدي تعيين `IsHidden = false` إلى إظهاره مرة أخرى وجعله مرئيًا.
يكون هذا الأسلوب مفيدًا عندما تكون قاعدة التصفية غير منتظمة أو خاصة بعنصر معين، مثل إخفاء عدد صغير من الفئات المسماة التي يجب ألا تظهر في تقرير معين. يقوم المثال أدناه بتحميل جدول محوري، وإخفاء عنصر محدد بالاسم، وعرض كيفية إظهاره مرة أخرى، ثم تحديث الجدول المحوري وحفظ المصنف.

```javascript
const AsposeCells = require("aspose.cells");
let workbook = new AsposeCells.Workbook("pivot_table_sample.xlsx");
// Access the first worksheet which contains the pivot table
let sheet = workbook.getWorksheets().get(0);
// Access the pivot table by index (the first pivot table on the sheet)
let pivotTable = sheet.getPivotTables().get(0);
// Retrieve the target PivotField (the first row label field that we'll hide/unhide items in)
let pivotField = pivotTable.getRowFields().get(0);
// Iterate through the PivotItems collection of the selected PivotField
let itemCount = pivotField.getPivotItems().getCount();
for (let i = 0; i < itemCount; i++) {
    let item = pivotField.getPivotItems().get(i);
    // Hide pivot items that match a specific name/criterion
    if (item.getName() == "Item1" || item.getName() == "Item2") {
        item.setHidden(true);
    }
    // Demonstrate unhiding: re-show a previously hidden pivot item
    if (item.getName() == "Item3") {
        item.setHidden(false);
    }
}
// Refresh and recalculate the pivot table so changes take effect
pivotTable.getPivotCache().refresh();
// Save the workbook — hidden items stay in the underlying data
// but are excluded from the displayed pivot table output
workbook.save("output_pivot_filtered.xlsx");
```

## **الملخص**
يوفر Aspose.Cells for Node.js via Java مجموعة كاملة من إمكانيات تصفية الجداول المحورية التي تطابق تلك الموجودة في Microsoft Excel. تغطي مرشحات التسميات والتاريخ والقيم معظم سيناريوهات التحليل الشائعة، بينما يتعامل مرشح أعلى 10 مع تقارير الترتيب. عندما تكون قاعدة التصفية غير منتظمة، توفر خاصية `PivotItem.IsHidden` بديلاً مرنًا على مستوى العناصر. يتيح لك الجمع بين هذه الاستراتيجيات — على سبيل المثال، تطبيق مرشح تسمية ثم إخفاء عناصر محددة — إنشاء تقارير جدول محوري مستهدفة بدقة بالكامل من خلال التعليمات البرمجية.

## المقالات ذات الصلة
- [إضافة حقول الصفوف والأعمدة للجدول المحوري في Aspose.Cells for Node.js via Java](/cells/ar/nodejs-java/pivot-table-add-row-and-column-fields/)
- [إضافة حقول التصفية إلى جدول محوري في Aspose.Cells for Node.js via Java](/cells/ar/nodejs-java/add-page-field-in-pivot-table/)
- [إدارة حقول قيم الجدول المحوري في Aspose.Cells for Node.js via Java](/cells/ar/nodejs-java/manage-value-fields/)
- [تحديث الجداول المحورية وذاكرة التخزين المؤقتة في Aspose.Cells for Node.js via Java](/cells/ar/nodejs-java/refresh-pivot-table/)

{{< app/cells/assistant language="nodejs-java" >}}