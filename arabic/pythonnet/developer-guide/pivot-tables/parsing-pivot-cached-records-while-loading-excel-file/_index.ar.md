---
title: تحليل السجلات المخزنة في حقول Pivot أثناء تحميل ملف Excel
type: docs
weight: 70
url: /ar/python-net/parsing-pivot-cached-records-while-loading-excel-file/
description: كيفية تحليل السجلات المخبأة للجدول المحوري أثناء تحميل ملف Excel باستخدام Aspose.Cells for Python via .NET.
keywords: Aspose.Cells for Python Excel، مكتبة Python Excel، كيفية تحليل السجلات المخبأة للجدول المحوري أثناء تحميل ملف Excel باستخدام مكتبة Aspose.Cells for Python Excel.
---

## **سيناريوهات الاستخدام المحتملة**

عند إنشاء جدول محوري، تقوم Microsoft Excel بنسخ البيانات المصدرية وتخزينها في ذاكرة التخزين المؤقت. تكون ذاكرة التخزين المؤقت موجودة داخل ذاكرة Microsoft Excel. لا يمكنك رؤيتها ولكن هذه هي البيانات التي يشير إليها الجدول المحوري عند بناء الجدول المحوري أو تغيير اختيار Slicer أو تحريك الصفوف/الأعمدة. يمكن لذلك Microsoft Excel أن يكون متجاوبًا جدًا مع التغييرات في الجدول المحوري ولكن يمكنه أيضًا مضاعفة حجم ملفك. بعد كل شيء، ذاكرة التخزين المؤقت مجرد نسخة مكررة من بياناتك المصدرية لذا يبدو منطقيًا أن يكون حجم ملفك مضاعف بشكل محتمل.

عندما تقوم بتحميل ملف الإكسل داخل كائن الدفتر، يمكنك أن تقرر ما إذا كنت تريد أيضًا تحميل سجلات التخزين المؤقت للجدول المحوري أم لا باستخدام خاصية [**LoadOptions.parsing_pivot_cached_records**](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions/parsing_pivot_cached_records/). القيمة الافتراضية لهذه الخاصية هي خاطئة. إذا كان تخزين المحور ضخمًا، فقد يزيد من الأداء. ولكن إذا كنت ترغب أيضًا في تحميل سجلات التخزين المؤقت للجدول المحوري، فيجب عليك ضبط هذه الخاصية على صواب.

## **كيفية تحليل السجلات المخبأة للجدول المحوري أثناء تحميل ملف Excel**

الكود العيني التالي يشرح استخدام خاصية [**LoadOptions.parsing_pivot_cached_records**](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions/parsing_pivot_cached_records/). يقوم بتحميل ملف الإكسل العيني مع تحليل السجلات المخزنة المحوري ثم يقوم بتحديث الجدول المحوري وحفظه كملف إكسل جديد.

## **الكود المثالي**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-ParsingPivotCachedRecordsWhileLoadingExcelFile.py" >}}
