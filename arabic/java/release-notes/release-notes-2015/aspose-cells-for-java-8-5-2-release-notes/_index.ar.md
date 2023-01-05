---
title: Aspose.Cells for Java 8.5.2 ملاحظات الإصدار
type: docs
weight: 30
url: /ar/java/aspose-cells-for-java-8-5-2-release-notes/
---
{{% alert color="primary" %}} 

 تحتوي هذه الصفحة على ملاحظات الإصدار لـ[Aspose.Cells for Java 8.5.2](https://downloads.aspose.com/cells/java/new-releases/aspose.cells-for-java-8.5.2/)

{{% /alert %}} 

 فيما يلي قائمة بالتحسينات والتغييرات في هذا الإصدار من Aspose.Cells



\1) Aspose.Cells 


## **تحسينات وتغييرات أخرى**

## **ميزات جديدة**


 (CELLSJAVA-41374) - إضافة "عدد مميز" ثابت لفئة ConsolidationFunction في الجداول المحورية


## **التحسينات**


 (CELLSJAVA-41373) - عدم تطابق في إعدادات المحاذاة بعد حفظ ملف Excel بتنسيق ملف HTML


## **البق**


 (CELLSJAVA-41332) - AttachedFilesDirectory و AttachedFilesUrlPrefix لا يعملان بشكل صحيح

 (CELLSJAVA-41303) - PivotField.IsRepeatItemLabels لا تعمل في الجدول المحوري

 (CELLSJAVA-41430) - تم تحديد خيار Merge & Center حتى لو كان يحتوي على خلية واحدة

(CELLSJAVA-41429) - تم تغيير إعدادات توافق Lotus لإدخال الصيغة الانتقالية بعد إعادة حفظ جدول البيانات

 (CELLSJAVA-41427) - عدد كبير جدًا من التحقق من الصحة Cells يفسد الملف XLS

 (CELLSJAVA-41424) - استخدام الوظيفة المخصصة عبر واجهة ICustomFunction لا يحسب القيمة الصحيحة

 (CELLSJAVA-41423) - تخطيط خاطئ عند تقديم PDF من ملف ODS

 (CELLSJAVA-41422) - Cells.copyRows مع التنسيق الشرطي في الخلايا يتسبب في زيادة حجم الملف ومشكلة في الأداء

 (CELLSJAVA-41419) - OutOfMemoryError ، Aspose.Cells يحتفظ بملايين الخلايا إلى الأبد

 (CELLSJAVA-41395) - ODS إلى HTML التحويل - مشكلات نمط النص

 (CELLSJAVA-41426) - مخطط Cell مع المحور السيني غير المقياس بشكل صحيح عند التحويل إلى pdf

 (CELLSJAVA-41421) - تنتقل الكلمة الأخيرة في مربع نص المخطط إلى السطر التالي

 (CELLSJAVA-41416) - قيمة مشكلة القسمة أثناء إعادة حفظ جدول البيانات باستخدام Aspose.Cells

 (CELLSJAVA-41387) - تم تجاوز تسميات البيانات بواسطة قسم الرأس


## **API العام والتغييرات غير المتوافقة مع الإصدارات السابقة**


 فيما يلي قائمة بأي تغييرات تم إجراؤها على API العام مثل الأعضاء المضافين أو المعاد تسميتهم أو المحذوفون أو المهملون بالإضافة إلى أي تغيير غير متوافق مع الإصدارات السابقة تم إجراؤه على Aspose.Cells for Java. إذا كانت لديك مخاوف بشأن أي تغيير مدرج ، فيرجى رفعه في منتدى الدعم Aspose.Cells.





 يضيف خاصية SaveOptions.MergeAreas.

يتم استخدامه لدمج CellAreas الفردية من التنسيق الشرطي والتحقق من الصحة.



 يضيف أسلوب PivotTable.GetCellByDisplayName (اسم عرض السلسلة)

 يحصل على العنصر Cell بواسطة DisplayName الخاص بـ PivotField.



 يضيف طريقة SheetRender.ToImage (int pageIndex ، Graphics g ، float x ، float y)

 تقديم صفحة معينة من SheetRender إلى رسومات.



 يضيف طريقة SheetRender.ToImage (int pageIndex، Graphics g، float x، float y، float width، float height).

 تقديم صفحة معينة من SheetRender إلى رسومات.



 يضيف خاصية Shape.Geometry.ShapeAdjustValues.

 الحصول على مجموعة من قيم ضبط الشكل.





 ملحوظة

 نظرًا لأن قاعدة الكود Aspose.Cells for Java تطابق رمز إصدار .NET ذي الصلة ، فإن معظم التغييرات والتحسينات والإصلاحات المضمنة في Aspose.Cells for .NET v8.5.2 مدرجة أيضًا في Aspose.Cells for Java v8.5.2.
