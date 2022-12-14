---
title: Aspose.Cells for .NET 8.1.2 ملاحظات الإصدار
type: docs
weight: 50
url: /ar/net/aspose-cells-for-net-8-1-2-release-notes/
---
{{% alert color="primary" %}} 

 تحتوي هذه الصفحة على ملاحظات الإصدار لـ[Aspose.Cells for .NET 8.1.2](https://downloads.aspose.com/cells/net/new-releases/aspose.cells-for-.net-8.1.2/)

{{% /alert %}} 

تم تحديث Aspose.Cells for .NET إلى الإصدار 8.1.2 ويسعدنا أن نعلن أن هذا الإصدار يجلب إضافة أكثر من 20 تحسينًا مفيدًا جديدًا.
باستخدام Aspose.Cells for .NET يمكنك العمل مع XLS و SpreadsheetML و OOXML و XLSB و CSV و HTML و ODS و PDF و XPS وغيرها من التنسيقات في تطبيقاتك. يمكنك أيضًا عرض وإنشاء وتعديل وتحويل وعرض وطباعة المصنفات كلها بدون استخدام Microsoft Excel.
قم بزيارة الوثائق لمعرفة كيفية البدء مع Aspose.Cells for .NET.
لاحظ أن هذا التنزيل يحتوي على إصدار كامل من المنتج ، ولكن بدون تعيين ترخيص ، سيتم تشغيله في وضع التقييم مع بعض القيود. لاختبار Aspose.Cells بدون قيود التقييم هذه ، يمكنك طلب ترخيص مؤقت مجاني لمدة 30 يومًا.
 فيما يلي قائمة بالتغييرات في هذا الإصدار من Aspose.Cells.

\1) Aspose.Cells 
## **تحسينات وتغييرات أخرى**

## **أداء**


 (CELLSNET-42820) - FileFormatUtil.DetectFileFormat يستخدم كل الذاكرة المتوفرة للنظام أثناء اكتشاف جدول بيانات تالف


## **البق**


 (CELLSNET-42801) - البيانات مفقودة عند تحويل PivotTable إلى PDF

 (CELLSNET-42800) - يكون العنوان الإجمالي مفقودًا عند تحويل PivotTable إلى PDF

(CELLSNET-42799) - Cell دمج المشكلة عند تحويل PivotTable إلى PDF

 (CELLSNET-42775) - خطأ PivotTable بخصوص المجاميع الفرعية

 (CELLSNET-42749) - خطوط الأسهم سميكة جدًا مما في Excel

 (CELLSNET-42438) - يختفي محتوى الخلية المدمجة عند تصفية الصفوف وتحويل جدول البيانات إلى HTML

 (CELLSNET-42353) - Aspose.Cells ينتج سمكًا مزدوجًا للسهم أثناء تحويل XLS إلى PDF

 (CELLSNET-42747) - لا يتم توسيط النتيجة المطبوعة بشكل صحيح ويتم فقد السطر الأخير

 (CELLSNET-42744) - لا يظهر النص الموجود في الخلايا المدمجة عند التحويل إلى PDF

 (CELLSNET-42781) - خطأ في الشكل إلى صورة أثناء تحويل ExcelShapeToImageRedactedEx.xls إلى Tiff

 (CELLSNET-42780) - خطأ في الشكل إلى صورة أثناء تحويل ExcelShapeToImageError.xls إلى Tiff

 (CELLSNET-42760) - الخط سميك جدًا عند حفظه بتنسيق pdf باستخدام خلايا Aspose

 (CELLSNET-42622) - تتداخل تسميات مخططات Excel بعد فتح ملف xlsm وحفظه

(CELLSNET-42836) - لم يتم حساب صيغة المطابقة بشكل صحيح مع Workbook.

 (CELLSNET-42818) - #NUM! خطأ عند قراءة خلايا معينة

 (CELLSNET-42811) - العلامات الذكية - Cells التنسيق لم يتم الاحتفاظ به في المجموعة: دمج ، تخطي: 1


## **استثناءات**


 (CELLSNET-42635) - يتسبب MonoDevelop في حدوث خطأ SIGSEGV

 (CELLSNET-42812) - CellsException أثناء تحويل جدول البيانات إلى PDF

 (CELLSNET-42788) - System.NullReferenceException عند حفظ ملف ods


## **API العام والتغييرات غير المتوافقة مع الإصدارات السابقة**


 فيما يلي قائمة بأي تغييرات تم إجراؤها على API العام مثل الأعضاء المضافين أو المعاد تسميتهم أو المحذوفون أو المهملون بالإضافة إلى أي تغيير غير متوافق مع الإصدارات السابقة تم إجراؤه على Aspose.Cells for .NET. إذا كانت لديك مخاوف بشأن أي تغيير مدرج ، فيرجى رفعه في منتدى الدعم Aspose.Cells.



 تحذير عام ، فئات WarningType ، واجهة IWarningCallback و SaveOptions.WarningCallback ، خاصية ImageOrPrintOptions.WarningCallback.

 يدعم التحذيرات عند استبدال الخط.



 حذف خاصية PdfSaveOptions.ChartImageType القديمة.


