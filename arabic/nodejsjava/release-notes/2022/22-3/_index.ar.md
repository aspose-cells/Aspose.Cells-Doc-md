---
title: Aspose.Cells لـ Node.js عبر Java 22.3 ملاحظات الإصدار
type: docs
weight: 10
url: /ar/nodejs-java/aspose-cells-for-node-js-via-java-22-3-release-notes/
---
{{% alert color="primary" %}}

 تحتوي هذه الصفحة على ملاحظات الإصدار لـ[Aspose.Cells لـ Node.js عبر Java 22.3](https://downloads.aspose.com/cells/nodejs/new-releases/aspose.cells-for-node.js-via-java-22.3/).

{{% /alert %}}

|**مفتاح**|**ملخص**|**فئة**|
|:- |:- |:- |
|CELLSJAVA-44369| ارتفاع الشكل غير صحيح|
|CELLSJAVA-44366|يؤدي نسخ محتوى الورقة إلى صفحة ورقة جديدة وحفظها بتنسيق html إلى نمط غير طبيعي لصيغة Excel الرياضية|
|CELLSJAVA-44408|يتم فقد تنسيق النسبة المئوية Cell عندما نقوم بتوسيع هذين الصفين اللذين قمنا بتغييرهما|
|CELLSJAVA-44341|عرض Cell غير صحيح في إخراج DOCX في تحويل Excel إلى DOCX|
|CELLSJAVA-44383|توقف التنسيق الشرطي عن العمل بعد إضافة خصائص مخصصة|
|CELLSJAVA-44370|تلف ملف Excel عند فتحه وحفظه باستخدام Aspose.Cells|
|CELLSJAVA-44344| مشكلة تتعلق بالنسخ الأفقي للنطاقات في الإخراج XLSX|
|CELLSJAVA-44363| لا يتطابق ارتفاع رأس الصف مع محتوى الصف في الملف مع freezepane|
|CELLSJAVA-44349|يجب الاحتفاظ بالصورة / الشكل بعد إعادة تشغيل الخادم لـ GridWeb|
|CELLSJAVA-44367|يتحول لون المخطط العمودي إلى اللون الأبيض عند التحويل إلى html|
|CELLSJAVA-44328| تُفقد بعض ملصقات البيانات الخاصة برسوم Excel عند حفظ ملف Excel بتنسيق HTML|
|CELLSJAVA-44193|تختلف زاوية عناصر محور الفئة في الرسم البياني في تحويل Excel إلى PDF|
|CELLSJAVA-44314|تسميات محور فئة المخطط خاطئة في عرض الرسم البياني للصورة|
|CELLSJAVA-44332|لا يمكن إزالة تسطير الارتباط Cell عند تحويل xlsx إلى html|
|CELLSJAVA-44323|استثناء أثناء إضافة سطر التوقيع|
|CELLSJAVA-44361|تم رفع CellsException أثناء تحويل xlsx إلى html|

## **API العام والتغييرات غير المتوافقة مع الإصدارات السابقة**

فيما يلي قائمة بأي تغييرات تم إجراؤها على API العام مثل الأعضاء المضافين أو المعاد تسميتهم أو المحذوفون أو المهملون بالإضافة إلى أي تغيير غير متوافق مع الإصدارات السابقة تم إجراؤه على Aspose.Cells for Java. إذا كانت لديك مخاوف بشأن أي تغيير مدرج ، فيرجى رفعه في منتدى الدعم Aspose.Cells.

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
