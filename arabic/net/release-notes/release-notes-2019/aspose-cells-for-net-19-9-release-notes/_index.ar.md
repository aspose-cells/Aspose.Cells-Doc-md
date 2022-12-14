---
title: Aspose.Cells for .NET 19.9 ملاحظات الإصدار
type: docs
weight: 40
url: /ar/net/aspose-cells-for-net-19-9-release-notes/
---
{{% alert color="primary" %}} 

 تحتوي هذه الصفحة على ملاحظات الإصدار لـ[Aspose.Cells for .NET 19.9](https://www.nuget.org/packages/Aspose.Cells/19.9.0).

{{% /alert %}} 

|**مفتاح**|**ملخص**|**فئة**|
|:- |:- |:- |
|CELLSNET-46864|دعم القراءة والتحكم في ملفات ODS|ميزة جديدة|
|CELLSNET-46877|أضف SheetRender.ToPrinter (PrinterSettings PrinterSettings) الزائد إلى واجهات برمجة التطبيقات|ميزة جديدة|
|CELLSNET-46907|قم بتكوين مستوى ضغط ZIP لـ XLSX / XLSB|ميزة جديدة|
|CELLSNET-46890|لا يجب إسناد نتائج القسمة الصحيحة إلى متغيرات الفاصلة العائمة|حشرة|
|CELLSNET-46883|لا تحتفظ PivotTables بخيارات تحديد متعددة بعد معالجة العلامات الذكية|حشرة|
|CELLSNET-46874|القيم غير مشتقة من الصيغة وتتطلب الضغط على F2 للحصول على القيم في الخلايا|حشرة|
|CELLSNET-46904|تُفقد الارتباطات التشعبية عند استيراد البيانات من DataTable|حشرة|
|CELLSNET-46875|تجاوزت المحتويات من الصفحة أثناء تحويل PDF|حشرة|
|CELLSNET-46865|يتم تغيير كائن بعد فتحه وحفظه|حشرة|
|CELLSNET-46866|تعيين الخط وحجم الخط في Drawing.TextBox لا يعمل في ODS|حشرة|
|CELLSNET-46867|فقدت خانات الاختيار أثناء إعادة حفظ XLSX|حشرة|
|CELLSNET-46873|المرجع! تظهر كصيغة غير مطبقة|حشرة|
|CELLSNET-46876|لا يمكن الوصول إلى ارتباط كائن OLE من ملف XLS|حشرة|
|CELLSNET-46881|التجميع وفك التجميع لا يخفي الحدود|حشرة|
|CELLSNET-46884|يتم تجميع أوراق العمل أثناء استخدام VisibilityType.VeryHidden / Hidden|حشرة|
|CELLSNET-46886|جدول مع صف واحد يتوسع إلى صف إضافي واحد أدناه بعد حفظ المصنف|حشرة|
|CELLSNET-46887|لا يتم الاحتفاظ بالتنسيق الشرطي بعد فتح الملف في MS Excel وحفظه.|حشرة|
|CELLSNET-46891|تتم قراءة تعبئة التدرج اللوني لـ OleObject على أنها FillType.Solid|حشرة|
|CELLSNET-46894|لم يتم تحديد إعداد إظهار علامة تبويب الورقة أثناء حفظ ملف Excel|حشرة|
|CELLSNET-46906|Aspose.Cells معلق عند فتح ملف XLSX|حشرة|
|CELLSNET-46909|تم تغيير تنسيق كائن OLE بعد فتح ملف Excel وحفظه|حشرة|
|CELLSNET-46857|تصفية الاتصالات في المخطط المحوري تفقد الإعدادات عند الحفظ بعد تحديث الجداول المحورية|حشرة|
|CELLSNET-46862|يُفقد الإعداد "إخفاء العناصر التي لا تحتوي على بيانات" في أداة تقطيع الشرائح بعد تحديث الجداول المحورية|حشرة|
### **API العام والتغييرات غير المتوافقة مع الإصدارات السابقة**
فيما يلي قائمة بأي تغييرات تم إجراؤها على API العام مثل الأعضاء المضافين أو المعاد تسميتهم أو المحذوفون أو المهملون بالإضافة إلى أي تغيير غير متوافق مع الإصدارات السابقة تم إجراؤه على Aspose.Cells for .NET. إذا كانت لديك مخاوف بشأن أي تغيير مدرج ، فيرجى رفعه في منتدى الدعم Aspose.Cells.
#### **يزيل خاصية Chart.Rotation التي عفا عليها الزمن**
استخدم خاصية Chart.RotationAngle بدلاً من ذلك.
#### **يزيل خاصية Chart.IsDataTableShown القديمة**
استخدم Chart.ShowDataTableproperty بدلاً من ذلك.
#### **يزيل خاصية Chart.IsLegendShown القديمة**
استخدم خاصية Chart.ShowLegend بدلاً من ذلك.
#### **يزيل عفا عليها الزمن Axis.Crosses الممتلكات**
استخدم الخاصية Axis.Crosses بدلاً من ذلك.
#### **يزيل فئة عفا عليها الزمن HTMLLoadOptions**
استخدم فئة HtmlLoadOptions بدلاً من ذلك.
#### **يزيل الفئة المتقادمة JSONUtility**
استخدم class JsonUtility بدلاً من ذلك.
#### **إضافة خصائص Enum OoxmlCompressionType و XlsbSaveOptions.CompressionType و OoxmlSaveOptions.CompressionType.**
يمثل نوع الضغط لملفات OOXML.
#### **يزيل فئة ODSLoadOptions المتقادمة**
استخدم فئة OdsLoadOptions بدلاً من ذلك.




