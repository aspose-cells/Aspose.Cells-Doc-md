---
title: Aspose.Cells لنظام Android عبر Java 19.4 ملاحظات الإصدار
type: docs
weight: 40
url: /ar/java/aspose-cells-for-android-via-java-19-4-release-notes/
---
{{% alert color="primary" %}} 

تحتوي هذه الصفحة على ملاحظات إصدار Aspose.Cells لنظام Android عبر Java 19.4.

{{% /alert %}} 

|**مفتاح**|**ملخص**|**فئة**|
|:- |:- |:- |
|CELLSJAVA-42838|تعطيل خاصية العرض التلقائي لجزء المهام.|ميزة جديدة|
|CELLSJAVA-42853|مشكلة في الأداء أثناء تحويل XLSX إلى HTML|التعزيز|
|CELLSANDROID-88|فقدت الصورة أثناء تحويل المصنف إلى PDF|حشرة|
|CELLSJAVA-42852|لا يتم عرض التسمية الموجودة على كلا المحورين|حشرة|
|CELLSJAVA-42856|Excel إلى مشكلة HTML|حشرة|
|CELLSJAVA-42872|صورة الورقة ، الأسطر اليمنى والسفلى مفقودة|حشرة|
|CELLSJAVA-42873|تحتوي الورقة المشروطة مسبقًا على العديد من خلفيات الخلايا والنصوص المفقودة وهي مخفية.|حشرة|
|CELLSJAVA-42874|فقدان العمود عند تصدير ملف إلى HTML|حشرة|
|CELLSJAVA-42875|العرض خاطئ والشاشة خارج الشكل|حشرة|
|CELLSJAVA-42878|نتيجة حساب الصيغ غير صحيحة|حشرة|
|CELLSJAVA-40419|لا يمكن إنشاء PDF بعلامات أثناء التصدير من Excel إلى PDF|حشرة|
|CELLSJAVA-40570|التحويل الخاطئ إلى PDF و JPG للصفحات ذات الأحجام المختلفة|حشرة|
|CELLSJAVA-42833|حدثت مشكلة أثناء تضمين ملف PDF نفسه في أوراق متعددة في مصنف|حشرة|
|CELLSJAVA-42858|مشكلة عند إضافة صورة إلى خلايا مدمجة باستخدام علامات ذكية مع صورة: خيار FitToCell|حشرة|
|CELLSJAVA-42862|تتم إعادة تسمية اسم الورقة في الصيغ بعد استيراد ملف CSV|حشرة|
|CELLSJAVA-42865|وقت غير صحيح للقراءة من خلية في ملف ODS|حشرة|
|CELLSJAVA-42879|تلف ملف Excel بعد الحفظ بواسطة Aspose.Cells|حشرة|
|CELLSJAVA-42860|java.lang.NullPointerException عند تحميل تنسيق ملف ODS|استثناء|
|CELLSJAVA-42871|java.lang.Exception: استنساخ غير مدعوم للدفق المدعوم أثناء تحويل XLSX إلى PDF|استثناء|
## **API العام والتغييرات غير المتوافقة مع الإصدارات السابقة**
فيما يلي قائمة بأية تغييرات تم إجراؤها على API العام مثل الأعضاء الذين تمت إضافتهم أو إعادة تسميتهم أو إزالة أو إهمالهم بالإضافة إلى أي تغيير غير متوافق مع الإصدارات السابقة تم إجراؤه على Aspose.Cells لنظام Android عبر Java. إذا كانت لديك مخاوف بشأن أي تغيير مدرج ، فيرجى ارفعه في منتدى الدعم Aspose.Cells.
### **يضيف واجهات برمجة التطبيقات لحفظ مستند Markdown: SaveFormat.Markdown ، FileFormatType.Markdown ، MarkdownSaveOptions**
يدعم حفظ محتوى الخلايا كجدول تخفيض السعر. باستخدام طريقة Workbook.Save () ، سيتم تصدير جميع محتويات الخلية في الورقة النشطة كجدول في مستند العلامات.
### **يزيل الخصائص القديمة لـ TxtLoadOptions**
الرجاء استخدام خاصية LoadStyleStrategy بدلاً من KeepExactFormat.
### **يزيل LoadDataOption فئة قديمة**
الرجاء استخدام فئة LoadFilter وخاصية LoadOptions.LoadFilter بدلاً من ذلك.
### **يزيل الخصائص القديمة لخيارات LoadOptions**
LoadOptions.ConvertNumericData: الرجاء استخدام هذه الخاصية مع الفئة الفرعية المقابلة من LoadOptions ، مثل TxtLoadOptions.
LoadOptions.LoadDataOptions: الرجاء استخدام خاصية LoadOptions.LoadFilter مع التنفيذ المخصص لـ LoadFilter.
LoadOptions.LoadDataFilterOptions: الرجاء استخدام LoadOptions.LoadFilter.LoadDataFilterOptions بدلاً من ذلك.
LoadOptions.OnlyLoadDocumentProperties: الرجاء استخدام LoadOptions.LoadFilter.LoadDataFilterOptions = LoadDataFilterOptions.DocumentProperties.
LoadOptions.LoadDataAndFormatting / LoadDataOnly: الرجاء استخدام LoadOptions.LoadFilter.LoadDataFilterOptions = LoadDataFilterOptions.CellData | LoadDataFilterOptions.DefinedNames.
### **يضيف خاصية PdfSaveOptions.ExportDocumentStructure**
الحصول على أو تحديد قيمة تحدد ما إذا كان سيتم تصدير بنية المستند أم لا.
### **إضافة فئات من مساحة الاسم Aspose.Cells.WebExtensions**
يمثل WebExtensions و WebExtensionTasks
### **إضافة خصائص WorksheetCollection.WebExtensions و WorksheetCollection.WebExtensionTaskPanes.**
يمثل جميع WebExtensions و WebExtensionTasks.
### **يضيف فئة WebExtensionShape**
يمثل شكل WebExtension.
### **يضيف Cells.InsertCutCells () طريقة.**
إدراج قطع الخلايا.
### **يضيف Cells.SetViewColumnWidthPixel.**
يضبط عرض عرض العمود.
### **يضيف فئات ThreadedCommentCollection و ThreadedComment.**
يمثل التعليق المترابط.
### **يضيف الخاصية WorksheetCollection.ThreadedCommentAuthors.**
يحصل على وتعيين مؤلفي التعليقات المترابطة.
### **يضيف تعليقًا.**
يمثل التعليقات المترابطة على التعليق.
### **أضف أساليب CommentCollection.AddThreadedComment () و CommentCollection.GetThreadedComments ().**
يضيف ويحصل على التعليقات المترابطة.
### **إضافة خاصية العنوان الفرعي.**
الحصول على العنوان الفرعي للرسم البياني. فقط لملف تنسيق ODS.
