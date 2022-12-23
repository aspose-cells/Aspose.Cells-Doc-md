---
title: Aspose.Cells for Java 20.6 ملاحظات الإصدار
type: docs
weight: 10
url: /ar/java/aspose-cells-for-java-20-6-release-notes/
---
{{% alert color="primary" %}} 

 تحتوي هذه الصفحة على ملاحظات الإصدار لـ[Aspose.Cells for Java 20.6](https://downloads.aspose.com/cells/java/new-releases/aspose.cells-for-java-20.6/).

{{% /alert %}} 

|**مفتاح**|**ملخص**|**فئة**|
|:- |:- |:- |
|CELLSJAVA-43186|احسب الإجمالي الكلي لكل صف بعمود موسع|التعزيز|
|CELLSJAVA-43191|توفير وسائل للتعامل مع السيناريوهات عند تحديد أنواع الخطوط غير الصحيحة|التعزيز|
|CELLSJAVA-43187|استثناء عند تحميل ملفات XLS "Microsoft Excel 5.0 / 95 Workbook"|التعزيز|
|CELLSJAVA-43180|HTML لتحويل Excel لإنشاء إخراج ورقة عمل سوداء|خلل برمجي|
|CELLSJAVA-43181|الفرق في ارتفاع الصف في تحويل Excel الى HTML|خلل برمجي|
|CELLSJAVA-43188|لم يتم الاحتفاظ بنمط لون الخلفية أثناء HTML لتحويل Excel|خلل برمجي|
|CELLSJAVA-43196|تم اكتشاف عدد مختلف من وحدات VBA باستخدام Aspose.Cells for Java 20.4 و 20.5|خلل برمجي|
|CELLSJAVA-43202|لم يتم تحرير الموارد عند اكتمال إنشاء المصنف|خلل برمجي|
|CELLSJAVA-43203|غير قادر على معالجة بعض قوائم التحقق من صحة Excel بناءً على النطاقات المسماة بأسماء Unicode|خلل برمجي|
|CELLSJAVA-43185|تكون جودة JPEG دائمًا 75 في setImageResample على Linux|خلل برمجي|
|CELLSJAVA-43192|قم بتحميل مجلد الخطوط / System / Library / Fonts على macOS افتراضيًا|خلل برمجي|
|CELLSJAVA-43157|لا يتم الاحتفاظ بلون سلسلة البيانات المخصصة عند إنشاء مخطط انحداري|خلل برمجي|
|CELLSJAVA-43175|مشكلة في اسم سلسلة المخطط عند الرجوع إلى مصنف إلى مصنفات أخرى|خلل برمجي|
|CELLSJAVA-43201|استثناء "java.util.EmptyStackException" عند الحفظ في HTML|استثناء|
|CELLSJAVA-43204|يحدث NegativeArraySizeException عند استخدام Cell.getDisplayStringValue ()|استثناء|
|CELLSJAVA-43189|تم رفع الاستثناء أثناء تحميل الملف XLS|استثناء|
|CELLSJAVA-43193|حدث NullPointerException عند تحميل بعض ملفات XLSX|استثناء|
|CELLSJAVA-43200|استثناء "java.lang.ArrayIndexOutOfBoundsException" عند تحميل الملف|استثناء|
## **API العام والتغييرات غير المتوافقة مع الإصدارات السابقة**
فيما يلي قائمة بأي تغييرات تم إجراؤها على API العام مثل الأعضاء المضافين أو المعاد تسميتهم أو المحذوفون أو المهملون بالإضافة إلى أي تغيير غير متوافق مع الإصدارات السابقة تم إجراؤه على Aspose.Cells for Java. إذا كانت لديك مخاوف بشأن أي تغيير مدرج ، فيرجى رفعه في منتدى الدعم Aspose.Cells.
### **يضيف أسلوب RefifiedArea.GetValues (bool calculateFormulas) / GetValue (int rowOffset، int colOffset، bool calculateFormulas).**
يمنح المستخدم القدرة على التحكم في ما إذا كان يجب حساب الصيغ بشكل متكرر في تنفيذ AbstractCalculationEngine.
### **إضافة WarningType.InvalidFontName و WarningType.InvalidTextOfDefinedName تعداد.**
يمثل نوع التحذير.
### **إضافة خصائص WarningInfo.CorrectedObject و WarningInfo.ErrorObject.**
يمثل بيانات خاطئة وبيانات محدثة عند إلقاء تحذير.
### **يضيف WorkbookDesigner.RepeatFormulasWithSubtotal الخصائص.**
يشير إلى ما إذا كان يتم تكرار الصيغ مع صفوف الإجمالي الفرعي.
### **يضيف خاصية PlotArea.IsAutomaticSize.**
يشير إلى ما إذا كان حجم منطقة الرسم تلقائيًا.
### **يحذف خاصية Style.Rotation التي عفا عليها الزمن.**
استخدم الخاصية Style.RotationAngle بدلاً من ذلك.
### **يضيف Gridweb.SetFontFolder (سلسلة fontFolder ، bool recursive) / SetFontFolders (سلسلة [] fontFolders ، bool recursive).**
يضبط مجلد / مجلدات الخطوط
