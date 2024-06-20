---
title: تحليل السجلات المخزنة في حقول Pivot أثناء تحميل ملف Excel
type: docs
weight: 100
url: /ar/java/parsing-pivot-cached-records-while-loading-excel-file/
---

## **سيناريوهات الاستخدام المحتملة**

عند إنشاء جدول محوري، تقوم Microsoft Excel بنسخ البيانات المصدرية وتخزينها في ذاكرة التخزين المؤقت. تكون ذاكرة التخزين المؤقت موجودة داخل ذاكرة Microsoft Excel. لا يمكنك رؤيتها ولكن هذه هي البيانات التي يشير إليها الجدول المحوري عند بناء الجدول المحوري أو تغيير اختيار Slicer أو تحريك الصفوف/الأعمدة. يمكن لذلك Microsoft Excel أن يكون متجاوبًا جدًا مع التغييرات في الجدول المحوري ولكن يمكنه أيضًا مضاعفة حجم ملفك. بعد كل شيء، ذاكرة التخزين المؤقت مجرد نسخة مكررة من بياناتك المصدرية لذا يبدو منطقيًا أن يكون حجم ملفك مضاعف بشكل محتمل.

عند تحميل ملف Excel داخل كائن الورقة، يمكنك أن تقرر ما إذا كنت تريد أيضًا تحميل السجلات في ذاكرة التخزين المؤقت المحوري أم لا، باستخدام خاصية ([**LoadOptions.ParsingPivotCachedRecords**](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions#ParsingPivotCachedRecords)). القيمة الافتراضية لهذه الخاصية هي **false**. إذا كانت ذاكرة التخزين المؤقت كبيرة بما فيه الكفاية، فقد يزيد ذلك من الأداء. ولكن إذا كنت أيضًا تريد تحميل السجلات في ذاكرة التخزين المؤقت، يجب عليك ضبط هذه الخاصية على **true**.

## **تحليل السجلات المخزنة في حقول Pivot أثناء تحميل ملف Excel**

الكود عينة التالي يشرح استخدام خاصية ([**LoadOptions.ParsingPivotCachedRecords**](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions#ParsingPivotCachedRecords)). يقوم بتحميل ملف Excel العيني (61767786.xlsx) أثناء تحليل السجلات المخزنة في حقول Pivot. ثم يقوم بتحديث الجدول المحوري وحفظه كملف Excel الناتج (61767785.xlsx).

## **الكود المثالي**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "PivotTables-ParsingPivotCachedRecordsWhileLoadingExcelFile.java" >}}
