---
title: Aspose.Cells for Java 8.4.0 ملاحظات الإصدار
type: docs
weight: 80
url: /ar/java/aspose-cells-for-java-8-4-0-release-notes/
---
{{% alert color="primary" %}} 

 تحتوي هذه الصفحة على ملاحظات الإصدار لـ[Aspose.Cells for Java 8.4.0](https://downloads.aspose.com/cells/java/new-releases/aspose.cells-for-java-8.4.0/)

{{% /alert %}} 

\1) Aspose.Cells

تحسينات وتغييرات أخرى

ميزات جديدة

(CELLSJAVA-41198) - استخراج بيانات الموضوع من ملفات Excel
(CELLSJAVA-41185) - توليد صور Databar

التحسينات

(CELLSJAVA-41169) - إزالة السمات الفارغة الزائفة في الملف HTML الذي تم إنشاؤه
(CELLSJAVA-41179) - دعم التقويم الياباني

البق

(CELLSJAVA-41222) - حقل فرز الجدول المحوري غير صحيح في إخراج XLSX
(CELLSJAVA-41173) - HtmlSaveOptions.setExportHiddenWorksheet (true) لا تعمل بشكل صحيح
(CELLSJAVA-41168) - التغييرات في اقتصاص نص الخلايا المتقاطعة منذ 8.3.1 إلى 8.3.1.5
(CELLSJAVA-41167) - يؤدي تحديث الجداول المحورية إلى إنشاء مصنف تالف
(CELLSJAVA-41232) - خطأ - تحتوي الصيغة على اسم محدد ينتهي بالرقم + e
(CELLSJAVA-41215) - EMF تم إنشاؤه باستخدام Aspose.Cells يتم عرضه بشكل مختلف في العارضين المختلفين
(CELLSJAVA-41196) - تلف XLSB بعد إضافة ورقة عمل وقيمة خلية
(CELLSJAVA-41227) - API لا يمكن استبدال الخط Arial بخطوط Liberation
(CELLSJAVA-41224) - خطأ في تحويل الصورة عند تقديم Excel إلى PDF
(CELLSJAVA-41223) - فشل توقيع ملفات PDF المصدرة
(CELLSJAVA-41208) - تلميحات التجسيد (Anti Aliasing) لا تعمل مع SheetRender
(CELLSJAVA-41193) - لا يتم عرض رموز Wingdings بشكل صحيح عند تحويل ورقة العمل إلى صورة
(CELLSJAVA-41184) - مشكلات عرض صورة الإخراج من المخطط
(CELLSJAVA-41106) - تتداخل تسميات البيانات للمخطط الدائري في صورة المخطط
(CELLSJAVA-40941) - تداخل DataLabels للمخطط الدائري عندما يتم تقديم المخطط كصورة
(CELLSJAVA-40813) - تتداخل تسمية بيانات المخطط الدائري في HTML المعروض
(CELLSJAVA-41182) - لا يكون الخط الأملس مناسبًا عندما يكون لون النقطة مختلفًا

استثناءات

(CELLSJAVA-41201) - java.lang.IllegalArgumentException: منطقة غير معروفة ، في PivotTable.refreshData
(CELLSJAVA-41192) - استثناء: "java.lang.Exception: وصلت نهاية الدفق" عند فتح ملف XLS
(CELLSJAVA-41228) - java.lang.ArrayIndexOutOfBoundsException at Workbook ctor أثناء تحميل XLS
(CELLSJAVA-41211) - يحدث استثناء أثناء تحليل مرجع الصيغة عند تعيين اسم الملف باستخدام Workbook.setFileName ()

\ 2) Aspose.Cells مجموعة الشبكة

تحسينات وتغييرات أخرى

(CELLSJAVA-41202) - عرض التعليقات Cell في مكون الشبكة

البق

(CELLSJAVA-41214) - يؤدي سحب ارتفاع الصف إلى 0 إلى عدم قيام GridWeb بعرض القيمة
(CELLSJAVA-41209) - لا يتم عرض قائمة التحقق من صحة البيانات في GridWeb
(CELLSJAVA-41205) - عندما تكون الحدود سميكة ، يزداد الارتفاع عند حذف قيمة الخلية في GridWeb
(CELLSJAVA-41204) - عندما تكون الحدود سميكة ، لا تتطابق ارتفاعات الرأس في GridWeb
(CELLSJAVA-41203) - لا يتطابق عرض الرأس والخلية في GridWeb
(CELLSJAVA-41073) - يختلف عرض رؤوس الأعمدة عن عروض الخلايا في Chrome / Opera

API العام والتغييرات غير المتوافقة مع الإصدارات السابقة

فيما يلي قائمة بأي تغييرات تم إجراؤها على API العام مثل الأعضاء المضافين أو المعاد تسميتهم أو المحذوفون أو المهملون بالإضافة إلى أي تغيير غير متوافق مع الإصدارات السابقة تم إجراؤه على Aspose.Cells for Java. إذا كانت لديك مخاوف بشأن أي تغيير مدرج ، فيرجى رفعه في منتدى الدعم Aspose.Cells.

 إضافة سمة HtmlSaveOptions.ExportBogusRowData
يشير إلى ما إذا كان سيتم تصدير بيانات صف سفلي زائفة أم لا. القيمة الافتراضية هي الحقيقية.

 يضيف سمة HtmlSaveOptions.CellCssPrefix
الحصول على بادئة اسم css وتعيينها ، القيمة الافتراضية هي "".

 يضيف أسلوب PivotTable.ShowInCompactForm ()
تخطيطات PivotTable في شكل مضغوط.

 يضيف أسلوب PivotTable.ShowInOutlineForm ()
تخطيطات PivotTable في نموذج المخطط التفصيلي.

 يضيف أسلوب PivotTable.ShowInTabularForm ()
تخطيطات PivotTable في شكل جدولي.

 إضافة طريقة PivotTableCollection.Remove (PivotTable pivotTable)
يحذف PivotTable المحدد

 يضيف طريقة PivotTableCollection.RemoveAt (فهرس int).
يحذف PivotTable في الفهرس المحدد

يضيف Aspose.Cells.Vba namespace و VbaPorject و VbaModuleCollection و VbaModule.
يتم استخدامها لقراءة وتعديل مشروع VBA في الملف.

 إضافة خاصية Border.ThemeColor.
الحصول على لون النسق للحدود وتعيينه.

 يضيف فئة TxtLoadStyleStrategy وخاصية TxtLoadOptions.LoadStyleStrategy.
يشير إلى إستراتيجية تطبيق النمط على القيم التي تم تحليلها عند تحويل قيمة السلسلة إلى رقم أو تاريخ ووقت.

 عفا عليها الزمن طرق TxtLoadOptions.KeepExactFormat.
الرجاء استخدام الخاصية TxtLoadOptions.LoadStyleStrategy بدلاً من ذلك.

 تقادم Cells.GetCellByIndex () وطريقة Row.GetCellByIndex ().
الرجاء استخدام طريقة GetEnumerator () لتكرار جميع الخلايا بدلاً من ذلك.

 عفا عليها الزمن DrawObject.mage خاصية
الرجاء استخدام خاصية DrawObject.ImageBytes للحصول على بيانات الصورة بدلاً من ذلك.

 إضافة خاصية DrawObject.ImageBytes
الحصول على وحدات البايت الخاصة بالصورة التي تم تحويلها من مخطط أو شكل.


ملحوظة
نظرًا لأن قاعدة الكود Aspose.Cells for Java تطابق رمز إصدار .NET ذي الصلة ، فإن معظم التغييرات والتحسينات والإصلاحات المضمنة في Aspose.Cells for .NET v8.4.0 مدرجة أيضًا في Aspose.Cells for Java v8.4.0.
