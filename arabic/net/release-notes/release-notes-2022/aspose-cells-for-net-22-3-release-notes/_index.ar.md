---
title: Aspose.Cells for .NET 22.3 ملاحظات الإصدار
type: docs
weight: 10
url: /ar/net/aspose-cells-for-net-22-3-release-notes/
---
{{% alert color="primary" %}}

 تحتوي هذه الصفحة على ملاحظات الإصدار لـ[Aspose.Cells for .NET 22.3](https://www.nuget.org/packages/Aspose.Cells/22.3.0).

{{% /alert %}}

|**مفتاح**|**ملخص**|**فئة**|
|:- |:- |:- |
|CELLSNET-50375|دعم فرز PivotField عبر القيم في الصف / العمود المحدد|
|CELLSNET-50559|دعم للحصول على أوراق الخلايا بشكل متكرر|
|CELLSNET-50512|دعم لإعادة حساب الخلايا التي تشير إلى الاسم المحدد عند تغيير الاسم المحدد وتمكين سلسلة الحساب|
|CELLSNET-50403|أضف SaveFormat.Ots و SaveFormat.Xlt|
|CELLSNET-50422|دعم الإعداد داخل boders|
|CELLSNET-50342|لا يتم فرز الجدول المحوري عند التحديث|
|CELLSNET-50451|يؤدي حذف ورقة العمل إلى حذف مقسمات العرض|
|CELLSNET-50462|الانحدار: بعد نسخ مجموعة من الصيغ الخلايا مفقودة|
|CELLSNET-50545| لا يتم تلوين الحقول المنسقة شرطيًا باللون الصحيح|
|CELLSNET-50565|لم يتم حساب الصيغ بشكل صحيح|
|CELLSNET-50309|النطاق حتى PNG: الإخراج ليس كما هو متوقع|
|CELLSNET-50334|الانحدار: XLS إلى PDF: لم يتم تقديم الرأس بشكل صحيح|
|CELLSNET-50367|يستغرق تحويل .XLSX إلى PDF وقتًا طويلاً وينتج صفحات إضافية|
|CELLSNET-50401|القيم الرقمية أو الأرقام التي تليها عناصر غير مرئية في ملف pdf الناتج|
|CELLSNET-50478|يُرجع Workbook.ExportXml الصف الأول فقط من بيانات الجدول|
|CELLSNET-50507|يقوم Xml Import بإظهار الأعمدة المخفية مسبقًا في النموذج|
|CELLSNET-50554|لم يتم تقديم المحتوى بشكل صحيح في Excel لتحويل PDF|
|CELLSNET-50316|لا تعمل النصوص الملتفة على المخططات عند توليد PDF|
|CELLSNET-50411|لم يتم تقديم تسميات المحور الأفقي للمخطط بشكل صحيح في الإخراج PDF|
|CELLSNET-50341|مشكلة في طي وتوسيع المجموعات متعددة المستويات|
|CELLSNET-50368|ODS إلى PDF التحويل غير صحيح|
|CELLSNET-50377|لم يتم تطبيق تنسيق "النص" المخصص في ملف XLS|
|CELLSNET-50380| لا تقوم خاصية ImportTableOptions.IsHtmlString بإخراج الارتباطات بشكل صحيح|
|CELLSNET-50418|تحميل HTML في المصنف لا يعمل|
|CELLSNET-50494|مشكلة في لون الخلايا المنسقة شرطيًا في ملف الإخراج XLSX|
|CELLSNET-50563|تحدث المشكلة عند تعيين الترخيص المضمن على "إنتاج ملف فردي" في تطبيق .NET 6.0|
|CELLSNET-50585|لا توجد خطوط مائلة للأمام ولكن مائلة للخلف للروابط الخارجية بعنوان URL|
|CELLSNET-50390| System.ArgumentException: لا يمكن أن يكون رقم الصف أو رقم العمود صفراً عند استيراد بيانات JSON كجدول|
|CELLSNET-50555| ArgumentOutOfRangeException أثناء محاولة الحصول على صيغة الخلية|

## **API العام والتغييرات غير المتوافقة مع الإصدارات السابقة**

فيما يلي قائمة بأي تغييرات تم إجراؤها على API العام مثل الأعضاء المضافين أو المعاد تسميتهم أو المحذوفون أو المهملون بالإضافة إلى أي تغيير غير متوافق مع الإصدارات السابقة تم إجراؤه على Aspose.Cells for .NET. إذا كانت لديك مخاوف بشأن أي تغيير مدرج ، فيرجى رفعه في منتدى الدعم Aspose.Cells.

### **يغير القيمة الافتراضية لـ HtmlSaveOptions.ExcludeUnusedStyles.**

عند حفظ ملفات html ، بالنسبة للإصدارات القديمة ، نقوم أحيانًا بإزالة الأنماط غير المستخدمة تلقائيًا عند وجود العديد من كائنات الأنماط في المجموعة ، بغض النظر عن قيمة هذه الخاصية. بالنسبة لملفات html التي تم إنشاؤها ، يمكن أن يؤدي استبعاد الأنماط غير المستخدمة إلى تصغير حجم الملف دون التأثير على التأثيرات المرئية. لذلك من هذا الإصدار ، نجعل القيمة الافتراضية لهذه الخاصية صحيحة لجعلها متوافقة مع سلوك الحفظ. إذا احتاج المستخدم إلى الاحتفاظ بجميع الأنماط في المصنف لـ html الذي تم إنشاؤه (مثل السيناريو الذي يحتاجه المستخدم لاستعادة المصنف من html الذي تم إنشاؤه لاحقًا) ، فيرجى تعيين هذه الخاصية على أنها false أثناء حفظ html.

### **يضيف Cell.GetLeafs (منطقي متكرر).**

دعم المستخدم للحصول على جميع أوراق خلية واحدة بشكل متكرر.

### **يضيف طريقة Range.SetInsideBorders (BorderType و CellBorderType و CellsColor).**

دعم لتعيين الحدود الداخلية للنطاق.

### **إضافة تعداد SaveFormat.Ots و SaveFormat.Xlt و LoadFormat.Ots.**

تحسين تحميل وحفظ ملفات ots و xlt.

### **يضيف فئة FormulaSettings.**

افصل جميع الإعدادات المتعلقة بالصيغة من WorkbookSettings وقم بتجميعها في صيغة FormulaSettings.

### **يضيف خاصية WorkbookSettings.FormulaSettings.**

يحصل على الإعدادات المجمعة للصيغ.

### **إضافة خاصية PivotItem.IsHideDetail.**

الحصول على وتحديد ما إذا كان العنصر المحوري يخفي التفاصيل أم لا.

### **Obsoletes WorkbookSettings.ReCalculateOnOpen الخاصية.**

الرجاء استخدام WorkbookSettings.FormulaSettings.CalculateOnOpen بدلاً من ذلك.

### **Obsoletes WorkbookSettings.RecalculateBeforeSave.**

الرجاء استخدام WorkbookSettings.FormulaSettings.CalculateOnSave بدلاً من ذلك.

### **Obsoletes WorkbookSettings.ForceFullCalculate property.**

الرجاء استخدام WorkbookSettings.FormulaSettings.ForceFullCalculation بدلاً من ذلك.

### **Obsoletes WorkbookSettings.PrecisionAsDisplayed property.**

الرجاء استخدام WorkbookSettings.FormulaSettings.PrecisionAsDisplayed بدلاً من ذلك.

### **Obsoletes WorkbookSettings.CalcMode الخاصية.**

الرجاء استخدام WorkbookSettings.FormulaSettings.CalculationMode بدلاً من ذلك.

### **Obsoletes WorkbookSettings.Iteration property.**

الرجاء استخدام WorkbookSettings.FormulaSettings.EnableIterativeCalculation بدلاً من ذلك.

### **Obsoletes WorkbookSettings.MaxIteration property.**

الرجاء استخدام WorkbookSettings.FormulaSettings.MaxIteration بدلاً من ذلك.

### **Obsoletes WorkbookSettings.MaxChange الملكية.**

الرجاء استخدام WorkbookSettings.FormulaSettings.MaxChange بدلاً من ذلك.

### **Obsoletes WorkbookSettings.CalculationId الخاصية.**

الرجاء استخدام WorkbookSettings.FormulaSettings.CalculationId بدلاً من ذلك.

### **Obsoletes WorkbookSettings.CreateCalcChain property.**

الرجاء استخدام WorkbookSettings.FormulaSettings.EnableCalculationChain بدلاً من ذلك.

### **Obsoletes WorkbookSettings.CalcStackSize الخاصية.**

الرجاء استخدام CalculationOptions مع حجم المكدس المحدد بدلاً من ذلك عند حساب الصيغ.
