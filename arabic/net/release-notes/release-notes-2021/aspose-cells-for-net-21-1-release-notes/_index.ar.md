---
title: Aspose.Cells for .NET 21.1 ملاحظات الإصدار
type: docs
weight: 30
url: /ar/net/aspose-cells-for-net-21-1-release-notes/
---
{{% alert color="primary" %}}

 تحتوي هذه الصفحة على ملاحظات الإصدار لـ[Aspose.Cells for .NET 21.1](https://www.nuget.org/packages/Aspose.Cells/21.1.0).

{{% /alert %}}

|**مفتاح**|**ملخص**|**فئة**|
|:- |:- |:- |
|CELLSNET-47376|الإصدار Aspose.Cells for .NET 5.0|ميزة جديدة|
|CELLSNET-40624| كيفية تبديل سلسلة بيانات الصف / العمود باستخدام aspose|ميزة جديدة|
|CELLSNET-42195|تحويل التحكم من xlsm إلى xls|ميزة جديدة|
|CELLSNET-47806|يحصل على نطاق مصدر البيانات للمخطط.|ميزة جديدة|
|CELLSNET-47756|لا يتم عرض أشكال SmartArt بشكل جيد في تحويل Excel إلى PDF|حشرة|
|CELLSNET-47391|لم يتم وضع الأشكال بشكل صحيح في تحويلات Excel إلى pdf|حشرة|
|CELLSNET-47766|الرسم البياني للسهم غير مكتمل|حشرة|
|CELLSNET-47653|Diagram يتم إزاحة الكتل عند التحويل إلى HTML|حشرة|
|CELLSNET-47720|ترميز CSS و HTML غير صالح عند تحويل XLSX إلى HTML|حشرة|
|CELLSNET-47746|علامات الاقتباس غير المشفرة في قيم سمات HTML|حشرة|
|CELLSNET-47792|الصور تتداخل مع النص عند استيراد html إلى excel|حشرة|
|CELLSNET-47797|ارتباط غير صالح عند عرض ملف XLSM بتنسيق HTML|حشرة|
|CELLSNET-47807|ترميز HTML غير صالح مع عناصر متداخلة|حشرة|
|CELLSNET-47778|يتم تقييم عملية حساب IRR إلى #NUM|حشرة|
|CELLSNET-47814|أشرطة التمرير GridDesktop ليست مخفية|حشرة|
|CELLSNET-47744|يتم سحق المخططات الشعاعية عند تصديرها إلى pdf|حشرة|
|CELLSNET-47786|لا يتم عرض XErrorBar في المخطط|حشرة|
|CELLSNET-47787|يختفي XErrorBars عند نسخ مخطط من مصنف إلى آخر|حشرة|
|CELLSNET-43907|لا يتم تقديم WordArt أثناء تحويل XLS إلى PDF|حشرة|
|CELLSNET-47780|مشكلة في تحديد نطاقين كمصدر بيانات للرسم البياني|حشرة|
|CELLSNET-47781|التفاف النص لا يعمل لملفات ODS|حشرة|
|CELLSNETCORE-94| تتزايد مجموعة الجدول المحوري حسب اليوم عند التحديث|حشرة|
|CELLSNETCORE-77|خطأ أثناء تحويل XLSX إلى PDF على Azure|حشرة|
|CELLSNETCORE-90|مشاكل أثناء إدراج المرفقات في ورقة عمل Excel|حشرة|
|CELLSNETCORE-93|لم يتم عرض علامة H1 بدون علامات إضافية مثل تسطير أو مائل أو غامق|حشرة|
|CELLSNETCORE-97|استدعاء RemoveExternalLinks () يثير استثناء|حشرة|
|CELLSNET-47719|فشل حفظ xlsb في xlsx|استثناء|
|CELLSNET-47784|استثناء أثناء استيراد مستند HTML باستخدام IStreamProvider|استثناء|
|CELLSNET-47801|يطرح CalculateData في جدول pivot استثناءً|استثناء|
|CELLSNET-47809|Cell.ContainsExternalLink رميات "تعذر الإرسال|استثناء|
|CELLSNET-47791| تسبب التخطيط في Workbook.Save فشل|استثناء|
|CELLSNET-47808|تم رفع الاستثناء أثناء حساب مخطط فارغ|استثناء|
|


## **API العام والتغييرات غير المتوافقة مع الإصدارات السابقة**

فيما يلي قائمة بأي تغييرات تم إجراؤها على API العام مثل الأعضاء المضافين أو المعاد تسميتهم أو المحذوفون أو المهملون بالإضافة إلى أي تغيير غير متوافق مع الإصدارات السابقة تم إجراؤه على Aspose.Cells for .NET. إذا كانت لديك مخاوف بشأن أي تغيير مدرج ، فيرجى رفعه في منتدى الدعم Aspose.Cells.

### **يحذف ReplaceOptions.ScaseSensitive المتقادمة (.NET فقط).**

استخدم ReplaceOptions.CaseSensitive بدلاً من ذلك.

### **مُنشئ PdfSaveOptions (SaveFormat) قديم.**

استخدم مُنشئ PdfSaveOptions () بدلاً من ذلك.

### **مُنشئ XlsbSaveOptions (SaveFormat) قديم.**

استخدم مُنشئ XlsbSaveOptions () بدلاً من ذلك.

### **مُنشئ XlsSaveOptions (SaveFormat) قديم.**

استخدم مُنشئ XlsSaveOptions () بدلاً من ذلك.

### **مُنشئ SpreadsheetML2003SaveOptions (SaveFormat) المتقادم.**

استخدم مُنشئ SpreadsheetML2003SaveOptions () بدلاً من ذلك.

### **يضيف طريقة Chart.GetChartDataRange ().**

يحصل على مصدر نطاق البيانات للرسم البياني.

### **يضيف طريقة Chart.SwitchRowColumn ().**

يقوم بتبديل الصف / العمود لمصدر نطاق بيانات المخطط.

### **يضيف أسلوب OleObject.SetEmbeddedObject ().**

يضبط الكائن المضمّن.

### **يضيف طريقة VbaProject.ValidatePassword ().**

 
يتحقق من صحة كلمة مرور مشروع VBA.

### **حذف خصائص ChartPoint.MarkerBackgroundColor و Series.MarkerBackgroundColor القديمة ، وإضافة خاصية Marker.BackgroundColor.**

يستخدم Marker.BackgroundColor بدلاً من ذلك.

### **حذف خصائص ChartPoint.MarkerForegroundColor و Series.MarkerForegroundColor القديمة ، وإضافة خاصية Marker.ForegroundColor.**

يستخدم Marker.ForegroundColor بدلاً من ذلك.

### **حذف خصائص ChartPoint.MarkerBackgroundColorSetType و Series.MarkerBackgroundColorSetType القديمة ، وإضافة خاصية Marker.BackgroundColorSetType.**

يستخدم Marker.BackgroundColorSetType بدلاً من ذلك.

### **حذف خصائص ChartPoint.MarkerForegroundColorSetType القديمة و Series.MarkerForegroundColorSetType ، وإضافة خاصية Marker.ForegroundColorSetType.**

يستخدم Marker.ForegroundColorSetType بدلاً من ذلك.

### **حذف خصائص ChartPoint.MarkerSize و Series.MarkerSize المتقادمة.**

يستخدم Marker.MarkerSize بدلاً من ذلك.

### **يحذف خصائص ChartPoint.MarkerStyle و Series.MarkerStyle القديمة.**

يستخدم Marker.MarkerStyle بدلاً من ذلك.

