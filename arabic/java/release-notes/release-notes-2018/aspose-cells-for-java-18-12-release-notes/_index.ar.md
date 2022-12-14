---
title: Aspose.Cells for Java 18.12 ملاحظات الإصدار
type: docs
weight: 10
url: /ar/java/aspose-cells-for-java-18-12-release-notes/
---
{{% alert color="primary" %}} 

تحتوي هذه الصفحة على ملاحظات إصدار Aspose.Cells for Java 18.12.

{{% /alert %}} 

|**مفتاح**|**ملخص**|**فئة**|
|:- |:- |:- |
|CELLSJAVA-42745|لا تحصل على نقاط اتصال لأن نوعها الذي تم إرجاعه هو "zo []"|ميزة جديدة|
|CELLSJAVA-42662|توفير القدرة على تصدير النطاق بتنسيق HTML|ميزة جديدة|
|CELLSJAVA-42746|أشرطة البيانات مفقودة عند تحويل XLSX إلى HTML|ميزة جديدة|
|CELLSJAVA-42747|تظل القيمة موجودة عند تحويل XLSX إلى تنسيق ملف HTML|ميزة جديدة|
|CELLSJAVA-42748|فشل LightCells API في تحميل ملف ضخم|التعزيز|
|CELLSJAVA-42727|تنسيق النص مفقود في إخراج HTML لنطاق MS Excel|حشرة|
|CELLSJAVA-42744|تصبح مجموعات الرموز غير محاذاة عند تحويل XLSX إلى HTML|حشرة|
|CELLSJAVA-42772|لا يتم تقديم تصدير بيانات النطاق المسمى بشكل صحيح إلى HTML (Java)|حشرة|
|CELLSJAVA-42753|تم العثور على مشكلة في النطاق المحدد|حشرة|
|CELLSJAVA-42764|يُرجع التحقق دائمًا صحيحًا لطريقة "getInCellDropDown ()"|حشرة|
|CELLSJAVA-42768|يتم إرجاع التنسيق المخصص للثقافة الخطأ لمواقع مختلفة (ألمانيا ، الفرنسية ، إيطاليا وإسبانيا)|حشرة|
|CELLSJAVA-42758|تحويل Excel إلى PDF - مشكلة عرض مخطط القياس|حشرة|
|CELLSJAVA-42761|يطرح تحويل PDF استثناء OutOfMemoryError|حشرة|
|CELLSJAVA-42759|CellsException أثناء تحويل الملفات|استثناء|
|CELLSJAVA-42755|استثناء "NullPointerException" عند إنشاء مثيل لملف (ملفات) XLSX|استثناء|
|CELLSJAVA-42762|NumberFormatException أثناء معالجة الملفات|استثناء|
|CELLSJAVA-42774|NullPointerException عند تحميل ملف CSV|استثناء|
|CELLSJAVA-42765|استثناء "com.aspose.cells.CellsException" عند تحويل ملف Excel إلى تنسيق ملف PDF|استثناء|
|CELLSJAVA-42754|"IllegalStateException: ترميز غير صالح: فارغ" عند إنشاء تنسيق ملف XLS|استثناء|
## **API العام والتغييرات غير المتوافقة مع الإصدارات السابقة**
فيما يلي قائمة بأي تغييرات تم إجراؤها على API العام مثل الأعضاء المضافين أو المعاد تسميتهم أو المحذوفون أو المهملون بالإضافة إلى أي تغيير غير متوافق مع الإصدارات السابقة تم إجراؤه على Aspose.Cells for Java. إذا كانت لديك مخاوف بشأن أي تغيير مدرج ، فيرجى رفعه في منتدى الدعم Aspose.Cells.
### **يضيف خاصية HtmlSaveOptions.ExportSingleTab**
يشير إلى ما إذا كان تصدير علامة التبويب المفردة عندما يحتوي الملف على ورقة عمل واحدة فقط. القيمة الافتراضية هي false.
### **يضيف خاصية HtmlSaveOptions.ExportPrintAreaOnly**
يشير إلى ما إذا كان يتم تصدير منطقة الطباعة فقط إلى ملف html. القيمة الافتراضية هي كاذبة.
### **يحذف طريقة Workbook.Initialize () التي عفا عليها الزمن**
استخدم مُنشئ المصنف بدلاً من ذلك.
### **حذف خاصية Workbook.Styles التي عفا عليها الزمن**
استخدم Workbook.CreateStyle () لإنشاء نمط المصنف ومعالجته بدلاً من StyleCollection.Add () ؛ استخدم Workbook.GetNamedStyle (سلسلة) للحصول على نمط مسمى بدلاً من StyleCollection.
### **يحذف Workbook.CheckWriteProtectedPassword () طريقة قديمة**
استخدم طريقة WorkbookSettings.WriteProtection.ValidatePassword بدلاً من ذلك.
### **يضيف LoadDataFilterOptions.VBA enum**
الخيار المستخدم لتجاهل مشاريع VBA أثناء تحميل ملف القالب.
### **يضيف خاصية Style.InvariantCustom**
الحصول على سلسلة نمط الثقافة المستقلة لتنسيق الأرقام (بما في ذلك سلسلة النمط للرقم المضمن).
### **يضيف خاصية FindOptions.ValueTypeSensitive**
يشير إلى ما إذا كان يجب أن يكون نوع قيمة الخلية التي تم البحث عنها هو نفسه مع المفتاح الذي تم البحث عنه.
### **تقادم FindOptions.SearchNext خاصية**
استخدم خاصية FindOptions.SearchBackward بدلاً من ذلك ، القيمة الحقيقية لهذه الخاصية الجديدة تقابل خطأ SearchNext.
### **حذف طرق البحث Cells.FindString و FindStringStartsWith و FindStringEndsWith و FindStringContains و FindNumber القديمة**
استخدم Cells. أوجد طريقة (كائن ، Cell ، FindOptions) بدلاً من ذلك. للحصول على نفس النتائج باستخدام الطرق FindNumber و FindString ، يرجى تعيين FindOptions.ValueTypeSensitive على أنه صحيح.
### **يحذف الطريقة القديمة Cells.ImportGridView (System.Web.UI.WebControls.GridView، int، int، bool، bool، bool)**
استخدم طريقة Cells.ImportGridView (System.Web.UI.WebControls.GridView GridView ، int firstRow ، int firstColumn ، ImportTableOptions options). في حين أن.
### **يحذف Cells المتقادم. خاصية البدء**
استخدم Cells.FirstCell بدلاً من ذلك.
### **يحذف خاصية النهاية Cells.End المتقادمة**
استخدم Cells.LastCell بدلاً من ذلك.
### **يحذف Cells خاصية [int]**
استخدم طريقة Cells.GetEnumerator () لتكرار كل الخلايا في ورقة العمل هذه بدلاً من ذلك.
### **يحذف طرق Cells**
استخدم طريقة Cells.ImportData (DataTable ، int ، int ، ImportTableOptions) بدلاً من ذلك.
### **يحذف طرق Cells**
استخدم طريقة Cells.ImportData (IDataReader، int، int، ImportTableOptions) بدلاً من ذلك.
### **يحذف خاصية دوران الشكل التي عفا عليها الزمن**
استخدم خاصية Shape.RotationAngle بدلاً من ذلك.
### **يحذف خاصية Validation.AreaList القديمة**
استخدم Validation.Areas property بدلاً من ذلك.
### **حذف مُنشئ النمط المتقادم**
استخدم طريقة CellsFactory.CreateStyle () أو Workbook.CreateStyle () بدلاً من ذلك.
### **يحذف Shape.Sinted property**
استخدم خاصية Shape.IsPrintable بدلاً من ذلك.
### **يحذف طريقة PivotItem.Move القديمة**
استخدام طريقة PivotItem.Move (int ، bool) بدلاً من ذلك.
### **يحذف Cells.ExportDataTable (int، int، int، int، bool، bool)، Cells.ExportDataTable (int، int، int، int، object [])، Cells.ExportDataTable (int، int، int، int، bool) ، Cells.ExportDataTable (DataTable، int، int []، int، bool) و Cells.ExportDataTable (DataTable، int، int، int، bool، bool)**
استخدم طريقة ExportDataTable (firstRow و firstColumn و totalRows و totalColumns و ExportTableOptions) بدلاً من ذلك.
### **إضافة ExtPage.setServlet (طلب HttpServletRequest و HttpServletResponse Response)**
 يقوم بتهيئة سياق servlet لـ ExtPage.
### **يضيف طريقة ExtPage.getBean ()**
 الحصول على مثيل GridWebBean من ExtPage.
### **يحذف طريقة ExtPage.getBean (طلب HttpServletRequest)**
 استخدم ExtPage.getBean () بدلاً من ذلك.
### **يضيف خاصية ExtPage.Maxholders**
يشير إلى الحد الأقصى لمثيلات GridWeb التي يجب الاحتفاظ بها للخادم (يعتبر إنشاء كل صفحة جديدة أو التحديث بمثابة مثيل تحكم جديد) ، والقيمة الافتراضية هي 1000.
### **يضيف خاصية ExtPage.Memoryinstanceexpires**
 يشير إلى وقت انتهاء الصلاحية بالثواني لمثيل التحكم على الخادم ، إذا انتهى الوقت ، فسيتم إزالته على الخادم ، القيمة الافتراضية هي 3600 ، حوالي ساعة واحدة.
### **إضافة خاصية ExtPage.MemoryCleanRateTime**
 يشير إلى كل مدة زمنية بالثواني للقيام بعمل الفحص ، للتحقق مما إذا كان مثيل عنصر التحكم منتهي الصلاحية ، وإذا انتهت صلاحيته ، فإنه يزيله ، القيمة الافتراضية هي 7200 ، حوالي ساعتين.
