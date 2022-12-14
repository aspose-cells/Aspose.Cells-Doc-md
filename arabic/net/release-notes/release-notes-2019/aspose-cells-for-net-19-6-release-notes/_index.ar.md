---
title: Aspose.Cells for .NET 19.6 ملاحظات الإصدار
type: docs
weight: 70
url: /ar/net/aspose-cells-for-net-19-6-release-notes/
---
{{% alert color="primary" %}} 

 تحتوي هذه الصفحة على ملاحظات الإصدار لـ[Aspose.Cells for .NET 19.6](https://www.nuget.org/packages/Aspose.Cells/19.6.0).

{{% /alert %}} 

|**مفتاح**|**ملخص**|**فئة**|
|:- |:- |:- |
|CELLSNET-41277|تعليقات في تصدير HTML لملفات XLS / XLSX|ميزة جديدة|
|CELLSNET-45194|دعم رسم القطاعة أثناء التقديم إلى PDF|ميزة جديدة|
|CELLSNET-46742|إضافة دعم تنسيق ملف OpenDocument Flat XML Spreadsheet (.fods)|ميزة جديدة|
|CELLSNET-46744|إضافة دعم تنسيق ملف StarOffice Calc Spreadsheet (.sxc)|ميزة جديدة|
|CELLSNET-46714|ملف OOXML مضمن كحزمة لـ XLSX.|التعزيز|
|CELLSNET-46722|تحذير أمني بعد إعادة حفظ تنسيق ملف XLS|التعزيز|
|CELLSNET-46737|مشاكل الخطوط المتوسطة / الخطوط السميكة عند حفظ XLSX كمواد ODS|التعزيز|
|CELLSNET-46755|الكشف عما إذا كان ملف الكائن مخططًا أم كائنًا أوليًا لـ ODS.|التعزيز|
|CELLSNET-46731|Worksheet.Copy () توقف التطبيق|أداء|
|CELLSNET-46770|نفاد الذاكرة عند تحديث PivotTable بمصدر بيانات كبير|أداء|
|CELLSNET-46730|Chart.ToImage () توقف التطبيق|أداء|
|CELLSNET-46670|تتداخل محتويات ملف Excel بعد إضافة خصائص مخصصة|حشرة|
|CELLSNET-46747|تتم طباعة خطوط الشبكة على الكائن المضمن أثناء التجسيد إلى PDF|حشرة|
|CELLSNET-41479|إعدادات Slicer في ملف PDF الذي تم إنشاؤه|حشرة|
|CELLSNET-41783|تحتاج الملفات التي تم إنشاؤها من ملف قالب يحتوي على أداة تقطيع إلى إصلاح|حشرة|
|CELLSNET-46733|فقد النمط / التنسيق أثناء حفظ الجدول المحوري بتنسيق HTML|حشرة|
|CELLSNET-46736|مشكلة الخط عند تحويل HTML إلى PDF|حشرة|
|CELLSNET-46751|لا يمكن تحويل XLSX إلى HTML|حشرة|
|CELLSNET-46766|لا تعمل الدالة XIRR إذا كان الصف الأخير أكبر من -62 في النطاق|حشرة|
|CELLSNET-46769|قيمة Cell المستخرجة تختلف عن Excel في الثقافة الألمانية|حشرة|
|CELLSNET-46761|مشكلة مع Aspose.Cells.GridDesktop Display عند ضبط الدقة والتكبير في شاشة 4K|حشرة|
|CELLSNET-46592|مشكلات عرض النص أثناء تحويل XLSX إلى PDF|حشرة|
|CELLSNET-46735|لا يتم إعادة تشغيل رقم الصفحة إلى 1 على كل ورقة في ملف PDF الناتج|حشرة|
|CELLSNET-46739|يتجاهل نوع ضغط Tiff تظليل الخلفية للمخططات والأشكال|حشرة|
|CELLSNET-46749|يُنشئ SheetRender.ToImage صورة EMF غير صحيحة|حشرة|
|CELLSNET-46093|لا تحترم المخططات إعداد الصفحة بالأبيض والأسود|حشرة|
|CELLSNET-46738|Aspose.Cells 19.4 تعذر فتح بعض ملفات .ots و. ods|حشرة|
|CELLSNET-46741|نتيجة غير صحيحة عند العمل مع القوائم المتداخلة|حشرة|
|CELLSNET-46748|يكون ملف الإخراج تالفًا دائمًا عند استخدام الترخيص المحدود|حشرة|
|CELLSNET-46752|تلف ملف XLSX الناتج بعد استدعاء InsertCutCells ()|حشرة|
|CELLSNET-46754|تتغير النطاقات المسماة عند استدعاء وظيفة InsertCutCells ()|حشرة|
|CELLSNET-46759|لم يظهر استثناء أثناء تحميل دفق خاطئ في المصنف|حشرة|
|CELLSNET-46043|System.InvalidCastException|استثناء|
|CELLSNET-46510|شكل على صورة خطأ! عند تحويل XLSX إلى PDF|استثناء|
|CELLSNET-46765|استثناء "System.StackOverflowException" عند تحويل ملف Excel إلى تنسيق ملف PDF|استثناء|
### **API العام والتغييرات غير المتوافقة مع الإصدارات السابقة**
فيما يلي قائمة بأي تغييرات تم إجراؤها على API العام مثل الأعضاء المضافين أو المعاد تسميتهم أو المحذوفون أو المهملون بالإضافة إلى أي تغيير غير متوافق مع الإصدارات السابقة تم إجراؤه على Aspose.Cells for .NET. إذا كانت لديك مخاوف بشأن أي تغيير مدرج ، فيرجى رفعه في منتدى الدعم Aspose.Cells.
#### **إضافة enum FileFormatType.FODS و FileFormatType.SXC و LoadFormat.FODS و LoadFormat.SXC و SaveFormat.FODS و SaveFormat.SXC**
يمثل نوعي تنسيقات الملفات .FODS و .SXC.
#### **إضافة نوع WarningType.UnsupportedFileFormat**
يمثل تنسيق ملف غير مدعوم لأنواع التحذير.
#### **يضيف تعداد ODSGeneratorType**
يمثل نوع مولد المواد المستنفدة للأوزون.
#### **OoxmlSaveOptions.EmbedOoxmlAsOleObject**
يشير إلى ما إذا كان يتم تضمين ملف ooxml كـ OleObject.
#### **إضافة Row.CopySettings (Aspose.Cells.Row ، System.Boolean)**
نسخ إعدادات الصف ، مثل النمط ، الارتفاع ، الرؤية ، ... إلخ.
