---
title: Aspose.Cells لـ Node.js عبر Java 22.12 ملاحظات الإصدار
type: docs
weight: 1
url: /ar/nodejs-java/aspose-cells-for-node-js-via-java-22-12-release-notes/
---
{{% alert color="primary" %}}

 تحتوي هذه الصفحة على ملاحظات الإصدار لـ[Aspose.Cells لـ Node.js عبر Java 22.12](https://releases.aspose.com/cells/nodejs/new-releases/aspose.cells-for-node.js-via-java-22.12/).

{{% /alert %}}

|**مفتاح**|**ملخص**|**فئة**|
|:- |:- |:- |
|CELLSJAVA-43645|لم يتم تقديم سمة "تنسيق ثلاثي الأبعاد" للمستطيل بشكل صحيح|
|CELLSJAVA-44936|تعيين إعدادات صورة المخطط (PNG) DPI|
|CELLSJAVA-44937|ضبط إعدادات صورة المخطط (JPG) DPI|
|CELLSJAVA-44998|اقتباس مزدوج تسبب في فشل النمط المضمّن في HTML|
|CELLSJAVA-44970|تحسين تأثير الظل|
|CELLSJAVA-44967|قم بتخطيط getDataLabels (). getText () بإرجاع قيمة مختلفة في v22.6.0 والإصدارات الأحدث|
|CELLSJAVA-44969|تحويل Excel إلى HTML ، تعرض قواعد البيانات الأخطاء|
|CELLSJAVA-44949|تغيرت الشفافية عند إدراج نطاق Excel كصورة بتنسيق مختلف في شريحة PowerPoint|
|CELLSJAVA-44985|تحويل Excel إلى HTML - لا تظهر وسيلة إيضاح الرسم البياني ويتم قطع منطقة الرسم|
|CELLSJAVA-44952|مشكلة في أسلوب DataBar.toImage بخصوص العرض|
|CELLSJAVA-44986|لا تتم محاذاة الصور المستوردة في خط عندما تكون الصور بتنسيق Div|
|CELLSJAVA-44987|يتم تغطية بعض الصور من قبل الآخرين عند تحميل html|
|CELLSJAVA-44988|لا يتم تدوير النص عند تحميل html|
|CELLSJAVA-44989|تُفقد إعدادات الخط في div عند تحميل html|
|CELLSJAVA-44997|البيانات والتنسيقات المفقودة في تحويل HTML إلى Excel|
|CELLSJAVA-44999| Aspose.Cells إعدادات العولمة المخصصة لا تعمل لمعظم الجدول المحوري|

## **API العام والتغييرات غير المتوافقة مع الإصدارات السابقة**

فيما يلي قائمة بأي تغييرات تم إجراؤها على API العام مثل الأعضاء المضافين أو المعاد تسميتهم أو المحذوفون أو المهملون بالإضافة إلى أي تغيير غير متوافق مع الإصدارات السابقة تم إجراؤه على Aspose.Cells for Java. إذا كانت لديك مخاوف بشأن أي تغيير مدرج ، فيرجى رفعه في منتدى الدعم Aspose.Cells.

### **يضيف نوع JsonExportHyperlinkType**

يمثل نوع تصدير الارتباط التشعبي إلى ملفات json.

### **تضيف طريقة JsonUtility.ExportRangeToJson (Range و JsonSaveOptions) وتتخلص من طريقة ExportRangeToJson (Range ، ExportRangeToJsonOptions)**

استخدم JsonUtility.ExportRangeToJson (Range ، JsonSaveOptions) بدلاً من ذلك.

### **إضافة خاصية PivotTable.DataFieldHeaderName**

الحصول على اسم رأس حقل منطقة القيمة في PivotTable وتعيينه.

### **يضيف طريقة تجاوز Range.SetStyle (نمط ، System.Boolean)**

فقط الكتابة فوق التنسيق الذي تم تعيينه صراحة عند تعيين العلم

### **إضافة خاصية PivotField.NonAutoSortDefault**

يشير إلى ما إذا كانت عملية الفرز التي سيتم تطبيقها على هذا الحقل المحوري هي عملية فرز تلقائي أم فرز بيانات بسيط.

### **يضيف طريقة GlobalizationSettings.GetDataFieldHeaderNameOfPivotTable ()**

الحصول على الاسم المحلي لرأس حقل منطقة القيمة في PivotTable.

### **يضيف خاصية Chart.PlotVisibleCellsOnly ويقضي على خاصية Chart.PlotVisibleCells.**

استخدم خاصية Chart.PlotVisibleCellsOnly بدلاً من ذلك.

### **يضيف خاصية JsonSaveOptions.ExportEmptyCells.**

الإشارة إلى ما إذا كان يتم تصدير خلايا فارغة كخلايا فارغة.

### **يضيف خاصية JsonSaveOptions.ExportHyperlinkType.**

يمثل نوع تصدير الارتباط التشعبي إلى json.

### **يضيف خاصية JsonSaveOptions.ExportNestedStructure.**

تم تصديره كهيكل Json للتسلسل الهرمي الأصل - الفرعي.

### **إضافة خاصية JsonSaveOptions.SkipEmptyRows.**

يشير إلى ما إذا كان يتم تخطي صفوف emtpy أم لا.

### **يحذف طريقة SheetRender.GetPageSize (System.Int32) المتقادمة**

استخدم SheetRender.GetPageSizeInch (System.Int32) بدلاً من ذلك.

### **يحذف طريقة WorkbookRender.GetPageSize (System.Int32) المتقادمة**

استخدم WorkbookRender.GetPageSizeInch (System.Int32) بدلاً من ذلك.

### **حذف AutoShapeType.TextWave3 و AutoShapeType.TextWave4 المتقادم**

استخدم UseAutoShape.TextDoubleWave1 و UseAutoShape.TextDoubleWave2 بدلاً من ذلك.