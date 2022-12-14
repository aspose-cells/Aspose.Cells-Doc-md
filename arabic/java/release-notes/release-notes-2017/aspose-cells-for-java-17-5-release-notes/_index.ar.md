---
title: Aspose.Cells for Java 17.5 ملاحظات الإصدار
type: docs
weight: 80
url: /ar/java/aspose-cells-for-java-17-5-release-notes/
---
{{% alert color="primary" %}} 

 تحتوي هذه الصفحة على ملاحظات الإصدار لـ[Aspose.Cells for Java 17.5](https://downloads.aspose.com/cells/java/new-releases/aspose.cells-for-java-17.5/).

{{% /alert %}} 

|**مفتاح**|**ملخص**|**فئة**|
|:- |:- |:- |
|CELLSJAVA-41130|قم بتغيير لغة الكلمات المحددة مسبقًا لـ Pivot Table|التعزيز|
|CELLSJAVA-42272|خيارات لتضمين الارتباط التشعبي في خلية Excel|التعزيز|
|CELLSJAVA-42283|يحدث NullPointerException عند وجود عامل التصفية خارج النطاق المحدد|حشرة|
|CELLSJAVA-42282|يؤدي نسخ ورقة عمل إلى إظهار الصفوف التي تمت تصفيتها في ملف HTML الناتج|حشرة|
|CELLSJAVA-42276|تظهر المحتويات بشكل مختلف (بعض النصوص مفقودة) في متصفحات بخلاف IE (مثل Google chrome) - عرض Excel إلى HTML|حشرة|
|CELLSJAVA-42247|يُفقد التنسيق الشرطي عند تحديث PivotTable في جدول البيانات|حشرة|
|CELLSJAVA-42257|نمط التنسيق الشرطي معطل|حشرة|
|CELLSJAVA-42202|صيغة Excel لا تعمل بشكل صحيح - تظهر على شكل 6 بدلاً من 0|حشرة|
|CELLSJAVA-42286|يستخدم حفظ ملف XLS مع الرسوم البيانية 100٪ وحدة المعالجة المركزية|حشرة|
|CELLSJAVA-42251|يتم إخفاء العنوان بواسطة تسميات الاتجاه في ملف PDF الناتج|حشرة|
|CELLSJAVA-42284|يعرض Workbook.getFonts () خطوطًا إضافية بعد إعادة تحميل نفس جدول البيانات|حشرة|
|CELLSJAVA-42281|الدمج / النسخ إلى أوراق Excel - لا يتم الاحتفاظ بالمسافات الموجودة في بداية الخلايا|حشرة|
|CELLSJAVA-42280|سلسلة غير صالحة في الملف - حدث خطأ عند فتح ملف Excel|حشرة|
|CELLSJAVA-42275|تم تغيير أسماء بعض معلمات الطرق العامة في الإصدار الأحدث|حشرة|
|CELLSJAVA-42271|Worksheet.autoFitColumns () لا يعمل بشكل جيد مع الخلايا التي تحتوي على فواصل أسطر|حشرة|
|CELLSJAVA-42266|يؤدي فرز ملف Excel الذي يحتوي على تعليقات إلى إتلاف ملف Excel الناتج|حشرة|
|CELLSJAVA-42265|يؤدي فرز التعليقات إلى ظهور خطأ "عثر Excel على محتوى غير قابل للقراءة ...." عند فتح ملف الإخراج في MS Excel|حشرة|
|CELLSJAVA-42264|مشكلات الأحرف المنخفضة والمرتفعة في ملف OpenOffice ODS عند التحويل إلى HTML أو PDF|حشرة|
|CELLSJAVA-42268|استثناء: "java.lang.NullPointerException" عند تقديم مخطط للصورة|استثناء|
|CELLSJAVA-42278|استثناء: "java.lang.IndexOutOfBoundsException: الفهرس: 12 ، الحجم: 12" عند الحفظ بتنسيق ملف HTML|استثناء|
|CELLSJAVA-42274|استثناء: "java.lang.StringIndexOutOfBoundsException: فهرس السلسلة خارج النطاق: 0" عند تحميل ملف XLSX|استثناء|
## **API العام والتغييرات غير المتوافقة مع الإصدارات السابقة**
فيما يلي قائمة بأي تغييرات تم إجراؤها على API العام مثل الأعضاء المضافين أو المعاد تسميتهم أو المحذوفون أو المهملون بالإضافة إلى أي تغيير غير متوافق مع الإصدارات السابقة تم إجراؤه على Aspose.Cells for Java. إذا كانت لديك مخاوف بشأن أي تغيير مدرج ، فيرجى رفعه في منتدى الدعم Aspose.Cells.
### **يضيف خاصية ExportTableOptions.ExportAsHtmlString**
يصدر قيمة سلسلة HTML للخلايا إلى DataTable.
### **يضيف طريقة PageSetup.Copy (مصدر PageSetup و CopyOptions copyOptions)**
ينسخ إعدادات إعداد الصفحة.
### **إضافة خاصية ImportTableOptions.ShiftFirstRowDown**
يشير إلى ما إذا كان سيتم نقل الصف الأول لأسفل عند إدراج الجدول.
### **يضيف طريقة PageSetup.CustomPaperSize ()**
يضبط حجم الورق المخصص بوحدة البوصة.
### **يضيف خاصية PageSetup.PrinterSettings**
الحصول على إعدادات الطابعة الافتراضية وتعيينها.
### **يضيف ثوابت PaperSizeType.CUSTOM**
يمثل حجم الورق المخصص.
### **يضيف ثوابت PdfCompliance.PDF_A_1_A**
يمثل تنسيق PDF متوافق مع PDFA-1a.


### **أمثلة على الاستخدام**
يرجى التحقق من قائمة مواضيع المساعدة المضافة في Aspose.Cells مستندات Wiki:

- [قم بتحويل ملف Excel إلى تنسيق PDF متوافق مع PDFA-1a](/cells/ar/java/convert-excel-file-to-pdf-format-compatible-with-pdfa-1a/)
- [انسخ إعدادات إعداد الصفحة من ورقة عمل المصدر إلى ورقة عمل الوجهة](/cells/ar/java/copy-page-setup-settings-from-source-worksheet-into-destination-worksheet/)
- [تنفيذ حجم الورق المخصص لورقة العمل للعرض](/cells/ar/java/implement-custom-paper-size-of-worksheet-for-rendering/)
- [قم بإزالة إعدادات PrinterSettings الموجودة من أوراق العمل في ملف Excel](/cells/ar/java/remove-existing-printersettings-of-worksheets-in-excel-file/)
- [نقل الصف الأول لأسفل عند ادخال Cells صفوف جدول البيانات](/cells/ar/java/shift-first-row-down-when-inserting-cells-data-table-rows/)
