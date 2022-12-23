---
title: Aspose.Cells for .NET 22.2 ملاحظات الإصدار
type: docs
weight: 11
url: /ar/net/aspose-cells-for-net-22-2-release-notes/
---
{{% alert color="primary" %}}

 تحتوي هذه الصفحة على ملاحظات الإصدار لـ[Aspose.Cells for .NET 22.2](https://www.nuget.org/packages/Aspose.Cells/22.2.0).

{{% /alert %}}

|**مفتاح**|**ملخص**|**فئة**|
|:- |:- |:- |
|CELLSNET-50332| قم باستخراج كافة مجموعات الأسماء من ورقة عمل معينة|
|CELLSNET-50353|أضف خاصية StandardHeightInch في فئة Cells|
|CELLSNET-50152| مشاكل عرض التنسيقات المختلفة والأشكال الأخرى في PDF و HTML من ملف Excel|
|CELLSNET-50300|لا يتم تقديم بعض الأشكال بشكل صحيح في Excel لتحويل PDF|
|CELLSNET-50301|قيمة غير صالحة للمرجع الخارجي في حقل DataSource في Pivot Table|
|CELLSNET-50241|الانحدار: التحويل من CSV إلى PDF لا يعمل|
|CELLSNET-50268|تم إرجاع صفيف CellsArea فارغ لملفات CSV/TSV|
|CELLSNET-50269|اللغة الفنلندية - Numbers المنسق كنسبة مئوية يفتقد المسافة قبل رمز النسبة المئوية|
|CELLSNET-50333|فشل Aspose.cell في تجميع سجلات مراجعة المصنف|
|CELLSNET-50239|الصفحة المفقودة بعد تحويل ملف Excel إلى PDF|
|CELLSNET-50255|نوع Cell خطأ بعد التصدير إلى html وإعادة تحميل html المُصدَّر|
|CELLSNET-50266|Chart.ToImage () مشكلة أمان الموضوع|
|CELLSNET-50302|الانحدار: التحويل إلى HTML لم يتم تقديمه بشكل صحيح|
|CELLSNET-50328|Cell تصبح الخلفية سوداء بعد التحويل إلى pdf|
|CELLSNET-50225| تم إرجاع وسيلة إيضاح الرسم البياني عند حفظ Excel بالرقم PDF|
|CELLSNET-50247|من خلال إدراج صفوف في الورقة ، تفقد سلسلة المخططات قيمها XValues|
|CELLSNET-50295|لا يتعرف Chart.SetChartDataRange (area، false) على الخلايا المدمجة|
|CELLSNET-50308|النطاق حتى PNG: الإخراج ليس كما هو متوقع|
|CELLSNET-50240| تصبح كائنات OLE غير المحمية الموجودة على ورقة محمية محمية بعد الحفظ|
|CELLSNET-50273|كشف تنسيق الملف لملف html خاص|
|CELLSNET-50294|يتم تحويل أزرار تحكم ActiveX إلى أشكال وتلف الملف من XLS إلى XLSM ثم العودة إلى XLS|
|CELLSNET-50340|خطوط أعمدة الجدول مفقودة عند تحويل ملفات معينة إلى HTML|
|CELLSNET-50286|Cells.RemoveDuplicates يطرح "System.IndexOutOfRangeException: كان الفهرس خارج حدود المصفوفة"|
|CELLSNET-50270|سلسلة الإدخال ليس بتنسيق الصحيح. استثناء عند فتح ملف XLS|
|CELLSNET-50271|تنسيق هذا الملف غير مدعوم أو أنك لم تحدد التنسيق الصحيح. استثناء عند فتح ملف XLS|
|CELLSNET-50293|يطرح ExportXml مع مخطط XML "NullReferenceException" لملف معقد آخر|
|CELLSNET-50352|NullReferenceException أثناء تحويل ملف XLSM إلى XLS|

## **API العام والتغييرات غير المتوافقة مع الإصدارات السابقة**

فيما يلي قائمة بأي تغييرات تم إجراؤها على API العام مثل الأعضاء المضافين أو المعاد تسميتهم أو المحذوفون أو المهملون بالإضافة إلى أي تغيير غير متوافق مع الإصدارات السابقة تم إجراؤه على Aspose.Cells for .NET. إذا كانت لديك مخاوف بشأن أي تغيير مدرج ، فيرجى رفعه في منتدى الدعم Aspose.Cells.

### **تقادم Cells.AddAddInFunction ().**

الرجاء استخدام أساليب WorksheetCollection.RegisterAddInFunction () بدلاً من ذلك.

### **إضافة طريقة NameCollection.Filter () وتعداد NameScopeType.**

يحصل على الأسماء المحددة حسب النطاق.

### **يضيف MsoDrawingType.Timeline تعداد.**

يمثل نوع الكائنات الرسومية للخط الزمني.
