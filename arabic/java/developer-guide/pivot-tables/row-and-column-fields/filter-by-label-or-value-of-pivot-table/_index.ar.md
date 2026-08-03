---
title: تصفية الجداول المحورية حسب التسمية أو القيمة
linktitle: تصفية الجداول المحورية حسب التسمية أو القيمة
description: يدعم Aspose.Cells for Java إمكانيات تصفية شاملة للجداول المحورية. تشرح هذه المقالة كيفية تصفية بيانات الجدول المحوري باستخدام مرشحات التسميات، ومرشحات التاريخ، ومرشحات القيم، ومرشحات أعلى 10، وعن طريق إخفاء أو إظهار عناصر الجدول المحوري.
keywords: Aspose.Cells, Java library, spreadsheet, pivot table, filter, label filter, value filter, date filter, top 10 filter, pivot item, hide pivot item
type: docs
weight: 10
url: /ar/java/filter-by-label-or-value-of-pivot-table/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---
{{% alert color="primary" %}}
يوفر Aspose.Cells خمس استراتيجيات عملية لتصفية البيانات المعروضة في الجدول المحوري. يمكنك تطبيق مرشحات التسميات على حقول الصفوف أو الأعمدة النصية، واستخدام مرشحات التاريخ عندما يحتوي الحقل على خلايا تاريخ ووقت فقط أو خلايا فارغة، وتطبيق مرشحات القيم مقابل الأرقام المجمعة، واستخدام مرشحات أعلى 10 للترتيب حسب حقل قيمة، أو إخفاء وإظهار عناصر الجدول المحوري يدويًا باستخدام خاصية `IsHidden`. يتم عرض كل استراتيجية من خلال واجهات برمجة تطبيقات مخصصة على فئتي `PivotField` و `PivotItem`.
{{% /alert %}}
## **المقدمة**
تعد الجداول المحورية أدوات تحليلية قوية، ولكن الملخصات الخام غالبًا ما تحتوي على معلومات أكثر بكثير مما تحتاج إلى عرضه. التصفية هي الآلية الأساسية لتضييق نطاق الجدول المحوري على الصفوف أو الأعمدة أو القيم التي تهم تقريرًا محددًا. يعكس Aspose.Cells for Java إمكانيات التصفية المتوفرة في Microsoft Excel، ويعرضها برمجيًا بحيث يمكن أتمتة إنشاء التقارير بالكامل.
تتناول هذه المقالة استراتيجيات التصفية التالية:
1. **مرشح التسمية** — يصفّي عناصر حقل الصف أو العمود بناءً على تسمياتها النصية.
2. **مرشح التاريخ** — يصفّي حقول الصفوف أو الأعمدة التي تحتوي على قيم تاريخ ووقت فقط (أو خلايا فارغة).
3. **مرشح القيمة** — يصفّي العناصر بناءً على القيم المجمعة لحقل بيانات.
4. **مرشح أعلى 10** — يعرض فقط أعلى أو أقل عدد N من العناصر مرتبة حسب حقل القيمة.
5. **إخفاء / إظهار عناصر الجدول المحوري** — يتحكم يدويًا في رؤية كل عنصر فردي في حقل.
تستخدم كل طريقة أسلوبًا مختلفًا على فئة `PivotField` أو خاصية على فئة `PivotItem`. بعد تطبيق أي مرشح، يجب استدعاء `refreshData()` و `calculateData()` على الجدول المحوري بحيث تعكس البيانات المخزنة مؤقتًا والقيم المحسوبة حالة المرشح الجديدة.
## **مرشح التسمية**
يسمح لك مرشح التسمية بتصفية عناصر حقل الصف أو العمود بمقارنة تسمياتها النصية بنمط معين. يكون هذا مفيدًا عندما تريد عرض المنتجات التي تبدأ أسماؤها بحرف معين فقط، أو تحتوي على كلمة معينة، أو تطابق معيارًا آخر قائمًا على التسمية.
يعرض Aspose.Cells تصفية التسميات من خلال طريقة `PivotField.filterByLabel(PivotFilterType, String)`. يتضمن تعداد `PivotFilterType` قيمًا مثل `CaptionBeginsWith` و `CaptionContains` و `CaptionEndsWith` و `CaptionDoesNotContain` و `CaptionIsNotBlank` و `CaptionIsBlank` وما إلى ذلك. توفر الوسيطة الثانية سلسلة التسمية المستخدمة للمقارنة.
يحمّل المثال التالي مصنفًا يحتوي على جدول محوري موجود، ويطبق مرشح تسمية بحيث تظل العناصر التي تبدأ تسمياتها ببادئة محددة مرئية فقط، ويحدّث الجدول المحوري، ويحفظ النتيجة.
```java
import com.aspose.cells.*;

String fileName = "sample.xlsx";
String prefix = "B";

// تحميل مصنف العمل الموجود الذي يحتوي على جدول محوري
Workbook workbook = new Workbook(fileName);

// الوصول إلى ورقة العمل حسب الفهرس (ورقة العمل الأولى)
Worksheet worksheet = workbook.getWorksheets().get(0);

// الوصول إلى الجدول المحوري حسب الفهرس
PivotTable pivotTable = worksheet.getPivotTables().get(0);

// Retrieve the first row PivotField
PivotField rowField = pivotTable.getRowFields().get(0);

// Apply the label filter - show only row items whose labels begin with the supplied prefix
rowField.filterByLabel(PivotFilterType.CAPTION_BEGINS_WITH, prefix, "");

// Refresh and recalculate the pivot table data so the filter takes effect
pivotTable.refreshData();

// Save the workbook back to disk
workbook.save(fileName);
```
## **مرشح التاريخ**
تتيح لك مرشحات التاريخ تضييق نطاق الجدول المحوري وفقًا لمعايير قائمة على التاريخ مثل اليوم، أو الأسبوع الماضي، أو هذا الشهر، أو الربع القادم، أو نطاق تاريخ محدد. هذه مرشحات متخصصة تعمل فقط ضد الحقول التي تخزن معلومات التاريخ والوقت.
{{% alert color="primary" %}}
لا يعمل مرشح التاريخ إلا عندما تحتوي منطقة الصف أو العمود على خلايا تاريخ ووقت فقط أو قيم فارغة. إذا كان الحقل الأساسي يحتوي على أنواع بيانات أخرى مثل الأرقام أو النصوص، فلن ينتج مرشح التاريخ النتيجة المتوقعة. تأكد من تنسيق الحقل كتاريخ وأن جميع القيم هي نسخ `DateTime` صالحة أو خلايا فارغة قبل تطبيق هذا المرشح.
{{% /alert %}}
يعرض Aspose.Cells تصفية التاريخ من خلال طريقة `PivotField.filterByDate(PivotFilterType, params DateTime[] values)`. يحتوي تعداد `PivotFilterType` على قيم تاريخ مخصصة مثل `Today` و `Yesterday` و `LastWeek` و `ThisWeek` و `NextWeek` و `LastMonth` و `ThisMonth` و `NextMonth` و `LastQuarter` و `ThisQuarter` و `NextQuarter` و `LastYear` و `ThisYear` و `NextYear` و `Between`. بناءً على نوع المرشح المختار، يمكنك تمرير قيمة `DateTime` واحدة أو قيمتين (بالنسبة لـ `Between`، تمرر تاريخي البداية والنهاية).
يحمّل المثال التالي مصنفًا يحتوي على جدول محوري توجد في منطقة الصفوف فيه حقل تاريخ، ويطبق مرشح تاريخ يقصر العناصر المرئية على نطاق تاريخ معين، ويحدّث الجدول المحوري، ويحفظ المصنف.
```java
;
import java.io.FileNotFoundException;

String inputPath = "sample.xlsx";
String outputPath = "output_filtered.xlsx";

if (!new File(inputPath).exists())
{
    throw new FileNotFoundException("Source workbook not found: " + inputPath);
}

// قم بتحميل مصنف العمل الموجود الذي يحتوي على الجدول المحوري
Workbook workbook = new Workbook(inputPath);

// الوصول إلى ورقة العمل التي تحتوي على الجدول المحوري (بالفهرس)
Worksheet worksheet = workbook.getWorksheets().get(0);

// الوصول إلى الجدول المحوري بواسطة الفهرس
PivotTable pivotTable = worksheet.getPivotTables().get(0);

// استرجاع حقل المحور التاريخي من منطقة الصفوف
// (يعمل مرشح التاريخ فقط عندما تحتوي منطقة الصف/العمود على خلايا تاريخ-وقت أو خانات فارغة فقط)
PivotField dateField = pivotTable.getRowFields().get(0);

// تحديد معيار التاريخ لمرشح Between
DateTime startDate = new DateTime(2020, 1, 1);
DateTime endDate = new DateTime(2020, 12, 31);

// تطبيق مرشح التاريخ على حقل المحور
dateField.filterByDate(PivotFilterType.DATE_BETWEEN, startDate, endDate);

// قم بتحديث وإعادة حساب الجدول المحوري حتى يصبح المرشح ساري المفعول
pivotTable.refreshData();

// حفظ مصنف العمل
workbook.save(outputPath);
```
## **مرشح القيمة**
تعمل مرشحات القيمة على القيم المجمعة التي يحسبها الجدول المحوري في منطقة البيانات. بدلاً من مطابقة تسميات النص، فإنها تقارن الإجماليات الرقمية بحد معين. تتضمن حالات الاستخدام النموذجية عرض المنتجات فقط التي يتجاوز مجموع مبيعاتها مبلغًا مستهدفًا، أو المناطق فقط التي يقع عدد معاملاتها ضمن نطاق معين.
يعرض Aspose.Cells تصفية القيم من خلال طريقة `PivotField.filterByValue(PivotField valueField, PivotFilterType filterType, params Object[] values)`. تستخدم معامل `filterType` قيمًا مثل `ValueGreaterThan` و `ValueLessThan` و `ValueBetween` و `ValueEqual` و `ValueNotEqual` و `ValueGreaterThanOrEqual` و `ValueLessThanOrEqual`. يحدد معامل `valueField` أي حقل بيانات يجب تقييمه، وتوفر الوسيطة (الوسائط) النهائية قيمة (قيم) العتبة.
يحمّل المثال التالي مصنفًا يحتوي على جدول محوري، ويطبق مرشح قيمة يحتفظ فقط بالعناصر التي تتجاوز مبيعاتها المجمعة عتبة رقمية، ويحدّث الجدول المحوري، ويحفظ المصنف.
```java
ells.*;

Workbook workbook = new Workbook("sample.xlsx");
Worksheet worksheet = workbook.getWorksheets().get(0);
PivotTable pivotTable = worksheet.getPivotTables().get(0);

PivotField rowField = pivotTable.getRowFields().get(0);
PivotField dataField = pivotTable.getDataFields().get(0);

// ابحث عن فهرس حقل البيانات يدويًا نظرًا لأن PivotFieldCollection لا يحتوي على IndexOf
int dataFieldIndex = -1;
for (int i = 0; i < pivotTable.getDataFields().getCount(); i++)
{
    if (pivotTable.getDataFields().get(i) == dataField)
    {
        dataFieldIndex = i;
        break;
    }
}

if (dataFieldIndex >= 0)
{
    rowField.filterByValue(dataFieldIndex, PivotFilterType.VALUE_GREATER_THAN, 5000, Double.MAX_VALUE);
}

pivotTable.refreshData();

workbook.save("output.xlsx");
```
## **مرشح أعلى 10**
مرشح أعلى 10 هو شكل متخصص من مرشح القيمة الذي يحتفظ فقط بأعلى أو أقل عدد N من العناصر بناءً على حقل قيمة مختار. يُستخدم بشكل شائع لتقارير الترتيب مثل "أفضل 10 منتجات حسب الإيرادات" أو "أقل 5 مناطق حسب عدد المبيعات".
{{% alert color="primary" %}}
يكون مرشح أعلى 10 فعالًا فقط عندما يحتوي الجدول المحوري على حقل قيمة محوري واحد أو أكثر في منطقة البيانات. بدون حقل قيمة واحد على الأقل، لا يوجد مقياس مجمع لترتيب العناصر مقابله، ولا يمكن تطبيق المرشح.
{{% /alert %}}
يعرض Aspose.Cells تصفية أعلى 10 من خلال طريقة `PivotField.filterTop10(int itemCount, boolean isTop, PivotField valueField, PivotFilterType filterType)`. يحدد معامل `itemCount` عدد العناصر التي يجب الاحتفاظ بها، ويشير `isTop` إلى ما إذا كان سيتم الاحتفاظ بأعلى العناصر (صحيح) أو أقل العناصر (خطأ)، ويشير `valueField` إلى حقل البيانات المستخدم للترتيب، ويتحكم `filterType` في كيفية حساب القيمة (عادةً `Sum`، ولكن أيضًا `Count` و `Percent`).
يحمّل المثال التالي مصنفًا يحتوي على جدول محوري يحتوي على حقل قيمة، ويطبق مرشح أعلى 10 للاحتفاظ فقط بأعلى 10 عناصر حسب مجموع المبيعات، ويحدّث الجدول المحوري، ويحفظ المصنف.
```java
import com.aspose.cells.*;

// تحميل المصنف الحالي الذي يحتوي على الجدول المحوري
String inputPath = "input.xlsx";
String outputPath = "output.xlsx";
Workbook workbook = new Workbook(inputPath);

// الوصول إلى ورقة العمل التي تحتوي على الجدول المحوري (الفهرس 0)
Worksheet worksheet = workbook.getWorksheets().get(0);

// الوصول إلى الجدول المحوري عن طريق الفهرس
PivotTable pivotTable = worksheet.getPivotTables().get(0);

// التحقق من وجود حقل محوري واحد على الأقل بقيمة في منطقة البيانات
if (pivotTable.getDataFields().getCount() == 0)
{
    throw new RuntimeException("Pivot table has no value (data) PivotField.");
}
PivotField valueField = pivotTable.getDataFields().get(0);

// استرجاع حقل الصف المحوري المستهدف (الحقل الذي نريد تطبيق أفضل 10 عليه)
PivotField rowField = pivotTable.getRowFields().get(0);

// حقل البيانات الأول (والوحيد) يقع في الفهرس 0؛ تقوم أفضل 10 بترتيب العناصر حسبه.
int valueFieldIndex = 0;

// تطبيق مرشح أفضل 10 على حقل الصف:
//   - itemCount   = 10
//   - filterType  = PivotFilterType.SUM
//   - isTop       = true (أفضل N؛ false تعني أسوأ N)
//   - valueFieldIndex = فهرس حقل البيانات المستخدم لترتيب العناصر
rowField.filterTop10(10, PivotFilterType.SUM, true, valueFieldIndex);

// تحديث بيانات الجدول المحوري وإعادة حسابها حتى يصبح المرشح ساري المفعول
pivotTable.refreshData();

// حفظ المصنف
workbook.save(outputPath);
```
## **التصفية عن طريق إخفاء أو إظهار عناصر الجدول المحوري**
بالإضافة إلى واجهات برمجة التطبيقات المنظمة للمرشحات، يتيح لك Aspose.Cells التحكم في رؤية كل عنصر محوري فردي بشكل مباشر. من خلال التكرار عبر مجموعة `PivotItems` الخاصة بـ `PivotField` وتبديل خاصية `IsHidden`، يمكنك قمع عناصر محددة بشكل انتقائي دون تطبيق مرشح قائم على الصيغة. يؤدي تعيين `IsHidden = true` إلى إخفاء العنصر من الجدول المحوري؛ بينما يؤدي تعيين `IsHidden = false` إلى إظهاره مرة أخرى وجعله مرئيًا.
يكون هذا الأسلوب مفيدًا عندما تكون قاعدة التصفية غير منتظمة أو خاصة بعنصر معين، مثل إخفاء عدد قليل من الفئات المسماة التي يجب ألا تظهر في تقرير معين. يحمّل المثال التالي جدولًا محوريًا، ويخفي عنصرًا محددًا بالاسم، ويوضح كيفية إظهاره، ويحدّث الجدول المحوري، ويحفظ المصنف.
```java
import com.aspose.cells.*;

// تحميل مصنف موجود يحتوي على جدول محوري
Workbook workbook = new Workbook("pivot_table_sample.xlsx");

// الوصول إلى ورقة العمل الأولى التي تحتوي على الجدول المحوري
Worksheet sheet = workbook.getWorksheets().get(0);

// الوصول إلى الجدول المحوري بواسطة الفهرس (الجدول المحوري الأول في الورقة)
PivotTable pivotTable = sheet.getPivotTables().get(0);

// استرجاع حقل المحور المستهدف (حقل تسمية الصف الأول الذي سنخفي/نظهر العناصر فيه)
PivotField pivotField = pivotTable.getRowFields().get(0);

// التكرار عبر مجموعة عناصر المحور في حقل المحور المحدد
int itemCount = pivotField.getPivotItems().getCount();
for (int i = 0; i < itemCount; i++)
{
    PivotItem item = pivotField.getPivotItems().get(i);

    // إخفاء عناصر المحور التي تطابق اسمًا/معيارًا محددًا
    if (item.getName() == "Item1" || item.getName() == "Item2")
    {
        item.setHidden(true);
    }

    // عرض كيفية إظهار عنصر محوري مخفي مسبقًا
    if (item.getName() == "Item3")
    {
        item.setHidden(false);
    }
}

// تحديث وإعادة حساب الجدول المحوري لتطبيق التغييرات
pivotTable.refreshData();

// حفظ المصنف - تبقى العناصر المخفية في البيانات الأساسية
// ولكن يتم استبعادها من مخرجات الجدول المحوري المعروضة
workbook.save("output_pivot_filtered.xlsx");
```
## **الملخص**
يوفر Aspose.Cells for Java مجموعة كاملة من إمكانيات تصفية الجداول المحورية التي تتطابق مع تلك الموجودة في Microsoft Excel. تغطي مرشحات التسميات والتاريخ والقيم أكثر السيناريوهات التحليلية شيوعًا، بينما يتعامل مرشح أعلى 10 مع تقارير الترتيب. عندما تكون قاعدة التصفية غير منتظمة، توفر خاصية `PivotItem.IsHidden` بديلاً مرنًا على مستوى العنصر. يتيح لك الجمع بين هذه الاستراتيجيات — على سبيل المثال، تطبيق مرشح تسمية ثم إخفاء عناصر محددة — إنشاء تقارير جدول محوري مستهدفة بدقة من الكود بالكامل.
{{< app/cells/assistant language="java" >}}