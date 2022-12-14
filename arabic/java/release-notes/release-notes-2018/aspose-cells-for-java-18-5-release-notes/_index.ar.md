---
title: Aspose.Cells for Java 18.5 ملاحظات الإصدار
type: docs
weight: 80
url: /ar/java/aspose-cells-for-java-18-5-release-notes/
---
{{% alert color="primary" %}} 

تحتوي هذه الصفحة على ملاحظات إصدار for Java Aspose.Cells 18.5.

{{% /alert %}} 

|**مفتاح**|**ملخص**|**فئة**|
|:- |:- |:- |
|CELLSJAVA-42550|التحويل المتزامن إلى PDF بينما يحتوي كل مصنف على مجموعة خطوطه الخاصة (الحصرية)|ميزة جديدة|
|CELLSJAVA-42594|كشف LoadFormat و FileFormatType من XLAM|التعزيز|
|CELLSJAVA-42604|تم تغيير تنسيق وسلوك Pivot Table بعد فتح / حفظ ملف القالب|حشرة|
|CELLSJAVA-41918|جدول البيانات (XLS) تالف بعد التحميل والحفظ البسيط|حشرة|
|CELLSJAVA-42616|Aspose.Cells يكسر واجهة المكرر عند استدعاء Iterator.hasnext () مرتين|حشرة|
|CELLSJAVA-42607|قيم الخصائص مشوهة عند استخراج خصائص الوثيقة|حشرة|
|CELLSJAVA-42601|المصنف تالف بعد إضافة علامة مائية|حشرة|
|CELLSJAVA-42600|يتم تنفيذ نفس الكود بشكل أبطأ في الإصدارات الجديدة|حشرة|
|CELLSJAVA-42598|لا يتم استخراج الخصائص في ملف القالب|حشرة|
|CELLSJAVA-42589|NullPointerException عند إضافة HTML إلى خلية|حشرة|
|CELLSJAVA-41414|اختفت الأسطر من المخطط عند إعادة حفظ ملف XLSX|حشرة|
|CELLSJAVA-42602|استثناء "IndexOutOfBoundsException" عند دمج الخلايا في وضع الوزن الخفيف|استثناء|
|CELLSJAVA-42610|استثناء "java.lang.IllegalStateException: ترميز غير صالح: فارغ" عند تحميل ملف XLS|استثناء|
|CELLSJAVA-42608|يحدث ArrayIndexOutOfBoundsException عند فتح ملف Excel|استثناء|
|CELLSJAVA-42596|يحدث "java.lang.ArrayIndexOutOfBoundsException" عند فتح ملف Excel|استثناء|
|CELLSJAVA-42595|يحدث "java.io.IOException: الملف تالف" عند فتح ملف Excel|استثناء|
|CELLSJAVA-42591|"com.aspose.cells.CellsException: صيغة غير صالحة" عند تحميل ملف Excel|استثناء|
## **API العام والتغييرات غير المتوافقة مع الإصدارات السابقة**
فيما يلي قائمة بأي تغييرات تم إجراؤها على API العام مثل الأعضاء المضافين أو المعاد تسميتهم أو المحذوفون أو المهملون بالإضافة إلى أي تغيير غير متوافق مع الإصدارات السابقة تم إجراؤه على Aspose.Cells for Java. إذا كانت لديك مخاوف بشأن أي تغيير مدرج ، فيرجى رفعه في منتدى الدعم Aspose.Cells.
### **إضافة خصائص جديدة Cell.IsTableFormula / IsArrayFormula لتحل محل Cell. IsInTable / IsInArray**
الإشارة إلى ما إذا كانت خلية واحدة جزءًا من صيغة الجدول أو صيغة الصفيف. الأسماء القديمة تثير الغموض ، لذلك جعلناها قديمة ونقدم أسماء جديدة.
### **يضيف فئة IndividualFontConfigs**
يمثل تكوينات الخط لكل كائن مصنف.
### **يضيف خاصية LoadOptions.FontConfigs**
يحصل ويضبط تكوينات الخطوط الفردية.
### **حذف خاصية FontSetting.ShapeFont القديمة**
استخدم خاصية FontSetting.TextOptions بدلاً من ذلك.
### **يضيف OoxmlCompliance enum و WorkbookSettings.Compliance الخاصية**
يدعم جدول بيانات Xml المفتوح الصارم.
### **يضيف طريقة GroupShape.Ungroup ()**
يفك تجميع الأشكال.
### **يضيف خاصية MsoFormatPicture.Gamma**
الحصول على جاما للصورة وتعيينها.
### **إضافة خصائص TextOptions.FarEastName و TextOptions.LatinName**
احصل على اسم الخط في الشرق الأقصى واللاتينية وقم بتعيينهما.
