---
title: تصفية الجداول المحورية حسب التسمية أو القيمة
linktitle: تصفية الجداول المحورية حسب التسمية أو القيمة
description: Aspose.Cells for .NET تدعم إمكانيات شاملة لتصفية الجداول المحورية. توضح هذه المقالة كيفية تصفية بيانات الجدول المحوري باستخدام مرشحات التسميات، ومرشحات التاريخ، ومرشحات القيم، ومرشحات أعلى 10، ومن خلال إخفاء أو إظهار عناصر الجدول المحوري.
keywords: Aspose.Cells, .NET, جدول بيانات, جدول محوري, تصفية, مرشح التسمية, مرشح القيمة, مرشح التاريخ, مرشح أعلى 10, عنصر محوري, إخفاء عنصر محوري
type: docs
weight: 10
url: /ar/net/filter-by-label-or-value-of-pivot-table/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---
{{% alert color="primary" %}}
توفر Aspose.Cells خمس استراتيجيات عملية لتصفية البيانات المعروضة في الجدول المحوري. يمكنك تطبيق مرشحات التسميات على حقول الصفوف أو الأعمدة المستندة إلى النص، واستخدام مرشحات التاريخ عندما يحتوي الحقل على خلايا تاريخ ووقت فقط أو خلايا فارغة، وتطبيق مرشحات القيم مقابل الأرقام المجمعة، واستخدام مرشحات أعلى 10 للترتيب حسب حقل قيمة، أو إخفاء وإظهار عناصر الجدول المحوري الفردية يدويًا باستخدام خاصية `IsHidden`. يتم عرض كل استراتيجية من خلال واجهات برمجة التطبيقات المخصصة في فئتي `PivotField` و`PivotItem`.
{{% /alert %}}
## **المقدمة**
تُعد الجداول المحورية أدوات تحليلية قوية، ولكن الملخصات الخام غالبًا ما تحتوي على معلومات أكثر بكثير مما تحتاج إلى عرضه. التصفية هي الآلية الأساسية لتضييق نطاق الجدول المحوري إلى الصفوف أو الأعمدة أو القيم المهمة لتقرير معين. Aspose.Cells for .NET تعكس إمكانيات التصفية المتوفرة في Microsoft Excel، وتعرضها برمجيًا بحيث يمكن أتمتة إنشاء التقارير بالكامل.
يتم تغطية استراتيجيات التصفية التالية في هذه المقالة:
1. **مرشح التسمية** — يصفي عناصر حقل الصف أو العمود بناءً على تسمياتها النصية.
2. **مرشح التاريخ** — يصفي حقول الصفوف أو الأعمدة التي تحتوي فقط على قيم تاريخ ووقت (أو خلايا فارغة).
3. **مرشح القيمة** — يصفي العناصر بناءً على القيم المجمعة لحقل البيانات.
4. **مرشح أعلى 10** — يعرض فقط أعلى أو أدنى عدد N من العناصر مرتبة حسب حقل قيمة.
5. **إخفاء / إظهار عناصر الجدول المحوري** — يتحكم يدويًا في رؤية كل عنصر فردي في حقل.
تستخدم كل طريقة أسلوبًا مختلفًا في فئة `PivotField` أو خاصية في فئة `PivotItem`. بعد تطبيق أي مرشح، يجب عليك استدعاء `PivotCache.Refresh()` على الجدول المحوري بحيث تعكس البيانات المخزنة مؤقتًا والقيم المحسوبة حالة المرشح الجديدة.
## **مرشح التسمية**
يتيح لك مرشح التسمية تصفية عناصر حقل الصف أو العمود بمقارنة تسمياتها النصية بنمط معين. يكون هذا مفيدًا عندما تريد عرض المنتجات التي تبدأ أسماؤها بحرف معين فقط، أو تحتوي على كلمة معينة، أو تطابق معيارًا آخر قائمًا على التسمية.
تعرض Aspose.Cells تصفية التسميات من خلال أسلوب `PivotField.FilterByLabel(PivotFilterType filterType, string label1, string label2)`. تحدد الوسيطة `filterType` وضع المقارنة، مثل `CaptionBeginsWith` و`CaptionContains` و`CaptionEndsWith` و`CaptionDoesNotContain` و`CaptionIsNotBlank` و`CaptionIsBlank`. توفر الوسيطتان `label1` و`label2` نص المقارنة؛ مرّر `string.Empty` إلى `label2` عندما تحتاج إلى مطابقة قيمة واحدة فقط، مثل "يبدأ بـ" أو "يحتوي على".
يحمل المثال التالي مصنفًا يحتوي على جدول محوري موجود، ويطبق مرشح تسمية بحيث تبقى العناصر التي تبدأ تسمياتها ببادئة محددة مرئية فقط، ويُحدّث الجدول المحوري، ويحفظ النتيجة.
```csharp
using System;
using System.IO;
using Aspose.Cells;
using Aspose.Cells.Pivot;

string fileName = "sample.xlsx";
string prefix = "B";

// تحميل المصنف الحالي الذي يحتوي على جدول محوري
Workbook workbook = new Workbook(fileName);

// الوصول إلى ورقة العمل حسب الفهرس (ورقة العمل الأولى)
Worksheet worksheet = workbook.Worksheets[0];

// الوصول إلى الجدول المحوري حسب الفهرس
PivotTable pivotTable = worksheet.PivotTables[0];

// استرجاع حقل الصف الأول PivotField
PivotField rowField = pivotTable.RowFields[0];

// تطبيق مرشح التسمية — إظهار عناصر الصفوف التي تبدأ تسميتها بالبادئة المقدمة فقط
rowField.FilterByLabel(PivotFilterType.CaptionBeginsWith, prefix, string.Empty);

// تحديث وإعادة حساب بيانات الجدول المحوري لتطبيق المرشح
pivotTable.PivotCache.Refresh();

// حفظ المصنف على القرص
workbook.Save(fileName);
```
## **مرشح التاريخ**
تتيح لك مرشحات التاريخ تضييق نطاق الجدول المحوري حسب معايير قائمة على التاريخ مثل اليوم، أو الأسبوع الماضي، أو هذا الشهر، أو الربع القادم، أو نطاق تاريخ محدد. هذه مرشحات متخصصة تعمل فقط مع الحقول التي تخزن معلومات التاريخ والوقت.
{{% alert color="primary" %}}
لا يعمل مرشح التاريخ إلا عندما تحتوي منطقة الصف أو العمود على خلايا تاريخ ووقت فقط أو قيم فارغة. إذا كان الحقل الأساسي يحتوي على أنواع بيانات أخرى مثل الأرقام أو النصوص، فلن ينتج مرشح التاريخ النتيجة المتوقعة. تأكد من تنسيق الحقل كتاريخ وأن جميع القيم هي نسخ صالحة من `DateTime` أو خلايا فارغة قبل تطبيق هذا المرشح.
{{% /alert %}}
تعرض Aspose.Cells تصفية التاريخ من خلال أسلوب `PivotField.FilterByDate(PivotFilterType, params DateTime[] values)`. يحتوي تعداد `PivotFilterType` على قيم تاريخ مخصصة مثل `Today` و`Yesterday` و`LastWeek` و`ThisWeek` و`NextWeek` و`LastMonth` و`ThisMonth` و`NextMonth` و`LastQuarter` و`ThisQuarter` و`NextQuarter` و`LastYear` و`ThisYear` و`NextYear` و`Between`. اعتمادًا على نوع المرشح المختار، تمرر قيمة أو قيمتين من `DateTime` (بالنسبة لـ `Between`، تمرر تاريخ البدء والانتهاء).
يحمل المثال التالي مصنفًا يحتوي على جدول محوري توجد به منطقة صفوف تحتوي على حقل تاريخ، ويطبق مرشح تاريخ يقصر العناصر المرئية على نطاق تاريخ معين، ويُحدّث الجدول المحوري، ويحفظ المصنف.
```csharp
using System;
using System.IO;
using Aspose.Cells;
using Aspose.Cells.Pivot;

string inputPath = "sample.xlsx";
string outputPath = "output_filtered.xlsx";

if (!File.Exists(inputPath))
{
    throw new FileNotFoundException("Source workbook not found.", inputPath);
}

// تحميل مصنف العمل الموجود الذي يحتوي على الجدول المحوري
var workbook = new Workbook(inputPath);

// الوصول إلى ورقة العمل التي تحتوي على الجدول المحوري (بالفهرس)
var worksheet = workbook.Worksheets[0];

// الوصول إلى الجدول المحوري بالفهرس
var pivotTable = worksheet.PivotTables[0];

// استرجاع حقل المحور التاريخي من منطقة الصفوف
// (يعمل مرشح التاريخ فقط عندما تحتوي منطقة الصف/العمود على خلايا تاريخ ووقت فقط أو خلايا فارغة)
PivotField dateField = pivotTable.RowFields[0];

// تحديد معيار التاريخ لمرشح Between
DateTime startDate = new DateTime(2020, 1, 1);
DateTime endDate = new DateTime(2020, 12, 31);

// تطبيق مرشح التاريخ على حقل المحور
dateField.FilterByDate(PivotFilterType.DateBetween, startDate, endDate);

// تحديث وإعادة حساب الجدول المحوري حتى يصبح المرشح ساري المفعول
pivotTable.PivotCache.Refresh();

// حفظ مصنف العمل
workbook.Save(outputPath);
```
## **مرشح القيمة**
تعمل مرشحات القيمة على القيم المجمعة التي يحسبها الجدول المحوري في منطقة البيانات الخاصة به. بدلاً من مطابقة تسميات النص، فإنها تقارن الإجماليات الرقمية بحد معين. تشمل حالات الاستخدام النموذجية عرض المنتجات التي يتجاوز مجموع مبيعاتها مبلغًا مستهدفًا فقط، أو المناطق التي يقع عدد معاملاتها ضمن نطاق معين فقط.
تعرض Aspose.Cells تصفية القيم من خلال أسلوب `PivotField.FilterByValue(int valueFieldIndex, PivotFilterType filterType, double value1, double value2)`. يحدد المعامل `valueFieldIndex` فهرس حقل البيانات الذي يجب تقييمه؛ يمكنك تحديد موضعه باستخدام `pivotTable.DataFields.IndexOf(dataField)` أو بالتكرار عبر المجموعة. يستخدم المعامل `filterType` قيمًا مثل `ValueGreaterThan` و`ValueLessThan` و`ValueBetween` و`ValueEqual` و`ValueNotEqual` و`ValueGreaterThanOrEqual` و`ValueLessThanOrEqual`. توفر وسيطتا `double` قيمة الحد أو قيمتيه.
يحمل المثال التالي مصنفًا يحتوي على جدول محوري، ويطبق مرشح قيمة يحتفظ فقط بالعناصر التي تتجاوز مبيعاتها المجمعة حدًا رقميًا، ويُحدّث الجدول المحوري، ويحفظ المصنف.
```csharp
using Aspose.Cells;
using Aspose.Cells.Pivot;

var workbook = new Workbook("sample.xlsx");
var worksheet = workbook.Worksheets[0];
var pivotTable = worksheet.PivotTables[0];

var rowField = pivotTable.RowFields[0];
var dataField = pivotTable.DataFields[0];

// البحث عن فهرس حقل البيانات يدويًا نظرًا لأن PivotFieldCollection لا يحتوي على IndexOf
int dataFieldIndex = -1;
for (int i = 0; i < pivotTable.DataFields.Count; i++)
{
    if (pivotTable.DataFields[i] == dataField)
    {
        dataFieldIndex = i;
        break;
    }
}

if (dataFieldIndex >= 0)
{
    rowField.FilterByValue(dataFieldIndex, PivotFilterType.ValueGreaterThan, 5000, double.MaxValue);
}

pivotTable.PivotCache.Refresh();

workbook.Save("output.xlsx");
```
## **مرشح أعلى 10**
مرشح أعلى 10 هو شكل متخصص من مرشح القيمة يحتفظ فقط بأعلى أو أدنى عدد N من العناصر بناءً على حقل قيمة مختار. يُستخدم بشكل شائع لتقارير الترتيب مثل "أفضل 10 منتجات حسب الإيرادات" أو "أسوأ 5 مناطق حسب عدد المبيعات".
{{% alert color="primary" %}}
يكون مرشح أعلى 10 فعالًا فقط عندما يحتوي الجدول المحوري على حقل قيمة واحد أو أكثر في منطقة البيانات. بدون حقل قيمة واحد على الأقل، لا يوجد مقياس مجمع لترتيب العناصر مقابله، ولا يمكن تطبيق المرشح.
{{% /alert %}}
تعرض Aspose.Cells تصفية أعلى 10 من خلال أسلوب `PivotField.FilterTop10(int itemCount, PivotFilterType filterType, bool isTop, int valueFieldIndex)`. يحدد المعامل `itemCount` عدد العناصر التي يجب الاحتفاظ بها، ويتحكم `filterType` في كيفية حساب القيمة، عادةً باستخدام `Sum` وكذلك `Count` أو `Percent`. يحدد `isTop` ما إذا كان يجب الاحتفاظ بأعلى العناصر (`true`) أو أدناها (`false`)، ويمثل `valueFieldIndex` فهرس حقل البيانات المستخدم لترتيب العناصر.
يحمل المثال التالي مصنفًا يحتوي على جدول محوري يحتوي على حقل قيمة، ويطبق مرشح أعلى 10 للاحتفاظ فقط بأعلى 10 عناصر حسب مجموع المبيعات، ويُحدّث الجدول المحوري، ويحفظ المصنف.
```csharp
using System;
using System.IO;
using Aspose.Cells;
using Aspose.Cells.Pivot;

// تحميل المصنف الموجود الذي يحتوي على الجدول المحوري
string inputPath = "input.xlsx";
string outputPath = "output.xlsx";
Workbook workbook = new Workbook(inputPath);

// الوصول إلى ورقة العمل التي تحتوي على الجدول المحوري (الفهرس 0)
Worksheet worksheet = workbook.Worksheets[0];

// الوصول إلى الجدول المحوري حسب الفهرس
PivotTable pivotTable = worksheet.PivotTables[0];

// التأكد من وجود حقل قيمة واحد على الأقل في منطقة البيانات
if (pivotTable.DataFields.Count == 0)
{
    throw new InvalidOperationException("Pivot table has no value (data) PivotField.");
}
PivotField valueField = pivotTable.DataFields[0];

// استرجاع حقل الصف المستهدف لتطبيق مرشح أعلى 10 عليه
PivotField rowField = pivotTable.RowFields[0];

// يقع حقل البيانات الأول والوحيد عند الفهرس 0، ويُستخدم للترتيب
int valueFieldIndex = 0;

// تطبيق مرشح أعلى 10 على حقل الصف:
//   - itemCount = 10
//   - filterType = PivotFilterType.Sum
//   - isTop = true لأعلى N، أو false لأدنى N
//   - valueFieldIndex = فهرس حقل البيانات المستخدم لترتيب العناصر
rowField.FilterTop10(10, PivotFilterType.Sum, true, valueFieldIndex);

// تحديث بيانات الجدول المحوري وإعادة حسابها لتطبيق المرشح
pivotTable.PivotCache.Refresh();

// حفظ المصنف
workbook.Save(outputPath);
```
## **التصفية عن طريق إخفاء أو إظهار عناصر الجدول المحوري**
بالإضافة إلى واجهات برمجة تطبيقات التصفية المنظمة، تتيح لك Aspose.Cells التحكم في رؤية كل عنصر فردي من عناصر الجدول المحوري مباشرةً. من خلال التكرار عبر مجموعة `PivotItems` الخاصة بـ `PivotField` وتبديل خاصية `IsHidden`، يمكنك قمع عناصر محددة بشكل انتقائي دون تطبيق مرشح قائم على الصيغة. يؤدي تعيين `IsHidden = true` إلى إخفاء العنصر من الجدول المحوري؛ ويؤدي تعيين `IsHidden = false` إلى إظهاره وجعله مرئيًا مرة أخرى.
يكون هذا الأسلوب مفيدًا عندما تكون قاعدة التصفية غير منتظمة أو خاصة بعنصر معين، مثل إخفاء عدد صغير من الفئات المسماة التي يجب ألا تظهر في تقرير معين. يحمل المثال التالي جدولًا محوريًا، ويخفي عنصرًا محددًا بالاسم، ويوضح كيفية إظهاره مرة أخرى، ويُحدّث الجدول المحوري، ويحفظ المصنف.
```csharp
using System;
using System.IO;
using Aspose.Cells;
using Aspose.Cells.Pivot;

// تحميل مصنف موجود يحتوي على جدول محوري
Workbook workbook = new Workbook("pivot_table_sample.xlsx");

// الوصول إلى ورقة العمل الأولى التي تحتوي على الجدول المحوري
Worksheet sheet = workbook.Worksheets[0];

// الوصول إلى الجدول المحوري حسب الفهرس (الجدول المحوري الأول في الورقة)
PivotTable pivotTable = sheet.PivotTables[0];

// استرجاع حقل المحور المستهدف (أول حقل تسمية صف سنقوم بإخفاء/إظهار عناصره)
PivotField pivotField = pivotTable.RowFields[0];

// التكرار عبر مجموعة PivotItems الخاصة بحقل المحور المحدد
int itemCount = pivotField.PivotItems.Count;
for (int i = 0; i < itemCount; i++)
{
    PivotItem item = pivotField.PivotItems[i];

    // إخفاء عناصر المحور التي تطابق اسمًا/معيارًا محددًا
    if (item.Name == "Item1" || item.Name == "Item2")
    {
        item.IsHidden = true;
    }

    // عرض توضيح لإظهار عنصر محوري تم إخفاؤه سابقًا
    if (item.Name == "Item3")
    {
        item.IsHidden = false;
    }
}

// تحديث الجدول المحوري وإعادة حسابه لتصبح التغييرات سارية المفعول
pivotTable.PivotCache.Refresh();

// حفظ المصنف — تظل العناصر المخفية في البيانات الأساسية
// ولكن يتم استبعادها من ناتج الجدول المحوري المعروض
workbook.Save("output_pivot_filtered.xlsx");
```
## **الملخص**
توفر Aspose.Cells for .NET مجموعة كاملة من إمكانيات تصفية الجداول المحورية التي تتطابق مع تلك الموجودة في Microsoft Excel. تغطي مرشحات التسميات والتاريخ والقيم معظم السيناريوهات التحليلية الشائعة، بينما يتعامل مرشح أعلى 10 مع تقارير الترتيب. عندما تكون قاعدة التصفية غير منتظمة، توفر خاصية `PivotItem.IsHidden` بديلاً مرنًا على مستوى العنصر. يتيح لك الجمع بين هذه الاستراتيجيات — على سبيل المثال، تطبيق مرشح تسمية ثم إخفاء عناصر معينة — إنشاء تقارير جدول محوري مستهدفة بدقة بالكامل من التعليمات البرمجية.
{{< app/cells/assistant language="csharp" >}}