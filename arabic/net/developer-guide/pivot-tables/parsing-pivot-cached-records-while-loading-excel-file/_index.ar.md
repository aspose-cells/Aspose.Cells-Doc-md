---
title: تحليل السجلات المحورية المخزنة مؤقتًا أثناء تحميل ملف Excel
type: docs
weight: 70
url: /ar/net/parsing-pivot-cached-records-while-loading-excel-file/
---
## **سيناريوهات الاستخدام الممكنة**

عند إنشاء Pivot Table ، يأخذ Microsoft Excel نسخة من البيانات المصدر ويخزنها في Pivot Cache. يتم الاحتفاظ بـ Pivot Cache داخل ذاكرة Microsoft Excel. لا يمكنك رؤيته ولكن هذه هي البيانات التي يشير إليها Pivot Table عند إنشاء Pivot Table أو تغيير تحديد Slicer أو نقل الصفوف / الأعمدة حولها. يتيح ذلك لـ Microsoft Excel أن يكون سريع الاستجابة للتغييرات في Pivot Table ولكن يمكنه أيضًا مضاعفة حجم ملفك. بعد كل شيء ، تعد ذاكرة التخزين المؤقت Pivot مجرد نسخة مكررة من بيانات المصدر الخاصة بك ، لذا فمن المنطقي أن حجم ملفك سيتضاعف على الأرجح.

عند تحميل ملف Excel داخل كائن المصنف ، يمكنك تحديد ما إذا كنت تريد أيضًا تحميل سجلات ذاكرة التخزين المؤقت المحورية أم لا ، باستخدام[**LoadOptions.ParsingPivotCachedRecords**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/parsingpivotcachedrecords) منشأه. القيمة الافتراضية لهذه الخاصية هي**خاطئة** . إذا كانت ذاكرة التخزين المؤقت المحورية كبيرة جدًا ، فيمكنها زيادة الأداء. ولكن إذا كنت تريد أيضًا تحميل سجلات Pivot Cache ، فيجب عليك تعيين هذه الخاصية على أنها**حقيقي**.

## **تحليل السجلات المحورية المخزنة مؤقتًا أثناء تحميل ملف Excel**

يشرح نموذج التعليمات البرمجية التالي استخدام[**LoadOptions.ParsingPivotCachedRecords**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/parsingpivotcachedrecords) منشأه. يقوم بتحميل ملف[نموذج لملف Excel](61767773.xlsx) أثناء تحليل السجلات المخبأة المحورية. ثم يقوم بتحديث الجدول المحوري وحفظه كملف[إخراج ملف Excel](61767774.xlsx).

## **عينة من الرموز**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "PivotTables-ParsingPivotCachedRecordsWhileLoadingExcelFile.cs" >}}
