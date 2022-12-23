---
title: Aspose.Cells for .NET 20.11 ملاحظات الإصدار
type: docs
weight: 2
url: /ar/net/aspose-cells-for-net-20-11-release-notes/
---
{{% alert color="primary" %}}

 تحتوي هذه الصفحة على ملاحظات الإصدار لـ[Aspose.Cells for .NET 20.11](https://www.nuget.org/packages/Aspose.Cells/20.11.0).

{{% /alert %}}

|**مفتاح**|**ملخص**|**فئة**|
|:- |:- |:- |
|CELLSNET-47706|دعم نمط التنسيق المعتمد على الإعدادات المحلية "aaaa" للعام في منطقة إسبانيا|التحسينات|
|CELLSNET-47641|تم رفع تحذير أثناء إضافة 29 ورقة وفتح ملف الإخراج XLS في MS Excel|أداء|
|CELLSNET-46716|تم قص النص عند تقديم PDF|البق|
|CELLSNET-47618|تصبح الصورة كلها بيضاء وبعض النص يتلف في الصور / الأشكال الأخرى|البق|
|CELLSNET-47635| القطاعة على طاولة مختلفة تولد ملف تالف|البق|
|CELLSNET-47642|XLSB الملف تالف بعد التحميل والحفظ|البق|
|CELLSNET-47660|حقل الرسم البياني الذي يحتوي على التواريخ له تنسيق مختلف بتنسيق PDF|البق|
|CELLSNET-47661|يقوم Aspose.Cells بإنشاء علامة HTML غير صالحة لورقة عمل معينة خاصة بمستند Cells|البق|
|CELLSNET-47680|لم يتم تحديث الجداول المحورية|البق|
|CELLSNET-47659|مشكلة البحث عن الخلايا ذات الأنماط المحددة|البق|
|CELLSNET-47679|الفرق في حساب Aspose.Cells و Excel|البق|
|CELLSNET-47666|لا يمكن عرض المصنف في SharePoint|البق|
|CELLSNET-47698|التحول في موضع الشعار أثناء تحويل ملف XLS إلى PDF|البق|
|CELLSNET-47651|تصدير المخطط القطبي إلى pdf منحرف|البق|
|CELLSNET-47662|تظهر تسميات البيانات الخاطئة عند تحويل مخطط Excel إلى صورة|البق|
|CELLSNET-47667|أشرطة مفقودة في المخطط الشريطي في صورة الإخراج|البق|
|CELLSNET-47697|تخرج بعض قيم المحور ص خارج المخطط في الناتج PDF|البق|
|CELLSNET-43579|يتم تغيير انحناء نص WortArt أثناء التحويل من Excel إلى PDF|البق|
|CELLSNET-47675|تم تغيير محتوى الملف XLS بعد التحميل والحفظ|البق|
|CELLSNET-47704|اختفت الخصائص المخصصة بعد تحرير / حفظ ملف XLS محمي بكلمة مرور (مشفر)|البق|
|CELLSNET-47708|لم يكن ترتيب الفرز يعمل بشكل صحيح مع الصيغ الديناميكية (العلامات الذكية)|البق|
|CELLSNET-47682|استثناء عند تحميل هتم معين|استثناءات|
|CELLSNET-47683|استثناء عند تحميل هتم معين|استثناءات|
|CELLSNET-47684|استثناء عند تحميل هتم معين|استثناءات|
|CELLSNET-47689|استثناء عند التحويل XLSB إلى PNG و HTML|استثناءات|
|CELLSNET-47701|فشل إنشاء نسخة من المصنف XLTX|استثناءات|
|CELLSNET-47628|يؤدي حذف الصفوف الفارغة من الخلايا إلى ArgumentOutOfRangeException|استثناءات|
|CELLSNET-47629|يؤدي استدعاء قيم الخلية بعد حذف الصفوف والأعمدة الفارغة إلى ظهور ArgumentException|استثناءات|
|CELLSNET-47700|يطرح CalculateFormula InvalidCastException|استثناءات|
|CELLSNET-47703|تم رفع الاستثناء أثناء استدعاء Workbook.CalculateFormula ()|استثناءات|
|CELLSNET-47669|تم طرح ArgumentException فهرس العمود غير صالح أثناء تحويل ورقة العمل الأولى إلى HTML|استثناءات|
|CELLSNET-47677|يقوم DataBar.ToImage بإصدار استثناء إذا كان الصف مخفيًا.|استثناءات|
|CELLSNET-47686|لا يمكن تحويل XLSB إلى XLSX|استثناءات|
|CELLSNET-47687|لا يمكن تحميل Ods|استثناءات|
|CELLSNET-47694|استثناء عند فتح ملف الوثيقة XLSX|استثناءات|
|CELLSNET-47695|اسم خلية غير صالح بعد DeleteRange|استثناءات|
|CELLSNET-47699|استثناء عند فتح ملف ODS|استثناءات|
|CELLSNET-47702| حدث الاستثناء عند تحميل ملفات "Microsoft Excel 5.0 / 95 Workbook" المشفرة|استثناءات|


## **API العام والتغييرات غير المتوافقة مع الإصدارات السابقة**

فيما يلي قائمة بأي تغييرات تم إجراؤها على API العام مثل الأعضاء المضافين أو المعاد تسميتهم أو المحذوفون أو المهملون بالإضافة إلى أي تغيير غير متوافق مع الإصدارات السابقة تم إجراؤه على Aspose.Cells for .NET. إذا كانت لديك مخاوف بشأن أي تغيير مدرج ، فيرجى رفعه في منتدى الدعم Aspose.Cells.

### **يحذف طريقة CellsHelper.IsProtectedByRMS () المتقادمة**

استخدم FileFormatUtil.DetectFileFormat (). الخاصية IsProtectedByRMS بدلاً من ذلك.

### **حذف طريقة CellsHelper.DetectLoadFormat () و CellsHelper.DetectFileFormat () المتقادمة**

استخدم FileFormatUtil.DetectFileFormat () بدلاً من ذلك.

### **يحذف خاصية CellsHelper.FontDir القديمة.**

استخدم FontConfigs.SetFontsFolder (سلسلة ، منطقية) بدلاً من ذلك.

### **يحذف خاصية CellsHelper.FontDirs المتقادمة.**

استخدم FontConfigs.SetFontFolders (سلسلة [] ، منطقي) بدلاً من ذلك.

### **حذف خاصية CellsHelper.FontFiles القديمة.**

استخدم FontConfigs.SetFontSources (FontSourceBase []) بدلاً من ذلك.

### **يضيف خاصية CellsHelper.IsCloudPlatform.**

يشير إلى ما إذا كان يعمل على منصة يمكن.

### **يضيف خاصية Shape.Worksheet.**

يحصل على ورقة العمل التي تحتوي على هذا الشكل.

### **يضيف خاصية SaveOptions.SortExternalNames.**

الإشارة إلى ما إذا كان يتم فرز الأسماء الخارجية عند حفظ ملفات .xlsx.

### **يضيف طريقة ListObject.Filter ().**

يصفي الجدول.

### **يضيف طريقة XmlMapCollection.Clear ().**

مسح كافة خرائط xml.

### **يضيف SaveFormat.Docx enum.**

يمثل هذا الحفظ كملفات docx.

### **يضيف ImageType.OfficeCompatibleEmf enum.**

Windows Enhanced Metafile وهو أكثر توافقًا مع Office.

