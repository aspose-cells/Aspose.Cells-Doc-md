---
title: Aspose.Cells for .NET 22.4 ملاحظات الإصدار
type: docs
weight: 9
url: /ar/net/aspose-cells-for-net-22-4-release-notes/
---
{{% alert color="primary" %}}

 تحتوي هذه الصفحة على ملاحظات الإصدار لـ[Aspose.Cells for .NET 22.4](https://www.nuget.org/packages/Aspose.Cells/22.4.0).

{{% /alert %}}

|**مفتاح**|**ملخص**|**فئة**|
|:- |:- |:- |
|CELLSNET-50624|دعم لإزالة خلايا فارغة ذيل لحفظ ملف CSV|
|CELLSNET-50747|أضف Style.HasBorders للتحقق من وجود حدود لها|
|CELLSNET-50627|احصل على نطاق مدمج فيما يتعلق بخلية ورقة العمل في Aspose.Cells.GridDesktop|
|CELLSNET-50675|إضافة GridLoadDataFilterOptions لـ GridDesktop و Worksheet. GetMergeByCell api|
|CELLSNET-50816|دعم تصميم عالي التباين في Aspose.Cells.GridDesktop|
|CELLSNET-50751|دعم PasteType.ValuesAndFormats عند نسخ النطاق.|
|CELLSNET-50620|عند تحويل xls إلى pdf ، لا يتم عرض حجم سطر النص الفارغ في مربع النص بشكل صحيح|
|CELLSNET-50684|مشكلة تتعلق باستخراج مرفقات OLE من ملف ODS|
|CELLSNET-50712|لا يتم عرض تأثيرات وأشكال WordArt بشكل صحيح في Excel لتحويل PDF|
|CELLSNET-50714|الملف XLSB تالف عند الفتح والحفظ بواسطة Aspose.Cells APIs|
|CELLSNET-50778|الخطوط العمودية مفقودة للجدول المحوري في الإخراج PDF|
|CELLSNET-50517|مرجع خاطئ في صيغة التنسيق الشرطي بعد إدراج / حذف الصفوف|
|CELLSNET-50622|لا يتم تصدير عنوان صف / عمود فارغ بنمط مخصص إلى ملف csv|
|CELLSNET-50645|نتائج غير صحيحة باستخدام طريقة Workbook.CalculateFormula|
|CELLSNET-50695|Name.RefersTo / R1C1RefersTo للتغيير عند الرجوع إلى عنوان خلية مفردة|
|CELLSNET-50553| لا يتم تطبيق نمط العمود على عمود كامل في GridDesktop|
|CELLSNET-50641|مشكلة في فتح ملف محمي بكلمة مرور بكلمة مرور فارغة ("") إلى Aspose.Cells.GridDesktop|
|CELLSNET-50672|إضافة حدث FailLoadFile|
|CELLSNET-50815| انقر نقرًا مزدوجًا على تعديل سلوك قيمة الخلية غير صحيح|
|CELLSNET-50594|يتم إخفاء النص خلف حقول الإدخال عند التحويل من XLSX إلى HTML|
|CELLSNET-50665|فشل التحقق من صحة Pdf / A-1b بعد تعيين CreatedTime أثناء التحويل إلى pdf|
|CELLSNET-50701|تتم إعادة ضبط سطوع الصورة المدرجة وتباينها في برنامج Excel إلى تحويل PDF|
|CELLSNET-50834|مشكلة في الخلايا المدمجة في الجدول في Excel لتحويل HTML|
|CELLSNET-50595|XLSX إلى SVG: الاختلافات في الرسم البياني|
|CELLSNET-50596|لا يتم تغيير وحدات المحور في ملف الإخراج XLSX|
|CELLSNET-50740|XLSX إلى JPG: تم إزاحة النص إلى الجانب الأيمن على الرسوم البيانية|
|CELLSNET-50309|النطاق حتى PNG: الإخراج ليس كما هو متوقع|
|CELLSNET-50610|RecalculateBeforeSave دائمًا كاذب في الإصدار الأحدث|
|CELLSNET-50611|مشكلة في القيمة المنطقية في Excel لعرض PDF|
|CELLSNET-50706| تم تقليل حجم الملف عدة مرات عند الحفظ باستخدام SaveToStream () في المرة الثانية|
|CELLSNET-50749| طريقة DeleteBlankColumns (خيارات) لحذف الأعمدة التي تحتوي على تعليقات فقط|
|CELLSNET-50759|لا يتم حفظ الصيغ بشكل صحيح عندما يحتوي المصنف على ارتباطات خارجية بمصنف لم يتم حفظه|
|CELLSNET-50776|لا تتم معالجة العلامات الذكية عند استخدام قائمة عامة من النوع System.Dynamic.ExpandoObject كمصدر بيانات لكائنات متداخلة|
|CELLSNET-50779| فقدان البيانات المحتمل فيما يتعلق بالكائنات المضمنة أثناء التحويل XLS -> XLSX -> XLS|
|CELLSNET-50821|مشكلة متعلقة بـ Range.AutoFill - لا يتم ملء البيانات تلقائيًا بشكل صحيح إذا كانت منطقة النطاق متقاطعة|
|CELLSNET-50777|يطرح أسلوب PutValue System.StackOverflowException بالتنسيق الإقليمي الأسترالي|
|CELLSNET-50275|استثناء "لم يتم تعيين مرجع الكائن لمثيل كائن" عند التقديم ODS إلى HTML|
|CELLSNET-50713|System.NullReferenceException عند تحميل ملف XLSB|

## **API العام والتغييرات غير المتوافقة مع الإصدارات السابقة**

فيما يلي قائمة بأي تغييرات تم إجراؤها على API العام مثل الأعضاء المضافين أو المعاد تسميتهم أو المحذوفون أو المهملون بالإضافة إلى أي تغيير غير متوافق مع الإصدارات السابقة تم إجراؤه على Aspose.Cells for .NET. إذا كانت لديك مخاوف بشأن أي تغيير مدرج ، فيرجى رفعه في منتدى الدعم Aspose.Cells.

### **يضيف فئة DefaultStyleSettings.**

مجموعة من القيم الافتراضية للخصائص ذات الصلة بالنمط.

### **يضيف خاصية LoadOptions.DefaultStyleSettings.**

دعم لتعيين القيم الافتراضية للخصائص ذات الصلة بالنمط لتهيئة مصنف.

### **يضيف خاصية TxtSaveOptions.TrimTailingBlankCells.**

دعم لإزالة جميع الخلايا الفارغة (الأحرف المتكررة للفاصل مثل "~ ، ~ ، ~ ، ~ ،") في نهاية سجل الصف عند تصدير csv / tsv.

### **يضيف خاصية Style.HasBorders.**

دعم للتحقق مما إذا كانت هناك حدود تم تعيينها للأسلوب.

### **تقادم LoadOptions.StandardFont / StandardFontSize خصائص.**

الرجاء استخدام LoadOptions.DefaultStyleSettings.FontName / FontSize بدلاً من ذلك.

### **يزيل التعداد المتقادم StyleModifyFlag.FontSubscript و FontSuperscript.**

الرجاء استخدام StyleModifyFlag.FontScript بدلاً من ذلك.

### **شكل قديم. خصائص نقاط الاتصال.**

استخدم طريقة GetConnectionPoints () بدلاً من ذلك.

### **يضيف طريقة Shape.GetConnectionPoints ().**

احصل على نقاط الاتصال.

### **يضيف Row.IsCollapsed و Column.IsCollapsed Properties.**

يشير إلى ما إذا كان الصف والعمود مطويًا أم لا.

### **يضيف PasteType.ValuesAndFormats enum.**

يشير فقط إلى نسخ القيم والتنسيقات.

### **يضيف خاصية Shape.IsInGroup.**

يشير إلى ما إذا كان الشكل مجمّعًا أم لا.

### **يضيف طريقة AutoFilter.GetCellArea ().**

يحصل على المنطقة التي ينطبق عليها التصفية التلقائية المحددة.

### **يضيف Cells.GetRowOriginalHeightPoint () طريقة.**

الحصول على ارتفاع الصف الأصلي بوحدة النقاط.

### **يضيف طريقة TimelineCollection.Add (PivotTable pivot ، سلسلة destCellName ، PivotField baseField).**

أضف مخططًا زمنيًا جديدًا باستخدام PivotTable كمصدر بيانات.

### **يضيف طريقة TimelineCollection.Add (PivotTable pivot ، int row ، int عمود ، PivotField baseField).**

أضف مخططًا زمنيًا جديدًا باستخدام PivotTable كمصدر بيانات.

### **يضيف طريقة TimelineCollection.Add (PivotTable pivot ، سلسلة destCellName ، int baseFieldIndex).**

أضف مخططًا زمنيًا جديدًا باستخدام PivotTable كمصدر بيانات.

### **يضيف طريقة TimelineCollection.Add (PivotTable pivot ، int row ، int column ، int baseFieldIndex).**

أضف مخططًا زمنيًا جديدًا باستخدام PivotTable كمصدر بيانات.

### **يضيف طريقة TimelineCollection.Add (PivotTable pivot ، سلسلة destCellName ، سلسلة baseFieldName).**

أضف مخططًا زمنيًا جديدًا باستخدام PivotTable كمصدر بيانات.

### **يضيف DataLabelShapeType.Line enum.**

يمثل شكل الخط. هذا النوع غير متوفر في Excel ، ويستخدم فقط لبعض الملفات الخاصة.
