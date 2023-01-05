---
title: Aspose.Cells for .NET 19.5 ملاحظات الإصدار
type: docs
weight: 80
url: /ar/net/aspose-cells-for-net-19-5-release-notes/
---
{{% alert color="primary" %}} 

 تحتوي هذه الصفحة على ملاحظات الإصدار لـ[Aspose.Cells for .NET 19.5](https://www.nuget.org/packages/Aspose.Cells/19.5.0).

{{% /alert %}} 

|**مفتاح**|**ملخص**|**فئة**|
|:- |:- |:- |
|CELLSNET-46703|لم يتم عرض التقويم الياباني الجديد بشكل صحيح|ميزة جديدة|
|CELLSNET-46693|دعم الخلفية ODS|ميزة جديدة|
|CELLSNET-46695|تعيين خلفية ODS الملف|ميزة جديدة|
|CELLSNET-46706|ترتيب الأرقام غير صالح عند تحويل الخط العربي إلى PDF.|التعزيز|
|CELLSNET-46692|تحكم في جميع البيانات الخارجية بواجهة IStreamProvider|التعزيز|
|CELLSNET-46711|يتم دمج ImportCustomObjects إلى فواصل المنطقة المدمجة|التعزيز|
|CELLSNET-46713|دائمًا ما تعود الطريقة "String.StartsWith (" \ 0 ")" صحيحة على نظام التشغيل macOS|التعزيز|
|CELLSNET-46719|استثناء عند ضبط سلسلة HTML باستخدام نموذج ألوان RGBA|التعزيز|
|CELLSNET-46701|تتوقف معالجة المخططات الفقاعية مع الإصدار 19.4|خلل برمجي|
|CELLSNET-46682|لم يتم تحديد الخيار "إخفاء العناصر التي لا تحتوي على بيانات" لإعدادات Slicer|خلل برمجي|
|CELLSNET-46707|يُرجع PivotTable.GetChildren () عددًا خاطئًا من التبعيات|خلل برمجي|
|CELLSNET-46689|يختلف حفظ مصنف باسم PDF عن إخراج Excel الأصلي|خلل برمجي|
|CELLSNET-46704|ناتج تحويل Excel إلى PDF باستخدام Aspose.Cells يختلف عن Excel|خلل برمجي|
|CELLSNET-46720|بنية الصفحة تالفة في الصفحة الأخيرة في Excel لتحويل PDF|خلل برمجي|
|CELLSNET-46727|ترقيم الصفحات خاطئ أثناء حفظ المصنف كـ PDF|خلل برمجي|
|CELLSNET-46700|تتداخل تسميات بيانات المخطط الدائري مع بعضها البعض|خلل برمجي|
|CELLSNET-46696|يؤدي تحويل XLS باستخدام مخطط الرسم البياني Microsoft إلى XLSX و XLSM إلى حدوث خطأ محتوى غير قابل للقراءة|خلل برمجي|
|CELLSNET-46697|يؤدي تحويل XLSM باستخدام عنصر OLE إلى XLS إلى حدوث خطأ|خلل برمجي|
|CELLSNET-46712|يؤدي تحويل XLS باستخدام مخطط الرسم البياني Microsoft إلى XLSX و XLSM إلى حدوث خطأ محتوى غير قابل للقراءة|خلل برمجي|
|CELLSNET-46715|Cells.InsertCutCells () إصدار|خلل برمجي|
|CELLSNET-46725|"_x000a_"تمت إضافة السلسلة في وصف النص البديل للمخطط متعدد الأسطر|خلل برمجي|
|CELLSNET-46683|استثناء عند تحويل ملف Excel إلى PDF|استثناء|
|CELLSNET-46690|حدث استثناء أثناء تحميل مصنف Excel من Shape.ForeignData (Diagram)|استثناء|
|CELLSNET-46728|استثناء أثناء حفظ الدفق كمصنف|استثناء|
### **API العام والتغييرات غير المتوافقة مع الإصدارات السابقة**
فيما يلي قائمة بأي تغييرات تم إجراؤها على API العام مثل الأعضاء المضافين أو المعاد تسميتهم أو المحذوفون أو المهملون بالإضافة إلى أي تغيير غير متوافق مع الإصدارات السابقة تم إجراؤه على Aspose.Cells for .NET. إذا كانت لديك مخاوف بشأن أي تغيير مدرج ، فيرجى رفعه في منتدى الدعم Aspose.Cells.
#### **يضيف مُنشئ StreamProviderOptions**
خيارات StreamProviderOptions الجديدة.
#### **إضافة تعداد FileFormatType.GraphChart**
يمثل ملف الرسم البياني المضمن.
#### **يضيف خصائص ImportTableOptions.CheckMergedCells**
يشير إلى ما إذا كان التحقق من الخلايا المدمجة عند استيراد البيانات.
#### **يضيف ODSCellFieldCollection وفئات ODSCellField و ODSCellFieldType enum.**
يمثل حقل الخلية ODS.
#### **يضيف Cells.ODSCellFields Properties.**
الحصول على كشف حقول الخلايا للرقم ODS.
#### **إضافة فئة ODSPageBackground وخاصية PageSetup.ODSPageBackground**
يمثل خلفية ODS.
