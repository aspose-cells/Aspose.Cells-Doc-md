---
title: Aspose.Cells for Java 20.11 ملاحظات الإصدار
type: docs
weight: 2
url: /ar/java/aspose-cells-for-java-20-11-release-notes/
---
{{% alert color="primary" %}}

 تحتوي هذه الصفحة على ملاحظات الإصدار لـ[Aspose.Cells for Java 20.11](https://downloads.aspose.com/cells/java/new-releases/aspose.cells-for-java-20.11/).

{{% /alert %}}

|**مفتاح**|**ملخص**|**فئة**|
|:- |:- |:- |
|CELLSJAVA-43322|مطلوب خاصية Shape.getWorksheet ()|ميزة جديدة|
|CELLSJAVA-43191| توفير وسائل للتعامل مع السيناريوهات عند تحديد أنواع الخطوط غير الصحيحة؟|التعزيز|
|CELLSJAVA-43319|مشكلة الحصول على قيمة الخلية مع الصيغة|خلل برمجي|
|CELLSJAVA-43330|مشكلة بعد إعادة حفظ ملف XLSB - ملف تالف|خلل برمجي|
|CELLSJAVA-43333|وضع الصور والنص بشكل خاطئ عند تقديم Excel كـ HTML|خلل برمجي|
|CELLSJAVA-43321|مشكلة التصفية التلقائية - يتم عرض صفوف فارغة|خلل برمجي|
|CELLSJAVA-43335|حدث طريق مسدود أثناء حساب الصيغ في المصنف|خلل برمجي|
|CELLSJAVA-43313|يغير ملصق الرسم البياني موضعه عند الطباعة|خلل برمجي|
|CELLSJAVA-43314|0/100٪ سطر لم تتم طباعته لـ 100٪ مخططات دائرية|خلل برمجي|
|CELLSJAVA-43316| مشاكل مختلفة عند طباعة الرسوم البيانية|خلل برمجي|
|CELLSJAVA-40582|لم يتم تقديم نص فني ذكي بشكل صحيح إلى PDF / صورة|خلل برمجي|
|CELLSJAVA-41639|لا يتم الاحتفاظ بعرض العمود عند التحويل من تنسيق "XML Spreadsheet 2003" إلى تنسيق XLSX|خلل برمجي|
|CELLSJAVA-43315|تحويل XLS إلى XLSX يجعل الملف تالفًا ويعطي خطأ "شكل إلى صورة" عند تحويل الإخراج XLSX إلى PDF|خلل برمجي|
|CELLSJAVA-43334|التصفية التلقائية في مسألة الجدول|خلل برمجي|
|


## **API العام والتغييرات غير المتوافقة مع الإصدارات السابقة**

فيما يلي قائمة بأي تغييرات تم إجراؤها على API العام مثل الأعضاء المضافين أو المعاد تسميتهم أو المحذوفون أو المهملون بالإضافة إلى أي تغيير غير متوافق مع الإصدارات السابقة تم إجراؤه على Aspose.Cells for Java. إذا كانت لديك مخاوف بشأن أي تغيير مدرج ، فيرجى رفعه في منتدى الدعم Aspose.Cells.

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

### **يضيف طريقة تجاوز XmlMapCollection.Clear ().**

مسح كافة خرائط xml.

### **يضيف SaveFormat.Docx enum.**

يمثل هذا الحفظ كملفات docx.

### **يضيف ImageType.OfficeCompatibleEmf enum.**

Windows Enhanced Metafile وهو أكثر توافقًا مع Office.

