---
title: Aspose.Cells for .NET 17.12 ملاحظات الإصدار
type: docs
weight: 10
url: /ar/net/aspose-cells-for-net-17-12-release-notes/
---
{{% alert color="primary" %}} 

تحتوي هذه الصفحة على ملاحظات إصدار for .NET Aspose.Cells 17.12.

{{% /alert %}} 

|**مفتاح**|**ملخص**|**فئة**|
|:- |:- |:- |
|CELLSNET-45358|احصل على CSS بشكل منفصل عن ترميز HTML عند التصدير إلى HTML باستخدام التدفقات|ميزة جديدة|
|CELLSNET-45697|نفذ Cell.FormulaLocal مثل Microsoft Interop FormulaLocal|ميزة جديدة|
|CELLSNET-45801|دعم وظائف Office الإضافية في Excel لعرض PDF|ميزة جديدة|
|CELLSNET-45796|العلامات الذكية - كيفية تعبئة البيانات تلقائيًا في ورقة العمل الثانية إذا كانت البيانات كبيرة جدًا ولا يمكن إدراجها في ورقة واحدة|ميزة جديدة|
|CELLSNET-45791|قم بتحديث "الاحتفاظ بمحفوظات التغيير" عند مشاركة المصنف|ميزة جديدة|
|CELLSNET-45746|يتداخل النص في الخلايا مع خلايا أخرى في Aspose.Cells.GridDesktop|ميزة جديدة|
|CELLSNET-45774|يتم الخلط بين الصور في شكل صورة مع تعبئة نسيج|التعزيز|
|CELLSNET-45731|تحديث PivotTable يفسد ملف MS Excel|خلل برمجي|
|CELLSNET-45794|يتم حساب صيغة المصفوفة التي تتضمن "MEDIAN" على أنها فارغة|خلل برمجي|
|CELLSNET-45779|Cell تم تغيير محاذاة النص في الصورة المحولة|خلل برمجي|
|CELLSNET-45772|فقدت صفحة واحدة عند تحويل ورقة العمل إلى صورة|خلل برمجي|
|CELLSNET-45764|حالة DataBars غير صحيحة في الإخراج PDF|خلل برمجي|
|CELLSNET-45785|وضع سلسلة "Nominale in Essere (mln)" تصنيفات البيانات غير صحيح|خلل برمجي|
|CELLSNET-45775|تسمية المحور العمودي الثانية مفقودة عند تحويل الرسم البياني إلى صورة|خلل برمجي|
|CELLSNET-45762|Chart.Calculate يستغرق المزيد من الوقت ولا يعمل|خلل برمجي|
|CELLSNET-45799|يتغير المسار المطلق إلى المسار النسبي عند إعادة حفظ ملف XLSX|خلل برمجي|
|CELLSNET-45797|SetArrayFormula - لا تتم معاملته كصيغة صفيف|خلل برمجي|
|CELLSNET-45792|فقدت الخلايا المدمجة عند النسخ ، والصق العمود في الأعمدة التالية|خلل برمجي|
|CELLSNET-45784|يؤدي إدراج عمود إلى مطالبة MS Excel برسالة خطأ|خلل برمجي|
|CELLSNET-45778|تم تغيير إعدادات التعليق عند فتح ملف MS Excel وحفظه|خلل برمجي|
|CELLSNET-45773|يتم تغيير تنسيق التعبئة لجميع أشكال النص في المصنف بدلاً من الشكل المحدد|خلل برمجي|
|CELLSNET-45770|ملف Xlsx تالف بعد التحميل والحفظ|خلل برمجي|
|CELLSNET-45769|القيمة الافتراضية للخاصية OoxmlSaveOptions.ExportCellName صحيحة بدلاً من false|خلل برمجي|
|CELLSNET-45768|Workbook.Save (دفق الدفق ، SaveFormat saveFormat) يفشل إذا كان الدفق لا يدعم Seek|خلل برمجي|
|CELLSNET-45780|مشكلة في عرض بيانات ورقة العمل من اليمين إلى اليسار|خلل برمجي|
|CELLSNET-45745|خطأ عند النقر فوق شريط التمرير في Aspose.Cells.GridDesktop|خلل برمجي|
|CELLSNET-45777|يحدث خطأ من شكل إلى صورة أثناء تحويل ملف Excel إلى PDF|استثناء|
|CELLSNET-45804|استثناء عند فتح ملف Excel (Strict Open XML Spreadsheet)|استثناء|
|CELLSNET-45798|كان الفهرس خارج حدود المصفوفة - استثناء أثناء عرض ملف Excel|استثناء|
|CELLSNET-45795|يجب إدخال بيانات لمعايير التحقق من الصحة - يحدث استثناء أثناء حفظ المصنف|استثناء|
|CELLSNET-45781|يحدث ArgumentOutOfRangeException عندما يتم نسخ ورقة العمل إلى مصنف آخر|استثناء|
### **API العام والتغييرات غير المتوافقة مع الإصدارات السابقة**
فيما يلي قائمة بأي تغييرات تم إجراؤها على API العام مثل الأعضاء المضافين أو المعاد تسميتهم أو المحذوفون أو المهملون بالإضافة إلى أي تغيير غير متوافق مع الإصدارات السابقة تم إجراؤه على Aspose.Cells for .NET. إذا كانت لديك مخاوف بشأن أي تغيير مدرج ، فيرجى رفعه في منتدى الدعم Aspose.Cells.
#### **يضيف خاصية HtmlSaveOptions.TableCssId**
الحصول على وتعيين بادئة اسم النوع css مثل tr ، col ، td وما إلى ذلك ، يتم تضمينها في عنصر الجدول الذي يحتوي على سمة TableCssId المحددة. النظام الأساسي "".
#### **يضيف Cell.FormulaLocal الملكية**
الحصول على الصيغة المنسقة محليًا والتي قد تختلف وفقًا لإعدادات الإعدادات المحلية المختلفة للفواصل ، والأسماء المضمنة ، وأسماء الوظائف ، ... إلخ. هذه المناطق تعتمد.
#### **يضيف طريقة GlobalizationSettings.GetLocalFunctionName (سلسلة معيارية)**
الحصول على اسم الوظيفة التابع للإعدادات المحلية وفقًا لاسم الوظيفة القياسي المحدد.
#### **يضيف أسلوب GlobalizationSettings.GetLocalBuiltInName (سلسلة standardName)**
الحصول على النص المعتمد على الإعدادات المحلية للاسم المضمن وفقًا للنص القياسي المحدد.
#### **يضيف خاصية GlobalizationSettings.ListSeparator**
الحصول على فاصل القائمة ، معاملات الوظيفة ، ... إلخ.
#### **يضيف خاصية GlobalizationSettings.RowSeparatorOfFormulaArray**
يحصل على فاصل الصفوف في بيانات الصفيف في الصيغة.
#### **يضيف خاصية GlobalizationSettings.ColumnSeparatorOfFormulaArray**
الحصول على فاصل العناصر الموجودة في بيانات صف الصفيف في الصيغة.
#### **إضافة خاصية HtmlSaveOptions.ExportWorksheetCSSS بشكل منفصل**
يشير إلى ما إذا كان سيتم تصدير css ورقة العمل بشكل منفصل. القيمة الافتراضية هي كاذبة.
#### **يضيف LoadDataFilterOptions.Structure لاستبدال LoadDataFilterOptions.None**
LoadDataFilterOptions.None أعطى اتجاهات غامضة وتسبب في حدوث ارتباك. تم تصميمه للإشارة إلى عدم تحميل أي شيء لبيانات ورقة العمل. الآن نقدم واحدًا جديدًا (عضوًا) ، أي هيكل ليحل محله.
#### **يضيف تعداد DataLabelShapeType**
يحدد الشكل الهندسي المعين مسبقًا والذي سيتم استخدامه للمخطط.
#### **يضيف خاصية DataLabels.ShapeType**
الحصول على نوع شكل تسمية البيانات أو تعيينه.
#### **يحذف بعض FileFormatType المتقادم**
يحذف أنواع تنسيقات الملفات القديمة.
#### **تمت إضافة خاصية WorksheetCollection.RevisionLogs وفئة RevisionLogCollection وفئة Revisions.RevisionLog**
يحصل على إعداد سجل المراجعة.
#### **يضيف التعداد MsoDrawingType.WebExtension**
يمثل شكل امتداد الويب.


#### **أمثلة على الاستخدام**
يرجى التحقق من قائمة مواضيع المساعدة المضافة في Aspose.Cells مستندات Wiki:

- [الملء التلقائي لبيانات العلامات الذكية في أوراق عمل أخرى إذا كانت البيانات كبيرة جدًا](/cells/ar/net/auto-populate-smart-marker-data-to-other-worksheets-if-data-is-too-large/)
- [تصدير ورقة العمل CSS بشكل منفصل في الإخراج HTML](/cells/ar/net/export-worksheet-css-separately-in-output/)
- [نفذ Cell.FormulaLocal مماثل لنطاق Excel VBA](/cells/ar/net/implement-cell-formulalocal-similar-to-excel-vba-range-formulalocal/)
- [أنماط عناصر الجدول البادئة مع الخاصية HtmlSaveOptions.TableCssId](/cells/ar/net/prefix-table-elements-styles-with-htmlsaveoptions-tablecssid-property/)
- [عرض وظائف Office الإضافية أثناء تحويل Excel إلى Pdf](/cells/ar/net/render-office-add-ins-while-converting-excel-to-pdf/)
- [قم بتعيين نوع شكل تسميات البيانات للمخطط](/cells/ar/net/set-the-shape-type-of-data-labels-of-chart/)
- [يتجاوز النص من خلية GridDesktop إذا كانت طويلة جدًا](/cells/ar/net/text-overflows-from-griddesktop-cell-if-it-is-too-long/)
- [تحديث الأيام مع الاحتفاظ بمحفوظات المراجعة في المصنف المشترك](/cells/ar/net/update-days-preserving-history-of-revision-logs-in-shared-workbook/)
