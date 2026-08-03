---
title: تصفية الجداول المحورية حسب التسمية أو القيمة
linktitle: تصفية الجداول المحورية حسب التسمية أو القيمة
description: يدعم Aspose.Cells for Python via Java إمكانيات تصفية شاملة للجداول المحورية. توضح هذه المقالة كيفية تصفية بيانات الجدول المحوري باستخدام عوامل تصفية التسميات، وعوامل تصفية التاريخ، وعوامل تصفية القيم، وعوامل تصفية أعلى 10، ومن خلال إخفاء عناصر الجدول المحوري أو إظهارها.
keywords: Aspose.Cells, مكتبة Python via Java, جدول بيانات, جدول محوري, تصفية, تصفية حسب التسمية, تصفية حسب القيمة, تصفية حسب التاريخ, تصفية أعلى 10, عنصر محوري, إخفاء عنصر محوري
type: docs
weight: 10
url: /ar/python-java/filter-by-label-or-value-of-pivot-table/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---
```

Now the body:

The first alert:
"Aspose.Cells provides five practical strategies for filtering the data displayed in a pivot table. You can apply label filters to text-based row or column fields, use date filters when the field contains only date-time cells or blanks, apply value filters against aggregated numbers, use top 10 filters to rank by a value field, or manually hide and unhide individual pivot items using the `is_hidden` property. Each strategy is exposed through dedicated APIs on the `PivotField` and `PivotItem` classes."

Translation:
"يوفر Aspose.Cells خمس استراتيجيات عملية لتصفية البيانات المعروضة في الجدول المحوري. يمكنك تطبيق عوامل تصفية التسميات على الحقول النصية في الصفوف أو الأعمدة، واستخدام عوامل تصفية التاريخ عندما يحتوي الحقل على خلايا من نوع التاريخ والوقت فقط أو خلايا فارغة، وتطبيق عوامل تصفية القيم على الأرقام المجمعة، واستخدام عوامل تصفية أعلى 10 للترتيب حسب حقل قيمة، أو إخفاء وإظهار عناصر الجدول المحوري يدوياً باستخدام الخاصية `is_hidden`. تتوفر كل استراتيجية من خلال واجهات برمجية مخصصة في فئتي `PivotField` و `PivotItem`."

Now the Introduction:
"Pivot tables are powerful analytical tools, but raw summaries often contain far more information than you need to present. Filtering is the primary mechanism for narrowing a pivot table down to the rows, columns, or values that matter for a specific report. Aspose.Cells for Python via Java mirrors the filtering capabilities that are available in Microsoft Excel, exposing them programmatically so that report generation can be fully automated."

Translation:
"تعد الجداول المحورية أدوات تحليلية قوية، لكن الملخصات الخام غالبًا ما تحتوي على معلومات أكثر بكثير مما تحتاج إلى عرضه. التصفية هي الآلية الأساسية لتضييق نطاق الجدول المحوري على الصفوف أو الأعمدة أو القيم المهمة لتقرير معين. يعكس Aspose.Cells for Python via Java إمكانيات التصفية المتوفرة في Microsoft Excel، ويعرضها برمجيًا بحيث يمكن أتمتة إنشاء التقارير بالكامل."

"The following filtering strategies are covered in this article:"

Translation:
"تتناول هذه المقالة استراتيجيات التصفية التالية:"

List:
1. **Label Filter** — filters row or column field items based on their text labels.
2. **Date Filter** — filters row or column fields that contain only date-time values (or blanks).
3. **Value Filter** — filters items based on the aggregated values of a data field.
4. **Top 10 Filter** — shows only the top or bottom N items ranked by a value field.
5. **Hide / Unhide Pivot Items** — manually controls the visibility of each individual item in a field.

Translation:
1. **تصفية حسب التسمية** — تصفية عناصر حقل الصف أو العمود بناءً على تسمياتها النصية.
2. **تصفية حسب التاريخ** — تصفية حقول الصفوف أو الأعمدة التي تحتوي على قيم التاريخ والوقت فقط (أو خلايا فارغة).
3. **تصفية حسب القيمة** — تصفية العناصر بناءً على القيم المجمعة لحقل البيانات.
4. **تصفية أعلى 10** — تعرض فقط أعلى أو أدنى N عنصر مرتبة حسب حقل القيمة.
5. **إخفاء / إظهار عناصر الجدول المحوري** — التحكم يدويًا في إمكانية رؤية كل عنصر منفرد في الحقل.

"Each approach uses a different method on the `PivotField` class or a property on the `PivotItem` class. After applying any filter, you must call `refresh_data()` and `calculate_data()` on the pivot table so that the cached data and calculated values reflect the new filter state."

Translation:
"تستخدم كل طريقة أسلوبًا مختلفًا في فئة `PivotField` أو خاصية في فئة `PivotItem`. بعد تطبيق أي عامل تصفية، يجب استدعاء `refresh_data()` و `calculate_data()` على الجدول المحوري بحيث تعكس البيانات المخزنة مؤقتًا والقيم المحسوبة حالة عامل التصفية الجديد."

```
## Label Filter

"A label filter allows you to filter the items of a row or column field by comparing their text captions against a pattern. This is useful when you want to display only products whose names start with a specific letter, contain a particular word, or match some other caption-based criterion."

"تتيح لك تصفية التسمية تصفية عناصر حقل الصف أو العمود بمقارنة تسمياتها النصية بنمط معين. يكون هذا مفيدًا عندما تريد عرض المنتجات التي تبدأ أسماؤها بحرف معين فقط، أو التي تحتوي على كلمة معينة، أو التي تطابق أي معيار آخر قائم على التسمية."

"Aspose.Cells exposes label filtering through the `PivotField.filter_by_label(PivotFilterType, str)` method. The `PivotFilterType` enumeration includes values such as `CaptionBeginsWith`, `CaptionContains`, `CaptionEndsWith`, `CaptionDoesNotContain`, `CaptionIsNotBlank`, `CaptionIsBlank`, and so on. The second argument supplies the label string used للمقارنة."

"يعرض Aspose.Cells تصفية التسميات من خلال الأسلوب `PivotField.filter_by_label(PivotFilterType, str)`. يتضمن تعداد `PivotFilterType` قيمًا مثل `CaptionBeginsWith` و `CaptionContains` و `CaptionEndsWith` و `CaptionDoesNotContain` و `CaptionIsNotBlank` و `CaptionIsBlank` وغيرها. يوفر الوسيط الثاني سلسلة التسمية المستخدمة للمقارنة."

"The following example loads a workbook containing an existing pivot table, applies a label filter so that only items whose captions begin with a specified prefix remain visible, refreshes the pivot table, and saves the result."

"يحمل المثال التالي مصنفًا يحتوي على جدول محوري موجود، ويطبق تصفية تسمية بحيث تظل العناصر التي تبدأ تسمياتها ببادئة محددة فقط مرئية، ثم يُحدّث الجدول المحوري ويحفظ النتيجة."

## Date Filter

"Date filters let you narrow a pivot table by date-based criteria such as today, last week, this month, next quarter, or a specific date range. They are specialized filters that work only against fields that store date-time information."

"تتيح لك عوامل تصفية التاريخ تضييق نطاق الجدول المحوري وفقًا لمعايير تستند إلى التاريخ مثل اليوم، أو الأسبوع الماضي، أو هذا الشهر، أو الربع القادم، أو نطاق تاريخي محدد. وهي عوامل تصفية متخصصة تعمل فقط مع الحقول التي تخزن معلومات التاريخ والوقت."

Alert:
"The date filter only works when the row or column area contains only date-time cells or blank values. If the underlying field contains other data types such as numbers or text, the date filter will not produce the expected result. Make sure the field is formatted as a date and that all values are valid `DateTime` instances or empty cells before applying this filter."

"لا يعمل عامل تصفية التاريخ إلا عندما تحتوي منطقة الصف أو العمود على خلايا من نوع التاريخ والوقت فقط أو خلايا فارغة. إذا كان الحقل الأساسي يحتوي على أنواع بيانات أخرى مثل الأرقام أو النصوص، فلن ينتج عن عامل تصفية التاريخ النتيجة المتوقعة. تأكد من تنسيق الحقل كتاريخ ومن أن جميع القيم هي نسخ صالحة من `DateTime` أو خلايا فارغة قبل تطبيق هذا العامل."

"Aspose.Cells exposes date filtering through the `PivotField.filter_by_date(PivotFilterType, values)` method. The `PivotFilterType` enumeration contains dedicated date values such as `Today`, `Yesterday`, `LastWeek`, `ThisWeek`, `NextWeek`, `LastMonth`, `ThisMonth`, `NextMonth`, `LastQuarter`, `ThisQuarter`, `NextQuarter`, `LastYear`, `ThisYear`, `NextYear`, and `Between`. Depending on the chosen filter type, you pass one or two `DateTime` values (for `Between`, you pass the start and end dates)."

"يعرض Aspose.Cells تصفية التاريخ من خلال الأسلوب `PivotField.filter_by_date(PivotFilterType, values)`. يحتوي تعداد `PivotFilterType` على قيم تاريخ مخصصة مثل `Today` و `Yesterday` و `LastWeek` و `ThisWeek` و `NextWeek` و `LastMonth` و `ThisMonth` و `NextMonth` و `LastQuarter` و `ThisQuarter` و `NextQuarter` و `LastYear` و `ThisYear` و `NextYear` و `Between`. بناءً على نوع التصفية المختار، تمرر قيمة واحدة أو قيمتي `DateTime` (بالنسبة إلى `Between`، تمرر تاريخي البداية والنهاية)."

"The following example loads a workbook with a pivot table whose row area contains a date field, applies a date filter that restricts the visible items to a particular date range, refreshes the pivot table, and saves the workbook."

"يحمل المثال التالي مصنفًا يحتوي على جدول محوري توجد في منطقة الصفوف فيه حقل تاريخ، ويطبق تصفية تاريخ تقصر العناصر المرئية على نطاق تاريخي معين، ثم يُحدّث الجدول المحوري ويحفظ المصنف."

## Value Filter

"Value filters operate on the aggregated values that a pivot table calculates in its data area. Instead of matching text labels, they compare numeric totals against a threshold. Typical use cases include showing only products whose sum of sales exceeds a target amount or only regions whose count of transactions falls within a range."

"تعمل عوامل تصفية القيم على القيم المجمعة التي يحسبها الجدول المحوري في منطقة البيانات الخاصة به. وبدلاً من مطابقة التسميات النصية، فإنها تقارن الإجماليات الرقمية بحد معين. تشمل حالات الاستخدام النموذجية عرض المنتجات التي يتجاوز مجموع مبيعاتها مبلغًا مستهدفًا فقط، أو المناطق التي يقع عدد معاملاتها ضمن نطاق معين فقط."

"Aspose.Cells exposes value filtering through the `PivotField.filter_by_value(value_field, filter_type, values)` method. The `filter_type` parameter uses values such as `ValueGreaterThan`, `ValueLessThan`, `ValueBetween`, `ValueEqual`, `ValueNotEqual`, `ValueGreaterThanOrEqual`, and `ValueLessThanOrEqual`. The `value_field` parameter specifies which data field should be evaluated, and the final argument(s) supply the threshold value(s)."

"يعرض Aspose.Cells تصفية القيم من خلال الأسلوب `PivotField.filter_by_value(value_field, filter_type, values)`. تستخدم وسيطة `filter_type` قيمًا مثل `ValueGreaterThan` و `ValueLessThan` و `ValueBetween` و `ValueEqual` و `ValueNotEqual` و `ValueGreaterThanOrEqual` و `ValueLessThanOrEqual`. تحدد وسيطة `value_field` حقل البيانات الذي يجب تقييمه، بينما توفر الوسيطات النهائية قيمة أو قيم الحد."

"The following example loads a workbook with a pivot table, applies a value filter that keeps only items whose aggregated sales exceed a numeric threshold, refreshes the pivot table, and saves the workbook."

"يحمل المثال التالي مصنفًا يحتوي على جدول محوري، ويطبق تصفية قيم تحتفظ فقط بالعناصر التي تتجاوز مبيعاتها المجمعة حدًا رقميًا، ثم يُحدّث الجدول المحوري ويحفظ المصنف."

## Top 10 Filter

"The top 10 filter is a specialized form of value filter that retains only the highest or lowest N items based on a chosen value field. It is commonly used for ranking reports such as "top 10 products by revenue" or "bottom 5 regions by sales count"."

"تُعد تصفية أعلى 10 شكلًا متخصصًا من تصفية القيم تحتفظ فقط بأعلى أو أدنى N عنصر بناءً على حقل قيمة مختار. تُستخدم عادةً لتقارير الترتيب مثل "أفضل 10 منتجات من حيث الإيرادات" أو "أسوأ 5 مناطق من حيث عدد المبيعات"."

Alert:
"The top 10 filter is only effective when the pivot table has one or more value pivot fields in the data area. Without at least one value field, there is no aggregated measure to rank the items against, and the filter cannot be applied."

"لا تكون تصفية أعلى 10 فعالة إلا عندما يحتوي الجدول المحوري على حقل قيمة واحد أو أكثر في منطقة البيانات. فبدون وجود حقل قيمة واحد على الأقل، لن يكون هناك مقياس مجمع لترتيب العناصر وفقًا له، ولا يمكن تطبيق عامل التصفية."

"Aspose.Cells exposes top 10 filtering through the `PivotField.filter_top10(item_count, is_top, value_field, filter_type)` method. The `item_count` parameter defines how many items to retain, `is_top` indicates whether to keep the top items (true) or the bottom items (false), `value_field` references the data field used for ranking, and `filter_type` controls how the value is computed (typically `Sum`, but also `Count` and `Percent`)."

"يعرض Aspose.Cells تصفية أعلى 10 من خلال الأسلوب `PivotField.filter_top10(item_count, is_top, value_field, filter_type)`. تحدد وسيطة `item_count` عدد العناصر التي يجب الاحتفاظ بها، وتشير `is_top` إلى ما إذا كان سيتم الاحتفاظ بأعلى العناصر (true) أو أدنى العناصر (false)، ويُشير `value_field` إلى حقل البيانات المستخدم للترتيب، ويتحكم `filter_type` في كيفية حساب القيمة (عادةً `Sum`، ولكن أيضًا `Count` و `Percent`)."

"The following example loads a workbook with a pivot table that contains a value field, applies a top 10 filter to keep only the highest 10 items by the sum of sales, refreshes the pivot table, and saves the workbook."

"يحمل المثال التالي مصنفًا يحتوي على جدول محوري يتضمن حقل قيمة، ويطبق تصفية أعلى 10 للاحتفاظ فقط بأعلى 10 عناصر من حيث مجموع المبيعات، ثم يُحدّث الجدول المحوري ويحفظ المصنف."

## Filter by Hiding or Unhiding Pivot Items

"In addition to the structured filter APIs, Aspose.Cells allows you to control the visibility of each individual pivot item directly. By iterating through the `PivotItems` collection of a `PivotField` and toggling the `is_hidden` property, you can selectively suppress specific items without applying a formula-based filter. Setting `is_hidden = True` hides the item from the pivot table; setting `is_hidden = False` unhides it and makes it visible again."

"بالإضافة إلى واجهات التصفية المنظمة، يتيح لك Aspose.Cells التحكم مباشرةً في إمكانية رؤية كل عنصر محوري منفرد. ومن خلال التكرار في مجموعة `PivotItems` الخاصة بـ `PivotField` وتبديل الخاصية `is_hidden`، يمكنك منع ظهور عناصر محددة بشكل انتقائي دون تطبيق تصفية قائمة على الصيغ. يؤدي تعيين `is_hidden = True` إلى إخفاء العنصر من الجدول المحوري، بينما يؤدي تعيين `is_hidden = False` إلى إظهاره مرة أخرى وجعله مرئيًا."

"This approach is useful when the filtering rule is irregular or item-specific, such as hiding a small number of named categories that should not appear in a particular report. The example below loads a pivot table, hides a specific item by name, demonstrates how to unhide it, refreshes the pivot table, and saves the workbook."

"يكون هذا الأسلوب مفيدًا عندما تكون قاعدة التصفية غير منتظمة أو خاصة بعنصر معين، مثل إخفاء عدد صغير من الفئات المسماة التي يجب ألا تظهر في تقرير معين. يحمّل المثال التالي جدولًا محوريًا، ويخفي عنصرًا محددًا بالاسم، ويوضح كيفية إظهاره مرة أخرى، ثم يُحدّث الجدول المحوري ويحفظ المصنف."

## Summary

"Aspose.Cells for Python via Java provides a complete set of pivot table filtering capabilities that match those found in Microsoft Excel. Label, date, and value filters cover the most common analytical scenarios, while the top 10 filter handles ranking reports. When the filtering rule is irregular, the `PivotItem.is_hidden` property offers a flexible, item-level fallback. Combining these strategies — for example, applying a label filter and then hiding specific items — allows you to build precisely targeted pivot table reports entirely from code."

"يوفر Aspose.Cells for Python via Java مجموعة كاملة من إمكانيات تصفية الجداول المحورية التي تطابق تلك المتوفرة في Microsoft Excel. تغطي عوامل تصفية التسميات والتاريخ والقيم السيناريوهات التحليلية الأكثر شيوعًا، بينما تتعامل تصفية أعلى 10 مع تقارير الترتيب. عندما تكون قاعدة التصفية غير منتظمة، توفر الخاصية `PivotItem.is_hidden` بديلاً مرنًا على مستوى العناصر. يتيح لك الجمع بين هذه الاستراتيجيات — على سبيل المثال، تطبيق تصفية تسمية ثم إخفاء عناصر محددة — إنشاء تقارير جدول محوري مستهدفة بدقة بالكامل من خلال التعليمات البرمجية."
I need to translate the captions for the related articles. The URLs stay the same.

- [إدراج جدول محوري](/cells/ar/python-java/pivot-tables/)
- [إضافة حقول الصفوف والأعمدة في Aspose.Cells for Python via Java](/cells/ar/python-java/pivot-table-add-row-and-column-fields/)
- [إضافة حقول التصفية إلى جدول محوري في Aspose.Cells for Python via Java](/cells/ar/python-java/add-page-field-in-pivot-table/)
- [إدارة حقول القيم في Aspose.Cells for Python via Java](/cells/ar/python-java/manage-value-fields/)
- [تحديث الجداول المحورية والتخزينات المؤقتة في Aspose.Cells for Python via Java](/cells/ar/python-java/refresh-pivot-table/)

"Aspose.Cells for Python via Java supports comprehensive pivot table filtering capabilities. This article explains how to filter pivot table data using label filters, date filters, value filters, top 10 filters, and by hiding or unhiding pivot items."

"يدعم Aspose.Cells for Python via Java إمكانيات تصفية شاملة للجداول المحورية. توضح هذه المقالة كيفية تصفية بيانات الجدول المحوري باستخدام عوامل تصفية التسميات، وعوامل تصفية التاريخ، وعوامل تصفية القيم، وعوامل تصفية أعلى 10، ومن خلال إخفاء عناصر الجدول المحوري أو إظهارها."

No colons. Good.

- Frontmatter keys are in English
- Title, description, keywords are translated
- type, weight, url are unchanged
- 5 code block placeholders preserved
- All Hugo shortcodes preserved
- No thinking/reasoning output
- No dual-language paragraphs
- Start with --- delimiter

{{% alert color="primary" %}}

يوفر Aspose.Cells خمس استراتيجيات عملية لتصفية البيانات المعروضة في الجدول المحوري. يمكنك تطبيق عوامل تصفية التسميات على الحقول النصية في الصفوف أو الأعمدة، واستخدام عوامل تصفية التاريخ عندما يحتوي الحقل على خلايا من نوع التاريخ والوقت فقط أو خلايا فارغة، وتطبيق عوامل تصفية القيم على الأرقام المجمعة، واستخدام عوامل تصفية أعلى 10 للترتيب حسب حقل قيمة، أو إخفاء وإظهار عناصر الجدول المحوري يدويًا باستخدام الخاصية `is_hidden`. تتوفر كل استراتيجية من خلال واجهات برمجية مخصصة في فئتي `PivotField` و `PivotItem`.

{{% /alert %}}

## **Introduction**

تُعد الجداول المحورية أدوات تحليلية قوية، لكن الملخصات الخام غالبًا ما تحتوي على معلومات أكثر بكثير مما تحتاج إلى عرضه. التصفية هي الآلية الأساسية لتضييق نطاق الجدول المحوري على الصفوف أو الأعمدة أو القيم المهمة لتقرير معين. يعكس Aspose.Cells for Python via Java إمكانيات التصفية المتوفرة في Microsoft Excel، ويعرضها برمجيًا بحيث يمكن أتمتة إنشاء التقارير بالكامل.

تتناول هذه المقالة استراتيجيات التصفية التالية:

1. **تصفية حسب التسمية** — تصفية عناصر حقل الصف أو العمود بناءً على تسمياتها النصية.
2. **تصفية حسب التاريخ** — تصفية حقول الصفوف أو الأعمدة التي تحتوي على قيم التاريخ والوقت فقط (أو خلايا فارغة).
3. **تصفية حسب القيمة** — تصفية العناصر بناءً على القيم المجمعة لحقل البيانات.
4. **تصفية أعلى 10** — تعرض فقط أعلى أو أدنى N عنصر مرتبة حسب حقل القيمة.
5. **إخفاء / إظهار عناصر الجدول المحوري** — التحكم يدويًا في إمكانية رؤية كل عنصر منفرد في الحقل.

تستخدم كل طريقة أسلوبًا مختلفًا في فئة `PivotField` أو خاصية في فئة `PivotItem`. بعد تطبيق أي عامل تصفية، يجب استدعاء `refresh_data()` و `calculate_data()` على الجدول المحوري بحيث تعكس البيانات المخزنة مؤقتًا والقيم المحسوبة حالة عامل التصفية الجديد.

## **Label Filter**

تتيح لك تصفية التسمية تصفية عناصر حقل الصف أو العمود بمقارنة تسمياتها النصية بنمط معين. يكون هذا مفيدًا عندما تريد عرض المنتجات التي تبدأ أسماؤها بحرف معين فقط، أو التي تحتوي على كلمة معينة، أو التي تطابق أي معيار آخر قائم على التسمية.

يعرض Aspose.Cells تصفية التسميات من خلال الأسلوب `PivotField.filter_by_label(PivotFilterType, str)`. يتضمن تعداد `PivotFilterType` قيمًا مثل `CaptionBeginsWith` و `CaptionContains` و `CaptionEndsWith` و `CaptionDoesNotContain` و `CaptionIsNotBlank` و `CaptionIsBlank` وغيرها. توفر الوسيطة الثانية سلسلة التسمية المستخدمة للمقارنة.

يحمل المثال التالي مصنفًا يحتوي على جدول محوري موجود، ويطبق تصفية تسمية بحيث تظل العناصر التي تبدأ تسمياتها ببادئة محددة فقط مرئية، ثم يُحدّث الجدول المحوري ويحفظ النتيجة.

```python
asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, PivotFilterType

fileName = "sample.xlsx"
prefix = "B"

# تحميل المصنف الحالي الذي يحتوي على جدول محوري
workbook = Workbook(fileName)

# الوصول إلى ورقة العمل حسب الفهرس (ورقة العمل الأولى)
worksheet = workbook.getWorksheets().get(0)

# الوصول إلى الجدول المحوري حسب الفهرس
pivotTable = worksheet.getPivotTables().get(0)

# استرداد حقل الصف الأول من الجدول المحوري
rowField = pivotTable.getRowFields().get(0)

# تطبيق مرشح التسمية — إظهار عناصر الصفوف التي تبدأ تسمياتها بالبادئة المقدمة فقط
rowField.filterByLabel(PivotFilterType.CaptionBeginsWith, prefix, "")

# تحديث وإعادة حساب بيانات الجدول المحوري حتى يسري مفعول المرشح
pivotTable.getPivotCache().refresh()

# حفظ المصنف مرة أخرى على القرص
workbook.save(fileName)

jpype.shutdownJVM()
```

## **Date Filter**

تتيح لك عوامل تصفية التاريخ تضييق نطاق الجدول المحوري وفقًا لمعايير تستند إلى التاريخ مثل اليوم، أو الأسبوع الماضي، أو هذا الشهر، أو الربع القادم، أو نطاق تاريخي محدد. وهي عوامل تصفية متخصصة تعمل فقط مع الحقول التي تخزن معلومات التاريخ والوقت.

{{% alert color="primary" %}}

لا يعمل عامل تصفية التاريخ إلا عندما تحتوي منطقة الصف أو العمود على خلايا من نوع التاريخ والوقت فقط أو خلايا فارغة. إذا كان الحقل الأساسي يحتوي على أنواع بيانات أخرى مثل الأرقام أو النصوص، فلن ينتج عن عامل تصفية التاريخ النتيجة المتوقعة. تأكد من تنسيق الحقل كتاريخ ومن أن جميع القيم هي نسخ صالحة من `DateTime` أو خلايا فارغة قبل تطبيق هذا العامل.

{{% /alert %}}

يعرض Aspose.Cells تصفية التاريخ من خلال الأسلوب `PivotField.filter_by_date(PivotFilterType, values)`. يحتوي تعداد `PivotFilterType` على قيم تاريخ مخصصة مثل `Today` و `Yesterday` و `LastWeek` و `ThisWeek` و `NextWeek` و `LastMonth` و `ThisMonth` و `NextMonth` و `LastQuarter` و `ThisQuarter` و `NextQuarter` و `LastYear` و `ThisYear` و `NextYear` و `Between`. بناءً على نوع التصفية المختار، تمرر قيمة واحدة أو قيمتي `DateTime` (بالنسبة إلى `Between`، تمرر تاريخي البداية والنهاية).

يحمل المثال التالي مصنفًا يحتوي على جدول محوري توجد في منطقة الصفوف فيه حقل تاريخ، ويطبق تصفية تاريخ تقصر العناصر المرئية على نطاق تاريخي معين، ثم يُحدّث الجدول المحوري ويحفظ المصنف.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, PivotFilterType

inputPath = "sample.xlsx"
outputPath = "output_filtered.xlsx"

if not os.path.exists(inputPath):
    raise FileNotFoundError(f"Source workbook not found: {inputPath}")

# تحميل مصنف العمل الحالي الذي يحتوي على الجدول المحوري
workbook = Workbook(inputPath)

# الوصول إلى ورقة العمل التي تحتوي على الجدول المحوري (بالفهرس)
worksheet = workbook.getWorksheets().get(0)

# الوصول إلى الجدول المحوري بالفهرس
pivotTable = worksheet.getPivotTables().get(0)

# استرجاع حقل التاريخ المحوري من منطقة الصفوف
# (يعمل مرشح التاريخ فقط عندما تحتوي منطقة الصف/العمود على خلايا تاريخ-وقت فقط أو فارغة)
dateField = pivotTable.getRowFields().get(0)

# تحديد معيار التاريخ لمرشح بين
Date = jpype.JClass("java.util.Date")
startDate = Date(2020 - 1900, 0, 1)
endDate = Date(2020 - 1900, 11, 31)

# تطبيق مرشح التاريخ على الحقل المحوري
dateField.filterByDate(PivotFilterType.DateBetween, startDate, endDate)

# تحديث وإعادة حساب الجدول المحوري حتى يسري المرشح
pivotTable.getPivotCache().refresh()

# حفظ مصنف العمل
workbook.save(outputPath)

jpype.shutdownJVM()
```

## **Value Filter**

تعمل عوامل تصفية القيم على القيم المجمعة التي يحسبها الجدول المحوري في منطقة البيانات الخاصة به. وبدلاً من مطابقة التسميات النصية، فإنها تقارن الإجماليات الرقمية بحد معين. تشمل حالات الاستخدام النموذجية عرض المنتجات التي يتجاوز مجموع مبيعاتها مبلغًا مستهدفًا فقط، أو المناطق التي يقع عدد معاملاتها ضمن نطاق معين فقط.

يعرض Aspose.Cells تصفية القيم من خلال الأسلوب `PivotField.filter_by_value(value_field, filter_type, values)`. تستخدم وسيطة `filter_type` قيمًا مثل `ValueGreaterThan` و `ValueLessThan` و `ValueBetween` و `ValueEqual` و `ValueNotEqual` و `ValueGreaterThanOrEqual` و `ValueLessThanOrEqual`. تحدد وسيطة `value_field` حقل البيانات الذي يجب تقييمه، بينما توفر الوسيطات النهائية قيمة أو قيم الحد.

يحمل المثال التالي مصنفًا يحتوي على جدول محوري، ويطبق تصفية قيم تحتفظ فقط بالعناصر التي تتجاوز مبيعاتها المجمعة حدًا رقميًا، ثم يُحدّث الجدول المحوري ويحفظ المصنف.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, PivotFilterType

workbook = Workbook("sample.xlsx")
worksheet = workbook.getWorksheets().get(0)
pivotTable = worksheet.getPivotTables().get(0)

rowField = pivotTable.getRowFields().get(0)
dataField = pivotTable.getDataFields().get(0)

# البحث عن فهرس حقل البيانات يدويًا نظرًا لأن PivotFieldCollection لا يحتوي على IndexOf
dataFieldIndex = -1
for i in range(pivotTable.getDataFields().getCount()):
    if pivotTable.getDataFields().get(i) == dataField:
        dataFieldIndex = i
        break

if dataFieldIndex >= 0:
    rowField.filterByValue(dataFieldIndex, PivotFilterType.VALUE_GREATER_THAN, 5000, float('inf'))

pivotTable.getPivotCache().refresh()

workbook.save("output.xlsx")

jpype.shutdownJVM()
```

## **Top 10 Filter**

تُعد تصفية أعلى 10 شكلًا متخصصًا من تصفية القيم تحتفظ فقط بأعلى أو أدنى N عنصر بناءً على حقل قيمة مختار. تُستخدم عادةً لتقارير الترتيب مثل "أفضل 10 منتجات من حيث الإيرادات" أو "أسوأ 5 مناطق من حيث عدد المبيعات".

{{% alert color="primary" %}}

لا تكون تصفية أعلى 10 فعالة إلا عندما يحتوي الجدول المحوري على حقل قيمة واحد أو أكثر في منطقة البيانات. فبدون وجود حقل قيمة واحد على الأقل، لن يكون هناك مقياس مجمع لترتيب العناصر وفقًا له، ولا يمكن تطبيق عامل التصفية.

{{% /alert %}}

يعرض Aspose.Cells تصفية أعلى 10 من خلال الأسلوب `PivotField.filter_top10(item_count, is_top, value_field, filter_type)`. تحدد وسيطة `item_count` عدد العناصر التي يجب الاحتفاظ بها، وتشير `is_top` إلى ما إذا كان سيتم الاحتفاظ بأعلى العناصر (true) أو أدنى العناصر (false)، ويُشير `value_field` إلى حقل البيانات المستخدم للترتيب، ويتحكم `filter_type` في كيفية حساب القيمة (عادةً `Sum`، ولكن أيضًا `Count` و `Percent`).

يحمل المثال التالي مصنفًا يحتوي على جدول محوري يتضمن حقل قيمة، ويطبق تصفية أعلى 10 للاحتفاظ فقط بأعلى 10 عناصر من حيث مجموع المبيعات، ثم يُحدّث الجدول المحوري ويحفظ المصنف.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, PivotTable, PivotField, PivotFilterType

# تحميل ملف العمل الموجود الذي يحتوي على الجدول المحوري
inputPath = "input.xlsx"
outputPath = "output.xlsx"
workbook = Workbook(inputPath)

# الوصول إلى ورقة العمل التي تحتوي على الجدول المحوري (الفهرس 0)
worksheet = workbook.getWorksheets().get(0)

# الوصول إلى الجدول المحوري عن طريق الفهرس
pivotTable = worksheet.getPivotTables().get(0)

# التأكد من وجود حقل قيمة واحد على الأقل في منطقة البيانات
if pivotTable.getDataFields().getCount() == 0:
    raise Exception("Pivot table has no value (data) PivotField.")
valueField = pivotTable.getDataFields().get(0)

# استرداد حقل الصف المستهدف (الحقل الذي نريد تطبيق أعلى 10 عليه)
rowField = pivotTable.getRowFields().get(0)

# حقل البيانات الأول (والوحيد) يقع في الفهرس 0؛ يتم الترتيب حسبه في أعلى 10
valueFieldIndex = 0

# تطبيق مرشح أعلى 10 على حقل الصف:
#   - itemCount   = 10
#   - filterType  = PivotFilterType.Sum
#   - isTop       = true (أعلى N؛ false تعني أسفل N)
#   - valueFieldIndex = فهرس حقل البيانات المستخدم لترتيب العناصر
rowField.filterTop10(10, PivotFilterType.Sum, True, valueFieldIndex)

# تحديث بيانات الجدول المحوري وإعادة حسابه حتى يتم تطبيق المرشح
pivotTable.getPivotCache().refresh()

# حفظ ملف العمل
workbook.save(outputPath)

jpype.shutdownJVM()
```

## **Filter by Hiding or Unhiding Pivot Items**

بالإضافة إلى واجهات التصفية المنظمة، يتيح لك Aspose.Cells التحكم مباشرةً في إمكانية رؤية كل عنصر محوري منفرد. ومن خلال التكرار في مجموعة `PivotItems` الخاصة بـ `PivotField` وتبديل الخاصية `is_hidden`، يمكنك منع ظهور عناصر محددة بشكل انتقائي دون تطبيق تصفية قائمة على الصيغ. يؤدي تعيين `is_hidden = True` إلى إخفاء العنصر من الجدول المحوري، بينما يؤدي تعيين `is_hidden = False` إلى إظهاره مرة أخرى وجعله مرئيًا.

يكون هذا الأسلوب مفيدًا عندما تكون قاعدة التصفية غير منتظمة أو خاصة بعنصر معين، مثل إخفاء عدد صغير من الفئات المسماة التي يجب ألا تظهر في تقرير معين. يحمّل المثال التالي جدولًا محوريًا، ويخفي عنصرًا محددًا بالاسم، ويوضح كيفية إظهاره مرة أخرى، ثم يُحدّث الجدول المحوري ويحفظ المصنف.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotTable, PivotField, PivotItem

# تحميل مصنف موجود يحتوي على جدول محوري
workbook = Workbook("pivot_table_sample.xlsx")

# الوصول إلى ورقة العمل الأولى التي تحتوي على الجدول المحوري
sheet = workbook.getWorksheets().get(0)

# الوصول إلى الجدول المحوري بواسطة الفهرس (الجدول المحوري الأول في الورقة)
pivotTable = sheet.getPivotTables().get(0)

# استرجاع حقل PivotField المستهدف (حقل تسمية الصف الأول الذي سنخفي/نظهر عناصره فيه)
pivotField = pivotTable.getRowFields().get(0)

# التكرار من خلال مجموعة PivotItems الخاصة بـ PivotField المحدد
itemCount = pivotField.getPivotItems().getCount()
for i in range(itemCount):
    item = pivotField.getPivotItems().get(i)

    # إخفاء عناصر الجدول المحوري التي تطابق اسم/معيار معين
    if item.getName() == "Item1" or item.getName() == "Item2":
        item.setIsHidden(True)

    # إظهار عنصر محوري مخفي سابقاً لإثبات إمكانية إلغاء الإخفاء
    if item.getName() == "Item3":
        item.setIsHidden(False)

# تحديث وإعادة حساب الجدول المحوري حتى تسري التغييرات
pivotTable.getPivotCache().refresh()

# حفظ المصنف — العناصر المخفية تبقى في البيانات الأساسية
# لكنها تُستبعد من مخرجات الجدول المحوري المعروضة
workbook.save("output_pivot_filtered.xlsx")

jpype.shutdownJVM()
```

## **Summary**

يوفر Aspose.Cells for Python via Java مجموعة كاملة من إمكانيات تصفية الجداول المحورية التي تطابق تلك المتوفرة في Microsoft Excel. تغطي عوامل تصفية التسميات والتاريخ والقيم السيناريوهات التحليلية الأكثر شيوعًا، بينما تتعامل تصفية أعلى 10 مع تقارير الترتيب. عندما تكون قاعدة التصفية غير منتظمة، توفر الخاصية `PivotItem.is_hidden` بديلاً مرنًا على مستوى العناصر. يتيح لك الجمع بين هذه الاستراتيجيات — على سبيل المثال، تطبيق تصفية تسمية ثم إخفاء عناصر محددة — إنشاء تقارير جدول محوري مستهدفة بدقة بالكامل من خلال التعليمات البرمجية.
{{< app/cells/assistant language="python" >}}