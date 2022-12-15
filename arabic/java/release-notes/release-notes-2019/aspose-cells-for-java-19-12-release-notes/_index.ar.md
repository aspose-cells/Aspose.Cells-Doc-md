---
title: Aspose.Cells for Java 19.12 ملاحظات الإصدار
type: docs
weight: 10
url: /ar/java/aspose-cells-for-java-19-12-release-notes/
---
{{% alert color="primary" %}} 

تحتوي هذه الصفحة على ملاحظات إصدار Aspose.Cells for Java 19.12.

{{% /alert %}} 

|**مفتاح**|**ملخص**|**فئة**|
|:- |:- |:- |
|CELLSJAVA-43047|إضافة نص تلميح إلى الخلية للتصدير بتنسيق HTML|ميزة جديدة|
|CELLSJAVA-43002|نقطة فعالة غير متوقعة لوحدة المعالجة المركزية في ZipOutputStream عند فتح XSLB|التعزيز|
|CELLSJAVA-43008|خيار لتعطيل تحميل كائن OLE أثناء فتح مصنف|التعزيز|
|CELLSJAVA-42793|تم فقد كائن Fontwork SmartArt أثناء تحويل ODS إلى XLSX|حشرة|
|CELLSJAVA-43020|رسم بياني شعاعي مشوه بعد استدعاء Chart.Calcluate ()|حشرة|
|CELLSJAVA-43022|خطأ من شكل إلى صورة لملفات XLS|حشرة|
|CELLSJAVA-43046|يؤدي LoadOptions.setParsingFormulaOnOpen (false) إلى نتائج غير مرغوب فيها أثناء استدعاء getFormula ()|حشرة|
|CELLSJAVA-43052|مشكلة التحقق من صحة القيم المنطقية|حشرة|
|CELLSJAVA-43054|مشكلة تتعلق بدمج CSV في الإعدادات البرتغالية|حشرة|
|CELLSJAVA-43056|Cell.setFormula () لا يتم تحديثه للروابط الخارجية|حشرة|
|CELLSJAVA-42767|فقدت الصورة أثناء تحويل Excel إلى PDF|حشرة|
|CELLSJAVA-42913|تم عرض كائنات Visio المضمنة بشكل غير صحيح إلى PDF|حشرة|
|CELLSJAVA-42883|مشكلة في استخراج نص الرسم البياني من ملف التنسيق Aspose.Cells for Java 95|حشرة|
|CELLSJAVA-42931|لم يتم جلب المرفقات / الكائنات من Excel95|حشرة|
|CELLSJAVA-43051|لم يتم الحفاظ على نسبة العرض إلى الارتفاع للصورة|حشرة|
|CELLSJAVA-43057|مشكلة تتعلق بإضافة صورة رأس إلى الصفحة الأولى في الإخراج Excel|حشرة|
|CELLSJAVA-43069|يعطي MS Excel رسالة إصلاح عند فتح الملف المعاد حفظه بحلول Aspose.Cells|حشرة|
|CELLSJAVA-43060|استثناء "java.lang.NullPointerException" في Workbook.save بعد تعيين مصدر البيانات الخارجية على أنه فارغ|استثناء|
|CELLSJAVA-42923|استثناءات أثناء تحميل مستند XLS|استثناء|

## **API العام والتغييرات غير المتوافقة مع الإصدارات السابقة**
فيما يلي قائمة بأي تغييرات تم إجراؤها على API العام مثل الأعضاء المضافين أو المعاد تسميتهم أو المحذوفون أو المهملون بالإضافة إلى أي تغيير غير متوافق مع الإصدارات السابقة تم إجراؤه على Aspose.Cells for Java. إذا كانت لديك مخاوف بشأن أي تغيير مدرج ، فيرجى رفعه في منتدى الدعم Aspose.Cells.
### **حذف خاصية DataLabels.BaseField القديمة**
الرجاء استخدام PivotField.BaseFieldIndex بدلاً من ذلك.
### **يحذف خاصية DataLabels.BaseItem القديمة**
الرجاء استخدام PivotField.BaseItemIndex بدلاً من ذلك.
### **حذف خاصية DataLabels.IsValueShown القديمة**
استخدم خاصية DataLabels.ShowValue بدلاً من ذلك.
### **حذف خاصية DataLabels.IsPercentageShown المتقادمة**
استخدم خاصية DataLabels.ShowPercentage بدلاً من ذلك.
### **حذف خاصية DataLabels.IsBubbleSizeShown القديمة**
استخدم خاصية DataLabels.ShowBubbleSize بدلاً من ذلك.
### **حذف خاصية DataLabels.IsCategoryNameShown القديمة**
استخدم خاصية DataLabels.ShowCategoryName بدلاً من ذلك.
### **حذف خاصية DataLabels.IsSeriesNameShown القديمة**
استخدم خاصية DataLabels.ShowSeriesName بدلاً من ذلك.
### **حذف خاصية DataLabels.IsLegendKeyShown القديمة**
استخدم خاصية DataLabels.ShowLegendKey بدلاً من ذلك.
### **يضيف خيار LoadOptions.KeepUnparsedData**
يشير الخيار إلى ما إذا كان سيتم الاحتفاظ بالبيانات التي لم يتم تحليلها في الذاكرة للمصنف عند تحميله من ملف قالب. إذا لم يكن المستخدمون بحاجة إلى حفظ المصنف بالكامل مرة أخرى ، خاصةً عندما يحتاجون فقط إلى قراءة بعض المحتوى الخاص بالمصنف (مثل نوع من LoadFilter) ، فلن تكون هناك حاجة إلى البيانات غير الموزعة بعد الآن وقد يقومون بتعيين هذه الخاصية على أنها خاطئة للحصول على أداء أفضل. بالنسبة للإصدارات القديمة ، عند تحميل المصنف من ملف قالب باستخدام LoadFilter المحدد من قبل المستخدم ، لم يتم الاحتفاظ بالبيانات غير المحللة للنظر في الأداء. نقدم الآن هذا الخيار ونجعل قيمته الافتراضية صحيحة ، فقد يؤثر ذلك على أداء حالات المستخدمين لاستخدام LoadFilter. إذا كان الأمر كذلك ، يجب على المستخدمين تعيين هذه الخاصية على أنها خطأ بشكل صريح في تطبيقاتهم.
### **يضيف خيار LoadDataFilterOptions.Picture**
الخيار الذي يشير إلى ما إذا كان يجب تحميل الصورة.
### **يضيف خيار LoadDataFilterOptions.OleObject**
الخيار الذي يشير إلى ما إذا كان يجب تحميل OleObject.
### **يضيف خيار LoadDataFilterOptions.Drawing**
الخيار الذي يشير إلى ما إذا كان يجب تحميل الكائنات الرسومية (بما في ذلك التخطيط والصورة و OleObject وكافة الكائنات الرسومية الأخرى).
### **يتخلى عن خيار LoadDataFilterOptions.Shape**
الرجاء استخدام (LoadDataFilterOptions.Drawing & ~ LoadDataFilterOptions.Chart) بدلاً من LoadDataFilterOptions.Shape.
### **يضيف فئة FormulaParseOptions**
يوفر خيارات المستخدم لإعداد الصيغ.
### **يضيف طرقًا: Cell.SetFormula (صيغة سلسلة ، خيارات FormulaParseOptions ، قيمة الكائن) ، SetArrayFormula (سلسلة مصفوفة ، صيغة int ، rowNumber ، int عمود ، FormulaParseOptions options) ، SetSharedFormula (string sharedFormula ، int rowNumber ، int columnNumber ، FormionsParse)**
يضبط الصيغ مع الخيارات.
### **الطرق القديمة: Cell.SetFormula (صيغة سلسلة ، منطقي هو R1C1 ، منطقي isLocal ، قيمة الكائن) ، SetArrayFormula (string arrayFormula ، int rowNumber ، int columnNumber ، bool isR1C1 ، bool isLocal) ، SetSharedFormula (string sharedFormula، int rowNumber ، int row) isR1C1 ، منطقي isLocal)**
الرجاء استخدام الطرق المقابلة مع FormulaParseOptions بدلاً من ذلك.
### **يضيف FileFormatType.OTP التعداد**
يدعم الكشف عن تنسيق ملف .OTP.
### **إضافة خاصية AutoFitterOptions.AutoFitWrappedTextType وتعداد AutoFitWrappedTextType.**
الحصول على نوع النص المغلف المناسب تلقائيًا وتعيينه.
### **يضيف فئة EmfRenderSetting**
مجموعات لعرض ملف تعريف EMF.
### **يضيف خاصية PdfSaveOptions.EmfRenderSetting**
مجموعات لعرض ملف تعريف EMF أثناء التقديم إلى ملف PDF.
### **يضيف طريقة ShapeCollection.AddSvg ()**
يضيف صورة svg.
### **يضيف خاصية WorkbookSettings.QuotePrefixToStyle**
الإشارة إلى ما إذا كان إعداد خاصية Style.QuotePrefix عند إدخال قيمة السلسلة (التي تبدأ بعلامة اقتباس مفردة) في الخلية
### **إضافة خاصية HtmlSaveOptions.AddTooltipText**
يشير إلى ما إذا كانت إضافة نص تلميح أداة عندما يتعذر عرض البيانات بالكامل. القيمة الافتراضية هي كاذبة.
