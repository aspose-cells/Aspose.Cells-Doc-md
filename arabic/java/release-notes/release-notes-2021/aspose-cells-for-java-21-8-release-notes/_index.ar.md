---
title: Aspose.Cells for Java 21.8 ملاحظات الإصدار
type: docs
weight: 5
url: /ar/java/aspose-cells-for-java-21-8-release-notes/
---
{{% alert color="primary" %}}

 تحتوي هذه الصفحة على ملاحظات الإصدار لـ[Aspose.Cells for Java 21.8](https://downloads.aspose.com/cells/java/new-releases/aspose.cells-for-java-21.8/).

{{% /alert %}}

|**مفتاح**|**ملخص**|**فئة**|
|:- |:- |:- |
|CELLSJAVA-42494|يتم إنشاء كمية كبيرة من الأنماط غير المستخدمة في قسم CSS|
|CELLSJAVA-43576|لا يتم عرض قيم النص الرسومي عند تحويل XLSX إلى PDF|
|CELLSJAVA-43483|لا يتم التأكيد على النص الموجود بعد علامة "br" داخل علامة "em" عند تحويل مستند HTML إلى مصنف|
|CELLSJAVA-43526|IllegalArgumentException: فهرس العمود غير صالح|
|CELLSJAVA-43557|لون غير صحيح عند الحفظ بتنسيق html|
|CELLSJAVA-43567|الانحدار: لم يتم حساب صيغة MDURATION بشكل صحيح|
|CELLSJAVA-43583|عامل الطاقة "^" لا يعمل لحسابات الصيغ|
|CELLSJAVA-43549|الصورة مفقودة في Output PDF|
|CELLSJAVA-43566|الخطوط الافتراضية على MacOS Big Sur|
|CELLSJAVA-42579|لا يتم عرض عناوين المحور بشكل صحيح - المحاذاة اليمنى مفقودة عند حفظ Excel في Pdf|
|CELLSJAVA-43554|لا يظهر نص جدول بيانات المخطط في صورة الإخراج|
|CELLSJAVA-43556|XLSX إلى PDF: عنوان مخطط غير كامل|
|CELLSJAVA-40051|دعم Apple iWork|
|CELLSJAVA-43119|التحويل إلى PDF - رقم تنسيق الملف غير المدعوم 3.5 منذ 2014|
|CELLSJAVA-43538|يتسبب التخطيط بدون بيانات في تلف XLSX بعد الحفظ باستخدام Aspose Cells|
|CELLSJAVA-43547|يقوم AutoFitRow بتغيير الارتفاع القياسي لورقة العمل|
|CELLSJAVA-43591|خطأ عند فتح ملف في MS Excel تم حفظه بواسطة Aspose.Cells|
|CELLSJAVA-43523|CellsException لقراءة اسم الماكرو للشكل: صيغة غير صالحة|
|CELLSJAVA-43565|"java.lang.ClassCastException" عند قراءة ملف XLSB باستخدام LightCells|
|CELLSJAVA-43546|NullPointerException عند استخراج اسم سلسلة الرسم البياني|

## **API العام والتغييرات غير المتوافقة مع الإصدارات السابقة**

فيما يلي قائمة بأي تغييرات تم إجراؤها على API العام مثل الأعضاء المضافين أو المعاد تسميتهم أو المحذوفون أو المهملون بالإضافة إلى أي تغيير غير متوافق مع الإصدارات السابقة تم إجراؤه على Aspose.Cells for Java. إذا كانت لديك مخاوف بشأن أي تغيير مدرج ، فيرجى رفعه في منتدى الدعم Aspose.Cells.

### **إضافة فئة AbstractInterruptMonitor.**

يوفر AbstractInterruptMonitor كأساس لتطبيقات مراقبة الانقطاع. أصبحت فئة InterruptMonitor الآن أحد تطبيقاتها. أصبح نوع خصائص InterruptMonitor لـ LoadOptions و Workbook الآن AbstractInterruptMonitor أيضًا بحيث يمكن للمستخدم استخدام التنفيذ الخاص به للتحكم في العمليات التي تستغرق وقتًا طويلاً.

### **إضافة خاصية HtmlSaveOptions.WorksheetScalable.**

يشير إلى ما إذا كان يتم تكبير أو تصغير html عبر مستوى تكبير ورقة العمل عند حفظ الملف إلى html ، فإن القيمة الافتراضية هي false.

### **يضيف تجاوز طريقة WorksheetCollection.GetRangeByName ().**

يحصل على كائن النطاق بالاسم من الجداول أو الأسماء المعرفة.

### **يضيف طريقة Range.AutoFill ().**

يملأ البيانات تلقائيًا إلى النطاق.

### **يضيف WarningType.IO enum.**

يمثل ملف تالف تحذير.
