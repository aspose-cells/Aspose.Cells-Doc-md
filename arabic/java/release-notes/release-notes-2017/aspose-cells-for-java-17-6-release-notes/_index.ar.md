---
title: Aspose.Cells for Java 17.6 ملاحظات الإصدار
type: docs
weight: 70
url: /ar/java/aspose-cells-for-java-17-6-release-notes/
---
{{% alert color="primary" %}} 

 تحتوي هذه الصفحة على ملاحظات الإصدار لـ[Aspose.Cells for Java 17.6](https://downloads.aspose.com/cells/java/new-releases/aspose.cells-for-java-17.6/).

{{% /alert %}} 

|**مفتاح**|**ملخص**|**فئة**|
|:- |:- |:- |
|CELLSJAVA-42315|إضافة عميل JS API لحدث AjaxCallFinished - GridWeb (JAVA)|ميزة جديدة|
|CELLSJAVA-42194|تجميع الصفوف في ورقة العمل - GridWeb (JAVA)|ميزة جديدة|
|CELLSJAVA-42308|PivotTable خاطئ (الصفوف المفقودة ، رؤوس الحقول المحورية المطبوعة مرتين ، التاريخ المحول إلى قيم رقمية ، إلخ) في Excel إلى عرض HTML|خلل برمجي|
|CELLSJAVA-42298|توجد أحرف إضافية في HTML إخراج ملف Excel|خلل برمجي|
|CELLSJAVA-42277|لا يتم عرض الصورة في الإخراج HTML عند تعيين HtmlSaveOptions.setExportHiddenWorksheet على false|خلل برمجي|
|CELLSJAVA-42259|HTML تعذر تحويلها إلى ملف Excel بشكل صحيح|خلل برمجي|
|CELLSJAVA-42256|مشكلة مع جدول HTML لتقديم Excel|خلل برمجي|
|CELLSJAVA-42319|مشكلة في حساب ناحية الطباعة عند تحديد الصيغ|خلل برمجي|
|CELLSJAVA-42273|لا تعمل ميزة تعيين تلميح رأس العمود في GridWeb (JAVA)|خلل برمجي|
|CELLSJAVA-42269|GridWorksheet.setColumnHeaderToolTip () لا يعمل في GridWeb (JAVA)|خلل برمجي|
|CELLSJAVA-42320|لا يتم تحديث المخطط إذا كان موجودًا في ورقة منفصلة|خلل برمجي|
|CELLSJAVA-42295|يتم إلحاق قيمة Cell في البداية عندما نضغط على خلية موجودة (لها بعض القيمة)|خلل برمجي|
|CELLSJAVA-42325|عند حفظ XLSX بالشكل PDF ، يتم عكس الكلمات|خلل برمجي|
|CELLSJAVA-42299|توجد أحرف إضافية في الإخراج PDF / صورة من ملف Excel|خلل برمجي|
|CELLSJAVA-42301|الأعمدة مفقودة في إخراج PDF للمخطط الشريطي|خلل برمجي|
|CELLSJAVA-42293|صورة المخطط خاطئة في الإخراج HTML|خلل برمجي|
|CELLSJAVA-42292|صورة المخطط غير صحيحة في الإخراج HTML|خلل برمجي|
|CELLSJAVA-42270|يكون المحتوى مفقودًا عند تحويل Excel Chart إلى PDF|خلل برمجي|
|CELLSJAVA-42258|يحتوي PDF على تنسيق تاريخ خاطئ لتسميات المحور س|خلل برمجي|
|CELLSJAVA-42252|تحجيم المحور Y غير الصحيح في PDF الناتج|خلل برمجي|
|CELLSJAVA-42245|النمط / التنسيق خطأ عند الحفظ بالرقم HTML|خلل برمجي|
|CELLSJAVA-42316|لا يتم الاحتفاظ بخيار ضغط الصور عند فتح ملف Excel وحفظه|خلل برمجي|
|CELLSJAVA-42306|يتم تغيير لون الخلفية للخلايا في File2 عند فتح المصنف وحفظه|خلل برمجي|
|CELLSJAVA-42305|يتم تغيير لون الخلفية للخلايا في File1 عند فتح المصنف وحفظه|خلل برمجي|
|CELLSJAVA-42303|تصبح خلية صيغة Excel خلية غير معادلة عند تعيين نص للشكل|خلل برمجي|
|CELLSJAVA-42284|يعرض Workbook.getFonts () خطًا إضافيًا بعد إعادة تحميل نفس جدول البيانات|خلل برمجي|
|CELLSJAVA-42307|استثناء: حدث "يجب ألا يكون فهرس الصف داخل التقرير المحوري" عند التقديم إلى تنسيق ملف HTML|استثناء|
|CELLSJAVA-42285|استثناء: حدث "لا يمكن أن يكون فهرس الصف سالبًا" إذا كان PivotTable موجودًا في ورقة العمل ليتم تحويله إلى تنسيق ملف HTML|استثناء|
|CELLSJAVA-42318|تم طرح استثناء عند محاولة فتح المصنف|استثناء|
|CELLSJAVA-42311|استثناء: "java.lang.NullPointerException" عند فتح ملف ODS عبر واجهات برمجة تطبيقات Aspose.Cells|استثناء|
|CELLSJAVA-42302|NullPointerException عند إنشاء مثيل مصنف من ملف Excel المصدر|استثناء|
## **API العام والتغييرات غير المتوافقة مع الإصدارات السابقة**
فيما يلي قائمة بأي تغييرات تم إجراؤها على API العام مثل الأعضاء المضافين أو المعاد تسميتهم أو المحذوفون أو المهملون بالإضافة إلى أي تغيير غير متوافق مع الإصدارات السابقة تم إجراؤه على Aspose.Cells for Java. إذا كانت لديك مخاوف بشأن أي تغيير مدرج ، فيرجى رفعه في منتدى الدعم Aspose.Cells.
### **إضافة خاصية Gridweb.OnAjaxCallFinishedClientFunction**
الحصول على أو تعيين اسم وظيفة جانب العميل ليتم استدعاؤها عند انتهاء ajaxcall.
### **يضيف تعداد StyleModifyFlag.RelativeIndent**
يمثل المسافة البادئة النسبية.
### **يضيف خاصية TextureFill.IsTiling**
يشير إلى ما إذا كانت صورة التجانب على هيئة نسيج.


### **أمثلة على الاستخدام**
يرجى التحقق من قائمة مواضيع المساعدة المضافة في Aspose.Cells مستندات Wiki:

- [تجانب الصورة كنسيج داخل الشكل](/cells/ar/java/tile-picture-as-a-texture-inside-the-shape/)
- [استخدام وظيفة OnAjaxCallFinishedClient في GridWeb](/cells/ar/java/using-onajaxcallfinishedclientfunction-of-gridweb/)
- [استخدام معلمة الصيغة في حقل العلامة الذكية](/cells/ar/java/using-formula-parameter-in-smart-marker-field/)
