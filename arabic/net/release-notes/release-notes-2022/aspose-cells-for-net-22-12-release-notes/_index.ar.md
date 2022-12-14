---
title: Aspose.Cells for .NET 22.12 ملاحظات الإصدار
type: docs
weight: 1
url: /ar/net/aspose-cells-for-net-22-12-release-notes/
---
{{% alert color="primary" %}}

 تحتوي هذه الصفحة على ملاحظات الإصدار لـ[Aspose.Cells for .NET 22.12](https://www.nuget.org/packages/Aspose.Cells/22.12.0).

{{% /alert %}}

|**مفتاح**|**ملخص**|**فئة**|
|:- |:- |:- |
|CELLSNET-42315|دعم ملفات crtx - تطبيق قوالب الرسوم البيانية المخصصة|
|CELLSNET-47895|الصور مشوهة في تحويل Excel إلى PDF / HTML|
|CELLSNET-47946|لا يتم عرض تأثير تدوير الصورة بشكل صحيح في pdf / html|
|CELLSNET-47947|لا يتم عرض تأثير دوران الصندوق المستطيل في مجموعة الرسومات بشكل صحيح في pdf / html|
|CELLSNET-52126|يتم تغيير بعض الأشكال بعد تحويل ملف Excel إلى PDF|
|CELLSNET-52197|تم تغيير المربعات عند تحويل مستند XLSX إلى PDF|
|CELLSNET-52330|لا يتم عرض أشكال الرسم بشكل جيد في HTML|
|CELLSNET-50042| يتم تغيير الاسم المحدد بعد إعادة الحفظ|
|CELLSNET-52270|لم يتم حساب دالة YEARFRAC بشكل صحيح|
|CELLSNET-52305|لم يتم حساب MMULT مع OFFSET بشكل صحيح|
|CELLSNET-52307|ترجع صيغة الارتباط المقطوع 0 بدلاً من #REF!|
|CELLSNET-52325| Workbook.CalculateFormula معلق في بعض الظروف|
|CELLSNET-52387|ينتج عن مراجع Cell للجداول أخطاء #REF بعد حذف الأعمدة|
|CELLSNET-52290|لم يتم التقاط محور المخططات بشكل صحيح|
|CELLSNET-52301|مخطط XLSX إلى صورة: تم تقديم أشرطة مخطط التحرير والسرد المخصصة بشكل غير صحيح|
|CELLSNET-52336|لا يتم عرض مخطط المدرج التكراري بشكل صحيح في تحويل XLSX إلى HTML / PDF|
|CELLSNET-52292|يتم عرض النص على الصفحة الخطأ في ملف PDF الناتج - تحويل Excel إلى PDF|
|CELLSNET-52367|ينتج عن AutofitRows نص مقتطع في إخراج تحويل PDF|
|CELLSNET-52242|التسلسل الهرمي للوالدين والطفل غير صحيح أثناء تحويل Excel إلى JSON والعكس صحيح|
|CELLSNET-52281|لا يمكن تجاهل رأس Json|
|CELLSNET-52289|يتم فقدان تنسيق الأرقام عند تحويل HTML إلى Excel|
|CELLSNET-52298|يتم تمكين خيار الفرز التلقائي للحقل المحوري عند إعادة حفظ XLSX|
|CELLSNET-52299| سمة HasRevisions غير صحيحة بعد حفظ مصنف|
|CELLSNET-52332|يتم عرض الأرقام كـ "#" أو رقم علمي أثناء التحويل إلى html|
|CELLSNET-52338| الناتج HTML غير محدد|
|CELLSNET-52344|الروابط التشعبية مفقودة في تحويل HTML إلى JSON|

## **API العام والتغييرات غير المتوافقة مع الإصدارات السابقة**

فيما يلي قائمة بأي تغييرات تم إجراؤها على API العام مثل الأعضاء المضافين أو المعاد تسميتهم أو المحذوفون أو المهملون بالإضافة إلى أي تغيير غير متوافق مع الإصدارات السابقة تم إجراؤه على Aspose.Cells for .NET. إذا كانت لديك مخاوف بشأن أي تغيير مدرج ، فيرجى رفعه في منتدى الدعم Aspose.Cells.

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
