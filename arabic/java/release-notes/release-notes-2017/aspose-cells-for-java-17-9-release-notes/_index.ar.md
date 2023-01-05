---
title: Aspose.Cells for Java 17.9 ملاحظات الإصدار
type: docs
weight: 40
url: /ar/java/aspose-cells-for-java-17-9-release-notes/
---
{{% alert color="primary" %}} 

 تحتوي هذه الصفحة على ملاحظات الإصدار لـ[Aspose.Cells for Java 17.9](https://downloads.aspose.com/cells/java/new-releases/aspose.cells-for-java-17.9/).

{{% /alert %}} 

|**مفتاح**|**ملخص**|**فئة**|
|:- |:- |:- |
|CELLSJAVA-42391|عرض Cell المعروض في PDF الناتج ليس هو نفسه الموجود في ملف Excel عند استخدام ميزة "إظهار الصيغة"|ميزة جديدة|
|CELLSJAVA-42379|تنفيذ الوجهة المسماة عند التقديم إلى إخراج PDF (استعلام إشارة مرجعية)|ميزة جديدة|
|CELLSJAVA-42401|يجب تعداد جميع الأشكال لتعيين ترتيب Z للشكل بشكل صحيح|التعزيز|
|CELLSJAVA-42368|تعيين اسم عنصر تحكم ActiveX (ListBox)|التعزيز|
|CELLSJAVA-42369|HTML إخراج مستند Excel يحتوي على قيم تجزئة بدلاً من القيم الفعلية|خلل برمجي|
|CELLSJAVA-42366|يؤدي حفظ "2.2 CompleteEmail.html" إلى تنسيق XLSX إلى إنشاء ملف تالف|خلل برمجي|
|CELLSJAVA-42365|يطرح تحميل "2.1 CompleteEmail.html" في كائن المصنف NullPointerException|خلل برمجي|
|CELLSJAVA-42381|حساب المصنف خاطئ لصيغة البحث في Excel|خلل برمجي|
|CELLSJAVA-42380|يتم حساب صيغة الصفيف في الورقة بشكل مختلف عن طريق Aspose.Cells|خلل برمجي|
|CELLSJAVA-42370|ارتباطات تشعبية غير صحيحة ومحتوى PDF|خلل برمجي|
|CELLSJAVA-42395|التقديم - صورة المخطط غير صحيحة|خلل برمجي|
|CELLSJAVA-42393|تسميات محور الفئة مفقودة عند تحويل Excel إلى PDF|خلل برمجي|
|CELLSJAVA-42384|لون الأشرطة السالبة غير صحيح عند تحويل Excel إلى PDF|خلل برمجي|
|CELLSJAVA-42378|تغير لون الشريط أثناء تحويل Excel إلى PDF عند استخدام setCrossAt ()|خلل برمجي|
|CELLSJAVA-42377|تم إرجاع قيمة الوحدات الرئيسية للمحور في المخطط بشكل خاطئ|خلل برمجي|
|CELLSJAVA-42364|لا تأتي علامات البيانات من نطاق الخلايا عند تصديرها إلى PDF|خلل برمجي|
|CELLSJAVA-42359|علامات البيانات المفقودة لسلسلة تحتوي على قيم شريطية مثل 100|خلل برمجي|
|CELLSJAVA-42314|الرسم البياني فارغ في الإخراج PNG|خلل برمجي|
|CELLSJAVA-42313|الرسم البياني فارغ في الإخراج PDF|خلل برمجي|
|CELLSJAVA-42374|تم تحليل مراجع الأحرف بشكل غير صحيح بواسطة Aspose Cells|خلل برمجي|
|CELLSJAVA-42373|يؤدي نسخ المصنف ثم الحفظ إلى إتلاف ملف Excel الناتج|خلل برمجي|
|CELLSJAVA-42392|استثناء "com.aspose.cells.CellsException: محتوى Excel غير معروف!" عند إنشاء مثيل لملف Excel مشفر|استثناء|
## **API العام والتغييرات غير المتوافقة مع الإصدارات السابقة**
فيما يلي قائمة بأي تغييرات تم إجراؤها على API العام مثل الأعضاء المضافين أو المعاد تسميتهم أو المحذوفون أو المهملون بالإضافة إلى أي تغيير غير متوافق مع الإصدارات السابقة تم إجراؤه على Aspose.Cells for Java. إذا كانت لديك مخاوف بشأن أي تغيير مدرج ، فيرجى رفعه في منتدى الدعم Aspose.Cells.
### **يضيف خاصية HTMLLoadOptions.LoadStyleStrategy**
يشير إلى استراتيجية تطبيق النمط على القيم التي تم تحليلها عند تحويل قيمة السلسلة إلى رقم أو التاريخ والوقت.
### **يضيف فئة AbstractCalculationMonitor**
يوفر واجهات برمجة التطبيقات (API) للمستخدمين لمراقبة تقدم حساب الصيغة.
### **يضيف خاصية CalculationOptions.CalculationMonitor**
يسمح للمستخدم بتوفير تنفيذ مخصص لمراقبة تقدم حساب الصيغة.
### **يضيف تعداد GridlineType**
تعداد نوع خطوط الشبكة.
### **إضافة خاصية ImageOrPrintOptions.GridlineType**
الحصول على نوع خط الشبكة أو تعيينه.
### **يضيف خاصية PdfSaveOptions.GridlineType**
الحصول على نوع خط الشبكة أو تعيينه.
### **يضيف أساليب Name.GetRanges (منطقي) و Name.GetRange (منطقي)**
بالنسبة إلى كائنات الاسم البسيط في الغالب ، مثل النطاقات المسماة ذات المراجع المطلقة ، لا يحتاج مرجع الاسم إلى أن يتم حسابه بشكل متكرر. لذلك لن يقوم GetRanges (false) / GetRange (false) بإعادة حساب كائن الاسم عند الحصول على النطاق (النطاقات) المقابل وبالتالي يمكن تحسين الأداء بشكل كبير إذا تم استدعاء هذه الطرق بشكل متكرر.
### **يضيف خاصية PdfBookmarkEntry.DestinationName**
يحصل أو يحدد اسم الوجهة. إذا تم تعيين اسم desitnation ، فسيتم تعريف desitnation كوجهة مسماة بهذا الاسم.
### **يضيف طريقة DataSorter.AddKey ()**
يضيف فهرس العمود المرتب وترتيب الفرز مع قائمة الفرز المخصصة.
### **يضيف طريقة Picture.Copy ()**
ينسخ الإعدادات من صورة أخرى.
### **يضيف طريقة Shape.ToFrontOrBack ()**
يجلب الشكل إلى الأمام أو يرسله إلى الخلف.
### **يضيف تعداد ConnectionDataSourceType.Table**
يمثل الجدول كمصدر بيانات الاتصال.
### **يضيف طريقة PageSetup.SetFitToPages ()**
يعيّن عدد الصفحات التي سيتم تغيير حجم ورقة العمل إليها عند طباعتها.
### **إضافة خاصية PdfSaveOptions.StreamProvider وتعداد ResourceLoadingType**
الحصول على نوع تحميل المورد الخارجي وتعيينه.
### **إضافة أساليب VbaModuleCollection.AddDesignerStorage () و GetDesignerStorage ()**
الحصول على تخزين المصمم لمشروع VBA وتعيينه.


### **أمثلة على الاستخدام**
يرجى التحقق من قائمة مواضيع المساعدة المضافة في Aspose.Cells مستندات Wiki:

- [قم بإضافة PDF إشارات مرجعية ذات الوجهات المحددة](/cells/ar/java/add-pdf-bookmarks-with-named-destinations/)
- [التحكم في تحميل الموارد الخارجية في مصنف MS Excel أثناء التقديم إلى PDF](/cells/ar/java/control-loading-of-external-resources-in-ms-excel-workbook-while-rendering-to-pdf/)
- [نسخ VBA ماكرو UserForm DesignerStorage من قالب إلى المصنف الهدف](/cells/ar/java/copy-vba-macro-userform-designerstorage-from-template-to-target-workbook/)
- [إنشاء إزالة والحصول على تعليقات GridCell](/cells/ar/java/create-remove-and-get-gridcell-comments/)
- [أرسل Shape Front أو Back داخل ورقة العمل](/cells/ar/java/send-shape-front-or-back-inside-the-worksheet/)
- [فرز البيانات في العمود باستخدام قائمة الفرز المخصصة](/cells/ar/java/sort-data-in-column-with-custom-sort-list/)
