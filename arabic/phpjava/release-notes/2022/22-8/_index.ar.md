---
title: Aspose.Cells for PHP via Java 22.8 ملاحظات الإصدار
type: docs
weight: 5
url: /ar/php-java/aspose-cells-for-php-via-java-22-8-release-notes/
---
{{% alert color="primary" %}}

 تحتوي هذه الصفحة على ملاحظات الإصدار لـ[Aspose.Cells for PHP via Java 22.8](https://releases.aspose.com/cells/php/new-releases/aspose.cells-for-php-via-java-22.8/).

{{% /alert %}}

|**مفتاح**|**ملخص**|**فئة**|
|:- |:- |:- |
|CELLSJAVA-44811|دعم لتحديد الأوراق لإخراجها أثناء التصدير إلى pdf / xps|
|CELLSJAVA-44777|تصدير الصيغ إلى html فقط بالاعتماد على خيار HtmlSaveOptions.Exportformula|
|CELLSJAVA-44791|تحسين تحليل سلسلة html إلى خلية|
|CELLSJAVA-44740|أدى تعيين التاريخ قبل 1581 لخلية إلى إنشاء سلسلة تاريخ غير صحيحة|
|CELLSJAVA-44758|نسخ ورقة العمل عبر المصنفات ، تنسيق الخلية غير طبيعي|
|CELLSJAVA-44796|محرك حساب الصيغة Aspose.Cells ينتج # N / A؟ قيم خلايا معينة|
|CELLSJAVA-44798|خطأ في التنسيق 0.9999999999999999 مع "#" المخصص لـ JDK8 أو الإصدارات الأحدث|
|CELLSJAVA-44773|يتم إفساد البيانات عند فتح مستند Excel بأعمدة مخفية في GridWeb (Java)|
|CELLSJAVA-44781|التحقيق في مشكلة تغيير حجم الصف عند تغيير الحجم إلى ارتفاع صغير جدًا|
|CELLSJAVA-44787|تم فقد الحد السفلي في الصف الأخير في المصنف|
|CELLSJAVA-44761|استخدام مفرط للذاكرة عند تحويل ملف Excel إلى HTML|
|CELLSJAVA-44801|تحويل Excel إلى PDF باستخدام Aspose.Cells for Java v22.7 يتسبب في أحرف مشوشة|
|CELLSJAVA-44741|فاصل الأسطر غير صحيح في الإخراج xlsx بعد تعيين سلسلة html في الخلية|
|CELLSJAVA-44776|فقد تصميم صف رأس الجدول عند نسخ الورقة|
|CELLSJAVA-44789|مشكلة تتعلق باستبدال سلسلة الأحرف لمربع نص تم وضعه في جدول بيانات Excel|
|CELLSJAVA-44792| مصنف حفظ لا نهاية له بتنسيق HTML (2892)|
|CELLSJAVA-44763|استثناء "java.lang.IllegalArgumentException: لا يمكن تحليل رقم الوسيطة: 1: X8" عند تحميل ملف Excel باستخدام "org.apache.commons.io.input.AutoCloseInputStream"|
|CELLSJAVA-44774|خطأ عند الحفظ كـ PDF - التحقيق مطلوب|

## **API العام والتغييرات غير المتوافقة مع الإصدارات السابقة**

فيما يلي قائمة بأي تغييرات تم إجراؤها على API العام مثل الأعضاء المضافين أو المعاد تسميتهم أو المحذوفون أو المهملون بالإضافة إلى أي تغيير غير متوافق مع الإصدارات السابقة تم إجراؤه على Aspose.Cells for Java. إذا كانت لديك مخاوف بشأن أي تغيير مدرج ، فيرجى رفعه في منتدى الدعم Aspose.Cells.

### **أضف طريقة FontSettingCollection.Replace ().**

استبدل نص الشكل.

### **أضف خاصية ShapeTextAlignment.NumberOfColumns.**

الحصول على عدد أعمدة نص الشكل وتعيينه.

### **أضف خاصية HtmlSaveOptions.ExportCommentsType.**

الحصول على نوع تعليقات التصدير إلى html وتعيينه.

### **أضف فئة أساسية PaginatedSaveOptions لـ PdfSaveOptions و XpsSaveOptions.**

يمثل خيارات ترقيم الصفحات.

### **أضف مجموعة أوراق الفصل.**

يصف مجموعة من الأوراق.

### **إضافة خاصية PaginatedSaveOptions.SheetSet.**

الحصول على الأوراق أو تعيينها للعرض.

### **إضافة خاصية ImageOrPrintOptions.SheetSet.**

الحصول على الأوراق أو تعيينها للعرض.

### **إضافة خاصية GridWeb.IgnoreStyleWithNoData.**

الحصول على أو تعيين ما إذا كان GridWeb يتجاهل إظهار الصفوف أو الأعمدة التي لا تحتوي على قيم خلية ولكنها لا تزال ذات نمط

### **خاصية ImageOrPrintOptions.SaveFormat قديمة.**

بالنسبة لـ Tiff / Svg ، الرجاء استخدام ImageType ؛ بالنسبة إلى Xps ، يرجى استخدام Workbook.Save (سلسلة ، SaveOptions) مع XpsSaveOptions.

### **مُنشئ قديم XpsSaveOptions (Aspose.Cells.SaveFormat saveFormat).**

الرجاء استخدام المُنشئ XpsSaveOptions () بدلاً من ذلك.

### **مُنشئ قديم SvgSaveOptions (Aspose.Cells.SaveFormat saveFormat).**

الرجاء استخدام المُنشئ SvgSaveOptions () بدلاً من ذلك.

### **إزالة المُنشئ PdfSaveOptions (Aspose.Cells.SaveFormat saveFormat).**

يُرجى استخدام المُنشئ PdfSaveOptions () بدلاً من ذلك.
