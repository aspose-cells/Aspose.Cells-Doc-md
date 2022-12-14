---
title: Aspose.Cells for Java 18.10 ملاحظات الإصدار
type: docs
weight: 30
url: /ar/java/aspose-cells-for-java-18-10-release-notes/
---
{{% alert color="primary" %}} 

تحتوي هذه الصفحة على ملاحظات إصدار Aspose.Cells for Java 18.10.

{{% /alert %}} 

|**مفتاح**|**ملخص**|**فئة**|
|:- |:- |:- |
|CELLSJAVA-42634|تحويل شكل الشريط الأيمن الأيسر إلى صورة|التعزيز|
|CELLSJAVA-42713|Aspose.Cells for Java JavaDocs - ملف قائمة الحزم مفقود|التعزيز|
|CELLSJAVA-42528|الخط ليس علامة HTML5 صالحة وعلامة الإغلاق الذاتي ومتصفحات الويب تحرف محتوياته|التعزيز|
|CELLSJAVA-42728|يظهر استثناء (StackOverFlow) عند الحفظ في إخراج PDF|حشرة|
|CELLSJAVA-42729|تم حساب قيمة خاطئة بواسطة ROUNDUP ()|حشرة|
|CELLSJAVA-42724|انسخ نطاقًا باستخدام PasteType.ALL (خيارات اللصق) لا ينسخ ارتفاعات الصف بشكل صحيح|حشرة|
|CELLSJAVA-42722|يتم فقد تنسيق نص الارتباط التشعبي عند تعيين نص جديد|حشرة|
|CELLSJAVA-42688|إخراج تنسيق التاريخ الروسي غير صالح|حشرة|
|CELLSJAVA-42721|مشكلة مع خطوط SheetRender|حشرة|
|CELLSJAVA-42723|استثناء "java.lang.OutOfMemoryError: Java heap space" عند تقديم ملف MS Excel إلى PDF|حشرة|
|CELLSJAVA-42725|تظهر علامات الاقتباس في الصيغة عند استرداد صيغة الخلية عبر Aspose.Cells|حشرة|
|CELLSJAVA-42720|تدهور الأداء عند استخدام التنسيق الشرطي|حشرة|
## **API العام والتغييرات غير المتوافقة مع الإصدارات السابقة**
فيما يلي قائمة بأي تغييرات تم إجراؤها على API العام مثل الأعضاء المضافين أو المعاد تسميتهم أو المحذوفون أو المهملون بالإضافة إلى أي تغيير غير متوافق مع الإصدارات السابقة تم إجراؤه على Aspose.Cells for Java. إذا كانت لديك مخاوف بشأن أي تغيير مدرج ، فيرجى رفعه في منتدى الدعم Aspose.Cells.
### **يضيف خاصية HtmlSaveOptions.WidthScalable**
يشير إلى ما إذا كان سيتم استخدام وحدة قابلة للقياس لوصف عرض العمود عند تصدير ملف إلى HTML. القيمة الافتراضية هي كاذبة.
### **يضيف خاصية WorkbookDesigner.UpdateEmptyStringAsNull**
يشير إلى ما إذا كانت معالجة قيمة السلسلة الفارغة فارغة أم لا.
### **يحدّث القيمة التي تم إرجاعها لأسلوب DocumentProperty.ToDateTime () وخصائص BuiltInDocumentPropertyCollection.CreatedTime و BuiltInDocumentPropertyCollection.LastPrinted و BuiltInDocumentPropertyCollection.LastSavedTime.**
إرجاع الوقت بالتوقيت المحلي.
### **يتطلب قيدًا أقوى لإدخال المستخدم لـ FormatCondition.Formula1 / Formula2**
لا يمكن تحديد سلسلة الإدخال العادية ما إذا كان يجب أن تشير إلى مرجع اسم أم أنها مجرد قيمة سلسلة ثابتة. لذا ، نطلب الآن أن تبدأ الصيغة بعلامة '='. للحصول على قيمة سلسلة عادية "sss" ، يرجى استخدام تنسيق مثل "= \" sss \ "".
