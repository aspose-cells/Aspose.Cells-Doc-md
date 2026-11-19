---
title: تصفية الجداول المحورية حسب التسمية أو القيمة
linktitle: تصفية الجداول المحورية حسب التسمية أو القيمة
description: يدعم Aspose.Cells for Node.js via C++ إمكانيات شاملة لتصفية الجداول المحورية. تشرح هذه المقالة كيفية تصفية بيانات الجدول المحوري باستخدام مرشحات التسميات ومرشحات التواريخ ومرشحات القيم ومرشحات أعلى 10 وعن طريق إخفاء أو إظهار عناصر الجدول المحوري.
keywords: Aspose.Cells, مكتبة Node.js عبر C++, جدول بيانات, جدول محوري, تصفية, مرشح التسمية, مرشح القيمة, مرشح التاريخ, مرشح أعلى 10, عنصر الجدول المحوري, إخفاء عنصر الجدول المحوري
type: docs
weight: 10
url: /ar/nodejs-cpp/filter-by-label-or-value-of-pivot-table/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
يوفر Aspose.Cells خمس استراتيجيات عملية لتصفية البيانات المعروضة في الجدول المحوري. يمكنك تطبيق مرشحات التسميات على حقول الصفوف أو الأعمدة المستندة إلى النص، واستخدام مرشحات التواريخ عندما يحتوي الحقل على خلايا تاريخ ووقت فقط أو خلايا فارغة، وتطبيق مرشحات القيم على الأرقام المجمعة، واستخدام مرشحات أعلى 10 للترتيب حسب حقل قيمة، أو إخفاء وإظهار عناصر الجدول المحوري يدويًا باستخدام خاصية `IsHidden`. تتعرض كل استراتيجية من خلال واجهات برمجية مخصصة في فئتي `PivotField` و `PivotItem`.
{{% /alert %}}

## **Introduction**
تُعد الجداول المحورية أدوات تحليلية قوية، ولكن الملخصات الأولية غالبًا ما تحتوي على معلومات أكثر بكثير مما تحتاج إلى عرضه. التصفية هي الآلية الأساسية لتضييق نطاق الجدول المحوري لتنحصر في الصفوف أو الأعمدة أو القيم المهمة لتقرير معين. يُطابق Aspose.Cells for Node.js via C++ إمكانيات التصفية المتوفرة في Microsoft Excel، ويعرضها برمجيًا بحيث يمكن أتمتة إنشاء التقارير بالكامل.
تُغطى استراتيجيات التصفية التالية في هذه المقالة:
1. **مرشح التسمية** — يُصفّي عناصر حقل الصف أو العمود بناءً على تسمياتها النصية.
2. **مرشح التاريخ** — يُصفّي حقول الصفوف أو الأعمدة التي تحتوي على قيم تاريخ ووقت فقط (أو خلايا فارغة).
3. **مرشح القيمة** — يُصفّي العناصر بناءً على القيم المجمعة لحقل بيانات.
4. **مرشح أعلى 10** — يعرض فقط أعلى أو أقل عدد N من العناصر مرتبة حسب حقل قيمة.
5. **إخفاء / إظهار عناصر الجدول المحوري** — يتحكم يدويًا في رؤية كل عنصر منفرد في الحقل.
تستخدم كل طريقة دالة مختلفة في فئة `PivotField` أو خاصية في فئة `PivotItem`. بعد تطبيق أي مرشح، يجب استدعاء `getPivotCache().refresh()` على الجدول المحوري بحيث تعكس البيانات المخزنة مؤقتًا والقيم المحسوبة حالة المرشح الجديدة.

## **Label Filter**
يتيح لك مرشح التسمية تصفية عناصر حقل الصف أو العمود بمقارنة تسمياتها النصية بنمط معين. يكون هذا مفيدًا عندما تريد عرض المنتجات التي تبدأ أسماؤها بحرف معين فقط، أو التي تحتوي على كلمة معينة، أو التي تطابق معيارًا آخر قائمًا على التسمية.
يعرض Aspose.Cells تصفية التسميات من خلال الدالة `PivotField.filterByLabel(PivotFilterType, string)`. يتضمن تعداد `PivotFilterType` قيمًا مثل `CaptionBeginsWith` و `CaptionContains` و `CaptionEndsWith` و `CaptionDoesNotContain` و `CaptionIsNotBlank` و `CaptionIsBlank` وما إلى ذلك. توفر الوسيطة الثانية سلسلة التسمية المستخدمة للمقارنة.
يُحمّل المثال التالي مصنفًا يحتوي على جدول محوري موجود، ويطبق مرشح تسمية بحيث تظل العناصر التي تبدأ تسمياتها ببادئة محددة مرئية فقط، ويُحدّث الجدول المحوري، ويحفظ النتيجة.

```javascript
const AsposeCells = require("aspose.cells.node");
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
rowField.filterByLabel(AsposeCells.PivotFilterType.CaptionBeginsWith, prefix, "");
// Refresh and recalculate the pivot table data so the filter takes effect
pivotTable.getPivotCache().refresh();
// Save the workbook back to disk
workbook.save(fileName);
```

## **Date Filter**
تتيح لك مرشحات التاريخ تضييق نطاق الجدول المحوري وفق معايير قائمة على التاريخ مثل اليوم أو الأسبوع الماضي أو هذا الشهر أو الربع القادم أو نطاق تاريخ محدد. وهي مرشحات متخصصة تعمل فقط مع الحقول التي تخزن معلومات التاريخ والوقت.

{{% alert color="primary" %}}
لا يعمل مرشح التاريخ إلا عندما تحتوي منطقة الصفوف أو الأعمدة على خلايا تاريخ ووقت فقط أو قيم فارغة. إذا كان الحقل الأساسي يحتوي على أنواع بيانات أخرى مثل الأرقام أو النصوص، فلن يُنتج مرشح التاريخ النتيجة المتوقعة. تأكد من تنسيق الحقل كتاريخ ومن أن جميع القيم هي نسخ `DateTime` صالحة أو خلايا فارغة قبل تطبيق هذا المرشح.
يعرض Aspose.Cells تصفية التواريخ من خلال الدالة `PivotField.filterByDate(PivotFilterType, params DateTime[] values)`. يحتوي تعداد `PivotFilterType` على قيم تواريخ مخصصة مثل `Today` و `Yesterday` و `LastWeek` و `ThisWeek` و `NextWeek` و `LastMonth` و `ThisMonth` و `NextMonth` و `LastQuarter` و `ThisQuarter` و `NextQuarter` و `LastYear` و `ThisYear` و `NextYear` و `Between`. بناءً على نوع المرشح المختار، تُمرر قيمة أو قيمتي `DateTime` (بالنسبة لـ `Between`، تُمرر تاريخي البداية والنهاية).
يُحمّل المثال التالي مصنفًا يحتوي على جدول محوري تشتمل منطقة صفوفه على حقل تاريخ، ويطبق مرشح تاريخ يقيد العناصر المرئية على نطاق تاريخ معين، ويُحدّث الجدول المحوري، ويحفظ المصنف.
{{% /alert %}}

```javascript
const AsposeCells = require("aspose.cells.node");
const fs = require("fs");
const inputPath = "sample.xlsx";
const outputPath = "output_filtered.xlsx";
if (!fs.existsSync(inputPath))
{
    throw new Error("Source workbook not found: " + inputPath);
}
// Load the existing workbook that contains the pivot table
const workbook = new AsposeCells.Workbook(inputPath);
// Access the worksheet that holds the pivot table (by index)
const worksheet = workbook.getWorksheets().get(0);
// Access the pivot table by index
const pivotTable = worksheet.getPivotTables().get(0);
// Retrieve the date PivotField from the row area
// (Date filter only works when the row/column area contains only date-time cells or blanks)
const dateField = pivotTable.getRowFields().get(0);
// Define the date criterion for the Between filter
const startDate = new Date(2020, 0, 1);
const endDate = new Date(2020, 11, 31);
// Apply the date filter on the pivot field
dateField.filterByDate(AsposeCells.PivotFilterType.DateBetween, startDate, endDate);
// Refresh and recalculate the pivot table so the filter takes effect
pivotTable.getPivotCache().refresh();
// Persist the workbook
workbook.save(outputPath);
```

## **Value Filter**
تعمل مرشحات القيم على القيم المجمعة التي يحسبها الجدول المحوري في منطقة البيانات الخاصة به. وبدلاً من مطابقة تسميات النص، تُقارن المجاميع العددية بحد معين. تتضمن حالات الاستخدام النموذجية عرض المنتجات التي يتجاوز مجموع مبيعاتها مبلغًا مستهدفًا فقط، أو المناطق التي يقع عدد معاملاتها ضمن نطاق معين فقط.
يعرض Aspose.Cells تصفية القيم من خلال الدالة `PivotField.filterByValue(PivotField valueField, PivotFilterType filterType, params object[] values)`. تستخدم وسيطة `filterType` قيمًا مثل `ValueGreaterThan` و `ValueLessThan` و `ValueBetween` و `ValueEqual` و `ValueNotEqual` و `ValueGreaterThanOrEqual` و `ValueLessThanOrEqual`. تُحدد وسيطة `valueField` حقل البيانات الذي يجب تقييمه، وتوفر الوسيطة (الوسائط) الأخيرة قيمة (قيم) الحد.
يُحمّل المثال التالي مصنفًا يحتوي على جدول محوري، ويطبق مرشح قيمة يحتفظ فقط بالعناصر التي تتجاوز مبيعاتها المجمعة حدًا عدديًا، ويُحدّث الجدول المحوري، ويحفظ المصنف.

```javascript
const AsposeCells = require("aspose.cells.node");
let dataFieldIndex = -1;
for (let i = 0; i < pivotTable.getDataFields().getCount(); i++) {
    if (pivotTable.getDataFields().get(i) === dataField) {
        dataFieldIndex = i;
        break;
    }
}
if (dataFieldIndex >= 0) {
    rowField.filterByValue(dataFieldIndex, AsposeCells.PivotFilterType.ValueGreaterThan, 5000, Number.MAX_VALUE);
}
pivotTable.getPivotCache().refresh();
workbook.save("output.xlsx");
```

## **Top 10 Filter**
مرشح أعلى 10 هو شكل متخصص من مرشح القيمة يحتفظ فقط بأعلى أو أقل عدد N من العناصر بناءً على حقل قيمة مختار. يُستخدم بشكل شائع لتقارير الترتيب مثل "أعلى 10 منتجات من حيث الإيرادات" أو "أقل 5 مناطق من حيث عدد المبيعات".

{{% alert color="primary" %}}
يكون مرشح أعلى 10 فعالًا فقط عندما يحتوي الجدول المحوري على حقل قيمة واحد أو أكثر في منطقة البيانات. فبدون وجود حقل قيمة واحد على الأقل، لن يكون هناك مقياس مجمع لترتيب العناصر وفقًا له، ولن يمكن تطبيق المرشح.
تكشف Aspose.Cells عن تصفية أفضل 10 من خلال الطريقة `PivotField.filterTop10(valueFieldIndex, filterType, isTop, itemCount)`. المعلمة `valueFieldIndex` هي فهرس حقل البيانات الذي تُرتَّب العناصر حسب قيمه المجمعة، وتحدد `filterType` وحدة `itemCount` (`PivotFilterType.Count` تحتفظ بعدد ثابت من العناصر، و`PivotFilterType.Percent` تحتفظ بنسبة مئوية من العناصر بحيث تكون `itemCount` هي النسبة المئوية نفسها)، وتشير `isTop` إلى ما إذا كان سيتم الاحتفاظ بأعلى العناصر (true) أم أدناها (false)، وتحدد `itemCount` عدد العناصر أو النسبة المئوية المطلوب الاحتفاظ بها.
يُحمّل المثال التالي مصنفًا يحتوي على جدول محوري يشتمل على حقل قيمة، ويطبق مرشح أعلى 10 للاحتفاظ فقط بأعلى 10 عناصر من حيث مجموع المبيعات، ويُحدّث الجدول المحوري، ويحفظ المصنف.
{{% /alert %}}

```javascript
const AsposeCells = require("aspose.cells.node");
// Load the existing workbook that contains the pivot table
const inputPath = "input.xlsx";
const outputPath = "output.xlsx";
const workbook = new AsposeCells.Workbook(inputPath);
// Access the worksheet that holds the pivot table (index 0)
const worksheet = workbook.getWorksheets().get(0);
// Access the pivot table by index
const pivotTable = worksheet.getPivotTables().get(0);
// Confirm there is at least one value PivotField in the data area
if (pivotTable.getDataFields().getCount() === 0) {
    throw new Error("Pivot table has no value (data) PivotField.");
}
const valueField = pivotTable.getDataFields().get(0);
// Retrieve the target row PivotField (the field we want to apply Top 10 on)
const rowField = pivotTable.getRowFields().get(0);
// The first (and only) data field is at index 0; Top 10 ranks by it.
const valueFieldIndex = 0;
// Apply the Top 10 filter on the row field:
//   - itemCount   = 10
//   - filterType  = PivotFilterType.Sum
//   - isTop       = true (top N; false would mean bottom N)
//   - valueFieldIndex = the index of the data field used to rank items
rowField.filterTop10(valueFieldIndex, AsposeCells.PivotFilterType.Count, true, 10);
// Refresh the pivot table data and recalculate it so the filter takes effect
pivotTable.getPivotCache().refresh();
// Save the workbook
workbook.save(outputPath);
```

## **Filter by Hiding or Unhiding Pivot Items**
بالإضافة إلى واجهات التصفية المنظمة، يتيح لك Aspose.Cells التحكم مباشرةً في رؤية كل عنصر منفرد من عناصر الجدول المحوري. من خلال التكرار عبر مجموعة `PivotItems` الخاصة بـ `PivotField` وتبديل خاصية `IsHidden`، يمكنك منع ظهور عناصر محددة بشكل انتقائي دون تطبيق مرشح قائم على الصيغة. يؤدي تعيين `IsHidden = true` إلى إخفاء العنصر من الجدول المحوري؛ بينما يؤدي تعيين `IsHidden = false` إلى إظهاره مجددًا وجعله مرئيًا مرة أخرى.
يكون هذا الأسلوب مفيدًا عندما تكون قاعدة التصفية غير منتظمة أو خاصة بعنصر معين، مثل إخفاء عدد صغير من الفئات المسماة التي يجب ألا تظهر في تقرير معين. يُحمّل المثال التالي جدولًا محوريًا، ويُخفي عنصرًا محددًا بالاسم، ويُوضح كيفية إظهاره مجددًا، ويُحدّث الجدول المحوري، ويحفظ المصنف.

```javascript
const AsposeCells = require("aspose.cells.node");
// Load an existing workbook containing a pivot table
const workbook = new AsposeCells.Workbook("pivot_table_sample.xlsx");
// Access the first worksheet which contains the pivot table
const sheet = workbook.getWorksheets().get(0);
// Access the pivot table by index (the first pivot table on the sheet)
const pivotTable = sheet.getPivotTables().get(0);
// Retrieve the target PivotField (the first row label field that we'll hide/unhide items in)
const pivotField = pivotTable.getRowFields().get(0);
// Iterate through the PivotItems collection of the selected PivotField
const itemCount = pivotField.getPivotItems().getCount();
for (let i = 0; i < itemCount; i++)
{
    const item = pivotField.getPivotItems().get(i);
    // Hide pivot items that match a specific name/criterion
    if (item.getName() == "Item1" || item.getName() == "Item2")
    {
        item.setIsHidden(true);
    }
    // Demonstrate unhiding: re-show a previously hidden pivot item
    if (item.getName() == "Item3")
    {
        item.setIsHidden(false);
    }
}
// Refresh and recalculate the pivot table so changes take effect
pivotTable.getPivotCache().refresh();
// Save the workbook — hidden items stay in the underlying data
// but are excluded from the displayed pivot table output
workbook.save("output_pivot_filtered.xlsx");
```

## **Summary**
يوفر Aspose.Cells for Node.js via C++ مجموعة كاملة من إمكانيات تصفية الجداول المحورية التي تُطابق تلك الموجودة في Microsoft Excel. تغطي مرشحات التسميات والتواريخ والقيم معظم السيناريوهات التحليلية الشائعة، بينما يتعامل مرشح أعلى 10 مع تقارير الترتيب. عندما تكون قاعدة التصفية غير منتظمة، توفر خاصية `PivotItem.IsHidden` بديلاً مرنًا على مستوى العنصر. يتيح لك الجمع بين هذه الاستراتيجيات — على سبيل المثال، تطبيق مرشح تسمية ثم إخفاء عناصر محددة — إنشاء تقارير جدول محوري مستهدفة بدقة بالكامل من خلال الكود.

## Related Articles
- [إدراج جدول محوري](/cells/ar/nodejs-cpp/create-pivot-table/)
- [إضافة حقول الصف والأعمدة إلى جدول محوري في Aspose.Cells for Node.js via C++](/cells/ar/nodejs-cpp/pivot-table-add-row-and-column-fields/)
- [إضافة حقول التصفية إلى جدول محوري في Aspose.Cells for Node.js via C++](/cells/ar/nodejs-cpp/add-page-field-in-pivot-table/)
- [إدارة حقول قيم الجدول المحوري في Aspose.Cells for Node.js via C++](/cells/ar/nodejs-cpp/manage-value-fields/)
- [تحديث الجداول المحورية وذاكرات التخزين المؤقت في Aspose.Cells for Node.js via C++](/cells/ar/nodejs-cpp/refresh-pivot-table/)

{{< app/cells/assistant language="nodejs-cpp" >}}