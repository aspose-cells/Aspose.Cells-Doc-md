---
title: Aspose.Cells for .NET 19.11 ملاحظات الإصدار
type: docs
weight: 20
url: /ar/net/aspose-cells-for-net-19-11-release-notes/
---
{{% alert color="primary" %}} 

 تحتوي هذه الصفحة على ملاحظات الإصدار لـ[Aspose.Cells for .NET 19.11](https://www.nuget.org/packages/Aspose.Cells/19.11.0).

{{% /alert %}} 

|**مفتاح**|**ملخص**|**فئة**|
|:- |:- |:- |
|CELLSNET-44956|دعم لإخفاء النطاقات المحددة وفرز النتائج المعروضة من Pivot Table|ميزة جديدة|
|CELLSNET-46852|دعم جدول القراءة والكتابة الذي يكون مصدر بياناته هو جدول استعلام في ملف XLS.|ميزة جديدة|
|CELLSNET-46967|دعم للحصول على حجم المسافة البادئة بوحدة البكسل|ميزة جديدة|
|CELLSNET-46973|صيغة Excel لا تعمل في ملف XLS الذي تم إنشاؤه|التعزيز|
|CELLSNET-46981|دعم القراءة / الكتابة مع دفق الذاكرة لـ Workbook.ImportXml و Workbook.ExportXml|التعزيز|
|CELLSNET-46905|لم يتم حفظ أي تغييرات لمصدر الارتباط في ملف XLS|التعزيز|
|CELLSNET-46898|تتحول خلفية النموذج ثلاثي الأبعاد إلى اللون الأزرق|حشرة|
|CELLSNET-46314|مشاكل أثناء تحديث Pivot Table بـ "إظهار القيمة كنسبة مئوية من الإجمالي الكلي"|حشرة|
|CELLSNET-46789|طريقة CalculateData لا تعمل بشكل صحيح مع تنسيق PDF|حشرة|
|CELLSNET-46955|يثير ملف HTML إلى Excel استثناء "تمت إضافة العنصر بالفعل"|حشرة|
|CELLSNET-46987|لا يمكن حساب الصيغة عند الرجوع إلى الخلايا|حشرة|
|CELLSNET-46968|الصيغة غير المباشرة لا تعمل بشكل صحيح في MS Excel|حشرة|
|CELLSNET-46991|ملف XLSX تالف.|حشرة|
|CELLSNET-46994|# قيمة! في ملف Excel الناتج (تم فتحه في Excel 365) بعد استدعاء حساب الصيغة
|حشرة|
|CELLSNET-47001|يؤدي CalculateFormula () إلى NullReferenceException|حشرة|
|CELLSNET-46953|يتم قطع المحتوى عند الطباعة|حشرة|
|CELLSNET-46966|الحد الأيمن مفقود عند تعيين HorizontalAlignment على Fill|حشرة|
|CELLSNET-45362|لا تعمل خيارات صور التجانب مع خلفيات المخططات في ملفات XLS|حشرة|
|CELLSNET-46949|تصبح كائنات OLE صورًا عند نسخ أوراق العمل|حشرة|
|CELLSNET-46963|تفقد تسميات المخططات التنسيق بعد حفظ ملف Excel|حشرة|
|CELLSNET-46965|Calling Chart.Calculate () على مخطط فارغ يحتوي على عنوان نص تلقائي فارغ يؤدي إلى حدوث خطأ|حشرة|
|CELLSNET-46971|تقوم الورقة المنسوخة حديثًا بإلغاء إخفاء أي أعمدة مخفية وأيضًا إعادة تعيين عرض الأعمدة|حشرة|
|CELLSNET-46972|تمت إزالة الفاصلة من عناوين المخططات بمجرد فك تشفير ملف Excel|حشرة|
|CELLSNET-46912|تم طرح StackOverflowException أثناء تحويل XLSX إلى HTML|استثناء|
### **API العام والتغييرات غير المتوافقة مع الإصدارات السابقة**
فيما يلي قائمة بأي تغييرات تم إجراؤها على API العام مثل الأعضاء المضافين أو المعاد تسميتهم أو المحذوفون أو المهملون بالإضافة إلى أي تغيير غير متوافق مع الإصدارات السابقة تم إجراؤه على Aspose.Cells for .NET. إذا كانت لديك مخاوف بشأن أي تغيير مدرج ، فيرجى رفعه في منتدى الدعم Aspose.Cells.
#### **إضافة طرق: Validation.AddArea (CellArea، bool، bool)، AddAreas (CellArea []، bool، bool)، RemoveAreas (CellArea [])**
يضيف / يزيل إعدادات التحقق من الصحة من منطقة (مناطق) معينة مع مراعاة الأداء.
#### **يضيف Workbook.ImportXml (دفق دفق ، سلسلة sheetName ، int row ، int col).**
يستورد دفق ملف XML في المصنف.
#### **يضيف طريقة Workbook.ExportXml (سلسلة mapName ، دفق تيار).**
تصدير بيانات XML إلى دفق.
#### **يضيف خاصية HtmlSaveOptions.ExportArea**
الحصول على أو تعيين CellArea المصدرة لورقة العمل النشطة الحالية. إذا قمت بتعيين هذه السمة ، فسيتم حذف منطقة الطباعة الخاصة بورقة العمل النشطة الحالية. سيتم تصدير المنطقة المحددة فقط عند حفظ الملف بتنسيق HTML.
#### **إضافة فئات: DataMashup و PowerQueryFormula و PowerQueryFormulaCollection و PowerQueryFormulaItem و PowerQueryFormulaItemCollection**
يحصل على معلومات في DataMashup.
#### **يضيف خاصية DBConnection.SeverCommand.**
الحصول على سلسلة نصية ثانية للأمر وتعيينها والتي تستمر عندما تكون حقول الصفحة المستندة إلى الخادم PivotTable قيد الاستخدام.
#### **يضيف طريقة CellsHelper.GetTextWidth ().**
الحصول على عرض النص بوحدة النقاط.
