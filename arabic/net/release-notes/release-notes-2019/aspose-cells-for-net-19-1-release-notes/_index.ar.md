---
title: Aspose.Cells for .NET 19.1 ملاحظات الإصدار
type: docs
weight: 120
url: /ar/net/aspose-cells-for-net-19-1-release-notes/
---
{{% alert color="primary" %}} 

 تحتوي هذه الصفحة على ملاحظات الإصدار لـ[Aspose.Cells for .NET 19.1](https://www.nuget.org/packages/Aspose.Cells/19.1.0).

{{% /alert %}} 

|**مفتاح**|**ملخص**|**فئة**|
|:- |:- |:- |
|CELLSNET-46429|إضافة PivotTable مع خيار إظهار صفحات تصفية التقرير|ميزة جديدة|
|CELLSNET-46014|دعم التعامل مع محتوى الخلية الفائض أثناء الحفظ بتنسيق PDF وصورة|ميزة جديدة|
|CELLSNET-46490|دعم ملفات Excel95 / 5.0 XLS|ميزة جديدة|
|CELLSNET-46500|الفرز حسب لون خلفية الخلية|ميزة جديدة|
|CELLSNET-46544|اكتشف ما إذا كان ملف MHT الذي تم إنشاؤه عبارة عن ورقة عمل أم لا|ميزة جديدة|
|CELLSNET-46538|عند حفظ XLSX كملف PDF أو TIFF ، يكون الجزء السفلي من النص مفقودًا|حشرة|
|CELLSNET-46509|تتم قراءة صيغ R1C1 بشكل غير صحيح لخلايا معينة|حشرة|
|CELLSNET-46513|يقوم محرك حساب الصيغة Aspose.Cells بحساب صيغة الخلية كـ "0" بدلاً من "#REF!" خطأ|حشرة|
|CELLSNET-46535|"#اسم؟" للصيغ المحفوظة بتنسيق XLSB|حشرة|
|CELLSNET-46539|قضية حساسة لحالة الصيغة|حشرة|
|CELLSNET-46531|إعادة تسمية مصنف ListColumns يفسد (عندما يكون هناك PivotTable)|حشرة|
|CELLSNET-46511|تم إنشاء TIFF بصفحات فارغة إضافية|حشرة|
|CELLSNET-46522|تطبيق الإعدادات الإقليمية لطباعة رؤوس الإعداد|حشرة|
|CELLSNET-46529|الصورة مفقودة بعد تحويل XLSX إلى PDF|حشرة|
|CELLSNET-46451|مشكلة عند تحويل ملف القالب إلى تنسيق ملف PDF|حشرة|
|CELLSNET-46518|مشكلة التخطيط (توجد بعض تسميات المحور في سطرين) عند تحويل ملف القالب إلى تنسيق ملف PDF|حشرة|
|CELLSNET-46113|تنسيق الملف ليس استثناءً مدعومًا لوثيقة XLS|حشرة|
|CELLSNET-46504|مشكلة مسار الروابط|حشرة|
|CELLSNET-46506|الاختلاف مع طريقة ImportObjectArray|حشرة|
|CELLSNET-46541|مخطط التحرير والسرد لا يعمل مع الإصدار 18.12.x ولكنه يعمل مع الإصدار 18.4 والإصدارات السابقة|حشرة|
|CELLSNET-46543|استثناء أثناء استدعاء Cells.DeleteBlankRows|استثناء|
|CELLSNET-46459|يظهر استثناء أثناء التحويل إلى تنسيق Open Strict XML|استثناء|
|CELLSNET-46485|استثناء عند تحميل تنسيق ملف XLSB|استثناء|
|CELLSNET-46508|استثناء عند تحميل تنسيق ملف XLSM|استثناء|
### **API العام والتغييرات غير المتوافقة مع الإصدارات السابقة**
فيما يلي قائمة بأي تغييرات تم إجراؤها على API العام مثل الأعضاء المضافين أو المعاد تسميتهم أو المحذوفون أو المهملون بالإضافة إلى أي تغيير غير متوافق مع الإصدارات السابقة تم إجراؤه على Aspose.Cells for .NET. إذا كانت لديك مخاوف بشأن أي تغيير مدرج ، فيرجى رفعه في منتدى الدعم Aspose.Cells.
#### **يضيف أسلوب PivotTable.ShowReportFilterPageByName (سلسلة fieldName)**
إظهار كافة صفحات عامل تصفية التقرير وفقًا لاسم PivotField ، ويجب أن يكون PivotField موجودًا في PageFields.
#### **إضافة طريقة PivotTable.ShowReportFilterPageByIndex (int posIndex)**
يعرض كل صفحات تصفية التقرير وفقًا لفهرس الموضع في PageFields.
#### **يضيف أسلوب PivotTable.ShowReportFilterPage (PivotField pageField)**
إظهار كافة صفحات عامل تصفية التقرير وفقًا لـ PivotField ، يجب أن يكون PivotField موجودًا في PageFields.
#### **يضيف فئة DataSorterKey و DataSorterKeyCollection**
يمثل مفتاح فارز البيانات.
#### **يضيف طريقة DataSorter.AddKey (Int32 ، SortOnType ، SortOrder ، كائن)**
يضيف مفتاح الفرز مثل لون خلفية الخلية ولون الخط.
#### **يضيف Aspose.Cells.DataSorter.Keys خاصية**
يحصل على جميع مفاتيح فارز البيانات.
#### **يضيف تعداد SortOnType**
يمثل نوع البيانات التي تم فرزها.
#### **يضيف فئة ODSLoadOptions**
يمثل خيارات تحميل ملف ODS.
#### **يضيف خاصية HTMLLoadOptions.ProgId**
يحصل على معرف البرنامج الخاص بإنشاء الملف. تستخدم فقط لملفات MHT.
#### **يضيف خاصية PdfSaveOptions.TextCrossType**
الحصول على عرض نوع النص أو تعيينه عندما يكون عرض النص أكبر من عرض الخلية.
#### **يضيف فئة تعداد TextCrossType**
تعداد عرض نوع النص عندما يكون عرض النص أكبر من عرض الخلية.
#### **يضيف أساليب WorksheetCollection.RegisterAddInFunction ()**
استبدال Cell.SetAddInFormula () ، طريقة أكثر ملاءمة وفعالية للمستخدمين لإضافة واستخدام الوظائف الإضافية.
#### **عفا عليها الزمن Cell.SetAddInFormula () طريقة**
يرجى تسجيل الدالات الإضافية أولاً بواسطة WorksheetCollection.RegisterAddInFunction () ثم قم بتعيين الصيغة لـ Cell بواسطة Cell.Formula / Cell.SetFormula () بدلاً من ذلك.
