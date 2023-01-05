---
title: Aspose.Cells for Java 8.8.3 ملاحظات الإصدار
type: docs
weight: 80
url: /ar/java/aspose-cells-for-java-8-8-3-release-notes/
---
## **1) Aspose.Cells**

|**مفتاح**|**ملخص**|**فئة**|
|:- |:- |:- |
|CELLSJAVA-41866|كيفية تعيين خصائص إدخال وسيلة الإيضاح لخيارات النص|ميزة جديدة|
|CELLSJAVA-41865|قم بإنشاء TextBox حيث يكون لكل سطر محاذاة أفقية مختلفة|ميزة جديدة|
|CELLSJAVA-41873|التحويل إلى HTML يجعل الصفوف الفارغة الزائدة عن الحاجة|خلل برمجي|
|CELLSJAVA-41869|يتم تغيير محاذاة النص بعد إعادة حفظ ملف قالب XLS|خلل برمجي|
|CELLSJAVA-41854|ملف Excel مع DataBars لم يتم تحويله إلى HTML بشكل صحيح|خلل برمجي|
|CELLSJAVA-41851|لا يتم عرض المخطط المحوري الذي تم إنشاؤه باستخدام Aspose.Cells في Excel 2016 لنظام التشغيل MAC|خلل برمجي|
|CELLSJAVA-41840|يتم الحاق Aspose.Cells بقيمة خالية في نهاية المسار للموارد HTML|خلل برمجي|
|CELLSJAVA-41878|تقوم واجهات برمجة تطبيقات LightCells بإنشاء أحداث للعمود الأول من الصف فقط|خلل برمجي|
|CELLSJAVA-41859|تظهر حدود Cell بعد إعادة حفظ XLS|خلل برمجي|
|CELLSJAVA-41888|يتم فقدان صورة الشعار أثناء التحويل XLS إلى PDF|خلل برمجي|
|CELLSJAVA-41874|يختلف موضع الحرف في PDF الذي تم تقديمه عن ملف XLS|خلل برمجي|
|CELLSJAVA-41852|تداخل النص عند تحويل أوراق العمل إلى EMF على Linux|خلل برمجي|
|CELLSJAVA-41823|تختلف كثافة النص وفواصل الأسطر مقارنةً بـ Excel الذي تم إنشاؤه PDF|خلل برمجي|
|CELLSJAVA-41822|يتم قطع النص وتداخله أثناء تقديم جدول البيانات إلى PDF|خلل برمجي|
|CELLSJAVA-41856|مشاكل تحويل المخطط إلى PDF|خلل برمجي|
|CELLSJAVA-41855|يؤدي فتح ملف Excel وحفظه إلى تغيير خطوط الاتجاه|خلل برمجي|
|CELLSJAVA-41890|حفظ المصنف مرتين ، سيكون المحتوى المحفوظ في المرة الثانية مختلفًا عن المرة الأولى|خلل برمجي|
|CELLSJAVA-41884|مشكلة في PageBreaks التي لم يتم فرزها قبل الحفظ في ملف Excel|خلل برمجي|
|CELLSJAVA-41876|الملف تالف إذا تم فتحه وحفظه وإعادة فتحه وحفظه بواسطة واجهات برمجة تطبيقات Aspose.Cells|خلل برمجي|
|CELLSJAVA-41867|تم تغيير قيم محور المخطط بعد إعادة حفظ ملف XLS|خلل برمجي|
|CELLSJAVA-41861|NullReferenceException أثناء تحميل ملف Excel XLS|خلل برمجي|
|CELLSJAVA-41298|عدم الحصول على معلومات دقيقة حول تنسيق شكل WordArt من Aspose.Cells APIs|خلل برمجي|
|CELLSJAVA-40366|رمز مضمن - لا تتم طباعته|خلل برمجي|
|CELLSJAVA-41883|CellsException: نوع الوظيفة الإضافية غير معروف: 9 ، في Workbook.calculateFormula|استثناء|
|CELLSJAVA-41858|CellsException: خطأ في حساب Cell [0BMW CAN Bus Codes V0.4! R4] ، في Workbook.calculateFormula|استثناء|
|CELLSJAVA-41870|java.lang.ArrayIndexOutOfBoundsException: 4 في Workbook.save أثناء إعادة الحفظ XLS|استثناء|
|CELLSJAVA-41864|استثناء: java.lang.IllegalStateException: ترميز غير صالح: فارغ عند إعادة حفظ ملف XLS|استثناء|
## **API العام والتغييرات غير المتوافقة مع الإصدارات السابقة**
فيما يلي قائمة بأي تغييرات تم إجراؤها على API العام مثل الأعضاء المضافين أو المعاد تسميتهم أو المحذوفون أو المهملون بالإضافة إلى أي تغيير غير متوافق مع الإصدارات السابقة تم إجراؤه على Aspose.Cells for Java. إذا كانت لديك مخاوف بشأن أي تغيير مدرج ، فيرجى رفعه في منتدى الدعم Aspose.Cells.
### **يضيف Cell.GetCharacters (flag) method**
ترجع جميع كائنات الأحرف.
### **إضافة خاصية OleObject.AutoLoad**
يحدد ما إذا كان سيتم استدعاء التطبيق المضيف للكائن المضمن لتحميل بيانات الكائن تلقائيًا عند فتح المصنف الأصلي.
### **يضيف خاصية HTMLLoadOptions.SupportDivTag**
 يشير إلى ما إذا كان سيتم دعم تخطيط<div> علامة عندما يحتوي ملف html<div> العلامات: القيمة الافتراضية هي false.
### **إضافة خاصية HtmlSaveOptions.ExportGridLines**
مبيناً ما إذا كان سيتم تصدير خطوط الشبكة أم لا. القيمة الافتراضية هي كاذبة.
### **إضافة خاصية ShapeTextAlignment.TextShapeType**
يحدد الشكل الهندسي المعين مسبقًا الذي سيتم استخدامه لالتواء الشكل على جزء من النص.
### **يضيف طريقة LoadOptions.SetPaperSize (نوع PaperSizeType)**
يضبط حجم ورق الطباعة الافتراضي من إعداد الطابعة الافتراضية.
### **يحذف طريقة Workbook.Decrypt () القديمة**
يرجى تعيين WorkbookSettings.Password على أنه فارغ.
### **يضيف خاصية ListObject.Comment**
يحصل ويضع تعليق الجدول.
### **يضيف طريقة ShapeCollection.AddActiveXControl ()**
يضيف عنصر تحكم ActiveX.

{{% alert color="primary" %}} 

نظرًا لأن قاعدة الكود Aspose.Cells for Java تطابق رمز إصدار .NET ذي الصلة ، فإن معظم التغييرات والتحسينات والإصلاحات المضمنة في Aspose.Cells for .NET v8.8.3 مدرجة أيضًا في Aspose.Cells for Java v8.8.3.

{{% /alert %}}
