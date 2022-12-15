---
title: Aspose.Cells for PHP via Java 22.9 ملاحظات الإصدار
type: docs
weight: 4
url: /ar/php-java/aspose-cells-for-php-via-java-22-9-release-notes/
---
{{% alert color="primary" %}}

 تحتوي هذه الصفحة على ملاحظات الإصدار لـ[Aspose.Cells for PHP via Java 22.9](https://releases.aspose.com/cells/php/new-releases/aspose.cells-for-php-via-java-22.9/).

{{% /alert %}}

|**مفتاح**|**ملخص**|**فئة**|
|:- |:- |:- |
|CELLSJAVA-44194|لا يتم تقديم شكل الرسم في عرض Excel إلى PDF|
|CELLSJAVA-44864|يؤدي التحميل المتزامن للمصنفات إلى ظهور أخطاء زائفة "الملف تالف"|
|CELLSJAVA-44327|تظهر الحدود وعدد أقل من الخطوط في شرائح دائرية بالأبيض والأسود في الرسم البياني لعرض الصورة|
|CELLSJAVA-44591|لا يتطابق استدارة نص التسميات مع Excel في صورة الإخراج للمخطط|
|CELLSJAVA-44775|تتداخل تسميات المخطط في الرسم البياني مع عرض الصورة|
|CELLSJAVA-44860|يختلف عرض نص الخلية كما هو الحال في Excel في بعض المناطق المدمجة|
|CELLSJAVA-44832|يتم إخراج صفحات متعددة بدلاً من صفحة واحدة كما في Excel أثناء التحويل إلى pdf|
|CELLSJAVA-44812|غير قادر على إنقاص منطقة الرسم للمخطط|
|CELLSJAVA-44831|يطالب MS Word بالخطأ "وجد Word محتوى غير قابل للقراءة في ..." عند فتح DOCX المحول من ملف XLSX بواسطة Aspose.Cells for Java|
|CELLSJAVA-44833|لا يتم تطبيق لون النص على كلمات مختلفة أو جزء من المحتويات في ملف Excel الناتج عند استخدام أسلوب Cell.setHtmlString ()|
|CELLSJAVA-44852| الحد غير صحيح عند تحويل ملف Excel الثابت إلى HTML|
|CELLSJAVA-44856| تحويل Excel إلى HTML - لا يتم عرض / عرض خط المؤشر (مخطط صغير)|
|CELLSJAVA-44859|لا تعمل بعض تنسيقات Html مع خلايا ورقة العمل في ملف Excel موجود|
|CELLSJAVA-44842|استثناء "java.lang.OutOfMemoryError: Java heap space" عند تحويل ملف XLSX إلى PDF|

## **API العام والتغييرات غير المتوافقة مع الإصدارات السابقة**

فيما يلي قائمة بأي تغييرات تم إجراؤها على API العام مثل الأعضاء المضافين أو المعاد تسميتهم أو المحذوفون أو المهملون بالإضافة إلى أي تغيير غير متوافق مع الإصدارات السابقة تم إجراؤه على Aspose.Cells for Java. إذا كانت لديك مخاوف بشأن أي تغيير مدرج ، فيرجى رفعه في منتدى الدعم Aspose.Cells.

### **يضيف Cell.SetTableFormula (...) طرق**

دعم لتعيين الصيغ لنطاق من الخلايا لإنشاء جدول بيانات ذي متغيرين وجدول بيانات متغير واحد.

### **يضيف Cell.SetDynamicArrayFormula (سلسلة arrayFormula ، FormulaParseOptions options ، object [] [] القيم ، bool calculateRange ، bool calculateValue، CalculationOptions copts)**

دعم لتعيين صيغة صفيف ديناميكية بخيارات مخصصة للحساب ، خاصةً عند وجود وظائف تحتاج إلى محرك مخصص للمستخدم للحساب في الصيغة.

### **يضيف Workbook.RefreshDynamicArrayFormulas (حساب منطقي ، CalculationOptions copts) طريقة**

دعم تحديث صيغ الصفيف الديناميكية بخيارات مخصصة للحساب ، خاصةً عند وجود وظائف تحتاج إلى محرك مخصص للمستخدم لوظائف الحساب في صيغ الصفيف الديناميكية.

### **إضافة خاصية ChartFrame.TextOptions.**

يمثل خيارات خط نص الرسم البياني.

### **إضافة خاصية ExportRangeToJsonOptions.ExportEmptyCells.**

الإشارة إلى ما إذا كان التصدير فارغًا إذا كانت الخلايا فارغة.

### **أضف مُنشئ NumbersLoadOptions.**

يمثل خيارات تحميل الأرقام.

### **يضيف تعداد LoadNumbersTableType.**

يمثل نوع تحميل جداول متعددة في ورقة عمل من أرقام Mac.

### **يضيف خاصية ProtectedRange.IsProtectedWithPassword.**

يستنتج ما إذا كان النطاق محميًا بكلمة مرور.

### **يضيف خصائص ImportTableOptions.ExportCaptionAsFieldName**

يشير إلى ما إذا كان يتم تصدير التسمية التوضيحية كاسم حقل عند استيراد جدول البيانات.

### **يضيف خاصية TextOptions.LanguageCode.**

الحصول على رمز لغة الخط وتعيينه.

### **يضيف التعداد PresetThemeGradientType.**

يمثل نوع التدرج اللوني للنسق المعين مسبقًا.

### **يضيف طريقة GradientFill.SetPresetThemeGradient ().**

يضبط نوع التدرج اللوني للنسق المعين مسبقًا.

### **يضيف طرق تجاوز Style.SetBorder ().**

يضبط الحدود بأنواع مختلفة من الألوان.

### **يضيف أساليب Range.SetOutlineBorder () و Range.SetOutlineBorders ()**

يضبط حدود النطاق بأنواع مختلفة من الألوان.
