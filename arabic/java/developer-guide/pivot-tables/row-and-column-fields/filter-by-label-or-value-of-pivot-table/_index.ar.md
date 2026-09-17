---
title: تصفية الجداول المحورية حسب التسمية أو القيمة
linktitle: تصفية الجداول المحورية حسب التسمية أو القيمة
description: يدعم Aspose.Cells for Java إمكانيات تصفية شاملة للجداول المحورية. تشرح هذه المقالة كيفية تصفية بيانات الجدول المحوري باستخدام مرشحات التسميات، ومرشحات التواريخ، ومرشحات القيم، ومرشحات أعلى 10، وكذلك من خلال إخفاء أو إظهار عناصر الجدول المحوري.
keywords: Aspose.Cells, مكتبة Java, جدول بيانات, جدول محوري, تصفية, مرشح التسمية, مرشح القيمة, مرشح التاريخ, مرشح أعلى 10, عنصر الجدول المحوري, إخفاء عنصر الجدول المحوري
type: docs
weight: 10
url: /ar/java/filter-by-label-or-value-of-pivot-table/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
يوفر Aspose.Cells خمس استراتيجيات عملية لتصفية البيانات المعروضة في جدول محوري. يمكنك تطبيق مرشحات التسميات على حقول الصفوف أو الأعمدة النصية، واستخدام مرشحات التواريخ عندما يحتوي الحقل على خلايا تاريخ ووقت فقط أو خلايا فارغة، وتطبيق مرشحات القيم على الأرقام المجمعة، واستخدام مرشحات أعلى 10 للترتيب حسب حقل قيمة، أو إخفاء وإظهار عناصر الجدول المحوري يدويًا باستخدام خاصية `IsHidden`. تتعرض كل استراتيجية من خلال واجهات برمجة التطبيقات المخصصة في فئتي `PivotField` و`PivotItem`.
{{% /alert %}}

## **مقدمة**
تُعد الجداول المحورية أدوات تحليلية قوية، لكن الملخصات الخام غالبًا ما تحتوي على قدر أكبر بكثير من المعلومات مما تحتاج إلى عرضه. التصفية هي الآلية الأساسية لتضييق نطاق جدول محوري إلى الصفوف أو الأعمدة أو القيم المهمة لتقرير معين. يدعم Aspose.Cells for Java إمكانيات التصفية المتاحة في Microsoft Excel، ويعرضها برمجيًا بحيث يمكن أتمتة إنشاء التقارير بالكامل.
تتناول هذه المقالة استراتيجيات التصفية التالية:
1. **مرشح التسمية** — يُصفّي عناصر حقل الصف أو العمود بناءً على تسمياتها النصية.
2. **مرشح التاريخ** — يُصفّي حقول الصفوف أو الأعمدة التي تحتوي على قيم تاريخ ووقت فقط (أو خلايا فارغة).
3. **مرشح القيمة** — يُصفّي العناصر بناءً على القيم المجمعة لحقل البيانات.
4. **مرشح أعلى 10** — يعرض فقط أعلى أو أدنى عدد N من العناصر مرتبة حسب حقل قيمة.
5. **إخفاء / إظهار عناصر الجدول المحوري** — يتحكم يدويًا في رؤية كل عنصر على حدة في الحقل.
يستخدم كل أسلوب طريقة مختلفة في فئة `PivotField` أو خاصية في فئة `PivotItem`. بعد تطبيق أي مرشح، يجب استدعاء `refreshData()` و`calculateData()` على الجدول المحوري بحيث تعكس البيانات المخزنة مؤقتًا والقيم المحسوبة حالة المرشح الجديدة.

## **مرشح التسمية**
يتيح لك مرشح التسمية تصفية عناصر حقل الصف أو العمود بمقارنة تسمياتها النصية بنمط معين. يكون هذا مفيدًا عندما تريد عرض المنتجات التي تبدأ أسماؤها بحرف معين فقط، أو التي تحتوي على كلمة معينة، أو التي تطابق معيارًا آخر قائمًا على التسمية.
يعرض Aspose.Cells ميزة تصفية التسميات من خلال الطريقة `PivotField.filterByLabel(PivotFilterType, String)`. يتضمن تعداد `PivotFilterType` قيمًا مثل `CaptionBeginsWith` و`CaptionContains` و`CaptionEndsWith` و`CaptionDoesNotContain` و`CaptionIsNotBlank` و`CaptionIsBlank` وغيرها. تُمرَّر الوسيطة الثانية كسلسلة نصية للتسمية المستخدمة في المقارنة.
يُحمِّل المثال التالي مصنفًا يحتوي على جدول محوري موجود، ويطبق مرشح تسمية بحيث تبقى العناصر التي تبدأ تسمياتها ببادئة محددة فقط مرئية، ثم يُحدِّث الجدول المحوري ويحفظ النتيجة.

```java
import com.aspose.cells.*;
String fileName = "sample.xlsx";
String prefix = "B";
// تحميل مصنف العمل الحالي الذي يحتوي على جدول محوري
Workbook workbook = new Workbook(fileName);
// الوصول إلى ورقة العمل بواسطة الفهرس (ورقة العمل الأولى)
Worksheet worksheet = workbook.getWorksheets().get(0);
// الوصول إلى الجدول المحوري بواسطة الفهرس
PivotTable pivotTable = worksheet.getPivotTables().get(0);
// استرجاع حقل الصف الأول PivotField
PivotField rowField = pivotTable.getRowFields().get(0);
// تطبيق فلتر التسمية - عرض عناصر الصفوف التي تبدأ تسمياتها بالبادئة المقدمة فقط
rowField.filterByLabel(PivotFilterType.CAPTION_BEGINS_WITH, prefix, "");
// تحديث وإعادة حساب بيانات الجدول المحوري حتى يتم تطبيق الفلتر
pivotTable.refreshData();
// حفظ مصنف العمل على القرص
workbook.save(fileName);
```

## **مرشح التاريخ**
تتيح لك مرشحات التاريخ تضييق نطاق جدول محوري وفق معايير تستند إلى التاريخ مثل اليوم، أو الأسبوع الماضي، أو هذا الشهر، أو الربع القادم، أو نطاق تاريخي محدد. وهي مرشحات متخصصة تعمل فقط مع الحقول التي تخزن معلومات التاريخ والوقت.

{{% alert color="primary" %}}
لا يعمل مرشح التاريخ إلا عندما تحتوي منطقة الصف أو العمود على خلايا تاريخ ووقت فقط ou قيم فارغة. إذا كان الحقل الأساسي يحتوي على أنواع بيانات أخرى مثل الأرقام أو النصوص، فلن يُنتج مرشح التاريخ النتيجة المتوقعة. تأكد من تنسيق الحقل كتاريخ ومن أن جميع القيم هي نسخ صالحة من `DateTime` أو خلايا فارغة قبل تطبيق هذا المرشح.
{{% /alert %}}

يعرض Aspose.Cells ميزة تصفية التواريخ من خلال الطريقة `PivotField.filterByDate(PivotFilterType, params DateTime[] values)`. يحتوي تعداد `PivotFilterType` على قيم تاريخ مخصصة مثل `Today` و`Yesterday` و`LastWeek` و`ThisWeek` و`NextWeek` و`LastMonth` و`ThisMonth` و`NextMonth` و`LastQuarter` و`ThisQuarter` و`NextQuarter` و`LastYear` و`ThisYear` و`NextYear` و`Between`. بناءً على نوع المرشح المختار، تُمرِّر قيمة أو قيمتين من نوع `DateTime` (بالنسبة لـ `Between`، تُمرِّر تاريخي البداية والنهاية).
يُحمِّل المثال التالي مصنفًا يحتوي على جدول محوري توجد في منطقة الصفوف فيه حقل تاريخ، ويطبق مرشح تاريخ يقصر العناصر المرئية على نطاق تاريخي معين، ثم يُحدِّث الجدول المحوري ويحفظ المصنف.

```java
import java.io.File;
import java.io.FileNotFoundException;
String inputPath = "sample.xlsx";
String outputPath = "output_filtered.xlsx";
if (!new File(inputPath).exists())
{
    throw new FileNotFoundException("Source workbook not found: " + inputPath);
}
// تحميل المصنف الموجود الذي يحتوي على الجدول المحوري
Workbook workbook = new Workbook(inputPath);
// الوصول إلى ورقة العمل التي تحتوي على الجدول المحوري (حسب الفهرس)
Worksheet worksheet = workbook.getWorksheets().get(0);
// الوصول إلى الجدول المحوري حسب الفهرس
PivotTable pivotTable = worksheet.getPivotTables().get(0);
// استرداد حقل التاريخ المحوري من منطقة الصفوف
// (يعمل مرشح التاريخ فقط عندما تحتوي منطقة الصفوف/الأعمدة على خلايا تاريخ-وقت فقط أو فراغات)
PivotField dateField = pivotTable.getRowFields().get(0);
// تعريف معيار التاريخ لمرشح Between
DateTime startDate = new DateTime(2020, 1, 1);
DateTime endDate = new DateTime(2020, 12, 31);
// تطبيق مرشح التاريخ على الحقل المحوري
dateField.filterByDate(PivotFilterType.DATE_BETWEEN, startDate, endDate);
// تحديث الجدول المحوري وإعادة حسابه حتى يصبح المرشح ساري المفعول
pivotTable.refreshData();
// حفظ المصنف
workbook.save(outputPath);
```

## **مرشح القيمة**
تعمل مرشحات القيمة على القيم المجمعة التي يحسبها الجدول المحوري في منطقة البيانات الخاصة به. وبدلاً من مطابقة تسميات نصية، تُقارن هذه المرشحات الإجماليات الرقمية بحد معين. تشمل حالات الاستخدام النموذجية عرض المنتجات التي يتجاوز مجموع مبيعاتها مبلغًا مستهدفًا فقط، أو المناطق التي يقع عدد معاملاتها ضمن نطاق معين فقط.
يعرض Aspose.Cells ميزة تصفية القيم من خلال الطريقة `PivotField.filterByValue(PivotField valueField, PivotFilterType filterType, params Object[] values)`. تستخدم وسيطة `filterType` قيمًا مثل `ValueGreaterThan` و`ValueLessThan` و`ValueBetween` و`ValueEqual` و`ValueNotEqual` و`ValueGreaterThanOrEqual` و`ValueLessThanOrEqual`. تحدد وسيطة `valueField` حقل البيانات الذي يجب تقييمه، وتُمرَّر الوسيطة الأخيرة (أو الوسائط) كقيمة (قيم) العتبة.
يُحمِّل المثال التالي مصنفًا يحتوي على جدول محوري، ويطبق مرشح قيمة يحتفظ فقط بالعناصر التي تتجاوز مبيعاتها المجمعة عتبة رقمية، ثم يُحدِّث الجدول المحوري ويحفظ المصنف.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook("sample.xlsx");
Worksheet worksheet = workbook.getWorksheets().get(0);
PivotTable pivotTable = worksheet.getPivotTables().get(0);
PivotField rowField = pivotTable.getRowFields().get(0);
PivotField dataField = pivotTable.getDataFields().get(0);
// ابحث عن فهرس حقل البيانات يدويًا لأن PivotFieldCollection لا يحتوي على IndexOf
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
مرشح أعلى 10 هو شكل متخصص من مرشحات القيمة يحتفظ فقط بأعلى أو أدنى عدد N من العناصر بناءً على حقل قيمة مختار. يُستخدم بشكل شائع في تقارير الترتيب مثل "أعلى 10 منتجات من حيث الإيرادات" أو "أدنى 5 مناطق من حيث عدد المبيعات".

{{% alert color="primary" %}}
لا يكون مرشح أعلى 10 فعالًا إلا عندما يحتوي الجدول المحوري على حقل قيمة واحد أو أكثر في منطقة البيانات. فبدون وجود حقل قيمة واحد على الأقل، لا يوجد مقياس مجمع لترتيب العناصر وفقًا له، ولا يمكن تطبيق المرشح.
{{% /alert %}}

يعرض Aspose.Cells ميزة تصفية أعلى 10 من خلال الطريقة `PivotField.filterTop10(int itemCount, boolean isTop, PivotField valueField, PivotFilterType filterType)`. تحدد وسيطة `itemCount` عدد العناصر التي يجب الاحتفاظ بها، وتشير `isTop` إلى ما إذا كان يجب الاحتفاظ بأعلى العناصر (true) أو أدنى العناصر (false)، وتشير `valueField` إلى حقل البيانات المستخدم للترتيب، وتتحكم `filterType` في كيفية حساب القيمة (عادةً `Sum`، ولكن أيضًا `Count` و`Percent`).
يُحمِّل المثال التالي مصنفًا يحتوي على جدول محوري يشمل حقل قيمة، ويطبق مرشح أعلى 10 للاحتفاظ فقط بأعلى 10 عناصر من حيث مجموع المبيعات، ثم يُحدِّث الجدول المحوري ويحفظ المصنف.

```java
import com.aspose.cells.*;
// تحميل دفتر العمل الموجود الذي يحتوي على الجدول المحوري
String inputPath = "input.xlsx";
String outputPath = "output.xlsx";
Workbook workbook = new Workbook(inputPath);
// الوصول إلى ورقة العمل التي تحتوي على الجدول المحوري (الفهرس 0)
Worksheet worksheet = workbook.getWorksheets().get(0);
// الوصول إلى الجدول المحوري بواسطة الفهرس
PivotTable pivotTable = worksheet.getPivotTables().get(0);
// التأكد من وجود حقل قيمة واحد على الأقل في منطقة البيانات
if (pivotTable.getDataFields().getCount() == 0)
{
    throw new RuntimeException("Pivot table has no value (data) PivotField.");
}
PivotField valueField = pivotTable.getDataFields().get(0);
// استرجاع حقل الصف المستهدف (الحقل الذي نريد تطبيق Top 10 عليه)
PivotField rowField = pivotTable.getRowFields().get(0);
// حقل البيانات الأول (والوحيد) يقع عند الفهرس 0؛ يتم الترتيب حسب Top 10 بناءً عليه.
int valueFieldIndex = 0;
// تطبيق مرشح Top 10 على حقل الصف:
//   - itemCount   = 10
//   - filterType  = PivotFilterType.SUM
//   - isTop       = true (أعلى N؛ القيمة false تعني أسفل N)
//   - valueFieldIndex = فهرس حقل البيانات المستخدم لترتيب العناصر
rowField.filterTop10(10, PivotFilterType.SUM, true, valueFieldIndex);
// تحديث بيانات الجدول المحوري وإعادة حسابها حتى يصبح المرشح ساري المفعول
pivotTable.refreshData();
// حفظ دفتر العمل
workbook.save(outputPath);
```

## **التصفية عن طريق إخفاء أو إظهار عناصر الجدول المحوري**
بالإضافة إلى واجهات برمجة التطبيقات المنظمة للمرشحات، يتيح لك Aspose.Cells التحكم مباشرةً في رؤية كل عنصر من عناصر الجدول المحوري على حدة. من خلال التكرار في مجموعة `PivotItems` الخاصة بـ `PivotField` وتبديل خاصية `IsHidden`، يمكنك إخفاء عناصر محددة بشكل انتقائي دون تطبيق مرشح قائم على صيغة. يؤدي تعيين `IsHidden = true` إلى إخفاء العنصر من الجدول المحوري، بينما يؤدي تعيين `IsHidden = false` إلى إظهاره وجعله مرئيًا مرة أخرى.
يكون هذا الأسلوب مفيدًا عندما تكون قاعدة التصفية غير منتظمة أو خاصة بعنصر معين، مثل إخفاء عدد صغير من الفئات المُسماة التي لا ينبغي أن تظهر في تقرير معين. يُحمِّل المثال التالي جدولًا محوريًا، ويُخفي عنصرًا محددًا بالاسم، ويُظهر كيفية إظهاره مرة أخرى، ثم يُحدِّث الجدول المحوري ويحفظ المصنف.

```java
import com.aspose.cells.*;
// تحميل مصنف موجود يحتوي على جدول محوري
Workbook workbook = new Workbook("pivot_table_sample.xlsx");
// الوصول إلى ورقة العمل الأولى التي تحتوي على الجدول المحوري
Worksheet sheet = workbook.getWorksheets().get(0);
// الوصول إلى الجدول المحوري عن طريق الفهرس (الجدول المحوري الأول في الورقة)
PivotTable pivotTable = sheet.getPivotTables().get(0);
// استرجاع حقل محوري مستهدف (حقل تسمية الصف الأول الذي سنخفي/نظهر عناصره فيه)
PivotField pivotField = pivotTable.getRowFields().get(0);
// التكرار خلال مجموعة PivotItems للحقل المحوري المحدد
int itemCount = pivotField.getPivotItems().getCount();
for (int i = 0; i < itemCount; i++)
{
    PivotItem item = pivotField.getPivotItems().get(i);
    // إخفاء عناصر الجدول المحوري التي تطابق اسمًا/معيارًا معينًا
    if (item.getName() == "Item1" || item.getName() == "Item2")
    {
        item.setHidden(true);
    }
    // عرض كيفية إظهار عنصر محوري مخفي سابقًا
    if (item.getName() == "Item3")
    {
        item.setHidden(false);
    }
}
// تحديث وإعادة حساب الجدول المحوري حتى تسري التغييرات
pivotTable.refreshData();
// حفظ المصنف - تظل العناصر المخفية في البيانات الأساسية
// ولكن يتم استبعادها من ناتج الجدول المحوري المعروض
workbook.save("output_pivot_filtered.xlsx");
```

## **ملخص**
يوفر Aspose.Cells for Java مجموعة كاملة من إمكانيات تصفية الجداول المحورية التي تُطابق تلك الموجودة في Microsoft Excel. تُغطي مرشحات التسميات والتواريخ والقيم معظم السيناريوهات التحليلية الشائعة، بينما يتعامل مرشح أعلى 10 مع تقارير الترتيب. عندما تكون قاعدة التصفية غير منتظمة، توفر خاصية `PivotItem.IsHidden` بديلاً مرنًا على مستوى العنصر. يتيح لك الجمع بين هذه الاستراتيجيات — على سبيل المثال، تطبيق مرشح تسمية ثم إخفاء عناصر محددة — بناء تقارير جدول محوري مستهدفة بدقة بالكامل من خلال الكود.

## مقالات ذات صلة
- [إدراج جدول محوري](/cells/ar/java/pivot-tables/)
- [إضافة حقول الصفوف والأعمدة للجدول المحوري في Aspose.Cells for Java](/cells/ar/java/pivot-table-add-row-and-column-fields/)
- [إضافة حقول مرشحات إلى جدول محوري في Aspose.Cells for Java](/cells/ar/java/add-page-field-in-pivot-table/)
- [إدارة حقول القيم في الجدول المحوري في Aspose.Cells for Java](/cells/ar/java/manage-value-fields/)
- [تحديث الجداول المحورية وذاكرة التخزين المؤقت في Aspose.Cells for Java](/cells/ar/java/refresh-pivot-table/)

{{< app/cells/assistant language="java" >}}