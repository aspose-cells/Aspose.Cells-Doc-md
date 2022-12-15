---
title: Aspose.Cells for .NET 18.12 ملاحظات الإصدار
type: docs
weight: 10
url: /ar/net/aspose-cells-for-net-18-12-release-notes/
---
{{% alert color="primary" %}} 

 تحتوي هذه الصفحة على ملاحظات الإصدار لـ[Aspose.Cells for .NET 18.12](https://www.nuget.org/packages/Aspose.Cells/18.12.0).

{{% /alert %}} 

|**مفتاح**|**ملخص**|**فئة**|
|:- |:- |:- |
|CELLSNET-46479|لا يتوفر اسم علامة التبويب عند تحويل مصنف الورقة المفردة إلى HTML|ميزة جديدة|
|CELLSNET-46503|التحكم في تحميل بيانات VBA باستخدام LoadDataFilterOptions|ميزة جديدة|
|CELLSNET-42414|فقدت التغييرات المتعقبة أثناء التحويل من XLSB إلى XLSM و XLS إلى XLSM|التعزيز|
|CELLSNET-46090|تحرك النص قليلاً بعد فك تجميع الشكل عند حفظ XLS إلى XLSX|التعزيز|
|CELLSNET-46439|تحسين أداء الذاكرة: حرر الدفق الأصلي بعد تحميل المصنف|أداء|
|CELLSNET-46371|لا يتم عرض خطوط الشبكة في بعض الأوراق أثناء تحويل XLSX-> HTML-> XLSX|حشرة|
|CELLSNET-46447|تنسيقات مفقودة في عرض HTML إلى XLS|حشرة|
|CELLSNET-46494|تحويل MHT إلى XLSX - مشكلة محتوى الخلية|حشرة|
|CELLSNET-46468|يطالب MS Excel بخطأ عند فتح ملف الإخراج|حشرة|
|CELLSNET-46487|صيغة اللغة غير الإنجليزية لا تعمل|حشرة|
|CELLSNET-46489|يؤدي حذف صف به فهرس وقراءة الصف الذي له نفس الفهرس إلى إرجاع Cell.ValuType: IsNull|حشرة|
|CELLSNET-46406|تعذر فتح مستند ODS المحمي بكلمة مرور|حشرة|
|CELLSNET-46466|النص السفلي الموجود أسفل الرمز الشريطي مفقود في عرض MS Excel إلى PDF|حشرة|
|CELLSNET-46470|الصورة مفقودة بعد نقلها إلى إخراج TIFF|حشرة|
|CELLSNET-46499|لا يتم عرض الصور بشكل صحيح عند تحويلها من Excel إلى PDF|حشرة|
|CELLSNET-46443|ظهر نص إضافي في الصورة المقدمة من مخطط MS Excel|حشرة|
|CELLSNET-46450|تحتوي الصورة المعروضة من مخطط MS Excel على وحدات محور أكثر من المخطط الأصلي|حشرة|
|CELLSNET-46451|مشكلة عند تقديم ملف القالب (الذي يحتوي على الرسم البياني) إلى تنسيق ملف PDF|حشرة|
|CELLSNET-46454|تم عرض ترتيب وسيلة الإيضاح بشكل مختلف عن مخطط Excel في الجلسة 0 مقابل الجلسة 1|حشرة|
|CELLSNET-46471|لا يمكن تعيين علامة اللون LineWithDataMarkers في تنسيق ملف XLS|حشرة|
|CELLSNET-42729|يتم إزاحة النص عندما يتم تقديم مخططات SmartArt كتنسيق ملف HTML|حشرة|
|CELLSNET-46462|يتكرر النص أثناء استبدال العلامة بالنص|حشرة|
|CELLSNET-46483|خطأ بعد تحويل المستند باستخدام Custom UI xml من XLSB إلى XLSM|حشرة|
|CELLSNET-46495|تم العثور على مشاكل أثناء تحويل الرسم البياني إلى صورة|حشرة|
|CELLSNET-46486|تم رفع الاستثناء أثناء تحويل XLS إلى PDF|استثناء|
|CELLSNET-46472|يثير PivotTable.GetChildren () استثناء "اسم غير صالح Cell"|استثناء|
|CELLSNET-46452|استثناء "NullReferenceException" عند تحميل تنسيق ملف XLSB|استثناء|
|CELLSNET-46456|ArgumentException عند تحميل المصنف|استثناء|
|CELLSNET-46460|استثناء أثناء الوصول إلى TextBox.HtmlText من XLS|استثناء|
### **API العام والتغييرات غير المتوافقة مع الإصدارات السابقة**
فيما يلي قائمة بأي تغييرات تم إجراؤها على API العام مثل الأعضاء المضافين أو المعاد تسميتهم أو المحذوفون أو المهملون بالإضافة إلى أي تغيير غير متوافق مع الإصدارات السابقة تم إجراؤه على Aspose.Cells for Java. إذا كانت لديك مخاوف بشأن أي تغيير مدرج ، فيرجى رفعه في منتدى الدعم Aspose.Cells.
#### **يضيف خاصية HtmlSaveOptions.ExportSingleTab**
يشير إلى ما إذا كان تصدير علامة التبويب المفردة عندما يحتوي الملف على ورقة عمل واحدة فقط. القيمة الافتراضية هي false.
#### **يضيف خاصية HtmlSaveOptions.ExportPrintAreaOnly**
يشير إلى ما إذا كان يتم تصدير منطقة الطباعة فقط إلى ملف html. القيمة الافتراضية هي كاذبة.
#### **يحذف طريقة Workbook.Initialize () التي عفا عليها الزمن**
استخدم مُنشئ المصنف بدلاً من ذلك.
#### **حذف خاصية Workbook.Styles التي عفا عليها الزمن**
استخدم Workbook.CreateStyle () لإنشاء نمط المصنف ومعالجته بدلاً من StyleCollection.Add () ؛ استخدم Workbook.GetNamedStyle (سلسلة) للحصول على نمط مسمى بدلاً من StyleCollection.
#### **يحذف Workbook.CheckWriteProtectedPassword () طريقة قديمة**
استخدم طريقة WorkbookSettings.WriteProtection.ValidatePassword بدلاً من ذلك.
#### **يضيف LoadDataFilterOptions.VBA enum**
الخيار المستخدم لتجاهل مشاريع VBA أثناء تحميل ملف القالب.
#### **يضيف خاصية Style.InvariantCustom**
الحصول على سلسلة نمط الثقافة المستقلة لتنسيق الأرقام (بما في ذلك سلسلة النمط للرقم المضمن).
#### **يضيف خاصية FindOptions.ValueTypeSensitive**
يشير إلى ما إذا كان يجب أن يكون نوع قيمة الخلية التي تم البحث عنها هو نفسه مع المفتاح الذي تم البحث عنه.
#### **تقادم FindOptions.SearchNext الخاصية**
استخدم خاصية FindOptions.SearchBackward بدلاً من ذلك ، القيمة الحقيقية لهذه الخاصية الجديدة تقابل خطأ SearchNext.
#### **حذف طرق البحث Cells.FindString و FindStringStartsWith و FindStringEndsWith و FindStringContains و FindNumber القديمة**
استخدم Cells. أوجد طريقة (كائن ، Cell ، FindOptions) بدلاً من ذلك. للحصول على نفس النتائج باستخدام الطرق FindNumber و FindString ، يرجى تعيين FindOptions.ValueTypeSensitive على أنه صحيح.
#### **يحذف الطريقة القديمة Cells.ImportGridView (System.Web.UI.WebControls.GridView، int، int، bool، bool، bool)**
استخدم طريقة Cells.ImportGridView (System.Web.UI.WebControls.GridView GridView ، int firstRow ، int firstColumn ، ImportTableOptions options). في حين أن.
#### **يحذف Cells المتقادم. خاصية البدء**
استخدم Cells.FirstCell بدلاً من ذلك.
#### **يحذف خاصية النهاية Cells.End المتقادمة**
استخدم Cells.LastCell بدلاً من ذلك.
#### **يحذف Cells خاصية [int]**
استخدم طريقة Cells.GetEnumerator () لتكرار كل الخلايا في ورقة العمل هذه بدلاً من ذلك.
#### **يحذف طرق Cells**
استخدم طريقة Cells.ImportData (DataTable ، int ، int ، ImportTableOptions) بدلاً من ذلك.
#### **يحذف طرق Cells**
استخدم طريقة Cells.ImportData (IDataReader، int، int، ImportTableOptions) بدلاً من ذلك.
#### **يحذف خاصية دوران الشكل التي عفا عليها الزمن**
استخدم خاصية Shape.RotationAngle بدلاً من ذلك.
#### **يحذف خاصية Validation.AreaList القديمة**
استخدم Validation.Areas property بدلاً من ذلك.
#### **حذف مُنشئ النمط المتقادم**
استخدم طريقة CellsFactory.CreateStyle () أو Workbook.CreateStyle () بدلاً من ذلك.
#### **يحذف Shape.Sinted property**
استخدم خاصية Shape.IsPrintable بدلاً من ذلك.
#### **يحذف طريقة PivotItem.Move القديمة**
استخدام طريقة PivotItem.Move (int ، bool) بدلاً من ذلك.
#### **يحذف Cells.ExportDataTable (int، int، int، int، bool، bool)، Cells.ExportDataTable (int، int، int، int، object [])، Cells.ExportDataTable (int، int، int، int، bool) ، Cells.ExportDataTable (DataTable، int، int []، int، bool) و Cells.ExportDataTable (DataTable، int، int، int، bool، bool)**
استخدم طريقة ExportDataTable (firstRow و firstColumn و totalRows و totalColumns و ExportTableOptions) بدلاً من ذلك.
