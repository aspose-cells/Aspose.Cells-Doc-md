---
title: تحليل السجلات المخزنة في حقول Pivot أثناء تحميل ملف Excel
type: docs
weight: 70
url: /ar/net/parsing-pivot-cached-records-while-loading-excel-file/
---

## **سيناريوهات الاستخدام المحتملة**

عند إنشاء جدول محوري، تقوم Microsoft Excel بنسخ البيانات المصدرية وتخزينها في ذاكرة التخزين المؤقت. تكون ذاكرة التخزين المؤقت موجودة داخل ذاكرة Microsoft Excel. لا يمكنك رؤيتها ولكن هذه هي البيانات التي يشير إليها الجدول المحوري عند بناء الجدول المحوري أو تغيير اختيار Slicer أو تحريك الصفوف/الأعمدة. يمكن لذلك Microsoft Excel أن يكون متجاوبًا جدًا مع التغييرات في الجدول المحوري ولكن يمكنه أيضًا مضاعفة حجم ملفك. بعد كل شيء، ذاكرة التخزين المؤقت مجرد نسخة مكررة من بياناتك المصدرية لذا يبدو منطقيًا أن يكون حجم ملفك مضاعف بشكل محتمل.

عندما تقوم بتحميل ملف الإكسل داخل كائن الدفتر، يمكنك أن تقرر ما إذا كنت تريد أيضًا تحميل سجلات التخزين المؤقت للجدول المحوري أم لا باستخدام خاصية [**LoadOptions.ParsingPivotCachedRecords**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/parsingpivotcachedrecords). القيمة الافتراضية لهذه الخاصية هي خاطئة. إذا كان تخزين المحور ضخمًا، فقد يزيد من الأداء. ولكن إذا كنت ترغب أيضًا في تحميل سجلات التخزين المؤقت للجدول المحوري، فيجب عليك ضبط هذه الخاصية على صواب.

## **تحليل السجلات المخزنة في حقول Pivot أثناء تحميل ملف Excel**

الكود العيني التالي يشرح استخدام خاصية [**LoadOptions.ParsingPivotCachedRecords**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/parsingpivotcachedrecords). يقوم بتحميل ملف الإكسل العيني مع تحليل السجلات المخزنة المحوري ثم يقوم بتحديث الجدول المحوري وحفظه كملف إكسل جديد.

## **الكود المثالي**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "PivotTables-ParsingPivotCachedRecordsWhileLoadingExcelFile.cs" >}}
{{< app/cells/assistant language="csharp" >}}
