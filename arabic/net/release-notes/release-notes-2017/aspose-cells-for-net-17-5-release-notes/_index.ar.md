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
|CELLSNET-41365|دعم PDF / A-1a الامتثال في PdfSaveOptions|ميزة جديدة|
|CELLSNET-45347|قم بإزالة PrinterSettings الموجودة في ملف Excel|ميزة جديدة|
|CELLSNET-45340|قم بتنفيذ خيارات حجم الصفحة المخصص لورقة العمل|ميزة جديدة|
|CELLSNET-45327|دعم تصدير بيانات HTML خلية إلى DataTable|ميزة جديدة|
|CELLSNET-45316|دعم عمل GridWeb عندما يكون وضع حالة الجلسة ASP.NET هو SQL Server|ميزة جديدة|
|CELLSNET-45350|حدث خطأ في OutOfMemory أثناء عرض الصورة|أداء|
|CELLSNET-45341|تحويل XLS إلى SpreadsheetML وجود مرشحات يفسد ملف الإخراج|أداء|
|CELLSNET-45217|يؤدي حفظ Excel إلى PDF إلى تدوير الصورة|خلل برمجي|
|CELLSNET-45306|أنماط خاطئة عند الحفظ بالرقم HTML ببادئة css|خلل برمجي|
|CELLSNET-45304|محاذاة النص للنص الذي تم تدويره رأسيًا خاطئة في الإخراج HTML|خلل برمجي|
|CELLSNET-45299|لا يتم احتواء النص في الخلية عند الحفظ كـ HTML|خلل برمجي|
|CELLSNET-45288|حدث استثناء عند تحميل ملف HTML|خلل برمجي|
|CELLSNET-45274|لم يتم تحديث بيانات الجدول المحوري بشكل صحيح|خلل برمجي|
|CELLSNET-45336|طريقة حساب المصنف غير قادرة على حساب صيغة XIRR - II|خلل برمجي|
|CELLSNET-45333|القيم الموجودة في الخلية M114 و N114 غير صحيحة بعد حساب صيغة المصنف|خلل برمجي|
|CELLSNET-45318|طريقة حساب المصنف غير قادرة على حساب صيغة XIRR|خلل برمجي|
|CELLSNET-45310|يواجه العديد من المستخدمين مشكلة في GridWeb عندما تكون حالة الجلسة خارج العملية|خلل برمجي|
|CELLSNET-45324|لم يتم محاذاة موضع الأحرف للوسط عند تقديم ملف Excel إلى PDF|خلل برمجي|
|CELLSNET-45339|تم تحويل ملف ODS إلى XML (SpreadsheetML) لم يتم فتحه بواسطة MS Excel|خلل برمجي|
|CELLSNET-45326|Cell.HtmlString لا يميز لون الخط المتداخل بشكل صحيح|خلل برمجي|
|CELLSNET-45325|تنتهي عمليات التحقق من صحة البيانات بغرابة بعد إدراج صفوف جديدة|خلل برمجي|
|CELLSNET-45322|تم تغيير طريقة Cells.ImportDataTable|خلل برمجي|
|CELLSNET-45314|لا تعمل الخاصية CopyOptions.ExtendToAdjacentRange|خلل برمجي|
|CELLSNET-45312|يختلف ملف Excel النهائي عن ملف Excel الأصلي|خلل برمجي|
|CELLSNET-45303|لم تعد الأشكال (المستطيلات ، الخطوط ، إلخ) مرتبطة بعد الآن عند إعادة الحفظ من تنسيق ملف XLSX إلى XLS|خلل برمجي|
|CELLSNET-45301|يؤدي فتح ملف Excel وحفظه إلى حدوث خطأ في المحاذاة|خلل برمجي|
|CELLSNET-45297|يؤدي فتح ملف XLSM وحفظه بإصدار أحدث إلى إتلافه|خلل برمجي|
|CELLSNET-45296|تؤدي إزالة جميع التعليقات من المصنف إلى حدوث أخطاء عند فتحه في Excel|خلل برمجي|
|CELLSNET-45308|ترجمة "أخرى" للمخطط الدائري|خلل برمجي|
|CELLSNET-45298|لا يتم إخفاء إدخالات وسيلة الإيضاح بشكل صحيح في المخطط المدمج|خلل برمجي|
|CELLSNET-45313|استثناء عند إضافة حقل محسوب إلى PivotTable|استثناء|
|CELLSNET-45307|خطأ في الشكل على الصورة أثناء عرض ورقة العمل على الصورة|استثناء|
### **API العام والتغييرات غير المتوافقة مع الإصدارات السابقة**
فيما يلي قائمة بأي تغييرات تم إجراؤها على API العام مثل الأعضاء المضافين أو المعاد تسميتهم أو المحذوفون أو المهملون بالإضافة إلى أي تغيير غير متوافق مع الإصدارات السابقة تم إجراؤه على Aspose.Cells for .NET. إذا كانت لديك مخاوف بشأن أي تغيير مدرج ، فيرجى رفعه في منتدى الدعم Aspose.Cells.
#### **يضيف خاصية ExportTableOptions.ExportAsHtmlString**
يقوم بتصدير قيمة سلسلة HTML للخلايا الى DataTable.
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
يمثل تنسيق PDF متوافقًا مع PDFA-1a.


#### **أمثلة على الاستخدام**
يرجى التحقق من قائمة مواضيع المساعدة المضافة في Aspose.Cells مستندات Wiki:

- [قم بتحويل ملف Excel إلى تنسيق PDF متوافق مع PDFA-1a](/cells/ar/net/convert-excel-file-to-pdf-format-compatible-with-pdfa-1a/)
- [انسخ إعدادات إعداد الصفحة من ورقة عمل المصدر إلى ورقة عمل الوجهة](/cells/ar/net/copy-page-setup-settings-from-source-worksheet-into-destination-worksheet/)
- [تنفيذ حجم الورق المخصص لورقة العمل للعرض](/cells/ar/net/implement-custom-paper-size-of-worksheet-for-rendering/)
- [قم بإزالة إعدادات PrinterSettings الموجودة من أوراق العمل في ملف Excel](/cells/ar/net/remove-existing-printersettings-of-worksheets-in-excel-file/)
- [نقل الصف الأول لأسفل عند ادخال Cells صفوف جدول البيانات](/cells/ar/net/shift-first-row-down-when-inserting-cells-data-table-rows/)
- [تصدير HTML سلسلة قيمة Cells إلى DataTable](/cells/ar/net/export-html-string-value-of-the-cells-to-the-datatable/)
- [العمل من GridWeb عندما يكون وضع حالة الجلسة ASP.NET هو SQL Server](/cells/ar/net/working-of-gridweb-when-asp-net-session-state-mode-is-sql-server/)
- [تمكين أوضاع GridWeb المختلفة](/cells/ar/net/enable-different-gridweb-modes/)


