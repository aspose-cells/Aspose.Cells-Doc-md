---
title: Aspose.Cells for .NET 17.5 ملاحظات الإصدار
type: docs
weight: 80
url: /ar/net/aspose-cells-for-net-17-5-release-notes/
---
{{% alert color="primary" %}} 

 تحتوي هذه الصفحة على ملاحظات الإصدار لـ[Aspose.Cells for .NET 17.5](https://downloads.aspose.com/cells/net/new-releases/aspose.cells-for-.net-17.5/).

{{% /alert %}} 

|**مفتاح**|**ملخص**|**فئة**|
|:- |:- |:- |
|CELLSNET-41365|دعم التوافق مع PDF / A-1a في PdfSaveOptions|ميزة جديدة|
|CELLSNET-45347|قم بإزالة PrinterSettings الموجودة في ملف Excel|ميزة جديدة|
|CELLSNET-45340|قم بتنفيذ خيارات حجم الصفحة المخصص لورقة العمل|ميزة جديدة|
|CELLSNET-45327|دعم تصدير بيانات خلايا HTML إلى DataTable|ميزة جديدة|
|CELLSNET-45316|دعم عمل GridWeb عندما يكون وضع حالة الجلسة ASP.NET هو SQL Server|ميزة جديدة|
|CELLSNET-45350|حدث خطأ في OutOfMemory أثناء عرض الصورة|أداء|
|CELLSNET-45341|تحويل XLS إلى SpreadsheetML مع وجود عوامل تصفية يفسد ملف الإخراج|أداء|
|CELLSNET-45217|يؤدي حفظ Excel إلى PDF إلى تدوير الصورة|حشرة|
|CELLSNET-45306|أنماط خاطئة عند الحفظ في HTML ببادئة css|حشرة|
|CELLSNET-45304|محاذاة النص للنص الذي تم تدويره رأسيًا خاطئة في إخراج HTML|حشرة|
|CELLSNET-45299|لا يتناسب النص مع الخلية عند الحفظ بتنسيق HTML|حشرة|
|CELLSNET-45288|حدث استثناء عند تحميل ملف HTML|حشرة|
|CELLSNET-45274|لم يتم تحديث بيانات الجدول المحوري بشكل صحيح|حشرة|
|CELLSNET-45336|طريقة حساب المصنف غير قادرة على حساب صيغة XIRR - II|حشرة|
|CELLSNET-45333|القيم الموجودة في الخلية M114 و N114 غير صحيحة بعد حساب صيغة المصنف|حشرة|
|CELLSNET-45318|طريقة حساب المصنف غير قادرة على حساب صيغة XIRR|حشرة|
|CELLSNET-45310|يواجه العديد من المستخدمين مشكلة في GridWeb عندما تكون حالة الجلسة خارج العملية|حشرة|
|CELLSNET-45324|لا يتم محاذاة موضع الأحرف للوسط عند تحويل ملف Excel إلى PDF|حشرة|
|CELLSNET-45339|لا يتم فتح ملف تم تحويله من ODS إلى XML (SpreadsheetML) بواسطة MS Excel|حشرة|
|CELLSNET-45326|Cell.HtmlString لا يميز لون الخط المتداخل بشكل صحيح|حشرة|
|CELLSNET-45325|تنتهي عمليات التحقق من صحة البيانات بغرابة بعد إدراج صفوف جديدة|حشرة|
|CELLSNET-45322|تم تغيير طريقة Cells.ImportDataTable|حشرة|
|CELLSNET-45314|لا تعمل الخاصية CopyOptions.ExtendToAdjacentRange|حشرة|
|CELLSNET-45312|يختلف ملف Excel النهائي عن ملف Excel الأصلي|حشرة|
|CELLSNET-45303|لم تعد الأشكال (المستطيلات والخطوط وما إلى ذلك) مرتبطة بعد الآن عند إعادة الحفظ من تنسيق ملف XLSX إلى XLS|حشرة|
|CELLSNET-45301|يؤدي فتح ملف Excel وحفظه إلى حدوث خطأ في المحاذاة|حشرة|
|CELLSNET-45297|فتح ملف XLSM وحفظه بإصدار أحدث يفسده|حشرة|
|CELLSNET-45296|تؤدي إزالة جميع التعليقات من المصنف إلى حدوث أخطاء عند فتحه في Excel|حشرة|
|CELLSNET-45308|ترجمة "أخرى" للمخطط الدائري|حشرة|
|CELLSNET-45298|لا يتم إخفاء إدخالات وسيلة الإيضاح بشكل صحيح في المخطط المدمج|حشرة|
|CELLSNET-45313|استثناء عند إضافة حقل محسوب إلى PivotTable|استثناء|
|CELLSNET-45307|خطأ في الشكل على الصورة أثناء عرض ورقة العمل على الصورة|استثناء|
### **API العام والتغييرات غير المتوافقة مع الإصدارات السابقة**
فيما يلي قائمة بأي تغييرات تم إجراؤها على API العام مثل الأعضاء المضافين أو المعاد تسميتهم أو المحذوفون أو المهملون بالإضافة إلى أي تغيير غير متوافق مع الإصدارات السابقة تم إجراؤه على Aspose.Cells for .NET. إذا كانت لديك مخاوف بشأن أي تغيير مدرج ، فيرجى رفعه في منتدى الدعم Aspose.Cells.
#### **يضيف خاصية ExportTableOptions.ExportAsHtmlString**
يصدر قيمة سلسلة HTML للخلايا إلى DataTable.
#### **يضيف طريقة PageSetup.Copy (مصدر PageSetup و CopyOptions copyOptions)**
ينسخ إعدادات إعداد الصفحة.
#### **إضافة خاصية ImportTableOptions.ShiftFirstRowDown**
يشير إلى ما إذا كان سيتم نقل الصف الأول لأسفل عند إدراج الجدول.
#### **يضيف طريقة PageSetup.CustomPaperSize ()**
يضبط حجم الورق المخصص بوحدة البوصة.
#### **يضيف خاصية PageSetup.PrinterSettings**
الحصول على إعدادات الطابعة الافتراضية وتعيينها.
#### **يضيف تعداد PaperSizeType.Custom**
يمثل حجم الورق المخصص.
#### **يضيف تعداد PdfCompliance.PdfA1a**
يمثل تنسيق PDF متوافق مع PDFA-1a.


#### **أمثلة على الاستخدام**
يرجى التحقق من قائمة مواضيع المساعدة المضافة في Aspose.Cells مستندات Wiki:

- [قم بتحويل ملف Excel إلى تنسيق PDF متوافق مع PDFA-1a](/cells/ar/net/convert-excel-file-to-pdf-format-compatible-with-pdfa-1a/)
- [انسخ إعدادات إعداد الصفحة من ورقة عمل المصدر إلى ورقة عمل الوجهة](/cells/ar/net/copy-page-setup-settings-from-source-worksheet-into-destination-worksheet/)
- [تنفيذ حجم الورق المخصص لورقة العمل للعرض](/cells/ar/net/implement-custom-paper-size-of-worksheet-for-rendering/)
- [قم بإزالة إعدادات PrinterSettings الموجودة من أوراق العمل في ملف Excel](/cells/ar/net/remove-existing-printersettings-of-worksheets-in-excel-file/)
- [نقل الصف الأول لأسفل عند ادخال Cells صفوف جدول البيانات](/cells/ar/net/shift-first-row-down-when-inserting-cells-data-table-rows/)
- [تصدير قيمة سلسلة HTML من Cells إلى DataTable](/cells/ar/net/export-html-string-value-of-the-cells-to-the-datatable/)
- [العمل من GridWeb عندما يكون وضع حالة الجلسة ASP.NET هو SQL Server](/cells/ar/net/working-of-gridweb-when-asp-net-session-state-mode-is-sql-server/)
- [تمكين أوضاع GridWeb المختلفة](/cells/ar/net/enable-different-gridweb-modes/)


