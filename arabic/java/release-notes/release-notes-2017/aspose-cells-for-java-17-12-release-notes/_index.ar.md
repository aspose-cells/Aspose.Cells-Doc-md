---
title: Aspose.Cells for Java 17.12 ملاحظات الإصدار
type: docs
weight: 10
url: /ar/java/aspose-cells-for-java-17-12-release-notes/
---
{{% alert color="primary" %}} 

تحتوي هذه الصفحة على ملاحظات إصدار for Java Aspose.Cells 17.12.

{{% /alert %}} 

|**مفتاح**|**ملخص**|**فئة**|
|:- |:- |:- |
|CELLSJAVA-42479|تمت إزالة الغموض والتعداد LoadDataFilterOptions المحسن|التعزيز|
|CELLSJAVA-42460|تنسيق CSV - D2 و D6 هما IsString ولكن Aspose.Cells يعاملانهما على أنهما IsNumeric|التعزيز|
|CELLSJAVA-42457|عندما يتم تحويل XLSX إلى PDF ، فإن بعض الخطوط في المخططات تكون مختلفة|خلل برمجي|
|CELLSJAVA-42465|بعض إعلانات فئة CSS غير مسبوقة في الإخراج HTML|خلل برمجي|
|CELLSJAVA-42456|إخراج HTML غير متوافق مع المصدر - تحويل Excel إلى HTML|خلل برمجي|
|CELLSJAVA-42478|يؤدي استيراد قيمة طويلة من HSQL DB إلى استثناء|خلل برمجي|
|CELLSJAVA-42466|لا يتم تقديم المعادلة بشكل جيد في الإخراج PDF|خلل برمجي|
|CELLSJAVA-42475|المخطط مفقود في الإخراج PDF|خلل برمجي|
|CELLSJAVA-42459|عناوين البيانات للرسم البياني مفقودة في الإخراج PDF / صورة|خلل برمجي|
|CELLSJAVA-42453|صورة المخطط ليست متشابهة Microsoft Excel|خلل برمجي|
|CELLSJAVA-42447|يتم عرض علامات البيانات بشكل خاطئ في تنسيق ملف الإخراج HTML|خلل برمجي|
|CELLSJAVA-42481|تعيين اسم مربع التحرير والسرد لا يعمل لملف Excel المصدر ولكن إذا تم إعادة حفظه بواسطة Microsoft Excel ، فإنه يعمل بشكل جيد|خلل برمجي|
|CELLSJAVA-42476|Microsoft تلف ورقة عمل Excel ذات التمكين الكلي (.xlsm) بعد فتحها وحفظها عبر واجهات برمجة تطبيقات Aspose.Cells|خلل برمجي|
|CELLSJAVA-42470|يؤدي تعيين خلية مرتبطة بـ Checkbox إلى مطالبة MS Excel برسالة خطأ عند فتح ملف الإخراج فيه|خلل برمجي|
|CELLSJAVA-42462|تؤدي قراءة الملف XLSB إلى ظهور NullPointerException|استثناء|
## **API العام والتغييرات غير المتوافقة مع الإصدارات السابقة**
فيما يلي قائمة بأي تغييرات تم إجراؤها على API العام مثل الأعضاء المضافين أو المعاد تسميتهم أو المحذوفون أو المهملون بالإضافة إلى أي تغيير غير متوافق مع الإصدارات السابقة تم إجراؤه على Aspose.Cells for Java. إذا كانت لديك مخاوف بشأن أي تغيير مدرج ، فيرجى رفعه في منتدى الدعم Aspose.Cells.
### **يضيف خاصية HtmlSaveOptions.TableCssId**
الحصول على وتعيين بادئة اسم النوع css مثل tr ، col ، td وما إلى ذلك ، يتم تضمينها في عنصر الجدول الذي يحتوي على سمة TableCssId المحددة. النظام الأساسي "".
### **يضيف Cell.FormulaLocal الملكية**
الحصول على الصيغة المنسقة محليًا والتي قد تختلف وفقًا لإعدادات الإعدادات المحلية المختلفة للفواصل ، والأسماء المضمنة ، وأسماء الوظائف ، ... إلخ. هذه المناطق تعتمد.
### **يضيف طريقة GlobalizationSettings.GetLocalFunctionName (سلسلة معيارية)**
الحصول على اسم الوظيفة التابع للإعدادات المحلية وفقًا لاسم الوظيفة القياسي المحدد.
### **يضيف أسلوب GlobalizationSettings.GetLocalBuiltInName (سلسلة standardName)**
الحصول على النص المعتمد على الإعدادات المحلية للاسم المضمن وفقًا للنص القياسي المحدد.
### **يضيف خاصية GlobalizationSettings.ListSeparator**
الحصول على فاصل القائمة ، معاملات الوظيفة ، ... إلخ.
### **يضيف خاصية GlobalizationSettings.RowSeparatorOfFormulaArray**
يحصل على فاصل الصفوف في بيانات الصفيف في الصيغة.
### **يضيف خاصية GlobalizationSettings.ColumnSeparatorOfFormulaArray**
الحصول على فاصل العناصر الموجودة في بيانات صف الصفيف في الصيغة.
### **إضافة خاصية HtmlSaveOptions.ExportWorksheetCSSS بشكل منفصل**
يشير إلى ما إذا كان سيتم تصدير css ورقة العمل بشكل منفصل. القيمة الافتراضية هي كاذبة.
### **يضيف LoadDataFilterOptions.Structure لاستبدال LoadDataFilterOptions.None**
LoadDataFilterOptions.None أعطى اتجاهات غامضة وتسبب في حدوث ارتباك. تم تصميمه للإشارة إلى عدم تحميل أي شيء لبيانات ورقة العمل. الآن نقدم واحدًا جديدًا (عضوًا) ، أي هيكل ليحل محله.
### **يضيف تعداد DataLabelShapeType**
يحدد الشكل الهندسي المعين مسبقًا والذي سيتم استخدامه للمخطط.
### **يضيف خاصية DataLabels.ShapeType**
الحصول على نوع شكل تسمية البيانات أو تعيينه.
### **يحذف بعض FileFormatType المتقادم**
يحذف أنواع تنسيقات الملفات القديمة.
### **تمت إضافة خاصية WorksheetCollection.RevisionLogs وفئة RevisionLogCollection وفئة Revisions.RevisionLog**
يحصل على إعداد سجل المراجعة.
### **يضيف التعداد MsoDrawingType.WebExtension**
يمثل شكل امتداد الويب.


### **أمثلة على الاستخدام**
يرجى التحقق من قائمة مواضيع المساعدة المضافة في Aspose.Cells مستندات Wiki:

- [الملء التلقائي لبيانات العلامات الذكية في أوراق عمل أخرى إذا كانت البيانات كبيرة جدًا](/cells/ar/java/auto-populate-smart-marker-data-to-other-worksheets-if-data-is-too-large/)
- [تصدير ورقة العمل CSS بشكل منفصل في الإخراج HTML](/cells/ar/java/export-worksheet-css-separately-in-output-html/)
- [نفذ Cell.FormulaLocal مماثل لنطاق Excel VBA](/cells/ar/java/implement-cell-formulalocal-similar-to-excel-vba-range-formulalocal/)
- [أنماط عناصر الجدول البادئة مع الخاصية HtmlSaveOptions.TableCssId](/cells/ar/java/prefix-table-elements-styles-with-htmlsaveoptions-tablecssid-property/)
- [عرض وظائف Office الإضافية أثناء تحويل Excel إلى Pdf](/cells/ar/java/render-office-add-ins-while-converting-excel-to-pdf/)
- [قم بتعيين نوع شكل تسميات البيانات للمخطط](/cells/ar/java/set-the-shape-type-of-data-labels-of-chart/)
- [تحديث الأيام مع الاحتفاظ بمحفوظات المراجعة في المصنف المشترك](/cells/ar/java/update-days-preserving-history-of-revision-logs-in-shared-workbook/)
