---
title: Aspose.Cells for Java 8.2.1 ملاحظات الإصدار
type: docs
weight: 20
url: /ar/java/aspose-cells-for-java-8-2-1-release-notes/
---
{{% alert color="primary" %}} 

 تحتوي هذه الصفحة على ملاحظات الإصدار لـ[Aspose.Cells for Java 8.2.1](https://downloads.aspose.com/cells/java/new-releases/aspose.cells-for-java-8.2.1/)

{{% /alert %}} 

 تم تحديث Aspose.Cells for Java إلى الإصدار 8.2.1 ويسعدنا أن نعلن أن هذا الإصدار يجلب إضافة أكثر من 30 تحسينًا مفيدًا جديدًا.
باستخدام Aspose.Cells for Java يمكنك العمل مع XLS و SpreadsheetML و OOXML و XLSB و CSV و HTML و ODS و PDF و XPS وغيرها من التنسيقات في تطبيقاتك. يمكنك أيضًا إنشاء المصنفات وتعديلها وتحويلها وعرضها وطباعتها دون استخدام Microsoft Excel.
قم بزيارة الوثائق لمعرفة كيفية البدء مع Aspose.Cells for Java.
لاحظ أن هذا التنزيل يحتوي على إصدار كامل من المنتج ، ولكن بدون تعيين ترخيص ، سيتم تشغيله في وضع التقييم مع بعض القيود. لاختبار Aspose.Cells بدون قيود التقييم هذه ، يمكنك طلب ترخيص مؤقت مجاني لمدة 30 يومًا.
 فيما يلي قائمة بالتغييرات في هذا الإصدار Aspose.Cells for Java.

\1) Aspose.Cells

تحسينات وتغييرات أخرى

ميزات جديدة

(CELLSJAVA-40955) - شكل الموضع المطلق
(CELLSJAVA-40943) - أضف خيارًا إلى PasteOptions للصق الخلايا المرئية فقط من النطاق

البق

(CELLSJAVA-40977) - لا يعمل التنسيق الشرطي عند تحويل ملف Excel إلى HTML
(CELLSJAVA-40959) - سمة محاذاة إضافية في إخراج HTML.
(CELLSJAVA-40954) - عدم تطابق الأعمدة في إخراج HTML
(CELLSJAVA-40953) - تم تمديد بعض حدود الخلايا قليلاً عند تحويل Excel إلى html
(CELLSJAVA-40980) - لم يتم تحديث قيمة الخلية المرتبطة من المصنف الخارجي
(CELLSJAVA-40957) - تؤدي حماية ورقة العمل في الوضع المرخص إلى تعطل MS Excel عند المعاينة
(CELLSJAVA-40956) - يقوم Chart.getName () بإرجاع اسم مخطط خاطئ
(CELLSJAVA-40952) - لا يُرجع Series.hasLeaderLines () القيمة الصحيحة
(CELLSJAVA-40944) - تلف ملف PDF المضمن بعد دمج Workbooks
(CELLSJAVA-40979) - يتم إرفاق بعض المربعات بملصقات البيانات في المخطط الدائري في ملف PDF المعروض
(CELLSJAVA-40975) - تحويل XLSX إلى Jpeg - الأداء
(CELLSJAVA-40973) - تعطيل setExtractContentPermission - خيار "إذن نسخ المحتوى أو استخراجه" لا يعمل
(CELLSJAVA-40965) - Cells تتعارض في ملف PDF
(CELLSJAVA-40962) - Aspose.Cells يعرض قيمة # N / A بشكل مختلف عن MS Excel
(CELLSJAVA-40926) - حدود الجدول طبيعية بدلاً من غامقة عند التكبير بنسبة 100٪
(CELLSJAVA-40833) - جودة الصورة في المخطط منخفضة - تحويل المخطط إلى صورة
(CELLSJAVA-40949) - لا يظهر المحور الأفقي في صورة المخطط
(CELLSJAVA-40948) - لا تظهر الصورة المخصصة في نقاط البيانات في صورة المخطط
(CELLSJAVA-40947) - لا تظهر الأحرف الصينية في صورة المخطط
(CELLSJAVA-40946) - ملصقات البيانات في موضع خاطئ داخل صورة المخطط
(CELLSJAVA-40821) - يكون مربع النص مفقودًا عند حفظ الرسم البياني على هيئة EMF باستخدام ToImage
(CELLSJAVA-40819) - قيم محور خاطئة عند حفظ الرسم البياني على هيئة EMF باستخدام ToImage
(CELLSJAVA-40818) - عنوان المحور مفقود عند حفظ الرسم البياني على هيئة EMF باستخدام ToImage
(CELLSJAVA-40830) - فهرس z معكوس في مخطط مساحي ومخطط شريطي عند التصدير إلى PDF

استثناءات

(CELLSJAVA-40985) - CellsException: تم الوصول إلى نهاية الملف في Workbook.save
(CELLSJAVA-40983) - java.lang.NullPointerException في Workbook.save
(CELLSJAVA-40981) - Aspose.Cells لا يمكنه قراءة ملفات Excel 2013 المحمية بكلمة مرور
(CELLSJAVA-40976) - سوف يرمي Sparkline NullPointerException عند استخدام insertRows
(CELLSJAVA-40969) - استثناء: "java.lang.StringIndexOutOfBoundsException: فهرس السلسلة خارج النطاق" أثناء تحديث قيمة الشكل
(CELLSJAVA-40967) - لا يمكن الإرسال إلى LineShape

API العام والتغييرات غير المتوافقة مع الإصدارات السابقة

فيما يلي قائمة بأي تغييرات تم إجراؤها على API العام مثل الأعضاء المضافين أو المعاد تسميتهم أو المحذوفون أو المهملون بالإضافة إلى أي تغيير غير متوافق مع الإصدارات السابقة تم إجراؤه على Aspose.Cells for Java. إذا كانت لديك مخاوف بشأن أي تغيير مدرج ، فيرجى رفعه في منتدى الدعم Aspose.Cells.

 يضيف Cell.GetValidation () طريقة
يحصل على التحقق الذي ينطبق على الخلية.

 يضيف Cell.GetValidationValue () طريقة
يشير إلى ما إذا كانت قيمة الخلية صالحة.

 يضيف طريقة WorkbookRender.ToPrinter (PrinterSettings PrinterSettings)
تقديم المصنف إلى الطابعة عبر إعدادات الطابعة.


ملحوظة
نظرًا لأن قاعدة الكود Aspose.Cells for Java تطابق رمز إصدار .NET ذي الصلة ، فإن معظم التغييرات والتحسينات والإصلاحات المضمنة في Aspose.Cells for .NET v8.2.1 مدرجة أيضًا في Aspose.Cells for Java v8.2.1.
