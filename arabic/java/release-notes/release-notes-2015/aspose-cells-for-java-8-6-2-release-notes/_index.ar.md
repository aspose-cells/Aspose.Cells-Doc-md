---
title: Aspose.Cells for Java 8.6.2 ملاحظات الإصدار
type: docs
weight: 10
url: /ar/java/aspose-cells-for-java-8-6-2-release-notes/
---
{{% alert color="primary" %}} 

 تحتوي هذه الصفحة على ملاحظات الإصدار لـ[Aspose.Cells for Java 8.6.2](https://downloads.aspose.com/cells/java/new-releases/aspose.cells-for-java-8.6.2/)

{{% /alert %}} 

 فيما يلي قائمة بالتحسينات والتغييرات في هذا الإصدار من Aspose.Cells



\1) Aspose.Cells 


## **تحسينات وتغييرات أخرى**

## **ميزات جديدة**


 (CELLSJAVA-41144) - القدرة على حذف النمط من StyleCollection


## **البق**


 (CELLSJAVA-41554) - صورة مفقودة عند التحويل من تنسيق HTML إلى تنسيق EXCEL

 (CELLSJAVA-41549) - XLSB تالف في Excel 2010 بعد الحفظ بواسطة Aspose.Cells v8.6.1

 (CELLSJAVA-41530) - فقد إعداد تخطيط PivotTable الكلاسيكي عند إعادة حفظ ملف XLSB للقالب

 (CELLSJAVA-41558) - متوسط التنسيقات الشرطية الحصول على صيغ مضافة

 (CELLSJAVA-41546) - Workbook.calculateFormula تتعطل طرق الصيغة لفترة غير محددة

(CELLSJAVA-41544) - مشكلة تنسيق التاريخ الياباني عند التحويل من "XML Spreadsheet 2003" إلى XLSX

 (CELLSJAVA-41543) - إصدار مع وظيفة CODE () للأحرف الروسية

 (CELLSJAVA-41541) - لا يتم الاحتفاظ بحجم الخط أثناء تحويل XML Spreadsheet 2003 إلى تنسيقات أخرى

 (CELLSJAVA-41538) - تؤدي إعادة حفظ جدول البيانات إلى إزالة بعض الخصائص من الورقة 1.xml لعلامة controlPr

 (CELLSJAVA-41567) - مشكلة بخط webdings في عروض Excel إلى PDF

 (CELLSJAVA-41559) - يؤدي الحفظ في PDF إلى إنشاء ألوان تدرج ألوان غير صحيحة

 (CELLSJAVA-41556) - تؤدي طباعة ملف PDF Aspose.Cells الذي تم إنشاؤه إلى تغيير الرمز الشريطي المضمن إلى حد ما

 (CELLSJAVA-41552) - يبدو أن عرض وارتفاع قيمة النص المستدير غير صحيحين

 (CELLSJAVA-41578) - لا يتم إنشاء الرسم البياني إلى PDF بعد تنفيذ طريقة chart.toPdf (اسم الملف)

 (CELLSJAVA-41574) - مشكلة التباعد بين المحور Y والأساطير

 (CELLSJAVA-41557) - تم تغيير الفرق بين علامات تحديد تسمية المحور من 10 إلى 20 أثناء عرض المخطط إلى PDF

(CELLSJAVA-41553) - تُظهر ألوان الرسم البياني تحولًا كبيرًا في إخراج PDF

 (CELLSJAVA-41539) - لا يتطابق نطاق المحور الرأسي مع المخطط المصدر أثناء تقديم جدول البيانات إلى PDF

 (CELLSJAVA-41536) - مشكلة تتعلق بأشكال خط السلسلة في المخطط وفقًا لـ MS Excel 2010/2013

 (CELLSJAVA-41533) - التباعد بين وسيلة الإيضاح وتسميات المحور في المخطط أقل من المتوقع

 (CELLSJAVA-41520) - يتم قطع صورة المخطط من الجانبين العلوي والأيمن

 (CELLSJAVA-41509) - مشاكل حدود المخطط أثناء عرض المخطط على PDF

 (CELLSJAVA-41505) - يتم قطع الحدود اليمنى والسفلى أثناء عرض المخطط على PDF

 (CELLSJAVA-41560) - كيفية الحصول على اللون الافتراضي لورقة العمل

 (CELLSJAVA-41542) - مشكلة في اسم خانة الاختيار عند إنشاء خانات اختيار باستخدام Aspose.Cells

 (CELLSJAVA-41469) - دعم العلامات الذكية المتداخلة


## **استثناءات**


 (CELLSJAVA-41550) - java.lang.NullPointerException في Workbook.combine

(CELLSJAVA-41564) - استدعاء NullPointerExceptions com.aspose.cells.Row



 2) Aspose.Cells مجموعة الشبكة


## **تحسينات وتغييرات أخرى**

## **البق**


 (CELLSJAVA-41566) - حجم الخط أصغر من الخلية الأخرى


## **API العام والتغييرات غير المتوافقة مع الإصدارات السابقة**


 فيما يلي قائمة بأي تغييرات تم إجراؤها على API العام مثل الأعضاء المضافين أو المعاد تسميتهم أو المحذوفون أو المهملون بالإضافة إلى أي تغيير غير متوافق مع الإصدارات السابقة تم إجراؤه على Aspose.Cells for Java. إذا كانت لديك مخاوف بشأن أي تغيير مدرج ، فيرجى رفعه في منتدى الدعم Aspose.Cells.



 يضيف خاصية WorkbookDesigner.CallBack وواجهة ISmartMarkerCallBack.

 يمثل واجهة رد لمعالجة العلامات الذكية ..



 يضيف Cells. خاصية النمط.

 الحصول على النمط الافتراضي لورقة العمل وتعيينه.



 يضيف طريقة Chart.ToPdf (اسم ملف سلسلة).

 يحفظ الرسم البياني في ملف pdf.



 يضيف طريقة Workbook.RemoveUnusedStyles ().

 يزيل كل الأنماط غير المستخدمة من تجمع أنماط المصنف.



 يضيف حدث AjaxCallFinished في GridWeb

 حرائق عند انتهاء تحديث ajax لعنصر التحكم. (يجب ضبط EnableAJAX على true).



 يضيف حدث CellModifiedOnAjax في GridWeb

 حرائق عندما يتم تعديل الخلية في ajaxcall.





 ملحوظة

نظرًا لأن قاعدة الكود Aspose.Cells for Java تطابق رمز إصدار .NET ذي الصلة ، فإن معظم التغييرات والتحسينات والإصلاحات المضمنة في Aspose.Cells for .NET v8.6.2 مدرجة أيضًا في Aspose.Cells for Java v8.6.2.
