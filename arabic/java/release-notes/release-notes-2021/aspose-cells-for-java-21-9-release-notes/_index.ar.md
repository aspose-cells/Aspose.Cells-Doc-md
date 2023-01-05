---
title: Aspose.Cells for Java 21.9 ملاحظات الإصدار
type: docs
weight: 4
url: /ar/java/aspose-cells-for-java-21-9-release-notes/
---
{{% alert color="primary" %}}

 تحتوي هذه الصفحة على ملاحظات الإصدار لـ[Aspose.Cells for Java 21.9](https://downloads.aspose.com/cells/java/new-releases/aspose.cells-for-java-21.9/).

{{% /alert %}}

|**مفتاح**|**ملخص**|**فئة**|
|:- |:- |:- |
|CELLSJAVA-43639|لا يمكن استخراج تاريخ ووقت الإنشاء وتاريخ التعديل|
|CELLSJAVA-43622|XLSX إلى PDF: خطأ في الشكل على الصورة|
|CELLSJAVA-43756| تشويه الصورة أثناء Excel إلى HTML|
|CELLSJAVA-43309|تم تغيير التفاصيل في Excel لتحويل HTML|
|CELLSJAVA-43578|مشاكل التنسيق أثناء تحويل Excel إلى HTML|
|CELLSJAVA-43579|مشكلة محاذاة النص أثناء تحويل Excel إلى HTML|
|CELLSJAVA-43630|الارتباط التشعبي لوظيفة الارتباط التشعبي غير صالح عند تحويل Excel إلى HTML|
|CELLSJAVA-43635|عند تصدير html ، يكون طول شريط البيانات أقصر من ذلك في Excel|
|CELLSJAVA-43709|إعادة حفظ الملف XLSM يتسبب في ظهور نافذة منبثقة لفساد الملف عند الفتح بواسطة ms excel|
|CELLSJAVA-43758|مشكلة تقييم صيغة الصفيف|
|CELLSJAVA-43680|مشكلة Databar للتنسيق الشرطي في ملف pdf الذي تم إنشاؤه|
|CELLSJAVA-43689|يؤدي تعيين التنسيق الشرطي للخلية واستخدام DataBar.toImage إلى ظهور صورة فارغة|
|CELLSJAVA-43723|لا يتم عرض الخط الموجود في الخلية بشكل كامل عند تحويل ملف Excel إلى PDF|
|CELLSJAVA-43724|غير قادر على تحويل المجمع HTML إلى CSV|
|CELLSJAVA-43728| تم تغيير اتجاه النص أثناء تحويل Excel إلى PDF|
|CELLSJAVA-43752|من Excel إلى تقديم HTML - إصدار التنسيق الشرطي لإخفاء الحدود|
|CELLSJAVA-43792|الخط غير صحيح عند تعيين HtmlLoadOptions للتحويل HTML إلى Excel|
|CELLSJAVA-43571| مشكلة اقتطاع DataLabels عند تحويل XLSX إلى PDF|
|CELLSJAVA-43587|وضع تسميات المخطط الدائري المجوف في غير محلها|
|CELLSJAVA-43620|لا يتم عرض قيم المحور الرأسي وتسميات النقاط بشكل صحيح عند عرض ملف Excel (الذي يحتوي على مخطط انحداري) إلى HTML|
|CELLSJAVA-43621|وظيفة RANDBETWEEN (أسفل ، أعلى) نتائج القيمة تختلف عن نتائج Excel|
|CELLSJAVA-41710|عرض خاطئ لـ HTML بعد التحويل من XLSX|
|CELLSJAVA-43422|HTML لتحويل Excel - "تجاهل mso: الحشو" في CSS ليس لها أي تأثير|
|CELLSJAVA-43606|تم تغيير تنسيق نص الخلفية أثناء دمج الملفات|
|CELLSJAVA-43769|لا يمكن تحميل مستند MSO Excel (XLS)|
|CELLSJAVA-43631|استثناء "java.lang.NullPointerException" عند تحميل ملف XLSM|
|CELLSJAVA-43655|ArrayIndexOutOfBoundsException مع getStringValue|
|CELLSJAVA-43788|تم رفع الاستثناء أثناء تعيين قيمة لسلسلة الرسوم البيانية|
|CELLSJAVA-43632| استثناء "Val FontUnderlineType string غير صالح" عند تحميل ملف XLSX|
|CELLSJAVA-43633|استثناء "Val MsoLineDashStyle string غير صالح" عند تحميل ملف XLSX|

## **API العام والتغييرات غير المتوافقة مع الإصدارات السابقة**

فيما يلي قائمة بأي تغييرات تم إجراؤها على API العام مثل الأعضاء المضافين أو المعاد تسميتهم أو المحذوفون أو المهملون بالإضافة إلى أي تغيير غير متوافق مع الإصدارات السابقة تم إجراؤه على Aspose.Cells for Java. إذا كانت لديك مخاوف بشأن أي تغيير مدرج ، فيرجى رفعه في منتدى الدعم Aspose.Cells.

### **يضيف خاصية AutoFitterOptions.FormatStrategy.**

الحصول على الإستراتيجية المنسقة للتركيب التلقائي وتعيينها.

### **إضافة خاصية MsoFormatPicture.Transparency.**

 إرجاع أو تعيين درجة شفافية المنطقة كقيمة من 0.0 (معتم) إلى 1.0 (واضح).

### **يضيف طرق PivotTableCollection.Remove () المحملة بشكل زائد.**

حذف PivotTable المحدد والتحقق مما إذا كان يتم الاحتفاظ ببيانات الخلايا.

### **يضيف خاصية ImageOrPrintOptions.IsOptimized.**

يشير إلى ما إذا كان سيتم تحسين عناصر الإخراج. القيمة الافتراضية هي كاذبة. حاليًا ، يتم تحسين خطوط الحدود فقط عند تعيين هذه الخاصية على "صواب".

