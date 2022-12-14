---
title: Aspose.Cells for Java 17.11 ملاحظات الإصدار
type: docs
weight: 20
url: /ar/java/aspose-cells-for-java-17-11-release-notes/
---
{{% alert color="primary" %}} 

تحتوي هذه الصفحة على ملاحظات إصدار for Java Aspose.Cells 17.11.

{{% /alert %}} 

|**مفتاح**|**ملخص**|**فئة**|
|:- |:- |:- |
|CELLSJAVA-42433|ImageOrPrintOptions.PageIndex و ImageOrPrintOptions.Count الخصائص المطلوبة للحصول على صورة الصفحات المطلوبة|ميزة جديدة|
|CELLSJAVA-42427|لا يعرض تصدير خطوط الشبكة ذات الحدود خطوط الشبكة داخل الحدود في عرض Excel إلى HTML|حشرة|
|CELLSJAVA-42438|يقوم LightCellsDataProvider بإزالة المسافات البادئة والزائدة|حشرة|
|CELLSJAVA-42422|يتم استخدام خط غير صحيح في إخراج PDF لمخطط MS Excel|حشرة|
|CELLSJAVA-42353|بعض الأسهم أو وسائل الشرح مفقودة في إخراج HTML|حشرة|
|CELLSJAVA-42455|التعليق الثاني مفقود من مجموعة تعليقات ورقة العمل|حشرة|
|CELLSJAVA-42454|يبدو أن إنشاء المصنف يتعطل عند القراءة من ملف XLSM|حشرة|
|CELLSJAVA-42450|لا تعمل الخاصية Style.QuotePrefix لملف XLSB|حشرة|
|CELLSJAVA-42445|يؤثر تعيين بيانات الصورة على الرسم البياني الآخر ويتم عرضها بشكل خاطئ|حشرة|
|CELLSJAVA-42444|تعمل طريقة CheckBox.setName () في MS Excel 2016 ولكنها لا تعمل في MS Excel 2007|حشرة|
|CELLSJAVA-42443|لم يتم تحويل مرشحات MS Excel بشكل صحيح - تحويل XLSB إلى XLSM|حشرة|
|CELLSJAVA-42442|لا يؤدي تغيير قيمة ComboBoxActiveXControl إلى تغيير قيمة الخلية المرتبطة|حشرة|
|CELLSJAVA-42435|Cells.setColumnWidthPixel و Cells.setRowHeightPixel لهما سلوكيات مختلفة|حشرة|
|CELLSJAVA-42431|يؤدي توسيع نطاق الجدول إلى تغيير محتويات الخلية بشكل غير متوقع|حشرة|
|CELLSJAVA-42434|استثناء: "java.lang.NumberFormatException" عند تحميل تنسيق ملف HTML|استثناء|
|CELLSJAVA-42448|تسبب Cells.deleteBlankRows في استثناء "java.lang.ArrayIndexOutOfBoundsException: 1937"|استثناء|
|CELLSJAVA-42426|استثناء في سلسلة الرسائل "main" java.lang.OutOfMemoryError: تجاوز حد GC العلوية - الملف الثالث|استثناء|
|CELLSJAVA-42425|استثناء في سلسلة الرسائل "main" java.lang.OutOfMemoryError: تجاوز حد GC العلوية - الملف II|استثناء|
|CELLSJAVA-42424|استثناء في سلسلة الرسائل "main" java.lang.OutOfMemoryError: تجاوز حد GC العلوية - الملف الأول|استثناء|
|CELLSJAVA-42428|ينتج Chart.toImage java.lang.ArrayIndexOutOfBoundsException|استثناء|
|CELLSJAVA-42452|حفظ مصنف كملف PDF بعد RemoveUnusedStyles API ينتج عنه CellsException|استثناء|
|CELLSJAVA-42440|حدث "java.lang.IllegalArgumentException: فهرس صف غير صالح"|استثناء|
|CELLSJAVA-42439|استثناء: "java.lang.IllegalArgumentException: فهرس صف غير صالح" عند حفظ تنسيق ملف XLSX|استثناء|
|CELLSJAVA-42437|الاستثناء: java.lang.NumberFormatException عند إعادة حفظ تنسيق ملف XLSB|استثناء|
## **API العام والتغييرات غير المتوافقة مع الإصدارات السابقة**
فيما يلي قائمة بأي تغييرات تم إجراؤها على API العام مثل الأعضاء المضافين أو المعاد تسميتهم أو المحذوفون أو المهملون بالإضافة إلى أي تغيير غير متوافق مع الإصدارات السابقة تم إجراؤه على Aspose.Cells for Java. إذا كانت لديك مخاوف بشأن أي تغيير مدرج ، فيرجى رفعه في منتدى الدعم Aspose.Cells.
### **يضيف طريقة Shape.GetResultOfSmartArt ()**
تحويل الفن الذكي إلى شكل مجموعة.
### **يضيف خاصية Shape.IsSmartArt**
يشير إلى ما إذا كان الشكل فنًا ذكيًا.
### **يضيف أساليب Workbook.ProtectSharedWorkbook () و Workbook.UnprotectSharedWorkbook ()**
يحمي المصنف المشترك ويزيل حمايته.
### **يضيف تعداد StyleModifyFlag.Spacing**
يحدد التباعد بين الأحرف في تشغيل النص.
### **يضيف خاصية PdfSaveOptions.IgnoreError**
يشير إلى ما إذا كنت بحاجة إلى إخفاء الخطأ أثناء العرض.
### **إضافة خاصية ImageOrPrintOptions.PageIndex**
الحصول على أو تحديد الفهرس الذي يستند إلى 0 للصفحة الأولى لحفظها.
### **إضافة خاصية ImageOrPrintOptions.PageCount**
الحصول على أو تحديد عدد الصفحات المراد حفظها.
### **إضافة خاصية XmlMap.RootElementName**
يحصل على اسم عنصر الجذر.
### **يضيف طريقة Worksheet.XmlMapQuery (مسار السلسلة ، XmlMap xmlMap)**
مناطق خلايا الاستعلام التي تم تعيينها / ربطها بالمسار المحدد لخريطة xml.
### **يضيف خاصية LoadOptions.AutoFitterOptions**
الحصول على خيارات التركيب التلقائي وتعيينها.


### **أمثلة على الاستخدام**
يرجى التحقق من قائمة مواضيع المساعدة المضافة في Aspose.Cells مستندات Wiki:

- [تحويل الفن الذكي إلى شكل المجموعة](/cells/ar/java/convert-the-smart-art-to-group-shape/)
- [قم بإنشاء مصنف مشترك باستخدام Aspose.Cells](/cells/ar/java/create-shared-workbook-with-aspose-cells/)
- [حدد ما إذا كان الشكل هو شكل فني ذكي](/cells/ar/java/determine-if-shape-is-smart-art-shape/)
- [ابحث عن اسم العنصر الجذر لخريطة Xml](/cells/ar/java/find-the-root-element-name-of-xml-map/)
- [تجاهل الأخطاء أثناء عرض Excel إلى Pdf](/cells/ar/java/ignore-errors-while-rendering-excel-to-pdf/)
- [حماية كلمة المرور أو إلغاء حماية المصنف المشترك](/cells/ar/java/password-protect-or-unprotect-the-shared-workbook/)
- [الاستعلام Cell المناطق المعينة لمسار خريطة Xml باستخدام أسلوب Worksheet.XmlMapQuery](/cells/ar/java/query-cell-areas-mapped-to-xml-map-path-using-worksheet-xmlmapquery-method/)
- [عرض تسلسل الصفحات باستخدام خصائص PageIndex و PageCount الخاصة بخيارات ImageOrPrintOptions](/cells/ar/java/render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions/)
