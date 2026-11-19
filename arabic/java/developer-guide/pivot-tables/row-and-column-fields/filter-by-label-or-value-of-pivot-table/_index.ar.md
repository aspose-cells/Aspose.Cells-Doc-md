---
title: تصفية الجداول المحورية حسب التسمية أو القيمة
description: يدعم Aspose.Cells for Java إمكانات تصفية شاملة للجداول المحورية. توضح هذه المقالة كيفية تصفية بيانات الجدول المحوري باستخدام مرشحات التسمية والتاريخ والقيمة وأفضل 10، وكذلك عن طريق إخفاء عناصر الجدول المحوري أو إظهارها.
linktitle: تصفية الجداول المحورية حسب التسمية أو القيمة
keywords: Aspose.Cells, مكتبة Java, جدول بيانات, جدول محوري, تصفية, مرشح التسمية, مرشح القيمة, مرشح التاريخ, مرشح أفضل 10 عناصر, عنصر محوري, إخفاء عنصر محوري
type: docs
weight: 10
url: /ar/java/filter-by-label-or-value-of-pivot-table/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
يوفر Aspose.Cells خمس استراتيجيات عملية لتصفية البيانات المعروضة في جدول محوري. يمكنك تطبيق مرشحات التسمية على حقول الصفوف أو الأعمدة النصية، أو استخدام مرشحات التاريخ عندما يحتوي الحقل على خلايا تاريخ ووقت فقط أو على خلايا فارغة، أو تطبيق مرشحات القيمة على الأرقام المجمعة، أو استخدام مرشح أفضل 10 للترتيب حسب حقل قيمة، أو إخفاء عناصر الجدول المحوري الفردية وإظهارها يدويًا باستخدام الخاصية `IsHidden`. تتوفر كل استراتيجية عبر واجهات API مخصصة في الصنفين `PivotField` و`PivotItem`.
{{% /alert %}}

## **مقدمة**
تعد الجداول المحورية أدوات تحليلية قوية، لكن الملخصات الخام غالبًا ما تتضمن معلومات أكثر بكثير مما تحتاج إلى عرضه. التصفية هي الآلية الأساسية لتضييق الجدول المحوري بحيث يقتصر على الصفوف أو الأعمدة أو القيم المهمة لتقرير معين. يوازي Aspose.Cells for Java إمكانات التصفية المتاحة في Microsoft Excel ويتيح الوصول إليها برمجيًا بحيث يمكن أتمتة إنشاء التقارير بالكامل.
تغطي هذه المقالة استراتيجيات التصفية التالية:
1. **مرشح التسمية** — يصفي عناصر حقول الصفوف أو الأعمدة استنادًا إلى تسمياتها النصية.
2. **مرشح التاريخ** — يصفي حقول الصفوف أو الأعمدة التي تحتوي على قيم تاريخ ووقت فقط أو على خلايا فارغة.
3. **مرشح القيمة** — يصفي العناصر استنادًا إلى القيم المجمعة لحقل بيانات.
4. **مرشح أفضل 10 عناصر** — يعرض فقط أفضل N أو أسوأ N عنصرًا مرتبةً حسب حقل قيمة.
5. **إخفاء / إظهار عناصر الجدول المحوري** — يتحكم يدويًا في رؤية كل عنصر فردي في الحقل.
يستخدم كل نهج أسلوبًا مختلفًا في الصنف `PivotField` أو خاصية في الصنف `PivotItem`. بعد تطبيق أي مرشح، يجب استدعاء `getPivotCache().refresh()` على الجدول المحوري حتى تعكس البيانات المخزنة مؤقتًا والقيم المحسوبة حالة المرشح الجديدة.

## **مرشح التسمية**
يسمح مرشح التسمية بتصفية عناصر حقل صف أو عمود عن طريق مقارنة تسمياتها النصية مع نمط. يكون ذلك مفيدًا عندما تريد عرض المنتجات التي تبدأ أسماؤها بحرف محدد أو تحتوي على كلمة معينة أو تطابق أي معيار آخر قائم على التسمية.
يوفر Aspose.Cells تصفية التسمية من خلال أسلوب `PivotField.filterByLabel(PivotFilterType, String)`. يضم تعداد `PivotFilterType` قيمًا مثل `CaptionBeginsWith` و`CaptionContains` و`CaptionEndsWith` و`CaptionDoesNotContain` و`CaptionIsNotBlank` و`CaptionIsBlank` وغيرها. ويوفر الوسيط الثاني سلسلة التسمية المستخدمة في المقارنة.
يحمّل المثال التالي مصنفًا يحتوي على جدول محوري موجود، ويطبق مرشح تسمية بحيث تبقى العناصر التي تبدأ تسمياتها ببادئة محددة فقط ظاهرة، ثم يحدّث الجدول المحوري ويحفظ النتيجة.

```java
import com.aspose.cells.*;
String fileName = "sample.xlsx";
String prefix = "B";
// Load the existing workbook containing a pivot table
Workbook workbook = new Workbook(fileName);
// Access the worksheet by index (first worksheet)
Worksheet worksheet = workbook.getWorksheets().get(0);
// Access the pivot table by index
PivotTable pivotTable = worksheet.getPivotTables().get(0);
// Retrieve the first row PivotField
PivotField rowField = pivotTable.getRowFields().get(0);
// Apply the label filter - show only row items whose labels begin with the supplied prefix
rowField.filterByLabel(PivotFilterType.CAPTION_BEGINS_WITH, prefix, "");
// Refresh and recalculate the pivot table data so the filter takes effect
pivotTable.getPivotCache().refresh();
// Save the workbook back to disk
workbook.save(fileName);
```

## **مرشح التاريخ**
تتيح مرشحات التاريخ تضييق الجدول المحوري وفق معايير تستند إلى التاريخ، مثل اليوم أو الأسبوع الماضي أو هذا الشهر أو الربع التالي أو نطاق تاريخ محدد. وهي مرشحات متخصصة لا تعمل إلا مع الحقول التي تخزن معلومات التاريخ والوقت.

{{% alert color="primary" %}}
لا يعمل مرشح التاريخ إلا إذا احتوت منطقة الصفوف أو الأعمدة على خلايا تاريخ ووقت أو قيم فارغة فقط. إذا احتوى الحقل الأساسي على أنواع بيانات أخرى مثل الأرقام أو النصوص، فلن ينتج مرشح التاريخ النتيجة المتوقعة. تأكد من أن الحقل منسق كتاريخ وأن جميع القيم إما نسخ `DateTime` صالحة أو خلايا فارغة قبل تطبيق هذا المرشح.
يوفر Aspose.Cells تصفية التاريخ من خلال أسلوب `PivotField.filterByDate(PivotFilterType, params DateTime[] values)`. يحتوي تعداد `PivotFilterType` على قيم تاريخ مخصصة مثل `Today` و`Yesterday` و`LastWeek` و`ThisWeek` و`NextWeek` و`LastMonth` و`ThisMonth` و`NextMonth` و`LastQuarter` و`ThisQuarter` و`NextQuarter` و`LastYear` و`ThisYear` و`NextYear` و`Between`. وبحسب نوع المرشح المختار، تمرر قيمة `DateTime` واحدة أو قيمتين (بالنسبة إلى `Between`، تمرر تاريخ البداية والنهاية).
يحمّل المثال التالي مصنفًا يحتوي على جدول محوري موجود في منطقة الصفوف فيه حقل تاريخ، ويطبق مرشح تاريخ يقصر العناصر الظاهرة على نطاق تاريخ محدد، ثم يحدّث الجدول المحوري ويحفظ المصنف.
{{% /alert %}}

```java
import java.io.File;
import java.io.FileNotFoundException;
String inputPath = "sample.xlsx";
String outputPath = "output_filtered.xlsx";
if (!new File(inputPath).exists())
{
    throw new FileNotFoundException("Source workbook not found: " + inputPath);
}
// Load the existing workbook that contains the pivot table
Workbook workbook = new Workbook(inputPath);
// Access the worksheet that holds the pivot table (by index)
Worksheet worksheet = workbook.getWorksheets().get(0);
// Access the pivot table by index
PivotTable pivotTable = worksheet.getPivotTables().get(0);
// Retrieve the date PivotField from the row area
// (Date filter only works when the row/column area contains only date-time cells or blanks)
PivotField dateField = pivotTable.getRowFields().get(0);
// Define the date criterion for the Between filter
DateTime startDate = new DateTime(2020, 1, 1);
DateTime endDate = new DateTime(2020, 12, 31);
// Apply the date filter on the pivot field
dateField.filterByDate(PivotFilterType.DATE_BETWEEN, startDate, endDate);
// Refresh and recalculate the pivot table so the filter takes effect
pivotTable.getPivotCache().refresh();
// Persist the workbook
workbook.save(outputPath);
```

## **مرشح القيمة**
تعمل مرشحات القيمة على القيم المجمعة التي يحسبها الجدول المحوري في منطقة البيانات. وبدلاً من مطابقة التسميات النصية، تقارن الإجماليات الرقمية بعتبة محددة. تشمل حالات الاستخدام النموذجية عرض المنتجات التي يزيد مجموع مبيعاتها عن مبلغ مستهدف فقط، أو المناطق التي يقع عدد معاملاتها ضمن نطاق محدد فقط.
يوفر Aspose.Cells تصفية القيمة من خلال أسلوب `PivotField.filterByValue(PivotField valueField, PivotFilterType filterType, params Object[] values)`. تستخدم الوسيط `filterType` قيمًا مثل `ValueGreaterThan` و`ValueLessThan` و`ValueBetween` و`ValueEqual` و`ValueNotEqual` و`ValueGreaterThanOrEqual` و`ValueLessThanOrEqual`. ويحدد الوسيط `valueField` حقل البيانات المطلوب تقييمه، بينما يوفر الوسيط الأخير أو الوسيطان الأخيران قيمة العتبة أو قيمها.
يحمّل المثال التالي مصنفًا يحتوي على جدول محوري، ويطبق مرشح قيمة يبقي على العناصر التي يتجاوز مجموع مبيعاتها عتبة رقمية فقط، ثم يحدّث الجدول المحوري ويحفظ المصنف.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook("sample.xlsx");
Worksheet worksheet = workbook.getWorksheets().get(0);
PivotTable pivotTable = worksheet.getPivotTables().get(0);
PivotField rowField = pivotTable.getRowFields().get(0);
PivotField dataField = pivotTable.getDataFields().get(0);
// Find the data field index manually since PivotFieldCollection doesn't have IndexOf
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
pivotTable.getPivotCache().refresh();
workbook.save("output.xlsx");
```

## **مرشح أفضل 10 عناصر**
مرشح أفضل 10 عناصر هو شكل متخصص من مرشح القيمة يحتفظ فقط على أعلى N أو أدنى N عنصرًا استنادًا إلى حقل قيمة محدد. ويستخدم عادةً في تقارير الترتيب، مثل «أفضل 10 منتجات حسب الإيرادات» أو «أسوأ 5 مناطق حسب عدد المبيعات».

{{% alert color="primary" %}}
لا يكون مرشح أفضل 10 فعالًا إلا عندما يحتوي الجدول المحوري على حقل قيمة واحد أو أكثر في منطقة البيانات. من دون حقل قيمة واحد على الأقل، لا توجد أي مقياس مجمع يمكن ترتيب العناصر بناءً عليه، ولا يمكن تطبيق المرشح.
يوفر Aspose.Cells تصفية أفضل 10 من خلال أسلوب `PivotField.filterTop10(int valueFieldIndex, PivotFilterType filterType, boolean isTop, int itemCount)`. يمثل الوسيط `valueFieldIndex` فهرس حقل البيانات الذي تُرتب العناصر وفق قيمه المجمعة، ويحدد `filterType` وحدة `itemCount` (يحتفظ `PivotFilterType.COUNT` بعدد ثابت من العناصر، بينما يحتفظ `PivotFilterType.PERCENT` بنسبة من العناصر بحيث تكون `itemCount` هي النسبة نفسها)، ويشير `isTop` إلى الاحتفاظ بالعناصر الأعلى (`true`) أو الأدنى (`false`)، ويحدد `itemCount` عدد العناصر أو النسبة التي ينبغي الاحتفاظ بها.
يحمّل المثال التالي مصنفًا يحتوي على جدول محوري يتضمن حقل قيمة، ويطبق مرشح أفضل 10_elements للحفاظ على أعلى 10 عناصر فقط استنادًا إلى مجموع المبيعات، ثم يحدّث الجدول المحوري ويحفظ المصنف.
{{% /alert %}}

```java
import com.aspose.cells.*;
// Load the existing workbook that contains the pivot table
String inputPath = "input.xlsx";
String outputPath = "output.xlsx";
Workbook workbook = new Workbook(inputPath);
// Access the worksheet that holds the pivot table (index 0)
Worksheet worksheet = workbook.getWorksheets().get(0);
// Access the pivot table by index
PivotTable pivotTable = worksheet.getPivotTables().get(0);
// Confirm there is at least one value PivotField in the data area
if (pivotTable.getDataFields().getCount() == 0)
{
    throw new RuntimeException("Pivot table has no value (data) PivotField.");
}
PivotField valueField = pivotTable.getDataFields().get(0);
// Retrieve the target row PivotField (the field we want to apply Top 10 on)
PivotField rowField = pivotTable.getRowFields().get(0);
// The first (and only) data field is at index 0; Top 10 ranks by it.
int valueFieldIndex = 0;
// Apply the Top 10 filter on the row field:
//   - itemCount   = 10
//   - filterType  = PivotFilterType.SUM
//   - isTop       = true (top N; false would mean bottom N)
//   - valueFieldIndex = the index of the data field used to rank items
rowField.filterTop10(valueFieldIndex, PivotFilterType.COUNT, true, 10);
// Refresh the pivot table data and recalculate it so the filter takes effect
pivotTable.getPivotCache().refresh();
// Save the workbook
workbook.save(outputPath);
```

## **التصفية عبر إخفاء عناصر الجدول المحوري أو إظهارها**
بالإضافة إلى واجهات API للمرشحات المنظَّمة، يتيح Aspose.Cells التحكم مباشرة في رؤية كل عنصر من عناصر الجدول المحوري. ومن خلال التكرار على مجموعة `PivotItems` التابعة لـ`PivotField` وتبديل الخاصية `IsHidden`، يمكنك إخفاء عناصر محددة بشكل انتقائي دون تطبيق مرشح قائم على الصيغ. لتعيين `IsHidden = true`، يُخفى العنصر من الجدول المحوري؛ بينما لتعيين `IsHidden = false`، يُظهره من جديد.
يكون هذا الأسلوب مفيدًا عندما تكون قاعدة التصفية غير منتظمة أو خاصة بعنصر معين، مثل إخفاء عدد قليل من الفئات المسماة التي ينبغي ألا تظهر في تقرير معين. يحمّل المثال التالي جدولًا محوريًا، ويخفي عنصرًا محددًا بالاسم، ويوضح كيفية إظهاره، ثم يحدّث الجدول المحوري ويحفظ المصنف.

```java
import com.aspose.cells.*;
// Load an existing workbook containing a pivot table
Workbook workbook = new Workbook("pivot_table_sample.xlsx");
// Access the first worksheet which contains the pivot table
Worksheet sheet = workbook.getWorksheets().get(0);
// Access the pivot table by index (the first pivot table on the sheet)
PivotTable pivotTable = sheet.getPivotTables().get(0);
// Retrieve the target PivotField (the first row label field that we'll hide/unhide items in)
PivotField pivotField = pivotTable.getRowFields().get(0);
// Iterate through the PivotItems collection of the selected PivotField
int itemCount = pivotField.getPivotItems().getCount();
for (int i = 0; i < itemCount; i++)
{
    PivotItem item = pivotField.getPivotItems().get(i);
    // Hide pivot items that match a specific name/criterion
    if (item.getName().equals("Item1") || item.getName().equals("Item2"))
    {
        item.setHidden(true);
    }
    // Demonstrate unhiding: re-show a previously hidden pivot item
    if (item.getName().equals("Item3"))
    {
        item.setHidden(false);
    }
}
// Refresh and recalculate the pivot table so changes take effect
pivotTable.getPivotCache().refresh();
// Save the workbook - hidden items stay in the underlying data
// but are excluded from the displayed pivot table output
workbook.save("output_pivot_filtered.xlsx");
```

## **ملخص**
يوفر Aspose.Cells for Java مجموعة كاملة من إمكانات تصفية الجداول المحورية المطابقة لتلك المتاحة في Microsoft Excel. تغطي مرشحات التسمية والتاريخ والقيمة أكثر السيناريوهات التحليلية شيوعًا، بينما يتولى مرشح أفضل 10 عناصر تقارير الترتيب. وعندما تكون قاعدة التصفية غير منتظمة، توفر الخاصية `PivotItem.IsHidden` حلًا احتياطيًا مرنًا على مستوى العنصر. وتتيح هذه الاستراتيجيات مجتمعةً، مثل تطبيق مرشح تسمية ثم إخفاء عناصر محددة، إنشاء تقارير جداول محورية دقيقة وموجهة بالكامل عبر التعليمات البرمجية.

## المقالات ذات الصلة
- [إدراج جدول محوري](/cells/ar/java/create-pivot-table/)
- [إضافة حقول الصفوف والأعمدة إلى جدول محوري في Aspose.Cells for Java](/cells/ar/java/pivot-table-add-row-and-column-fields/)
- [إضافة حقول التصفية إلى جدول محوري في Aspose.Cells for Java](/cells/ar/java/add-page-field-in-pivot-table/)
- [إدارة حقول القيمة في جدول محوري في Aspose.Cells for Java](/cells/ar/java/manage-value-fields/)
- [تحديث الجداول المحورية ومخازنها المؤقتة في Aspose.Cells for Java](/cells/ar/java/refresh-pivot-table/)

{{< app/cells/assistant language="java" >}}