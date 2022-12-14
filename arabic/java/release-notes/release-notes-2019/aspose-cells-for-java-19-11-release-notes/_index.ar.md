---
title: Aspose.Cells for Java 19.11 ملاحظات الإصدار
type: docs
weight: 20
url: /ar/java/aspose-cells-for-java-19-11-release-notes/
---
{{% alert color="primary" %}} 

تحتوي هذه الصفحة على ملاحظات إصدار Aspose.Cells for Java 19.11.

{{% /alert %}} 

|**مفتاح**|**ملخص**|**فئة**|
|:- |:- |:- |
|CELLSJAVA-43032|إضافة طريقة Validation.addArea (CellArea cellArea ، boolean skipArea) أو طريقة Validation.setAreas () / التحميلات الزائدة إلى واجهات برمجة التطبيقات|ميزة جديدة|
|CELLSJAVA-42851|احصل على تفاصيل اتصال ODATA|ميزة جديدة|
|CELLSJAVA-43018|تصدير نطاق منطقة الطباعة إلى HTML دون تغيير بعض حالات المصنف ضمنيًا|التعزيز|
|CELLSJAVA-43041|Cells.importCSV يطرح استثناء "لا يمكن أن تتجاوز قيمة السلسلة 255 حرفًا"|التعزيز|
|CELLSJAVA-43043|Cells.remove - تستغرق المضاعفات وقتًا أطول لمجموعة البيانات الكبيرة|التعزيز|
|CELLSJAVA-43019|لم يتم تقديم الرسم البياني الشعاعي بشكل صحيح إلى HTML|حشرة|
|CELLSJAVA-43027|بعد التسليم إلى PNG ، يختلف مقياس المحور.|حشرة|
|CELLSJAVA-42474|لا يتم تحديث PivotTable وتلف بعد تحديث البيانات المصدر|حشرة|
|CELLSJAVA-43033|التحويل إلى PDF لا ينتهي.|حشرة|
|CELLSJAVA-43034|تم استرداد إخراج تنسيق التاريخ الروسي (المخصص) غير صالح|حشرة|
|CELLSJAVA-43040|لا يأخذ LoadFilter الورقة المطلوبة في الاعتبار|حشرة|
|CELLSJAVA-43035|يتم فقد الحدود أثناء تحويل ملف Excel إلى EMF|حشرة|
|CELLSJAVA-43016|عدد الصفحات غير صالح من SheetRender|حشرة|
|CELLSJAVA-43026|بعد تقديم المخطط إلى صورة ما ، تغير تسميات البيانات النمط والقيم ليست هي نفسها|حشرة|
|CELLSJAVA-43038|لم يتم تصدير الارتباطات التشعبية باستخدام Cell.setHtmlString ()|حشرة|
|CELLSJAVA-43039|Cell.setHtmlString () لا يعرض علامات / نصوص HTML معينة لتصدير Excel|حشرة|

## **API العام والتغييرات غير المتوافقة مع الإصدارات السابقة**
فيما يلي قائمة بأي تغييرات تم إجراؤها على API العام مثل الأعضاء المضافين أو المعاد تسميتهم أو المحذوفون أو المهملون بالإضافة إلى أي تغيير غير متوافق مع الإصدارات السابقة تم إجراؤه على Aspose.Cells for Java. إذا كانت لديك مخاوف بشأن أي تغيير مدرج ، فيرجى رفعه في منتدى الدعم Aspose.Cells.
### **إضافة طرق: Validation.AddArea (CellArea، bool، bool)، AddAreas (CellArea []، bool، bool)، RemoveAreas (CellArea [])**
يضيف / يزيل إعدادات التحقق من الصحة من منطقة (مناطق) معينة مع مراعاة الأداء.
### **يضيف Workbook.ImportXml (دفق دفق ، سلسلة sheetName ، int row ، int col).**
يستورد دفق ملف XML في المصنف.
### **يضيف طريقة Workbook.ExportXml (سلسلة mapName ، دفق تيار).**
تصدير بيانات XML إلى دفق.
### **يضيف خاصية HtmlSaveOptions.ExportArea**
الحصول على أو تعيين CellArea المصدرة لورقة العمل النشطة الحالية. إذا قمت بتعيين هذه السمة ، فسيتم حذف منطقة الطباعة الخاصة بورقة العمل النشطة الحالية. سيتم تصدير المنطقة المحددة فقط عند حفظ الملف بتنسيق HTML.
### **إضافة فئات: DataMashup و PowerQueryFormula و PowerQueryFormulaCollection و PowerQueryFormulaItem و PowerQueryFormulaItemCollection**
يحصل على معلومات في DataMashup.
### **يضيف خاصية DBConnection.SeverCommand.**
الحصول على سلسلة نصية ثانية للأمر وتعيينها والتي تستمر عندما تكون حقول الصفحة المستندة إلى الخادم PivotTable قيد الاستخدام.
### **يضيف طريقة CellsHelper.GetTextWidth ().**
الحصول على عرض النص بوحدة النقاط.
