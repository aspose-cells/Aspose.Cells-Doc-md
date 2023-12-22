---
title: تحليل السجلات المحورية المخزنة مؤقتًا أثناء تحميل ملف Excel
type: docs
weight: 70
url: /ar/python-net/parsing-pivot-cached-records-while-loading-excel-file/
description: كيفية تحليل السجلات المحورية المخزنة مؤقتًا أثناء تحميل ملف Excel باستخدام Aspose.Cells for Python via .NET.
keywords: Parse Pivot Cached Records while loading Excel file.
---
##  **سيناريوهات الاستخدام المحتملة**

عندما تقوم بإنشاء جدول محوري، Microsoft يأخذ Excel نسخة من البيانات المصدر ويخزنها في Pivot Cache. يتم الاحتفاظ بذاكرة التخزين المؤقت المحورية داخل ذاكرة Microsoft Excel. لا يمكنك رؤيتها ولكن هذه هي البيانات التي يشير إليها Pivot Table عند إنشاء Pivot Table الخاص بك أو تغيير تحديد Slicer أو تحريك الصفوف/الأعمدة. يتيح ذلك لـ Microsoft Excel أن يكون سريع الاستجابة للتغييرات في Pivot Table ولكنه يمكنه أيضًا مضاعفة حجم ملفك. بعد كل شيء، تعد Pivot Cache مجرد نسخة مكررة من بيانات المصدر الخاصة بك، لذا فمن المنطقي أن يتضاعف حجم ملفك.

عندما تقوم بتحميل ملف Excel الخاص بك داخل كائن المصنف، يمكنك أن تقرر ما إذا كنت تريد أيضًا تحميل سجلات Pivot Cache أم لا، باستخدام[**LoadOptions.parsing_pivot_cached_records**](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions/parsing_pivot_cached_records/)ملكية. القيمة الافتراضية لهذه الخاصية هي كاذبة**. إذا كانت Pivot Cache كبيرة جدًا، فيمكنها زيادة الأداء. ولكن إذا كنت تريد أيضًا تحميل سجلات Pivot Cache، فيجب عليك تعيين هذه الخاصية على أنها *true**.

##  **تحليل السجلات المحورية المخزنة مؤقتًا أثناء تحميل ملف Excel**

يشرح نموذج التعليمات البرمجية التالي استخدام[**LoadOptions.parsing_pivot_cached_records**](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions/parsing_pivot_cached_records/)ملكية. يقوم بتحميل[عينة من ملف إكسل](61767773.xlsx) أثناء تحليل السجلات المحورية المخزنة مؤقتًا. ثم يقوم بتحديث الجدول المحوري وحفظه باسم[إخراج ملف إكسل](61767774.xlsx).

##  **عينة من الرموز**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-ParsingPivotCachedRecordsWhileLoadingExcelFile.py" >}}
